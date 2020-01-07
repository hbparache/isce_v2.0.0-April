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





        subroutine getGeoWidth(varInt)
            use geocodeState
            implicit none
            integer varInt
            varInt = geowidth
        end

        subroutine getGeoLength(varInt)
            use geocodeState
            implicit none
            integer varInt
            varInt = geolength
        end

        subroutine getLatitudeSpacing(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = latSpacing
        end

        subroutine getLongitudeSpacing(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = lonSpacing
        end

        subroutine getMinimumGeoLatitude(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = geomin_lat
        end

        subroutine getMinimumGeoLongitude(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = geomin_lon
        end

        subroutine getMaximumGeoLatitude(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = geomax_lat
        end

        subroutine getMaxmumGeoLongitude(varInt)
            use geocodeState
            implicit none
            double precision varInt
            varInt = geomax_lon
        end

