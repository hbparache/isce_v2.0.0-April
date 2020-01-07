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





        subroutine getLocationAcross(array1d,dim1)
            use estimateoffsetsState
            implicit none
            integer dim1,i
            integer, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = locationAcross(i)
            enddo
        end

        subroutine getLocationAcrossOffset(array1d,dim1)
            use estimateoffsetsState
            implicit none
            integer dim1,i
            real*4, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = locationAcrossOffset(i)
            enddo
        end

        subroutine getLocationDown(array1d,dim1)
            use estimateoffsetsState
            implicit none
            integer dim1,i
            integer, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = locationDown(i)
            enddo
        end

        subroutine getLocationDownOffset(array1d,dim1)
            use estimateoffsetsState
            implicit none
            integer dim1,i
            real*4, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = locationDownOffset(i)
            enddo
        end

        subroutine getSNR(array1d,dim1)
            use estimateoffsetsState
            implicit none
            integer dim1,i
            real*4, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = snrRet(i)
            enddo
        end

