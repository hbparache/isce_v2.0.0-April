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




        subroutine setInputWidth(varInt)
            use resamp_slcState
            implicit none
            integer varInt
            inwidth = varInt
        end subroutine setInputWidth

        subroutine setInputLines(varInt)
            use resamp_slcState
            implicit none
            integer varInt
            inlength = varInt
        end subroutine setInputLines

        subroutine setOutputLines(varInt)
            use resamp_slcState
            implicit none
            integer varInt
            outlength = varInt
        end subroutine setOutputLines

        subroutine setOutputWidth(varInt)
            use resamp_slcState
            implicit none
            integer varInt
            outwidth = varInt
        end subroutine setOutputWidth

        subroutine setRadarWavelength(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            WVL = varInt
        end subroutine setRadarWavelength

        subroutine setReferenceWavelength(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            REFWVL = varInt
        end subroutine setReferenceWavelength

        subroutine setSlantRangePixelSpacing(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            SLR = varInt
        end subroutine setSlantRangePixelSpacing

        subroutine setReferenceSlantRangePixelSpacing(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            REFSLR = varInt
        end subroutine setReferenceSlantRangePixelSpacing

        subroutine setStartingRange(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            R0 = varInt
        end subroutine setStartingRange

        subroutine setReferenceStartingRange(varInt)
            use resamp_slcState
            implicit none
            real*8 varInt
            REFR0 = varInt
        end subroutine setReferenceStartingRange

        subroutine setRangeCarrier(varPoly)
            use resamp_slcState
            implicit none
            type(poly2dType) :: varPoly
            rgCarrier = varPoly
        end subroutine setRangeCarrier

        subroutine setAzimuthCarrier(varPoly)
            use resamp_slcState
            implicit none
            type(poly2dType) :: varPoly
            azCarrier = varPoly
        end subroutine setAzimuthCarrier

        subroutine setAzimuthOffsetsPoly(varPoly)
            use resamp_slcState
            implicit none
            type(poly2dType) :: varPoly
            azOffsetsPoly = varPoly
        end subroutine setAzimuthOffsetsPoly

        subroutine setRangeOffsetsPoly(varPoly)
            use resamp_slcState
            implicit none
            type(poly2dType) :: varPoly
            rgOffsetsPoly = varPoly
        end subroutine setRangeOffsetsPoly

        subroutine setDopplerPoly(varPoly)
            use resamp_slcState
            implicit none
            type(poly2dType) :: varPoly
            dopplerPoly = varPoly
        end subroutine setDopplerPoly

        subroutine setIsComplex(varInt)
            use resamp_slcState
            implicit none
            integer :: varInt
            iscomplex = varInt
        end subroutine setIsComplex

        subroutine setMethod(varInt)
            use resamp_slcState
            implicit none
            integer :: varInt
            method = varInt
        end subroutine setMethod

        subroutine setFlatten(varInt)
            use resamp_slcState
            implicit none
            integer :: varInt
            flatten = varInt
        end subroutine setFlatten
