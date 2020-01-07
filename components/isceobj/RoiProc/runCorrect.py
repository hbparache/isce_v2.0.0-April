#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2010 to the present, california institute of technology.
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
import stdproc
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
import datetime
import numpy as np
from isceobj.Constants import SPEED_OF_LIGHT
logger = logging.getLogger('isce.insar.runCorrect') 


def runCorrect(self):
    from zerodop.geo2rdr import createGeo2rdr
    logger.info("Running correct")

    info = self._insar.slaveFrame
    slc = self.insar.formSLC2

    intImage = self.insar.topoIntImage.clone()
    planet = info.instrument.platform.planet

    
    correct = createGeo2rdr()
    correct.configure()

    correct.slantRangePixelSpacing = 0.5 * SPEED_OF_LIGHT / info.rangeSamplingRate
    correct.prf = info.instrument.PRF
    correct.radarWavelength = info.instrument.radarWavelength
    correct.orbit = info.orbit
    correct.wireInputPort(name='planet', object=planet)
    correct.numberRangeLooks = self.insar.numberRangeLooks
    correct.numberAzimuthLooks = self.insar.numberAzimuthLooks
    correct.lookSide = info.instrument.platform.pointingDirection
    
    correct.fmrateCoeffs = [0.]
    correct.setSensingStart(slc.slcSensingStart + datetime.timedelta(seconds = 0.5*(self.insar.numberAzimuthLooks-1)/correct.prf))
    correct.rangeFirstSample = slc.startingRange + 0.5*(self.insar.numberRangeLooks-1)*correct.slantRangePixelSpacing

    demImage = isceobj.createImage()
    demImage.load(self.insar.heightFilename + '.xml')
    demImage.setAccessMode('READ')

    latImage = isceobj.createImage()
    latImage.load(self.insar.latFilename + '.xml')
    latImage.setAccessMode('READ')

    lonImage = isceobj.createImage()
    lonImage.load(self.insar.lonFilename + '.xml')
    lonImage.setAccessMode('READ')

    correct.width = latImage.getWidth()
    correct.length = latImage.getLength()

    correct.demImage = demImage
    correct.latImage = latImage
    correct.lonImage = lonImage

    correct.rangeOffsetImageName = 'range.off'

    ####Compute the native doppler polynomial
    dop = info._dopplerVsPixel[::-1]
    xx = np.linspace(0, (slc.slcImage.width-1), num=len(dop)+ 1)
    x = (slc.startingRange - info.startingRange)/correct.slantRangePixelSpacing + xx 
    v = np.polyval(dop, x)
    p = np.polyfit(xx, v, len(dop)-1)[::-1]

    print(p)
    correct.dopplerCentroidCoeffs = list(p)

    correct.geo2rdr()
   
    flattenWithOffsets(intImage.filename, 'range.off', self.insar.topophaseFlatFilename, info, correct.numberRangeLooks)

    return correct


def flattenWithOffsets(fname, offname, flatname, frame, rglooks):
    from isceobj.Util.ImageUtil import ImageLib as IML
    import logging

    ifg = IML.mmapFromISCE(fname, logging).bands[0]
    off = IML.mmapFromISCE(offname, logging).bands[0]

    lgt = min(ifg.shape[0], off.shape[0])

    delr = 0.5 * SPEED_OF_LIGHT / frame.rangeSamplingRate
    wvl = frame.getInstrument().getRadarWavelength()
    factor = 4 * np.pi * delr * rglooks / wvl
    cJ = np.complex64(1.0j)

    fid = open(flatname, 'wb')
    for ii in range(lgt):
        data = ifg[ii] * np.exp(-cJ * factor* off[ii])
        data.astype(np.complex64).tofile(fid)

    fid.close()

    img = isceobj.createIntImage()
    img.setFilename(flatname)
    img.setWidth(ifg.shape[1])
    img.setAccessMode('READ')
    img.renderHdr()

    pass
