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
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj import Constants as CN
import numpy as np
from zerodop.baseline.Baseline import Baseline

logger = logging.getLogger('isce.insar.runOffsetprf')

def runOffsetprf(self):
    from isceobj.Catalog import recordInputs

    logger.info("Calculate offset between slcs")

    masterFrame = self._insar.getMasterFrame()
    slaveFrame = self._insar.getSlaveFrame()
    prf1 = masterFrame.getInstrument().getPulseRepetitionFrequency()
    prf2 = slaveFrame.getInstrument().getPulseRepetitionFrequency()
    fs1 = masterFrame.getInstrument().getRangeSamplingRate()

    ###There seems to be no other way of determining image length - Piyush
    patchSize = self._insar.getPatchSize()
    numPatches = self._insar.getNumberPatches()
    valid_az_samples =  self._insar.getNumberValidPulses()
    firstAc =  self._insar.getFirstSampleAcrossPrf()
    firstDown =  self._insar.getFirstSampleDownPrf()
    numLocationAcross =  self._insar.getNumberLocationAcrossPrf()
    numLocationDown =  self._insar.getNumberLocationDownPrf()
    objSlc =  self._insar.formSLC1.slcImage
#    widthSlc = max(self._insar.getMasterSlcImage().getWidth(),
#                   self._insar.getSlaveSlcImage().getWidth())
    widthSlc = objSlc.getWidth()

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


    print("gross Rg: ",self.grossRg)

    if self.grossRg is not None:
        coarseAcross = self.grossRg
        pass


    print("gross Az: ", self.grossAz)

    if self.grossAz is not None:
        coarseDown = self.grossAz
        pass

    coarseAcross = 0 + coarseAcross
    coarseDown = 0 + coarseDown

    mSlcImage = self._insar.formSLC1.slcImage
    mSlc = isceobj.createSlcImage()
    IU.copyAttributes(mSlcImage, mSlc)
#    scheme = 'BIL'
#    mSlc.setInterleavedScheme(scheme)    #Faster access with bands
    accessMode = 'read'
    mSlc.setAccessMode(accessMode)
    mSlc.createImage()

    sSlcImage = self._insar.formSLC2.slcImage
    sSlc = isceobj.createSlcImage()
    IU.copyAttributes(sSlcImage, sSlc)
#    scheme = 'BIL'
#    sSlc.setInterleavedScheme(scheme)   #Faster access with bands
    accessMode = 'read'
    sSlc.setAccessMode(accessMode)
    sSlc.createImage()

    objOffset = isceobj.createEstimateOffsets(name='insarapp_slcs_estoffset')
    objOffset.configure()

    if objOffset.acrossGrossOffset is not None:
        coarseAcross = objOffset.acrossGrossOffset

    if objOffset.downGrossOffset is not None:
        coarseDown = objOffset.downGrossOffset

    if not objOffset.searchWindowSize:
        objOffset.setSearchWindowSize(self.offsetSearchWindowSize, self.sensorName)
    margin = 2*objOffset.searchWindowSize + objOffset.windowSize

    offAc = max(firstAc,-coarseAcross)+margin+1
    offDn = max(firstDown,-coarseDown)+margin+1

    mWidth = mSlc.getWidth()
    sWidth = sSlc.getWidth()
    mLength = mSlc.getLength()
    sLength = sSlc.getLength()

    offDnmax = int(coarseDown + ((prf2/prf1)-1)*mLength)
    lastAc = int(min(mWidth, sWidth-coarseAcross) - margin-1)
    lastDown = int(min(mLength, sLength-offDnmax) - margin-1)


    if not objOffset.firstSampleAcross:
        objOffset.setFirstSampleAcross(offAc)

    if not objOffset.lastSampleAcross:
        objOffset.setLastSampleAcross(lastAc)

    if not objOffset.firstSampleDown:
        objOffset.setFirstSampleDown(offDn)

    if not objOffset.lastSampleDown:
        objOffset.setLastSampleDown(lastDown)

    if not objOffset.numberLocationAcross:
        objOffset.setNumberLocationAcross(numLocationAcross)

    if not objOffset.numberLocationDown:
        objOffset.setNumberLocationDown(numLocationDown)

    if not objOffset.acrossGrossOffset:
        objOffset.setAcrossGrossOffset(coarseAcross)

    if not objOffset.downGrossOffset:
        objOffset.setDownGrossOffset(coarseDown)

    ###Always set these values
    objOffset.setFirstPRF(prf1)
    objOffset.setSecondPRF(prf2)

    # Record the inputs
    recordInputs(self._insar.procDoc,
                 objOffset,
                 "runOffsetprf",
                 logger,
                 "runOffsetprf")

    objOffset.estimateoffsets(image1=mSlc,image2=sSlc,band1=0,band2=0)

    # Record the outputs
    from isceobj.Catalog import recordOutputs
    recordOutputs(self._insar.procDoc,
                  objOffset,
                  "runOffsetprf",
                  logger,
                  "runOffsetprf")

    mSlc.finalizeImage()
    sSlc.finalizeImage()

    # save the input offset field for the record
    self._insar.setOffsetField(objOffset.getOffsetField())
    self._insar.setRefinedOffsetField(objOffset.getOffsetField())
