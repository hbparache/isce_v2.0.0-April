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
# Author: Brett George
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import stdproc
from stdproc.rectify.geocode.Geocodable import Geocodable
from zerodop.geozero import createGeozero
import isceobj
import iscesys
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
import os
from isceobj.Constants import SPEED_OF_LIGHT
import datetime
import numpy as np


logger = logging.getLogger('isce.insar.runGeocode')

def runGeocode(self, prodlist, unwrapflag, bbox):
    '''Generalized geocoding of all the files listed above.'''
    from isceobj.Catalog import recordInputsAndOutputs
    logger.info("Geocoding Image")
    insar = self.insar

    if isinstance(prodlist,str):
        from isceobj.Util.StringUtils import StringUtils as SU
        tobeGeocoded = SU.listify(prodlist)
    else:
        tobeGeocoded = prodlist

    #####Remove the unwrapped interferogram if no unwrapping is done
    if not unwrapflag:
        try:
            tobeGeocoded.remove(insar.unwrappedIntFilename)
        except ValueError:
            pass

    print('Number of products to geocode: ', len(tobeGeocoded))

    frame = insar.masterFrame
    slc = insar.formSLC1
    planet = frame._instrument._platform._planet
    prf = frame._instrument.getPulseRepetitionFrequency()
    wvl = frame._instrument.getRadarWavelength()
    lookSide = frame._instrument._platform.pointingDirection
    sensingStart = insar.formSLC1.slcSensingStart
    delr = 0.5 * SPEED_OF_LIGHT / frame.rangeSamplingRate
    startingRange = slc.startingRange

    if bbox is None:
        snwe = insar.topo.snwe
    else:
        snwe = list(bbox)
        if len(snwe) != 4:
            raise ValueError('Bounding box should be a list/tuple of length 4')

    #####Geocode one by one
    first = False
    ge = Geocodable()
    for prod in tobeGeocoded:
        objGeo = createGeozero()
        objGeo.configure()

        ####IF statements to check for user configuration
        if objGeo.minimumLatitude is None:
            objGeo.minimumLatitude = snwe[0]

        if objGeo.maximumLatitude is None:
            objGeo.maximumLatitude = snwe[1]

        if objGeo.minimumLongitude is None:
            objGeo.minimumLongitude = snwe[2]

        if objGeo.maximumLongitude is None:
            objGeo.maximumLongitude = snwe[3]

        if objGeo.demCropFilename is None:
            objGeo.demCropFilename = insar.demCropFilename


        objGeo.orbit = frame.orbit

        if objGeo.numberRangeLooks is None:
            objGeo.numberRangeLooks = insar.numberRangeLooks

        if objGeo.numberAzimuthLooks is None:
            objGeo.numberAzimuthLooks = insar.numberAzimuthLooks

        #create the instance of the input image and the appropriate
        #geocode method
        inImage,method = ge.create(prod)
        if objGeo.method is None:
            objGeo.method = method

        if(inImage):
            #demImage = isceobj.createDemImage()
            #IU.copyAttributes(insar.demImage, demImage)
            demImage = insar.demImage.clone()

            objGeo.slantRangePixelSpacing = delr
            objGeo.radarWavelength = wvl
            objGeo.width = inImage.getWidth()
            objGeo.length = inImage.getLength()
            objGeo.lookSide = lookSide
            objGeo.prf = prf

            objGeo.setSensingStart(sensingStart + datetime.timedelta(seconds=(objGeo.numberAzimuthLooks-1)/(2*objGeo.prf)))
            objGeo.rangeFirstSample = startingRange + delr * (objGeo.numberRangeLooks-1) /2

            #print('method ', objGeo.method)
            #print('prf ', objGeo.prf)
            #print('delr ', objGeo.slantRangePixelSpacing)
            #print('azlooks ', objGeo.numberAzimuthLooks)
            #print('rglooks ', objGeo.numberRangeLooks)
            #print('tstart ', objGeo.sensingStart)
            #print('rstart ', objGeo.rangeFirstSample)

            objGeo.demInterpolationMethod = 'BIQUINTIC'
            objGeo.geoFilename = inImage.filename + '.geo'

            objGeo.wireInputPort(name='dem', object=demImage)
            objGeo.wireInputPort(name='planet', object=planet)
            objGeo.wireInputPort(name='tobegeocoded', object=inImage)

            ####Doppler coefficients
            dop = frame._dopplerVsPixel[::-1]
            xx = np.linspace(0, (slc.slcImage.width-1), num=len(dop)+ 1)
            x = (slc.startingRange - frame.startingRange)/objGeo.slantRangePixelSpacing + xx 
            v = np.polyval(dop, x)
            p = np.polyfit(xx, v, len(dop)-1)[::-1]

            pp = [x/prf for x in p]
            objGeo.dopplerCentroidCoeffs = pp

            objGeo.geocode()
