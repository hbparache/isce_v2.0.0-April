c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c copyright: 2010 to the present, california institute of technology.
c all rights reserved. united states government sponsorship acknowledged.
c any commercial use must be negotiated with the office of technology transfer
c at the california institute of technology.
c 
c this software may be subject to u.s. export control laws. by accepting this
c software, the user agrees to comply with all applicable u.s. export laws and
c regulations. user has the responsibility to obtain export licenses,  or other
c export authority as may be required before exporting such information to
c foreign countries or providing access to foreign persons.
c 
c installation and use of this software is restricted by a license agreement
c between the licensee and the california institute of technology. it is the
c user's responsibility to abide by the terms of the license agreement.
c
c Author: Giangi Sacco
c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





        subroutine getPegLatitude(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = pegLatitude
        end

        subroutine getPegLongitude(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = pegLongitude
        end

        subroutine getPegHeading(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = pegHeading
        end

        subroutine getPegRadiusOfCurvature(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = pegRadiusOfCurvature
        end

        subroutine getFirstAverageHeight(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = have1
        end

        subroutine getSecondAverageHeight(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = have2
        end

        subroutine getFirstProcVelocity(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = vel1
        end

        subroutine getSecondProcVelocity(varInt)
            use setmocomppathState
            implicit none
            double precision varInt
            varInt = vel2
        end

