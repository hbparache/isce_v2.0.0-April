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
# Author: Brett George
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import stdproc
logger = logging.getLogger('isce.insar.runSetmocomppath')

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
    from isceobj.Location.Peg import Peg
    from stdproc.orbit.pegManipulator import averagePeg
    from isceobj.Catalog import recordInputsAndOutputs

    logger.info("Selecting individual peg points")

    planet = self._insar.getMasterFrame().getInstrument().getPlatform().getPlanet()
    masterOrbit = self._insar.getMasterOrbit()
    slaveOrbit = self._insar.getSlaveOrbit()

    if peg:
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

        return


    pegpts = []

    for orbitObj, order in zip((masterOrbit, slaveOrbit)
                                ,('First', 'Second')):
        objGetpeg = stdproc.createGetpeg()
        if peg:
            objGetpeg.setPeg(peg)

        objGetpeg.wireInputPort(name='planet', object=planet)
        objGetpeg.wireInputPort(name='Orbit', object=orbitObj)
        self._stdWriter.setFileTag("getpeg", "log")
        self._stdWriter.setFileTag("getpeg", "err")
        self._stdWriter.setFileTag("getpeg", "out")
        objGetpeg.setStdWriter(self._stdWriter)
        logger.info('Peg points are computed for individual SAR scenes.')
        objGetpeg.estimatePeg()
        pegpts.append(objGetpeg.getPeg())

        recordInputsAndOutputs(self._insar.procDoc, objGetpeg, "getpeg", \
                    logger, "runSetmocomppath")
        #Piyush
        # I set these values here for the sake of continuity, but they need to be updated
        # in orbit2sch as the correct peg point is not yet known
        getattr(self._insar,'set%sAverageHeight'%(order))(objGetpeg.getAverageHeight())
        getattr(self._insar,'set%sProcVelocity'%(order))(objGetpeg.getProcVelocity())


    logger.info('Combining individual peg points.')
    peg = averagePeg(pegpts, planet)

    if self.pegSelect.upper() == 'MASTER':
        logger.info('Using master info for peg point')
        self._insar.setPeg(pegpts[0])
    elif self.pegSelect.upper() == 'SLAVE':
        logger.info('Using slave infor for peg point')
        self._insar.setPeg(pegpts[1])
    elif self.pegSelect.upper() == 'AVERAGE':
        logger.info('Using average peg point')
        self._insar.setPeg(peg)
    else:
        raise Exception('Unknown peg selection method')

