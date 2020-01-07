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
# Authors: Kosal Khun, Marco Lavalle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



from __future__ import print_function
import sys
from iscesys.Component.Component import Component


NB_SCENES = 100 # number of scenes and rasters that can be processed

class Stack(Component):
    """
    Stack scenes, used for processing.
    """
    # We have to suppose that there will be 100 scenes and 100 rasters,
    # which ids range from 1 to 100, and add them to the dictionary of variables
    # to fully take advantage of the parser.
    # If we happend to accept more scenes (or rasters), we have to change NB_SCENES,
    # that also applies to the number of rasters.

    def __init__(self, family=None, name=None):
        """
        Instantiate a stack.
        """
        super(Stack, self).__init__(family, name)
        self.scenes = {} ##contains all the scenes (for each selected scene and pol)
        self._ignoreMissing = True #ML 2014-05-08 with GNG

        self.dictionaryOfVariables = {}
        for attr in ['SCENE', 'RASTER']:
            for i in range(1, NB_SCENES+1):
                key = attr + str(i)
                self.dictionaryOfVariables[key] =  [key.lower(), dict, False]



    def addscene(self, scene):
        """
        Add a scene dictionary to the stack.
        """
        if not isinstance(scene, dict): ##scene is not a dictionary
            sys.exit("Scene must be a dictionary")
        else:
            sceneid = scene['id']
            self.scenes[sceneid] = scene


    def getscenes(self):
        """
        Return the scenes inside the stack.
        """
        return self.scenes
