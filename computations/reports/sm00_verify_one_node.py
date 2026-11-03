"""Independent verification for m8/d4 (positive half of A21).

(1) dim of the tau-invariant part of |O(4,4)| on P^1xP^1 is 13  => |V| = P^12, H_p = P^11.
(2) The explicit invariant branch curve of the report (sec-explicit-curve) has singular
    locus exactly the tau-fixed point p in the chart x0=y0=1, and is smooth in the other
    three charts (exact Groebner bases over Q).
(3) Its quadratic part at p is x^2+xy+2y^2, discriminant -7 != 0: an ordinary node.
(4) Blow-up chart check: the exceptional curve is the conic Z^2 = q(1,Y), smooth since
    disc q != 0 (supports Lemma 2.1's "D = P^1, D^2 = -2").
"""
import sympy as sp

x0, x1, y0, y1 = sp.symbols('x0 x1 y0 y1')
# coefficients of the affine chart x0=y0=1, from writing/coble/heegner-report/... sec-explicit-curve
coeffs = {(4,4):29,(4,2):23,(4,0):19,(3,3):17,(3,1):13,(2,4):11,(2,2):7,(2,0):1,(1,3):5,(1,1):1,(0,4):3,(0,2):2}
F = sp.expand(sum(c*x1**a*x0**(4-a)*y1**b*y0**(4-b) for (a,b),c in coeffs.items()))
print("dim of tau-invariant forms in H^0(O(4,4)) =", sum(1 for a in range(5) for b in range(5) if (a+b)%2==0))
print("=> |V| = P^12, H_p = {f(p)=0} = P^11")

x, y = sp.symbols('x y')
f = sp.expand(F.subs({x0:1,y0:1,x1:x,y1:y}))
print("term total degrees present:", sorted({sum(t[0]) for t in sp.Poly(f,x,y).terms()}), "(all even => tau-invariant)")
print("f(p) =", f.subs({x:0,y:0}))
q = sp.expand(sum(c*x**a*y**b for (a,b),c in coeffs.items() if a+b==2))
print("quadratic part at p:", q, "  disc b^2-4ac =", sp.expand(1**2 - 4*1*2), "  det Hess = 4ac-b^2 =", sp.expand(4*1*2-1**2))

for name, subs, v in [("x0=1,y0=1",{x0:1,y0:1},(x1,y1)),
                      ("x0=1,y1=1",{x0:1,y1:1},(x1,y0)),
                      ("x1=1,y0=1",{x1:1,y0:1},(x0,y1)),
                      ("x1=1,y1=1",{x1:1,y1:1},(x0,y0))]:
    g = sp.expand(F.subs(subs)); u, w = v
    G = sp.groebner([g, sp.diff(g,u), sp.diff(g,w)], u, w, order='lex')
    print(f"chart {name}: Groebner basis (g, g_u, g_v) =", list(G.exprs))

# blow-up chart: x=X, y=XY1, z=XZ1  =>  Z1^2 = q(1,Y1) + O(X); exceptional conic Z1^2 = q(1,Y1)
X, Y1, Z1 = sp.symbols('X Y1 Z1')
qsub = sp.expand(q.subs({x:1, y:Y1}))
print("exceptional conic: Z1^2 =", qsub, "; its discriminant in Y1 =", sp.expand(1**2 - 4*2), "(nonzero => smooth conic, D = P^1)")
