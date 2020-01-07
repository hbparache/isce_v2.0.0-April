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


class icu(Component):
    '''Specific connector from an insarApp object to a Snaphu object.'''
    def __init__(self, obj):

        basename = obj.insar.topophaseFlatFilename
        wrapName = basename
        unwrapName = basename.replace('.flat', '.unw')

        #Setup images
        self.ampImage = obj.insar.resampAmpImage.copy(access_mode='read')
        self.width = self.ampImage.getWidth()

        #intImage
        intImage = isceobj.createIntImage()
        intImage.initImage(wrapName, 'read', self.width)
        intImage.createImage()
        self.intImage = intImage

        #unwImage
        unwImage = isceobj.Image.createImage()
        unwImage.setFilename(unwrapName)
        unwImage.setWidth(self.width)
        unwImage.imageType = 'unw'
        unwImage.bands = 2
        unwImage.scheme = 'BIL'
        unwImage.dataType = 'FLOAT'
        unwImage.setAccessMode('write')
        unwImage.createImage()
        self.unwImage = unwImage


    def unwrap(self):
        icuObj = Icu()
        icuObj.filteringFlag = False      ##insarApp.py already filters it
        icuObj.initCorrThreshold = 0.1
        icuObj.icu(intImage=self.intImage, ampImage=self.ampImage, unwImage = self.unwImage)

        self.ampImage.finalizeImage()
        self.intImage.finalizeImage()
        self.unwImage.finalizeImage()
        self.unwImage.renderHdr()

