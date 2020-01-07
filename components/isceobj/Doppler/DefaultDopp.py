#!usr/bin/env python

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



from __future__ import print_function
import sys
import numpy as np
from iscesys.Component.Component import Component, Port

class DefaultDopp(Component):
   
    def calculateDoppler(self):
        print('Using default doppler values for sensor: %s'%(self._sensor.__class__.__name__))
        self.activateInputPorts()
        pass

    def fitDoppler(self):
        pass

    def addSensor(self):
        sensor = self._inputPorts.getPort('sensor').getObject()
        self._sensor =  sensor
        if (sensor):
            self.quadratic = sensor.extractDoppler()  #insarapp
            self.coeff_list = sensor.frame._dopplerVsPixel #roiApp
            self.prf = sensor.frame.getInstrument().getPulseRepetitionFrequency()

    logging_name = 'DefaultDopp'

    def __init__(self):
        super(DefaultDopp, self).__init__()
        self._sensor = None
        self.quadratic = {}
        self.coeff_list = None
        self.prf = None
        return None

    def createPorts(self):
        sensorPort = Port(name='sensor',method=self.addSensor)
        self._inputPorts.add(sensorPort)
        return None


if __name__ == '__main__':
    pass
