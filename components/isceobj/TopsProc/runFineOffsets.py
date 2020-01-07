#
# Author: Piyush Agram
# Copyright 2016
#


import numpy as np 
import os
import isceobj
import datetime
import sys
import logging
from isceobj.Util.decorators import use_api

logger = logging.getLogger('isce.topsinsar.fineoffsets')

def runGeo2rdr(info, rdict, misreg_az=0.0, misreg_rg=0.0):
    from zerodop.geo2rdr import createGeo2rdr
    from isceobj.Planet.Planet import Planet

    latImage = isceobj.createImage()
    latImage.load(rdict['lat'] + '.xml')
    latImage.setAccessMode('READ')
    latImage.createImage()

    lonImage = isceobj.createImage()
    lonImage.load(rdict['lon'] + '.xml')
    lonImage.setAccessMode('READ')
    lonImage.createImage()

    demImage = isceobj.createImage()
    demImage.load(rdict['hgt'] + '.xml')
    demImage.setAccessMode('READ')
    demImage.createImage()

    delta = datetime.timedelta(seconds=misreg_az)
    logger.info('Additional time offset applied in geo2rdr: {0} secs'.format(misreg_az))
    logger.info('Additional range offset applied in geo2rdr: {0} m'.format(misreg_rg))


    #####Run Geo2rdr
    planet = Planet(pname='Earth')
    grdr = createGeo2rdr()
    grdr.configure()

    grdr.slantRangePixelSpacing = info.rangePixelSize
    grdr.prf = 1.0 / info.azimuthTimeInterval
    grdr.radarWavelength = info.radarWavelength
    grdr.orbit = info.orbit
    grdr.width = info.numberOfSamples
    grdr.length = info.numberOfLines
    grdr.demLength = demImage.getLength()
    grdr.demWidth = demImage.getWidth()
    grdr.wireInputPort(name='planet', object=planet)
    grdr.numberRangeLooks = 1
    grdr.numberAzimuthLooks = 1
    grdr.lookSide = -1  
    grdr.setSensingStart(info.sensingStart - delta)
    grdr.rangeFirstSample = info.startingRange - misreg_rg
    grdr.dopplerCentroidCoeffs = [0.]  ###Zero doppler

    grdr.rangeOffsetImageName = rdict['rangeOffName']
    grdr.azimuthOffsetImageName = rdict['azOffName']
    grdr.demImage = demImage
    grdr.latImage = latImage
    grdr.lonImage = lonImage

    grdr.geo2rdr()

    return


def runFineOffsets(self):
    '''
    Estimate offsets using geometry
    '''

    ##Catalog
    catalog = isceobj.Catalog.createCatalog(self._insar.procDoc.name)

    misreg_az = self._insar.slaveTimingCorrection
    catalog.addItem('Initial slave azimuth timing correction', misreg_az, 'fineoff')

    misreg_rg = self._insar.slaveRangeCorrection
    catalog.addItem('Initial slave range timing correction', misreg_rg, 'fineoff')

    swathList = self._insar.getValidSwathList(self.swaths)

    for swath in swathList:

        ##Load slave metadata
        slave = self._insar.loadProduct( os.path.join(self._insar.slaveSlcProduct, 'IW{0}.xml'.format(swath)))

        ###Offsets output directory
        outdir = os.path.join(self._insar.fineOffsetsDirname, 'IW{0}'.format(swath))

        if not os.path.isdir(outdir):
            os.makedirs(outdir)


        ###Burst indices w.r.t master
        minBurst, maxBurst = self._insar.commonMasterBurstLimits(swath-1)
        geomDir = os.path.join(self._insar.geometryDirname, 'IW{0}'.format(swath))

        if minBurst == maxBurst:
            print('Skipping processing of swath {0}'.format(swath))
            continue


        slaveBurstStart = self._insar.commonBurstStartSlaveIndex[swath-1]

        catalog.addItem('Number of bursts - IW{0}'.format(swath), maxBurst - minBurst, 'fineoff')

        for mBurst in range(minBurst, maxBurst):

            ###Corresponding slave burst
            sBurst = slaveBurstStart + (mBurst - minBurst)
            burst = slave.bursts[sBurst]

            logger.info('IW{3} - Burst {1} of master matched with Burst {2} of slave'.format(mBurst-minBurst, mBurst, sBurst, swath))
            ####Generate offsets for top burst
            rdict = {'lat': os.path.join(geomDir,'lat_%02d.rdr'%(mBurst+1)),
                     'lon': os.path.join(geomDir,'lon_%02d.rdr'%(mBurst+1)),
                     'hgt': os.path.join(geomDir,'hgt_%02d.rdr'%(mBurst+1)),
                     'rangeOffName': os.path.join(outdir, 'range_%02d.off'%(mBurst+1)),
                     'azOffName': os.path.join(outdir, 'azimuth_%02d.off'%(mBurst+1))}
        
            runGeo2rdr(burst, rdict, misreg_az=misreg_az, misreg_rg=misreg_rg)

