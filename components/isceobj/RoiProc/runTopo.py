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
logger = logging.getLogger('isce.insar.runTopo') 

def runTopo(self):
    from zerodop.topozero import createTopozero
    from isceobj.Planet.Planet import Planet

    logger.info("Running topo")

    #IU.copyAttributes(demImage, objDem)
    objDem = self.insar.demImage.clone()

    info = self.insar.masterFrame
    slc = self.insar.formSLC1
    intImage = slc.slcImage


    planet = info.getInstrument().getPlatform().getPlanet()
    topo = createTopozero()

    topo.slantRangePixelSpacing = 0.5 * SPEED_OF_LIGHT / info.rangeSamplingRate
    topo.prf = info.PRF
    topo.radarWavelength = info.radarWavelegth
    topo.orbit = info.orbit
    topo.width = intImage.getWidth()
    topo.length = intImage.getLength()
    topo.wireInputPort(name='dem', object=objDem)
    topo.wireInputPort(name='planet', object=planet)
    topo.numberRangeLooks = 1
    topo.numberAzimuthLooks = 1
    topo.lookSide = info.getInstrument().getPlatform().pointingDirection
    topo.sensingStart = slc.slcSensingStart 
    topo.rangeFirstSample = slc.startingRange

    topo.demInterpolationMethod='BIQUINTIC'
    topo.latFilename = self.insar.latFilename
    topo.lonFilename = self.insar.lonFilename
    topo.losFilename = self.insar.losFilename
    topo.heightFilename = self.insar.heightFilename
#    topo.incFilename = os.path.join(info.outdir, 'inc.rdr')
#    topo.maskFilename = os.path.join(info.outdir, 'mask.rdr')


    ####Doppler adjustment
    dop = info._dopplerVsPixel[::-1]
    xx = np.linspace(0, (topo.width-1), num=len(dop)+ 1)
    x = (topo.rangeFirstSample - info.startingRange)/topo.slantRangePixelSpacing + xx * topo.numberRangeLooks
    v = np.polyval(dop, x)
    p = np.polyfit(xx, v, len(dop)-1)[::-1]

    doppler = Poly2D()
    doppler.setWidth(topo.width)
    doppler.setLength(topo.length)
    doppler.initPoly(rangeOrder = len(dop)-1, azimuthOrder=0, coeffs=[list(p)])

    topo.polyDoppler = doppler

    topo.topo()


    # Record the inputs and outputs
    from isceobj.Catalog import recordInputsAndOutputs
    recordInputsAndOutputs(self._insar.procDoc, topo, "runTopo",
                           logger, "runTopo")

    self._insar.setTopo(topo)

    return topo
