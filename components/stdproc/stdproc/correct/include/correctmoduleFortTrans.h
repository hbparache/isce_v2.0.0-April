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





#ifndef correctmoduleFortTrans_h
#define correctmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define allocate_midpoint_f allocate_midpoint_
                        #define allocate_mocbaseArray_f allocate_mocbasearray_
                        #define allocate_s1sch_f allocate_s1sch_
                        #define allocate_s2sch_f allocate_s2sch_
                        #define allocate_s_mocompArray_f allocate_s_mocomparray_
                        #define allocate_smsch_f allocate_smsch_
                        #define correct_f correct_
                        #define deallocate_midpoint_f deallocate_midpoint_
                        #define deallocate_mocbaseArray_f deallocate_mocbasearray_
                        #define deallocate_s1sch_f deallocate_s1sch_
                        #define deallocate_s2sch_f deallocate_s2sch_
                        #define deallocate_s_mocompArray_f deallocate_s_mocomparray_
                        #define deallocate_smsch_f deallocate_smsch_
                        #define setBodyFixedVelocity_f setbodyfixedvelocity_
                        #define setEllipsoidEccentricitySquared_f setellipsoideccentricitysquared_
                        #define setEllipsoidMajorSemiAxis_f setellipsoidmajorsemiaxis_
                        #define setISMocomp_f setismocomp_
                        #define setLength_f setlength_
                        #define setMidpoint_f setmidpoint_
                        #define setMocompBaseline_f setmocompbaseline_
                        #define setNumberAzimuthLooks_f setnumberazimuthlooks_
                        #define setNumberRangeLooks_f setnumberrangelooks_
                        #define setPRF_f setprf_
                        #define setPegHeading_f setpegheading_
                        #define setPegLatitude_f setpeglatitude_
                        #define setPegLongitude_f setpeglongitude_
                        #define setPlanetLocalRadius_f setplanetlocalradius_
                        #define setRadarWavelength_f setradarwavelength_
                        #define setRangeFirstSample_f setrangefirstsample_
                        #define setRangePixelSpacing_f setrangepixelspacing_
                        #define setReferenceOrbit_f setreferenceorbit_
                        #define setSc_f setsc_
                        #define setSch1_f setsch1_
                        #define setSch2_f setsch2_
                        #define setSpacecraftHeight_f setspacecraftheight_
                        #define setWidth_f setwidth_
                        #define setLookSide_f setlookside_
                        #define setDopCoeff_f setdopcoeff_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //correctmoduleFortTrans_h
