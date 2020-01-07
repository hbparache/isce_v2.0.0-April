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




#ifndef ALOS_fbs2fbdmodule_h
#define ALOS_fbs2fbdmodule_h

#include <Python.h>

    PyObject * ALOS_fbs2fbd_C(PyObject *, PyObject *);
    PyObject * setNumberGoodBytes_C(PyObject *, PyObject *);
    PyObject * setNumberBytesPerLine_C(PyObject *, PyObject *);
    PyObject * setNumberLines_C(PyObject *, PyObject *);
    PyObject * setFirstSample_C(PyObject *, PyObject *);
    PyObject * setInPhaseValue_C(PyObject *, PyObject *);
    PyObject * setQuadratureValue_C(PyObject *, PyObject *);
    PyObject * setInputFilename_C(PyObject* self, PyObject* args);
    PyObject * setOutputFilename_C(PyObject* self, PyObject* args);


static PyMethodDef ALOS_fbs2fbd_methods[] =
{
    {"ALOS_fbs2fbd_Py", ALOS_fbs2fbd_C, METH_VARARGS, " "},
    {"setNumberGoodBytes_Py", setNumberGoodBytes_C, METH_VARARGS, " "},
    {"setNumberBytesPerLine_Py", setNumberBytesPerLine_C, METH_VARARGS,
        " "},
    {"setNumberLines_Py", setNumberLines_C, METH_VARARGS, " "},
    {"setFirstSample_Py", setFirstSample_C, METH_VARARGS, " "},
    {"setInPhaseValue_Py", setInPhaseValue_C, METH_VARARGS, " "},
    {"setQuadratureValue_Py", setQuadratureValue_C, METH_VARARGS, " "},
    {"setInputFilename_Py",setInputFilename_C, METH_VARARGS, " "},
    {"setOutputFilename_Py",setOutputFilename_C, METH_VARARGS, " "},
    {NULL, NULL, 0, NULL}
};
#endif
// end of file
