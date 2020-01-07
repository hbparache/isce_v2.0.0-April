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



# Comment: Adapted from InsarProc/runFormSLCisce.py
import logging
import stdproc
import isceobj
from iscesys.ImageUtil.ImageUtil import ImageUtil as IU

logger = logging.getLogger('isce.isceProc.runFormSLCisce')


def runFormSLC(self, patchSize=None, goodLines=None, numPatches=None):
    #NOTE tested the formslc() as a stand alone by passing the same inputs
    #computed in Howard terraSAR.py. The differences here arises from the
    #differences in the orbits when using the same orbits the results are very
    #close jng this will make the second term in coarseAz in offsetprf equal
    #zero. we do so since for tsx there is no such a term. Need to ask
    #confirmation
    self._isce.patchSize = self._isce.numberValidPulses
    # the below value is zero because of we just did above, but just want to be
    #  explicit in the definition of is_mocomp
    self._isce.get_is_mocomp()

    v, h = self._isce.vh()
    peg = self._isce.peg
    dopplerCentroid = self._isce.dopplerCentroid
    stdWriter = self._stdWriter
    sensorname = self.sensorName

    for sceneid in self._isce.selectedScenes:
        #self._isce.slcImages[sceneid] = {} #ML
        self._isce.formSLCs[sceneid] = {}
        for pol in self._isce.selectedPols:
            frame = self._isce.frames[sceneid][pol]
            orbit = self._isce.orbits[sceneid][pol]
            rawImage = self._isce.slcImages[sceneid][pol]
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            sid = self._isce.formatname(sceneid, pol)
            slcImage, formSlc = run(rawImage, frame, dopplerCentroid, orbit, peg, v, h, sensorname, stdWriter, catalog=catalog, sceneid=sid)
            self._isce.slcImages[sceneid][pol] = slcImage
            self._isce.formSLCs[sceneid][pol] = formSlc

    self._isce.numberPatches = slcImage.getLength() / float(self._isce.numberValidPulses)


def run(rawImage, frame, dopplerCentroid, orbit, peg, velocity, height, sensorname, stdWriter, catalog=None, sceneid='NO_ID'):
    logger.info("Forming SLC: %s" % sceneid)

    imSlc = isceobj.createSlcImage()
    IU.copyAttributes(rawImage, imSlc)
    imSlc.setAccessMode('read')
    imSlc.createImage()
    formSlc = stdproc.createFormSLC(sensorname)
    formSlc.setBodyFixedVelocity(velocity)
    formSlc.setSpacecraftHeight(height)
    formSlc.wireInputPort(name='doppler', object=dopplerCentroid)
    formSlc.wireInputPort(name='peg', object=peg)
    formSlc.wireInputPort(name='frame', object=frame)
    formSlc.wireInputPort(name='orbit', object=orbit)
    formSlc.wireInputPort(name='rawImage', object=None)
    formSlc.wireInputPort(name='planet', object=frame.instrument.platform.planet)
    for item in formSlc.inputPorts:
        item()
    formSlc.slcWidth = imSlc.getWidth()
    formSlc.startingRange = formSlc.rangeFirstSample
    formSlc.rangeChirpExtensionsPoints = 0
    formSlc.setLookSide(frame.platform.pointingDirection)
    formSlc.slcSensingStart = frame.getSensingStart()
    formSlc.outOrbit = orbit

    formSlc.stdWriter = stdWriter.set_file_tags("formslcISCE",
                                                "log",
                                                "err",
                                                "out")

    time, position, vel, relTo = orbit._unpackOrbit()
    mocomp_array = [[],[]]
    for (t, p) in zip(time, position):
        mocomp_array[0].append(t-time[0])
        mocomp_array[1].append( p[0])

    formSlc.mocompPosition = mocomp_array
    formSlc.mocompIndx = list(range(1,len(time)+1))
    formSlc.dim1_mocompPosition = 2
    formSlc.dim2_mocompPosition = len(time)
    formSlc.dim1_mocompIndx = len(time)


#    slcImage = formSlc()
    imSlc.finalizeImage()
    if catalog is not None:
        isceobj.Catalog.recordInputsAndOutputs(catalog, formSlc,
                                               "runFormSLCisce.%s" % sceneid,
                                               logger,
                                               "runFormSLCisce.%s" % sceneid)
    return imSlc, formSlc
