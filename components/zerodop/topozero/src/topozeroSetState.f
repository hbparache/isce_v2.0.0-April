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





        subroutine setNumberIterations(var)
            use topozeroState
            implicit none
            integer var
            numiter = var
        end

        subroutine setDemWidth(var)
            use topozeroState
            implicit none
            integer var
            idemwidth = var
        end

        subroutine setDemLength(var)
            use topozeroState
            implicit none
            integer var
            idemlength = var
        end

        subroutine setOrbit(corb)
            use topozeroState
            type(orbitType) :: corb
            orbit = corb
        end

        subroutine setFirstLatitude(var)
            use topozeroState
            implicit none
            double precision var
            firstlat = var
        end

        subroutine setFirstLongitude(var)
            use topozeroState
            implicit none
            double precision var
            firstlon = var
        end

        subroutine setDeltaLatitude(var)
            use topozeroState
            implicit none
            double precision var
            deltalat = var
        end

        subroutine setDeltaLongitude(var)
            use topozeroState
            implicit none
            double precision var
            deltalon = var
        end


        subroutine setEllipsoidMajorSemiAxis(var)
            use topozeroState
            implicit none
            double precision var
            major = var
        end

        subroutine setEllipsoidEccentricitySquared(var)
            use topozeroState
            implicit none
            double precision var
            eccentricitySquared = var
        end

        subroutine setLength(var)
            use topozeroState
            implicit none
            integer var
            length = var
        end

        subroutine setWidth(var)
            use topozeroState
            implicit none
            integer var
            width = var
        end

        subroutine setRangePixelSpacing(var)
            use topozeroState
            implicit none
            double precision var
            rspace = var
        end

        subroutine setRangeFirstSample(var)
            use topozeroState
            implicit none
            double precision var
            r0 = var
        end

        subroutine setNumberRangeLooks(var)
            use topozeroState
            implicit none
            integer var
            Nrnglooks = var
        end

        subroutine setNumberAzimuthLooks(var)
            use topozeroState
            implicit none
            integer var
            Nazlooks = var
        end

        subroutine setPegHeading(var)
            use topozeroState
            implicit none
            double precision var
            peghdg = var
        end

        subroutine setPRF(var)
            use topozeroState
            implicit none
            double precision var
            prf = var
        end

        subroutine setSensingStart(var)
            use topozeroState
            implicit none
            double precision var
            t0 = var
        end

        subroutine setRadarWavelength(var)
            use topozeroState
            implicit none
            double precision var
            wvl = var
        end

        subroutine setLatitudePointer(var)
            use topozeroState
            implicit none
            integer*8 var
            latAccessor = var
        end

        subroutine setLongitudePointer(var)
            use topozeroState
            implicit none
            integer*8 var
            lonAccessor = var
        end

        subroutine setHeightPointer(var)
            use topozeroState
            implicit none
            integer*8 var
            heightAccessor = var
        end

        subroutine setLosPointer(var)
            use topozeroState
            implicit none
            integer*8 var
            losAccessor=var
        end

        subroutine setIncPointer(var)
            use topozeroState
            implicit none
            integer*8 var
            incAccessor = var
        end

        subroutine setMaskPointer(var)
            use topozeroState
            implicit none
            integer*8 var
            maskAccessor = var
        end 

        subroutine setLookSide(var)
            use topozeroState
            implicit none
            integer var
            ilrl = var
        end

        subroutine setSecondaryIterations(var)
            use topozeroState
            implicit none
            integer var
            extraiter = var
        end

        subroutine setThreshold(var)
            use topozeroState
            implicit none 
            double precision var
            thresh = var
        end 

        subroutine setMethod(var)
            use topozeroState
            implicit none
            integer var
            method = var
        end

        subroutine setOrbitMethod(var)
            use topozeroState
            implicit none
            integer var
            orbitMethod = var
        end
