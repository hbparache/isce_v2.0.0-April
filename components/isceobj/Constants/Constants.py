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
# Authors: Giangi Sacco, Eric Belz
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



"""Docstring"""

Version = "$Revision: 876$"
# $Source$ 
from iscesys.Compatibility import Compatibility
from isceobj.Planet.Planet import Planet
from isceobj.Planet.AstronomicalHandbook import c as SPEED_OF_LIGHT

EARTH = Planet(pname='Earth')
EarthGM = EARTH.GM
EarthSpinRate = EARTH.spin
EarthMajorSemiAxis = EARTH.ellipsoid.a
EarthEccentricitySquared = EARTH.ellipsoid.e2

def nu2lambda(nu):
    return SPEED_OF_LIGHT/nu

def lambda2nu(lambda_):
    return SPEED_OF_LIGHT/lambda_
