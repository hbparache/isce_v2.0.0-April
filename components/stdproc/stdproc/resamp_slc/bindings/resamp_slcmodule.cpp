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




#include <Python.h>
#include "resamp_slcmodule.h"
#include <cmath>
#include <sstream>
#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
using namespace std;

static const char * const __doc__ = "Python extension for resamp_slc.F";

PyModuleDef moduledef = {
    // header
    PyModuleDef_HEAD_INIT,
    // name of the module
    "resamp_slc",
    // module documentation string
    __doc__,
    // size of the per-interpreter state of the module;
    // -1 if this state is global
    -1,
    resamp_slc_methods,
};

// initialization function for the module
// *must* be called PyInit_resamp_slc
PyMODINIT_FUNC
PyInit_resamp_slc()
{
    // create the module using moduledef struct defined above
    PyObject * module = PyModule_Create(&moduledef);
    // check whether module creation succeeded and raise an exception if not
    if (!module) {
        return module;
    }
    // otherwise, we have an initialized module
    // and return the newly created module
    return module;
}

PyObject * resamp_slc_C(PyObject* self, PyObject* args)
{
    uint64_t var0;
    uint64_t var1;
    uint64_t var2;
    uint64_t var3;
    if(!PyArg_ParseTuple(args, "KKKK",&var0,&var1,&var2,&var3))
    {
        return NULL;
    }
    resamp_slc_f(&var0,&var1,&var2,&var3);
    return Py_BuildValue("i", 0);
}
PyObject * setInputWidth_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setInputWidth_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setOutputWidth_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setOutputWidth_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setInputLines_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setInputLines_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setOutputLines_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setOutputLines_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject *  setIsComplex_C(PyObject * self, PyObject *args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setIsComplex_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject* setMethod_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setMethod_f(&var);
    return Py_BuildValue("i",0);
}

PyObject* setFlatten_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setFlatten_f(&var);
    return Py_BuildValue("i",0);
}

PyObject * setRadarWavelength_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setRadarWavelength_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject * setReferenceWavelength_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setReferenceWavelength_f(&var);
    return Py_BuildValue("i", 0);
}


PyObject * setSlantRangePixelSpacing_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setSlantRangePixelSpacing_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject * setReferenceSlantRangePixelSpacing_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setReferenceSlantRangePixelSpacing_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject * setAzimuthCarrier_C(PyObject* self, PyObject* args)
{
    cPoly2d* poly;
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K",&var))
    {
        return NULL;
    }
    poly = (cPoly2d*) var;
    setAzimuthCarrier_f(poly);
    return Py_BuildValue("i",0);
}

PyObject * setRangeCarrier_C(PyObject* self, PyObject* args)
{
    cPoly2d* poly;
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K",&var))
    {
        return NULL;
    }
    poly = (cPoly2d*) var;
    setRangeCarrier_f(poly);
    return Py_BuildValue("i", 0);
}

PyObject * setAzimuthOffsetsPoly_C(PyObject* self, PyObject *args)
{
    cPoly2d* poly;
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    poly = (cPoly2d*) var;
    setAzimuthOffsetsPoly_f(poly);
    return Py_BuildValue("i",0);
}

PyObject *setRangeOffsetsPoly_C(PyObject* self, PyObject *args)
{
    cPoly2d* poly;
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    poly = (cPoly2d*) var;
    setRangeOffsetsPoly_f(poly);
    return Py_BuildValue("i", 0);
}

PyObject *setDopplerPoly_C(PyObject* self, PyObject *args)
{
    cPoly2d* poly;
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K", &var))
    {
        return NULL;
    }
    poly = (cPoly2d*) var;
    setDopplerPoly_f(poly);
    return Py_BuildValue("i", 0);
}

PyObject * setStartingRange_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setStartingRange_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject * setReferenceStartingRange_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setReferenceStartingRange_f(&var);
    return Py_BuildValue("i", 0);
}

// end of file
