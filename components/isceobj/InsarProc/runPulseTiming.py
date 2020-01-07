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



import datetime
import logging

from isceobj.Orbit.Orbit import Orbit

logger = logging.getLogger('isce.insar.runPulseTiming')

def runPulseTiming(self):
    master = self.insar.masterFrame
    slave = self.insar.slaveFrame
    # add orbits to main object -law of demeter pls.
    self.insar.masterOrbit = pulseTiming(master, self.insar.procDoc, 'master')
    self.insar.slaveOrbit = pulseTiming(slave, self.insar.procDoc, 'slave')
    return None

def pulseTiming(frame, catalog, which):
    logger.info("Pulse Timing")
    numberOfLines = frame.getNumberOfLines()
    prf = frame.getInstrument().getPulseRepetitionFrequency()
    pri = 1.0 / prf
    startTime = frame.getSensingStart()
    orbit = frame.getOrbit()
    pulseOrbit = Orbit(name=which+'orbit')
    startTimeUTC0 = (startTime -
                     datetime.datetime(startTime.year,
                                       startTime.month,startTime.day)
                     )
    timeVec = [pri*i +
               startTimeUTC0.seconds +
               10**-6*startTimeUTC0.microseconds for i in range(numberOfLines)
               ]
    catalog.addItem("timeVector", timeVec, "runPulseTiming.%s" % which)
    for i in range(numberOfLines):
        dt = i * pri
        time = startTime + datetime.timedelta(seconds=dt)
        sv = orbit.interpolateOrbit(time, method='hermite')
        pulseOrbit.addStateVector(sv)
        
    return pulseOrbit
