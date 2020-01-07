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



# Comment: Adapted from InsarProc/runEstimateHeights.py
import logging
import stdproc
import isceobj

logger = logging.getLogger('isce.isceProc.runEstimateHeights')

def runEstimateHeights(self):
    for sceneid in self._isce.selectedScenes:
        self._isce.fdHeights[sceneid] = {}
        for pol in self._isce.selectedPols:
            frame = self._isce.frames[sceneid][pol]
            orbit = self._isce.orbits[sceneid][pol]
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            sid = self._isce.formatname(sceneid, pol)
            chv = run(frame, orbit, catalog=catalog, sceneid=sid)
            self._isce.procDoc.addAllFromCatalog(catalog)
            self._isce.fdHeights[sceneid][pol] = chv.height


def run(frame, orbit, catalog=None, sceneid='NO_ID'):
    """
    Estimate heights from orbit.
    """
    (time, position, velocity, offset) = orbit._unpackOrbit()

    half = len(position)//2 - 1
    xyz = position[half]
    sch = frame._ellipsoid.xyz_to_sch(xyz)

    chv = stdproc.createCalculateFdHeights()
#    planet = frame.getInstrument().getPlatform().getPlanet()
#    chv(frame=frame, orbit=orbit, planet=planet)
    chv.height = sch[2]

    if catalog is not None:
        isceobj.Catalog.recordInputsAndOutputs(catalog, chv,
                                               "runEstimateHeights.CHV.%s" % sceneid,
                                               logger,
                                               "runEstimateHeights.CHV.%s" % sceneid)
    return chv
