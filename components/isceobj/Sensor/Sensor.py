#!/usr/bin/env python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2013 to the present, california institute of technology.
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
# Author: Piyush Agram
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




import datetime
import logging
import isceobj
from isceobj.Scene.Frame import Frame
from iscesys.Component.Component import Component

OUTPUT = Component.Parameter(
    'output',
    public_name='OUTPUT',
    default='',
    type=str,
    mandatory=False,
    intent='input',
    doc='Raw output file name.'
)
class Sensor(Component):
    """
    Base class for storing Sensor data
    """
    parameter_list = (
                      OUTPUT,                    
                     )
    logging_name =  None
    lookMap = {'RIGHT' : -1,
               'LEFT'  : 1}
    family = 'sensor'

    def __init__(self,family='',name=''):
        super(Sensor, self).__init__(family if family else  self.__class__.family, name=name)
        self.frame = Frame()
        self.frame.configure()

        self.logger = logging.getLogger(self.logging_name)

        self.frameList = []
       
        return None


    def getFrame(self):
        '''
        Return the frame object.
        '''
        return self.frame

    def parse(self):
        '''
        Dummy routine.
        '''
        raise NotImplementedError("In Sensor Base Class")


    def populateMetadata(self, **kwargs):
        """
        Create the appropriate metadata objects from our HDF5 file
        """
        self._populatePlatform(**kwargs)
        self._populateInstrument(**kwargs)
        self._populateFrame(**kwargs)
        self._populateOrbit(**kwargs)

    def _populatePlatform(self,**kwargs):
        '''
        Dummy routine to populate platform information.
        '''
        raise NotImplementedError("In Sensor Base Class")

    def _populateInstrument(self,**kwargs):
        """
        Dummy routine to populate instrument information.
        """
        raise NotImplementedError("In Sensor Base Class")

    def _populateFrame(self,**kwargs):
        """
        Dummy routine to populate frame object.
        """
        raise NotImplementedError("In Sensor Base Class")

    def _populateOrbit(self,**kwargs):
        """
        Dummy routine to populate orbit information.
        """
        raise NotImplementedError("In Sensor Base Class")

    def extractImage(self):
        """
        Dummy routine to extract image.
        """
        raise NotImplementedError("In Sensor Base Class")

    def extractDoppler(self):
        """
        Dummy routine to extract doppler centroid information.
        """
        raise NotImplementedError("In Sensor Base Class")
