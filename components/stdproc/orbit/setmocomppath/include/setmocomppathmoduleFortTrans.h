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





#ifndef setmocomppathmoduleFortTrans_h
#define setmocomppathmoduleFortTrans_h

        #if defined(NEEDS_F77_TRANSLATION)

                #if defined(F77EXTERNS_LOWERCASE_TRAILINGBAR)
                        #define allocate_vxyz1_f allocate_vxyz1_
                        #define allocate_vxyz2_f allocate_vxyz2_
                        #define allocate_xyz1_f allocate_xyz1_
                        #define allocate_xyz2_f allocate_xyz2_
                        #define deallocate_vxyz1_f deallocate_vxyz1_
                        #define deallocate_vxyz2_f deallocate_vxyz2_
                        #define deallocate_xyz1_f deallocate_xyz1_
                        #define deallocate_xyz2_f deallocate_xyz2_
                        #define getFirstAverageHeight_f getfirstaverageheight_
                        #define getFirstProcVelocity_f getfirstprocvelocity_
                        #define getPegHeading_f getpegheading_
                        #define getPegLatitude_f getpeglatitude_
                        #define getPegLongitude_f getpeglongitude_
                        #define getPegRadiusOfCurvature_f getpegradiusofcurvature_
                        #define getSecondAverageHeight_f getsecondaverageheight_
                        #define getSecondProcVelocity_f getsecondprocvelocity_
                        #define setEllipsoidEccentricitySquared_f setellipsoideccentricitysquared_
                        #define setEllipsoidMajorSemiAxis_f setellipsoidmajorsemiaxis_
                        #define setFirstPosition_f setfirstposition_
                        #define setFirstVelocity_f setfirstvelocity_
                        #define setStdWriter_f setstdwriter_
                        #define setPlanetGM_f setplanetgm_
                        #define setSecondPosition_f setsecondposition_
                        #define setSecondVelocity_f setsecondvelocity_
                        #define setmocomppath_f setmocomppath_
                #else
                        #error Unknown translation for FORTRAN external symbols
                #endif

        #endif

#endif //setmocomppathmoduleFortTrans_h
