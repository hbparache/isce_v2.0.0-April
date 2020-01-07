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
#include "histogrammodule.h"

// A C++ extension is required for this code since
// ctypes does not currently allow interfacing with C++ code
// (name-mangling and all).

static const char * __doc__ = "module for p2.cpp";

PyModuleDef moduledef = {
    // header
    PyModuleDef_HEAD_INIT,
    // name of the module
    "histogram",
    // module documentation string
    __doc__,
    // size of the per-interpreter state of the module;
    // -1 if this state is global
    -1,
    histogram_methods,
};

// initialization function for the module
// *must* be called PyInit_filter
PyMODINIT_FUNC
PyInit_histogram()
{
    // create the module using moduledef struct defined above
    PyObject * module = PyModule_Create(&moduledef);
    // check whether module creation succeeded and raise an exception if not
    if (!module) {
        return module;
    }
    // otherwise, we have an initialized module
    // and return the newly created module
    return module;
}

PyObject *realHistogram_C(PyObject *self, PyObject *args)
{
    uint64_t imagePointer;
    int width, height, bands;
    int nBins,i,j,k,ind;
    double nullValue, key;
    DataAccessor* img;
    double *line;
    double *qt;
    double *val;

    //Histogram objects
    p2_t *hists;


    //Parse command line
    if(!PyArg_ParseTuple(args, "Kid", &imagePointer, &nBins,&nullValue))
    {
      return NULL;
    }

    //Get image dimensions
    img = (DataAccessor*) imagePointer;
    bands = img->getBands();
    width = img->getWidth();
    height = img->getNumberOfLines();

    std::cout << "Dimensions: " << width << " " << height << "\n";
    //Allocate memory for one line of data
    line = new double[width*bands];
    qt = new double[nBins + 1];
    val = new double[nBins + 1];

    //Create histogram objects
    hists = new p2_t[bands];
    for(k=0; k<bands; k++)
        hists[k].add_equal_spacing(nBins);


    //For each line
    for(i=0; i<height; i++)
    {
        img->getLineSequential((char*) line);

        //For each band
        for(k=0; k<bands; k++)
        {
            //For each pixel
            for(j=0; j<width;j++)
            {
                ind = j*bands + k;
                key = line[ind];
                if (key != nullValue)
                    hists[k].add(key);
            }
        }
    }


//    for(k=0;k<bands;k++)
//        hists[k].report();

    //Delete line 
    delete [] line;

    //Convert to Python Lists
    PyObject *list = PyList_New(bands); 

    for (k=0;k<bands;k++)
    {
        hists[k].getStats(qt, val);
        PyObject *qlist = PyList_New(nBins + 1);
        PyObject *vlist = PyList_New(nBins + 1);

        for(i=0; i< (nBins+1); i++)
        {
            PyObject* listEl = PyFloat_FromDouble(qt[i]);
            if(listEl == NULL)
            {
                std::cout << "Error in file " << __FILE__   << " at line " << __LINE__ << ". Cannot set list element" << endl;
                exit(1);
            }            
            PyList_SetItem(qlist,i, listEl);

            listEl = PyFloat_FromDouble(val[i]);
            if(listEl == NULL)
            {
                std::cout << "Error in file " << __FILE__   << " at line " << __LINE__ << ". Cannot set list element" << endl;
                exit(1);
            }
            PyList_SetItem(vlist,i, listEl);
        }

        PyObject *tuple = PyTuple_New(2);
        PyTuple_SetItem(tuple, 0, qlist);
        PyTuple_SetItem(tuple, 1, vlist);

        PyList_SetItem(list, k, tuple);
    }

    //Delete stats arrays
    delete [] qt;
    delete [] val;

    //Delete the histogram object
    delete [] hists;

    return Py_BuildValue("N",list);
}


