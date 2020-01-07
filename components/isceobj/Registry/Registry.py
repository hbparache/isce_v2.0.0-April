#!/usr/bin/env python3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  copyright: 2014 to the present, california institute of technology.
#  all rights reserved. united states government sponsorship acknowledged.
#  any commercial use must be negotiated with the office of technology transfer
#  at the california institute of technology.
#  
#  this software may be subject to u.s. export control laws. by accepting this
#  software, the user agrees to comply with all applicable u.s. export laws and
#  regulations. user has the responsibility to obtain export licenses,  or other
#  export authority as may be required before exporting such information to
#  foreign countries or providing access to foreign persons.
#  
#  installation and use of this software is restricted by a license agreement
#  between the licensee and the california institute of technology. it is the
#  user's responsibility to abide by the terms of the license agreement.
# 
#  Authors: Giangi Sacco, Eric Gurrola
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from collections import OrderedDict
import sys
class Registry:
    class __Registry:
        _registry = None
        _template = None
        def __init__(self):
            #define the keyword used to specify the actual filename
            self._filename = 'name'
            if self._registry is None:
                self._registry = OrderedDict()
            if self._template is None:
                self._template = OrderedDict()
        def _addToDict(self,dictIn,args):
            if(len(args) == 2):#reach the end
                #the last element is a string
                if(isinstance(args[0],str)):
                    dictIn[args[0]] = args[1]
            else:
                if not args[0] in dictIn:
                    dictIn[args[0]] = OrderedDict()
                self._addToDict(dictIn[args[0]],args[1:])

        def _toTuple(self,root,kwargs):
            ret = []
            for k in self._template[root]:
                for k1,v1 in kwargs.items():
                    if(k == k1):
                        ret.append(v1)
                        break
            return tuple(ret)
        def _getFromDict(self,dictIn,args):
            ret  = None
            if(len(args) == 1):
                ret = dictIn[args[0]]
            else:
                ret = self._getFromDict(dictIn[args[0]],args[1:])
            return ret
        def get(self,root,*args,**kwargs):
            ret = self._registry[root]
            if(args):
                ret = self._getFromDict(self._registry[root],args)
            #allow to get values using kwargs so order does not need to be respected
            elif(kwargs):
                argsNow = self._toTuple(root,kwargs)
                ret = self._getFromDict(self._registry[root],args)
            return ret

        def set(self,root,*args,**kwargs):
            #always need to specify the root node
            if not root in self._registry:
                self._registry[root] = OrderedDict()
            if(args):
                self._addToDict(self._registry[root],args)
            #allow to set values using kwargs so order does not need to be respected
            elif(kwargs):
                argsNow = self._toTuple(root,kwargs)
                self._addToDict(self._registry[root],argsNow)




    _instance = None
    def __new__(cls,*args):
        if not cls._instance:
            cls._instance = Registry.__Registry()
        #assume that if args is provided then it creates the template
        if(args):
            argsNow = list(args[1:])
            argsNow.append(cls._instance._filename)
            cls._instance._template[args[0]] = tuple(argsNow)



        return cls._instance
def printD(dictIn,tabn):
    for k,v in dictIn.items():
        print('\t'*tabn[0] + k)
        if(isinstance(v,OrderedDict)):
            tabn[0] += 1
            printD(v,tabn)
        else:
            if not v:
                print('\t'*(tabn[0] + 1) + 'not set yet\n')
            else:
                print('\t'*(tabn[0] + 1) + v + '\n')

    tabn[0] -= 1


def main():
    #create template
    rg = Registry('imageslc','sceneid','pol')
    #add node {'imageslc':{'alos1':{'hh':'image_alos1_hh'} using set
    rg.set('imageslc',pol='hh',sceneid='alos1',name='image_alos1_hh')
    tabn = [0]
    printD(rg._registry['imageslc'],tabn)
    pols = rg.get('imageslc','alos1')
    #add node  {'alos1':{'vv':'image_alos1_vv'} using dict syntax
    pols['vv'] = 'image_alos1_hh'
    tabn = [0]
    printD(rg.get('imageslc'),tabn)
    #add alos2 using positinal
    rg.set('imageslc','alos2','hh','image_alos2_hh')
    tabn = [0]
    printD(rg.get('imageslc'),tabn)
    #change value to test that also the underlying _registry changed
    pols['hh'] = 'I have been changed'
    tabn = [0]
    printD(rg.get('imageslc'),tabn)
    '''
    rg = Registry('imageslc','alos1','hh')
    tabn = [0]
    printD(rg,tabn)
    rg['alos1']['hh'] = 'slc_alos1_hh'
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg = Registry('imageslc','alos1','hv')
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg['alos1']['hv'] = 'slc_alos1_hv'
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg = Registry('imageslc','alos2','hh')
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg['alos2']['hh'] = 'slc_alos2_hh'
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg = Registry('imageslc','alos2','hv')
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    rg['alos2']['hv'] = 'slc_alos2_hv'
    tabn = [0]
    print('***********\n')
    printD(rg,tabn)
    '''
if __name__ == '__main__':
    sys.exit(main())
