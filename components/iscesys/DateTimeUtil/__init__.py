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
# Author: Eric Belz
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



"""Date and Time utilites, on top of the datetime standard library.

New Usage:

>>>from iscesys import DateTimeUtil as DTU

replaces former usage:

>>>from iscesys.DateTimeUtil.DateTimeUtil import DateTimeUtil as DTU

Note, both:

javaStyleUtils()   and   pythonic_utils()

are available.
"""
from .DateTimeUtil import timedelta_to_seconds, seconds_since_midnight, date_time_to_decimal_year

## JavaStyleNames for the pythonic_names
timeDeltaToSeconds = timedelta_to_seconds
secondsSinceMidnight =  seconds_since_midnight
dateTimeToDecimalYear = date_time_to_decimal_year
