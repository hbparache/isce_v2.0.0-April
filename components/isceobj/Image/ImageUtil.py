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

class ImageUtil:

    def copyAttributes(self,fromIm,toIm, listAtt = None):
        if not (listAtt == None):
            self._listOfAttributes = listAtt
        for att in self._listOfAttributes:
            try:
                fromAtt = getattr(fromIm,att)
                setattr(toIm,att,fromAtt)
            except Exception:
                pass# the image might not have the attributes listed by default

    def __init__(self):

        self._listOfAttributes = ['width','filename','byteOrder','dataType','xmin','xmax','numberGoodBytes','firstLatitude','firstLongitude','deltaLatitude','deltaLongitude']
