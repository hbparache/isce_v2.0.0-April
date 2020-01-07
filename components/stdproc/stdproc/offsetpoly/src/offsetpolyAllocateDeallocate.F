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
! Author: Piyush Agram
!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





        subroutine allocateFieldArrays(var)
            use offsetpolyState
            implicit none
            integer :: var
            numOffsets = var
            allocate(r_ranposV(var))
            allocate(r_offV(var))
            allocate(r_azposV(var))
            allocate(r_sigV(var))
        end subroutine allocateFieldArrays

        subroutine deallocateFieldArrays()
            use offsetpolyState
            implicit none
            numOffsets = 0
            deallocate(r_ranposV)
            deallocate(r_azposV)
            deallocate(r_offV)
            deallocate(r_sigV)
        end subroutine deallocateFieldArrays

        subroutine allocatePolyArray(var)
            use offsetpolyState
            implicit none

            integer :: var
            i_ma = var
            allocate(r_polyV(var))
        end subroutine allocatePolyArray

        subroutine deallocatePolyArray()
            use offsetpolyState
            implicit none
            i_ma = 0
            deallocate(r_polyV)
        end subroutine deallocatePolyArray

