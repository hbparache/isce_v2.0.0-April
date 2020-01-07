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




import numpy as np
import isce
from isceobj import createImage
import os
def runMaskImages(self):
    if self.insar.applyWaterMask:
        corrName  = self.insar.coherenceFilename
        wrapName = self.insar.topophaseFlatFilename
        maskName = self.insar.waterMaskImageName
        ampName = self.insar.resampOnlyAmpName
        prefix = self.insar.unmaskedPrefix
        newCorrName = prefix + '_' + corrName
        newWrapName =  prefix + '_' + wrapName
        newAmpName =  prefix + '_' + ampName
    
        os.system('cp -r ' + corrName + ' ' + newCorrName)
        os.system('cp -r ' + wrapName + ' ' + newWrapName)
        os.system('cp -r ' + ampName + ' ' + newAmpName)
    
        corrImage = createImage()
        corrImage.load(corrName+'.xml')
        corrmap = np.memmap(corrName,corrImage.toNumpyDataType(),'r+',
                            shape=(corrImage.bands*corrImage.coord2.coordSize,corrImage.coord1.coordSize))
        wrapImage = createImage()
        wrapImage.load(wrapName+'.xml')
        wrapmap = np.memmap(wrapName,wrapImage.toNumpyDataType(),'r+',
                            shape=(wrapImage.coord2.coordSize,wrapImage.coord1.coordSize))
        maskImage = createImage()
        maskImage.load(maskName+'.xml')
        maskmap = np.memmap(maskName,maskImage.toNumpyDataType(),'r',
                            shape=(maskImage.coord2.coordSize,maskImage.coord1.coordSize))
        ampImage = createImage()
        ampImage.load(ampName+'.xml')
        ampmap = np.memmap(ampName,ampImage.toNumpyDataType(),'r+',
                            shape=(ampImage.coord2.coordSize,ampImage.bands*ampImage.coord1.coordSize))
        #NOTE:thre is a bug in the calculation of lat.rd and lon.rdr so the two have one more line 
        #then the corr and wrap images. Add some logic to remove potential extra line
        lastLine = min(wrapmap.shape[0],maskmap.shape[0])
        #corr file is a 2 bands BIL scheme so multiply each band
        corrmap[:corrImage.bands*lastLine:2,:] = corrmap[:corrImage.bands*lastLine:2,:]*maskmap[:lastLine,:]
        corrmap[1:corrImage.bands*lastLine:2,:] = corrmap[1:corrImage.bands*lastLine:2,:]*maskmap[:lastLine,:]
        wrapmap[:lastLine,:] = wrapmap[:lastLine,:]*maskmap[:lastLine,:]
        ampmap[0:lastLine,::2] = ampmap[0:lastLine,::2]*maskmap[:lastLine,:]
        ampmap[0:lastLine,1::2] = ampmap[0:lastLine,1::2]*maskmap[:lastLine,:]
    
        #change the filename in the metadata and then save the xml file for the unmasked images
        corrImage.filename = newCorrName
        corrImage.dump(newCorrName+'.xml')
        wrapImage.filename = newWrapName
        wrapImage.dump(newWrapName+'.xml')
        ampImage.filename = newAmpName
        ampImage.dump(newAmpName+'.xml')