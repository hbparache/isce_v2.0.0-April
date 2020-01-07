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
# Authors: Kosal Khun, Marco Lavalle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Comment: Adapted from InsarProc/runPrepareResamps.py
import math
import logging

from isceobj.Constants import SPEED_OF_LIGHT

logger = logging.getLogger('isce.isceProc.runPrepareResamps')

def runPrepareResamps(self, rgLooks=None, azLooks=None):
    refScene = self._isce.refScene
    refPol = self._isce.refPol

    orbit = self._isce.orbits[refScene][refPol]
    frame = self._isce.frames[refScene][refPol]
    peg = self._isce.peg
    slcImage = self._isce.slcImages[refScene][refPol]

    time, schPosition, schVelocity, offset = orbit._unpackOrbit()
    s2 = schPosition[0][0]
    s2_2 = schPosition[1][0]

    lines = self._isce.numberPatches * self._isce.numberValidPulses
    self._isce.numberResampLines = lines

    fs = frame.getInstrument().getRangeSamplingRate()
    dr = (SPEED_OF_LIGHT / (2 * fs))
    self._isce.slantRangePixelSpacing = dr

    widthSlc = slcImage.getWidth()

    radarWavelength = frame.getInstrument().getRadarWavelength()

    rc = peg.getRadiusOfCurvature()
    ht = self._isce.averageHeight
    r0 = frame.getStartingRange()

    range = r0 + (widthSlc / 2 * dr)

    costheta = (2*rc*ht+ht*ht-range*range)/-2/rc/range
    sininc = math.sqrt(1 - (costheta * costheta))

    posting = self.posting
    grndpixel = dr / sininc

    if rgLooks:
        looksrange = rgLooks
    else:
        looksrange = int(posting/grndpixel+0.5)

    if azLooks:
        looksaz = azLooks
    else:
        looksaz = int(round(posting/(s2_2 - s2)))

    if (looksrange < 1):
        logger.warn("Number range looks less than zero, setting to 1")
        looksrange = 1
    if (looksaz < 1):
        logger.warn("Number azimuth looks less than zero, setting to 1")
        looksaz = 1

    self._isce.numberAzimuthLooks = looksaz
    self._isce.numberRangeLooks = looksrange
