#!/usr/bin/env python3 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2014 to the present, california institute of technology.
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



# APR. 02, 2015    add the ability to extract Restituted Orbit
#                  by Cunren Liang
#
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from xml.etree.ElementTree import ElementTree
import datetime
import isceobj
from isceobj.Scene.Frame import Frame
from isceobj.Planet.Planet import Planet
from isceobj.Orbit.Orbit import StateVector, Orbit
from isceobj.Orbit.OrbitExtender import OrbitExtender
from isceobj.Planet.AstronomicalHandbook import Const
from iscesys.Component.Component import Component
from iscesys.DateTimeUtil.DateTimeUtil import DateTimeUtil as DTUtil
import os
import numpy as np

sep = "\n"
tab = "    "
lookMap = { 'RIGHT' : -1,
            'LEFT' : 1}

class Sentinel1A(Component):
    """
        A Class representing RadarSAT 2 data
    """
    def __init__(self):
        Component.__init__(self)        
        self.xml = None
        self.tiff = None
        self.orbitfile = None
        self.output = None
        self.frame = Frame()
        self.frame.configure()
    
        self._xml_root=None
        self.descriptionOfVariables = {}
        self.dictionaryOfVariables = {'XML': ['self.xml','str','mandatory'],
                                      'TIFF': ['self.tiff','str','mandatory'],
                                      'ORBITFILE' : ['self.orbitfile', 'str', 'optional'],
                                      'OUTPUT': ['self.output','str','optional']}
        
                                               
    def getFrame(self):
        return self.frame
    
    def parse(self):
        try:
            fp = open(self.xml,'r')
        except IOError as strerr:
            print("IOError: %s" % strerr)
            return
        self._xml_root = ElementTree(file=fp).getroot()                     
#        self.product.set_from_etnode(self._xml_root)
        self.populateMetadata()
        
        fp.close()

    def grab_from_xml(self, path):
        try:
            res = self._xml_root.find(path).text
        except:
            raise Exception('Tag= %s not found'%(path))

        if res is None:
            raise Exception('Tag = %s not found'%(path))

        return res

    def convertToDateTime(self, string):
        dt = datetime.datetime.strptime(string,"%Y-%m-%dT%H:%M:%S.%f")
        return dt

    
    def populateMetadata(self):
        """
            Create metadata objects from the metadata files
        """
        ####Set each parameter one - by - one
        mission = self.grab_from_xml('adsHeader/missionId')
        swath = self.grab_from_xml('adsHeader/swath')
        polarization = self.grab_from_xml('adsHeader/polarisation')

        frequency = float(self.grab_from_xml('generalAnnotation/productInformation/radarFrequency'))
        passDirection = self.grab_from_xml('generalAnnotation/productInformation/pass')

        rangePixelSize = float(self.grab_from_xml('imageAnnotation/imageInformation/rangePixelSpacing'))
        azimuthPixelSize = float(self.grab_from_xml('imageAnnotation/imageInformation/azimuthPixelSpacing'))
        rangeSamplingRate = Const.c/(2.0*rangePixelSize)
        prf = 1.0/float(self.grab_from_xml('imageAnnotation/imageInformation/azimuthTimeInterval'))

        lines = int(self.grab_from_xml('imageAnnotation/imageInformation/numberOfLines'))
        samples = int(self.grab_from_xml('imageAnnotation/imageInformation/numberOfSamples'))

        startingRange = float(self.grab_from_xml('imageAnnotation/imageInformation/slantRangeTime'))*Const.c/2.0
        incidenceAngle = float(self.grab_from_xml('imageAnnotation/imageInformation/incidenceAngleMidSwath'))
        dataStartTime = self.convertToDateTime(self.grab_from_xml('imageAnnotation/imageInformation/productFirstLineUtcTime'))
        dataStopTime = self.convertToDateTime(self.grab_from_xml('imageAnnotation/imageInformation/productLastLineUtcTime'))


        pulseLength = float(self.grab_from_xml('generalAnnotation/downlinkInformationList/downlinkInformation/downlinkValues/txPulseLength'))
        chirpSlope = float(self.grab_from_xml('generalAnnotation/downlinkInformationList/downlinkInformation/downlinkValues/txPulseRampRate'))
        pulseBandwidth = pulseLength * chirpSlope

        ####Sentinel is always right looking
        lookSide = -1
        facility = 'EU'
        version = '1.0'


#        height = self.product.imageGenerationParameters.sarProcessingInformation._satelliteHeight

        ####Populate platform
        platform = self.frame.getInstrument().getPlatform()
        platform.setPlanet(Planet(pname="Earth"))
        platform.setMission(mission)
        platform.setPointingDirection(lookSide)
        platform.setAntennaLength(2*azimuthPixelSize)

        ####Populate instrument
        instrument = self.frame.getInstrument()
        instrument.setRadarFrequency(frequency)
        instrument.setPulseRepetitionFrequency(prf)
        instrument.setPulseLength(pulseLength)
        instrument.setChirpSlope(pulseBandwidth/pulseLength)
        instrument.setIncidenceAngle(incidenceAngle)
        #self.frame.getInstrument().setRangeBias(0)
        instrument.setRangePixelSize(rangePixelSize)
        instrument.setRangeSamplingRate(rangeSamplingRate)
        instrument.setBeamNumber(swath)
        instrument.setPulseLength(pulseLength)


        #Populate Frame
        #self.frame.setSatelliteHeight(height)
        self.frame.setSensingStart(dataStartTime)
        self.frame.setSensingStop(dataStopTime)
        diffTime = DTUtil.timeDeltaToSeconds(dataStopTime - dataStartTime)/2.0
        sensingMid = dataStartTime + datetime.timedelta(microseconds=int(diffTime*1e6))
        self.frame.setSensingMid(sensingMid)
        self.frame.setPassDirection(passDirection)
        self.frame.setPolarization(polarization) 
        self.frame.setStartingRange(startingRange)
        self.frame.setFarRange(startingRange + (samples-1)*rangePixelSize)
        self.frame.setNumberOfLines(lines)
        self.frame.setNumberOfSamples(samples)
        self.frame.setProcessingFacility(facility)
        self.frame.setProcessingSoftwareVersion(version)
        
        self.frame.setPassDirection(passDirection)

        ResOrbFlag = self.extractResOrbit()
        if ResOrbFlag == 0:
            print("cannot find POD Restituted Orbit, using orbit coming along with SLC")
            self.extractOrbit()

######################################################################################
    def extractResOrbit(self):
        #read ESA's POD Restituted Orbit by Cunren Liang, APR. 2, 2015.
        import pathlib

        useResOrbFlag = 0

        ResOrbDir = os.environ.get('RESORB')
        if ResOrbDir !=  None:
            print("Trying to find POD Restituted Orbit...")
            #get start time and stop time of the SLC data from data xml file
            dataStartTime = self.convertToDateTime(self.grab_from_xml('imageAnnotation/imageInformation/productFirstLineUtcTime'))
            dataStopTime = self.convertToDateTime(self.grab_from_xml('imageAnnotation/imageInformation/productLastLineUtcTime'))

            #RESORB has an orbit every 10 sec, extend the start and stop time by 50 sec.
            dataStartTimeExt = dataStartTime - datetime.timedelta(0, 50)
            dataStopTimeExt =  dataStopTime + datetime.timedelta(0, 50)

            ###########################
            #deal with orbit directory
            ###########################

            orbList = pathlib.Path(ResOrbDir).glob('**/*.EOF')
            for orb in orbList:
                #save full path
                orb = str(orb)
                orbx = orb
                
                #get orbit file name
                orb = os.path.basename(os.path.normpath(orb))
                #print("{0}".format(orb))
                
                #get start and stop time of the orbit file
                orbStartTime = datetime.datetime.strptime(orb[42:57],"%Y%m%dT%H%M%S")
                orbStopTime = datetime.datetime.strptime(orb[58:73],"%Y%m%dT%H%M%S")
                #print("{0}, {1}".format(orbStartTime, orbStopTime))

                if dataStartTimeExt >= orbStartTime and dataStopTimeExt <= orbStopTime:
                    try:
                        orbfp = open(orbx,'r')
                    except IOError as strerr:
                        print("IOError: %s" % strerr)
                        return useResOrbFlag
                    orbxml = ElementTree(file=orbfp).getroot()
                    print('using orbit file: {0}'.format(orbx))

                    frameOrbit = Orbit()
                    frameOrbit.setOrbitSource('Restituted')

                    #find the orbit data from the file, and use them
                    node = orbxml.find('Data_Block/List_of_OSVs') #note upper case and lower case
                    for child in node.getchildren():
                        timestamp = self.convertToDateTime(child.find('UTC').text[4:])
                        if timestamp < dataStartTimeExt:
                            continue
                        if timestamp > dataStopTimeExt:
                            break

                        pos = []
                        vel = []
                        for tag in ['X','Y','Z']:
                            pos.append(float(child.find(tag).text))
                            vel.append(float(child.find('V' + tag).text))

                        vec = StateVector()
                        vec.setTime(timestamp)
                        vec.setPosition(pos)
                        vec.setVelocity(vel)
                        frameOrbit.addStateVector(vec)

                    #there is no need to extend the orbit any longer
                    #planet = self.frame.instrument.platform.planet
                    #orbExt = OrbitExtender(planet=planet)
                    #orbExt.configure()
                    #newOrb = orbExt.extendOrbit(frameOrbit)

                    self.frame.getOrbit().setOrbitSource('Restituted')
                    for sv in frameOrbit:
                        self.frame.getOrbit().addStateVector(sv)

                    orbfp.close()
                    useResOrbFlag = 1
                    break
        return useResOrbFlag
######################################################################################
        
    def extractOrbit(self):
        '''
        Extract orbit information from xml node.
        '''

        node = self._xml_root.find('generalAnnotation/orbitList')
        frameOrbit = Orbit()
        frameOrbit.setOrbitSource('Header')

        for child in node.getchildren():
            timestamp = self.convertToDateTime(child.find('time').text)
            pos = []
            vel = []
            posnode = child.find('position')
            velnode = child.find('velocity')
            for tag in ['x','y','z']:
                pos.append(float(posnode.find(tag).text))

            for tag in ['x','y','z']:
                vel.append(float(velnode.find(tag).text))

            vec = StateVector()
            vec.setTime(timestamp)
            vec.setPosition(pos)
            vec.setVelocity(vel)
            frameOrbit.addStateVector(vec)

        planet = self.frame.instrument.platform.planet
        orbExt = OrbitExtender(planet=planet)
        orbExt.configure()
        newOrb = orbExt.extendOrbit(frameOrbit)

        self.frame.getOrbit().setOrbitSource('Header')
        for sv in newOrb:
            self.frame.getOrbit().addStateVector(sv)

        return

    def extractPreciseOrbit(self):
        '''
        Extract precise orbit from given Orbit file.
        '''
        try:
            fp = open(self.orbitfile,'r')
        except IOError as strerr:
            print("IOError: %s" % strerr)
            return

        _xml_root = ElementTree(file=fp).getroot()
       
        node = _xml_root.find('Data_Block/List_of_OSVs')

        orb = Orbit()
        orb.configure()

        margin = datetime.timedelta(seconds=40.0)
        tstart = self.frame.getSensingStart() - margin
        tend = self.frame.getSensingStop() + margin

        for child in node.getchildren():
            timestamp = self.convertToDateTime(child.find('UTC').text[4:])

            if (timestamp >= tstart) and (timestamp < tend):

                pos = [] 
                vel = []

                for tag in ['VX','VY','VZ']:
                    vel.append(float(child.find(tag).text))

                for tag in ['X','Y','Z']:
                    pos.append(float(child.find(tag).text))

                vec = StateVector()
                vec.setTime(timestamp)
                vec.setPosition(pos)
                vec.setVelocity(vel)
                orb.addStateVector(vec)

        fp.close()

        self.frame.getOrbit().setOrbitSource('Header')
        for sv in orb:
            self.frame.getOrbit().addStateVector(sv)

        return

    def extractImage(self):
        """
           Use gdal python bindings to extract image
        """
        try:
            from osgeo import gdal
        except ImportError:
            raise Exception('GDAL python bindings not found. Need this for RSAT2/ TandemX / Sentinel1A.')

        self.parse()
        width = self.frame.getNumberOfSamples()
        lgth = self.frame.getNumberOfLines()

        src = gdal.Open(self.tiff.strip(), gdal.GA_ReadOnly)
        band = src.GetRasterBand(1)
        fid = open(self.output, 'wb')
        for ii in range(lgth):
            data = band.ReadAsArray(0,ii,width,1)
            data.tofile(fid)

        fid.close()
        src = None
        band = None

        ####
        slcImage = isceobj.createSlcImage()
        slcImage.setByteOrder('l')
        slcImage.setFilename(self.output)
        slcImage.setAccessMode('read')
        slcImage.setWidth(self.frame.getNumberOfSamples())
        slcImage.setLength(self.frame.getNumberOfLines())
        slcImage.setXmin(0)
        slcImage.setXmax(self.frame.getNumberOfSamples())
        self.frame.setImage(slcImage)

    def extractDoppler(self):
        '''
        self.parse()
        Extract doppler information as needed by mocomp
        '''
#        ins = self.frame.getInstrument()
#        dc = self.product.imageGenerationParameters.dopplerCentroid
        quadratic = {}

#        r0 = self.frame.startingRange
#        fs = ins.getRangeSamplingRate()
#        tNear = 2*r0/Const.c

#        tMid = tNear + 0.5*self.frame.getNumberOfSamples()/fs
#        t0 = dc.dopplerCentroidReferenceTime
#        poly = dc.dopplerCentroidCoefficients
       
#        fd_mid = 0.0
#        for kk in range(len(poly)):
#            fd_mid += poly[kk] * (tMid - t0)**kk
        
#        quadratic['a'] = fd_mid / ins.getPulseRepetitionFrequency()
        quadratic['a'] = 0.
        quadratic['b'] = 0.
        quadratic['c'] = 0.
        return quadratic

