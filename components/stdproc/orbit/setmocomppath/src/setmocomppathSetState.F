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





        subroutine setStdWriter(varInt)
            use setmocomppathState
            implicit none
            integer*8 varInt
            ptStdWriter = varInt
        end
        subroutine setFirstPosition(array2dT,dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    xyz1(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setFirstVelocity(array2dT,dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    vxyz1(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setSecondPosition(array2dT,dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    xyz2(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setSecondVelocity(array2dT,dim1,dim2)
            use setmocomppathState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    vxyz2(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setPlanetGM(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            GM = varInt
        end

        subroutine setEllipsoidMajorSemiAxis(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            major = varInt
        end

        subroutine setEllipsoidEccentricitySquared(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            eccentricitySquared = varInt
        end

