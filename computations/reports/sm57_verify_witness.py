import sympy as sp
from itertools import product

x,y = sp.symbols('x y')

# tau-invariant sections of O(4,4) on P1xP1 with tau=(x,y)->(-x,-y):
# monomials x^i y^j with i+j even, 0<=i,j<=4  (affine chart)
mons = [(i,j) for i,j in product(range(5),range(5)) if (i+j)%2==0]
coef = {}
for (i,j) in mons:
    coef[(i,j)] = sp.Symbol('a_%d_%d'%(i,j))
    if (i,j)==(0,0): coef[(i,j)] = sp.Integer(0)   # f(p)=0, p=(0,0)
f = sum(coef[m]*x**m[0]*y**m[1] for m in mons)

# impose: restriction to the ruling {x=1} equals (y-1)^2 (y-3)^2  (bitangency at y=1,y=3)
target = sp.expand((y-1)**2*(y-3)**2)
restr  = sp.expand(f.subs(x,1))
eqs = [sp.expand(restr-target).coeff(y,k) for k in range(5)]
sol = sp.solve(eqs, [coef[m] for m in mons if m!=(0,0)] , dict=True)
print("num solutions:", len(sol))
s = sol[0]
# choose free parameters generically but explicitly (small integers)
free = [v for v in s.values() if v.free_symbols]
fsyms = sorted({sym for v in free for sym in v.free_symbols}, key=str)
subs_free = {sym: sp.Integer(k+2) for k,sym in enumerate(fsyms)}
print("free params:", fsyms, "->", subs_free)
F = sp.expand(f.subs(s).subs(subs_free))
print("f =", F)
print("f(1,y) - target =", sp.expand(F.subs(x,1)-target))
print("f(0,0) =", F.subs({x:0,y:0}))
print("a11^2-4a20a02 =", sp.expand(F).coeff(x,1).coeff(y,1)**2
      - 4*sp.expand(F).coeff(x,2)*sp.expand(F).coeff(y,2))

# singular locus in the affine chart
fx, fy = sp.diff(F,x), sp.diff(F,y)
G = sp.groebner([sp.expand(F), sp.expand(fx), sp.expand(fy)], x, y, order='lex')
print("GB of <f,fx,fy> in Q[x,y]:", G.exprs)
# is the only solution (0,0)?
print("dim of ideal (should be 0):", G.is_zero_dimensional if hasattr(G,'is_zero_dimensional') else '-')

# check all four affine charts of P1xP1 for singular points.
# homogeneous bidegree (4,4): X0^i X1^(4-i) Y0^j Y1^(4-j)
X0,X1,Y0,Y1 = sp.symbols('X0 X1 Y0 Y1')
Fh = 0
for m in mons:
    i,j = m; c = sp.expand(F).coeff(x,i).coeff(y,j)
    Fh += c * X0**i * X1**(4-i) * Y0**j * Y1**(4-j)
Fh = sp.expand(Fh)
charts = {'x0=1':(X0,1),'x1=1':(X1,1),'y0=1':(Y0,1),'y1=1':(Y1,1)}
for name,(V,one) in charts.items():
    sub = {V:1}
    Gc = sp.groebner([sp.expand(sp.diff(Fh,v).subs(sub)) for v in (X0,X1,Y0,Y1)]
                     + [sp.expand(Fh.subs(sub))], order='grevlex')
    print("chart",name," GB:", Gc.exprs)

# clean node check at p: the quadratic part
Fc = sp.Poly(F, x, y)
a11 = Fc.coeff_monomial(x*y); a20 = Fc.coeff_monomial(x**2); a02 = Fc.coeff_monomial(y**2)
print("quadratic part at p:", a20, "x^2 +", a11, "xy +", a02, "y^2 ;  a11^2-4a20a02 =", a11**2-4*a20*a02)
