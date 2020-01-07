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
import logging
from iscesys.Component.Component import Component,Port
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from ImageFactory import *
import test1
class TestImage:

    def test1(self,file1,file2,width1,width2,test):
        #import pdb
        #pdb.set_trace()
        obj1 = createSlcImage()
        obj2 = createOffsetImage()
        if test == 1:
            obj1.setFilename(file1)
            obj1.setWidth(width1)
            obj1.setAccessMode('read')
            obj2.setFilename(file2)
            obj2.setWidth(width2)
            obj2.setAccessMode('write')
            obj1.createImage()
            obj2.createImage()
            acc1 = obj1.getImagePointer()
            acc2 = obj2.getImagePointer()

        elif test == 2:
            obj1.setFilename(file1)
            obj1.setWidth(width1)
            obj1.setAccessMode('write')
            obj2.setFilename(file2)
            obj2.setWidth(width2)
            obj2.setAccessMode('read')
            obj1.createImage()
            obj2.createImage()
            acc1 = obj1.getImagePointer()
            acc2 = obj2.getImagePointer()
        test1.test1_Py(acc1,acc2,width1,width2,test)

        obj1.finalizeImage()
        obj2.finalizeImage()


    def __init__(self):
        pass



#end class

