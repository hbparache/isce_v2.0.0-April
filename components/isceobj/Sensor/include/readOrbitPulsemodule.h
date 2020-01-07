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





#ifndef readOrbitPulsemodule_h
#define readOrbitPulsemodule_h

#include <Python.h>
#include <stdint.h>
#include "readOrbitPulsemoduleFortTrans.h"

extern "C"
{
        void readOrbitPulse_f(uint64_t *,uint64_t *,uint64_t *);
        PyObject * readOrbitPulse_C(PyObject *, PyObject *);
        void setNumberBitesPerLine_f(int *);
        PyObject * setNumberBitesPerLine_C(PyObject *, PyObject *);
        void setNumberLines_f(int *);
        PyObject * setNumberLines_C(PyObject *, PyObject *);

}

static PyMethodDef readOrbitPulse_methods[] =
{
        {"readOrbitPulse_Py", readOrbitPulse_C, METH_VARARGS, " "},
        {"setNumberBitesPerLine_Py", setNumberBitesPerLine_C, METH_VARARGS, " "},
        {"setNumberLines_Py", setNumberLines_C, METH_VARARGS, " "},
        {NULL, NULL, 0, NULL}
};
#endif //readOrbitPulsemodule_h
