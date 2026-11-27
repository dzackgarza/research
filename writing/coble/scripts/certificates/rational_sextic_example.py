"""Exact arithmetic for the recovered ten-nodal sextic.

See ex:explicit-ten-nodal-sextic in rational-sextic-calculations.md for
the properness and degree arguments; the arithmetic alone is not the theorem.
Run with Sage Python.
"""
from sage.all import GF, QQ, ZZ, PolynomialRing, gcd, matrix
R = PolynomialRing(QQ, names=('s','t')); s,t=R.gens()
coeffs = [[1,1,2,3,2,1,1],[2,3,1,2,3,1,2],[3,2,3,1,2,3,1]]
param = [sum(c*s**(6-i)*t**i for i,c in enumerate(cs)) for cs in coeffs]
S = PolynomialRing(ZZ, names=('x','y','z')); x,y,z=S.gens()
F = 19783*x**6 -277523*x**5*y +1236290*x**4*y**2 -1155576*x**3*y**3 +608968*x**2*y**4 -195808*x*y**5 +26447*y**6 +205052*x**5*z -1702068*x**4*y*z +1686557*x**3*y**2*z -1099558*x**2*y**3*z +366024*x*y**4*z -45478*y**5*z +584140*x**4*z**2 -622975*x**3*y*z**2 +609573*x**2*y**2*z**2 -130204*x*y**3*z**2 +8334*y**4*z**2 +3528*x**3*z**3 -73520*x**2*y*z**3 -118908*x*y**2*z**3 +15408*y**3*z**3 -16747*x**2*z**4 +89450*x*y*z**4 +2144*y**2*z**4 -14520*x*z**5 -9276*y*z**5 +2732*z**6
assert F(*param)==0
print('exact polynomial substitution: zero',flush=True)
for prime in [101]:
  k=GF(prime); K=PolynomialRing(k,'u');u=K.gen()
  ps=[K(sum(c*u**(6-i) for i,c in enumerate(cs))) for cs in coeffs]
  if gcd(ps)!=1:continue
  assert any(cs[0]%prime for cs in coeffs)
  exponents=[(i,j,5-i-j) for i in range(6) for j in range(6-i)]
  cols=[(ps[0]**i*ps[1]**j*ps[2]**l).list() for i,j,l in exponents]
  A=matrix(k,31,21,lambda i,j: cols[j][i] if i<len(cols[j]) else 0)
  if A.rank()!=21:continue
  C=PolynomialRing(k,names=('a','b'));a,b=C.gens()
  bad=[]
  for chart in [(1,a,b),(a,1,b),(a,b,1)]:
    f=C(F(*chart)); D=f.derivative(a,2)*f.derivative(b,2)-f.derivative(a).derivative(b)**2
    G=C.ideal([f,f.derivative(a),f.derivative(b),D]).groebner_basis()
    bad.append(G==[1])
  print('prime',prime,'gcd',gcd(ps),'rank',A.rank(),'bad-locus unit ideals',bad,flush=True)
  if all(bad):break
else: raise AssertionError('no chosen prime gives certificate')
assert all(bad)
