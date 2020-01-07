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
from iscesys.Component.FactoryInit import FactoryInit
from mroipac.formimage.FormSLC import FormSLC
from iscesys.Compatibility import Compatibility
import getopt
Compatibility.checkPythonVersion()

class DriverFormSLC(FactoryInit):
    
            
        
    
    def main(self):
        #get the initialized objects i.e. the raw and slc image and the FormSLC 
        objSlc = self.getComponent('SlcImage')
        objSlc.createImage()
        objRaw = self.getComponent('RawImage')
        objRaw.createImage()
        objFormSlc = self.getComponent('FormSlc')        
        ####
        objFormSlc.formSLCImage(objRaw,objSlc)
        objSlc.finalizeImage()
        objRaw.finalizeImage()

    def __init__(self,argv):
        FactoryInit.__init__(self)
        #call the init factory passing the init file DriverFormSLC.xml as a argument when calling the script
        self.initFactory(argv[1:])

if __name__ == "__main__":
    runObj = DriverFormSLC(sys.argv)
    runObj.main()
