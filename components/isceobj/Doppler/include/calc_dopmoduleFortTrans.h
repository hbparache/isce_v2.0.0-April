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





#ifndef calc_dopmoduleFortTrans_h
#define calc_dopmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define allocate_rngDoppler_f allocate_rngdoppler_
                        #define calc_dop_f calc_dop_
                        #define deallocate_rngDoppler_f deallocate_rngdoppler_
                        #define getDoppler_f getdoppler_
                        #define getRngDoppler_f getrngdoppler_
                        #define setFirstLine_f setfirstline_
                        #define setHeader_f setheader_
                        #define setIoffset_f setioffset_
                        #define setLastLine_f setlastline_
                        #define setQoffset_f setqoffset_
                        #define setWidth_f setwidth_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //calc_dopmoduleFortTrans_h
