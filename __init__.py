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

from .version import release_version, release_svn_revision, release_date
from .version import svn_revision

__version__ = release_version

import sys, os
isce_path = os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(1,isce_path)
sys.path.insert(1,os.path.join(isce_path,'applications'))
sys.path.insert(1,os.path.join(isce_path,'components'))
sys.path.insert(1,os.path.join(isce_path,'library'))

try:
    os.environ['ISCE_HOME']
except KeyError:
    print('Using default ISCE Path: %s'%(isce_path))
    os.environ['ISCE_HOME'] = isce_path
