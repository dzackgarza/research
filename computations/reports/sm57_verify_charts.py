import sympy as sp
from itertools import product
x,y = sp.symbols('x y')
mons = [(i,j) for i,j in product(range(5),range(5)) if (i+j)%2==0]
F = 8*x**4*y**4 + 7*x**4*y**2 + 6*x**4 + 5*x**3*y**3 + 4*x**3*y + 3*x**2*y**4 + 2*x**2*y**2 + 3*x**2 - 13*x*y**3 - 28*x*y - 10*y**4 + 13*y**2
X0,X1,Y0,Y1 = sp.symbols('X0 X1 Y0 Y1')
Fh = 0
for (i,j) in mons:
    c = sp.expand(F).coeff(x,i).coeff(y,j)
    Fh += c*X0**i*X1**(4-i)*Y0**j*Y1**(4-j)
Fh = sp.expand(Fh)
# four charts: choose one coordinate =1 in each factor; remaining two are the local coords
charts = [('X1=1,Y1=1',{X1:1,Y1:1},(X0,Y0)),
          ('X1=1,Y0=1',{X1:1,Y0:1},(X0,Y1)),
          ('X0=1,Y1=1',{X0:1,Y1:1},(X1,Y0)),
          ('X0=1,Y0=1',{X0:1,Y0:1},(X1,Y1))]
for name,sub,vs in charts:
    G = sp.expand(Fh.subs(sub))
    eqs = [G] + [sp.expand(sp.diff(G,v)) for v in vs]
    Gd = sp.groebner(eqs, *vs, order='grevlex')
    print(name, " coords",vs, " GB:", Gd.exprs)
