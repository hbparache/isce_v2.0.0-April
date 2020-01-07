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
# Author: Piyush Agram
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import mroipac.formimage.FormSLC import FormSLC
import isceobj

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj.Catalog import recordInputsAndOutputs

logger = logging.getLogger('isce.insar.runFormSLCisce')

def runFormSLC(self, patchSize=None, goodLines=None, numPatches=None):
    #NOTE tested the formslc() as a stand alone by passing the same inputs
    #computed in Howard terraSAR.py. The differences here arises from the
    #differences in the orbits when using the same orbits the results are very
    #close jng this will make the second term in coarseAz in offsetprf equal
    #zero. we do so since for tsx there is no such a term. Need to ask
    #confirmation
    self.insar.setPatchSize(self.insar.numberValidPulses)
    # the below value is zero because of we just did above, but just want to be
    #  explicit in the definition of is_mocomp

    imageSlc1 =  self.insar.masterRawImage
    imSlc1 = isceobj.createSlcImage()
    IU.copyAttributes(imageSlc1, imSlc1)
    imSlc1.setAccessMode('read')
    imSlc1.createImage()
    formSlc1 = FormSLC()
    formSlc1.configure()

    formSlc1.slcWidth = imSlc1.getWidth()
    formSlc1.startingRange = self.insar.masterFrame.startingRange
    formSlc1.sensingStart = self.insar.masterFrame.sensingStart 
    formSlc1.rangeChirpExtensionPoints = 0

    self.insar.formSLC1 = formSlc1
    self.insar.masterSlcImage = imSlc1
    
    
    imageSlc2 =  self.insar.slaveRawImage
    imSlc2 = isceobj.createSlcImage()
    IU.copyAttributes(imageSlc2, imSlc2)
    imSlc2.setAccessMode('read')
    imSlc2.createImage()
    formSlc2 = stdproc.createFormSLC()

    formSlc2.slcWidth = imSlc2.getWidth()
    formSlc2.startingRange = self.insar.slaveFrame.startingRange
    formSlc2.sensingStart = self.insar.slaveFrame.sensingStart
    formSlc2.rangeChirpExtensionPoints = 0

    self.insar.setNumberPatches(
        imSlc1.getLength()/float(self.insar.numberValidPulses)
        )
    imSlc1.finalizeImage()
    imSlc2.finalizeImage()

    self.insar.setFormSLC1(formSlc1)
    self.insar.setFormSLC2(formSlc2)
