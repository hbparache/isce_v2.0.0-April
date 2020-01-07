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
# Author: Piyush Agram
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# giangi: taken Piyush code for snaphu and adapted

import sys
import isceobj
from contrib.Snaphu.Snaphu import Snaphu
from isceobj.Constants import SPEED_OF_LIGHT
import copy

def runUnwrap(self,costMode = None,initMethod = None, defomax = None, initOnly = None):

    if costMode is None:
        costMode   = 'DEFO'
    
    if initMethod is None:
        initMethod = 'MST'
    
    if  defomax is None:
        defomax = 4.0
    
    if initOnly is None:
        initOnly = False
    
    wrapName = self.insar.topophaseFlatFilename
    unwrapName = self.insar.unwrappedIntFilename

    wavelength = self.insar.masterFrame.getInstrument().getRadarWavelength()
    width      = self.insar.resampIntImage.width

    orbit = self.insar.masterFrame.orbit
    prf = self.insar.masterFrame.PRF
    elp = copy.copy(self.insar.masterFrame.instrument.platform.planet.ellipsoid)
    sv = orbit.interpolate(self.insar.masterFrame.sensingMid, method='hermite')
    hdg = orbit.getHeading()
    llh = elp.xyz_to_llh(sv.getPosition())
    elp.setSCH(llh[0], llh[1], hdg)

    earthRadius = elp.pegRadCur
    sch, vsch = elp.xyzdot_to_schdot(sv.getPosition(), sv.getVelocity())
    azimuthSpacing = vsch[0] * earthRadius / ((earthRadius + sch[2]) *prf)


    earthRadius = elp.pegRadCur
    altitude   = sch[2]
    corrfile  = self.insar.getCoherenceFilename()
    rangeLooks = self.insar.topo.numberRangeLooks
    azimuthLooks = self.insar.topo.numberAzimuthLooks

    azres = self.insar.masterFrame.platform.antennaLength/2.0
    azfact = self.insar.topo.numberAzimuthLooks * azres / azimuthSpacing

    rBW = self.insar.masterFrame.instrument.pulseLength * self.insar.masterFrame.instrument.chirpSlope
    rgres = abs(SPEED_OF_LIGHT / (2.0 * rBW))
    rngfact = rgres/self.insar.topo.slantRangePixelSpacing

    corrLooks = self.insar.topo.numberRangeLooks * self.insar.topo.numberAzimuthLooks/(azfact*rngfact) 
    maxComponents = 20

    snp = Snaphu()
    snp.setInitOnly(initOnly)
    snp.setInput(wrapName)
    snp.setOutput(unwrapName)
    snp.setWidth(width)
    snp.setCostMode(costMode)
    snp.setEarthRadius(earthRadius)
    snp.setWavelength(wavelength)
    snp.setAltitude(altitude)
    snp.setCorrfile(corrfile)
    snp.setInitMethod(initMethod)
    snp.setCorrLooks(corrLooks)
    snp.setMaxComponents(maxComponents)
    snp.setDefoMaxCycles(defomax)
    snp.setRangeLooks(rangeLooks)
    snp.setAzimuthLooks(azimuthLooks)
    snp.prepare()
    snp.unwrap()

    ######Render XML
    outImage = isceobj.Image.createUnwImage()
    outImage.setFilename(unwrapName)
    outImage.setWidth(width)
    outImage.setAccessMode('read')
    outImage.createImage()
    outImage.finalizeImage()
    outImage.renderHdr()

    #####Check if connected components was created
    if snp.dumpConnectedComponents:
        connImage = isceobj.Image.createImage()
        connImage.setFilename(unwrapName+'.conncomp')
        #At least one can query for the name used
        self.insar.connectedComponentsFilename = unwrapName+'.conncomp'
        connImage.setWidth(width)
        connImage.setAccessMode('read')
        connImage.setDataType('BYTE')
        connImage.createImage()
        connImage.finalizeImage()
        connImage.renderHdr()

    return
def runUnwrapMcf(self):
    runUnwrap(self,costMode = 'SMOOTH',initMethod = 'MCF', defomax = 2, initOnly = True)
    return
