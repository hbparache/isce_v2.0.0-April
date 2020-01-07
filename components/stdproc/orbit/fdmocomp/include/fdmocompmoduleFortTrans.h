//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2013 to the present, california institute of technology.
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





#ifndef fdmocompmoduleFortTrans_h
#define fdmocompmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define allocate_fdArray_f allocate_fdarray_
                        #define allocate_vsch_f allocate_vsch_
                        #define deallocate_fdArray_f deallocate_fdarray_
                        #define deallocate_vsch_f deallocate_vsch_
                        #define fdmocomp_f fdmocomp_
                        #define getCorrectedDoppler_f getcorrecteddoppler_
                        #define setDopplerCoefficients_f setdopplercoefficients_
                        #define setHeigth_f setheigth_
                        #define setPRF_f setprf_
                        #define setPlatformHeigth_f setplatformheigth_
                        #define setRadarWavelength_f setradarwavelength_
                        #define setRadiusOfCurvature_f setradiusofcurvature_
                        #define setRangeSamplingRate_f setrangesamplingrate_
                        #define setSchVelocity_f setschvelocity_
                        #define setStartingRange_f setstartingrange_
                        #define setWidth_f setwidth_
                        #define setLookSide_f setlookside_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //fdmocompmoduleFortTrans_h
