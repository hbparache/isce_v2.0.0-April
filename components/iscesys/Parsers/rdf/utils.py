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




"""Non RDF specific python helpers"""
## \namespace rdf.utils Non-RDF specific utilities

## Generate non-zero entries from an ASCII file
## \param src Is the source file name
## \param purge = True reject blanks (unless False)
## \retval< <a href="https://wiki.python.org/moin/Generators">Generator</a> 
## that generates (nonzero) lines for an ASCII file
def read_file(src):
    """src --> src file name
    purge=True igonors black lines"""
    with open(src, 'r') as fsrc:
        for line in read_stream(fsrc):
            yield line

## Yield stripped lines from a file
## \param fsrc A readable file-like object
## \retval< <a href="https://wiki.python.org/moin/Generators">Generator</a> 
## that generates fsrc.readline() (stripped).
def read_stream(fsrc):
    """Generate lines from a stream (fsrc)"""
    tell = fsrc.tell()
    line = fsrc.readline().strip()
    while tell != fsrc.tell() or line:
        yield line
        tell = fsrc.tell()
        line = fsrc.readline().strip()

