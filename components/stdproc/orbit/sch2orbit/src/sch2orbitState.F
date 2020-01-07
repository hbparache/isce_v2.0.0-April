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





        module sch2orbitState
            integer*8 ptStdWriter
            double precision, allocatable, dimension(:,:) ::  xyz
            integer len_vec
            double precision, allocatable, dimension(:,:) ::  vxyz
            double precision, allocatable, dimension(:,:) ::  axyz
            double precision major
            double precision eccentricitySquared
            double precision pegLatitude
            double precision pegLongitude
            double precision pegHeading
            double precision radius
            double precision GM
            double precision, allocatable, dimension(:,:) ::  sch
            double precision, allocatable, dimension(:,:) ::  vsch
        end module sch2orbitState 
