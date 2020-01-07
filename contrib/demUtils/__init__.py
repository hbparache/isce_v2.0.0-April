#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2014 to the present, california institute of technology.
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



def createDemStitcher(type='version3',name = ''):
    if(type == 'version3'):        
        from contrib.demUtils.DemStitcherV3 import DemStitcher
    if(type == 'version2'):
        from contrib.demUtils.DemStitcher import DemStitcher
    return DemStitcher(name=name)
def createSWBDStitcher(name = ''):
    from contrib.demUtils.SWBDStitcher import SWBDStitcher
    return SWBDStitcher(name=name)

def createCorrect_geoid_i2_srtm(name=''):
    from contrib.demUtils.Correct_geoid_i2_srtm import Correct_geoid_i2_srtm
    return Correct_geoid_i2_srtm(name=name)
def getFactoriesInfo():
    return  {'DemStitcher':
                     {'args':
                           {
                            'type':{'value':['version2','version3'],'type':'str','optional':True,'default':'version3'}
                            },
                     'factory':'createDemStitcher'                     
                     },
             'SWBDStitcher':
                     {
                     'factory':'createSWDBStitcher'                     
                     },
              'Correct_geoid_i2_srtm':
                     {
                     'factory':'createCorrect_geoid_i2_srtm'                     
                     }
              }