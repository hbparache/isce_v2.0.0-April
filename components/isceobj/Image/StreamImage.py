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
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()

from .Image import Image

from iscesys.Component.Component import Component
##
# This class allows the creation of a SlcImage object. The parameters that need to be set are
#\verbatim
#WIDTH: width of the image in units of the DATA_TYPE. Mandatory. 
#FILE_NAME: name of the file containing the image. Mandatory.
#DATA_TYPE: data  type used to store the image. The naming convention is the one adopted by numpy (see LineAccessor class). Optional. Default value 'BYTE'. 
#ACCESS_MODE: access mode of the file such as 'read', 'write' etc. See LineAccessor class for all possible values. Mandatory.
#SCHEME: the interleaving scheme adopted for the image. Could be BIL (band interleaved by line), BIP (band intereleaved by pixel) and BSQ (band sequential). Optional. BIP set by default.
#CASTER: define the type of caster. For example DoubleToFloat reads the image data as double but puts it into a buffer that is of float type. Optional. If not provided casting is not performed.
#\endverbatim
#Since the SlcImage class inherits the Image.Image, the methods of initialization described in the Component package can be used.
#Moreover each parameter can be set with the corresponding accessor method setParameter() (see the class member methods).
#@see DataAccessor.Image.
#@see Component.Component.
DATA_TYPE = Component.Parameter('dataType',
                      public_name='DATA_TYPE',
                      default='byte',
                      type=str,
                      mandatory=True,
                      doc='Image data type.')
IMAGE_TYPE = Component.Parameter('imageType',
                       public_name='IMAGE_TYPE',
                       default='stream',
                       type=str,
                       mandatory=False,
                       private=True,
                       doc='Image type used for displaying.')
'''
WIDTH = Component.Parameter('width',
                       public_name='WIDTH',
                       default=1,
                       type=int,
                       mandatory=True,
                       doc='Image width.')
'''
class StreamImage(Image):

    parameter_list = (
                  DATA_TYPE,
                  IMAGE_TYPE,
                  #WIDTH
                  ) 

    def createImage(self):
        
        self.checkInitialization()
        Image.createImage(self)        

    def initImage(self,filename,accessmode):#overload baseclass method since no need to define the width, since it's 1
        Image.initImage(self,filename,accessmode,self.width)
 
    def updateParameters(self):
        self.extendParameterList(Image,StreamImage)
        super(StreamImage,self).updateParameters()
 
    family = "streamimage"

    def __init__(self,family='',name=''):

        self.updateParameters()
        super(StreamImage, self).__init__(family if family else  self.__class__.family, name=name)
        #self._instanceInit()
        self.width = 1;
        self.initOptionalAndMandatoryLists()
        self.addDescription('STR":" byte stream object.')  
        

        self.logger = logging.getLogger('isce.Image.StreamImage')
        
        return
    
    def __getstate__(self):
        d = dict(self.__dict__)
        del d['logger']
        return d
    def __setstate__(self,d):
        self.__dict__.update(d)
        self.logger = logging.getLogger('isce.Image.StreamImage')
        return

#end class

