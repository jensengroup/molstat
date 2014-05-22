C THE LENNARD-JONES POTENTIAL, GRADIENT AND THE VIRIAL
      subroutine LennardJones(U,box,Epot,F,Vir,N)
cf2py intent(in) U
cf2py intent(in) box
cf2py intent(out) Epot
cf2py intent(out) F
cf2py intent(out) Vir
      implicit none
      double precision U,Epot,F,box,Vir
      integer N
      dimension U(3,N),F(3,N),box(3)
C
      double precision zero,one,X,Y,Z,r2,r2i,r6i,feight,half,
     * ftmp,four,rc2,rc2i,rc6i,ecut
      integer i,j
C
      parameter(zero=0.0D+00,one=1.0D+00,feight=48.0D+00,
     * half=0.5D+00,four=4.0D+00,rc2=(6.25D+00),
     * rc2i=one/rc2,rc6i=rc2i*rc2i*rc2i,ecut=rc6i*(rc6i-one))
      Epot = zero
      Vir = zero
      do i=1,N
        F(1,i) = zero
        F(2,i) = zero
        F(3,i) = zero
      enddo
      do i=1,N-1
        do j=i+1,N
          X  = U(1,j) - U(1,i)
          Y  = U(2,j) - U(2,i)
          Z  = U(3,j) - U(3,i)
          X  = X - box(1)*nint(X/box(1))
          Y  = Y - box(2)*nint(Y/box(2))
          Z  = Z - box(3)*nint(Z/box(3))
          r2 = X*X + Y*Y + Z*Z
          if(r2.lt.rc2) then
            r2i = one / r2
            r6i = r2i*r2i*r2i
            Epot = Epot + r6i*(r6i-one) - ecut
            ftmp = feight*r6i*(r6i-half)
            F(1,i) = F(1,i) - ftmp*X*r2i
            F(2,i) = F(2,i) - ftmp*Y*r2i
            F(3,i) = F(3,i) - ftmp*Z*r2i
            F(1,j) = F(1,j) + ftmp*X*r2i
            F(2,j) = F(2,j) + ftmp*Y*r2i
            F(3,j) = F(3,j) + ftmp*Z*r2i
            Vir = Vir + ftmp
          endif
        enddo
      enddo
      Epot = Epot * four
      return
      end
