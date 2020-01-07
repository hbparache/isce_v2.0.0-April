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





        subroutine allocate_fdArray(dim1)
            use fdmocompState
            implicit none
            integer dim1
            dim1_fdArray = dim1
            allocate(fdArray(dim1)) 
        end

        subroutine deallocate_fdArray()
            use fdmocompState
            deallocate(fdArray) 
        end

        subroutine allocate_vsch(dim1,dim2)
            use fdmocompState
            implicit none
            integer dim1,dim2
            dim1_vsch = dim2
            dim2_vsch = dim1
            allocate(vsch(dim2,dim1)) 
        end

        subroutine deallocate_vsch()
            use fdmocompState
            deallocate(vsch) 
        end

