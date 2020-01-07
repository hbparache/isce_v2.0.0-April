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
# Author: Eric Belz
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




## \namespace rdf.read Reading Functions
"""(Lazy) Functions to read rdf files and yield unwrapped lines"""

from __future__ import absolute_import

import itertools

from . import utils
from .reserved import glyphs

## unwrap lines from a generator
# \param gline A iteratable that pops file lines (rdf.utils.read_file())
# \param wrap = rdf.reserved.glyphs.WRAP The line coninutation character
# \retval< <a href="https://wiki.python.org/moin/Generators">Generator</a>
# that generates complete RDF input lines.
def _unwrap_lines(gline, wrap=glyphs.WRAP):
    """given a read_stream() generator, yield UNWRAPPED RDF lines"""
    while True:
        line = next(gline)
        while line.endswith(wrap):
            line = line[:-len(wrap)] + next(gline)
        yield line

## file name --> unwrapped lines
# \param src A file name
# \param wrap = rdf.reserved.glyphs.WRAP The line coninutation character
# \retval< <a href="https://wiki.python.org/moin/Generators">Generator</a>
# that generates complete RDF input lines.
def unwrap_file(src, wrap=glyphs.WRAP):
    """Take a file name (src) and yield unwrapped lines"""
    return filter(
        bool,
        _unwrap_lines(utils.read_file(src), wrap=wrap)
        )
