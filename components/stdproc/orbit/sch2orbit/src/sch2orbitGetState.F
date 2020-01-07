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





        subroutine getXYZPosition(array2dT,dim1)
            use sch2orbitState
            implicit none
            integer dim1,i,j
            double precision, dimension(3,dim1):: array2dT
            do i = 1, dim1
                do j = 1, 3
                    array2dT(j,i) = xyz(j,i)
                enddo
            enddo
        end

        subroutine getXYZVelocity(array2dT,dim1)
            use sch2orbitState
            implicit none
            integer dim1,i,j
            double precision, dimension(3,dim1):: array2dT
            do i = 1, dim1
                do j = 1, 3
                    array2dT(j,i) = vxyz(j,i)
                enddo
            enddo
        end

        subroutine getXYZGravitationalAcceleration(array2dT,dim1)
            use sch2orbitState
            implicit none
            integer dim1,i,j
            double precision, dimension(3,dim1):: array2dT
            do i = 1, dim1
                do j = 1, 3
                    array2dT(j,i) = axyz(j,i)
                enddo
            enddo
        end

