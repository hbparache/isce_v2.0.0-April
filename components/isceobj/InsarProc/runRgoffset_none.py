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
# Authors: Giangi Sacco, Maxim Neumann
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import logging
import isceobj

from isceobj.Location.Offset import OffsetField,Offset

logger = logging.getLogger('isce.insar.runRgoffset')

def runRgoffset(self):

    # dummy zero-valued offset field
    offField = OffsetField()
    for i in range(200):
        offField.addOffset(Offset(10+i,10+i,0,0,10,1,1,0))

    # save the input offset field for the record
    self._insar.setOffsetField(offField)
    self._insar.setRefinedOffsetField(offField)
