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




#ifndef crossmulmodule_h
#define crossmulmodule_h

#include <Python.h>
#include <stdint.h>
#include "crossmul.h"

extern "C"
{
    PyObject * createCrossMul_C(PyObject *, PyObject *);
    PyObject * setWidth_C(PyObject *, PyObject *);
    PyObject * setLength_C(PyObject *, PyObject *);
    PyObject * setLooksAcross_C(PyObject *, PyObject *);
    PyObject * setLooksDown_C(PyObject *, PyObject *);
    PyObject * setScale_C(PyObject *, PyObject *);
    PyObject * setBlocksize_C(PyObject *, PyObject *);
    PyObject * setWavelengths_C(PyObject *, PyObject *);
    PyObject * setSpacings_C(PyObject*, PyObject*);
    PyObject * setFlattenFlag_C(PyObject*, PyObject*);
    PyObject * setFilterWeight_C(PyObject*, PyObject*);
    void crossmul_f(crossmulState*, uint64_t*, uint64_t*, uint64_t*,
        uint64_t*);
    PyObject * crossmul_C(PyObject*, PyObject*);
    PyObject * destroyCrossMul_C(PyObject *, PyObject *);

}

static PyMethodDef crossmul_methods[] =
{
     {"createCrossMul_Py", createCrossMul_C, METH_VARARGS, " "},
     {"destroyCrossMul_Py", destroyCrossMul_C, METH_VARARGS, " "},
     {"setWidth_Py", setWidth_C, METH_VARARGS, " "},
     {"setLength_Py", setLength_C, METH_VARARGS, " "},
     {"setLooksAcross_Py", setLooksAcross_C, METH_VARARGS, " "},
     {"setLooksDown_Py", setLooksDown_C, METH_VARARGS, " "},
     {"setScale_Py", setScale_C, METH_VARARGS, " "},
     {"setBlocksize_Py", setBlocksize_C, METH_VARARGS, " "},
     {"setWavelengths_Py", setWavelengths_C, METH_VARARGS, " "},
     {"setSpacings_Py", setSpacings_C, METH_VARARGS, " "},
     {"setFlattenFlag_Py", setFlattenFlag_C, METH_VARARGS, " "},
     {"setFilterWeight_Py", setFilterWeight_C, METH_VARARGS, " "},
     {"crossmul_Py", crossmul_C, METH_VARARGS, " "},
     {NULL, NULL, 0, NULL}
};
#endif

// end of file
