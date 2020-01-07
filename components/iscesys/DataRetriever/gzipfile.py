#!/usr/bin/env python3

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
# Author: Giangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Author: Giangi Sacco
# Copyright 2012, 2015 by the California Institute of Technology.
# ALL RIGHTS RESERVED.
# United States Government Sponsorship acknowledged. Any commercial use must be
# negotiated with the Office of Technology Transfer at the
# California Institute of Technology.
#
import gzip
import os
def is_gzipfile(filename):
    fp = gzip.GzipFile(filename)
    #since it fails for non gz file just try and catch
    try:
        s = fp.read()
        ret = True
    except OSError:
        ret = False
    return ret
class GZipFile:
    def __init__(self,filename):
        self._filename = filename
    
    def extractall(self,path):
        try:
            os.mkdir(path)
        except Exception:
            pass
        fp = gzip.GzipFile(self._filename)
        s = fp.read()
        fp.close()
        #remove last extension
        fp = open(os.path.join(path,'.'.join(os.path.basename(self._filename).split('.')[:-1])),'wb')
        fp.write(s)
        fp.close()
        