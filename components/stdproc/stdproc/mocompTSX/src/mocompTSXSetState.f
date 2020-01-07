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





        subroutine setStdWriter(var)
            use mocompTSXState
            implicit none
            integer var
            stdWriter = var
        end

        subroutine setNumberRangeBins(var)
            use mocompTSXState
            implicit none
            integer var
            nr = var
        end

        subroutine setNumberAzLines(var)
            use mocompTSXState
            implicit none
            integer var
            naz = var
        end

        subroutine setDopplerCentroidCoefficients(array1d,dim1)
            use mocompTSXState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                dopplerCentroidCoefficients(i) = array1d(i)
            enddo
        end

        subroutine setTime(array1d,dim1)
            use mocompTSXState
            implicit none
            integer dim1,i
            double precision, dimension(dim1):: array1d
            do i = 1, dim1
                time(i) = array1d(i)
            enddo
        end

        subroutine setPosition(array2dT,dim1,dim2)
            use mocompTSXState
            implicit none
            integer dim1,dim2,i,j
            double precision, dimension(dim2,dim1):: array2dT
            do i = 1, dim2
                do j = 1, dim1
                    sch(i,j) = array2dT(i,j)
                enddo
            enddo
        end


        subroutine setPlanetLocalRadius(var)
            use mocompTSXState
            implicit none
            double precision var
            rcurv = var
        end

        subroutine setBodyFixedVelocity(var)
            use mocompTSXState
            implicit none
            double precision var
            vel = var
        end

        subroutine setSpacecraftHeight(var)
            use mocompTSXState
            implicit none
            double precision var
            ht = var
        end

        subroutine setPRF(var)
            use mocompTSXState
            implicit none
            double precision var
            prf = var
        end

        subroutine setRangeSamplingRate(var)
            use mocompTSXState
            implicit none
            double precision var
            fs = var
        end

        subroutine setRadarWavelength(var)
            use mocompTSXState
            implicit none
            double precision var
            wvl = var
        end

        subroutine setRangeFisrtSample(var)
            use mocompTSXState
            implicit none
            double precision var
            r0 = var
        end

        subroutine setLookSide(var)
            use mocompTSXState
            implicit none
            integer var
            ilrl = var
        end

        subroutine setEllipsoid(a,e2)
            use mocompTSXState
            implicit none
            double precision :: a, e2
            elp%r_a = a
            elp%r_e2 = e2
        end subroutine setEllipsoid


        subroutine setPegPoint(lat,lon,hdg)
            use mocompTSXState
            implicit none
            double precision :: lat,lon,hdg
            peg%r_lat = lat
            peg%r_lon = lon
            peg%r_hdg = hdg
        end subroutine setPegPoint

        subroutine setOrbit(corb)
            use mocompTSXState
            implicit none

            type(orbitType) :: corb
            orbit = corb
        end subroutine

        subroutine setMocompOrbit(corb)
            use mocompTSXState
            implicit none

            type(orbitType) :: corb
            mocompOrbit = corb
        end subroutine

        subroutine setPlanet(spin,gm)
            use mocompTSXState
            implicit none
            double precision :: spin,gm
            pln%r_spindot = spin
            pln%r_gm = gm
        end subroutine setPlanet

        subroutine setSensingStart(varDbl)
            use mocompTSXState
            implicit none
            double precision varDbl
            sensingStart = varDbl
        end subroutine
