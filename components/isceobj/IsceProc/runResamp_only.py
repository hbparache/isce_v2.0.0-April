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



# Comment: Adapted from InsarProc/runResamp_only.py
import logging
import stdproc
import isceobj
import os

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU

logger = logging.getLogger('isce.isceProc.runResamp_only')

def runResamp_only(self):
    infos = {}
    for attribute in ['dopplerCentroid', 'resampOnlyImageName', 'numberFitCoefficients', 'slantRangePixelSpacing']:
        infos[attribute] = getattr(self._isce, attribute)

    stdWriter = self._stdWriter

    pair = self._isce.pairsToCoreg[0]
    offsetField = self._isce.refinedOffsetFields[pair]

    for sceneid1, sceneid2 in self._isce.selectedPairs:
        pair = (sceneid1, sceneid2)
        self._isce.resampOnlyImages[pair] = {}
        self._isce.resampOnlyAmps[pair] = {}
        for pol in self._isce.selectedPols:
            imageInt = self._isce.resampIntImages[pair][pol]
            imageAmp = self._isce.resampAmpImages[pair][pol]
            frame1 = self._isce.frames[sceneid1][pol]
            instrument = frame1.getInstrument()
            sid = self._isce.formatname(pair, pol)
            infos['outputPath'] = os.path.join(self.getoutputdir(sceneid1, sceneid2), sid)
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            objIntOut, objAmpOut = run(imageInt, imageAmp, instrument, offsetField, infos, stdWriter, catalog=catalog, sceneid=sid)
            self._isce.resampOnlyImages[pair][pol] = objIntOut
            self._isce.resampOnlyAmps[pair][pol] = objAmpOut


def run(imageInt, imageAmp, instrument, offsetField, infos, stdWriter, catalog=None, sceneid='NO_ID'):
    logger.info("Running Resamp_only: %s" % sceneid)

    objInt = isceobj.createIntImage()
    objIntOut = isceobj.createIntImage()
    IU.copyAttributes(imageInt, objInt)
    IU.copyAttributes(imageInt, objIntOut)
    outIntFilename = infos['outputPath'] + '.' + infos['resampOnlyImageName']
    objInt.setAccessMode('read')
    objIntOut.setFilename(outIntFilename)

    objIntOut.setAccessMode('write')
    objInt.createImage()
    objIntOut.createImage()

    objAmp = isceobj.createAmpImage()
    objAmpOut = isceobj.createAmpImage()
    IU.copyAttributes(imageAmp, objAmp)
    IU.copyAttributes(imageAmp, objAmpOut)
    outAmpFilename = outIntFilename.replace('int', 'amp')
    objAmp.setAccessMode('read')
    objAmpOut.setFilename(outAmpFilename)

    objAmpOut.setAccessMode('write')
    objAmp.createImage()
    objAmpOut.createImage()

    numRangeBin = objInt.getWidth()
    lines = objInt.getLength()


    dopplerCoeff = infos['dopplerCentroid'].getDopplerCoefficients(inHz=False)

    objResamp = stdproc.createResamp_only()

    objResamp.setNumberLines(lines)
    objResamp.setNumberFitCoefficients(infos['numberFitCoefficients'])
    objResamp.setSlantRangePixelSpacing(infos['slantRangePixelSpacing'])
    objResamp.setNumberRangeBin(numRangeBin)
    objResamp.setDopplerCentroidCoefficients(dopplerCoeff)

    objResamp.wireInputPort(name='offsets', object=offsetField)
    objResamp.wireInputPort(name='instrument', object=instrument)
    #set the tag used in the outfile. each message is precided by this tag
    #if the writer is not of "file" type the call has no effect
    objResamp.stdWriter = stdWriter.set_file_tags("resamp_only",
                                                  "log",
                                                  "err",
                                                  "out")

    objResamp.resamp_only(objInt, objIntOut, objAmp, objAmpOut)

    if catalog is not None:
        # Record the inputs and outputs
        isceobj.Catalog.recordInputsAndOutputs(catalog, objResamp,
                                               "runResamp_only.%s" % sceneid,
                                               logger,
                                               "runResamp_only.%s" % sceneid)
    objInt.finalizeImage()
    objIntOut.finalizeImage()
    objAmp.finalizeImage()
    objAmpOut.finalizeImage()

    return objIntOut, objAmpOut
