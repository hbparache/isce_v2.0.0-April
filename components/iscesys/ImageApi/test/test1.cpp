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
#include "test1.h"
#include <cmath>
#include <sstream>
#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
using namespace std;
extern "C" void inittest1()
{
 	Py_InitModule3("test1", test1_methods, moduleDoc);
}
PyObject * test1_C(PyObject* self, PyObject* args) 
{
	uint64_t var0;
	uint64_t var1;
    int var2;
    int var3;
    int var4;
	if(!PyArg_ParseTuple(args, "KKiii",&var0,&var1,&var2,&var3,&var4)) 
	{
		return NULL;  
	}  
	test1_f(&var0,&var1,&var2,&var3,&var4);
	return Py_BuildValue("i", 0);
}

