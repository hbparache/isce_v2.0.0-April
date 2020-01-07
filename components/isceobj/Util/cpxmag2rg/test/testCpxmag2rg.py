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
from iscesys.Component.InitFromXmlFile import InitFromXmlFile
from isceobj.Image.SlcImage import SlcImage
Compatibility.checkPythonVersion()
from isceobj.Util.Cpxmag2rg import Cpxmag2rg

def main():
    obj = Cpxmag2rg()
    initfileSlc1 = 'SlcImage1.xml'
    initSlc1 = InitFromXmlFile(initfileSlc1)
    objSlc1 = SlcImage()
    # only sets the parameter
    objSlc1.initComponent(initSlc1)
    # it actually creates the C++ object
    objSlc1.createImage()
    
    
    initfileSlc2 = 'SlcImage2.xml'
    initSlc2 = InitFromXmlFile(initfileSlc2)
    objSlc2 = SlcImage()
    # only sets the parameter
    objSlc2.initComponent(initSlc2)
    # it actually creates the C++ object
    objSlc2.createImage()
    outname = 'testRGOut'
    obj.setOutputImageName(outname)
    obj.cpxmag2rg(objSlc1,objSlc2)
    objSlc1.finalizeImage()
    objSlc2.finalizeImage()
if __name__ == "__main__":
    sys.exit(main())
