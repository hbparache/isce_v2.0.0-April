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



from .SRTMManager import SRTMManager
from iscesys.Component.Component import Component
import numpy as np
from isceobj.Image import createDemImage

EXTRA = Component.Parameter('_extra',
    public_name = 'extra',default = '.SRTMGL1',
    type = str,
    mandatory = False,
    doc = 'String to append to default name such as .SRTMGL1 for dem. Since the default is set to read usgs' \
          +' dems if extra is empty one needs to enter a empty string "" in the xml file' +\
          ' otherwise if no value is provided is then interpreted as None by the xml reader.')
DATA_EXT = Component.Parameter('_dataExt',
    public_name = 'dataExt',default = '.hgt',
    type = str,
    mandatory = False,
    doc = 'Extension of the data such as .hgt')
URL = Component.Parameter('_url',
    public_name = 'URL',default = 'http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11',
    type = str,
    mandatory = False,
    doc = "Url for the high resolution DEM.") 
DTYPE = Component.Parameter('_dtype',
    public_name = 'dtype',
    default = 'SHORT',
    type = str,
    mandatory = False,
    doc = 'Data type')
TILE_SIZE = Component.Parameter('_tileSize',
    public_name = 'tileSize',
    default = [3601,3601],
    container=list,
    type=int,
    mandatory = True,
    doc = 'Two element list with the number of row and columns of the tile.')
FILLING_VALUE = Component.Parameter('_fillingValue',
    public_name = 'fillingValue',
    default = -32768,
    type=float,
    mandatory = True,
    doc = 'Value used for missing tiles.')
CORRECT = Component.Parameter('_correct',
    public_name='correct',
    default = False,
    type = bool,
    mandatory = False,
    doc = "Apply correction  EGM96 -> WGS84 (default: True). The output metadata is in xml \n" +
    "format only")
##Base class to handle product such as dem or water mask
class Dem1Manager(SRTMManager):
    family = 'dem1manager'
    parameter_list = (
                       EXTRA,
                       DATA_EXT,
                       URL,
                       DTYPE,
                       TILE_SIZE,
                       FILLING_VALUE,
                       CORRECT
                       )
    #provide default name for output if not provided
    def stitch(self,lats,lons):
        if not self.outputFile:
            self.outputFile = self.defaultName([min(lats[0],lats[1]),max(lats[0],lats[1]),
                                                min(lons[0],lons[1]),max(lons[0],lons[1])])
        return super(Dem1Manager,self).stitch(lats,lons)
       
    ## Corrects the self._image from EGM96 to WGS84 and viceversa.
    #@param image \c Image if provided is used instead of the instance attribute self._image
    #@param conversionType \c int -1 converts from  EGM96 to WGS84, 1 converts from  WGS84 to EGM96
    #@return \c Image instance the converted Image
    def correct(self,image = None,conversionType=-1):
        '''Corrects the self._image from EGM96 to WGS84 and viceversa.'''
        from contrib.demUtils.Correct_geoid_i2_srtm import (
            Correct_geoid_i2_srtm
            )
        cg = Correct_geoid_i2_srtm()
        return cg(image,conversionType) if image else cg(self._image,conversionType)
         
    def createImage(self,lats,lons,filename):
        img = createDemImage()
        lons = np.sort(lons)
        img.initImage(filename,'read',self._tileWidth*int(np.diff(lons)[0]))
        img._metadataLocation = filename + '.xml'
        img.coord1.coordStart = lons[0]
        img.coord1.coordDelta = 1./self._tileWidth
        img.coord2.coordStart = np.sort(lats)[-1]
        img.coord2.coordDelta = -1./self._tileWidth
        return img
    
    def defaultName(self,snwe):
        latMin = np.floor(snwe[0])
        latMax = np.ceil(snwe[1])
        lonMin = np.floor(snwe[2])
        lonMax = np.ceil(snwe[3])
        nsMin,ewMin = self.convertCoordinateToString(latMin, lonMin)
        nsMax,ewMax = self.convertCoordinateToString(latMax, lonMax)
        demName = (
            'demLat_' + nsMin + '_' +nsMax +
            '_Lon_' + ewMin +
            '_' + ewMax  + '.dem'
            )

        return demName
    def __init__(self,family = '', name = ''):
        self.parameter_list = self.parameter_list + super(SRTMManager,self).parameter_list
        self.updateParameters()
        super(Dem1Manager, self).__init__(family if family else  self.__class__.family, name=name)
        self._tileWidth = 3600
    def updateParameters(self):
        self.extendParameterList(SRTMManager,Dem1Manager)
        super(Dem1Manager,self).updateParameters()
   