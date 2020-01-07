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





        module topozeroState
            use orbitModule
            integer numiter
            integer idemwidth
            integer idemlength
            type(orbitType) :: orbit
            double precision firstlat
            double precision firstlon
            double precision deltalat
            double precision deltalon
            double precision major
            double precision eccentricitySquared
            integer length
            integer width
            double precision rspace
            double precision r0
            integer Nrnglooks
            integer Nazlooks
            double precision peghdg
            double precision prf
            double precision t0
            double precision wvl
            integer*8 latAccessor
            integer*8 lonAccessor
            integer*8 heightAccessor
            integer*8 losAccessor
            integer*8 incAccessor
            integer*8 maskAccessor
            double precision min_lat
            double precision min_lon
            double precision max_lat
            double precision max_lon
            double precision thresh
            integer ilrl
            integer extraiter
            integer method
            integer orbitMethod

            !!!For cropping DEM
            !!!Min global height
            !!!Max global height
            !!!Margin around bbox in degrees
            double precision MIN_H, MAX_H, MARGIN
            parameter(MIN_H=-500.0d0, MAX_H=9000.0d0, MARGIN=0.15d0)

            integer HERMITE_METHOD, LEGENDRE_METHOD, SCH_METHOD
            parameter(HERMITE_METHOD=0,SCH_METHOD=1,LEGENDRE_METHOD=2)
        end module topozeroState 
