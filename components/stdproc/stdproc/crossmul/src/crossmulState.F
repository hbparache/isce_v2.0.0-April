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





        module crossmulState
        use, intrinsic:: iso_c_binding

            type, bind(C) :: crossmulType
                integer(C_INT) :: na    !c Number across in range
                integer(C_INT) :: nd    !c Number down in azimuth
                real(C_DOUBLE) ::  scale  !c Scaling the numbers numerically
                integer (C_INT):: looksac          !c Looks across
                integer (C_INT):: looksdn          !c Looks down
                integer (C_INT):: blocksize        !c Number of azimuth lines in a block
                real(C_DOUBLE) :: wvl1  !c Master wavelength
                real(C_DOUBLE) :: wvl2  !c Slave wavelength
                real(C_DOUBLE) :: drg1  !c Master slant range spacing
                real(C_DOUBLE) :: drg2  !c Slave slant range spacing
                integer(C_INT) :: flatten  !c Flatten flag
                real(C_DOUBLE) :: wgt  !c Range filter weight
            end type crossmulType
        end module crossmulState
