#!/usr/bin/env python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2011 to the present, california institute of technology.
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
import sys
import os
import math
from isceobj.Image.StreamImage import StreamImage
from isceobj.Image.IntImage import IntImage
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from stdproc.rectify.dismphfile.Dismphfile import Dismphfile

def main():
    obj = Dismphfile()
    maxLat  = 34.7641666673 
    minLat  = 33.6266666705 
    minLon  = -118.618333334 
    maxLon  = -118.119166669

    geoFilename = sys.argv[1]
    geoImage = IntImage()
    geoAccessMode = 'read'
    geoEndian = 'l'
    geoWidth = 1798
    obj.setKmlFilename('testKml.kml')
    obj.setTitle('test Title')
    obj.setDescription('test description')
    geoImage.initImage(geoFilename,geoAccessMode,geoEndian,geoWidth)
  
    obj.setBoundingBox([minLat,maxLat,minLon,maxLon])
    obj.dismphfile(geoImage,'testOut.tiff')

if __name__ == "__main__":
    sys.exit(main())
