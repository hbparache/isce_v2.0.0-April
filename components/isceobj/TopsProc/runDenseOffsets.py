#
# Author: Joshua Cohen
# Copyright 2016
# Based on Piyush Agram's denseOffsets.py script
#

import os
import isce
import isceobj
import logging

from mroipac.ampcor.DenseAmpcor import DenseAmpcor
from isceobj.Util.decorators import use_api

logger = logging.getLogger('isce.insar.DenseOffsets')

def runDenseOffsets(self):
    '''
    Estimate dense offset field between merged master bursts and slave bursts.
    '''

    os.environ['VRT_SHARED_SOURCE'] = "0"

    if not self.doDenseOffsets:
        print('Dense offsets not requested. Skipping ....')
        return


    print('\n============================================================')
    print('Configuring DenseAmpcor object for processing...\n')

    ### Determine appropriate filenames
    mf = 'master.slc'
    sf = 'slave.slc'
    if not ((self.numberRangeLooks == 1) and (self.numberAzimuthLooks==1)):
        mf += '.full'
        sf += '.full'
    master = os.path.join(self._insar.mergedDirname, mf)
    slave = os.path.join(self._insar.mergedDirname, sf)

    ### Load the master object
    m = isceobj.createSlcImage()
    m.load(master + '.xml')
    m.setAccessMode('READ')
#    m.createImage()

    ### Load the slave object
    s = isceobj.createSlcImage()
    s.load(slave + '.xml')
    s.setAccessMode('READ')
#    s.createImage()
    
    width = m.getWidth()
    length = m.getLength()

    objOffset = DenseAmpcor(name='dense')
    objOffset.configure()

#    objOffset.numberThreads = 1
    ### Configure dense Ampcor object
    print('\nMaster frame: %s' % (mf))
    print('Slave frame: %s' % (sf))
    print('Main window size width: %d' % (self.winwidth))
    print('Main window size height: %d' % (self.winhgt))
    print('Search window size width: %d' % (self.srcwidth))
    print('Search window size height: %d' % (self.srchgt))
    print('Skip sample across: %d' % (self.skipwidth))
    print('Skip sample down: %d' % (self.skiphgt))
    print('Field margin: %d' % (self.margin))
    print('Oversampling factor: %d' % (self.oversample))
    print('Gross offset across: %d' % (self.rgshift))
    print('Gross offset down: %d\n' % (self.azshift))

    objOffset.setWindowSizeWidth(self.winwidth)
    objOffset.setWindowSizeHeight(self.winhgt)
    objOffset.setSearchWindowSizeWidth(self.srcwidth)
    objOffset.setSearchWindowSizeHeight(self.srchgt)
    objOffset.skipSampleAcross = self.skipwidth
    objOffset.skipSampleDown = self.skiphgt
    objOffset.oversamplingFactor = self.oversample
    objOffset.setAcrossGrossOffset(self.rgshift)
    objOffset.setDownGrossOffset(self.azshift)
    
    objOffset.setFirstPRF(1.0)
    objOffset.setSecondPRF(1.0)
    if m.dataType.startswith('C'):
        objOffset.setImageDataType1('mag')
    else:
        objOffset.setImageDataType1('real')
    if s.dataType.startswith('C'):
        objOffset.setImageDataType2('mag')
    else:
        objOffset.setImageDataType2('real')

    objOffset.offsetImageName = os.path.join(self._insar.mergedDirname, self._insar.offsetfile)
    objOffset.snrImageName = os.path.join(self._insar.mergedDirname, self._insar.snrfile)

    print('Output dense offsets file name: %s' % (objOffset.offsetImageName))
    print('Output SNR file name: %s' % (objOffset.snrImageName))
    print('\n======================================')
    print('Running dense ampcor...')
    print('======================================\n')
    
    objOffset.denseampcor(m, s) ### Where the magic happens...

    ### Store params for later
    self._insar.offset_width = objOffset.offsetCols
    self._insar.offset_length = objOffset.offsetLines
    self._insar.offset_top = objOffset.locationDown[0][0]
    self._insar.offset_left = objOffset.locationAcross[0][0]

#    m.finalizeImage()
#    s.finalizeImage()

if __name__ == '__main__' :
    '''
    Default routine to plug master.slc.full/slave.slc.full into
    Dense Offsets Ampcor module.
    '''

    main()
