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





#ifndef geo2rdrmoduleFortTrans_h
#define geo2rdrmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define geo2rdr_f geo2rdr_
                        #define setDemLength_f setdemlength_
                        #define setDemWidth_f setdemwidth_
                        #define setLookSide_f setlookside_
                        #define setDopplerAccessor_f setdoppleraccessor_
                        #define setEllipsoidEccentricitySquared_f setellipsoideccentricitysquared_
                        #define setEllipsoidMajorSemiAxis_f setellipsoidmajorsemiaxis_
                        #define setLength_f setlength_
                        #define setNumberAzimuthLooks_f setnumberazimuthlooks_
                        #define setNumberRangeLooks_f setnumberrangelooks_
                        #define setPRF_f setprf_
                        #define setRadarWavelength_f setradarwavelength_
                        #define setRangeFirstSample_f setrangefirstsample_
                        #define setRangePixelSpacing_f setrangepixelspacing_
                        #define setOrbit_f setorbit_
                        #define setSensingStart_f setsensingstart_
                        #define setWidth_f setwidth_
                        #define setBistaticFlag_f setbistaticflag_
                        #define setOrbitMethod_f setorbitmethod_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //geo2rdrmoduleFortTrans_h
