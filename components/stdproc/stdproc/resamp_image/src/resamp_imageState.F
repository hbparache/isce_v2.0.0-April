!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
! copyright: 2010 to the present, california institute of technology.
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





        module resamp_imageState
            integer*8 ptStdWriter
            integer i_ma
            integer npl
            integer nl
            integer looks
            integer istoff
            real*4 WVL
            real*4 SLR
            double precision, allocatable, dimension(:) ::  dopplerCoefficients
            integer dim1_dopplerCoefficients
            double precision, allocatable, dimension(:) ::  r_ranposV
            integer dim1_r_ranpos
            double precision, allocatable, dimension(:) ::  r_ranoffV
            integer dim1_r_ranoff
            double precision, allocatable, dimension(:) ::  r_azposV
            integer dim1_r_azpos
            double precision, allocatable, dimension(:) ::  r_azoffV
            integer dim1_r_azoff
            double precision, allocatable, dimension(:) ::  r_sigV
            integer dim1_r_sig
            double precision, allocatable, dimension(:) ::  r_ranpos2V
            integer dim1_r_ranpos2
            double precision, allocatable, dimension(:) ::  r_ranoff2V
            integer dim1_r_ranoff2
            double precision, allocatable, dimension(:) ::  r_azpos2V
            integer dim1_r_azpos2
            double precision, allocatable, dimension(:) ::  r_azoff2V
            integer dim1_r_azoff2
            double precision, allocatable, dimension(:) ::  r_sig2V
            integer dim1_r_sig2
        end module 
