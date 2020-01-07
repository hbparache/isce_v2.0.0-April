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
from iscesys.Component.InitFromDictionary import InitFromDictionary
from mroipac.looks.Cpxlooks import Cpxlooks

def main():
    obj = Cpxlooks()
    infile = "/Users/giangi/TEST_DIR/int_930110_950523/flat_PRC_930110-950523.int"
    outfile = 'testCpx'
    rlook = 4;
    alook = 4;
    width = 5700
    phRange = 0.0001
    phAzimuth = 0.0002
    enIn = 'l'
    enOut = 'l'
    length = 2593 
    #with all arguments
    #dict = {'PHASE_RANGE':phRange,'INPUT_ENDIANNESS':enIn,'OUTPUT_ENDIANNESS':enOut,'LENGTH':length,'PHASE_AZIMUTH':phAzimuth,'WIDTH':width,'INPUT_IMAGE':infile,'OUTPUT_IMAGE':outfile,'RANGE_LOOK':rlook,'AZIMUTH_LOOK':alook}
    #with only mandatory arguments
    dict = {'WIDTH':width,'INPUT_IMAGE':infile,'OUTPUT_IMAGE':outfile,'RANGE_LOOK':rlook,'AZIMUTH_LOOK':alook}
    initDict = InitFromDictionary(dict)
    obj.initComponent(initDict)
    obj.cpxlooks()

if __name__ == "__main__":
    sys.exit(main())
