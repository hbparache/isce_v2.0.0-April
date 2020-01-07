#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2009 to the present, california institute of technology.
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
# Author: Giangi Sacco
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



from __future__ import print_function
from isceobj.XmlUtil.XmlUtil import XmlUtil
##
#This class is an initializer and can be used with all the objects that inherit the Component class. It allows to initialize an object from an xml file. 
#The format of the file must be like
#\verbatim
#<component>
#    <name>NameOfTheObject</name>
#    <property>
#        <name>VARAIBLE1</name>
#        <value>value1</value>
#        <doc>"documentation for VARIABLE1"</doc>
#    </property>
#    <property>
#        <name>VARAIBLE2</name>
#        <value>value2</value>
#         <units>m/s</units>
#    </property>
#</component>
#\endverbatim
#Everything that follows the \# will be discarded. If a variable is a list, the elements are separated by white spaces.
# Once an instance of this class is created (say obj), the object that needs to be initialized invokes the initComponent(obj) method (inherited from the Component class)  passing the instance as argument.
#@see Component::initComponent()
class InitFromXmlFile(object):
    
##
# This method must be implemented by each initializer class. It returns a dictionary of dictionaries. The object argument is not used but
# needs to be present in each implementation of the init() method.
#@return retDict dictionary of dictinaries.
    def init(self,object = None):
        objXmlUtil = XmlUtil()
        retDict =  objXmlUtil.createDictionary(objXmlUtil.readFile(self.filename))
        return retDict


##
# Constructor. It takes as argument the filename where the information  to initialize the specific object is stored.
#@param filename xml file from which the object is initlized.
    def __init__(self,filename):
        self.filename = filename
        return
        
