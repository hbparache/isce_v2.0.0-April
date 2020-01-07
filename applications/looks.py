#!/usr/bin/env python3

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
# Author: Piyush Agram
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




import os
import logging
import sys

import isce
import argparse
from isceobj.Image import createImage,createDemImage
from mroipac.looks.Looks import Looks

class customArgparseFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''
    For better help message that also shows the defaults.
    '''
    pass

def cmdLineParse():
    '''
    Command Line Parser.
    '''
    parser = argparse.ArgumentParser(description='Take integer number of looks.',
            formatter_class=customArgparseFormatter,
            epilog = '''

Example: 

looks.py -i input.file -o output.file -r 4  -a 4
            
''')
    parser.add_argument('-i','--input', type=str, required=True, help='Input ISCEproduct with a corresponding .xml file.', dest='infile')
    parser.add_argument('-o','--output',type=str, default=None, help='Output ISCE DEproduct with a corresponding .xml file.', dest='outfile')
    parser.add_argument('-r', '--range', type=int, default=1, help='Number of range looks. Default: 1', dest='rglooks')
    parser.add_argument('-a', '--azimuth', type=int, default=1, help='Number of azimuth looks. Default: 1', dest='azlooks')

    values = parser.parse_args()
    if (values.rglooks == 1) and (values.azlooks == 1):
        print('Nothing to do. One look requested in each direction. Exiting ...')
        sys.exit(0)

    return values

def main(inps):
    '''
    The main driver.
    '''

    if inps.infile.endswith('.xml'):
        inFileXml = inps.infile
        inFile = os.path.splitext(inps.infile)[0]
    else:
        inFile = inps.infile
        inFileXml = inps.infile + '.xml'

    if inps.outfile is None:
        spl = os.path.splitext(inFile)
        ext = '.{0}alks_{1}rlks'.format(inps.azlooks, inps.rglooks)
        outFile = spl[0] + ext + spl[1]

    elif inps.outfile.endswith('.xml'):
        outFile = os.path.splitext(inps.outfile)[0]
    else:
        outFile = inps.outfile

 

    print('Output filename : {0}'.format(outFile))
    #hackish, just to know the image type to instantiate the correct type
    #until we put the info about how to generate the instance in the xml 
    from iscesys.Parsers.FileParserFactory import createFileParser
    FP = createFileParser('xml')
    tmpProp, tmpFact, tmpMisc = FP.parse(inFileXml)
    if('image_type' in tmpProp and tmpProp['image_type'] == 'dem'):        
        inImage = createDemImage()
    else:
        inImage = createImage()

    inImage.load(inFileXml)
    inImage.filename = inFile 

    lkObj = Looks()
    lkObj.setDownLooks(inps.azlooks)
    lkObj.setAcrossLooks(inps.rglooks)
    lkObj.setInputImage(inImage)
    lkObj.setOutputFilename(outFile)
    lkObj.looks()

    return outFile

if __name__ == '__main__':
    '''
    Makes the script executable.
    '''

    inps = cmdLineParse()
    main(inps)
