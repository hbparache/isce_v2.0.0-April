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
# Author: Brett George
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import stdproc
import isceobj
import copy
from mroipac.formimage.FormSLC import FormSLC
import numpy as np 
from isceobj.Location.Peg import Peg

logger = logging.getLogger('isce.insar.runFormSLC')

#Run FormSLC for master
def focus(frame):
    from isceobj.Catalog import recordInputsAndOutputs
    from iscesys.ImageUtil.ImageUtil import ImageUtil as IU


    raw_r0 = frame.startingRange
    raw_dr = frame.getInstrument().getRangePixelSize()
    img = frame.getImage()
    dop = frame._dopplerVsPixel



    #####Velocity/ acceleration etc
    planet = frame.instrument.platform.planet
    elp =copy.copy( planet.ellipsoid)
    svmid = frame.orbit.interpolateOrbit(frame.sensingMid, method='hermite') 
    xyz = svmid.getPosition()
    vxyz = svmid.getVelocity()
    llh = elp.xyz_to_llh(xyz)

    heading = frame.orbit.getENUHeading(frame.sensingMid)

    elp.setSCH(llh[0], llh[1], heading)
    sch, schvel = elp.xyzdot_to_schdot(xyz, vxyz)
    vel = np.linalg.norm(schvel)
    hgt = sch[2]
    radius = elp.pegRadCur
   
    dist = np.linalg.norm(xyz)
    r_spinvec = np.array([0., 0., planet.spin])
    r_tempv = np.cross(r_spinvec, xyz)
    
    inert_acc = np.array([-planet.GM*x/(dist**3) for x in xyz])

    r_tempa = np.cross(r_spinvec, vxyz)
    r_tempvec = np.cross(r_spinvec, r_tempv)

    r_bodyacc = inert_acc - 2 * r_tempa - r_tempvec
    schbasis = elp.schbasis(sch)

    schacc = np.dot(schbasis.xyz_to_sch, r_bodyacc).tolist()[0]


    print('SCH velocity: ', schvel)
    print('SCH acceleration: ', schacc)
    print('Body velocity: ', vel)
    print('Height: ', hgt)
    print('Radius: ', radius)    
    

    #####Setting up formslc
    
    form = FormSLC()
    form.configure()

    ####Width
    form.numberBytesPerLine = img.getWidth()

    ###Includes header
    form.numberGoodBytes = img.getWidth()


    ####Different chirp extensions
#    form.nearRangeChirpExtFrac = 0.0
#    form.farRangeChirpExtFrac = 0.0
#    form.earlyAzimuthChirpExtFrac = 0.0
#    form.lateAzimuthChirpExtrFrac = 0.0


    ###First Line - set with defaults
    ###Depending on extensions
#    form.firstLine = 0

    ####First Sample
    form.firstSample = img.getXmin() // 2

    ####Start range bin - set with defaults
    ###Depending on extensions
#    form.startRangeBin = 1

    ####Starting range
    form.rangeFirstSample = frame.startingRange

    ####Number range bin
    ###Determined in FormSLC.py using chirp extensions
#    form.numberRangeBin = img.getWidth() // 2 - 1000

    ####Azimuth looks
    form.numberAzimuthLooks = 1


    ####debug
    form.debugFlag = False

    ####PRF
    form.prf = frame.PRF
    form.sensingStart = frame.sensingStart

    ####Bias
    form.inPhaseValue = frame.getInstrument().inPhaseValue
    form.quadratureValue = frame.getInstrument().quadratureValue

    ####Resolution
    form.antennaLength = frame.instrument.platform.antennaLength
    form.azimuthResolution = 0.6 * form.antennaLength  #85% of max bandwidth
    ####Sampling rate
    form.rangeSamplingRate = frame.getInstrument().rangeSamplingRate

    ####Chirp parameters
    form.chirpSlope = frame.getInstrument().chirpSlope
    form.rangePulseDuration = frame.getInstrument().pulseLength

    ####Wavelength
    form.radarWavelength = frame.getInstrument().radarWavelength

    ####Secondary range migration
    form.secondaryRangeMigrationFlag = True

    ####Doppler centroids
    cfs = [0., 0., 0., 0.]
    for ii in range(min(len(dop),4)):
        cfs[ii] = dop[ii]/form.prf

    form.dopplerCentroidCoefficients = cfs

    ####Create raw image
    rawimg = isceobj.createRawImage()
    rawimg.load(img.filename + '.xml')
    rawimg.setAccessMode('READ')
    rawimg.createImage()

    form.rawImage = rawimg


    ####All the orbit parameters
    form.antennaSCHVelocity = schvel
    form.antennaSCHAcceleration = schacc
    form.bodyFixedVelocity = vel
    form.spacecraftHeight = hgt
    form.planetLocalRadius = radius


    ###Create SLC image
    slcImg = isceobj.createSlcImage()
    slcImg.setFilename(img.filename + '.slc')
    form.slcImage = slcImg

    form.formslc()

    return form


def runFormSLC(self):

    self.insar.formSLC1 = focus(self.insar.masterFrame)
    self.insar.formSLC2 = focus(self.insar.slaveFrame)
    self.insar.setNumberPatches(min(self.insar.formSLC1.numberPatches, self.insar.formSLC2.numberPatches))
    self.insar.patchSize = self.insar.formSLC1.azimuthPatchSize
    self.insar.numberValidPulses = self.insar.formSLC1.numberValidPulses
    logger.info('Number of Valid Pulses = %d'%(self.insar.numberValidPulses))

    return None

