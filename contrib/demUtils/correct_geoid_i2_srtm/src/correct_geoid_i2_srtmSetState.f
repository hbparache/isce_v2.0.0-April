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





        subroutine setWidth(var)
            use correct_geoid_i2_srtmState
            implicit none
            integer var
            i_samples = var
        end
        subroutine setStdWriter(var)
            use correct_geoid_i2_srtmState
            implicit none
            integer*8 var
            stdWriter = var
        end
        subroutine setStartLatitude(var)
            use correct_geoid_i2_srtmState
            implicit none
            double precision var
            d_clat = var
        end

        subroutine setStartLongitude(var)
            use correct_geoid_i2_srtmState
            implicit none
            double precision var
            d_clon = var
        end

        subroutine setDeltaLatitude(var)
            use correct_geoid_i2_srtmState
            implicit none
            double precision var
            d_dlat = var
        end

        subroutine setDeltaLongitude(var)
            use correct_geoid_i2_srtmState
            implicit none
            double precision var
            d_dlon = var
        end

        subroutine setNumberLines(var)
            use correct_geoid_i2_srtmState
            implicit none
            integer var
            i_numlines = var
        end

        subroutine setConversionType(var)
            use correct_geoid_i2_srtmState
            implicit none
            integer var
            i_sign = var
        end

        subroutine setNullIsWater(var)
            use correct_geoid_i2_srtmState
            implicit none
            integer var
            nullIsWater = var
        end

        subroutine setGeoidFilename(varString, var)
            use iso_c_binding, only: c_char
            use correct_geoid_i2_srtmState
            use fortranUtils
            implicit none
            integer*4 var
            character(kind=c_char, len=1),dimension(var),intent(in)::  varString
            character*50, parameter :: pName = "correct_geoid_i2_srtmSetState::setGeoidFilename"
            call c_to_f_string(pName, varString, var, a_geoidfile, len_geoidfile)
        end


