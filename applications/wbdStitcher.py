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




import isce
import logging
import logging.config
from iscesys.Component.Application import Application
from iscesys.Component.Component import Component
from contrib.demUtils.SWBDStitcher import SWBDStitcher

import os
STITCHER = Application.Facility(
    '_stitcher',
    public_name='wbd stitcher',
    module='contrib.demUtils',
    factory='createSWBDStitcher',
    args=('awbdstitcher',),
    mandatory=True,
    doc="Water body stitcher"
                              )
class Stitcher(Application):    
    def main(self):
        # prevent from deliting local files
        if(self._stitcher._useLocalDirectory):
            self._stitcher._keepAfterFailed = True
            self._stitcher._keepWbds = True
        # is a metadata file is created set the right type
        if(self._stitcher._meta == 'xml'):
            self._stitcher.setCreateXmlMetadata(True)
        
        # check for the action to be performed
        if(self._stitcher._action == 'stitch'):
            if(self._stitcher._bbox):
                lat = self._stitcher._bbox[0:2]
                lon = self._stitcher._bbox[2:4]
                if (self._stitcher._outputFile is None):
                    self._stitcher._outputFile = self._stitcher.defaultName(self._stitcher._bbox)
    
                if not(self._stitcher.stitchWbd(lat,lon,self._stitcher._outputFile,self._stitcher._downloadDir, \
                        keep=self._stitcher._keepWbds)):
                    print('Could not create a stitched water body mask. Some tiles are missing')
                
            else:
                print('Error. The "bbox" attribute must be specified when the action is "stitch"')
                raise ValueError
        elif(self._stitcher._action == 'download'):
            if(self._stitcher._bbox):
                lat = self._stitcher._bbox[0:2]
                lon = self._stitcher._bbox[2:4]
                self._stitcher.getWbdsInBox(lat,lon,self._stitcher._downloadDir)
          
        else:
            print('Unrecognized action ',self._stitcher._action)
            return
    
        if(self._stitcher._report):
            for k,v in list(self._stitcher._downloadReport.items()):
                print(k,'=',v)
                
    def Usage(self):
        print("\nUsage: wbdStitcher.py input.xml\n")
    
    facility_list = (STITCHER,)
    
    @property
    def stitcher(self):
        return self._stitcher
    @stitcher.setter
    def stitcher(self,stitcher):
        self._stitcher = stitcher
    
    family = 'wbdstitcher' 
    
    def __init__(self,family = '', name = ''):
        super(Stitcher, self).__init__(family if family else  self.__class__.family, name=name)
       

if __name__ == "__main__":
    import sys
    ds = Stitcher('wbdstitcher')
    ds.configure()
    ds.run()