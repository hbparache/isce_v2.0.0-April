#
# Author: Piyush Agram
# Copyright 2016
#


import numpy as np 
import os
import isceobj
import datetime
import logging
from isceobj.Util.ImageUtil import ImageLib as IML
from isceobj.Util.decorators import use_api


def mergeBurstsVirtual(frame, fileList, outfile, validOnly=True):
    '''
    Merging using VRTs.
    '''
    
    from .VRTManager import Swath, VRTConstructor


    swaths = [Swath(x) for x in frame]

    ###Identify the 4 corners and dimensions
    topSwath = min(swaths, key = lambda x: x.sensingStart)
    botSwath = max(swaths, key = lambda x: x.sensingStop)
    leftSwath = min(swaths, key = lambda x: x.nearRange)
    rightSwath = max(swaths, key = lambda x: x.farRange)


    totalWidth = int( np.round((rightSwath.farRange - leftSwath.nearRange)/leftSwath.dr + 1))
    totalLength = int(np.round((botSwath.sensingStop - topSwath.sensingStart).total_seconds()/topSwath.dt + 1 ))


    ###Determine number of bands and type
    img  = isceobj.createImage()
    img.load( fileList[0][0] + '.xml')
    bands = img.bands 
    dtype = img.dataType
    img.filename = outfile


    #####Start the builder
    ###Now start building the VRT and then render it
    builder = VRTConstructor(totalLength, totalWidth)
    builder.setReferenceTime( topSwath.sensingStart)
    builder.setReferenceRange( leftSwath.nearRange)
    builder.setTimeSpacing( topSwath.dt )
    builder.setRangeSpacing( leftSwath.dr)
    builder.setDataType( dtype.upper())

    builder.initVRT()


    ####Render XML and default VRT. VRT will be overwritten.
    img.width = totalWidth
    img.length =totalLength
    img.renderHdr()


    for bnd in range(1,bands+1):
        builder.initBand(band = bnd)

        for ind, swath in enumerate(swaths):
            ####Relative path
            relfilelist = [os.path.relpath(x, 
                os.path.dirname(outfile))  for x in fileList[ind]]

            builder.addSwath(swath, relfilelist, band=bnd, validOnly=validOnly)

        builder.finishBand()
    builder.finishVRT()

    with open(outfile + '.vrt', 'w') as fid:
        fid.write(builder.vrt)



def mergeBursts(frame, fileList, outfile,
        method='top'):
    '''
    Merge burst products into single file.
    Simple numpy based stitching
    '''

    ###Check against metadata
    if frame.numberOfBursts != len(fileList):
        print('Warning : Number of burst products does not appear to match number of bursts in metadata')


    t0 = frame.bursts[0].sensingStart
    dt = frame.bursts[0].azimuthTimeInterval
    width = frame.bursts[0].numberOfSamples

    #######
    tstart = frame.bursts[0].sensingStart 
    tend = frame.bursts[-1].sensingStop
    nLines = int( np.round((tend - tstart).total_seconds() / dt)) + 1
    print('Expected total nLines: ', nLines)


    img = isceobj.createImage()
    img.load( fileList[0] + '.xml')
    bands = img.bands
    scheme = img.scheme
    npType = IML.NUMPY_type(img.dataType)

    azMasterOff = []
    for index in range(frame.numberOfBursts):
        burst = frame.bursts[index]
        soff = burst.sensingStart + datetime.timedelta(seconds = (burst.firstValidLine*dt)) 
        start = int(np.round((soff - tstart).total_seconds() / dt))
        end = start + burst.numValidLines

        azMasterOff.append([start,end])

        print('Burst: ', index, [start,end])

        if index == 0:
            linecount = start

    outMap = IML.memmap(outfile, mode='write', nchannels=bands,
            nxx=width, nyy=nLines, scheme=scheme, dataType=npType)

    for index in range(frame.numberOfBursts):
        curBurst = frame.bursts[index]
        curLimit = azMasterOff[index]

        curMap = IML.mmapFromISCE(fileList[index], logging)

        #####If middle burst
        if index > 0:
            topBurst = frame.bursts[index-1]
            topLimit = azMasterOff[index-1]
            topMap = IML.mmapFromISCE(fileList[index-1], logging)

            olap = topLimit[1] - curLimit[0]

            if olap <= 0:
                raise Exception('No Burst Overlap')


            for bb in range(bands):
                topData =  topMap.bands[bb][topBurst.firstValidLine: topBurst.firstValidLine + topBurst.numValidLines,:]

                curData =  curMap.bands[bb][curBurst.firstValidLine: curBurst.firstValidLine + curBurst.numValidLines,:]

                im1 = topData[-olap:,:]
                im2 = curData[:olap,:]

                if method=='avg':
                    data = 0.5*(im1 + im2)
                elif method == 'top':
                    data = im1
                elif method == 'bot':
                    data = im2
                else:
                    raise Exception('Method should be top/bot/avg')

                outMap.bands[bb][linecount:linecount+olap,:] = data

            tlim = olap
        else:
            tlim = 0

        linecount += tlim
            
        if index != (frame.numberOfBursts-1):
            botBurst = frame.bursts[index+1]
            botLimit = azMasterOff[index+1]
            
            olap = curLimit[1] - botLimit[0]

            if olap < 0:
                raise Exception('No Burst Overlap')

            blim = botLimit[0] - curLimit[0]
        else:
            blim = curBurst.numValidLines
       
        lineout = blim - tlim
        
        for bb in range(bands):
            curData =  curMap.bands[bb][curBurst.firstValidLine: curBurst.firstValidLine + curBurst.numValidLines,:]
            outMap.bands[bb][linecount:linecount+lineout,:] = curData[tlim:blim,:] 

        linecount += lineout
        curMap = None
        topMap = None

    IML.renderISCEXML(outfile, bands,
            nLines, width,
            img.dataType, scheme)

    oimg = isceobj.createImage()
    oimg.load(outfile + '.xml')
    oimg.imageType = img.imageType
    oimg.renderHdr()
    try:
        outMap.bands[0].base.base.flush()
    except:
        pass


def multilook(infile, outname=None, alks=5, rlks=15):
    '''
    Take looks.
    '''

    from mroipac.looks.Looks import Looks

    print('Multilooking {0} ...'.format(infile))

    inimg = isceobj.createImage()
    inimg.load(infile + '.xml')

    if outname is None:
        spl = os.path.splitext(inimg.filename)
        ext = '.{0}alks_{1}rlks'.format(alks, rlks)
        outname = spl[0] + ext + spl[1]

    lkObj = Looks()
    lkObj.setDownLooks(alks)
    lkObj.setAcrossLooks(rlks)
    lkObj.setInputImage(inimg)
    lkObj.setOutputFilename(outname)
    lkObj.looks()

    return outname

def runMergeBursts(self):
    '''
    Merge burst products to make it look like stripmap.
    Currently will merge interferogram, lat, lon, z and los.
    '''
    virtual = self.useVirtualFiles


    swathList = self._insar.getValidSwathList(self.swaths)
    frames=[]
    intList = []
    corList = []
    latList = []
    lonList = []
    hgtList = []
    losList = []
    mslcList = []
    sslcList = []

    for swath in swathList:
        minBurst, maxBurst = self._insar.commonMasterBurstLimits(swath-1)

        if minBurst==maxBurst:
            print('Skipping processing of swath {0}'.format(swath))
            continue

        ifg = self._insar.loadProduct( os.path.join(self._insar.fineIfgDirname, 'IW{0}.xml'.format(swath)))
        frames.append(ifg)

        ####Geometry products
        latList.append([os.path.join(self._insar.geometryDirname, 'IW{0}'.format(swath), 'lat_%02d.rdr'%(x+1)) for x in range(minBurst, maxBurst)])
        lonList.append([os.path.join(self._insar.geometryDirname, 'IW{0}'.format(swath), 'lon_%02d.rdr'%(x+1)) for x in range(minBurst, maxBurst)])
        hgtList.append([os.path.join(self._insar.geometryDirname, 'IW{0}'.format(swath), 'hgt_%02d.rdr'%(x+1)) for x in range(minBurst, maxBurst)])
        losList.append([os.path.join(self._insar.geometryDirname, 'IW{0}'.format(swath), 'los_%02d.rdr'%(x+1)) for x in range(minBurst, maxBurst)])

        mslcList.append([os.path.join(self._insar.masterSlcProduct, 'IW{0}'.format(swath), 'burst_%02d.slc'%(x+1)) for x in range(minBurst, maxBurst)])

        sslcList.append([os.path.join(self._insar.fineCoregDirname, 'IW{0}'.format(swath), 'burst_%02d.slc'%(x+1)) for x in range(minBurst, maxBurst)])
        if self.doInSAR:
            ####Interferogram
            intList.append([x.image.filename for x in ifg.bursts])
            corList.append([os.path.join(self._insar.fineIfgDirname, 'IW{0}'.format(swath),  'burst_%02d.cor'%(x+1)) for x in range(minBurst, maxBurst)])


    mergedir = self._insar.mergedDirname
    if not os.path.isdir(mergedir):
        os.makedirs(mergedir)

    
    suffix = '.full'
    if (self.numberRangeLooks == 1) and (self.numberAzimuthLooks==1):
        suffix=''


    ####Virtual flag is ignored for multi-swath data
    if (not virtual) and (len(frames) == 1):

        if self.doInSAR:
            ####Merge interferograms
            mergeBursts(frames[0], intList[0], os.path.join(mergedir, self._insar.mergedIfgname+suffix))
            mergeBursts(frames[0], corList[0], os.path.join(mergedir, self._insar.correlationFilename+suffix))

        ###Merge LOS
        mergeBursts(frames[0], losList[0], os.path.join(mergedir, self._insar.mergedLosName+suffix))

        ###Merge lat, lon, z
        mergeBursts(frames[0], latList[0], os.path.join(mergedir, 'lat.rdr'+suffix))
        mergeBursts(frames[0], lonList[0], os.path.join(mergedir, 'lon.rdr'+suffix))
        mergeBursts(frames[0], hgtList[0], os.path.join(mergedir, 'z.rdr'+suffix))

        ### Merge the SLCs
        mergeBursts(frames[0], mslcList[0], os.path.join(mergedir, 'master.slc'+suffix))
        mergeBursts(frames[0], sslcList[0], os.path.join(mergedir, 'slave.slc'+suffix))


    else:
        if (not virtual):
            print('User requested for multi-swath stitching.')
            print('Virtual files are the only option for this.')
            print('Proceeding with virtual files.')


        if self.doInSAR:
            ####Merge interferograms
            mergeBurstsVirtual(frames, intList, os.path.join(mergedir, self._insar.mergedIfgname+suffix))
            mergeBurstsVirtual(frames, corList, os.path.join(mergedir, self._insar.correlationFilename+suffix))

        ###Merge LOS
        mergeBurstsVirtual(frames, losList, os.path.join(mergedir, self._insar.mergedLosName+suffix), validOnly=False)

        ###Merge lat, lon, z
        mergeBurstsVirtual(frames, latList, os.path.join(mergedir, 'lat.rdr'+suffix), validOnly=False)
        mergeBurstsVirtual(frames, lonList, os.path.join(mergedir, 'lon.rdr'+suffix), validOnly=False)
        mergeBurstsVirtual(frames, hgtList, os.path.join(mergedir, 'z.rdr'+suffix), validOnly=False)


        ####Merge the SLCs
        mergeBurstsVirtual(frames, mslcList, os.path.join(mergedir, 'master.slc'+suffix))
        mergeBurstsVirtual(frames, sslcList, os.path.join(mergedir, 'slave.slc'+suffix))


    if suffix not in ['',None]:
        if self.doInSAR:
            multilook(os.path.join(mergedir, self._insar.mergedIfgname+suffix),
              outname = os.path.join(mergedir, self._insar.mergedIfgname),
              alks = self.numberAzimuthLooks, rlks=self.numberRangeLooks)

            multilook(os.path.join(mergedir, self._insar.correlationFilename+suffix),
              outname = os.path.join(mergedir, self._insar.correlationFilename),
              alks = self.numberAzimuthLooks, rlks=self.numberRangeLooks)

            multilook(os.path.join(mergedir, self._insar.mergedLosName+suffix),
              outname = os.path.join(mergedir, self._insar.mergedLosName),
              alks = self.numberAzimuthLooks, rlks=self.numberRangeLooks)

    else:
        print('Skipping multi-looking ....')

if __name__ == '__main__' :
    '''
    Merge products burst-by-burst.
    '''

    main()
