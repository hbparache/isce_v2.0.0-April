!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
! copyright: 2013 to the present, california institute of technology.
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





        module fdmocompState
        ! Inputs
            double precision r001 !< Starting Range [m]
            double precision prf !< Pulse repetition frequency [Hz]
            double precision wavl !< Radar wavelength [m]
            integer nlinesaz !< Number of range bins
            integer nlines !< Number of values in the vsch array
            integer ht1 !< Satellite height [m]
            double precision fs !< Range sampling rate [Hz]
            double precision rcurv !< Radius of curvature [m]
            double precision, allocatable, dimension(:) ::  fdArray !< Cubic polynomial coefficients for the Doppler polynomial as a function of range [%PRF]
            integer dim1_fdArray
            double precision, allocatable, dimension(:,:) ::  vsch!< Velocity components in SCH coordinates
            integer dim1_vsch, dim2_vsch
        ! Output 
            double precision fdnew !< Motion compensated Doppler centroid [%PRF]
            integer ilrl
        end module 
