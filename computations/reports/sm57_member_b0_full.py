import sympy as sp
from itertools import product
x, y = sp.symbols('x y')
X0,X1,Y0,Y1 = sp.symbols('X0 X1 Y0 Y1')
mons = [(i,j) for i,j in product(range(5),range(5)) if (i+j)%2==0]
coef = {(4,4):5,(4,2):-2,(4,0):3,(3,3):1,(3,1):-4,(2,4):2,(2,2):1,(2,0):2,(1,3):-3,(1,1):7,(0,4):-1,(0,2):-5,(0,0):0}
f = sp.expand(sum(coef[m]*x**m[0]*y**m[1] for m in mons))
print("MEMBER b0:  f =", f)
print("node at p: f(p) =", f.subs({x:0,y:0}), "; quadratic part 2x^2+7xy-5y^2, disc =", 7**2-4*2*(-5))
# four charts
Fh = sp.expand(sum(coef[m]*X0**m[0]*X1**(4-m[0])*Y0**m[1]*Y1**(4-m[1]) for m in mons))
for name,sub,vs in [('X1=1,Y1=1',{X1:1,Y1:1},(X0,Y0)),('X1=1,Y0=1',{X1:1,Y0:1},(X0,Y1)),
                    ('X0=1,Y1=1',{X0:1,Y1:1},(X1,Y0)),('X0=1,Y0=1',{X0:1,Y0:1},(X1,Y1))]:
    Gc = sp.expand(Fh.subs(sub))
    eqs = [Gc]+[sp.expand(sp.diff(Gc,v)) for v in vs]
    print("chart", name, "GB:", sp.groebner(eqs,*vs,order='grevlex').exprs)
# ruling discriminants
Dy = sp.expand(sp.discriminant(sp.Poly(f,y), y)); Dx = sp.expand(sp.discriminant(sp.Poly(f,x), x))
for nm,D,v in (("disc_y(f)",Dy,x),("disc_x(f)",Dx,y)):
    fac = sp.factor_list(D)
    print(nm, "= ", fac[0], "*", [(sp.factor(b),e) for b,e in fac[1]], "  deg =", sp.degree(D,v))
    print("   squarefree part of", nm, "/%s^2 :" % v, sp.factor(sp.sqf_part(D)))
    print("   multiplicity of the forced root:", [e for b,e in fac[1] if b==v])
