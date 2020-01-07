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
! Author: Piyush Agram
!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





        module offsetpolyState
            integer i_ma             !c Number of fit Coefficients
            integer numOffsets       !c Number of offsets

            !c Location across array 1
            double precision, allocatable, dimension(:) ::  r_ranposV

            !c Location across offset array 1
            double precision, allocatable, dimension(:) ::  r_offV

            !c Location down array 1
            double precision, allocatable, dimension(:) ::  r_azposV

            !c SNR array 1
            double precision, allocatable, dimension(:) ::  r_sigV

            !Polynomial arrays
            double precision, allocatable, dimension(:) :: r_polyV
        end module offsetpolyState 
