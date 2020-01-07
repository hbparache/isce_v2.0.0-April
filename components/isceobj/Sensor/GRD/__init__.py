#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2015 to the present, california institute of technology.
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




def createGRDProduct():
    from .GRDProduct import GRDProduct
    return GRDProduct()

def createSentinel1(name=None):
    from .Sentinel1 import Sentinel1
    return Sentinel1()

def createRadarsat2(name=None):
    from .Radarsat2 import Radarsat2
    return Radarsat2()

def createTerrasarx(name=None):
    from .Terrasarx import Terrasarx
    return Terrasarx()


SENSORS = {
             'SENTINEL1' : createSentinel1,
             'RADARSAT2' : createRadarsat2,
             'TERRASARX' : createTerrasarx
          }

def getFactoriesInfo():
    """
    Returns a dictionary with information on how to create an object Sensor from its factory
    """
    return  {'Sensor':
                     {'args':
                           {
                            'sensor':{'value':list(SENSORS.keys()),'type':'str','optional':False}
                            },
                     'factory':'createSensor'
                     }
              }



def createSensor(sensor='', name=None):
    try:
        cls = SENSORS[str(sensor).upper()]
        try:
            instance = cls(name)
        except AttributeError:
            raise TypeError("'sensor name'=%s  cannot be interpreted" %
                            str(sensor))
        pass
    except:
        print("Sensor type not recognized. Valid Sensor types:\n",
              SENSORS.keys())
        instance = None
        pass
    return instance
