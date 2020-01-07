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





        module topoState
            use geometryModule
            use orbitModule
            integer numiter
            integer idemwidth
            integer idemlength
            double precision, allocatable, dimension(:) ::  s_mocomp
            integer dim1_s_mocompArray
            double precision firstlat
            double precision firstlon
            double precision deltalat
            double precision deltalon
            integer is_mocomp
            double precision major
            double precision eccentricitySquared
            integer length
            integer width
            double precision rspace
            double precision r0
            double precision height
            double precision rcurv
            real*4 vel
            integer Nrnglooks
            integer Nazlooks
            double precision peglat
            double precision peglon
            double precision peghdg
            double precision prf
            double precision wvl
            integer*8 latAccessor
            integer*8 lonAccessor
            integer*8 heightRAccessor
            integer*8 heightSchAccessor
            integer*8 losAccessor
            integer*8 incAccessor
            double precision azspace
            double precision re
            double precision s0
            double precision send
            double precision min_lat
            double precision min_lon
            double precision max_lat
            double precision max_lon
            double precision, allocatable, dimension(:) ::  squintshift
            integer dim1_squintshift
            integer ilrl
            integer method
            type(orbitType):: orbit
            double precision sensingStart
        end module topoState 
