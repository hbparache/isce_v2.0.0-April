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




"""eRdf Experimental RDF stuff- no warranty"""
## \namespace rdf.eRDF __e__ xperimental RDF objects



## A generic base class for RDF wrapped data structures -clients should
## use this when they have an object with RDF dependency injection and then
## further behavior as defined by the sub-classes methods.
class RDFWrapper(object):
    """RDFWrapper(rdf instance):

    is a base class for classes that wrap rdf instances.
    """
    
    ## Initialized with an RDF instance
    ## \param rdf_ a bonafide rdf.data.files.RDF object
    def __init__(self, rdf_):
        ## The wrapped rdf 
        self._rdf = rdf_
        return None
    
    ## self.rdf == self.rdf() == self._rdf
    @property
    def rdf(self):
        return self._rdf

    ## Access rdf dictionary
    def __getitem__(self, key):
        return self._rdf.__getitem__(self, key)
    
    ## Access rdf dictionary
    def __setitem__(self, key, field):
        return self._rdf.__setitem__(self, key, field)
    
    ## Access rdf dictionary
    def __delitem__(self, key):
        return self._rdf.__delitem__(self, key)
    
    ## Access rdf dictionary
    def __len__(self, key):
        return len(self._rdf)
    
    
    
## Experimental function to factor keys and rdf.
def factor(rdf_):
    _k = rdf_.keys()
    _k.sort()
    k = _k[:]
    longest = max(map(len, k))
    import numpy as np
    m = np.zeros( (len(k), 27 ), dtype=int )
    for jdx, key in enumerate(k):
        for idx, cc in enumerate(key):
            m[jdx, idx] = ord(cc)
    base = [2**__ for __ in map(long, range(len(m[0])))]
    

