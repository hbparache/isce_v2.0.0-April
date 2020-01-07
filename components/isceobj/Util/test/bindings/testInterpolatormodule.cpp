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




#include <Python.h>
#include "testInterpolatormodule.h"
using namespace std;

static const char * const __doc__ = "Python extension for image API data accessors";

PyModuleDef moduledef =
{
// header
    PyModuleDef_HEAD_INIT,
    // name of the module
    "testInterpolator",
    // module documentation string
    __doc__,
    // size of the per-interpreter state of the module;
    // -1 if this state is global
    -1, testInterpolator_methods, };

// initialization function for the module
// *must* be called PyInit_formslc
PyMODINIT_FUNC
PyInit_testInterpolator()
{
  // create the module using moduledef struct defined above
  PyObject * module = PyModule_Create(&moduledef);
  // check whether module creation succeeded and raise an exception if not
  if (!module)
  {
    return module;
  }
  // otherwise, we have an initialized module
  // and return the newly created module
  return module;
}

PyObject *
testInterpolator_C(PyObject* self, PyObject* args)
{
  uint64_t ptPoly2 = 0;
  uint64_t ptPoly1 = 0;

  if (!PyArg_ParseTuple(args, "KK", &ptPoly1, &ptPoly2))
  {
    return NULL;
  }

 testinterpolator_(&ptPoly1, &ptPoly2);

  return Py_BuildValue("i", 0);
}
