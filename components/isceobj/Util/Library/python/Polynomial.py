#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2013 to the present, california institute of technology.
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



from iscesys.Component.Configurable import Configurable


class Polynomial(Configurable):
    '''
    Class to store 1D polynomials in ISCE.
    Implented as a list of coefficients:

    [    1,     x^1,     x^2, ...., x^n]

    The size of the 1D list will correspond to 
    [order+1].
    '''
    family = 'polynomial'
    def __init__(self, family='', name=''):
        '''
        Constructor for the polynomial object.
        '''
        self._coeffs = []       
        self._accessor = None
        self._factory = None
        self._poly = None
        self._width = 0
        self._length = 0
        super(Polynomial,self).__init__(family if family else  self.__class__.family, name)
        
        
        return
    def initPoly(self,image = None):
        
        if(image):
            self._width = image.width
            self._length = image.length
            
    def setCoeffs(self, parms):
        '''
        Set the coefficients using another nested list.
        '''
        raise NotImplementedError("Subclasses should implement setCoeffs!")

    def getCoeffs(self):
        return self._coeffs


    def setImage(self, width):
        self._width = image.width
        self._length = image.length

   
    def exportToC(self):
        '''
        Use the extension module and return a pointer in C.
        '''
        raise NotImplementedError("Subclasses should implement exportToC!")


    def importFromC(self, pointer, clean=True):
        pass

    def copy(self):
        pass
        
    def setWidth(self, var):
        self._width = int(var)
        return

    @property
    def width(self):
        return self._width

    def setLength(self, var):
        self._length = int(var)
        return

    @property
    def length(self):
        return self._length

    def getPointer(self):
        return self._accessor
