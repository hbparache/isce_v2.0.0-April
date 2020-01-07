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
import stdproc

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU


logger = logging.getLogger('isce.insar.runResamp_image')

def runResamp_image(self):
    imageSlc =  self._insar.getMasterSlcImage()
    widthSlc = max(self._insar.getMasterSlcImage().getWidth(), self._insar.getSlaveSlcImage().getWidth())
    offsetField = self._insar.getRefinedOffsetField()                
    
    instrument = self._insar.getMasterFrame().getInstrument()
    
    dopplerCoeff = self._insar.getDopplerCentroid().getDopplerCoefficients(inHz=False)
    
    pixelSpacing = self._insar.getSlantRangePixelSpacing()
    looks = self._insar.getNumberLooks() 
    lines = self._insar.getNumberResampLines() 
    numFitCoeff = self._insar.getNumberFitCoefficients() 
    
    offsetFilename = self._insar.getOffsetImageName()
    offsetAz = 'azimuth' + offsetFilename.capitalize()
    offsetRn = 'range' + offsetFilename.capitalize()
    widthOffset = int(widthSlc / looks)
    imageAz = isceobj.createOffsetImage()
    imageAz.setFilename(offsetAz)
    imageAz.setWidth(widthOffset)
    imageRn = isceobj.createOffsetImage()
    imageRn.setFilename(offsetRn)
    imageRn.setWidth(widthOffset)
   
    self._insar.setOffsetAzimuthImage(imageAz)
    self._insar.setOffsetRangeImage(imageRn)

    objAz = isceobj.createOffsetImage()
    objRn = isceobj.createOffsetImage()
    IU.copyAttributes(imageAz, objAz)
    IU.copyAttributes(imageRn, objRn)
    objAz.setAccessMode('write')
    objAz.createImage()
    objRn.setAccessMode('write')
    objRn.createImage()
    
    
    objResamp_image = stdproc.createResamp_image()
    objResamp_image.wireInputPort(name='offsets', object=offsetField)
    objResamp_image.wireInputPort(name='instrument', object=instrument)
    objResamp_image.setSlantRangePixelSpacing(pixelSpacing)
    objResamp_image.setDopplerCentroidCoefficients(dopplerCoeff)
    objResamp_image.setNumberLooks(looks)
    objResamp_image.setNumberLines(lines)
    objResamp_image.setNumberRangeBin(widthSlc)
    objResamp_image.setNumberFitCoefficients(numFitCoeff)
    #set the tag used in the outfile. each message is precided by this tag
    #is the writer is not of "file" type the call has no effect
    self._stdWriter.setFileTag("resamp_image", "log")
    self._stdWriter.setFileTag("resamp_image", "err")
    self._stdWriter.setFileTag("resamp_image", "out")
    objResamp_image.setStdWriter(self._stdWriter)

    objResamp_image.resamp_image(objRn, objAz)

    # Record the inputs and outputs
    from isceobj.Catalog import recordInputsAndOutputs
    recordInputsAndOutputs(self._insar.procDoc, objResamp_image, "runResamp_image", \
                  logger, "runResamp_image")

    objRn.finalizeImage()
    objAz.finalizeImage()
