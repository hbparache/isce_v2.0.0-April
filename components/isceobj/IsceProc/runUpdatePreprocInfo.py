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
# Authors: Kosal Khun, Marco Lavalle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Comment: Adapted from InsarProc/runUpdatePreprocInfo.py runFdMocomp.py
import logging
import stdproc
import sys
import isceobj

logger = logging.getLogger('isce.isceProc.runUpdatePreprocInfo')

## Mapping from use_dop keyword
USE_DOP = {'AVERAGE' : lambda doplist, index: float(sum(doplist))/len(doplist),
           'SCENE': lambda doplist, index: doplist[index]
           }


def runUpdatePreprocInfo(self, use_dop="average"):
    fds = {}
    dops = {}
    peg = self._isce.peg
    lookside = self._isce.lookSide
    chirpExtension = self._isce.chirpExtension
    for sceneid in self._isce.selectedScenes:
        fds[sceneid] = {}
        dops[sceneid] = {}
        for pol in self._isce.selectedPols:
            frame = self._isce.frames[sceneid][pol]
            orbit = self._isce.orbits[sceneid][pol]
            fdHeight = self._isce.fdHeights[sceneid][pol]
            dopplerCentroid = self._isce.dopplers[sceneid][pol]
            dops[sceneid][pol] = dopplerCentroid
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            sid = self._isce.formatname(sceneid, pol)
            fd = run(frame, orbit, dopplerCentroid.fractionalCentroid, peg, fdHeight, chirpExtension, lookside, catalog=catalog, sceneid=sid)
            self._isce.procDoc.addAllFromCatalog(catalog)
            fds[sceneid][pol] = fd

    use_dop = use_dop.split('_')
    if use_dop[0] == 'scene':
        sid = use_dop[1]
        try:
            index = self._isce.selectedScenes.index(sid)
        except AttributeError:
            sys.exit("Could not find scene with id: %s" % sid)
        use_dop = 'scene'
    else:
        use_dop = 'average'
        index = 0
    polfds = []
    poldops = []
    for pol in self._isce.selectedPols:
        polfds.extend(self._isce.getAllFromPol(pol, fds))
        poldops.extend(self._isce.getAllFromPol(pol, dops))

    avgdop = getdop(polfds, poldops, use_dop=use_dop, index=index, sceneid='ALL')
    self._isce.dopplerCentroid = avgdop


def run(frame, orbit, dopplerCentroid, peg, fdHeight, chirpextension, lookside, catalog=None, sceneid='NO_ID'):
    """
    Calculate motion compensation correction for Doppler centroid
    """
    rangeSamplingRate = frame.instrument.rangeSamplingRate
    rangePulseDuration = frame.instrument.pulseLength
    chirpSize = int(rangeSamplingRate * rangePulseDuration)

    number_range_bins = frame.numberRangeBins
    logger.info("Correcting Doppler centroid for motion compensation: %s" % sceneid)

    fdmocomp = stdproc.createFdMocomp()
    fdmocomp.wireInputPort(name='frame', object=frame)
    fdmocomp.wireInputPort(name='peg', object=peg)
    fdmocomp.wireInputPort(name='orbit', object=orbit)
    fdmocomp.setWidth(number_range_bins)
    fdmocomp.setSatelliteHeight(fdHeight)
    fdmocomp.setDopplerCoefficients([dopplerCentroid, 0.0, 0.0, 0.0])
    fdmocomp.setLookSide(lookside)
    fdmocomp.fdmocomp()
    dopplerCorrection = fdmocomp.dopplerCentroid
    if catalog is not None:
        isceobj.Catalog.recordInputsAndOutputs(catalog, fdmocomp,
                                               "runUpdatePreprocInfo." + sceneid, logger, "runUpdatePreprocInfo." + sceneid)
    return dopplerCorrection


def getdop(fds, dops, use_dop='average', index=0, sceneid='NO_POL'):
    """
    Get average doppler.
    """
    try:
        fd = USE_DOP[use_dop.upper()](fds, index)
    except KeyError:
        print("Unrecognized use_dop option.  use_dop = ", use_dop)
        print("Not found in dictionary:", USE_DOP.keys())
        sys.exit(1)
    logger.info("Updated Doppler Centroid %s: %s" % (sceneid, fd))

    averageDoppler = dops[0]
    for dop in dops[1:]:
        averageDoppler = averageDoppler.average(dop)
    averageDoppler.fractionalCentroid = fd
    return averageDoppler
