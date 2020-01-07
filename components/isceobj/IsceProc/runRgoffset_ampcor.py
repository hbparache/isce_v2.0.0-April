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



# Comment: Adapted from InsarProc/runRgoffsetprf_ampcor.py
import logging
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from mroipac.ampcor.Ampcor import Ampcor
from isceobj import Constants as CN

logger = logging.getLogger('isce.isceProc.runRgoffset')

def runRgoffset(self):
    infos = {}
    for attribute in ['firstSampleAcrossPrf', 'firstSampleDownPrf', 'numberLocationAcrossPrf', 'numberLocationDownPrf']:
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

    prf = self._isce.frames[refScene][refPol].getInstrument().getPulseRepetitionFrequency()
    fs1 = self._isce.frames[refScene][refPol].getInstrument().getRangeSamplingRate()
    sid = self._isce.formatname(refScene)
    infos['outputPath'] = self.getoutputdir(refScene)
    catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
    offsetField = run(imageAmp, imageSim, bandRef, prf, fs1, infos, stdWriter, catalog=catalog, sceneid=sid)
    self._isce.procDoc.addAllFromCatalog(catalog)
    # assign the same offsetField to all pairs in pairsToCoreg (will be used by runOffoutliers)
    for pair in self._isce.pairsToCoreg:
        self._isce.offsetFields[pair] = offsetField
        self._isce.refinedOffsetFields[pair] = offsetField


def run(imageAmp, imageSim, numBand, prf, fs1, infos, stdWriter, catalog=None, sceneid='NO_ID'):
    #fs1: range sampling rate
    firstAc =  infos['firstSampleAcrossPrf']
    firstDown =  infos['firstSampleDownPrf']
    numLocationAcross =  infos['numberLocationAcrossPrf']
    numLocationDown =  infos['numberLocationDownPrf']
    coarseAcross = 0
    coarseDown = 0

    #Fake amplitude image as a complex image
    objAmp = isceobj.createImage()
    objAmp.setAccessMode('read')
    objAmp.dataType = 'CFLOAT'
    objAmp.bands = 1
    objAmp.setFilename(imageAmp.filename)
    objAmp.setWidth(imageAmp.width)
    objAmp.createImage()
    widthAmp = objAmp.getWidth()
    intLength = objAmp.getLength()

    objSim = isceobj.createImage()
    objSim.setFilename(imageSim.filename)
    objSim.setWidth(imageSim.width)
    objSim.dataType='FLOAT'
    objSim.setAccessMode('read')
    objSim.createImage()

    # check if it's correct
    delRg1 = CN.SPEED_OF_LIGHT / (2*fs1)

    objAmpcor = Ampcor()
    objAmpcor.setImageDataType1('real')
    objAmpcor.setImageDataType2('complex')

    ####Adjust first and last values using window sizes
    xMargin = 2*objAmpcor.searchWindowSizeWidth + objAmpcor.windowSizeWidth
    yMargin = 2*objAmpcor.searchWindowSizeHeight + objAmpcor.windowSizeHeight

    offAc = max(firstAc, -coarseAcross) + xMargin
    offDn = max(firstDown, -coarseDown) + yMargin
    lastAc = int(min(widthAmp, widthAmp-offAc) - xMargin)
    lastDn = int(min(intLength, intLength-offDn) - yMargin)

    print(xMargin, yMargin)
    print(offAc, lastAc)
    print(offDn, lastDn)
    objAmpcor.setFirstSampleAcross(offAc)
    objAmpcor.setLastSampleAcross(lastAc)
    objAmpcor.setNumberLocationAcross(numLocationAcross)
    objAmpcor.setFirstSampleDown(offDn)
    objAmpcor.setLastSampleDown(lastDn)
    objAmpcor.setNumberLocationDown(numLocationDown)

    #set the tag used in the outfile. each message is preceded by this tag
    #if the writer is not of "file" type the call has no effect
    objAmpcor.stdWriter = stdWriter.set_file_tags("rgoffset",
                                                  "log",
                                                  "err",
                                                  "out")

    objAmpcor.setFirstPRF(prf)
    objAmpcor.setSecondPRF(prf)
    objAmpcor.setAcrossGrossOffset(coarseAcross)
    objAmpcor.setDownGrossOffset(coarseDown)
    objAmpcor.setFirstRangeSpacing(delRg1)
    objAmpcor.setSecondRangeSpacing(delRg1)

    objAmpcor.ampcor(objSim,objAmp)

    if catalog is not None:
        # Record the inputs and outputs
        isceobj.Catalog.recordInputsAndOutputs(catalog, objAmpcor,
                                               "runRgoffset_ampcor.%s" % sceneid,
                                               logger,
                                               "runRgoffset_ampcor.%s" % sceneid)

    objAmp.finalizeImage()
    objSim.finalizeImage()

    return objAmpcor.getOffsetField()
