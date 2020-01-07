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



# Comment: Adapted from InsarProc/extractInfo.py by Brett George
from contrib.frameUtils.FrameInfoExtractor import FrameInfoExtractor
import logging
logger = logging.getLogger('isce.isceProc.ExtractInfo')


def extractInfo(self, frames):
    FIE = FrameInfoExtractor()
    infos = []
    for frame in frames:
        infos.append(FIE.extractInfoFromFrame(frame))

    mainInfo = infos[0]
    mainInfo.sensingStart = [ info.sensingStart for info in infos ]
    mainInfo.sensingStop = [ info.sensingStop for info in infos ]

    # for stitched frames do not make sense anymore
    bbs = [ info.getBBox() for info in infos ]
    bbxy = {}
    for x in range(4):
        bbxy[x] = {}
        for y in range(2):
            bbxy[x][y] = [ bb[x][y] for bb in bbs ]
    latEarlyNear = bbxy[0][0][0]
    latLateNear = bbxy[2][0][0]

    #figure out which one is the bottom
    if latEarlyNear > latLateNear:
        #early is the top
        ret = []
        # the calculation computes the minimum bbox. it is not exact, but given
        # the approximation in the estimate of the corners, it's ok
        for x, op1, op2 in zip(range(4), (min, min, max, max), (max, min, max, min)):
            ret.append([op1(bbxy[x][0]), op2(bbxy[x][1])])
    else:
        # late is the top
        ret = []
        for x, op1, op2 in zip(range(4), (max, max, min, min), (max, min, max, min)):
            ret.append([op1(bbxy[x][0]), op2(bbxy[x][1])])

    mainInfo.bbox = ret
    return mainInfo
    # the track should be the same for all

