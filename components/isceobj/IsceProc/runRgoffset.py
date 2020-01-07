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
# Authors: Kosal Khun, Marco Lavalle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Comment: Adapted from InsarProc/runRgoffset.py
import logging
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU

logger = logging.getLogger('isce.isce.runRgoffset')

def runRgoffset(self):
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

    pair = (sceneid1, sceneid2)
    imageAmp = self._isce.resampAmpImages[pair][refPol]
    if not imageAmp:
        pair = (sceneid2, sceneid1)
        imageAmp = self._isce.resampAmpImages[pair][refPol]

    prf = self._isce.frames[refScene][refPol].getInstrument().getPulseRepetitionFrequency()
    sid = self._isce.formatname(refScene)
    infos['outputPath'] = self.getoutputdir(refScene)
    catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
    offsetField = run(imageAmp, imageSim, prf, infos, stdWriter, catalog=catalog, sceneid=sid)

    for pair in self._isce.pairsToCoreg:
        self._isce.offsetFields[pair] = offsetField
        self._isce.refinedOffsetFields[pair] = offsetField



def run(imageAmp, imageSim, prf, infos, stdWriter, catalog=None, sceneid='NO_ID'):
    logger.info("Running Rgoffset: %s" % sceneid)

    firstAc =  infos['firstSampleAcross']
    firstDown =  infos['firstSampleDown']
    numLocationAcross =  infos['numberLocationAcross']
    numLocationDown =  infos['numberLocationDown']

    objAmp = isceobj.createIntImage()
    IU.copyAttributes(imageAmp, objAmp)
    objAmp.setAccessMode('read')
    objAmp.createImage()
    widthAmp = objAmp.getWidth()
    intLength = objAmp.getLength()
    lastAc = widthAmp - firstAc
    lastDown = intLength - firstDown

    objSim = isceobj.createImage()
    IU.copyAttributes(imageSim, objSim)
    objSim.setAccessMode('read')
    objSim.createImage()

    # Start modify from here ML 2014-08-05
    #objOffset = isceobj.createEstimateOffsets()
    objOffset = isceobj.createEstimateOffsets(name='insarapp_intsim_estoffset') #ML 2014-08-05
    objOffset.configure()

    if objOffset.acrossGrossOffset is not None:
        coarseAcross = objOffset.acrossGrossOffset
    else:
        coarseAcross = 0

    if objOffset.downGrossOffset is not None:
        coarseDown = objOffset.downGrossOffset
    else:
        coarseDown = 0

    if objOffset.searchWindowSize is None:
        objOffset.setSearchWindowSize(infos['offsetSearchWindowSize'], infos['sensorName'])

    margin = 2*objOffset.searchWindowSize + objOffset.windowSize

    simWidth = objSim.getWidth()
    simLength = objSim.getLength()

    firAc = max(firstAc, -coarseAcross) + margin + 1
    firDn = max(firstDown, -coarseDown) + margin + 1
    lastAc = int(min(widthAmp, simWidth-coarseAcross) - margin - 1)
    lastDn = int(min(intLength, simLength-coarseDown) - margin - 1)


    if not objOffset.firstSampleAcross:
        objOffset.setFirstSampleAcross(firAc)

    if not objOffset.lastSampleAcross:
        objOffset.setLastSampleAcross(lastAc)

    if not objOffset.numberLocationAcross:
        objOffset.setNumberLocationAcross(numLocationAcross)

    if not objOffset.firstSampleDown:
        objOffset.setFirstSampleDown(firDn)

    if not objOffset.lastSampleDown:
        objOffset.setLastSampleDown(lastDn)

    if not objOffset.numberLocationDown:
        objOffset.setNumberLocationDown(numLocationDown)



    # # old isceApp --- from here down
    # objOffset.setSearchWindowSize(infos['offsetSearchWindowSize'], infos['sensorName'])
    # objOffset.setFirstSampleAcross(firstAc)
    # objOffset.setLastSampleAcross(lastAc)
    # objOffset.setNumberLocationAcross(numLocationAcross)
    # objOffset.setFirstSampleDown(firstDown)
    # objOffset.setLastSampleDown(lastDown)
    # objOffset.setNumberLocationDown(numLocationDown)
    # #set the tag used in the outfile. each message is precided by this tag
    # #if the writer is not of "file" type the call has no effect
    objOffset.stdWriter = stdWriter.set_file_tags("rgoffset",
                                                  "log",
                                                  "err",
                                                  "out")

    # objOffset.setFirstPRF(prf)
    # objOffset.setSecondPRF(prf)
    # objOffset.setAcrossGrossOffset(0)
    # objOffset.setDownGrossOffset(0)
    # objOffset.estimateoffsets(image1=objSim, image2=objAmp, band1=0, band2=0)

    ##set the tag used in the outfile. each message is precided by this tag
    ##is the writer is not of "file" type the call has no effect
    ##self._stdWriter.setFileTag("rgoffset", "log")
    ##self._stdWriter.setFileTag("rgoffset", "err")
    ##self._stdWriter.setFileTag("rgoffset", "out")
    ##objOffset.setStdWriter(self._stdWriter)
    ##prf = self._insar.getMasterFrame().getInstrument().getPulseRepetitionFrequency()

    objOffset.setFirstPRF(prf)
    objOffset.setSecondPRF(prf)

    if not objOffset.acrossGrossOffset:
        objOffset.setAcrossGrossOffset(0)

    if not objOffset.downGrossOffset:
        objOffset.setDownGrossOffset(0)

    objOffset.estimateoffsets(image1=objSim, image2=objAmp, band1=0, band2=0)

    if catalog is not None:
        # Record the inputs and outputs
        isceobj.Catalog.recordInputsAndOutputs(catalog, objOffset,
                                               "runRgoffset.%s" % sceneid,
                                               logger,
                                               "runRgoffset.%s" % sceneid)

    objAmp.finalizeImage()
    objSim.finalizeImage()

    return objOffset.getOffsetField()
