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



# Comment: Adapted from InsarProc/runOrbit2sch.py
import logging
import stdproc
import isceobj

logger = logging.getLogger('isce.isceProc.runOrbit2sch')

def runOrbit2sch(self):
    planet = self._isce.planet
    peg = self._isce.peg
    pegHavg = self._isce.averageHeight
    stdWriter = self._stdWriter
    for sceneid in self._isce.selectedScenes:
        for pol in self._isce.selectedPols:
            frame = self._isce.frames[sceneid][pol]
            orbit = self._isce.orbits[sceneid][pol]
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            sid = self._isce.formatname(sceneid, pol)
            orbit, velocity = run(orbit, peg, pegHavg, planet, stdWriter, catalog=catalog, sceneid=sid)
            self._isce.orbits[sceneid][pol] = orbit ##update orbit
            self._isce.pegProcVelocities[sceneid][pol] = velocity ##update velocity



def run(orbit, peg, pegHavg, planet, stdWriter, catalog=None, sceneid='NO_ID'):
    """
    Convert orbit to SCH.
    """
    logger.info("Converting the orbit to SCH coordinates: %s" % sceneid)

    objOrbit2sch = stdproc.createOrbit2sch(averageHeight=pegHavg)
    objOrbit2sch.stdWriter = stdWriter.set_file_tags("orbit2sch",
                                                     "log",
                                                     "err",
                                                     "log")

    objOrbit2sch(planet=planet, orbit=orbit, peg=peg)
    if catalog:
        isceobj.Catalog.recordInputsAndOutputs(catalog, objOrbit2sch,
                                               "runOrbit2sch." + sceneid,
                                               logger,
                                               "runOrbit2sch." + sceneid)


    #Piyush
    ####The heights and the velocities need to be updated now.
    (ttt, ppp, vvv, rrr) = objOrbit2sch.orbit._unpackOrbit()
    procVelocity = vvv[len(vvv)//2][0]

    return objOrbit2sch.orbit, procVelocity
