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





        subroutine setEllipsoidMajorSemiAxis(varInt)
            use geozeroState
            implicit none
            double precision varInt
            majorSemiAxis = varInt
        end subroutine

        subroutine setEllipsoidEccentricitySquared(varInt)
            use geozeroState
            implicit none
            double precision varInt
            eccentricitySquared = varInt
        end subroutine

        subroutine setMinimumLatitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            min_lat = varInt
        end subroutine

        subroutine setMinimumLongitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            min_lon = varInt
        end subroutine

        subroutine setMaximumLatitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            max_lat = varInt
        end subroutine

        subroutine setMaximumLongitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            max_lon = varInt
        end subroutine

        subroutine setRangePixelSpacing(varInt)
            use geozeroState
            implicit none
            real*8 varInt
            drho = varInt
        end subroutine

        subroutine setLookSide(varInt)
            use geozeroState
            implicit none
            integer varInt
            ilrl = varInt
        end subroutine

        subroutine setRangeFirstSample(varInt)
            use geozeroState
            implicit none
            double precision varInt
            rho0 = varInt
        end subroutine

        subroutine setDopplerAccessor(varInt)
            use geozeroState
            implicit none
            type(poly1dType) ::  varInt
            dopAcc = varInt
        end subroutine

        subroutine setPRF(varInt)
            use geozeroState
            implicit none
            real*8 varInt
            prf = varInt
        end subroutine

        subroutine setRadarWavelength(varInt)
            use geozeroState
            implicit none
            real*8 varInt
            wvl = varInt
        end subroutine

        subroutine setSensingStart(varInt)
            use geozeroState
            implicit none
            double precision varInt
            t0 = varInt
        end subroutine

        subroutine setFirstLatitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            lat_first = varInt
        end subroutine

        subroutine setFirstLongitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            lon_first = varInt
        end subroutine

        subroutine setDeltaLatitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            dlat = varInt
        end subroutine

        subroutine setDeltaLongitude(varInt)
            use geozeroState
            implicit none
            double precision varInt
            dlon = varInt
        end subroutine

        subroutine setLength(varInt)
            use geozeroState
            implicit none
            integer varInt
            length = varInt
        end subroutine

        subroutine setWidth(varInt)
            use geozeroState
            implicit none
            integer varInt
            width = varInt
        end subroutine

        subroutine setNumberRangeLooks(varInt)
            use geozeroState
            implicit none
            integer varInt
            nrnglooks = varInt
        end subroutine

        subroutine setNumberAzimuthLooks(varInt)
            use geozeroState
            implicit none
            integer varInt
            nazlooks = varInt
        end subroutine

        subroutine setDemWidth(varInt)
            use geozeroState
            implicit none
            integer varInt
            demwidth = varInt
        end subroutine

        subroutine setDemLength(varInt)
            use geozeroState
            implicit none
            integer varInt
            demlength = varInt
        end subroutine

        subroutine setOrbit(corb)
            use geozeroState
            implicit none
            type(orbitType):: corb
            orbit = corb
        end subroutine

