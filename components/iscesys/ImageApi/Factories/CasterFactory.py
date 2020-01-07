#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2010 to the present, california institute of technology.
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



from __future__ import print_function
import sys
import math
import logging

dataTypesReal = ['BYTE','CHAR','SHORT','INT','LONG','FLOAT','DOUBLE']
dataTypesCpx = ['CBYTE','CCHAR','CSHORT','CINT','CLONG','CFLOAT','CDOUBLE']

def getCaster(datain,dataout):
    suffix = 'Caster'
    #check for custom types first
    if(datain.upper() == 'CIQBYTE' and dataout.upper() == 'CFLOAT'):
        typein = 'IQByte'
        typeout = dataout[1:].lower().capitalize()
        suffix = 'CpxCaster'
    elif(datain.upper() in dataTypesReal and dataout.upper() in  dataTypesReal):
        typein = datain.lower().capitalize()
        typeout = dataout.lower().capitalize()
    elif(datain.upper() in dataTypesCpx and dataout.upper() in dataTypesCpx):
        typein = datain[1:].lower().capitalize()
        typeout = dataout[1:].lower().capitalize()
        suffix = 'CpxCaster'
    else:
        print('Casting only allowed between compatible types and not',datain,'and',dataout)  
        raise ValueError
    if typein == typeout:
        caster = ''
    else:
        caster = typein + 'To' + typeout + suffix
    return caster
