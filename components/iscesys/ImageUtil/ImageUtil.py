"""This module is a static class that needs to be refactor into an image
method..
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2010 to the present, california institute of technology.
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
# Author: Giangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



from __future__ import print_function
from iscesys.Compatibility import Compatibility

class ImageUtil:
    
    @staticmethod 
    def copyAttributes(fromIm,toIm, listAtt = None):
#        raise DeprecationWarning("No, not this one")
        if not (listAtt == None):
            listOfAttributes = listAtt
        else:
            listOfAttributes = ['bands','scheme','caster','width','filename','byteOrder','dataType','xmin','xmax','numberGoodBytes','firstLatitude','firstLongitude','deltaLatitude','deltaLongitude']
        for att in listOfAttributes:
            try:
                fromAtt = getattr(fromIm,att)
                setattr(toIm,att,fromAtt)
            except Exception:
                pass# the image might not have the attributes listed by default
     
    listOfAttributes = []

    ## The is the temporary that overwrite the previous functions-- it
    ## calls a method on the 1st arg-- which is why this must be a method.
    @staticmethod
    def copyAttributes(fromIm,toIm, listAtt=()):
        return fromIm.copy_attributes(toIm, *listAtt)
