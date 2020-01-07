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
import operator
import isceobj


from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from mroipac.correlation.correlation import Correlation
from isceobj.Util.decorators import use_api

logger = logging.getLogger('isce.insar.runCoherence')

## mapping from algorithm method to Correlation instance method name
CORRELATION_METHOD = {
    'phase_gradient' : operator.methodcaller('calculateEffectiveCorrelation'),
    'cchz_wave' : operator.methodcaller('calculateCorrelation')
    }

@use_api
def runCoherence(self, method="phase_gradient"):
                          
    logger.info("Calculating Coherence")

    # Initialize the amplitude
#    resampAmpImage =  self.insar.resampAmpImage
#    ampImage = isceobj.createAmpImage()
#    IU.copyAttributes(resampAmpImage, ampImage)
#    ampImage.setAccessMode('read')
#    ampImage.createImage()
#    ampImage = self.insar.getResampOnlyAmp().copy(access_mode='read')
    ampImage = isceobj.createImage()
    ampImage.load( self.insar.getResampOnlyAmp().filename + '.xml')
    ampImage.setAccessMode('READ')
    ampImage.createImage()
    
    # Initialize the flattened inteferogram
    topoflatIntFilename = self.insar.topophaseFlatFilename
    intImage = isceobj.createImage()
    intImage.load ( self.insar.topophaseFlatFilename + '.xml')
    intImage.setAccessMode('READ')
    intImage.createImage()

#    widthInt = self.insar.resampIntImage.getWidth()
#    intImage.setFilename(topoflatIntFilename)
#    intImage.setWidth(widthInt)
#    intImage.setAccessMode('read')
#    intImage.createImage()

    # Create the coherence image
    cohFilename = topoflatIntFilename.replace('.flat', '.cor')
    cohImage = isceobj.createOffsetImage()
    cohImage.setFilename(cohFilename)
    cohImage.setWidth(intImage.width)
    cohImage.setAccessMode('write')
    cohImage.createImage()

    cor = Correlation()
    cor.configure()
    cor.wireInputPort(name='interferogram', object=intImage)
    cor.wireInputPort(name='amplitude', object=ampImage)
    cor.wireOutputPort(name='correlation', object=cohImage)
   
    cohImage.finalizeImage()
    intImage.finalizeImage()
    ampImage.finalizeImage()

    cor.calculateCorrelation()
#    try:
#        CORRELATION_METHOD[method](cor)
#    except KeyError:
#        print("Unrecognized correlation method")
#        sys.exit(1)
#        pass
    return None
