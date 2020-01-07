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





#ifndef cpxmag2rgmodule_h
#define cpxmag2rgmodule_h

#include <Python.h>
#include <stdint.h>
#include "cpxmag2rgmoduleFortTrans.h"

extern "C"
{
    void setStdWriter_f(uint64_t *);
    PyObject * setStdWriter_C(PyObject *, PyObject *);
        void cpxmag2rg_f(uint64_t *,uint64_t *,uint64_t *);
        PyObject * cpxmag2rg_C(PyObject *, PyObject *);
        void setLineLength_f(int *);
        PyObject * setLineLength_C(PyObject *, PyObject *);
        void setFileLength_f(int *);
        PyObject * setFileLength_C(PyObject *, PyObject *);
        void setAcOffset_f(int *);
        PyObject * setAcOffset_C(PyObject *, PyObject *);
        void setDnOffset_f(int *);
        PyObject * setDnOffset_C(PyObject *, PyObject *);

}

static char * moduleDoc = "module for cpxmag2rg.F";

static PyMethodDef cpxmag2rg_methods[] =
{
    {"setStdWriter_Py", setStdWriter_C, METH_VARARGS, " "},
        {"cpxmag2rg_Py", cpxmag2rg_C, METH_VARARGS, " "},
        {"setLineLength_Py", setLineLength_C, METH_VARARGS, " "},
        {"setFileLength_Py", setFileLength_C, METH_VARARGS, " "},
        {"setAcOffset_Py", setAcOffset_C, METH_VARARGS, " "},
        {"setDnOffset_Py", setDnOffset_C, METH_VARARGS, " "},
        {NULL, NULL, 0, NULL}
};
#endif //cpxmag2rgmodule_h
