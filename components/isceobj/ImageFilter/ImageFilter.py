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
from isceobj.ImageFilter import Filter as FL
from isceobj.Image.Image import Image
import logging


class Filter:
#Use kwargs so possible subclasses can add parameters to the init function.  

    def init(self,imgIn,nameOut,**kwargs):
        """Abstract method"""
        raise NotImplementedError

    def finalize(self):
        """Call to the bindings finalize. Subclass can extend it but needs to call the baseclass one"""
        FL.finalize(self._filter)
        

    def extract(self):
        """Perform the data extraction"""
        FL.extract(self._filter)


#This is specific to the extract band filter. Put in the base class all the methods
#we need for the provided filters. New filters will implement their own if needed
#in the subclass
    
    def selectBand(self,band):
        """Select a specified band from the Image"""
        FL.selectBand(self._filter,band)
    
    def setStartLine(self,line):
        """Set the line where extraction should start"""
        FL.setStartLine(self._filter,line)
    
    def setEndLine(self,line):
        """Set the line where extraction should end"""
        FL.setEndLine(self._filter,line)
    
    def __init__(self):
        #get the filter C++ object pointer
        self._filter = None
        self._imgOut = None 



if __name__ == "__main__":
    sys.exit(main())
