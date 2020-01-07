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





#ifndef test1_h
#define test1_h

#include <Python.h>
#include <stdint.h>
#include "test1FortTrans.h"

extern "C"
{
        void test1_f(uint64_t *,uint64_t *, int *, int *, int *);
        PyObject * test1_C(PyObject *, PyObject *);

}

static char * moduleDoc = "module for test1.F";

static PyMethodDef test1_methods[] =
{
        {"test1_Py", test1_C, METH_VARARGS, " "},
        {NULL, NULL, 0, NULL}
};
#endif //test1_h
