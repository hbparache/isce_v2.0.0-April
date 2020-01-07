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





        subroutine allocate_dopplerCentroidCoefficients(dim1)
            use mocompTSXState
            implicit none
            integer dim1
            dim1_dopplerCentroidCoefficients = dim1
            allocate(dopplerCentroidCoefficients(dim1)) 
        end

        subroutine deallocate_dopplerCentroidCoefficients()
            use mocompTSXState
            deallocate(dopplerCentroidCoefficients) 
        end

        subroutine allocate_time(dim1)
            use mocompTSXState
            implicit none
            integer dim1
            dim1_time = dim1
            allocate(time(dim1)) 
        end

        subroutine deallocate_time()
            use mocompTSXState
            deallocate(time) 
        end

        subroutine allocate_sch(dim1,dim2)
            use mocompTSXState
            implicit none
            integer dim1,dim2
            dim1_sch = dim2
            dim2_sch = dim1
            allocate(sch(dim2,dim1)) 
        end

        subroutine deallocate_sch()
            use mocompTSXState
            deallocate(sch) 
        end


