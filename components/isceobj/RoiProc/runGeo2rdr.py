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



import isceobj
import stdproc
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from isceobj.Util.Polynomial import Polynomial
from isceobj.Util.Poly2D import Poly2D
from isceobj.Constants import SPEED_OF_LIGHT
import logging
import numpy as np
import datetime
logger = logging.getLogger('isce.insar.runGeo2rdr') 

def runGeo2rdr(self):
    from zerodop.geo2rdr import createGeo2rdr
    from isceobj.Planet.Planet import Planet

    logger.info("Running geo2rdr")

    info = self.insar.slaveFrame
    slc = self.insar.formSLC2
    intImage = slc.slcImage

    topo = createGeo2rdr()
    topo.configure()

    planet = info.getInstrument().getPlatform().getPlanet()
    topo.slantRangePixelSpacing = info.getInstrument().getRangePixelSize()
    topo.prf = info.getInstrument().getPulseRepetitionFrequency()
    topo.radarWavelength = info.getInstrument().getRadarWavelength()
    topo.orbit = info.getOrbit()
    topo.width = intImage.getWidth()
    topo.length = intImage.getLength()
    topo.wireInputPort(name='planet', object=planet)
    topo.lookSide =  info.instrument.platform.pointingDirection

    topo.setSensingStart(slc.slcSensingStart)
    topo.rangeFirstSample = slc.startingRange
    topo.numberRangeLooks = 1
    topo.numberAzimuthLooks = 1


    if 'native' in self.insar.slaveGeometrySystem.lower():
        print('Native doppler')

        dop = info._dopplerVsPixel[::-1]
        xx = np.linspace(0, (topo.width-1), num=len(dop)+ 1)
        x = (topo.rangeFirstSample - info.startingRange)/topo.slantRangePixelSpacing + xx * topo.numberRangeLooks
        v = np.polyval(dop, x)
        p = np.polyfit(xx, v, len(dop)-1)[::-1] / topo.prf
        p = list(p)

    else:
        print('Zero doppler')
        p = [0.]

    topo.dopplerCentroidCoeffs = p
    topo.fmrateCoeffs = [0.]

    ###Input and output files
    topo.rangeOffsetImageName = self.insar.rangeOffsetImageName
    topo.azimuthOffsetImageName= self.insar.azimuthOffsetImageName


    demImg = isceobj.createImage()
    demImg.load(self.insar.heightFilename + '.xml')
    demImg.setAccessMode('READ')
    topo.demImage = demImg

    latImg = isceobj.createImage()
    latImg.load(self.insar.latFilename + '.xml')
    latImg.setAccessMode('READ')
    topo.latImage = latImg

    lonImg = isceobj.createImage()
    lonImg.load(self.insar.lonFilename + '.xml')
    lonImg.setAccessMode('READ')

    topo.lonImage = lonImg

    topo.geo2rdr()

    return
