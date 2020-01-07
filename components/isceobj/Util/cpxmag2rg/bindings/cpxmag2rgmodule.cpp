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
#include "cpxmag2rgmodule.h"
#include <cmath>
#include <sstream>
#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
using namespace std;
extern "C" void initcpxmag2rg()
{
 	Py_InitModule3("cpxmag2rg", cpxmag2rg_methods, moduleDoc);
}
PyObject * setStdWriter_C(PyObject* self, PyObject* args)
{
    uint64_t var;
    if(!PyArg_ParseTuple(args, "K", &var))
    {
        return NULL;
    }
    setStdWriter_f(&var);
    return Py_BuildValue("i", 0);
}
PyObject * cpxmag2rg_C(PyObject* self, PyObject* args) 
{
	uint64_t var0;
	uint64_t var1;
	uint64_t var2;
	if(!PyArg_ParseTuple(args, "KKK",&var0,&var1,&var2)) 
	{
		return NULL;  
	}  
	cpxmag2rg_f(&var0,&var1,&var2);
	return Py_BuildValue("i", 0);
}
PyObject * setLineLength_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setLineLength_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setFileLength_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setFileLength_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setAcOffset_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setAcOffset_f(&var);
	return Py_BuildValue("i", 0);
}
PyObject * setDnOffset_C(PyObject* self, PyObject* args) 
{
	int var;
	if(!PyArg_ParseTuple(args, "i", &var)) 
	{
		return NULL;  
	}  
	setDnOffset_f(&var);
	return Py_BuildValue("i", 0);
}
