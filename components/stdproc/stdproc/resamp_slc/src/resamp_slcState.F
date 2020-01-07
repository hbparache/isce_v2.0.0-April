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





        module resamp_slcState
            use poly2dModule
            integer outwidth
            integer outlength
            integer inwidth
            integer inlength
            integer iscomplex
            integer method
            integer flatten
            real*8 WVL
            real*8 SLR
            real*8 R0

            real*8 REFWVL
            real*8 REFR0
            real*8 REFSLR

            type(poly2dType) :: rgCarrier
            type(poly2dType) :: azCarrier
            type(poly2dType) :: rgOffsetsPoly
            type(poly2dType) :: azOffsetsPoly
            type(poly2dType) :: dopplerPoly
        end module 
