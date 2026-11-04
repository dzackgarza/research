from sage.all import *
R = PolynomialRing(QQ, 'x0,x1,y0,y1'); x0,x1,y0,y1 = R.gens()
C = {(0,0):0,(0,2):0,(0,4):1,(1,1):1,(1,3):1,(2,0):1,(2,2):1,(3,1):1,(4,0):1,(4,4):1}
F = sum(QQ(C[(a,b)])*x0**a*x1**(4-a)*y0**b*y1**(4-b)
        for a in range(5) for b in range(5) if (a+b)%2==0 and (a,b) in C)
print("F =", F)
print("[1] tau-invariance F(-x0,x1,-y0,y1)==F :", F(x0=-x0,y0=-y0)==F)
print("[2] every monomial has x-degree 4 and y-degree 4 :",
      all(m.degree(x0)+m.degree(x1)==4 and m.degree(y0)+m.degree(y1)==4 for m in F.monomials()))
print("[3] F(p) for p=([0:1],[0:1]) :", F(x0=0,y0=0), "| F at the other three tau-fixed points :",
      [F(x1=0,y1=0), F(x1=0,y0=0), F(x0=0,y1=0)])
CHARTS = {'x1y1':(1,1),'x0y1':(0,1),'x1y0':(1,0),'x0y0':(0,0)}
print("[4] singular locus of B = {F=0} in the four affine charts (dim -1 <=> empty):")
for name,(i,j) in CHARTS.items():
    S = PolynomialRing(QQ,2,'u,v'); u,v = S.gens()
    xm = [u,S(1)] if i==1 else [S(1),u]; ym = [v,S(1)] if j==1 else [S(1),v]
    f = R.hom([xm[0],xm[1],ym[0],ym[1]],S)(F)
    I = S.ideal([f,f.derivative(u),f.derivative(v)])
    print("      %-5s GB=%-28s dim=%s" % (name, str(list(I.groebner_basis())), I.dimension()))
S = PolynomialRing(QQ,2,'x,y'); x,y = S.gens(); f = R.hom([x,S(1),y,S(1)],S)(F)
q2 = sum(c*x**mm[0]*y**mm[1] for mm,c in f.dict().items() if sum(mm)==2)
lin = sum(c*x**mm[0]*y**mm[1] for mm,c in f.dict().items() if sum(mm)==1)
print("[5] local equation at p :", f)
print("    linear part :", lin, "| quadratic part :", q2,
      "| discriminant of quadratic part :", f.coefficient({x:1,y:1})**2 - 4*f.coefficient({x:2,y:0})*f.coefficient({x:0,y:2}),
      "-> ordinary node")
print("[6] restriction to the tau-fixed ruling {x0=0} :", factor(F(x0=0)), "(a square of a quadratic: branch 4[y0=0])")
print("    restriction to the other tau-fixed ruling {y0=0} :", factor(F(y0=0)), "(not a square)")
# ---------- resolution of the A1 point: chart x = X*y, z = Z*y ----------
SR = PolynomialRing(QQ,3,'X,Z,Y'); X,Z,Y = SR.gens()
h = SR(f.subs({x:X*Y, y:Y}))
g = Z**2 - h.quo_rem(Y**2)[0]
print("[7] strict transform of X^sharp in the chart (x,z) = (X Y, Z Y) : 0 =", g)
I = SR.ideal([g, g.derivative(X), g.derivative(Z), g.derivative(Y)])
print("    singular locus of the strict transform (dim -1 = smooth) :", I.dimension(), list(I.groebner_basis()))
D  = SR.ideal([g, Y]);  C1 = SR.ideal([g, X, Z-Y]);  C2 = SR.ideal([g, X, Z+Y])
for nm,Ide in [("D = exceptional",D),("C1",C1),("C2",C2)]:
    print("    %-16s GB=%-24s dim=%s" % (nm, str(list(Ide.groebner_basis())), Ide.dimension()))
def meet(A,B): 
    J = SR.ideal(list(A.groebner_basis())+list(B.groebner_basis())); return list(J.groebner_basis())
print("    C1 cap C2 :", meet(C1,C2), " (equals (g,X,Z,Y): the two branches meet in one transverse point)")
print("    C1 cap D  :", meet(C1,D),  " (one transverse point)")
print("    C2 cap D  :", meet(C2,D),  " (one transverse point)")
print("[8] total transform of the ruling {x0=x=0}: (x) = (X)*(Y) = strict transform + exceptional, multiplicity 1")
print("    so the fibre of the elliptic fibration is F = C1 + C2 + D ; F^2 = -2-2-2+2(3) = 0, F.D = 1+1-2 = 0 = pi^*(O(1,0)).D")
print("    adjunction on the resolution (K=0): every component is a smooth rational curve, so every component has square -2")
