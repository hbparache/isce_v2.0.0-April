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





        module estimateoffsetsRead
            implicit none

            contains
                subroutine readCpxAmp(acc,arr,irow,band,n,carr)
                    complex, dimension(:) :: carr
                    real, dimension(:)  :: arr
                    integer*8 :: acc
                    integer :: irow,band,n,i

                    call getLineBand(acc,carr,band,irow)
                    !call getLine(acc, carr, irow)
                    do i=1,n
                        arr(i) = cabs(carr(i))
                    end do
                end subroutine readCpxAmp

                subroutine readAmp(acc,arr,irow,band,n,carr)
                    complex, dimension(:) :: carr
                    real, dimension(:) :: arr
                    integer*8 :: acc
                    integer :: irow,band,n

                    call getLineBand(acc,arr,band,irow)
                end subroutine

        end module estimateoffsetsRead 
