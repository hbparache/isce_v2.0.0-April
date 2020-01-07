#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2012 to the present, california institute of technology.
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
# Author: Brett George
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU

logger = logging.getLogger('isce.insar.runShadecpx2rg')

def runShadecpx2rg(self):

    imageAmp = self._insar.getResampAmpImage()
    widthAmp = imageAmp.getWidth()
    endian = self._insar.getMachineEndianness()

    filenameSimAmp = self._insar.getSimAmpImageName()
    objSimAmp = isceobj.createImage()
    widthSimAmp = widthAmp
    objSimAmp.initImage(filenameSimAmp,'read',widthSimAmp,'FLOAT')
    
    imageSimAmp = isceobj.createImage()
    IU.copyAttributes(objSimAmp, imageSimAmp)
    self._insar.setSimAmpImage(imageSimAmp) 
    objSimAmp.setAccessMode('write')
    objSimAmp.createImage()
    filenameHt = self._insar.getHeightFilename()
    widthHgtImage = widthAmp # they have same width by construction
    objHgtImage = isceobj.createImage()
    objHgtImage.initImage(filenameHt,'read',widthHgtImage,'FLOAT')
    imageHgt = isceobj.createImage()
    IU.copyAttributes(objHgtImage, imageHgt)
    self._insar.setHeightTopoImage(imageHgt) 
    
    objHgtImage.createImage()
   
    logger.info("Running Shadecpx2rg")
    objShade = isceobj.createSimamplitude()
    #set the tag used in the outfile. each message is precided by this tag
    #is the writer is not of "file" type the call has no effect
    self._stdWriter.setFileTag("simamplitude", "log")
    self._stdWriter.setFileTag("simamplitude", "err")
    self._stdWriter.setFileTag("simamplitude", "out")
    objShade.setStdWriter(self._stdWriter)

    shade = self._insar.getShadeFactor()

    objShade.simamplitude(objHgtImage, objSimAmp, shade=shade)

    # Record the inputs and outputs
    from isceobj.Catalog import recordInputsAndOutputs
    recordInputsAndOutputs(self._insar.procDoc, objShade, "runSimamplitude", \
                  logger, "runSimamplitude")
   
    objHgtImage.finalizeImage()
    objSimAmp.finalizeImage()
    objSimAmp.renderHdr()
