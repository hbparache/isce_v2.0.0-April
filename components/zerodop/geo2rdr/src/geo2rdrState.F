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





        module geo2rdrState
            use poly1dModule
            use orbitModule

            !!Planet description
            double precision majorSemiAxis
            double precision eccentricitySquared

            !!Range spacing
            double precision drho
            double precision rho0

            !!Radar Geometry
            type(poly1dType) ::  dopAcc
            type(orbitType) :: orbit

            !!Acquisition properties
            double precision wvl
            double precision t0
            double precision prf
            integer length
            integer width
            integer ilrl

            !!Number of looks
            integer Nrnglooks
            integer Nazlooks

            !!DEM information
            integer demwidth
            integer demlength

            !!Bistatic flag
            logical bistatic

            !!Orbit method
            integer orbitMethod
            integer HERMITE_METHOD, SCH_METHOD, LEGENDRE_METHOD
            parameter(HERMITE_METHOD=0,SCH_METHOD=1,LEGENDRE_METHOD=2) 
        end module geo2rdrState 
