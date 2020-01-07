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





        module offoutliersState
            integer*8 ptStdWriter
            integer, allocatable, dimension(:) ::  indexArray
            integer dim1_indexArray
            integer indexArraySize
            real*4 cdn
            real*4 cac
            integer MP
            double precision, allocatable, dimension(:) ::  xd
            integer dim1_xd
            double precision, allocatable, dimension(:) ::  acshift
            integer dim1_acshift
            double precision, allocatable, dimension(:) ::  yd
            integer dim1_yd
            double precision, allocatable, dimension(:) ::  dnshift
            integer dim1_dnshift
            real*4 distance
            double precision, allocatable, dimension(:) ::  sig
            integer dim1_sig
            double precision, allocatable, dimension(:) ::  s
            integer dim1_s
        end module 
