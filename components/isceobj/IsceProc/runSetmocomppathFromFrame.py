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



# Comment: Adapted from InsarProc/runSetMocomppath.py
import logging
import stdproc
import isceobj
from isceobj.InsarProc.runSetmocomppathFromFrame import averageHeightAboveElp, sVelocityAtMidOrbit

logger = logging.getLogger('isce.isceProc.runSetmocomppath')

def runSetmocomppath(self, peg=None):
    """
    Set the peg point, mocomp heights, and mocomp velocities.
    From information provided in the sensor object
    Possible named input peg (in degrees) is used to set the peg
    rather than using the one given in the Frame.
    """

    getpegs = {}
    stdWriter = self._stdWriter

    if peg:
        self._isce.peg = peg
        logger.info("Using the given peg = %r", peg)
        for sceneid in self._isce.selectedScenes:
            self._isce.pegAverageHeights[sceneid] = {}
            self._isce.pegProcVelocities[sceneid] = {}
            for pol in self._isce.selectedPols:
                frame = self._isce.frames[sceneid][pol]
                planet = frame.getInstrument().getPlatform().getPlanet()
                orbit = self._isce.orbits[sceneid][pol]
                catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
                self._isce.pegAverageHeights[sceneid][pol] = averageHeightAboveElp(planet, peg, orbit)
                self._isce.pegProcVelocities[sceneid][pol] = sVelocityAtMidOrbit(planet, peg, orbit)
                self._isce.procDoc.addAllFromCatalog(catalog)
        return

    logger.info("Selecting peg points from frames")
    for sceneid in self._isce.selectedScenes:
        getpegs[sceneid] = {}
        self._isce.pegAverageHeights[sceneid] = {}
        self._isce.pegProcVelocities[sceneid] = {}
        for pol in self._isce.selectedPols:
            frame = self._isce.frames[sceneid][pol]
            planet = frame.getInstrument().getPlatform().getPlanet()
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            getpegs[sceneid][pol] = frame.peg
            self._isce.pegAverageHeights[sceneid][pol] = frame.platformHeight
            self._isce.pegProcVelocities[sceneid][pol] = frame.procVelocity
            self._isce.procDoc.addAllFromCatalog(catalog)

#    objpegpts = []
#    for pol in self._isce.selectedPols:
#        objpegpts.extend(self._isce.getAllFromPol(pol, getpegs))

    catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
#    peg = averageObjPeg(objpegpts, planet, catalog=catalog, sceneid='ALL') ##planet is the last one from the loop
    peg = frame.peg
    self._isce.procDoc.addAllFromCatalog(catalog)
    self._isce.peg = peg



def averageObjPeg(objpegpts, planet, catalog=None, sceneid='NO_POL'):
    """
    Average peg points.
    """
    logger.info('Combining individual peg points: %s' % sceneid)
    peg = stdproc.orbit.pegManipulator.averagePeg([gp.getPeg() for gp in objpegpts], planet)
    pegheights = [gp.getAverageHeight() for gp in objpegpts]
    pegvelocities = [gp.getProcVelocity() for gp in objpegpts]
    peg.averageheight = float(sum(pegheights)) / len(pegheights)
    peg.averagevelocity = float(sum(pegvelocities)) / len(pegvelocities)
    if catalog is not None:
        isceobj.Catalog.recordInputsAndOutputs(catalog, peg,
                                               "runSetmocomppath.averagePeg.%s" % sceneid,
                                               logger,
                                               "runSetmocomppath.averagePeg.%s" % sceneid)
    return peg
