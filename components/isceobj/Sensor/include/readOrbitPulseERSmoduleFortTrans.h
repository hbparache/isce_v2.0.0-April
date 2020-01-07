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





#ifndef readOrbitPulseERSmoduleFortTrans_h
#define readOrbitPulseERSmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define getStartingTime_f getstartingtime_
                        #define readOrbitPulseERS_f readorbitpulseers_
                        #define setDeltaClock_f setdeltaclock_
                        #define setICUoffset_f seticuoffset_
                        #define setNumberLines_f setnumberlines_
                        #define setPRF_f setprf_
                        #define setSatelliteUTC_f setsatelliteutc_
                        #define setWidth_f setwidth_
                        #define setEncodedBinaryTimeCode_f setencodedbinarytimecode_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //readOrbitPulseERSmoduleFortTrans_h
