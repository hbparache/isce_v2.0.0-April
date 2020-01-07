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





        subroutine allocate_dopplerCoefficients(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_dopplerCoefficients = dim1
            allocate(dopplerCoefficients(dim1)) 
        end

        subroutine deallocate_dopplerCoefficients()
            use resamp_onlyState
            deallocate(dopplerCoefficients) 
        end

        subroutine allocate_r_ranpos(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_ranpos = dim1
            allocate(r_ranposV(dim1)) 
        end

        subroutine deallocate_r_ranpos()
            use resamp_onlyState
            deallocate(r_ranposV) 
        end

        subroutine allocate_r_ranoff(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_ranoff = dim1
            allocate(r_ranoffV(dim1)) 
        end

        subroutine deallocate_r_ranoff()
            use resamp_onlyState
            deallocate(r_ranoffV) 
        end

        subroutine allocate_r_azpos(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_azpos = dim1
            allocate(r_azposV(dim1)) 
        end

        subroutine deallocate_r_azpos()
            use resamp_onlyState
            deallocate(r_azposV) 
        end

        subroutine allocate_r_azoff(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_azoff = dim1
            allocate(r_azoffV(dim1)) 
        end

        subroutine deallocate_r_azoff()
            use resamp_onlyState
            deallocate(r_azoffV) 
        end

        subroutine allocate_r_sig(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_sig = dim1
            allocate(r_sigV(dim1)) 
        end

        subroutine deallocate_r_sig()
            use resamp_onlyState
            deallocate(r_sigV) 
        end

        subroutine allocate_r_ranpos2(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_ranpos2 = dim1
            allocate(r_ranpos2V(dim1)) 
        end

        subroutine deallocate_r_ranpos2()
            use resamp_onlyState
            deallocate(r_ranpos2V) 
        end

        subroutine allocate_r_ranoff2(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_ranoff2 = dim1
            allocate(r_ranoff2V(dim1)) 
        end

        subroutine deallocate_r_ranoff2()
            use resamp_onlyState
            deallocate(r_ranoff2V) 
        end

        subroutine allocate_r_azpos2(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_azpos2 = dim1
            allocate(r_azpos2V(dim1)) 
        end

        subroutine deallocate_r_azpos2()
            use resamp_onlyState
            deallocate(r_azpos2V) 
        end

        subroutine allocate_r_azoff2(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_azoff2 = dim1
            allocate(r_azoff2V(dim1)) 
        end

        subroutine deallocate_r_azoff2()
            use resamp_onlyState
            deallocate(r_azoff2V) 
        end

        subroutine allocate_r_sig2(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_r_sig2 = dim1
            allocate(r_sig2V(dim1)) 
        end

        subroutine deallocate_r_sig2()
            use resamp_onlyState
            deallocate(r_sig2V) 
        end

        subroutine allocate_azimuthCarrier(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_azimuthCarrier = dim1
            allocate(azimuthCarrier(dim1)) 
        end

        subroutine deallocate_azimuthCarrier()
            use resamp_onlyState
            deallocate(azimuthCarrier) 
        end

        subroutine allocate_rangeCarrier(dim1)
            use resamp_onlyState
            implicit none
            integer dim1
            dim1_rangeCarrier = dim1
            allocate(rangeCarrier(dim1)) 
        end

        subroutine deallocate_rangeCarrier()
            use resamp_onlyState
            deallocate(rangeCarrier) 
        end

