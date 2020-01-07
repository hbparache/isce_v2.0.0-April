#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2014 to the present, california institute of technology.
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



# Comment: Adapted from InsarProc/runUnwrapGrass.py
import logging
import isceobj
from iscesys.Component.Component import Component
from mroipac.grass.grass import Grass
import os
# giangi: taken Piyush code grass.py and adapted

logger = logging.getLogger('isce.isceProc.runUnwrap')

def runUnwrap(self):
    infos = {}
    for attribute in ['topophaseFlatFilename', 'unwrappedIntFilename', 'coherenceFilename']:
        infos[attribute] = getattr(self._isce, attribute)

    for sceneid1, sceneid2 in self._isce.selectedPairs:
        pair = (sceneid1, sceneid2)
        for pol in self._isce.selectedPols:
            intImage = self._isce.resampIntImages[pair][pol]
            width = intImage.width
            sid = self._isce.formatname(pair, pol)
            infos['outputPath'] = os.path.join(self.getoutputdir(sceneid1, sceneid2), sid)
            run(width, infos, sceneid=sid)


def run(width, infos, sceneid='NO_ID'):
    logger.info("Unwrapping interferogram using Grass: %s" % sceneid)
    wrapName   = infos['outputPath'] + '.' + infos['topophaseFlatFilename']
    unwrapName = infos['outputPath'] + '.' + infos['unwrappedIntFilename']
    corName    = infos['outputPath'] + '.' + infos['coherenceFilename']

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

