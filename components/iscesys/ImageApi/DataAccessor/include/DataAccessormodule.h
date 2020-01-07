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




#ifndef DataAccessormodule_h
#define DataAccessormodule_h
#ifndef MESSAGE
#define MESSAGE cout << "file " << __FILE__ << " line " << __LINE__ << endl;
#endif
#ifndef ERR_MESSAGE
#define ERR_MESSAGE cout << "Error in file " << __FILE__ << " at line " << __LINE__  << " Exiting" <<  endl; exit(1);
#endif
#include <Python.h>

extern "C"
{
  PyObject *
  createPolyAccessor_C(PyObject *, PyObject *);
  PyObject *
  createAccessor_C(PyObject *, PyObject *);
  PyObject *
  finalizeAccessor_C(PyObject *, PyObject *);
  PyObject *
  getFileLength_C(PyObject *, PyObject *);
  PyObject *
  createFile_C(PyObject *, PyObject *);
  PyObject *
  getTypeSize_C(PyObject *, PyObject *);
  PyObject *
  rewind_C(PyObject* self, PyObject* args);
  string getString(PyObject * key);

}

static PyMethodDef DataAccessor_methods[] =
{
{ "createPolyAccessor", createPolyAccessor_C, METH_VARARGS, " " },
{ "createAccessor", createAccessor_C, METH_VARARGS, " " },
{ "finalizeAccessor", finalizeAccessor_C, METH_VARARGS, " " },
{ "getFileLength", getFileLength_C, METH_VARARGS, " " },
{ "createFile", createFile_C, METH_VARARGS, " " },
{ "rewind", rewind_C, METH_VARARGS, " " },
{ "getTypeSize", getTypeSize_C, METH_VARARGS, " " },
{ NULL, NULL, 0, NULL } };
#endif //DataAccessormodule_h
