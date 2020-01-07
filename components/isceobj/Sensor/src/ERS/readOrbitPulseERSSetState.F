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





        subroutine setWidth(varInt)
            use readOrbitPulseERSState
            implicit none
            integer varInt
            width = varInt
        end

        subroutine setICUoffset(varInt)
            use readOrbitPulseERSState
            implicit none
            integer varInt
            ICUoffset = varInt
        end

        subroutine setNumberLines(varInt)
            use readOrbitPulseERSState
            implicit none
            integer varInt
            lines = varInt
        end

        subroutine setSatelliteUTC(varInt)
            use readOrbitPulseERSState
            implicit none
            double precision varInt
            sat_utc = varInt
        end

        subroutine setPRF(varInt)
            use readOrbitPulseERSState
            implicit none
            double precision varInt
            prf = varInt
        end

        subroutine setDeltaClock(varInt)
            use readOrbitPulseERSState
            implicit none
            double precision varInt
            dICU = varInt
        end

        subroutine setEncodedBinaryTimeCode(varInt)
            use readOrbitPulseERSState
            implicit none
            integer*8 varInt
            ICUb = varInt
        end
