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




import sys
import isceobj
from iscesys.Component.Component import Component
from mroipac.grass.grass import Grass

# giangi: taken Piyush code grass.py and adapted

def runUnwrap(self):
    wrapName = self.insar.topophaseFlatFilename
    unwrapName = self.insar.unwrappedIntFilename
    corName = self.insar.coherenceFilename
    width = self.insar.resampIntImage.width
    with isceobj.contextIntImage(
        filename=wrapName,
        width=width,
        accessMode='read') as intImage:

        with isceobj.contextOffsetImage(
            filename=corName,
            width = width,
            accessMode='read') as cohImage:

            with isceobj.contextUnwImage(
                filename=unwrapName,
                width = width,
                accessMode='write') as unwImage:

                grs=Grass(name='insarapp_grass')
                grs.configure()
                grs.wireInputPort(name='interferogram',
                    object=intImage)
                grs.wireInputPort(name='correlation',
                    object=cohImage)
                grs.wireInputPort(name='unwrapped interferogram',
                    object=unwImage)
                grs.unwrap()
                unwImage.renderHdr()

                pass
            pass
        pass

    return None
