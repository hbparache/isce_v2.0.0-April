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




## \namespace rdf.language.lexis The Lexis comprises the words in the language.
import abc

## The Pragamtic's are RDF lines meaning.
class Word(str):
    """Word is an ABC that subclasses str. It has a call
    that dyamically dispatches args = (line, grammar) to
    the sub classes' sin qua non method-- which is the
    method that allows them to do their business.
    """

    __metaclass__ = abc.ABCMeta

    # Call the Pragamtic's 'sin_qua_non' method -which is TBDD \n
    # (To be Dynamically Dispathed ;-)
    def __call__(self, line, grammar):
        return self.sin_qua_non(line, grammar)

    @abc.abstractmethod
    def sin_qua_non(self, line, grammar):
        pass
