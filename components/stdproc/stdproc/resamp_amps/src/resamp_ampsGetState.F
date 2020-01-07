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





        subroutine getULRangeOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = ULRangeOffset
        end

        subroutine getULAzimuthOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = ULAzimuthOffset
        end

        subroutine getURRangeOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = URRangeOffset
        end

        subroutine getURAzimuthOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = URAzimuthOffset
        end

        subroutine getLLRangeOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = LLRangeOffset
        end

        subroutine getLLAzimuthOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = LLAzimuthOffset
        end

        subroutine getLRRangeOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = LRRangeOffset
        end

        subroutine getLRAzimuthOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = LRAzimuthOffset
        end

        subroutine getCenterRangeOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = CenterRangeOffset
        end

        subroutine getCenterAzimuthOffset(varInt)
            use resamp_ampsState
            implicit none
            double precision varInt
            varInt = CenterAzimuthOffset
        end

