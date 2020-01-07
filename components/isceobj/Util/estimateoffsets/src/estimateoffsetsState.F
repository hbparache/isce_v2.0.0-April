!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
! copyright: 2012 to the present, california institute of technology.
! all rights reserved. united states government sponsorship acknowledged.
! any commercial use must be negotiated with the office of technology transfer
! at the california institute of technology.
! 
! this software may be subject to u.s. export control laws. by accepting this
! software, the user agrees to comply with all applicable u.s. export laws and
! regulations. user has the responsibility to obtain export licenses,  or other
! export authority as may be required before exporting such information to
! foreign countries or providing access to foreign persons.
! 
! installation and use of this software is restricted by a license agreement
! between the licensee and the california institute of technology. it is the
! user's responsibility to abide by the terms of the license agreement.
!
! Author: Giangi Sacco
!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





        module estimateoffsetsState
            !Range location of window
            integer, allocatable, dimension(:) ::  locationAcross 
            integer dim1_locationAcross
            !Range offset
            real*4, allocatable, dimension(:) ::  locationAcrossOffset
            integer dim1_locationAcrossOffset

            !Azimuth location of window
            integer, allocatable, dimension(:) ::  locationDown
            integer dim1_locationDown
            !Azimuth offset
            real*4, allocatable, dimension(:) ::  locationDownOffset
            integer dim1_locationDownOffset
            !SNR of correlation maximum
            real*4, allocatable, dimension(:) ::  snrRet
            integer dim1_snrRet

            !File widths in range pixels
            integer len1, len2

            !If input data is complex
            integer iscpx1, iscpx2

            !Band numbers for input data
            integer band1, band2

            !File lengths in azimuth lines
            integer lines1, lines2
            integer isamp_s
            integer isamp_f
            integer nloc
            integer isamp_sdn
            integer isamp_fdn
            integer nlocdn
            integer ioffac
            integer ioffdn
            real*4 prf1
            real*4 prf2
            character*1 talk

            integer NPTS   !Window size
            integer NOFF   !Search window
            integer NDISP  !Search window around maximum
            integer NOVS   !Oversampling factor 
        end module estimateoffsetsState 
