#!/usr/bin/env python3 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2010 to the present, california institute of technology.
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
from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()
from isceobj.ImageFilter.ComplexExtractor import ComplexExtractor
from isceobj.ImageFilter.BandExtractor import BandExtractor



def createFilter(typeExtractor,fromWhat):
    """Extractor factory"""
    instanceType = ''
    #What is passed here -> how it is passed to the FilterFactory.cpp -> What is instantiated in FilterFactory.cpp
    #(MagnitudeExtractor,'cartesian') -> (MagnitudeExtractor,0) -> MagnitudeExtractor
    #(MagnitudeExtractor,'polar') -> (ComponentExtractor,0) -> ComponentExtractor, 0
    #(PhaseExtractor,'cartesian') -> (PhaseExtractor,0) -> PhaseExtractor
    #(PhaseExtractor,'polar') -> (ComponentExtractor,1) -> ComponentExtractor, 1
    #(RealExtractor,'cartesian') -> (ComplexExtractor,0) -> ComponentExtractor 0
    #(ImagExtractor,'cartesian') -> (ComplexExtractor,1) -> ComponentExtractor 1
    #(RealExtractor,'polar') -> (RealExtractor,0) -> RealExtractor 
    #(ImagExtractor,'polar') -> (ImagExtractor,1) -> ImagExtractor 
    #(BandExtractor,band) -> (BandExtractor,band) -> BandExtractor band
    if typeExtractor.lower() == 'magnitudeextractor' and fromWhat.lower()  == 'cartesian':
        return ComplexExtractor('MagnitudeExtractor',0)
    elif typeExtractor.lower() == 'magnitudeextractor' and fromWhat.lower()  == 'polar':
        return ComplexExtractor('ComponentExtractor',0)
    elif typeExtractor.lower() == 'phaseextractor' and fromWhat.lower()  == 'cartesian':
        return ComplexExtractor('PhaseExtractor',0)
    elif typeExtractor.lower() == 'phaseextractor' and fromWhat.lower()  == 'polar':
        return ComplexExtractor('ComponentExtractor',1)
    elif typeExtractor.lower() == 'realextractor' and fromWhat.lower()  == 'cartesian':
        return ComplexExtractor('ComponentExtractor',0)
    elif typeExtractor.lower() == 'imagextractor' and fromWhat.lower()  == 'cartesian':
        return ComplexExtractor('ComponentExtractor',1)
    elif typeExtractor.lower() == 'realextractor' and fromWhat.lower()  == 'polar':
        return ComplexExtractor('RealExtractor',0)
    elif typeExtractor.lower() == 'imagextractor' and fromWhat.lower()  == 'polar':
        return ComplexExtractor('ImagExtractor',0)
    elif typeExtractor.lower() == 'bandextractor':
        #in this case fromWhat it's actually the band to extract
        return BandExtractor(typeExtractor,fromWhat)
    

    




if __name__ == "__main__":
    sys.exit(main())
