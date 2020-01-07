c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c copyright: 2010 to the present, california institute of technology.
c all rights reserved. united states government sponsorship acknowledged.
c any commercial use must be negotiated with the office of technology transfer
c at the california institute of technology.
c 
c this software may be subject to u.s. export control laws. by accepting this
c software, the user agrees to comply with all applicable u.s. export laws and
c regulations. user has the responsibility to obtain export licenses,  or other
c export authority as may be required before exporting such information to
c foreign countries or providing access to foreign persons.
c 
c installation and use of this software is restricted by a license agreement
c between the licensee and the california institute of technology. it is the
c user's responsibility to abide by the terms of the license agreement.
c
c Author: Giangi Sacco
c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





        subroutine allocate_xyz(dim1,dim2)
            use orbit2schState
            implicit none
            integer dim1,dim2
            dim1_xyz = dim2
            dim2_xyz = dim1
            allocate(xyz(dim2,dim1)) 
        end

        subroutine deallocate_xyz()
            use orbit2schState
            deallocate(xyz) 
        end

        subroutine allocate_vxyz(dim1,dim2)
            use orbit2schState
            implicit none
            integer dim1,dim2
            dim1_vxyz = dim2
            dim2_vxyz = dim1
            allocate(vxyz(dim2,dim1)) 
        end

        subroutine deallocate_vxyz()
            use orbit2schState
            deallocate(vxyz) 
        end

        subroutine allocate_sch(dim1,dim2)
            use orbit2schState
            implicit none
            integer dim1,dim2
            dim1_sch = dim2
            dim2_sch = dim1
            allocate(sch(dim2,dim1)) 
        end

        subroutine deallocate_sch()
            use orbit2schState
            deallocate(sch) 
        end

        subroutine allocate_vsch(dim1,dim2)
            use orbit2schState
            implicit none
            integer dim1,dim2
            dim1_vsch = dim2
            dim2_vsch = dim1
            allocate(vsch(dim2,dim1)) 
        end

        subroutine deallocate_vsch()
            use orbit2schState
            deallocate(vsch) 
        end

        subroutine allocate_asch(dim1,dim2)
            use orbit2schState
            implicit none
            integer dim1,dim2
            dim1_asch = dim2
            dim2_asch = dim1
            allocate(asch(dim2,dim1)) 
        end

        subroutine deallocate_asch()
            use orbit2schState
            deallocate(asch) 
        end

