#!/usr/bin/env python3

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
# Author: Walter Szeliga
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





import os
import math
import logging
import logging.config
logging.config.fileConfig(os.path.join(os.environ['ISCE_HOME'], 'defaults',
    'logging', 'logging.conf'))
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from isceobj.Location.Peg import Peg
from iscesys.Component.FactoryInit import FactoryInit

class CalculatePegPoint(FactoryInit):

    def calculatePegPoint(self):
        self.logger.info("Parsing Raw Data")
        self.sensorObj.parse()
        frame = self.sensorObj.getFrame()
        # First, get the orbit nadir location at mid-swath and the end of the scene
        orbit = self.sensorObj.getFrame().getOrbit()
        midxyz = orbit.interpolateOrbit(frame.getSensingMid())
        endxyz = orbit.interpolateOrbit(frame.getSensingStop())
        # Next, calculate the satellite heading from the mid-point to the end of the scene
        ellipsoid = frame.getInstrument().getPlatform().getPlanet().get_elp()
        midllh = ellipsoid.xyz_to_llh(midxyz.getPosition())
        endllh = ellipsoid.xyz_to_llh(endxyz.getPosition())
        heading = ellipsoid.geo_hdg(midllh,endllh)
        # Then create a peg point from this data
        peg = Peg(latitude=midllh[0],longitude=midllh[1],heading=heading,ellipsoid=ellipsoid)
        self.logger.info("Peg Point:\n%s" % peg)

    def __init__(self,arglist):
        FactoryInit.__init__(self)
        self.initFactory(arglist)
        self.sensorObj = self.getComponent('Sensor')
        self.logger = logging.getLogger('isce.calculatePegPoint')

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("Usage:%s <xml-parameter file>" % sys.argv[0])
        sys.exit(1)
    runObj = CalculatePegPoint(sys.argv[1:])
    runObj.calculatePegPoint()
