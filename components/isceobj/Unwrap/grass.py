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


class grass(Component):
    '''Specific Connector from an insarApp object to a Grass object.''' 
    def __init__(self, obj):

        basename = obj.insar.topophaseFlatFilename
        self.wrapName = basename
        self.unwrapName = basename.replace('.flat', '.unw')

        ###To deal with missing filt_*.cor
        if basename.startswith('filt_'):
            self.corName  = basename.replace('.flat', '.cor')[5:]
        else:
            self.corName  = basename.replace('.flat', '.cor')
   
            self.width = obj.insar.resampIntImage.width

#   print("Wrap: ", self.wrapName)
#   print("Unwrap: ", self.unwrapName)
#   print("Coh: ", self.corName)
#   print("Width: ", self.width)


    def unwrap(self):
   
        with isceobj.contextIntImage(
            filename=self.wrapName,
            width=self.width,
            accessMode='read') as intImage:

            with isceobj.contextOffsetImage(
                filename=self.corName,
                width = self.width,
                accessMode='read') as cohImage:


                with isceobj.contextIntImage(
                    filename=self.unwrapName,
                    width = self.width,
                    accessMode='write') as unwImage:

                    grs=Grass()
                    grs.wireInputPort(name='interferogram',
                        object=intImage)
                    grs.wireInputPort(name='correlation',
                        object=cohImage)
                    grs.wireOutputPort(name='unwrapped interferogram',
                        object=unwImage)
                    grs.unwrap()
                    unwImage.renderHdr()

                    pass
                pass
            pass
    
        return None
