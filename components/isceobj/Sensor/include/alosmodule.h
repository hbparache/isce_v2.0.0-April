//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2009 to the present, california institute of technology.
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




#ifndef alosmodule_h
#define alosmodue_h

#include <Python.h>
#include <stdint.h>
#include "image_sio.h"
#include "alosglobals.h"

extern "C"
{
    PyObject *alos_C(PyObject *self,PyObject *args);
    PyObject *alose_C(PyObject *self,PyObject *args);
    PyObject *createDictionaryOutput(struct PRM *prm,PyObject *dict);
    int ALOS_pre_process(struct PRM inputPRM, struct PRM *outputPRM,
        struct GLOBALS globals);
}

static PyMethodDef alos_methods[]  =
{
    {"alos_Py",alos_C,METH_VARARGS," "},
    {"alose_Py",alose_C,METH_VARARGS," "},
    {NULL,NULL,0,NULL}
};

#endif
// end of file

