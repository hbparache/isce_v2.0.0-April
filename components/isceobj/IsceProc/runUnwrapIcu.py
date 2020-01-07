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



# Comment: Adapted from InsarProc/UnwrapIcu.py
import logging
import isceobj
from mroipac.icu.Icu import Icu
import os
# giangi: taken Piyush code grass.py and adapted
logger = logging.getLogger('isce.isceProc.runUnwrap')

def runUnwrap(self):
    infos = {}
    for attribute in ['topophaseFlatFilename', 'unwrappedIntFilename']:
        infos[attribute] = getattr(self._isce, attribute)

    for sceneid1, sceneid2 in self._isce.selectedPairs:
        pair = (sceneid1, sceneid2)
        for pol in self._isce.selectedPols:
            resampAmpImage = self._isce.resampAmpImages[pair][pol]
            sid = self._isce.formatname(pair, pol)
            infos['outputPath'] = os.path.join(self.getoutputdir(sceneid1, sceneid2), sid)
            run(resampAmpImage, infos, sceneid=sid)


def run(resampAmpImage, infos, sceneid='NO_ID'):
    logger.info("Unwrapping interferogram using ICU: %s" % sceneid)
    wrapName = infos['outputPath'] + '.' + infos['topophaseFlatFilename']
    unwrapName = infos['outputPath'] + '.' + infos['unwrappedIntFilename']

    #Setup images
    ampImage = resampAmpImage.copy(access_mode='read')
    width = ampImage.getWidth()

    #intImage
    intImage = isceobj.createIntImage()
    intImage.initImage(wrapName, 'read', width)
    intImage.createImage()

    #unwImage
    unwImage = isceobj.Image.createUnwImage()
    unwImage.setFilename(unwrapName)
    unwImage.setWidth(width)
    unwImage.imageType = 'unw'
    unwImage.bands = 2
    unwImage.scheme = 'BIL'
    unwImage.dataType = 'FLOAT'
    unwImage.setAccessMode('write')
    unwImage.createImage()

    #icuObj = Icu()
    #icuObj.filteringFlag = False      ##insarApp.py already filters it
    icuObj = Icu(name='insarapp_icu')
    icuObj.configure()
    icuObj.initCorrThreshold = 0.1
    icuObj.icu(intImage=intImage, ampImage=ampImage, unwImage = unwImage)

    ampImage.finalizeImage()
    intImage.finalizeImage()
    unwImage.finalizeImage()
    unwImage.renderHdr()

