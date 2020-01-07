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



def createPulsetiming():
    from .Pulsetiming import Pulsetiming
    return Pulsetiming()

def createSetmocomppath():
    from .Setmocomppath import Setmocomppath
    return Setmocomppath()

def createOrbit2sch(*args, **kwargs):
    from .Orbit2sch import Orbit2sch
    return Orbit2sch(*args, **kwargs)

def createSch2orbit(*args, **kwargs):
    from .Sch2orbit import Sch2orbit
    return Sch2orbit(*args, **kwargs)

def createMocompbaseline(name = ''):
    from .Mocompbaseline import Mocompbaseline
    return Mocompbaseline(name=name)

def createCalculateFdHeights():
        from .orbitLib.CalcSchHeightVel import CalcSchHeightVel as CHV
        return CHV()

def createFdMocomp():
        from .fdmocomp import Fdmocomp
        return Fdmocomp.FdMocomp()

def createGetpeg():
    from .Getpeg import Getpeg
    return Getpeg()

from . import pegManipulator

def getFactoriesInfo():
    """
    Returns a dictionary with information on how to create the objects from their factories
    """
    return  {'Mocompbaseline':
                     {
                     'factory':'createMocompbaseline'
                     }
              }