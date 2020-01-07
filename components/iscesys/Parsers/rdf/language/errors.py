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




"""RDF Exceptions"""
## \namespace rdf.language.errors RDF Exceptions


## Fatal attempt to CODE badly
class RDFError(Exception):
    """Base RDF Error for BAD RDF coding (Fatal)"""
    
## <a href="http://en.wikipedia.org/wiki/Speech_error">Morphere Exchange
## Currents</a>?
class MorphemeExchangeError(RDFError):
    """fix-pre and/or sufix would cast list v. str type errors on "+" 
    anyway, so this is a TypeError
    """

class FatalUnitError(RDFError):
    """raise for unregocnized units (fatally)"""


## RDF Warning of INPUT problems
class RDFWarning(Warning):
    """Base RDF Warning for bad RDF input grammar"""
    
    
class UnknownUnitWarning(Warning):
    """Unrecognized unit (ignored)"""
    
    
## RDF Error for a unit problem (not sure what kind of error this is)
class UnitsError(RDFWarning, ValueError):
    """Raised for a non-existent unit"""

    
## Error for using a character in RESERVED
class ReservedCharacterError(RDFWarning):
    """Error for using a RESERVED character badly"""

    
## Unmatched or un parsable pairs
class UnmatchedBracketsError(ReservedCharacterError):
    """1/2 a delimeter was used"""

    
## Unmatched or un parsable pairs
class RunOnSentenceError(ReservedCharacterError):
    """Too many punctuation marks"""

    
## Unmatched or un parsable pairs
class BackwardBracketsError(ReservedCharacterError):
    """Inverted Punctuation"""

    
## Should be thrown in constructor?
class NullCommandError(RDFWarning):
    """Setting a required command to nothing"""


