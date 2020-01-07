#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2011 to the present, california institute of technology.
# all rights reserved. united states government sponsorship acknowledged.
# any commercial use must be negotiated with the office of technology transfer
# at the california institute of technology.
# 
# this software may be subject to u.s. export control laws. by accepting this
# software, the user agrees to comply with all applicable u.s. export laws and
# regulations. user has the responsibility to obtain export licenses,  or other
# export authority as may be required before exporting such information to
# foreign countries or providing access to foreign persons.
# 
# installation and use of this software is restricted by a license agreement
# between the licensee and the california institute of technology. it is the
# user's responsibility to abide by the terms of the license agreement.
#
# Author: Eric Gurrola
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




def createCatalog(name):
    from .Catalog import Catalog
    return Catalog(name)

def createOrderedDict():
    from OrderedDict import OrderedDict
    return OrderedDict

def recordInputs(mainCatalog, obj, node, logger, title):
    """This is merely a convenience method to create a new catalog, add all the
    inputs from the given object, print the catalog, and then import the
    catalog in the main catalog. It returns the created catalog."""
    catalog = createCatalog(mainCatalog.name)
    catalog.addInputsFrom(obj, node + ".inputs")
    catalog.printToLog(logger, title + " - Inputs")
    mainCatalog.addAllFromCatalog(catalog)
    return catalog

def recordOutputs(mainCatalog, obj, node, logger, title):
    """This is merely a convenience method to create a new catalog, add all the
    outputs from the given object, print the catalog, and then import the
    catalog in the main catalog. It returns the created catalog."""
    catalog = createCatalog(mainCatalog.name)
    catalog.addOutputsFrom(obj, node + ".outputs")
    catalog.printToLog(logger, title + " - Outputs")
    mainCatalog.addAllFromCatalog(catalog)
    return catalog

def recordInputsAndOutputs(mainCatalog, obj, node, logger, title):
    """This is a short-hand for using both recordInputs and recordOutputs"""
    recordInputs(mainCatalog, obj, node, logger, title)
    recordOutputs(mainCatalog, obj, node, logger, title)

def testInputsChanged(startCatalog, node, obj):
    endCatalog = createCatalog(startCatalog.name)
    endCatalog.addInputsFrom(obj, node + ".inputs")
    if not (startCatalog == endCatalog):
        import sys
        print("The inputs changed.")
        sys.exit(1)

