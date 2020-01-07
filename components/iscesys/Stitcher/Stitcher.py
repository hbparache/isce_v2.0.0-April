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



#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Author: Giangi Sacco
# Copyright 2012, 2015 by the California Institute of Technology.
# ALL RIGHTS RESERVED.
# United States Government Sponsorship acknowledged. Any commercial use must be
# negotiated with the Office of Technology Transfer at the
# California Institute of Technology.
from iscesys.Component.Component import Component
from isceobj.Image.Image import TO_NUMPY
import numpy as np
import os
#Parameters definitions
DTYPE = Component.Parameter('_dtype',
    public_name = 'dtype',
    default = '',
    type = str,
    mandatory = True,
    doc = 'Data type')
OUTPUT_FILE = Component.Parameter('_outputFile',
    public_name='outputFile',
    default = '',
    type = str,
    mandatory = True,
    doc = 'Output file.')
FILE_LIST = Component.Parameter('_fileList',
    public_name = 'fileList',
    default = '',
    type = str,
    mandatory = True,
    doc = 'Ordered list of the files to stitch. The order must be from top ' + \
          'top left to bottom right')
TILE_SIZE = Component.Parameter('_tileSize',
    public_name = 'tileSize',
    default = [],
    container=list,
    type=int,
    mandatory = True,
    doc = 'Two element list with the number of row and columns of the tile.')
OVERLAP = Component.Parameter('_overlap',
    public_name = 'overlap',
    default = [1,1],
    container=list,
    type=int,
    mandatory = False,
    doc = 'Number of overlapping pixels  between two tiles along the rows and columns.')

ARRANGEMENT = Component.Parameter('_arrangement',
    public_name = 'arrangement',
    default = [],
    container=list,
    type=int,
    mandatory = True,
    doc = 'Two element list with the number of tiles along ' +\
           'the vertical and the horizontal directions.')
FILLING_VALUE = Component.Parameter('_fillingValue',
    public_name = 'fillingValue',
    default = 0,
    type=float,
    mandatory = True,
    doc = 'Value used for missing tiles.')
ENDIAN = Component.Parameter('_endian',
    public_name = 'endian',
    default = '>',
    type = str,
    mandatory = False,
    doc = 'Data endianness. > big endian, < small endian')
DIRECTORY = Component.Parameter('_directory',
    public_name='directory',
    default = './',
    type = str,
    mandatory = False,
    doc = "Location where the files to be stitched are")
class Stitcher(Component):
    family = 'stitcher'
    parameter_list = (DTYPE,
                      OUTPUT_FILE,
                      FILE_LIST,
                      TILE_SIZE,
                      OVERLAP,
                      ARRANGEMENT,
                      FILLING_VALUE,
                      ENDIAN,
                      DIRECTORY
                      )
    @property
    def fillValue(self):
        return self._fillValue
    @fillValue.setter
    def fillValue(self,val):
        self._fillValue = val
    @property
    def dtype(self):
        return self._dtype
    @dtype.setter
    def dtype(self,val):
        self._dtype = val
    @property
    def outputFile(self):
        return self._outputFile
    @outputFile.setter
    def outputFile(self,val):
        self._outputFile = val
    @property
    def fileList(self):
        return self._fileList
    @fileList.setter
    def fileList(self,val):
        self._fileList = val
    @property
    def tileSize(self):
        return self._tileSize
    @tileSize.setter
    def tileSize(self,val):
        self._tileSize = val
    @property
    def overlap(self):
        return self._overlap
    @overlap.setter
    def overlap(self,val):
        self._overlap = val
    @property
    def arrangement(self):
        return self._arrangement
    @arrangement.setter
    def arrangement(self,val):
        self._arrangement = val
    @property
    def endian(self):
        return self._endian
    @endian.setter
    def endian(self,val):
        self._endian = val
    @property
    def directory(self):
        return self._directory
    @directory.setter
    def directory(self,val):
        self._directory = val
    def getDataType(self):
        ret = ''
        if self._dtype:
            ret = TO_NUMPY[self._dtype]
        return ret
         
    def stitch(self):
        dtype = self.getDataType()
        dr = self._tileSize[0] - self._overlap[0]
        dc = self._tileSize[0] - self._overlap[0]
        mmap = np.memmap(self._outputFile,dtype,'w+',
                         shape=(self._arrangement[0]*dr,
                                self._arrangement[1]*dc))
        pos = 0
        mmap[:] = self._fillingValue 
        for i in range(self._arrangement[0]):
            for j in range(self._arrangement[1]):
                name =  self._fileList[pos]
                #if the filename is _toSkipName the skip this data.
                #it will be filled with _fillingValue
                if not name == self._toSkipName:
                    data = np.reshape(np.fromfile(os.path.join(self.directory,name),self._endian + dtype),self._tileSize)
                    mmap[i*dr:(i+1)*dr,j*dc:(j+1)*dc] = data[:dr,:dc]
                pos += 1
            

    def __init__(self,family = '', name = ''):

        super(Component, self).__init__(family if family else  self.__class__.family, name=name)
        self._toSkipName = 'toSkip'