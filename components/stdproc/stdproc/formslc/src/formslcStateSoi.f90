!c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!c copyright: 2010 to the present, california institute of technology.
!c all rights reserved. united states government sponsorship acknowledged.
!c any commercial use must be negotiated with the office of technology transfer
!c at the california institute of technology.
!c 
!c this software may be subject to u.s. export control laws. by accepting this
!c software, the user agrees to comply with all applicable u.s. export laws and
!c regulations. user has the responsibility to obtain export licenses,  or other
!c export authority as may be required before exporting such information to
!c foreign countries or providing access to foreign persons.
!c 
!c installation and use of this software is restricted by a license agreement
!c between the licensee and the california institute of technology. it is the
!c user's responsibility to abide by the terms of the license agreement.
!c
!c Author: Giangi Sacco
!c~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



      
      module formslcStateSoi
          use orbitModule
          use geometryModule
      integer ngood            !Number of good bytes in a line
      integer nbytes           !Number of bytes in a line
      integer ifirstline       !First line to process
      integer na_valid         !Number of valid azimuth lines
      integer ifirstpix        !First range sample
      integer npatches         !Number of azimuth patches
      integer ifirstrgsave     !Starting range bin
      integer nrange           !Number of range bins
      integer nlooks           !Number of azimuth looks
      integer nextend          !Range chirp extension
      integer nazpatch         !Azimuth patch size
      integer overlap          !Overlap between patches
      integer ranfftov         !Offset Video FFT size
      integer ranfftiq         !I/Q FFT size
      integer iflag            !Debug flag
      integer ilrl             !Left [1] / Right [-1] side of satellite
      double precision caltone1    !Caltone location
      double precision rcurv       !Radius of curvature
      double precision vel1        !Platform velocity
      double precision ht1         !Reference height of platform
      double precision prf1        !Pulse repetition frequency
      double precision xmi1        !I-channel bias
      double precision xmq1        !Q-channel bias
      double precision azres       !Desired azimuth resolution
      double precision fs          !Range sampling frequency
      double precision slope       !Range chirp slopre
      double precision pulsedur    !Range chirp duration
      double precision wavl        !Radar wavelength
      double precision rawr001        !Range to first sample in raw
      double precision rhww        !Range spectral weighting
      double precision pctbw       !Spectral shift fraction
      integer*8 ptStdWriter        !Pointer to writer
      integer*8 imrc1Accessor      !Pointer to range compressed image
      integer*8 immocompAccessor   !Pointer to mocomped range compressed image
      integer*8 imrcas1Accessor    !Pointer to range compressed azimuth spectrum
      integer*8 imrcrm1Accessor    !Pointer to range compressed - range migrated 
      integer*8 transAccessor      !Pointer to transformed data
      character*1 iqflip           !I/Q channels are flipped
      character*1 deskew           !Deskewing flag
      character*1 srm              !Secondary range migration flag
      integer mocompPositionSize   !Maximum Azimuth size
      double precision, allocatable, dimension(:,:) ::  sch     !SCH positions
      integer dim1_sch, dim2_sch                                !Dimensions
      double precision, allocatable, dimension(:,:) :: vsch     !VSCH positions
      integer dim1_vsch, dim2_vsch                              !Dimensions
      double precision, allocatable, dimension(:) ::  time      !UTC times
      integer dim1_time                                         !Dimensions
      double precision, allocatable, dimension(:) ::  dopplerCoefficients
      integer dim1_dopplerCoefficients
      
      type planet_type
        double precision :: r_spindot !< Planet spin rate
        double precision :: r_gm !< Planet GM
      end type planet_type

      type(pegType) :: peg
      type(ellipsoidType) :: elp
      type(planet_type) :: pln

      integer  nrangeout        !Number of range bins in the output
      double precision rawr01   !Modified raw starting range with extensions
      double precision slcr01   !SLC starting range modified by mocomp
      double precision shift    !Number of pixels for azimuth shift (KK, ML 2013-07-15)

      type(orbitType) :: orbit  !Input short orbit
      type(orbitType) :: mocompOrbit !Output short orbit
      double precision :: sensingStart !UTC time corresponding to first raw line
      double precision :: slcSensingStart !UTC time corresponding to first slc line
      double precision :: rho_mocomp   !Range used for motion compensation
      type(pegtransType) :: ptm  !For WGS84 to SCH
      end module formslcStateSoi
