#
#
# Author: Brett George
# Copyright 2010
#

# Path to the _RunWrapper factories
_PATH = "isceobj.RoiProc."

__todo__ = "use 2.7's importlib"

## A factory to make _RunWrapper factories
def _factory(name, other_name=None):
    """create_run_wrapper = _factory(name)
    name is the module and class function name
    """
    other_name = other_name or name
    module = __import__(
        _PATH+name, fromlist=[""]
        )
    cls = getattr(module, other_name)
    def creater(other, *args, **kwargs):
        """_RunWrapper for object calling %s"""
        return _RunWrapper(other, cls)
    return creater

## Put in "_" to prevent import on "from Factorties import *"
class _RunWrapper(object):
    """_RunWrapper(other, func)(*args, **kwargs)

    executes:

    func(other, *args, **kwargs)

    (like a method)
    """
    def __init__(self, other, func):
        self.method = func
        self.other = other
        return None

    def __call__(self, *args, **kwargs):
        return self.method(self.other, *args, **kwargs)

    pass




# we turned runFormSLC into a facility
def createFormSLC(other, sensor):
    if sensor.lower() in ["terrasarx","cosmo_skymed_slc","radarsat2",'tandemx', 'kompsat5','risat1_slc','sentinel1a', 'alos2','ers_slc','alos_slc','envisat_slc', 'uavsar_rpi']:
        from .runFormSLCisce import runFormSLC
    else:
#        from .runFormSLC import runFormSLC
        from .runROI import runFormSLC
    return _RunWrapper(other, runFormSLC)


def createUnwrapper(other, do_unwrap = None, unwrapperName = None,
                    unwrap = None):
    if not do_unwrap and not unwrap:
        #if not defined create an empty method that does nothing
        def runUnwrap(self):
            return None
    elif unwrapperName.lower() == 'snaphu':
        from .runUnwrapSnaphu import runUnwrap
    elif unwrapperName.lower() == 'snaphu_mcf':
        from .runUnwrapSnaphu import runUnwrapMcf as runUnwrap
    elif unwrapperName.lower() == 'icu':
        from .runUnwrapIcu import runUnwrap
    elif unwrapperName.lower() == 'grass':
        from .runUnwrapGrass import runUnwrap
    return _RunWrapper(other, runUnwrap)

def createOffsetprf(other, coregisterMethod, do_offsetprf=True):
    if not do_offsetprf:
        from .runOffsetprf_none import runOffsetprf
    elif coregisterMethod.lower() == "ampcor":
        from .runOffsetprf_ampcor import runOffsetprf
    elif coregisterMethod.lower() == "nstage":
        from .runOffsetprf_nstage import runOffsetprf
    else:
        from .runOffsetprf import runOffsetprf
    return _RunWrapper(other, runOffsetprf)

def createRgoffset(other, coregisterMethod, do_rgoffset=True):
    if not do_rgoffset:
        from .runRgoffset_none import runRgoffset
    elif coregisterMethod.lower() == "ampcor":
        from .runRgoffset_ampcor import runRgoffset
    elif coregisterMethod.lower() == "nstage":
        from .runRgoffset_nstage import runRgoffset
    else:
        from .runRgoffset import runRgoffset
    return _RunWrapper(other, runRgoffset)

createCreateDem = _factory("createDem")
createExtractInfo = _factory("extractInfo")
createPreprocessor = _factory("runPreprocessor")
createOffoutliers = _factory("runOffoutliers")
createPrepareResamps = _factory("runPrepareResamps")
createResamp = _factory("runResamp")
createTopo = _factory("runTopo")
createGeo2rdr = _factory("runGeo2rdr")
createCorrect = _factory("runCorrect")
createShadecpx2rg = _factory("runShadecpx2rg")
createResamp_only = _factory("runResamp_only")
createCoherence = _factory("runCoherence")
createFilter = _factory("runFilter")
createGrass = _factory("runGrass")
createGeocode = _factory("runGeocode")
