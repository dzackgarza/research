import sympy as sp
x,y = sp.symbols('x y')
MONS = [(i,j) for i in range(5) for j in range(5) if (i+j)%2==0]
def poly(a): return sum(sp.Rational(a[m])*x**m[0]*y**m[1] for m in MONS)
aA = {m:0 for m in MONS}
aA.update({(4,4):29,(4,2):23,(4,0):19,(3,3):17,(3,1):13,(2,4):11,(2,2):7,(2,0):1,(1,3):5,(1,1):1,(0,4):3,(0,2):2})
aB = {(0,0):0,(0,2):-6,(0,4):8,(1,1):-1,(1,3):4,(2,0):-2,(2,2):1,(2,4):-3,(3,1):1,(3,3):-4,(4,0):3,(4,2):3,(4,4):-4}
for nm,a in (("A",aA),("B",aB)):
    f = poly(a)
    D = sp.Poly(sp.expand(sp.discriminant(f,y)),x)
    print("member",nm,": disc degree",D.degree())
    L = sp.Poly(sp.cancel(D.as_expr()/x**2),x)
    print("   disc / x^2 =",sp.factor(L.as_expr()), "  degree:",L.degree())
    print("   squarefree?", sp.degree(sp.gcd(L.as_expr(),sp.diff(L.as_expr(),x)),x))
    print("   disc value at x=1:", sp.expand(sp.discriminant(f,y)).subs(x,1))
    print("   f(1,y) discriminant:", sp.discriminant(sp.expand(f.subs(x,1)),y))
    print("   number of distinct roots of f(1,y):", len(sp.roots(sp.Poly(sp.expand(f.subs(x,1)),y))))
    # H-degree bookkeeping: check that all N-classes pair evenly with H (by construction) and record the fibre classes
print()
print("Sanity: H.L1=2, H.L2=2, H.D=0 by definition of N; so H.x is even for x in N.")
