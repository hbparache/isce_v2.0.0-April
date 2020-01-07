#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2014 to the present, california institute of technology.
# all rights reserved. united states government sponsorship acknowledged.
# any commercial use must be negotiated with the office of technology transfer
# at the california institute of technology.
# 
# this software may be subject to u.s. export control laws. by accepting this
# software, the user agrees to comply with all applicable u.s. export laws and
# regulations. user has the responsibility to obtain export licenses,  or other
# export authority as may be required before exporting such information to
# foreign countries or providing access to foreign persons.
# 
# installation and use of this software is restricted by a license agreement
# between the licensee and the california institute of technology. it is the
# user's responsibility to abide by the terms of the license agreement.
#
# Author: Kosal Khun
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Comment: Adapted from InsarProc/runRgoffset_nstage.py
import logging
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj import Constants as CN
from mroipac.ampcor.Ampcor import Ampcor

logger = logging.getLogger('isce.isceProc.runRgoffset')

def runRgoffset(self, nstages=4, scale=2):
    infos = {}
    for attribute in ['firstSampleAcross', 'firstSampleDown', 'numberLocationAcross', 'numberLocationDown']:
        infos[attribute] = getattr(self._isce, attribute)
    for attribute in ['sensorName', 'offsetSearchWindowSize']:
        infos[attribute] = getattr(self, attribute)

    stdWriter = self._stdWriter

    refPol = self._isce.refPol
    refScene = self._isce.refScene

    imageSim = self._isce.simAmpImage
    sceneid1, sceneid2 = self._isce.pairsToCoreg[0]
    if sceneid1 != refScene:
        sys.exit("runRgoffset: should have refScene here!")
        #refScene should always be the first scene in each pair of pairsToCoreg (reference strategy)

    pairRef = None #pair with refScene in it
    for pair in self._isce.selectedPairs:
        if refScene == pair[0]:
            # refScene is first scene of pair (=> band 0 of imageAmp)
            bandRef = 0
            pairRef = pair
            break
        if refScene == pair[1]:
            # refScene is second scene of pair (=> band 1 of imageAmp)
            bandRef = 1
            pairRef = pair
    if pairRef is None:
        sys.exit("runRgoffset: refScene not in any selected pairs!")
        # can happen if refScene was used to coregister only but no pair was formed with it

    imageAmp = self._isce.resampAmpImages[pairRef][refPol]

    sid = self._isce.formatname(refScene)
    infos['outputPath'] = self.getoutputdir(refScene)
    catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
    offsetField = run(imageAmp, imageSim, bandRef, nstages, scale, infos, stdWriter, catalog=catalog, sceneid=sid)
    self._isce.procDoc.addAllFromCatalog(catalog)
    # assign the same offsetField to all pairs in pairsToCoreg (will be used by runOffoutliers)
    for pair in self._isce.pairsToCoreg:
        self._isce.offsetFields[pair] = offsetField
        self._isce.refinedOffsetFields[pair] = offsetField


def run(imageAmp, imageSim, numBand, infos, nstages, scale, stdWriter, catalog=None, sceneid='NO_ID'):
    logger.info("Running Rgoffset: %s" % sceneid)

    coarseAcross = 0
    coarseDown = 0
    firstAc =  infos['firstSampleAcross']
    firstDown =  infos['firstSampleDown']
    numLocationAcross =  infos['numberLocationAcross']
    numLocationDown =  infos['numberLocationDown']

    slaveWidth = imageAmp.getWidth()
    slaveLength = imageAmp.getLength()
    objAmp = isceobj.createSlcImage()
    objAmp.dataType = 'CFLOAT'
    objAmp.bands = 1
    objAmp.setFilename(imageAmp.getFilename())
    objAmp.setAccessMode('read')
    objAmp.setWidth(slaveWidth)
    objAmp.createImage()

    masterWidth = imageSim.getWidth()
    objSim = isceobj.createImage()
    objSim.setFilename(imageSim.getFilename())
    objSim.dataType = 'FLOAT'
    objSim.setWidth(masterWidth)
    objSim.setAccessMode('read')
    objSim.createImage()
    masterLength = imageSim.getLength()

    finalIteration = False
    for iterNum in xrange(nstages-1,-1,-1):
        ####Rewind the images
        try:
            objAmp.rewind()
            objSim.rewind()
        except:
            print('Issues when rewinding images.') #KK sys.exit?

        ######
        logger.debug('Starting Iteration Stage : %d'%(iterNum))
        logger.debug("Gross Across: %s" % (coarseAcross))
        logger.debug("Gross Down: %s" % (coarseDown))

        ####Clear objs
        objAmpcor = None
        objOff = None
        offField = None

        objAmpcor = Ampcor()
        objAmpcor.setImageDataType1('real')
        objAmpcor.setImageDataType2('complex')

        ####Dummy values as there is no scale difference at this step
        objAmpcor.setFirstPRF(1.0)
        objAmpcor.setSecondPRF(1.0)
        objAmpcor.setFirstRangeSpacing(1.0)
        objAmpcor.setSecondRangeSpacing(1.0)

        #####Scale all the reference and search windows
        scaleFactor = scale**iterNum
        objAmpcor.windowSizeWidth *= scaleFactor
        objAmpcor.windowSizeHeight *= scaleFactor
        objAmpcor.searchWindowSizeWidth *= scaleFactor
        objAmpcor.searchWindowSizeHeight *= scaleFactor
        xMargin = 2*objAmpcor.searchWindowSizeWidth + objAmpcor.windowSizeWidth
        yMargin = 2*objAmpcor.searchWindowSizeHeight + objAmpcor.windowSizeHeight


        #####Set image limits for search
        offAc = max(firstAc,-coarseAcross)+xMargin
        offDn = max(firstDn,-coarseDown)+yMargin

        offAcmax = int(coarseAcross)
        logger.debug("Gross Max Across: %s" % (offAcmax))
        lastAc = int(min(masterWidth, slaveWidth-offAcmax) - xMargin)

        offDnmax = int(coarseDown)
        logger.debug("Gross Max Down: %s" % (offDnmax))

        lastDn = int(min(masterLength, slaveLength-offDnmax)  - yMargin)
        logger.debug("Last Down: %s" %(lastDn))
        objAmpcor.setFirstSampleAcross(offAc)
        objAmpcor.setLastSampleAcross(lastAc)
        objAmpcor.setFirstSampleDown(offDn)
        objAmpcor.setLastSampleDown(lastDn)
        objAmpcor.setAcrossGrossOffset(coarseAcross)
        objAmpcor.setDownGrossOffset(coarseDown)

        if (offAc > lastAc) or (offDn > lastDn):
            print('Search window scale is too large.')
            print('Skipping Scale: %d'%(iterNum+1))
            continue

        if ((lastAc - offAc) <=  (2*xMargin)) or ((lastDn - offDn) <= (2*yMargin)):
            print('Image not large enough accounting for margins.')
            print('Skipping Scale: %d'%(iterNum+1))
            continue

        logger.debug('Looks = %d'%scaleFactor)
        logger.debug('Correlation window sizes: %d  %d'%(objAmpcor.windowSizeWidth, objAmpcor.windowSizeHeight))
        logger.debug('Search window sizes: %d %d'%(objAmpcor.searchWindowSizeWidth, objAmpcor.searchWindowSizeHeight))
        logger.debug(' Across pos: %d %d out of (%d,%d)'%(objAmpcor.firstSampleAcross, objAmpcor.lastSampleAcross, masterWidth, slaveWidth))
        logger.debug(' Down pos: %d %d out of (%d,%d)'%(objAmpcor.firstSampleDown, objAmpcor.lastSampleDown, masterLength, slaveLength))
        if (iterNum == 0) or finalIteration:
            if catalog is not None:
                # Record the inputs
            isceobj.Catalog.recordInputs(catalog, objAmpcor,
                                         "runRgoffset.%s" % sceneid,
                                         logger,
                                         "runRgoffset.%s" % sceneid)
            objAmpcor.setNumberLocationAcross(numLocationAcross)
            objAmpcor.setNumberLocationDown(numLocationDown)
        else:
            objAmpcor.setNumberLocationAcross(20)
            objAmpcor.setNumberLocationDown(20)
            objAmpcor.setAcrossLooks(scaleFactor)
            objAmpcor.setDownLooks(scaleFactor)
            objAmpcor.setZoomWindowSize(scale*objAmpcor.zoomWindowSize)
            objAmpcor.setOversamplingFactor(2)


        objAmpcor.ampcor(objSim,objAmp)
        offField = objAmpcor.getOffsetField()

        if (iterNum == 0) or finalIteration:
            if catalog is not None:
                # Record the outputs
                isceobj.Catalog.recordOutputs(catalog, objAmpcor,
                                              "runRgoffset.%s" % sceneid,
                                              logger,
                                              "runRgoffset.%s" % sceneid)
        else:
            objOff = isceobj.createOffoutliers()
            objOff.wireInputPort(name='offsets', object=offField)
            objOff.setSNRThreshold(2.0)
            objOff.setDistance(10)
            objOff.setStdWriter = stdWriter.set_file_tags("nstage_offoutliers"+str(iterNum),
                                                          "log",
                                                          "err",
                                                          "out")
            objOff.offoutliers()
            coarseAcross = int(objOff.averageOffsetAcross)
            coarseDown = int(objOff.averageOffsetDown)

    objSim.finalizeImage()
    objAmp.finalizeImage()
    objOff = None
    objAmpcor = None

    return offField
