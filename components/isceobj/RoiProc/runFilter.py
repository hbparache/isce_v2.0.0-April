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
from mroipac.filter.Filter import Filter
from mroipac.icu.Icu import Icu

logger = logging.getLogger('isce.insar.runFilter')

def runFilter(self, filterStrength):
    logger.info("Applying power-spectral filter")

    # Initialize the flattened interferogram
    topoflatIntFilename = self.insar.topophaseFlatFilename
    intImage = isceobj.createIntImage()
    widthInt = self.insar.resampIntImage.width
    intImage.setFilename(topoflatIntFilename)
    intImage.setWidth(widthInt)
    intImage.setAccessMode('read')
    intImage.createImage()

    # Create the filtered interferogram
    filtIntFilename = 'filt_' + topoflatIntFilename
    filtImage = isceobj.createIntImage()
    filtImage.setFilename(filtIntFilename)
    filtImage.setWidth(widthInt)
    filtImage.setAccessMode('write')
    filtImage.createImage()

    objFilter = Filter()
    objFilter.wireInputPort(name='interferogram',object=intImage)
    objFilter.wireOutputPort(name='filtered interferogram',object=filtImage)
    if filterStrength is not None:
        self.insar.filterStrength = filterStrength

    objFilter.goldsteinWerner(alpha=self.insar.filterStrength)

    intImage.finalizeImage()
    filtImage.finalizeImage()
    del filtImage
    
    #Create phase sigma correlation file here
    filtImage = isceobj.createIntImage()
    filtImage.setFilename(filtIntFilename)
    filtImage.setWidth(widthInt)
    filtImage.setAccessMode('read')
    filtImage.createImage()

    phsigImage = isceobj.createImage()
    phsigImage.dataType='FLOAT'
    phsigImage.bands = 1
    phsigImage.setWidth(widthInt)
    phsigImage.setFilename(self.insar.phsigFilename)
    phsigImage.setAccessMode('write')
    phsigImage.setImageType('cor')#the type in this case is not for mdx.py displaying but for geocoding method
    phsigImage.createImage()

    
    ampImage = isceobj.createAmpImage()
    IU.copyAttributes(self.insar.resampAmpImage, ampImage)
    ampImage.setAccessMode('read')
    ampImage.createImage()


    icuObj = Icu(name='insarapp_filter_icu')
    icuObj.configure()
    icuObj.unwrappingFlag = False

    icuObj.icu(intImage = filtImage, ampImage=ampImage, phsigImage=phsigImage)

    filtImage.finalizeImage()
    phsigImage.finalizeImage()
    phsigImage.renderHdr()
    ampImage.finalizeImage()



    # Set the filtered image to be the one geocoded
    self.insar.topophaseFlatFilename = filtIntFilename
