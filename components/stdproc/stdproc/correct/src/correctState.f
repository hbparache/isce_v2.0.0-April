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





        module correctState
            double precision, allocatable, dimension(:) ::  s_mocomp
            integer dim1_s_mocompArray
            double precision, allocatable, dimension(:,:) ::  mocbase
            integer dim1_mocbaseArray, dim2_mocbaseArray
            integer is_mocomp
            double precision major
            double precision eccentricitySquared
            integer length
            integer width
            double precision rspace
            double precision r0
            double precision height
            double precision rcurv
            real*4 vel
            integer Nrnglooks
            integer Nazlooks
            double precision peglat
            double precision peglon
            double precision peghdg
            integer*8 dopAcc
            double precision prf
            double precision wvl
            double precision, allocatable, dimension(:,:) ::  midpoint
            integer dim1_midpoint, dim2_midpoint
            double precision, allocatable, dimension(:,:) ::  s1sch
            integer dim1_s1sch, dim2_s1sch
            double precision, allocatable, dimension(:,:) ::  s2sch
            integer dim1_s2sch, dim2_s2sch
            double precision, allocatable, dimension(:,:) ::  smsch
            integer dim1_smsch, dim2_smsch
            integer ilrl
        end module correctState 
