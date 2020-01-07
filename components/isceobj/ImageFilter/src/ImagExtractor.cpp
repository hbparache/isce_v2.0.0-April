//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2010 to the present, california institute of technology.
// all rights reserved. united states government sponsorship acknowledged.
// any commercial use must be negotiated with the office of technology transfer
// at the california institute of technology.
// 
// this software may be subject to u.s. export control laws. by accepting this
// software, the user agrees to comply with all applicable u.s. export laws and
// regulations. user has the responsibility to obtain export licenses,  or other
// export authority as may be required before exporting such information to
// foreign countries or providing access to foreign persons.
// 
// installation and use of this software is restricted by a license agreement
// between the licensee and the california institute of technology. it is the
// user's responsibility to abide by the terms of the license agreement.
//
// Author: Giangi Sacco
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#include <iostream>
#include <limits>
#include <cmath>
#include "ImagExtractor.h"

using namespace std;

void ImagExtractor::extract()
{
    int eof = 1;
    //loop through the image. The DataType size is ImageIn->DataSizeIn.  
    int width = ImageIn->getWidth();  
    int bands = ImageIn->getBands();  
    int sizeIn = ImageIn->getSizeIn();  
    char * bufIn = new char[width*sizeIn*bands];
    char * bufOut = new char[width*(sizeIn/2)*bands];
    int cnt = StartLine;
    ImageIn->initSequentialAccessor(StartLine);
    while(true)
    {
        eof = ImageIn->getLineSequential(bufIn);
        ++cnt;
        if(eof < 0 || cnt > EndLine)
        {
            break;
        }
        for(int i = 0; i < width*bands; ++i)
        {
            //we don't know a priori the data type so at this point try to figure the right casting
            if(sizeIn/2 == sizeof(float))
            {
                float * mag = (float *) &bufIn[i*sizeIn];
                float * ph = (float *) &bufIn[i*sizeIn + sizeIn/2];
                float imag = (*mag)*sin((*ph));
                (* (float *) &bufOut[i*sizeIn/2]) = imag;
            }   
            else if(sizeIn/2 == sizeof(double))
            {
                double * mag = (double *) &bufIn[i*sizeIn];
                double * ph = (double *) &bufIn[i*sizeIn + sizeIn/2];
                double imag = (*mag)*sin((*ph));
                (* (double *) &bufOut[i*sizeIn/2]) = imag;
            }
            else
            {
                cout << "Datatype size not supported." << endl;
                ERR_MESSAGE;
            }
        }
        ImageOut->setLineSequential(bufOut);
    }
    delete [] bufIn;
    delete [] bufOut;
}

