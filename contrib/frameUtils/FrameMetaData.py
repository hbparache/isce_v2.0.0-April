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
import os
from mroipac.geolocate.Geolocate import Geolocate
import logging
import math
class FrameMetaData(object):
    
    def getExtremes(self,delta):
        latMax = -1000
        latMin = 1000
        lonMax = -1000
        lonMin = 1000
    
        for bb in self._bbox:
            if bb[0] > latMax:
                latMax = bb[0]
            if bb[0] < latMin:
                latMin = bb[0]
            if bb[1] > lonMax:
                lonMax = bb[1]
            if bb[1] < lonMin:
                lonMin = bb[1]
    
        latMin = math.floor(latMin-delta)
        latMax = math.ceil(latMax+delta)
        lonMin = math.floor(lonMin-delta)
        lonMax = math.ceil(lonMax+delta)
        return latMin,latMax,lonMin,lonMax
        
    def getSpacecraftName(self):
        return self._spacecraftName
    def getOrbitNumber(self):
        return self._orbitNumber
    def getTrackNumber(self):
        return self._trackNumber
    def getFrameNumber(self):
        return self._frameNumber
    def getBBox(self):
        return self._bbox
    def getSensingStart(self):
        return self._sensingStart
    def getSensingStop(self):
        return self._sensingStop
    def getDirection(self):
        return self._direction
    
    def setOrbitNumber(self,val):
        self._orbitNumber = val
    def setTrackNumber(self,val):
        self._trackNumber = val
    def setFrameNumber(self,val):
        self._frameNumber = val
    def setSpacecraftName(self,val):
        self._spacecraftName = val
    def setBBox(self,val):
        self._bbox = val
    def setSensingStart(self,val):
        self._sensingStart = val
    def setSensingStop(self,val):
        self._sensingStop = val
    def setDirection(self,val):
        self._direction = val

    def __init__(self):
        self._spacecraftName = ''
        self._orbitNumber = None
        self._trackNumber = None
        self._frameNumber = None
        self._bbox = [] # [near start, far start, near end, far end]  
        self._sensingStart = None
        self._sensingStop = None
        self._direction = ''
        
    spacecraftName = property(getSpacecraftName,setSpacecraftName)
    orbitNumber = property(getOrbitNumber,setOrbitNumber)
    trackNumber = property(getTrackNumber,setTrackNumber)
    frameNumber = property(getFrameNumber,setFrameNumber)
    bbox =  property(getBBox,setBBox)
    sensingStart = property(getSensingStart,setSensingStart)
    sensingStop = property(getSensingStop,setSensingStop)
    direction = property(getDirection,setDirection)
