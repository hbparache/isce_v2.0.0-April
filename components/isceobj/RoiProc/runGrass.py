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



import isceobj

from mroipac.grass.grass import Grass

## Interface to get class attributes's attributes that the function needs
def runGrass(self):
    return fGrass(self.insar.resampIntImage.width,
                  self.insar.topophaseFlatFilename)

## A fully context managed (2.6.x format) execution of the function
def fGrass(widthInt, topoflatIntFilename):

    with isceobj.contextIntImage(
        filename=topoflatIntFilename,
        width=widthInt,
        accessMode='read') as intImage:

        ## Note: filename is extecpted to  end in'.flat'- what
        ## if it doesn't??? Use:
        ## os.path.extsep + topoflatIntFilename.split(os.path.extsep)[-1]
        with isceobj.contextOffsetImage(
            filename=topoflatIntFilename.replace('.flat', '.cor'),
            width=widthInt,
            accessMode='write') as cohImage:
            
            with isceobj.contextIntImage(
                filename=topoflatIntFilename.replace('.flat', '.unw'),
                width=widthInt,
                accessMode='write') as unwImage:

                grass = Grass()
                grass.wireInputPort(name='interferogram', object=intImage)
                grass.wireInputPort(name='correlation', object=cohImage)
                grass.wireOutputPort(name='unwrapped interferogram', object=unwImage)
                grass.unwrap()
                
                pass
            pass
        pass
    return None
