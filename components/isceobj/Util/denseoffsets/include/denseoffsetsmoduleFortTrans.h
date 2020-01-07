//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2014 to the present, california institute of technology.
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
// Author: Piyush Agram
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#ifndef denseoffsetsmoduleFortTrans_h
#define denseoffsetsmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define denseoffsets_f denseoffsets_
                        #define setAcrossGrossOffset_f setacrossgrossoffset_
                        #define setDebugFlag_f setdebugflag_
                        #define setDownGrossOffset_f setdowngrossoffset_
                        #define setFileLength1_f setfilelength1_
                        #define setFileLength2_f setfilelength2_
                        #define setScaleFactorX_f setscalefactorx_
                        #define setFirstSampleAcross_f setfirstsampleacross_
                        #define setFirstSampleDown_f setfirstsampledown_
                        #define setLastSampleAcross_f setlastsampleacross_
                        #define setLastSampleDown_f setlastsampledown_
                        #define setLineLength1_f setlinelength1_
                        #define setLineLength2_f setlinelength2_
                        #define setSkipSampleAcross_f setskipsampleacross_
                        #define setSkipSampleDown_f setskipsampledown_
                        #define setScaleFactorY_f setscalefactory_
                        #define setWindowSizeWidth_f setwindowsizewidth_
                        #define setWindowSizeHeight_f setwindowsizeheight_
                        #define setSearchWindowSizeWidth_f setsearchwindowsizewidth_
                        #define setSearchWindowSizeHeight_f setsearchwindowsizeheight_
                        #define setZoomWindowSize_f setzoomwindowsize_
                        #define setOversamplingFactor_f setoversamplingfactor_
                        #define setIsComplex1_f setiscomplex1_
                        #define setIsComplex2_f setiscomplex2_
                        #define setBand1_f setband1_
                        #define setBand2_f setband2_
                        #define setNormalizeFlag_f setnormalizeflag_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //denseoffsetsmoduleFortTrans_h
