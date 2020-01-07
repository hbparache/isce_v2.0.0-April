//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2011 to the present, california institute of technology.
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




#ifndef dismphfilemodule_h
#define dismphfilemodule_h

#include <Python.h>
#include <stdint.h>
#include "dismphfilemoduleFortTrans.h"

extern "C"
{
    void dismphfile_f(uint64_t *, uint64_t *);
    PyObject * dismphfile_C(PyObject *, PyObject *);
    void setLength_f(int *);
    PyObject * setLength_C(PyObject *, PyObject *);
    void setFirstLine_f(int *);
    PyObject * setFirstLine_C(PyObject *, PyObject *);
    void setNumberLines_f(int *);
    PyObject * setNumberLines_C(PyObject *, PyObject *);
    void setFlipFlag_f(int *);
    PyObject * setFlipFlag_C(PyObject *, PyObject *);
    void setScale_f(float *);
    PyObject * setScale_C(PyObject *, PyObject *);
    void setExponent_f(float *);
    PyObject * setExponent_C(PyObject *, PyObject *);

}

static PyMethodDef dismphfile_methods[] =
{
    {"dismphfile_Py", dismphfile_C, METH_VARARGS, " "},
    {"setLength_Py", setLength_C, METH_VARARGS, " "},
    {"setFirstLine_Py", setFirstLine_C, METH_VARARGS, " "},
    {"setNumberLines_Py", setNumberLines_C, METH_VARARGS, " "},
    {"setFlipFlag_Py", setFlipFlag_C, METH_VARARGS, " "},
    {"setScale_Py", setScale_C, METH_VARARGS, " "},
    {"setExponent_Py", setExponent_C, METH_VARARGS, " "},
    {NULL, NULL, 0, NULL}
};
#endif //dismphfilemodule_h
