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

logger = logging.getLogger('isce.insar.runOrbit2sch')


def runOrbit2sch(self):
    from isceobj.Catalog import recordInputsAndOutputs
    import numpy
    logger.info("Converting the orbit to SCH coordinates")

    # Piyush
    ####We don't know the correct SCH heights yet.
    ####Not computing average peg height yet.
    peg = self.insar.peg
    pegHavg = self.insar.averageHeight
    planet = self.insar.planet

#    if self.pegSelect.upper() == 'MASTER':
#        pegHavg = self.insar.getFirstAverageHeight()
#    elif self.pegSelect.upper() == 'SLAVE':
#        pegHavg = self.insar.getSecondAverageHeight()
#    elif self.pegSelect.upper() == 'AVERAGE':
#        pegHavg = self.insar.averageHeight
#    else:
#        raise Exception('Unknown peg selection method: ', self.pegSelect)

    masterOrbit = self.insar.masterOrbit
    slaveOrbit = self.insar.slaveOrbit

    objOrbit2sch1 = stdproc.createOrbit2sch(averageHeight=pegHavg)
    objOrbit2sch1.stdWriter = self.stdWriter.set_file_tags("orbit2sch",
                                                           "log",
                                                           "err",
                                                           "log")
    objOrbit2sch2 = stdproc.createOrbit2sch(averageHeight=pegHavg)
    objOrbit2sch2.stdWriter = self.stdWriter

    ## loop over master/slave orbits
    for obj, orb, tag, order in zip((objOrbit2sch1, objOrbit2sch2),
                                    (self.insar.masterOrbit, self.insar.slaveOrbit),
                                    ('master', 'slave'),
                                    ('First', 'Second')):
        obj(planet=planet, orbit=orb, peg=peg)
        recordInputsAndOutputs(self.insar.procDoc, obj,
                               "runOrbit2sch." + tag,
                               logger,
                               "runOrbit2sch." + tag)

        #equivalent to self.insar.masterOrbit =
        setattr(self.insar,'%sOrbit'%(tag), obj.orbit)

        #Piyush
        ####The heights and the velocities need to be updated now.
        (ttt, ppp, vvv, rrr) = obj.orbit._unpackOrbit()

        #equivalent to self.insar.setFirstAverageHeight()
        # SCH heights replacing the earlier llh heights
        # getattr(self.insar,'set%sAverageHeight'%(order))(numpy.sum(numpy.array(ppp),axis=0)[2] /(1.0*len(ppp)))

        #equivalent to self.insar.setFirstProcVelocity()
        getattr(self.insar,'set%sProcVelocity'%(order))(vvv[len(vvv)//2][0])

    return None

