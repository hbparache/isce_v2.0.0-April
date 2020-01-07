//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2012 to the present, california institute of technology.
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
#include "readOrbitPulseERSmodule.h"
#include <cmath>
#include <sstream>
#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
using namespace std;
extern "C" void initreadOrbitPulseERS()
{
 	Py_InitModule3("readOrbitPulseERS", readOrbitPulseERS_methods, moduleDoc);
}
PyObject * readOrbitPulseERS_C(PyObject* self, PyObject* args) 
{
	readOrbitPulseERS_f();
	return Py_BuildValue("i", 0);
}
PyObject * setEncodedBinaryTimeCode_C(PyObject* self, PyObject* args) 
{
	uint64_t var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setEncodedBinaryTimeCode_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setWidth_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setWidth_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setICUoffset_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setICUoffset_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setNumberLines_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setNumberLines_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setSatelliteUTC_C(PyObject* self, PyObject* args) 
{
	double var;
	if(!PyArg_ParseTuple(args, "d", &var)) 
	{
		return NULL;  
	}  
	setSatelliteUTC_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setPRF_C(PyObject* self, PyObject* args) 
{
	double var;
	if(!PyArg_ParseTuple(args, "d", &var)) 
	{
		return NULL;  
	}  
	setPRF_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setDeltaClock_C(PyObject* self, PyObject* args) 
{
	double var;
	if(!PyArg_ParseTuple(args, "d", &var)) 
	{
		return NULL;  
	}  
	setDeltaClock_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * getStartingTime_C(PyObject* self, PyObject* args) 
{
	double var;
	getStartingTime_f(&var);
	return Py_BuildValue("d",var);
}
