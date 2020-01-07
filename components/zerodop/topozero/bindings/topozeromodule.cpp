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




#include <Python.h>
#include "topozeromodule.h"
#include <cmath>
#include <sstream>
#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
using namespace std;

static const char * const __doc__ = "Python extension for topo.F";

PyModuleDef moduledef = {
    //header
    PyModuleDef_HEAD_INIT,
    //name of the module
    "topozero",
    //module documentation string
    __doc__,
    //size of the per-interpreter state of the module
    //-1 if this state is global
    -1,
    topozero_methods,
};

//initialization function for the module
//// *must* be called PyInit_topo
PyMODINIT_FUNC
PyInit_topozero()
{
    //create the module using moduledef struct defined above
    PyObject * module = PyModule_Create(&moduledef);
    //check whether module create succeeded and raise exception if not
    if(!module)
    {
        return module;
    }
    //otherwise we have an initialized module
    //and return the newly created module
    return module;
}

PyObject * topo_C(PyObject* self, PyObject* args)
{
    uint64_t var0,var1,var2;
    if(!PyArg_ParseTuple(args, "KKK",&var0,&var1,&var2))
    {
        return NULL;
    }
    topo_f(&var0,&var1,&var2);
    return Py_BuildValue("i", 0);
}
PyObject * setNumberIterations_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setNumberIterations_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setDemWidth_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setDemWidth_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setDemLength_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setDemLength_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setOrbit_C(PyObject* self, PyObject* args)
{
    uint64_t orbPtr;
    cOrbit* ptr;
    if(!PyArg_ParseTuple(args, "K", &orbPtr))
    {
        return NULL;
    }

    ptr = (cOrbit*) orbPtr;
    setOrbit_f(ptr);
    return Py_BuildValue("i", 0);
}

PyObject * setFirstLatitude_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setFirstLatitude_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setFirstLongitude_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setFirstLongitude_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setDeltaLatitude_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setDeltaLatitude_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setDeltaLongitude_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setDeltaLongitude_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setEllipsoidMajorSemiAxis_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setEllipsoidMajorSemiAxis_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setEllipsoidEccentricitySquared_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setEllipsoidEccentricitySquared_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setLength_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setLength_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setWidth_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setWidth_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setRangePixelSpacing_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setRangePixelSpacing_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setRangeFirstSample_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setRangeFirstSample_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setLookSide_C(PyObject* self, PyObject *args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
    return NULL;
    }
    setLookSide_f(&var);
    return Py_BuildValue("i",0);
}
PyObject * setNumberRangeLooks_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setNumberRangeLooks_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setNumberAzimuthLooks_C(PyObject* self, PyObject* args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setNumberAzimuthLooks_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setPegHeading_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setPegHeading_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setPRF_C(PyObject* self, PyObject* args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setPRF_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setSensingStart_C(PyObject* self, PyObject *args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setSensingStart_f(&var);
    return Py_BuildValue("i", 0);
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
PyObject * setLatitudePointer_C(PyObject* self, PyObject* args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    setLatitudePointer_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setLongitudePointer_C(PyObject* self, PyObject* args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    setLongitudePointer_f(&var);
    return Py_BuildValue("i", 0);
}

PyObject * setHeightPointer_C(PyObject* self, PyObject* args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    setHeightPointer_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * setLosPointer_C(PyObject* self, PyObject *args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K", &var))
    {
    return NULL;
    }
    setLosPointer_f(&var);
    return Py_BuildValue("i",0);
}
PyObject * setIncPointer_C(PyObject* self, PyObject *args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K", &var))
    {
    return NULL;
    }
    setIncPointer_f(&var);
    return Py_BuildValue("i",0);
}
PyObject * setMaskPointer_C(PyObject* self, PyObject *args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args,"K", &var))
    {
        return NULL;
    }
    setMaskPointer_f(&var);
    return Py_BuildValue("i",0);
}
PyObject * getMinimumLatitude_C(PyObject* self, PyObject* args)
{
    double var;
    getMinimumLatitude_f(&var);
    return Py_BuildValue("d",var);
}
PyObject * getMinimumLongitude_C(PyObject* self, PyObject* args)
{
    double var;
    getMinimumLongitude_f(&var);
    return Py_BuildValue("d",var);
}
PyObject * getMaximumLatitude_C(PyObject* self, PyObject* args)
{
    double var;
    getMaximumLatitude_f(&var);
    return Py_BuildValue("d",var);
}
PyObject * getMaximumLongitude_C(PyObject* self, PyObject* args)
{
    double var;
    getMaximumLongitude_f(&var);
    return Py_BuildValue("d",var);
}
PyObject * setSecondaryIterations_C(PyObject* self, PyObject *args)
{
    int var;
    if(!PyArg_ParseTuple(args, "i", &var))
    {
        return NULL;
    }
    setSecondaryIterations_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject *setThreshold_C(PyObject* self, PyObject *args)
{
    double var;
    if(!PyArg_ParseTuple(args, "d", &var))
    {
        return NULL;
    }
    setThreshold_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject *setMethod_C(PyObject* self, PyObject *args)
{
    int var;
    if(!PyArg_ParseTuple(args,"i",&var))
    {
        return NULL;
    }
    setMethod_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject *setOrbitMethod_C(PyObject* self, PyObject *args)
{
    int var;
    if(!PyArg_ParseTuple(args,"i",&var))
    {
        return NULL;
    }
    setOrbitMethod_f(&var);
    return Py_BuildValue("i", 0);
}

// end of file
