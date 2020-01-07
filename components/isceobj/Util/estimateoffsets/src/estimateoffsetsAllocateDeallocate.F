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





        subroutine allocate_locationAcross(dim1)
            use estimateoffsetsState
            implicit none
            integer dim1
            dim1_locationAcross = dim1
            allocate(locationAcross(dim1)) 
        end

        subroutine deallocate_locationAcross()
            use estimateoffsetsState
            deallocate(locationAcross) 
        end

        subroutine allocate_locationAcrossOffset(dim1)
            use estimateoffsetsState
            implicit none
            integer dim1
            dim1_locationAcrossOffset = dim1
            allocate(locationAcrossOffset(dim1)) 
        end

        subroutine deallocate_locationAcrossOffset()
            use estimateoffsetsState
            deallocate(locationAcrossOffset) 
        end

        subroutine allocate_locationDown(dim1)
            use estimateoffsetsState
            implicit none
            integer dim1
            dim1_locationDown = dim1
            allocate(locationDown(dim1)) 
        end

        subroutine deallocate_locationDown()
            use estimateoffsetsState
            deallocate(locationDown) 
        end

        subroutine allocate_locationDownOffset(dim1)
            use estimateoffsetsState
            implicit none
            integer dim1
            dim1_locationDownOffset = dim1
            allocate(locationDownOffset(dim1)) 
        end

        subroutine deallocate_locationDownOffset()
            use estimateoffsetsState
            deallocate(locationDownOffset) 
        end

        subroutine allocate_snrRet(dim1)
            use estimateoffsetsState
            implicit none
            integer dim1
            dim1_snrRet = dim1
            allocate(snrRet(dim1)) 
        end

        subroutine deallocate_snrRet()
            use estimateoffsetsState
            deallocate(snrRet) 
        end

