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


from isceobj.Constants import SPEED_OF_LIGHT
import copy

logger = logging.getLogger('isce.insar.runPrepareResamps')

def runPrepareResamps(self, rangeLooks=None, azLooks=None):
    import math
    
    valid_az_samples =  self.insar.numberValidPulses
    numPatches = self.insar.numberPatches
    lines = numPatches * valid_az_samples 
    
    fs = self._insar.masterFrame.getInstrument().getRangeSamplingRate()
    dr = (SPEED_OF_LIGHT / (2 * fs))
    
    self._insar.setSlantRangePixelSpacing(dr)
    
#    widthSlc = max(self._insar.getMasterSlcImage().getWidth(), self._insar.getSlaveSlcImage().getWidth())
    widthSlc = self._insar.formSLC1.slcImage.getWidth()
    
    radarWavelength = self._insar.masterFrame.getInstrument().getRadarWavelength()
    
    ####Compute ground pixel spacing
    frame = self._insar.masterFrame
    svmid = frame.orbit.interpolate(frame.sensingMid, method='hermite')
    hdg = frame.orbit.getHeading()
    elp = frame._instrument._platform._planet.ellipsoid
    

    llh = elp.xyz_to_llh(svmid.getPosition())
    elp.setSCH(llh[0], llh[1], hdg)
    sch,vsch = elp.xyzdot_to_schdot(svmid.getPosition(),svmid.getVelocity())
    rcurv = elp.pegRadCur
    ht = sch[2]
    rng = frame.getStartingRange() + 0.5*widthSlc *dr
    
    costheta = (2*rcurv*ht+ht*ht-rng*rng)/-2/rcurv/rng
    sininc = math.sqrt(1 - (costheta * costheta))
    prf = frame._instrument.getPulseRepetitionFrequency()

    grndpixel = dr/sininc
    azpixel = vsch[0] * rcurv / (prf *(rcurv + sch[2]))
    
    posting = self.posting
    
    if rangeLooks:
        looksrange=rangeLooks
    else:
        looksrange=int(posting/grndpixel+0.5)

    if azLooks:
        looksaz=azLooks
    else:
        looksaz=int(round(posting/azpixel))
    
    if (looksrange < 1):
        logger.warn("Number range looks less than zero, setting to 1")
        looksrange = 1
    if (looksaz < 1):
        logger.warn("Number azimuth looks less than zero, setting to 1")
        looksaz = 1

    self._insar.setNumberAzimuthLooks(looksaz) 
    self._insar.setNumberRangeLooks(looksrange) 
    self._insar.setNumberResampLines(lines) 

    #jng at one point this will go in the defaults of the self._insar calss
    numFitCoeff = 6
    self._insar.setNumberFitCoefficients(numFitCoeff) 
