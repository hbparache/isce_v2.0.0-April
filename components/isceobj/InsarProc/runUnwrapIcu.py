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
# Author: Piyush Agram
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




import sys
import isce
from mroipac.icu.Icu import Icu
from iscesys.Component.Component import Component
from isceobj.Constants import SPEED_OF_LIGHT
import isceobj

# giangi: taken Piyush code grass.py and adapted

def runUnwrap(self):
    '''Specific connector from an insarApp object to a Snaphu object.'''

    wrapName = self.insar.topophaseFlatFilename
    unwrapName = self.insar.unwrappedIntFilename

    #Setup images
    ampImage = self.insar.resampAmpImage.copy(access_mode='read')
    width = ampImage.getWidth()

    #intImage
    intImage = isceobj.createIntImage()
    intImage.initImage(wrapName, 'read', width)
    intImage.createImage()

    #unwImage
    unwImage = isceobj.Image.createUnwImage()
    unwImage.setFilename(unwrapName)
    unwImage.setWidth(width)
    unwImage.imageType = 'unw'
    unwImage.bands = 2
    unwImage.scheme = 'BIL'
    unwImage.dataType = 'FLOAT'
    unwImage.setAccessMode('write')
    unwImage.createImage()

    icuObj = Icu(name='insarapp_icu')
    icuObj.configure()
    icuObj.icu(intImage=intImage, ampImage=ampImage, unwImage = unwImage)
    #At least one can query for the name used
    self.insar.connectedComponentsFilename =  icuObj.conncompFilename
    ampImage.finalizeImage()
    intImage.finalizeImage()
    unwImage.finalizeImage()
    unwImage.renderHdr()

