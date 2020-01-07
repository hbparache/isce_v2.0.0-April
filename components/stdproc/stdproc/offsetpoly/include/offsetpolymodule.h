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




#ifndef offsetpolymodule_h
#define offsetpolymodule_h

#include <Python.h>
#include <stdint.h>
#include "offsetpolymoduleFortTrans.h"

extern "C"
{
    void offsetpoly_f();
    PyObject * offsetpoly_C(PyObject *, PyObject *);

    void allocateFieldArrays_f(int *);
    PyObject *allocateFieldArrays_C(PyObject *, PyObject *);

    void deallocateFieldArrays_f();
    PyObject *deallocateFieldArrays_C(PyObject *, PyObject *);

    void allocatePolyArray_f(int *);
    PyObject *allocatePolyArray_C(PyObject *, PyObject *);

    void deallocatePolyArray_f();
    PyObject *deallocatePolyArray_C(PyObject *, PyObject *);

    PyObject * setLocationAcross_C(PyObject *, PyObject *);
    void setLocationAcross_f(double *, int *);

    void setOffset_f(double *, int *);
    PyObject * setOffset_C(PyObject *, PyObject*);


    void setLocationDown_f(double *, int *);
    PyObject * setLocationDown_C(PyObject *, PyObject *);


    void setSNR_f(double *, int *);
    PyObject * setSNR_C(PyObject *, PyObject *);

    PyObject* getOffsetPoly_C(PyObject*, PyObject *);
    void getOffsetPoly_f(double *, int *);
}

static PyMethodDef offsetpoly_methods[] =
{
    {"offsetpoly_Py", offsetpoly_C, METH_VARARGS, " "},
    {"setLocationAcross_Py", setLocationAcross_C, METH_VARARGS, " "},
    {"setOffset_Py", setOffset_C, METH_VARARGS, " "},
    {"setLocationDown_Py", setLocationDown_C, METH_VARARGS, " "},
    {"setSNR_Py", setSNR_C, METH_VARARGS, " "},
    {"allocateFieldArrays_Py", allocateFieldArrays_C, METH_VARARGS, " "},
    {"deallocateFieldArrays_Py", deallocateFieldArrays_C, METH_VARARGS, " "},
    {"allocatePolyArray_Py", allocatePolyArray_C, METH_VARARGS, " "},
    {"deallocatePolyArray_Py", deallocatePolyArray_C, METH_VARARGS, " "},
    {"getOffsetPoly_Py", getOffsetPoly_C, METH_VARARGS, " "},
    {NULL, NULL, 0, NULL}
};
#endif
// end of file
