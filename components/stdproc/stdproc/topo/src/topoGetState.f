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





        subroutine getAzimuthSpacing(var)
            use topoState
            implicit none
            double precision var
            var = azspace
        end

        subroutine getPlanetLocalRadius(var)
            use topoState
            implicit none
            double precision var
            var = re
        end

        subroutine getSCoordinateFirstLine(var)
            use topoState
            implicit none
            double precision var
            var = s0
        end

        subroutine getSCoordinateLastLine(var)
            use topoState
            implicit none
            double precision var
            var = send
        end

        subroutine getMinimumLatitude(var)
            use topoState
            implicit none
            double precision var
            var = min_lat
        end

        subroutine getMinimumLongitude(var)
            use topoState
            implicit none
            double precision var
            var = min_lon
        end

        subroutine getMaximumLatitude(var)
            use topoState
            implicit none
            double precision var
            var = max_lat
        end

        subroutine getMaximumLongitude(var)
            use topoState
            implicit none
            double precision var
            var = max_lon
        end

        subroutine getSquintShift(array1d,dim1)
            use topoState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                array1d(i) = squintshift(i)
            enddo
        end

        subroutine getLength(dim1)
            use topoState
            implicit none
            integer dim1
            dim1 = length
        end

