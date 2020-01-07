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
    from isceobj.Catalog import recordInputsAndOutputs
    chv = []
    for frame, orbit, tag in zip((self._insar.getMasterFrame(),
                                  self._insar.getSlaveFrame()),
                                 (self.insar.masterOrbit,
                                  self.insar.slaveOrbit),
                                 ('master', 'slave')):

        (time, position, velocity, offset) = orbit._unpackOrbit()

        half = len(position)//2 - 1
        xyz = position[half]
        import math
        sch = frame._ellipsoid.xyz_to_sch(xyz)

        chv.append(stdproc.createCalculateFdHeights())
        chv[-1].height = sch[2]

        recordInputsAndOutputs(self.procDoc, chv[-1],
                               "runEstimateHeights.CHV_"+tag, logger,
                               "runEstimateHeights.CHV_"+tag)

    self.insar.fdH1, self.insar.fdH2 = [item.height for item in chv]
    return None
