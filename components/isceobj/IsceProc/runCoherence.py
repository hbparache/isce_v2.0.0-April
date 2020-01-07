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



# Comment: Adapted from InsarProc/runCoherence.py
import logging
import operator
import isceobj
import sys
import os

from iscesys.ImageUtil.ImageUtil import ImageUtil as IU
from mroipac.correlation.correlation import Correlation

logger = logging.getLogger('isce.isceProc.runCoherence')

## mapping from algorithm method to Correlation instance method name
CORRELATION_METHOD = {
    'phase_gradient' : operator.methodcaller('calculateEffectiveCorrelation'),
    'cchz_wave' : operator.methodcaller('calculateCorrelation')
    }

def runCoherence(self, method="phase_gradient"):
    # correlation method is checked here, to raise an error as soon as possible
    if method not in CORRELATION_METHOD.keys():
        sys.exit("Unrecognized correlation method in runCoherence: %s" % method)

    infos = {}
    for attribute in ['topophaseFlatFilename']:
        infos[attribute] = getattr(self._isce, attribute)

    stdWriter = self._stdWriter

    for sceneid1, sceneid2 in self._isce.selectedPairs:
        pair = (sceneid1, sceneid2)
        resampAmpImages = self._isce.resampAmpImages[pair]
        widthInt = self._isce.resampIntImages[pair][self._isce.refPol].getWidth()
        for pol in self._isce.selectedPols:
            ampImage = resampAmpImages[pol].copy(access_mode='read')
            sid = self._isce.formatname(pair, pol)
            infos['outputPath'] = os.path.join(self.getoutputdir(sceneid1, sceneid2), sid)
            catalog = isceobj.Catalog.createCatalog(self._isce.procDoc.name)
            run(method, ampImage, widthInt, infos, stdWriter, catalog=catalog, sceneid=sid)
            self._isce.procDoc.addAllFromCatalog(catalog)


def run(method, ampImage, widthInt, infos, stdWriter, catalog=None, sceneid='NO_ID'):
    logger.info("Calculating Coherence: %s" % sceneid)

    # Initialize the flattened inteferogram
    topoflatIntFilename = infos['outputPath'] + '.' + infos['topophaseFlatFilename']
    intImage = isceobj.createIntImage()
    intImage.setFilename(topoflatIntFilename)
    intImage.setWidth(widthInt)
    intImage.setAccessMode('read')
    intImage.createImage()

    # Create the coherence image
    cohFilename = topoflatIntFilename.replace('.flat', '.cor')
    cohImage = isceobj.createOffsetImage()
    cohImage.setFilename(cohFilename)
    cohImage.setWidth(widthInt)
    cohImage.setAccessMode('write')
    cohImage.createImage()

    cor = Correlation()
    cor.configure()
    cor.wireInputPort(name='interferogram', object=intImage)
    cor.wireInputPort(name='amplitude', object=ampImage)
    cor.wireOutputPort(name='correlation', object=cohImage)

    try:
        CORRELATION_METHOD[method](cor)
    except KeyError:
        print("Unrecognized correlation method")
        sys.exit(1)
        pass
    return None
