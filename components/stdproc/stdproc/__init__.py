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



from .formslc import *
from .resamp import *
from .resamp_image import *
from .resamp_amps import *
from .resamp_only import *
from .resamp_slc import *
from .topo import *
from .correct import createCorrect, contextCorrect
from .mocompTSX import *
from .estamb import *

#ing added sensor argument to turn it into a real factory, allowing other type
# of formSLC and moved instantiation here
def createFormSLC(sensor=None, name=''):
    if sensor is None or 'uavsar' in sensor.lower():
        from .formslc.Formslc import Formslc as cls
        return cls(name=name)
    elif str(sensor).lower() in ['terrasarx','cosmo_skymed_slc','radarsat2','sentinel1a','tandemx','kompsat5','risat1_slc','alos2','ers_slc','alos_slc','envisat_slc']:
        from .mocompTSX.MocompTSX import MocompTSX as cls
    else:
        raise ValueError("Unrecognized Sensor: %s" % str(sensor))
    return cls()

def getFactoriesInfo():
    """
    Returns a dictionary with information on how to create an object Sensor from its factory
    """
    return  {'FormSLC':
                     {'args':
                           {
                            'sensor':{'value':['None','uavsar','terrasarx','cosmo_skymed_slc','radarsat2','sentinel1a','tandemx',
                                               'kompsat5','risat1_slc','alos2','ers_slc','alos_slc','envisat_slc'],
                                      'type':'str','optional':True,'default':None}
                            },
                     'factory':'createFormSLC'
                     }
              }


