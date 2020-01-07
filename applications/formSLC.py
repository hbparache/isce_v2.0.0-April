#!/usr/bin/env python3 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2011 to the present, california institute of technology.
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





from iscesys.Compatibility import Compatibility
Compatibility.checkPythonVersion()

from iscesys.Component.FactoryInit import FactoryInit
class FormSLCApp(FactoryInit):
    
  def main(self):
    self.objFormSlc.formSLCImage(self.objRaw,self.objSlc)
    print('second time')
    self.objFormSlc.formSLCImage(self.objRaw,self.objSlc)
    self.objSlc.finalizeImage()
    self.objRaw.finalizeImage()
    return
  
  def __init__(self, arglist):
    FactoryInit.__init__(self)
    self.initFactory(arglist)
    self.objSlc = self.getComponent('SlcImage')
    self.objSlc.createImage()
    self.objRaw = self.getComponent('RawImage')
    self.objRaw.createImage()
    self.objFormSlc = self.getComponent('FormSlc')        
    return
    
if __name__ == "__main__":
  import sys    
  runObj = FormSLCApp(sys.argv[1:])
  runObj.main()
    
