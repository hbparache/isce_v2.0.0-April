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





        module mocompTSXState
            use orbitModule
            use geometryModule

            integer stdWriter
            integer nr
            integer naz
            double precision, allocatable, dimension(:) ::  dopplerCentroidCoefficients
            integer dim1_dopplerCentroidCoefficients
            double precision, allocatable, dimension(:) ::  time
            integer dim1_time
            double precision, allocatable, dimension(:,:) ::  sch
            integer dim1_sch, dim2_sch
            double precision rcurv
            double precision vel
            double precision ht
            double precision prf
            double precision fs
            double precision wvl
            double precision r0
            integer dim1_i_mocomp
            integer mocompPositionSize
            integer ilrl
            double precision adjustr0

            type planet_type
              double precision :: r_spindot !< Planet spin rate
              double precision :: r_gm !< Planet GM
            end type planet_type
            type(orbitType) :: orbit  !Input short orbit
            type(orbitType) :: mocompOrbit !Output short orbit
            double precision :: sensingStart !UTC time corresponding to first raw line
            double precision :: slcSensingStart !UTC time corresponding to first slc line
            double precision :: rho_mocomp   !Range used for motion compensation
            type(pegtransType) :: ptm  !For WGS84 to SCH
            type(pegType) :: peg
            type(ellipsoidType) :: elp
            type(planet_type) :: pln

        end module
