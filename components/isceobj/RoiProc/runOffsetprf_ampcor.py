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
# Author: Gaiangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import isceobj
import mroipac
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj import Constants as CN
from mroipac.ampcor.Ampcor import Ampcor
import numpy as np
from zerodop.baseline.Baseline import Baseline

logger = logging.getLogger('isce.insar.runOffsetprf')

def runOffsetprf(self):
    from isceobj.Catalog import recordInputs

    logger.info("Calculate offset between slcs using ampcor")
    masterFrame = self._insar.getMasterFrame()
    slaveFrame = self._insar.getSlaveFrame()
    masterOrbit = self._insar.masterFrame.orbit
    slaveOrbit = self._insar.slaveFrame.orbit
    prf1 = masterFrame.getInstrument().getPulseRepetitionFrequency()
    prf2 = slaveFrame.getInstrument().getPulseRepetitionFrequency()
    nearRange1 = self.insar.formSLC1.startingRange
    nearRange2 = self.insar.formSLC2.startingRange
    fs1 = masterFrame.getInstrument().getRangeSamplingRate()
    fs2 = slaveFrame.getInstrument().getRangeSamplingRate()

    ###There seems to be no other way of determining image length - Piyush
    patchSize = self._insar.getPatchSize() 
    numPatches = self._insar.getNumberPatches()
    valid_az_samples =  self._insar.getNumberValidPulses()
    firstAc =  self._insar.getFirstSampleAcrossPrf()
    firstDown =  self._insar.getFirstSampleDownPrf()
    numLocationAcross =  self._insar.getNumberLocationAcrossPrf()
    numLocationDown =  self._insar.getNumberLocationDownPrf()

    delRg1 = CN.SPEED_OF_LIGHT / (2*fs1)
    delRg2 = CN.SPEED_OF_LIGHT / (2*fs2)


    try:
        bObj = Baseline()
        bObj.configure()
        bObj.baselineLocation = 'top'
        bObj.wireInputPort(name='masterFrame', object=masterFrame)
        bObj.wireInputPort(name='slaveFrame', object=slaveFrame)
        azoff, rgoff = bObj.baseline()
        coarseAcross = np.mean(rgoff)
        coarseDown = np.mean(azoff)
    except:
        bObj = Baseline()
        bObj.configure()
        bObj.baselineLocation = 'top'
        bObj.wireInputPort(name='masterFrame', object=slaveFrame)
        bObj.wireInputPort(name='slaveFrame', object=masterFrame)
        azoff, rgoff = bObj.baseline()
        coarseAcross = -np.mean(rgoff)
        coarseDown = -np.mean(azoff)

    if self.grossRg is not None:
        coarseAcross = self.grossRg
        pass

    if self.grossAz is not None:
        coarseDown = self.grossAz
        pass

    mSlcImage = self._insar.formSLC1.slcImage
    mSlc = isceobj.createSlcImage()
    IU.copyAttributes(mSlcImage, mSlc)
    accessMode = 'read'
    mSlc.setAccessMode(accessMode)
    mSlc.createImage()
    masterWidth = mSlc.getWidth()
    masterLength = mSlc.getLength()
    
    sSlcImage = self._insar.formSLC2.slcImage
    sSlc = isceobj.createSlcImage()
    IU.copyAttributes(sSlcImage, sSlc)
    accessMode = 'read'
    sSlc.setAccessMode(accessMode)
    sSlc.createImage()
    slaveWidth = sSlc.getWidth()
    slaveLength = sSlc.getLength()

    objAmpcor = Ampcor(name='insarapp_slcs_ampcor')
    objAmpcor.configure()
    objAmpcor.setImageDataType1('complex')
    objAmpcor.setImageDataType2('complex')

    if objAmpcor.acrossGrossOffset is not None:
        coarseAcross = objAmpcor.acrossGrossOffset

    if objAmpcor.downGrossOffset is not None:
        coarseDown = objAmpcor.downGrossOffset
    

    xMargin = 2*objAmpcor.searchWindowSizeWidth + objAmpcor.windowSizeWidth
    yMargin = 2*objAmpcor.searchWindowSizeHeight + objAmpcor.windowSizeHeight

    #####Compute image positions
    offAc = max(firstAc,-coarseAcross)+xMargin
    offDn = max(firstDown,-coarseDown)+yMargin

    offAcmax = int(coarseAcross + ((fs2/fs1)-1)*masterWidth)
    logger.debug("Gross Max Across: %s" % (offAcmax))
    lastAc = int(min(masterWidth, slaveWidth- offAcmax) - xMargin)

    offDnmax = int(coarseDown + ((prf2/prf1)-1)*masterLength)
    logger.debug("Gross Max Down: %s" % (offDnmax))
    lastDown = int( min(masterLength, slaveLength-offDnmax) - yMargin)


    if not objAmpcor.firstSampleAcross:
        objAmpcor.setFirstSampleAcross(offAc)

    if not objAmpcor.lastSampleAcross:
        objAmpcor.setLastSampleAcross(lastAc)

    if not objAmpcor.numberLocationAcross:
        objAmpcor.setNumberLocationAcross(numLocationAcross)

    if not objAmpcor.firstSampleDown:
        objAmpcor.setFirstSampleDown(offDn)

    if not objAmpcor.lastSampleDown:
        objAmpcor.setLastSampleDown(lastDown)

    if not objAmpcor.numberLocationDown:
        objAmpcor.setNumberLocationDown(numLocationDown)

    #####Override gross offsets if not provided
    if not objAmpcor.acrossGrossOffset:
        objAmpcor.setAcrossGrossOffset(coarseAcross)

    if not objAmpcor.downGrossOffset:
        objAmpcor.setDownGrossOffset(coarseDown)


    #####User inputs are overriden here
    objAmpcor.setFirstPRF(prf1)
    objAmpcor.setSecondPRF(prf2)
    objAmpcor.setFirstRangeSpacing(delRg1)
    objAmpcor.setSecondRangeSpacing(delRg2)
    
    
    # Record the inputs
    recordInputs(self._insar.procDoc,
                 objAmpcor,
                 "runOffsetprf",
                 logger,
                 "runOffsetprf")
    
    objAmpcor.ampcor(mSlc,sSlc)

    # Record the outputs
    from isceobj.Catalog import recordOutputs
    recordOutputs(self._insar.procDoc,
                  objAmpcor,
                  "runOffsetprf",
                  logger,
                  "runOffsetprf")

    mSlc.finalizeImage()
    sSlc.finalizeImage()
    
   
    # save the input offset field for the record
    self._insar.setOffsetField(objAmpcor.getOffsetField())
    self._insar.setRefinedOffsetField(objAmpcor.getOffsetField())
