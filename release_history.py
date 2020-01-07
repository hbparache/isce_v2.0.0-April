#!/usr/bin/env python3

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
# Author: Eric Gurrola
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




import collections

Tag = collections.namedtuple('Tag', 'version svn_revision yyyymmdd')

releases = (Tag('1.0.0',   '739', '20120814'),
            Tag('1.5.0',  '1180', '20131018'),
            Tag('1.5.01', '1191', '20131028'),
            Tag('2.0.0',  '1554', '20140724'),
            Tag('2.0.0_201409',  '1612', '20140918'),
            Tag('2.0.0_201410',  '1651', '20141103'),
            Tag('2.0.0_201505',  '1733', '20150504'),
            Tag('2.0.0_201506',  '1783', '20150619'),
            Tag('2.0.0_201511',  '1917', '20151123'),
            Tag('2.0.0_201512',  '1931', '20151221'),
            Tag('2.0.0_201604',  '2047', '20160426'),
            Tag('2.0.0_201604_dempatch', '2118:2047', '20160727'),
            Tag('2.0.0_201609',  '2143', '20160903'),
            Tag('2.0.0_20160906',  '2145', '20160906'),
            Tag('2.0.0_20160908',  '2150', '20160908'),
            Tag('2.0.0_20160912',  '2153', '20160912'),
            Tag('2.0.0_20170403',  '2256', '20170403'))

#Note: 2.0.0_201604_dempatch only changed the following files:
#    release_history.py
#    contrib/demUtils/demstitcher/DemStitcher.py
#    contrib/demUtils/demstitcher/DemStitcherV3.py
#    contrib/demUtils/swbdstitcher/SWBDStitcher.py
#    components/iscesys/DataRetriever/DataRetriever.py


release_version = releases[-1].version
release_svn_revision = releases[-1].svn_revision
release_date = releases[-1].yyyymmdd
