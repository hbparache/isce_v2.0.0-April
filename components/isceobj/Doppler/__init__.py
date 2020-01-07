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
# Authors: Walter Szeliga, Eric Gurrola
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



from __future__ import print_function

__all__ = ('createDoppler',)

def useDefault(name=None):
    if name:
        instance = None
    else:
        import isceobj.Doppler.DefaultDopp
        instance = DefaultDopp.DefaultDopp()
        return instance

def useDOPIQ(name=None):
    if name:
        instance = None
    else:
        import mroipac.dopiq.DopIQ
        instance = mroipac.dopiq.DopIQ.DopIQ()
        return instance

def useCalcDop(name=None):
    if name:
        instance = None
    else:
        import isceobj.Doppler.Calc_dop
        instance = isceobj.Doppler.Calc_dop.Calc_dop()
    return instance


def useDoppler(name=None):
    if name:
        instance = None
    else:
        import mroipac.doppler.Doppler
        instance = mroipac.doppler.Doppler.Doppler()
    return instance
    

doppler_facilities = {'USEDOPIQ' : useDOPIQ,
         'USECALCDOP' : useCalcDop,
         'USEDOPPLER' : useDoppler,
         'USEDEFAULT': useDefault}

def getFactoriesInfo():
    """
    Returns a dictionary with information on how to create an object Doppler from its factory
    """
    return  {'Doppler':
                     {'args':
                           {
                            'doppler':{'value':list(doppler_facilities.keys()),'type':'str'}
                            },
                     'factory':'createDoppler'
                     }
              }
    
def createDoppler(doppler=None, name=None):
    if doppler.upper() in doppler_facilities.keys():
        instance = doppler_facilities[doppler.upper()](name)
    else:
        instance = None
        print(
            "Doppler calculation method not recognized. Valid methods: ",
            doppler_facilities.keys())
    return instance

