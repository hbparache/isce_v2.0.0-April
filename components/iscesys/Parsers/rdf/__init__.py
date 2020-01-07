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



"""Usage:

Interactive:

>>>import rdf
>>>rdf_mapping = rdf.rdfparse("<src>")

Shell Script:

%python rdf/parse.py <src> > <dst>
"""
__author__ = "Eric Belz"
__copyright__ = "Copyright 2013,  by the California Institute of Technology."
__credits__ = ["Eric Belz", "Scott Shaffer"]
__license__ = NotImplemented
__version__ = "1.0.1"
__maintainer__ = "Eric Belz"
__email__ = "eric.belz@jpl.nasa.gov"
__status__ = "Production"

## \namespace rdf The rdf package
from .uRDF import rdf_reader, RDF


## Backwards compatible rdf readers.
rdfparse = rdf_reader
## less redundant parser
parse = rdf_reader


def test():
    """test() function - run from rdf/test"""
    import os
    rdf_ = rdfparse('rdf.txt')
    with open('new.rdf', 'w') as fdst:
        fdst.write(str(rdf_))
    if os.system("xdiff old.rdf new.rdf"):
        os.system("diff old.rdf new.rdf")
