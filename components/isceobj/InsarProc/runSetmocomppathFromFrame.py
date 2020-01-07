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
# Author: Eric Gurrola
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import stdproc
logger = logging.getLogger('isce.insar.runSetmocomppath')
from isceobj.Catalog import recordInputsAndOutputs

def averageHeightAboveElp(planet, peg, orbit):
    elp = planet.get_elp()
    elp.setSCH(peg.latitude, peg.longitude, peg.heading)
    t, posXYZ, velXYZ, offset = orbit._unpackOrbit()
    hsum = 0.
    for xyz in posXYZ:
        llh = elp.xyz_to_llh(xyz)
        hsum += llh[2]
    print("averageHeightAboveElp: hsum, len(posXYZ), havg = ",
        hsum, len(posXYZ), havg)
    return hsum/len(posXYZ)

def sVelocityAtMidOrbit(planet, peg, orbit):
    elp = planet.get_elp()
    elp.setSCH(peg.latitude, peg.longitude, peg.heading)
    t, posXYZ, velXYZ, offset = orbit._unpackOrbit()
    sch, vsch = elp.xyzdot_to_schdot(
        posXYZ[len(posXYZ)/2+1], velXYZ[len(posXYZ)/2+1])
    print("sVelocityAtPeg: len(posXYZ)/2., vsch = ",
          len(posXYZ)/2+1, vsch)
    return vsch[0]

def runSetmocomppath(self, peg=None):
    """
    Set the peg point, mocomp heights, and mocomp velocities.
    From information provided in the sensor object
    Possible named input peg (in degrees) is used to set the peg
    rather than using the one given in the Frame.
    """

    planet = (
        self._insar.getMasterFrame().getInstrument().getPlatform().getPlanet())
    masterOrbit = self._insar.getMasterOrbit()
    slaveOrbit = self._insar.getSlaveOrbit()

    if peg:
        #If the input peg is set, then use it
        self._insar.setPeg(peg)
        logger.info("Using the given peg = %r", peg)
        self._insar.setFirstAverageHeight(
            averageHeightAboveElp(planet, peg, masterOrbit))
        self._insar.setSecondAverageHeight(
            averageHeightAboveElp(planet, peg, slaveOrbit))
        self._insar.setFirstProcVelocity(
            sVelocityAtMidOrbit(planet, peg, masterOrbit))
        self._insar.setSecondProcVelocity(
            sVelocityAtMidOrbit(planet, peg, slaveOrbit))
#        recordInputsAndOutputs(self._insar.procDoc, peg, "peg",
#            logger, "runSetmocomppath")
        return

    logger.info("Selecting peg points from frames")

    pegpts = []
    pegpts.append(self._insar.getMasterFrame().peg)
    pegpts.append(self._insar.getMasterFrame().peg)
    peg = averagePeg(pegpts, planet)
    self._insar.setPeg(peg)

    self._insar.setFirstAverageHeight(
        self._insar.getMasterFrame().platformHeight)
    self._insar.setSecondAverageHeight(
        self._insar.getSlaveFrame().platformHeight)
    self._insar.setFirstProcVelocity(
        self._insar.getMasterFrame().procVelocity)
    self._insar.setSecondProcVelocity(
        self._insar.getSlaveFrame().procVelocity)

