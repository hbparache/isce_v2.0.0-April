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





#ifndef resamp_slcmoduleFortTrans_h
#define resamp_slcmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define resamp_slc_f resamp_slc_
                        #define setInputLines_f setinputlines_
                        #define setOutputLines_f setoutputlines_
                        #define setInputWidth_f setinputwidth_
                        #define setOutputWidth_f setoutputwidth_
                        #define setRadarWavelength_f setradarwavelength_
                        #define setReferenceWavelength_f setreferencewavelength_
                        #define setSlantRangePixelSpacing_f setslantrangepixelspacing_
                        #define setReferenceSlantRangePixelSpacing_f setreferenceslantrangepixelspacing_
                        #define setAzimuthCarrier_f setazimuthcarrier_
                        #define setRangeCarrier_f setrangecarrier_
                        #define setAzimuthOffsetsPoly_f setazimuthoffsetspoly_
                        #define setRangeOffsetsPoly_f setrangeoffsetspoly_
                        #define setDopplerPoly_f setdopplerpoly_
                        #define setIsComplex_f setiscomplex_
                        #define setMethod_f setmethod_
                        #define setFlatten_f setflatten_
                        #define setStartingRange_f setstartingrange_
                        #define setReferenceStartingRange_f setreferencestartingrange_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //resamp_slcmoduleFortTrans_h
