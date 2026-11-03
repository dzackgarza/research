"""Independent numerical cross-check of the elimination in verify_members.py.

For a quartic q in y the test "q = (a y^2 + b y + d)^2 for some a,b,d" is decided by
a^2 = c4, d^2 = c0, 2ab = c3, 2bd = c1, b^2 + 2ad = c2; eliminating a,b,d gives the
residual max(|c2 - (b^2+2ad)|, |c1 - 2bd|)/max(1,|c_i|) for the two sign choices of a
and d.  A square has residual 0.  (The elimination test in verify_members.py is exact;
this is a check of it at the 22 roots of the squarefree factor, at 60 digits.)

Result: f0 -- minimum residual 7.5e-01 over all 22 singular x: no square fibre.
        f* -- residual 0.00 at x = 1 (and near-0 structure at x = -1), as it must be
              for the bitangent member, whose f*(1,y) and f*(-1,y) are exact squares.
"""
import sympy as sp, mpmath as mp
from fractions import Fraction
x,y=sp.symbols('x y')
f0 = 5*x**4*y**4 - 2*x**4*y**2 + 3*x**4 + x**3*y**3 - 4*x**3*y + 2*x**2*y**4 + x**2*y**2 + 2*x**2 - 3*x*y**3 + 7*x*y - y**4 - 5*y**2
fs = 8*x**4*y**4 + 7*x**4*y**2 + 6*x**4 + 5*x**3*y**3 + 4*x**3*y + 3*x**2*y**4 + 2*x**2*y**2 + 3*x**2 - 13*x*y**3 - 28*x*y - 10*y**4 + 13*y**2
mp.mp.dps=60
def to_mp(cs):  # list of sympy rationals (ascending in x) -> mpmath coeffs
    out=[]
    for c in cs:
        fr=Fraction(int(sp.numer(c)),int(sp.denom(c)))
        out.append(mp.mpf(fr.numerator)/mp.mpf(fr.denominator))
    return out
def coeffpolys(f):
    P=sp.Poly(sp.expand(f),y)
    return [P.coeff_monomial(y**k) for k in range(5)]
def horner(cl,x0):
    acc=mp.mpc(0)
    for c in reversed(cl): acc=acc*x0+c
    return acc
def square_residual(c):
    c0,c1,c2,c3,c4=c; best=None
    for sa in (1,-1):
        a=sa*mp.sqrt(c4)
        for sd in (1,-1):
            d=sd*mp.sqrt(c0); b=c3/(2*a)
            r=max(abs(c2-(b*b+2*a*d)),abs(c1-2*b*d))/max(1,abs(c0),abs(c1),abs(c2),abs(c3),abs(c4))
            best=r if best is None else min(best,r)
    return best
for nm,f in (("f0",f0),("fs",fs)):
    cs=coeffpolys(f); cl=[to_mp([sp.Poly(c,x).coeff_monomial(x**k) for k in range(sp.degree(sp.Poly(c,x),x)+1)]) for c in cs]
    Dy=sp.expand(sp.discriminant(sp.Poly(f,y),y)); qP=sp.Poly(sp.cancel(Dy/x**2),x)
    qc=to_mp([qP.coeff_monomial(x**k) for k in range(qP.degree()+1)])
    rts=mp.polyroots(qc,maxsteps=500,extraprec=800)
    print(f"{nm}: {len(rts)} roots of the squarefree degree-22 factor of disc_{y}/x^2")
    res=sorted(square_residual([horner(cl[k],x0) for k in range(5)]) for x0 in rts)
    print("    square residual: min %.2e   median %.2e   max %.2e" % (res[0], res[len(res)//2], res[-1]))
print("controls:")
for nm,f,x0 in (("fs",fs,1),("fs",fs,-1),("f0",f0,1),("f0",f0,0),("fs",fs,0)):
    cs=coeffpolys(f); cl=[to_mp([sp.Poly(c,x).coeff_monomial(x**k) for k in range(sp.degree(sp.Poly(c,x),x)+1)]) for c in cs]
    print("    %s at x=%s: residual %.2e" % (nm, x0, float(square_residual([horner(cl[k],mp.mpc(x0)) for k in range(5)]))))
