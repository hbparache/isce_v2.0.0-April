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
# Author: Walter Szeliga
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




from iscesys.Component.Component import Component

##
# This class provides a basis for image and metadata renderers
#
class BaseRenderer(Component):
    
    def __init__(self):
        Component.__init__(self)        
        
        
        self.dictionaryOfVariables = {'COMPONENT': ['self.component','Component','mandatory']}
        
    def setComponent(self,component):
        if (isinstance(component,Component)):
            self.component = component
        else:
            raise TypeError("component should be of type Component but was of type %s" % component.__class__)
        
    def getComponent(self):
        return self.component
