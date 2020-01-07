//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2012 to the present, california institute of technology.
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




#ifndef filtermodule_h
#define filtermodule_h 1

#include <Python.h>
#include <complex>
#include "Image.hh"
#include "Filter.hh"
#include "header.h"

int meanFilterPhase(char *inFile, char *outFile, int imageWidth,
    int imageHeight,int filterWidth,int filterHeight);
int gaussianFilterPhase(char *inFile, char *outFile, int imageWidth,
    int imageHeight,int filterWidth,int filterHeight,double sigma);
int medianFilterPhase(char *inFile, char *outFile, int imageWidth,
    int imageHeight,int filterWidth,int filterHeight);

extern "C"
{
  PyObject *meanFilter_C(PyObject *self,PyObject *args);
  PyObject *gaussianFilter_C(PyObject *self,PyObject *args);
  PyObject *medianFilter_C(PyObject *self,PyObject *args);
}

static PyMethodDef filter_methods[] =
{
    {"meanFilter_Py",meanFilter_C,METH_VARARGS," "},
    {"gaussianFilter_Py",gaussianFilter_C,METH_VARARGS," "},
    {"medianFilter_Py",medianFilter_C,METH_VARARGS," "},
    {NULL,NULL,0,NULL}
};

#endif
