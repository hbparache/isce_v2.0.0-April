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





#ifndef offsetpolymoduleFortTrans_h
#define offsetpolymoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define allocateFieldArrays_f allocatefieldarrays_
                        #define deallocateFieldArrays_f deallocatefieldarrays_
                        #define allocatePolyArray_f allocatepolyarray_
                        #define deallocatePolyArray_f deallocatepolyarray_
                        #define getOffsetPoly_f getoffsetpoly_
                        #define offsetpoly_f offsetpoly_
                        #define setLocationAcross_f setlocationacross_
                        #define setOffset_f setoffset_
                        #define setLocationDown_f setlocationdown_
                        #define setSNR_f setsnr_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //offsetpolymoduleFortTrans_h
