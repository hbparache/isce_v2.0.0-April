//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2013 to the present, california institute of technology.
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
// Author: Piyush Agram
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#ifndef upsampledemmodule_h
#define upsampledemmodule_h

#include <Python.h>
#include <stdint.h>
#include "upsampledemmoduleFortTrans.h"

extern "C"
{
    void upsampledem_f(uint64_t *,uint64_t *, int *);
    PyObject * upsampledem_C(PyObject *, PyObject *);
    void setWidth_f(int *);
    PyObject * setWidth_C(PyObject *, PyObject *);
    void setXFactor_f(int *);
    PyObject * setXFactor_C(PyObject *, PyObject *);
    void setYFactor_f(int *);
    PyObject * setYFactor_C(PyObject *, PyObject *);
    void setNumberLines_f(int *);
    PyObject * setNumberLines_C(PyObject *, PyObject *);
    void setStdWriter_f(uint64_t *);
    PyObject * setStdWriter_C(PyObject *, PyObject *);
    void setPatchSize_f(int *);
    PyObject * setPatchSize_C(PyObject *, PyObject *);
}

static PyMethodDef upsampledem_methods[] =
{
    {"upsampledem_Py",upsampledem_C, METH_VARARGS, " "},
    {"setWidth_Py", setWidth_C, METH_VARARGS, " "},
    {"setXFactor_Py", setXFactor_C, METH_VARARGS, " "},
    {"setYFactor_Py", setYFactor_C, METH_VARARGS, " "},
    {"setNumberLines_Py", setNumberLines_C, METH_VARARGS, " "},
    {"setStdWriter_Py", setStdWriter_C, METH_VARARGS, " "},
    {"setPatchSize_Py", setPatchSize_C, METH_VARARGS, " "},
    {NULL, NULL, 0, NULL}
};
#endif
// end of file

