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





        subroutine setReferenceOrbit(array1d,dim1)
            use correctState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                s_mocomp(i) = array1d(i)
            enddo
        end

        subroutine setMocompBaseline(array2dT,dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    mocbase(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setISMocomp(var)
            use correctState
            implicit none
            integer var
            is_mocomp = var
        end

        subroutine setEllipsoidMajorSemiAxis(var)
            use correctState
            implicit none
            double precision var
            major = var
        end

        subroutine setEllipsoidEccentricitySquared(var)
            use correctState
            implicit none
            double precision var
            eccentricitySquared = var
        end

        subroutine setLength(var)
            use correctState
            implicit none
            integer var
            length = var
        end

        subroutine setWidth(var)
            use correctState
            implicit none
            integer var
            width = var
        end

        subroutine setRangePixelSpacing(var)
            use correctState
            implicit none
            double precision var
            rspace = var
        end

        subroutine setLookSide(var)
            use correctState
            implicit none
            integer var
            ilrl = var
        end

        subroutine setRangeFirstSample(var)
            use correctState
            implicit none
            double precision var
            r0 = var
        end

        subroutine setSpacecraftHeight(var)
            use correctState
            implicit none
            double precision var
            height = var
        end

        subroutine setPlanetLocalRadius(var)
            use correctState
            implicit none
            double precision var
            rcurv = var
        end

        subroutine setBodyFixedVelocity(var)
            use correctState
            implicit none
            real*4 var
            vel = var
        end

        subroutine setNumberRangeLooks(var)
            use correctState
            implicit none
            integer var
            Nrnglooks = var
        end

        subroutine setNumberAzimuthLooks(var)
            use correctState
            implicit none
            integer var
            Nazlooks = var
        end

        subroutine setPegLatitude(var)
            use correctState
            implicit none
            double precision var
            peglat = var
        end

        subroutine setPegLongitude(var)
            use correctState
            implicit none
            double precision var
            peglon = var
        end

        subroutine setPegHeading(var)
            use correctState
            implicit none
            double precision var
            peghdg = var
        end

        subroutine setPRF(var)
            use correctState
            implicit none
            double precision var
            prf = var
        end

        subroutine setRadarWavelength(var)
            use correctState
            implicit none
            double precision var
            wvl = var
        end

        subroutine setMidpoint(array2dT,dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    midpoint(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setSch1(array2dT,dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    s1sch(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setSch2(array2dT,dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    s2sch(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setSc(array2dT,dim1,dim2)
            use correctState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    smsch(i,j) = array2dT(i,j)
                enddo
            enddo
        end

        subroutine setDopCoeff(var)
            use correctState
            implicit none
            integer*8 var
            dopAcc = var
        end subroutine setDopCoeff

