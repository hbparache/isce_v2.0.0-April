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





#ifndef topozeromoduleFortTrans_h
#define topozeromoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define getMaximumLatitude_f getmaximumlatitude_
                        #define getMaximumLongitude_f getmaximumlongitude_
                        #define getMinimumLatitude_f getminimumlatitude_
                        #define getMinimumLongitude_f getminimumlongitude_
                        #define setDeltaLatitude_f setdeltalatitude_
                        #define setDeltaLongitude_f setdeltalongitude_
                        #define setDemLength_f setdemlength_
                        #define setDemWidth_f setdemwidth_
                        #define setEllipsoidEccentricitySquared_f setellipsoideccentricitysquared_
                        #define setEllipsoidMajorSemiAxis_f setellipsoidmajorsemiaxis_
                        #define setFirstLatitude_f setfirstlatitude_
                        #define setFirstLongitude_f setfirstlongitude_
                        #define setHeightPointer_f setheightpointer_
                        #define setLatitudePointer_f setlatitudepointer_
                        #define setLength_f setlength_
                        #define setLongitudePointer_f setlongitudepointer_
                        #define setLosPointer_f setlospointer_
                        #define setIncPointer_f setincpointer_
                        #define setMaskPointer_f setmaskpointer_
                        #define setNumberAzimuthLooks_f setnumberazimuthlooks_
                        #define setNumberIterations_f setnumberiterations_
                        #define setNumberRangeLooks_f setnumberrangelooks_
                        #define setPRF_f setprf_
                        #define setSensingStart_f setsensingstart_
                        #define setPegHeading_f setpegheading_
                        #define setRadarWavelength_f setradarwavelength_
                        #define setRangeFirstSample_f setrangefirstsample_
                        #define setRangePixelSpacing_f setrangepixelspacing_
                        #define setOrbit_f setorbit_
                        #define setWidth_f setwidth_
                        #define setLookSide_f setlookside_
                        #define topo_f topo_
                        #define setSecondaryIterations_f setsecondaryiterations_
                        #define setThreshold_f setthreshold_
                        #define setMethod_f setmethod_
                        #define setOrbitMethod_f setorbitmethod_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //topozeromoduleFortTrans_h
