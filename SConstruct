#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2010 to the present, california institute of technology.
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



import os
import sys

if ((sys.version_info[0] > 2)):
    print ("Sorry. Compiling requires a python version < 3")
    raise Exception

if 'SCONS_CONFIG_DIR' in os.environ:
    sconsConfigDir = os.environ['SCONS_CONFIG_DIR']
else:
    print("Error. Need to set the variable SCONS_CONFIG_DIR in the shell environment")
    raise Exception

from configuration import sconsConfigFile
#allow scons to take the input argument --setupfile=someOtherFile to allow change of the default SConfigISCE
AddOption('--setupfile',dest='setupfile',type='string',default='SConfigISCE')
AddOption('--isrerun',dest='isrerun',type='string',default='no')

env = Environment(ENV = os.environ)
sconsSetupFile = GetOption('setupfile')
isrerun = GetOption('isrerun')

sconsConfigFile.setupScons(env,sconsSetupFile)
#add some information that are necessary to build the framework such as specific includes, libpath and so on
buildDir = env['PRJ_SCONS_BUILD']
libPath = os.path.join(buildDir,'libs')
#this is the directory where all the built library are put so they can easily be found during linking
env['PRJ_LIB_DIR'] = libPath

# add the libPath to the LIBPATH environment that is where all the libs are serched
env.AppendUnique(LIBPATH = [libPath])

# add the modPath to the FORTRANMODDIR environment that is where all the fortran mods are searched

#not working yet
modPath = os.path.join(buildDir,'mods')
env['FORTRANMODDIR'] =  modPath
env.AppendUnique(FORTRANPATH = [modPath])
env.AppendUnique(F90PATH = [modPath])
env.AppendUnique(F77PATH = [modPath])
#add the includes needed by the framework
imageApiInc = os.path.join(buildDir,'components/iscesys/ImageApi/include')
dataCasterInc = os.path.join(buildDir,'components/iscesys/ImageApi/DataCaster/include')
lineAccessorInc = os.path.join(buildDir,'components/isceobj/LineAccessor/include')
stdOEInc =  os.path.join(buildDir,'components/iscesys/StdOE/include')
utilInc =  os.path.join(buildDir,'components/isceobj/Util/include')
utilLibInc =  os.path.join(buildDir,'components/isceobj/Util/Library/include')

env.AppendUnique(CPPPATH = [imageApiInc,dataCasterInc,lineAccessorInc,stdOEInc,utilInc,utilLibInc])
env['HELPER_DIR'] = os.path.join(env['PRJ_SCONS_INSTALL'],'helper')
env['HELPER_BUILD_DIR'] = os.path.join(env['PRJ_SCONS_BUILD'],'helper')

#put the pointer function createHelp in the environment so it can be access anywhere
from configuration.buildHelper import createHelp
env['HELP_BUILDER'] = createHelp
#Create an env variable to hold all the modules added to the sys.path by default.
#They are the same as the one in in __init__.py in the same directory of this file
moduleList = []
installDir = env['PRJ_SCONS_INSTALL']
moduleList.append(os.path.join(installDir,'applications'))
moduleList.append(os.path.join(installDir,'components'))
env['ISCEPATH'] = moduleList
env.PrependUnique(LIBS=['gdal'])
Export('env')


inst = env['PRJ_SCONS_INSTALL']

####new part
#####PSA. Check for header files and libraries up front
confinst = Configure(env)
hdrparams = [('python3 header', 'Python.h', 'Install python3-dev or add path to Python.h to CPPPATH'),
          ('fftw3', 'fftw3.h', 'Install fftw3 or libfftw3-dev or add path to fftw3.h to CPPPATH and FORTRANPATH'),
          ('gdal header', 'gdal_priv.h', 'Install gdal or add path to gdal includes to CPPPATH'),
          ('hdf5', 'hdf5.h', 'Install HDF5 of libhdf5-dev or add path to hdf5.h to CPPPATH'),
          ('X11', 'X11/Xlib.h', 'Install X11 or libx11-dev or add path to X11 directory to X11INCPATH'),
          ('Xm', 'Xm/Xm.h', 'Install libXm or libXm-dev or add path to Xm directory to MOTIFINCPATH'),
          ('openmp', 'omp.h', 'Compiler not built with OpenMP. Use a different compiler or add path to omp.h to CPPPATH'),]

allflag  = False
for (name,hname,msg) in hdrparams:
    if not (confinst.CheckCHeader(hname) or confinst.CheckCXXHeader(hname)):
        print('Could not find: {0} header for {1}'.format(hname, name))
        print('Error: {0}'.format(msg))
        allflag = True
#        raw_input("Press Enter to continue ...")

libparams=  [('libhdf5', 'hdf5', 'Install hdf5 or libhdf5-dev'),
             ('libgdal', 'gdal', 'Install gdal'),
          ('libfftw3f', 'fftw3f', 'Install fftw3 or libfftw3-dev'),
          ('libXm', 'Xm', 'Install Xm or libXm-dev'),
          ('libXt', 'Xt', 'Install Xt or libXt-dev')]

for (name,hname,msg) in libparams:
    if not confinst.CheckLib(hname):
        print('Could not find: {0} header for {1}'.format(hname, name))
        print('Error: {0}'.format(msg))
        allflag = True
#        raw_input("Press Enter to continue ...")

fortparams = [('fftw3', 'fftw3.f', 'Install fftw3 or libfftw3-dev or add path to FORTRANPATH'),]
for (name,hname,msg) in fortparams:
    if env.FindFile('fftw3.f', env['FORTRANPATH']) is None:
        print('Checking for F include {0}... no'.format(name))
        print('Could not find: {0} header for {1}'.format(hname, name))
        print('Error: {0}'.format(msg))
        allflag = True
        raw_input("Press Enter to continue ...")
    else:
        print('Checking for F include {0}... yes'.format(name))

if allflag:
    print('Not all components of ISCE will be installed and can result in errors.')
    raw_input('Press Enter to continue.... Ctrl-C to exit')
else:
    print('Scons appears to find everything needed for installation')

env = confinst.Finish()
###End of new part

file = '__init__.py'
if not os.path.exists(file):
    fout = open(file,"w")
    fout.write("#!/usr/bin/env python3")
    fout.close()

env.Install(inst,file)
try:
    from subprocess import check_output
    svn_revision = check_output('svnversion').strip() or 'Unknown'
except ImportError:
    try:
        import popen2
        stdout, stdin, stderr = popen2.popen3('svnversion')
        svn_revision = stdout.read().strip()
        if stderr.read():
            raise Exception
    except Exception:
        svn_revision = 'Unknown'
except OSError:
    svn_revision = 'Unknown'

if not os.path.exists(inst):
    os.makedirs(inst)

fvers = open(os.path.join(inst,'version.py'),'w')

from release_history import release_version, release_svn_revision, release_date
fvers_lines = ["release_version = '"+release_version+"'\n",
               "release_svn_revision = '"+release_svn_revision+"'\n",
               "release_date = '"+release_date+"'\n",
               "svn_revision = '"+svn_revision+"'\n\n"]

fvers.write(''.join(fvers_lines))
fvers.close()
v = 0
if isrerun == 'no':
    v = os.system('scons -Q install --isrerun=yes')
if v == 0:
    env.Alias('install',inst)
    applications = os.path.join('applications','SConscript')
    SConscript(applications)
    components = os.path.join('components','SConscript')
    SConscript(components)
    defaults = os.path.join('defaults','SConscript')
    SConscript(defaults)
    library = os.path.join('library','SConscript')
    SConscript(library)
    contrib = os.path.join('contrib','SConscript')
    SConscript(contrib)

    if 'test' in sys.argv:
        #Run the unit tests
        env['Test'] = True
    else:
        #Don't run tests.
        #This option only installs test support package for future test runs.
        env['Test'] = False

    tests = os.path.join('test', 'SConscript')
    SConscript(tests)
