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





        subroutine allocate_xyz1(dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2
            dim1_xyz1 = dim2
            dim2_xyz1 = dim1
            allocate(xyz1(dim2,dim1)) 
        end

        subroutine deallocate_xyz1()
            use setmocomppathState
            deallocate(xyz1) 
        end

        subroutine allocate_vxyz1(dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2
            dim1_vxyz1 = dim2
            dim2_vxyz1 = dim1
            allocate(vxyz1(dim2,dim1)) 
        end

        subroutine deallocate_vxyz1()
            use setmocomppathState
            deallocate(vxyz1) 
        end

        subroutine allocate_xyz2(dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2
            dim1_xyz2 = dim2
            dim2_xyz2 = dim1
            allocate(xyz2(dim2,dim1)) 
        end

        subroutine deallocate_xyz2()
            use setmocomppathState
            deallocate(xyz2) 
        end

        subroutine allocate_vxyz2(dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2
            dim1_vxyz2 = dim2
            dim2_vxyz2 = dim1
            allocate(vxyz2(dim2,dim1)) 
        end

        subroutine deallocate_vxyz2()
            use setmocomppathState
            deallocate(vxyz2) 
        end

