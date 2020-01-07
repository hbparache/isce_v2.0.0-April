      subroutine rciq(rawAccessor,nnn,nlinesaz,unpacki,unpackq, &
          irec,ifrst,nbytes,ngood,iflip,ranfft)

      !rawAccessor    -> File pointer
      !nnn            -> Number of azimuth lines in a patch
      !nlinesaz	      -> Size of the output array in range
      !unpacki        -> Unpacking I channel array
      !unpackq        -> Unpacking Q channel array
      !irec           -> First line in the file to read
      !ifrst          -> First pixel to read
      !nbytes         -> Number of bytes in a line in raw file
      !ngood          -> Number of good bytes in a line in raw file
      !iflip          -> If the I/Q channels are flipped 
      !ranfft         -> FFT size for range 

      use arraymodule
      implicit none
      include 'omp_lib.h'

      integer*8 rawAccessor	    !File pointer
      integer*4 ranfft,iflip	    !Size of FFT, I/Q flip
      integer*4 nnn,irec	    !Number of lines, First line to read
      integer*4 ifrst,nbytes        !First pixel to read, Number of bytes per line
      integer*4 ngood,nlinesaz	    !Number of good bytes, Number of range pixels 
      integer*4 i,j                 !Local Variables
      real*4    unpacki(256),unpackq(256)   !Unpacking arrays
      integer colPos,rowPos,numEl   !Local Variables
      complex*8,allocatable :: tmp(:,:)         !Array for storing one line of complex data

      integer*4 ieof;
      write(*,*)'I/Q range starting record, pixel: ',irec,ifrst

!c   init ffts for parallel version
      call cfft1d_jpl(ranfft,tmp,0)	    !Create FFTW plan

!c   checking if I/Q channels need to be flipped
      if(iflip.ne.0.and.iflip.ne.1)then
         write(*,*)'I/Q flip error!'
         stop
      end if
      if(iflip.eq.1)write(*,*)'Flipping i/q data...'

!c   Initialize buffers
      allocate(tmp(ranfft,nnn)) !jng
      trans1 = 0		    !Intialize O/P buffer to zero
      tmp = 0			    !Initialize temporary buffer to zero

!c   Actually read in the buffer
      rowPos = irec + 1		    !First line starts from irec+1
      colPos =  1		    !Starting from first column 
      numEl = nbytes*nnn            !Number of bytes to read
      ieof = 0
      !skip the first ifrst bytes in each line
      call setLineOffset(rawAccessor,ifrst)
      !start from line rowPos
      call initSequentialAccessor(rawAccessor,rowPos)
      do j = 1, nnn 
        call getLineSequential(rawAccessor,tmp(1:ngood/2,j),ieof)
        if(ieof .lt. 0) then
          ! jng note that the eof is reached when reading the full last line.
          ! I would expected that the next read would have set the eof flag. That's
          ! why is not numEl = nbytes*(j-1) 
          numEl = nbytes*j
          exit
        end if
          
      end do
!c   Report if fewer elements were read in
      if(numEl .ne. nbytes*nnn) then
           write(6,*) "Warning. Number of elements requested is ", nbytes*nnn ,"while the number of elements read is", numEl 
      endif

!c    Start of the openmp parallel loop

!$omp parallel &
!$omp shared(nnn,unpacki,unpackq,ifrst,iflip,nbytes,ngood,numEl,trans1,tmp)
!$omp do
      do j = 1, min(numEl/nbytes,nnn)      !For each line read in
         
	 !Fill the rest of the line with zeros
	 do i=ngood/2+1,ranfft   !-ifrst ==> Piyush
            tmp(i,j)=cmplx(0.,0.)

         end do

         !Forward transform the data line 
         call cfft1d_jpl(ranfft,tmp(:,j),-1)
	 !Multiply with the FFT of the reference chirp
         do i=1,ranfft
            tmp(i,j)=tmp(i,j)*ref1(i)

         end do

	 !Inverse Fourier Transform
         call cfft1d_jpl(ranfft,tmp(:,j),1)


	 ! Number of valid samples copied to output
         do i=1,nlinesaz
            trans1(j,i)=tmp(i,j)

         end do
      end do
!$omp end do
!$omp end parallel 

     
      ! Destroy FFTW plans
      call cfft1d_jpl(ranfft,tmp(:,1),2)

      deallocate(tmp)
      return
      end
