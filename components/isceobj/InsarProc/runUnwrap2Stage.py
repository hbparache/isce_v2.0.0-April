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
# Author: Ravi Lanka
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# giangi: taken Piyush code for snaphu and adapted

import sys
import isceobj

from contrib.UnwrapComp.unwrapComponents import UnwrapComponents

def runUnwrap2Stage(self, unwrapper_2stage_name=None, solver_2stage=None):

    if unwrapper_2stage_name is None:
        unwrapper_2stage_name = 'REDARC0'
    
    if solver_2stage is None:
        # If unwrapper_2state_name is MCF then solver is ignored
        # and relaxIV MCF solver is used by default
        solver_2stage = 'pulp'
    
    print('Unwrap 2 Stage Settings:')
    print('Name: %s'%unwrapper_2stage_name)
    print('Solver: %s'%solver_2stage)

    inpFile = self.insar.unwrappedIntFilename
    ccFile  = self.insar.connectedComponentsFilename
    outFile = self.insar.unwrapped2StageFilename

    # Hand over to 2Stage unwrap
    unw = UnwrapComponents()
    unw.setInpFile(inpFile)
    unw.setConnCompFile(ccFile)
    unw.setOutFile(outFile)
    unw.setSolver(solver_2stage)
    unw.setRedArcs(unwrapper_2stage_name)
    unw.unwrapComponents()
    return
