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
import logging
import logging.config
logging.config.fileConfig(os.path.join(os.environ['ISCE_HOME'], 'defaults',
    'logging', 'logging.conf'))
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from iscesys.Component.FactoryInit import FactoryInit
from mroipac.baseline.Baseline import Baseline

class calculateBaselineApp(FactoryInit):

    def main(self):
        masterFrame = self.populateFrame(self.masterObj)
        slaveFrame = self.populateFrame(self.slaveObj)

        # Calculate the baseline information
        baseline = Baseline()
        baseline.wireInputPort(name='masterFrame',object=masterFrame)
        baseline.wireInputPort(name='slaveFrame',object=slaveFrame)
        baseline.wireInputPort(name='masterOrbit',object=masterFrame.getOrbit())
        baseline.wireInputPort(name='slaveOrbit',object=slaveFrame.getOrbit())
        baseline.wireInputPort(name='ellipsoid',object=masterFrame.getInstrument().getPlatform().getPlanet().get_elp())
        baseline.baseline()
        print(baseline)

    def populateFrame(self,sensorObj):
        # Parse the image metadata and extract the image
        self.logger.info('Parsing image metadata')
        sensorObj.parse()
        frame = sensorObj.getFrame()

        # Calculate the height, height_dt, and velocity
        self.logger.info("Calculating Spacecraft Velocity")
        frame.calculateHeightDt()
        frame.calculateVelocity()

        return frame

    def __init__(self,arglist):
        FactoryInit.__init__(self)
        self.initFactory(arglist)
        self.masterObj = self.getComponent('Master')
        self.slaveObj = self.getComponent('Slave')
        self.logger = logging.getLogger('isce.calculateBaseline')

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("Usage:%s <xml-parameter file>" % sys.argv[0])
        sys.exit(1)
    runObj = calculateBaselineApp(sys.argv[1:])
    runObj.main()
