---
tag: 3HLC
kind: source
name: A2 x D4
id: union:223
sections:
  DET:
  - '1296'
  DIMENSION:
  - '8'
  DIVISORS:
  - 1 1 1 1 6 6 6 6
  GRAM:
  - 8 8
  - '    4   2   0   0  -2  -1   0   0'
  - '     2   4   2   2  -1  -2  -1  -1'
  - '     0   2   4   0   0  -1  -2   0'
  - '     0   2   0   4   0  -1   0  -2'
  - '    -2  -1   0   0   4   2   0   0'
  - '    -1  -2  -1  -1   2   4   2   2'
  - '     0  -1  -2   0   0   2   4   0'
  - '     0  -1   0  -2   0   2   0   4'
  GROUP_GENERATORS:
  - '3'
  - '8'
  - '    0   0   0   0   0  -1   1   1'
  - '     0   0   0   0   0   0   0   1'
  - '     0   0   0   0   1  -1   0   1'
  - '     0   0   0   0   0   1   0   0'
  - '     0   1  -1  -1   0   1  -1  -1'
  - '     0   0   0  -1   0   0   0  -1'
  - '    -1   1   0  -1  -1   1   0  -1'
  - '     0  -1   0   0   0  -1   0   0'
  - '8'
  - '    0   0   0   0  -1   1  -1  -1'
  - '     0   0   0   0  -1   0   0   0'
  - '     0   0   0   0   0  -1   1   0'
  - '     0   0   0   0   0  -1   0   1'
  - '    -1   1  -1  -1   0   0   0   0'
  - '    -1   0   0   0   0   0   0   0'
  - '     0  -1   1   0   0   0   0   0'
  - '     0  -1   0   1   0   0   0   0'
  - '8'
  - '   -1   1  -1  -1   0   0   0   0'
  - '    -1   0   0   0   0   0   0   0'
  - '     0  -1   1   0   0   0   0   0'
  - '     0  -1   0   1   0   0   0   0'
  - '     0   0   0   0  -1   1  -1  -1'
  - '     0   0   0   0  -1   0   0   0'
  - '     0   0   0   0   0  -1   1   0'
  - '     0   0   0   0   0  -1   0   1'
  GROUP_NAME:
  - S3 x W(F4) = W(A2) x W(F4)
  GROUP_ORDER:
  - '6912'
  KISSING_NUMBER:
  - '72'
  LAST_LINE: []
  MINIMAL_NORM:
  - '4'
  NAME:
  - A2 x D4
  PROPERTIES:
  - INTEGRAL=1
  - MODULAR=6
  REFERENCES:
  - Plesken & Pohst, Math. Comp. 31 (1977), 552-573.
  - 'Conway-Sloane, "Low-Dimensional Lattices II: Subgroups of GL(n,Z)",'
  - Proc. Royal Soc. London, A 419 (1988), 29-68.
  THETA_SERIES:
  - 'Theta series of A2 X D4 ( = G2 X F4):'
  - ''
  - Define th3 (theta_3) and eta as usual, or more precisely so that
  - ''
  - '> series(th3,q,10);'
  - '                       1 + 2*q + 2*q^4  + 2*q^9  + O(q^{16}  )'
  - ''
  - '> series(eta,q,10);'
  - '    q^(1/12)- q^(25/12)- q^(49/12) + O(q^(121/12))'
  - ''
  - Define eta^{(3)} as
  - ''
  - 'eta(q)eta(q^3),   and call it "e3":'
  - ''
  - '> series(e3,q,10);'
  - '      q^(1/3)- q^(7/3)- q^(13/3)- q^(19/3)+ q^(25/3)+ O(q^(13/3) )'
  - ''
  - ''
  - 'Define g1 and g2 as follows:'
  - ''
  - g1:=th3*subs(q=q^2,th3)*subs(q=q^3,th3)*subs(q=q^6,th3);
  - ''
  - '> series(g1,q,5);'
  - '                    1 + 2* q + 2*q^2  + 6*q^3  + 6*q^4  + O(q^5 )'
  - ''
  - t1:=subs(q=sqrt(q),e3);
  - t2:=subs(q=q^4,e3);
  - t3:=e3;
  - t4:=subs(q=q^2,e3);
  - g2:=series( (t1*t2/(t3*t4))^2,q, m1);
  - ''
  - '> series(g2,q,5);'
  - '                        q - 2*q^2  + q^3  - 4*q^4  + O(q^5 )'
  - ''
  - By Quebbemann JNT Oct 1995 or Rains-Sloane 1998,
  - 'we know that the theta series we want is of the form:'
  - t5:=series( g1^2*sum( c[i]*g2^i, i=0..4),q,40);
  - ''
  - 'Take these coefiicients:'
  - t6:=subs({c[0]=1,c[1]=-4,c[2]=0,c[3]=-16,c[4]=16},t5);
  - ''
  - 'and we get the desired answer :'
  - '> series(t6,q,10);'
  - '                    1 + 72*q^4  + 192*q^6  + 504*q^8  + O(q^{10}  )'
  - ''
  - 'or with more terms:'
  - 1+72*q^4+192*q^6+504*q^8+576*q^10+2280*q^12+1728*q^14+4248*q^16+4800*q^18+7920*q^20+6336*q^22+19416*q^24+10368*
  - q^26+21312*q^28+22464*q^30+33624*q^32+24192*q^34+63048*q^36+32832*q^38+65808*q^40+60864*q^42+83232*q^44+57600*q^46+
  - 155640*q^48+76032*q^50+137520*q^52+130944*q^54+180288*q^56+116928*q^58+290736*q^60+O(q^61),q,61)
  - ''
  - 'The Rains-Sloane reference is:'
  - E. M. Rains and N. J. A. Sloane,
  - The Shadow Theory of Modular and Unimodular Lattices,
  - J. Number Theory, 73 (1998), pp. 359-389;
  - http://neilsloane.com/doc/shad.pdf or shad.ps
  - ''
  - 'Here are the maple commands that NJAS uses::'
  - ' maxd:=101:'
  - kernelopts(printbytes=false);
  - '# get th2, th3, th4 = Jacobi theta constants out to degree maxd'
  - 'temp0:=trunc(evalf(sqrt(maxd)))+2:'
  - 'a:=0: for i from -temp0 to temp0 do a:=a+q^( (i+1/2)^2): od:'
  - th2:=series(a,q,maxd);
  - 'a:=0: for i from -temp0 to temp0 do a:=a+q^(i^2): od:'
  - th3:=series(a,q,maxd);
  - th4:=series(subs(q=-q,th3),q,maxd);
  - 'a:=q^(1/24) : for m from 1 to maxd do a:=a*(1-q^m); od:'
  - eta:=a;
  - ''
  - m1:=100;
  - g1:=th3*subs(q=q^2,th3)*subs(q=q^3,th3)*subs(q=q^6,th3);
  - g1:=series(g1,q,m1);
  - eta:=subs(q=q^2,eta);
  - e3:=eta*subs(q=q^3,eta);
  - e3:=series(e3,q,m1);
  - t1:=subs(q=sqrt(q),e3);
  - t2:=subs(q=q^4,e3);
  - t3:=e3;
  - t4:=subs(q=q^2,e3);
  - g2:=series( (t1*t2/(t3*t4))^2,q, m1);
  - i:='i';
  - t5:=series( g1^2*sum( c[i]*g2^i, i=0..4),q,m1);
  - t6:=subs({c[0]=1,c[1]=-4,c[2]=0,c[3]=-16,c[4]=16},t5);
source: nebe_sloane
---
