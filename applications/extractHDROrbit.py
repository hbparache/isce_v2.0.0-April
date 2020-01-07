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
import datetime
import logging
import logging.config
logging.config.fileConfig(os.path.join(os.environ['ISCE_HOME'], 'defaults',
    'logging', 'logging.conf'))
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from iscesys.Component.FactoryInit import FactoryInit

class extractHDROrbit(FactoryInit):

    def main(self):
        # Parse the image metadata and extract the image
        self.logger.info('Parsing image metadata')
        self.sensorObj.parse()
        frame = self.sensorObj.getFrame()
        for sv in frame.getOrbit():
            epoch = self.datetimeToEpoch(sv.getTime())
            (x,y,z) = sv.getPosition()
            (vx,vy,vz) = sv.getVelocity()
            print(epoch,x,y,z,vx,vy,vz)

    def datetimeToEpoch(self,dt):
        epoch = dt.hour*60*60 + dt.minute*60 + dt.second
        return epoch

    def __init__(self,arglist):
        FactoryInit.__init__(self)
        self.initFactory(arglist)
        self.sensorObj = self.getComponent('Sensor')
        self.logger = logging.getLogger('isce.extractHDROrbits')

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("Usage:%s <xml-parameter file>" % sys.argv[0])
        sys.exit(1)
    runObj = extractHDROrbit(sys.argv[1:])
    runObj.main()
