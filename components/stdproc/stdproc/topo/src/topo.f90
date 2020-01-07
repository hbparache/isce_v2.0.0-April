!c  topocorrect - approximate topo correction
    subroutine topo(demAccessor, dopAccessor)
      use topoState
      use topoMethods
      use fortranUtils
      use linalg3Module
      use geometryModule

      implicit none
      include 'omp_lib.h'
      integer*8 demAccessor,dopAccessor
      integer lineFile,mocompSize
      !integer width, length
      real*4, allocatable :: z(:),zsch(:)
      real*8, allocatable :: lat(:), lon(:)
      real*4, allocatable :: losang(:)
      real*4, allocatable :: incang(:)
      real*8, allocatable :: dopline(:)
      real*4, allocatable :: distance(:)
      real*8 terheight, radius0
      real*8, allocatable :: rho(:)
      !real*8, allocatable :: rho(:,:),squintshift(:)
      real*4, allocatable :: dem(:,:)
      real*8 sch_p_first(3),sch_p_last(3),sch(3),xyz(3),llh(3)

      !!! To deal with symmetry - PSA
      real*8 llh_prev(3), xyz_prev(3)
      real*8 xyzsat(3), schsat(3)
      real*8 enumat(3,3), xyz2enu(3,3)
      real*8 enu(3)
      integer, allocatable :: converge(:)
      real*8  thresh
      integer totalconv

      real*8 r2d,refhgt
      integer pixel
      real*8 beta
      real*8 tanbeta,cosalpha
      real*8 look_angle, beta_angle
      real*8 fd
      real*8 arg,rminoraxis,rlatg,st,ct
      real*4 z1,z2
      real*8 fraclat,fraclon,demlat,demlon
      integer line,iter
      integer idemlat,idemlon,i_type,i,j!,i_cnt1,i_cnt2,i_loff,i_el,i_sl
      real*8 pi
      integer extraiter 
      integer,parameter :: b1=1
      integer,parameter :: b2=1

!c  types needed

        type(ellipsoidType) :: elp
        type(pegType) :: peg
        type(pegtransType) :: ptm


        procedure(intpTemplate), pointer :: intp_dem => null()
          !!!Set up DEM interpolation method
          if (method.eq.SINC_METHOD) then
            intp_dem => intp_sinc
          else if (method.eq.BILINEAR_METHOD) then
            intp_dem => intp_bilinear
          else if (method.eq.BICUBIC_METHOD) then
            intp_dem => intp_bicubic
          else if (method.eq.NEAREST_METHOD) then
            intp_dem => intp_nearest
          else if (method.eq.AKIMA_METHOD) then
            intp_dem => intp_akima
          else if (method.eq.BIQUINTIC_METHOD) then
              intp_dem => intp_biquintic
          else
            print *, 'Undefined interpolation method.'
            stop
          endif
          call prepareMethods(method)


        pi = getPI()

        lineFile  = 0

        !!Number of extra iterations to eliminate symmetry issues
        !!PSA
        extraiter = 10
        thresh = 0.10   !!For convergence
        totalconv = 0

        min_lat = 10000.
        max_lat = -10000.
        min_lon = 10000.
        max_lon = -10000.
        
!$omp parallel
        if(omp_get_thread_num().eq.1) then
            write(6,*), 'Max threads used: ', omp_get_num_threads()
        end if
!$omp end parallel

!c this should be fixed by decoupling the mocomp array length from the interferogram length
!c      
        print *,'start sample, length : ',is_mocomp,length
        length=min(length,(dim1_s_mocompArray+Nazlooks/2-is_mocomp)/Nazlooks)
        print *, 'reset length: ',length

!c  allocate variable arrays
        allocate (lat(width))
        allocate (lon(width))
        allocate (dopline(width))
        allocate (z(width))
        allocate (zsch(width))
        allocate (rho(width))
        allocate (distance(width))
        allocate (losang(2*width))
        allocate (incang(width))
        allocate (converge(width)) !!PSA

!c  some constants
      refhgt=0
      r2d=180.d0/pi
      elp%r_a = major
      elp%r_e2 = eccentricitySquared
      
      peg%r_lat =  peglat
      peg%r_lon =  peglon
      peg%r_hdg =  peghdg

!c  get re and insert it into database
      rminoraxis=sqrt(1.-elp%r_e2)*elp%r_a
      rlatg = atan(tan(peg%r_lat)*elp%r_a*elp%r_a/(rminoraxis*rminoraxis));
      st = sin(rlatg);
      ct = cos(rlatg);
      arg = (ct*ct)/(elp%r_a*elp%r_a) + (st*st)/(rminoraxis*rminoraxis);
      re = 1./(sqrt(arg));
      print *,'re, rminoraxis',re,rminoraxis
      print *,'Local earth radius of curvature: ',rcurv

      print *,'DEM parameters:'
      print *,idemwidth,idemlength,firstlon,firstlat,deltalon,deltalat
      print *

!c  allocate dem array
      allocate (dem(idemwidth,idemlength))

          do j=1,idemlength
              call getLineSequential(demAccessor,dem(:,j),lineFile)
          enddo

      print *,'read DEM: ',idemlength

      !c  initialize the transformation matrices

      radius0 =  rdir(elp,peg%r_hdg,peg%r_lat)
      terheight = rcurv - radius0
      call radar_to_xyz(elp,peg,ptm,terheight)


!c  Interpolate the orbit here for comparison
      !!!!Compare s_mocomp with orbit interpolation
      do line = 1, length
         beta = sensingStart + (line-1) * Nazlooks /prf 
         pixel = interpolateWGS84Orbit_f(orbit, beta, xyz, sch)
         if (pixel .ne. 0) then
             print *, 'Orbit interpolation failed in line ', line
             stop
         endif

         call convert_sch_to_xyz(ptm, sch, xyz, XYZ_2_SCH)

         if (mod(line,200).eq.1) then
             print *, 'Line: ', line, s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2)
             print *, 'Delta s: ', sch(1) - s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2), rcurv * vel/(prf*(rcurv+height))
             print *, 'C : ', sch(2)
             print *, 'Delta h: ', sch(3) - height
         endif

      enddo


!c  precalculate squint-related shift for each range location
      line=1
      call getLine(dopAccessor,dopline, line)
      do pixel=1,width
         rho(pixel)=r0+rspace*(pixel-1)*Nrnglooks
         tanbeta=-prf*dopline(pixel)*(height+rcurv)*wvl*rho(pixel)/vel/(rcurv**2+(height+rcurv)**2-rho(pixel)**2)
         squintshift(pixel) = -rcurv*atan(tanbeta)
      end do

      print *,'is_mocomp,length: ',is_mocomp, length
      print *,'first, last mocomp addresses: ',is_mocomp+1*Nazlooks-Nazlooks/2,is_mocomp+length*Nazlooks-Nazlooks/2
      print *,'mocomp array dimension: ',dim1_s_mocompArray

!c  sch of s/c at line 1
      sch_p_first(1)=s_mocomp(is_mocomp+1*Nazlooks-Nazlooks/2)
      sch_p_first(2)=0.
      sch_p_first(3)=height

!c  sch of s/c at last line
      sch_p_last(1)=s_mocomp(is_mocomp+length*Nazlooks-Nazlooks/2)
      sch_p_last(2)=0.
      sch_p_last(3)=height
 
      print *,'calculated sch first and last: ',sch_p_first, sch_p_last



!c  lat lon of s/c, line 1
      i_type=SCH_2_XYZ
      call convert_sch_to_xyz(ptm,sch_p_first,xyz,i_type)
      i_type=XYZ_2_LLH
      call latlon(elp,xyz,llh,i_type)
      print *,sch_p_first,' sch s/c first'
      print *,llh(1)*r2d,llh(2)*r2d,llh(3),' lat/lon s/c line 1'
!c  lat lon of s/c, line last
      i_type=SCH_2_XYZ
      call convert_sch_to_xyz(ptm,sch_p_last,xyz,i_type)
      i_type=XYZ_2_LLH
      call latlon(elp,xyz,llh,i_type)
      print *,sch_p_last,' sch s/c last'
      print *,llh(1)*r2d,llh(2)*r2d,llh(3),' lat/lon s/c line last'
      print *

!c  sch of line 1, pixel 1
      line=1
      pixel=1
!c  save rho to the point
      rho(pixel)=r0+rspace*(pixel-1)*Nrnglooks
      cosalpha=((height+rcurv)**2+rcurv**2-rho(pixel)**2)/2./(height+rcurv)/rcurv
      sch(1)=s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2)
      sch(1)=sch(1)+squintshift(pixel)
      beta=-squintshift(pixel)/rcurv

      !!Look side of satellite matters for C coordinate
      sch(2)=ilrl*rcurv*acos(cosalpha/cos(beta))
      sch(3)=0.
      s0=sch(1)

      print *,sch,' sch line 1 pixel 1'

!c  lat lon of location 1,1
      i_type=SCH_2_XYZ
      call convert_sch_to_xyz(ptm,sch,xyz,i_type)

      i_type=XYZ_2_LLH
      call latlon(elp,xyz,llh,i_type)

      print *,llh(1)*r2d,llh(2)*r2d,llh(3),' lat/lon 1,1'

!c  sch of line last, pixel last
      line=length
      call getLine(dopAccessor, dopline, line)
      do pixel=1,width
           tanbeta=-prf*dopline(pixel)*(height+rcurv)*wvl*rho(pixel)/vel/(rcurv  **2+(height+rcurv)**2-rho(pixel)**2)
           squintshift(pixel) = -rcurv*atan(tanbeta)
      end do
      pixel=width
!c  save rho to the point
      rho(pixel)=r0+rspace*(pixel-1)*Nrnglooks
      cosalpha=((height+rcurv)**2+rcurv**2-rho(pixel)**2)/2./(height+rcurv)/rcurv
      sch(1)=s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2)
      sch(1)=sch(1)+squintshift(pixel)
      beta=-squintshift(pixel)/rcurv 

      !!Accounting for look side of the satellite
      sch(2)=ilrl*rcurv*acos(cosalpha/cos(beta))
      sch(3)=0.
      send=sch(1)
      azspace=(send-s0)/(length-1)

      print *,sch,' sch line last pixel last ',is_mocomp+line*Nazlooks-Nazlooks/2

!c  lat lon of location
      i_type=SCH_2_XYZ
      call convert_sch_to_xyz(ptm,sch,xyz,i_type)

      i_type=XYZ_2_LLH
      call latlon(elp,xyz,llh,i_type)

      print *,llh(1)*r2d,llh(2)*r2d,llh(3),' lat/lon line last pixel last'




      !!!File for debugging
!!      open(31, file='distance',access='direct',recl=4*width,form='unformatted')

      call rewindAccessor(dopAccessor)
      do line=1, length         !c For each line 
                ! Initialize lat lon arrays

             !!!Setup doppler information           
            call getLineSequential(dopAccessor, dopline, pixel)
            do pixel=1,width
                 tanbeta=-prf*dopline(pixel)*(height+rcurv)*wvl*rho(pixel)/vel  /(rcurv**2+(height+rcurv)**2-rho(pixel)**2)
                 squintshift(pixel) = -rcurv*atan(tanbeta)
            end do
            if (mod(line,1000).eq.1) then
                print *, 'Line :', line, prf*dopline(1), prf*dopline(width/2),prf*dopline(width)
            endif

         converge = 0     !!PSA
         zsch = 0.
         do iter=1,numiter+extraiter+1

            !$omp parallel do private(pixel,sch,beta,cosalpha) &
            !$omp private(i_type,llh,idemlat,idemlon,xyz,arg) &
            !$omp private(z1,z2,fraclat,fraclon,demlat,demlon) &
            !$omp private(llh_prev,xyz_prev,xyzsat,schsat) &
            !$omp shared(length,width,is_mocomp,s_mocomp,Nazlooks,height) &
            !$omp shared(rcurv,rho,ptm,elp,lat,lon,z,zsch,line,ilrl,iter) &
            !$omp shared(distance,converge,thresh,numiter,totalconv)&
            !$omp shared(idemwidth,idemlength)
            do pixel=1,width

               if(converge(pixel).eq.0) then

                  !!!!Save previous llh in degrees and meters
                  llh_prev(1) = lat(pixel)*pi/180.0d0
                  llh_prev(2) = lon(pixel)*pi/180.0d0
                  llh_prev(3) = z(pixel)

                  !c  sch of line, pixel
                  cosalpha=((height+rcurv)**2+(rcurv+zsch(pixel))**2-rho(pixel)**2)/2./(height+rcurv)/(rcurv+zsch(pixel))
                  sch(1)=s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2)
                  schsat(1) = sch(1)

                  sch(1)=sch(1)+squintshift(pixel)
                  beta=-squintshift(pixel)/rcurv

                  !!Account for satellite look side
                  sch(2)=ilrl*rcurv*acos(cosalpha/cos(beta))
                  schsat(2) = 0.

                  sch(3)=zsch(pixel)
                  schsat(3)=height

                  !c Convert to xyz for sat
                  i_type=SCH_2_XYZ
                  call convert_sch_to_xyz(ptm,schsat,xyzsat,i_type)

                  !c  lat lon of location
                  i_type=SCH_2_XYZ
                  call convert_sch_to_xyz(ptm,sch,xyz,i_type)
                  i_type=XYZ_2_LLH
                  call latlon(elp,xyz,llh,i_type)

                  !c  convert lat, lon, hgt to xyz coordinates
                  lat(pixel)=llh(1)*r2d
                  lon(pixel)=llh(2)*r2d
                  demlat=(lat(pixel)-firstlat)/deltalat+1
                  demlon=(lon(pixel)-firstlon)/deltalon+1
                  if(demlat.lt.1)demlat=1
                  if(demlat.gt.idemlength-1)demlat=idemlength-1
                  if(demlon.lt.1)demlon=1
                  if(demlon.gt.idemwidth-1)demlon=idemwidth-1

                  !!!!! This whole part can be put into a function 
                  idemlat=int(demlat)
                  idemlon=int(demlon)
                  fraclat=demlat-idemlat
                  fraclon=demlon-idemlon

                  z(pixel) = intp_dem(dem,idemlon,idemlat,fraclon,fraclat,idemwidth,idemlength)
                  !!!!!! This whole part can be put into a function


                  if(z(pixel).lt.-500.0)z(pixel)=-500.0

                  ! given llh, where h = z(pixel,line) in WGS84, get the SCH height
                  llh(1) = lat(pixel)*pi/180.d0
                  llh(2) = lon(pixel)*pi/180.d0
                  llh(3) = z(pixel)

                  i_type = LLH_2_XYZ
                  call latlon(elp,xyz,llh,i_type)
                  i_type = XYZ_2_SCH
                  call convert_sch_to_xyz(ptm,sch,xyz,i_type)
                  ! print *, 'after = ', sch
                  zsch(pixel) = sch(3)

                  !!!!Absolute distance
                  distance(pixel) = sqrt((xyz(1)-xyzsat(1))**2 +(xyz(2)-xyzsat(2))**2 + (xyz(3)-xyzsat(3))**2) - rho(pixel)

                  if(abs(distance(pixel)).le.thresh) then
                     zsch(pixel) = sch(3)
                     converge(pixel) = 1
                     totalconv = totalconv+1

                 else if(iter.gt.(numiter+1)) then
                     i_type=LLH_2_XYZ
                     call latlon(elp, xyz_prev,llh_prev,i_type)

                     xyz(1) = 0.5*(xyz_prev(1)+xyz(1))
                     xyz(2) = 0.5*(xyz_prev(2)+xyz(2))
                     xyz(3) = 0.5*(xyz_prev(3)+xyz(3))


                     !!!!Repopulate lat,lon,z
                     i_type=XYZ_2_LLH
                     call latlon(elp,xyz,llh,i_type)
                     lat(pixel) = llh(1)*r2d
                     lon(pixel) = llh(2)*r2d
                     z(pixel) = llh(3)

                     i_type=XYZ_2_SCH
                     call convert_sch_to_xyz(ptm,sch,xyz,i_type)
                     zsch(pixel) = sch(3)
                     !!!!Absolute distance
                     distance(pixel) = sqrt((xyz(1)-xyzsat(1))**2 +(xyz(2)-xyzsat(2))**2 + (xyz(3)-xyzsat(3))**2) - rho(pixel)
                 endif
             endif

            end do
            !$omp end parallel do

         end do

         !!Setup satellite position for the line
         schsat(1)=s_mocomp(is_mocomp+line*Nazlooks-Nazlooks/2)
         schsat(2) = 0.
         schsat(3)=height

         i_type=SCH_2_XYZ
         call convert_sch_to_xyz(ptm,schsat,xyzsat,i_type)

         !$omp parallel do private(pixel,look_angle,beta_angle,beta,cosalpha) &
         !$omp private(xyz,sch,llh,i_type,enumat,xyz2enu,enu)&
         !$omp private(demlat,demlon,idemlat,idemlon,fraclat,fraclon)&
         !$omp shared(zsch,line,rcurv,rho,height,losang,width,ptm) &
         !$omp shared(squintshift,peghdg,r2d,ilrl,schsat,xyzsat,elp)&
         !$omp shared(incang,firstlat,firstlon,deltalat,deltalon)&
         !$omp shared(idemlength,idemwidth,dem)
         do pixel=1,width

            cosalpha = ((height+rcurv)**2+(rcurv+zsch(pixel))**2-rho(pixel)**2)/2./(height+rcurv)/(rcurv+zsch(pixel))
            sch(1)=schsat(1)+squintshift(pixel)
            beta=squintshift(pixel)/rcurv
            sch(2)=ilrl*rcurv*acos(cosalpha/cos(beta))
            sch(3)=zsch(pixel)


            !c Convert to xyz for sat
            i_type = SCH_2_XYZ
            call convert_sch_to_xyz(ptm,sch,xyz,i_type)

            !c  lat lon of location
            i_type=XYZ_2_LLH
            call latlon(elp,xyz,llh,i_type)

            !!!Computations in enu coordinates around target
            call enubasis(llh(1), llh(2), enumat)
            xyz2enu = transpose(enumat)

            !!!Using sch array for delta
            sch = xyzsat - xyz
            enu = matmul(xyz2enu, sch)

            cosalpha = abs(enu(3))/ norm(enu)

            !!!LOS vectors
            losang(2*pixel-1) = acos(cosalpha)*r2d
            losang(2*pixel)= (atan2(enu(2),enu(1)) - 0.5*pi)*r2d

            !!!Local incidence angle
            demlat=(llh(1)*r2d-firstlat)/deltalat+1
            demlon=(llh(2)*r2d-firstlon)/deltalon+1
            if(demlat.lt.2)demlat=2
            if(demlat.gt.idemlength-1)demlat=idemlength-1
            if(demlon.lt.2)demlon=2
            if(demlon.gt.idemwidth-1)demlon=idemwidth-1

            idemlat=int(demlat)
            idemlon=int(demlon)
            fraclat=demlat-idemlat
            fraclon=demlon-idemlon

            !!!Using sch array and xyz temporarily 
            !!!Slopex
            sch(1) = intp_dem(dem,idemlon-1,idemlat,fraclon,fraclat,idemwidth,idemlength)
            sch(2) = intp_dem(dem,idemlon-1,idemlat,fraclon,fraclat,idemwidth,idemlength)
            sch(3) = (sch(2)-sch(1))*r2d/(2.0d0 * reast(elp,llh(1))*deltalon) 

            !!!Slopey
            xyz(1) = intp_dem(dem,idemlon,idemlat-1,fraclon,fraclat,idemwidth,idemlength)
            xyz(2)  = intp_dem(dem,idemlon,idemlat+1,fraclon,fraclat,idemwidth,idemlength)
            xyz(3) = (xyz(2)-xyz(1))*r2d/(2.0d0 * rnorth(elp,llh(1))*deltalat)

            enu = enu / norm(enu)
            cosalpha = (-enu(1)*sch(3) - enu(2)*xyz(3)+enu(3))/sqrt(1.0d0+sch(3)*sch(3)+xyz(3)*xyz(3))
            incang(pixel) = acos(cosalpha)*r2d            

         end do
         !$omp end parallel do


         !c Maybe add hmin and hmax?
         min_lat = min(minval(lat), min_lat)
         max_lat = max(maxval(lat), max_lat)
         min_lon = min(minval(lon), min_lon)
         max_lon = max(maxval(lon), max_lon)
!!         write(31,rec=line)(distance(j),j=1,width)
         call setLineSequential(latAccessor, lat)
         call setLineSequential(lonAccessor, lon)
         call setLineSequential(heightSchAccessor, zsch)
         call setLineSequential(heightRAccessor, z)
         if(losAccessor.gt.0) then
             call setLineSequential(losAccessor,losang)
         endif

         if(incAccessor.gt.0) then
             call setLineSequential(incAccessor,incang)
         endif
      end do

      call unprepareMethods(method)
!!      print *, 'Total convergence:', totalconv, ' out of ', width*length

!!       close(31)
       deallocate (converge)
       deallocate (dopline)
       deallocate (distance)
       deallocate (lat)
       deallocate (lon)
       deallocate (z)
       deallocate (zsch)
       deallocate (rho)
       deallocate (dem)
       deallocate(losang)
       deallocate(incang)
      end

