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




        subroutine setStdWriter(varInt)
            use offoutliersState
            implicit none
            integer*8 varInt
            ptStdWriter = varInt
        end

        subroutine setNumberOfPoints(varInt)
            use offoutliersState
            implicit none
            integer varInt
            MP = varInt
        end

        subroutine setLocationAcross(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                xd(i) = array1d(i)
            enddo
        end

        subroutine setLocationAcrossOffset(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                acshift(i) = array1d(i)
            enddo
        end

        subroutine setLocationDown(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                yd(i) = array1d(i)
            enddo
        end

        subroutine setLocationDownOffset(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                dnshift(i) = array1d(i)
            enddo
        end

        subroutine setDistance(varInt)
            use offoutliersState
            implicit none
            real*4 varInt
            distance = varInt
        end

        subroutine setSign(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                sig(i) = array1d(i)
            enddo
        end

        subroutine setSNR(array1d,dim1)
            use offoutliersState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                s(i) = array1d(i)
            enddo
        end

