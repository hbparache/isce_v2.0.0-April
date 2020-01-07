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





        subroutine allocate_s_mocompArray(dim1)
            use correctState
            implicit none
            integer dim1
            dim1_s_mocompArray = dim1
            allocate(s_mocomp(dim1)) 
        end

        subroutine deallocate_s_mocompArray()
            use correctState
            deallocate(s_mocomp) 
        end

        subroutine allocate_mocbaseArray(dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2
            dim1_mocbaseArray = dim2
            dim2_mocbaseArray = dim1
            allocate(mocbase(dim2,dim1)) 
        end

        subroutine deallocate_mocbaseArray()
            use correctState
            deallocate(mocbase) 
        end

        subroutine allocate_midpoint(dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2
            dim1_midpoint = dim2
            dim2_midpoint = dim1
            allocate(midpoint(dim2,dim1)) 
        end

        subroutine deallocate_midpoint()
            use correctState
            deallocate(midpoint) 
        end

        subroutine allocate_s1sch(dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2
            dim1_s1sch = dim2
            dim2_s1sch = dim1
            allocate(s1sch(dim2,dim1)) 
        end

        subroutine deallocate_s1sch()
            use correctState
            deallocate(s1sch) 
        end

        subroutine allocate_s2sch(dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2
            dim1_s2sch = dim2
            dim2_s2sch = dim1
            allocate(s2sch(dim2,dim1)) 
        end

        subroutine deallocate_s2sch()
            use correctState
            deallocate(s2sch) 
        end

        subroutine allocate_smsch(dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2
            dim1_smsch = dim2
            dim2_smsch = dim1
            allocate(smsch(dim2,dim1)) 
        end

        subroutine deallocate_smsch()
            use correctState
            deallocate(smsch) 
        end

