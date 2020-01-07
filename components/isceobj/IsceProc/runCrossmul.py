#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2013 to the present, california institute of technology.
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



# Comment: Adapted from IsceProc/runResamp.py
import os
import logging
from components.stdproc.stdproc import crossmul
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU

logger = logging.getLogger('isce.isceProc.runCrossmul')

def runCrossmul(self):
    #stdWriter = self._stdWriter
    resampName = self._isce.resampImageName
    azLooks = self._isce.numberAzimuthLooks
    rgLooks = self._isce.numberRangeLooks
    lines = int( self._isce.numberResampLines ) # ML 2014-08-21 - added int, but need to change IsceProc

    for sceneid1, sceneid2 in self._isce.selectedPairs:
        pair = (sceneid1, sceneid2)
        self._isce.resampIntImages[pair] = {}
        self._isce.resampAmpImages[pair] = {}
        for pol in self._isce.selectedPols:
            imageSlc1 = self._isce.slcImages[sceneid1][pol]
            imageSlc2 = self._isce.slcImages[sceneid2][pol]

            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            sid = self._isce.formatname(pair, pol)
            resampFilename = os.path.join(self.getoutputdir(sceneid1, sceneid2), self._isce.formatname(pair, pol, resampName))
            imageInt, imageAmp = run(imageSlc1, imageSlc2, resampFilename, azLooks, rgLooks, lines, catalog=catalog, sceneid=sid)
            self._isce.resampIntImages[pair][pol] = imageInt
            self._isce.resampAmpImages[pair][pol] = imageAmp


def run(imageSlc1, imageSlc2, resampName, azLooks, rgLooks, lines, catalog=None, sceneid='NO_ID'):
    logger.info("Generating interferogram: %s" % sceneid)

    objSlc1 = isceobj.createSlcImage()
    IU.copyAttributes(imageSlc1, objSlc1)
    objSlc1.setAccessMode('read')
    objSlc1.createImage()

    objSlc2 = isceobj.createSlcImage()
    IU.copyAttributes(imageSlc2, objSlc2)
    objSlc2.setAccessMode('read')
    objSlc2.createImage()

    slcWidth = imageSlc1.getWidth()
    intWidth = int(slcWidth / rgLooks)

    logger.info("Will ouput interferogram and amplitude: %s" % sceneid)
    resampAmp = resampName + '.amp'
    resampInt = resampName + '.int'

    objInt = isceobj.createIntImage()
    objInt.setFilename(resampInt)
    objInt.setWidth(intWidth)
    imageInt = isceobj.createIntImage()
    IU.copyAttributes(objInt, imageInt)
    objInt.setAccessMode('write')
    objInt.createImage()

    objAmp = isceobj.createAmpImage()
    objAmp.setFilename(resampAmp)
    objAmp.setWidth(intWidth)
    imageAmp = isceobj.createAmpImage()
    IU.copyAttributes(objAmp, imageAmp)
    objAmp.setAccessMode('write')
    objAmp.createImage()

    objCrossmul = crossmul.createcrossmul()
    objCrossmul.width = slcWidth
    objCrossmul.length = lines
    objCrossmul.LooksDown = azLooks
    objCrossmul.LooksAcross = rgLooks

    #set the tag used in the outfile. each message is precided by this tag
    #is the writer is not of "file" type the call has no effect
#    objCrossmul.stdWriter = stdWriter.set_file_tags("resamp",
#                                                  "log",
#                                                  "err",
#                                                  "out")
    objCrossmul.crossmul(objSlc1, objSlc2, objInt, objAmp)

    if catalog is not None:
        # Record the inputs and outputs
        isceobj.Catalog.recordInputsAndOutputs(catalog, objCrossmul,
                                               "runCrossmul.%s" % sceneid,
                                               logger,
                                               "runCrossmul.%s" % sceneid)

    for obj in [objInt, objAmp, objSlc1, objSlc2]:
        obj.finalizeImage()

    return imageInt, imageAmp
