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





        module geocodeState
            use poly1dModule
            integer*8 ptStdWriter
            double precision majorSemiAxis
            double precision eccentricitySquared
            double precision min_lat
            double precision min_lon
            double precision max_lat
            double precision max_lon
            double precision peglat
            double precision peglon
            double precision peghdg
            real*4 drho
            double precision rho0
            real*4 h
            double precision ra
            real*4 vel
            type(poly1dType) ::  dopAcc
            real*4 prf
            real*4 wvl
            double precision s0
            double precision daz
            double precision lat_first
            double precision lon_first
            double precision dlat
            double precision dlon
            integer length
            integer width
            integer nrnglooks
            integer nazlooks
            integer ipts
            integer is_mocomp
            integer demwidth
            integer demlength
            double precision, allocatable, dimension(:) ::  s_mocomp
            integer dim1_s_mocomp
            integer geowidth
            integer geolength
            double precision latSpacing
            double precision lonSpacing
            double precision geomin_lat
            double precision geomin_lon
            double precision geomax_lat
            double precision geomax_lon
            integer ilrl
        end module geocodeState 
