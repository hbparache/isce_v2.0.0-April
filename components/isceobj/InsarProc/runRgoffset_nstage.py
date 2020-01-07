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
# Author: Giangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import isceobj
import mroipac
import numpy
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj import Constants as CN
from mroipac.ampcor.NStage import NStage
logger = logging.getLogger('isce.insar.runRgoffset')

def runRgoffset(self):
    from isceobj.Catalog import recordInputs,recordOutputs

    coarseAcross = 0
    coarseDown = 0
    numLocationAcross = self._insar.getNumberLocationAcross()
    numLocationDown = self._insar.getNumberLocationDown()
    firstAc = self._insar.getFirstSampleAcross()
    firstDn = self._insar.getFirstSampleDown()

    ampImage = self._insar.getResampAmpImage()
    slaveWidth = ampImage.getWidth()
    slaveLength = ampImage.getLength()
    objAmp = isceobj.createSlcImage()
    objAmp.dataType = 'CFLOAT'
    objAmp.bands = 1
    objAmp.setFilename(ampImage.getFilename())
    objAmp.setAccessMode('read')
    objAmp.setWidth(slaveWidth)
    objAmp.createImage()

    simImage = self._insar.getSimAmpImage()
    masterWidth = simImage.getWidth()
    objSim = isceobj.createImage()
    objSim.setFilename(simImage.getFilename())
    objSim.dataType = 'FLOAT'
    objSim.setWidth(masterWidth)
    objSim.setAccessMode('read')
    objSim.createImage()
    masterLength = simImage.getLength()


    nStageObj = NStage(name='insarapp_intsim_nstage')
    nStageObj.configure()
    nStageObj.setImageDataType1('real')
    nStageObj.setImageDataType2('complex')

    if nStageObj.acrossGrossOffset is None:
        nStageObj.setAcrossGrossOffset(0)

    if nStageObj.downGrossOffset is None:
        nStageObj.setDownGrossOffset(0)


    # Record the inputs
    recordInputs(self._insar.procDoc,
                nStageObj,
                "runRgoffset",
                logger,
                "runRgoffset")

    nStageObj.nstage(slcImage1=objSim,slcImage2=objAmp)

    recordOutputs(self._insar.procDoc,
                    nStageObj,
                    "runRgoffset",
                    logger,
                    "runRgoffset")

    offField = nStageObj.getOffsetField()

    # save the input offset field for the record
    self._insar.setOffsetField(offField)
    self._insar.setRefinedOffsetField(offField)
