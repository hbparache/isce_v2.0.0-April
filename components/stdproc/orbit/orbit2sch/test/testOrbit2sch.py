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
# Author: Giangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





from __future__ import print_function
import sys
import os
import math
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from stdproc.orbit.Orbit2sch import Orbit2sch

def main():
    obj = Orbit2sch()
    pegFlag = -1
    obj.setComputePegInfoFlag(pegFlag)
    f1 = open(sys.argv[1])  # position.out from mocomp
    allLines1 = f1.readlines()
    position1 = []
    velocity1 = []
    for i in range(len(allLines1)):
        split1 = allLines1[i].split()
        p1 = [float(split1[2]),float(split1[3]),float(split1[4])] 
        v1 = [float(split1[5]),float(split1[6]),float(split1[7])] 
        position1.append(p1)
        velocity1.append(v1)
    obj.setOrbitPosition(position1)
    obj.setOrbitVelocity(velocity1)
    
    if(pegFlag == -1): 
        pegLat = 0.589368483391443
        pegLon = -2.11721339735596
        pegHdg = -0.227032945109943
        pegHave = 698594.962390185
        obj.setPegLatitude(pegLat)
        obj.setPegLongitude(pegLon)
        obj.setPegHeading(pegHdg)
        obj.setAverageHeight(pegHave)
    obj.orbit2sch()

if __name__ == "__main__":
    sys.exit(main())
