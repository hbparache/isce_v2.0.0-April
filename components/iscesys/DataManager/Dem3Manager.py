#!/usr/bin/env python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2012 to the present, california institute of technology.
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



from .Dem1Manager import Dem1Manager
from iscesys.Component.Component import Component
import numpy as np
from isceobj.Image import createDemImage

EXTRA = Component.Parameter('_extra',
    public_name = 'extra',default = '.SRTMGL3',
    type = str,
    mandatory = False,
    doc = 'String to append to default name such as .SRTMGL3 for dem. Since the default is set to read usgs' \
          +' dems if extra is empty one needs to enter a empty string "" in the xml file' \
          +' otherwise if no value is provided is then interpreted as None by the xml reader.')

URL = Component.Parameter('_url',
    public_name = 'URL',default = 'http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL3.003/2000.02.11',
    type = str,
    mandatory = False,
    doc = "Url for the high resolution DEM.") 

TILE_SIZE = Component.Parameter('_tileSize',
    public_name = 'tileSize',
    default = [1201,1201],
    container=list,
    type=int,
    mandatory = True,
    doc = 'Two element list with the number of row and columns of the tile.')

##Base class to handle product such as dem or water mask
class Dem3Manager(Dem1Manager):
    family = 'dem1manager'
    parameter_list = (
                       EXTRA,
                       URL,
                       TILE_SIZE
                       ) + Dem1Manager.parameter_list
        
    
    def __init__(self,family = '', name = ''):
        self.parameter_list = self.parameter_list + super(Dem1Manager,self).parameter_list
        self.updateParameters()
        super(Dem3Manager, self).__init__(family if family else  self.__class__.family, name=name)
        self._tileWidth = 1200
    def updateParameters(self):
        self.extendParameterList(Dem1Manager,Dem3Manager)
        super(Dem3Manager,self).updateParameters()
   