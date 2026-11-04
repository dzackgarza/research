"""Verification of the two one-node members used to refute A21's chamber clause.

Member b0:  f0 ;  Member b*:  fs  (the bitangent member), both in the 13-monomial
tau-invariant system of deg = (4,4) on Y = P1 x P1, node at p = (0,0).

Everything printed here is an exact rational/algebraic computation (sympy over Q,
Groebner over Q, elimination over Q: an elimination ideal = <1> means no zero over
any extension field, i.e. over the algebraic closure).

Claims checked:
 (1) both are tau-invariant members of the invariant system, node at p (nondegenerate
     quadratic part), smooth away from p in all four charts;
 (2) b0: the ruling discriminants are (ruling coordinate)^2 * squarefree of degree 22,
     and the ruling fibres are NEVER squares -- in either ruling family, in the affine
     chart or at infinity.  Hence b0 has no reducible ruling fibre away from p's two
     rulings, hence nu(b0) = 0 (Lemma B of proof.md);
 (3) b*: f(1,y) = (y-1)^2 (y-3)^2 and f(-1,y) = (y+1)^2(y+3)^2, so the rulings x = 1
     and x = -1 split, giving C_+, C_- with the stated intersection numbers; nu(b*) >= 2.
"""
import sympy as sp

x, y = sp.symbols('x y')
X0, X1, Y0, Y1 = sp.symbols('X0 X1 Y0 Y1')

f0 = (5*x**4*y**4 - 2*x**4*y**2 + 3*x**4 + x**3*y**3 - 4*x**3*y + 2*x**2*y**4
      + x**2*y**2 + 2*x**2 - 3*x*y**3 + 7*x*y - y**4 - 5*y**2)
fs = (8*x**4*y**4 + 7*x**4*y**2 + 6*x**4 + 5*x**3*y**3 + 4*x**3*y + 3*x**2*y**4
      + 2*x**2*y**2 + 3*x**2 - 13*x*y**3 - 28*x*y - 10*y**4 + 13*y**2)


def coeffs(f):
    f = sp.expand(f)
    return {(i, j): f.coeff(x, i).coeff(y, j) for i in range(5) for j in range(5)}


print("=" * 78)
print("(1) membership in the invariant system, node, smoothness away from p")
print("=" * 78)
for nm, f in (("b0", f0), ("b*", fs)):
    c = coeffs(f)
    supp = [m for m, v in c.items() if v != 0]
    print(f"{nm}: #nonzero monomials = {len(supp)}; all with i+j even: "
          f"{all((i + j) % 2 == 0 for i, j in supp)}; all 0<=i,j<=4: {all(i <= 4 and j <= 4 for i, j in supp)}")
    p = {x: 0, y: 0}
    a = sp.diff(f, x, 2).subs(p) / 2
    b = sp.diff(f, x, 1, y, 1).subs(p)
    d = sp.diff(f, y, 2).subs(p) / 2
    print(f"{nm}: f(p) = {f.subs(p)};  quadratic part = {a}x^2 + {b}xy + {d}y^2;  "
          f"disc = {b**2 - 4*a*d} (nonzero = {b**2 - 4*a*d != 0}: ordinary node)")
    Fh = sp.expand(sum(c[m] * X0**m[0] * X1**(4 - m[0]) * Y0**m[1] * Y1**(4 - m[1])
                       for m in c))
    for name, sub, vs in [('X1=1,Y1=1', {X1: 1, Y1: 1}, (X0, Y0)),
                          ('X1=1,Y0=1', {X1: 1, Y0: 1}, (X0, Y1)),
                          ('X0=1,Y1=1', {X0: 1, Y1: 1}, (X1, Y0)),
                          ('X0=1,Y0=1', {X0: 1, Y0: 1}, (X1, Y1))]:
        G = sp.expand(Fh.subs(sub))
        eqs = [G] + [sp.expand(sp.diff(G, v)) for v in vs]
        gb = sp.groebner(eqs, *vs, order='grevlex').exprs
        print(f"    chart {name}: Groebner basis of (F, dF) = {gb}")

print()
print("=" * 78)
print("(2a) b0: ruling discriminants")
print("=" * 78)
for nm, f in (("b0", f0), ("b*", fs)):
    for var, other in ((x, y), (y, x)):
        D = sp.expand(sp.discriminant(sp.Poly(f, other), other))
        fac = sp.factor_list(D)
        print(f"{nm}: disc_{other} = {fac[0]} * {[(sp.factor(b), e) for b, e in fac[1]]}")
        q = sp.Poly(sp.cancel(D / var**2), var)
        print(f"      degree = {sp.degree(D, var)};  (disc/{var}^2) squarefree: "
              f"{sp.degree(sp.gcd(q, q.diff(var)), var) == 0}, degree {q.degree()}")

print()
print("=" * 78)
print("(2b) b0: no ruling fibre is a square  (elimination over Q; <1> = none at all)")
print("=" * 78)


def squaretest(f, var, par, label):
    # f = (s2 var^2 + s1 var + s0)^2 identically in var, for some value of par
    n = sp.Poly(f, var).degree()
    k = n // 2
    S = sp.symbols(f's0:{k + 1}')
    root = sum(S[i] * var**i for i in range(k + 1))
    eqs = sp.Poly(sp.expand(f - root**2), var).all_coeffs()
    G = sp.groebner(eqs, *S, par, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {par}]
    print(f"  {label}: deg_{var} = {n};  elimination ideal in {par}: {elim}")
    return elim


for nm, f in (("b0", f0), ("b*", fs)):
    squaretest(f, y, x, f"{nm}: x-fibration fibres f({x},y) squares in y?")
    squaretest(f, x, y, f"{nm}: y-fibration fibres f(x,{y}) squares in x?")

print()
print("  infinity charts: fibre over x = inf is zeta^2 = (coefficient of x^4);")
print("  fibre over y = inf is zeta^2 = (coefficient of y^4); a quartic with nonzero")
print("  discriminant is not a square and is a smooth (hence irreducible) fibre.")
for nm, f in (("b0", f0), ("b*", fs)):
    cx4 = sp.expand(f).coeff(x, 4)
    cy4 = sp.expand(f).coeff(y, 4)
    print(f"  {nm}: coeff x^4 = {sp.factor(cx4)},  disc_y = "
          f"{sp.discriminant(sp.Poly(cx4, y), y)}")
    print(f"  {nm}: coeff y^4 = {sp.factor(cy4)},  disc_x = "
          f"{sp.discriminant(sp.Poly(cy4, x), x)}")
print("  b0 node rulings: f0(0,y) =", sp.factor(f0.subs(x, 0)), ";  f0(x,0) =",
      sp.factor(f0.subs(y, 0)), " (not squares)")
print("  b* node rulings: f*(0,y) =", sp.factor(fs.subs(x, 0)), ";  f*(x,0) =",
      sp.factor(fs.subs(y, 0)), " (not squares)")

print()
print("=" * 78)
print("(3) b*: the bitangent ruling at x = 1 (and its tau-image at x = -1)")
print("=" * 78)
print("  f*(1,y) =", sp.factor(fs.subs(x, 1)))
print("  f*(-1,y) =", sp.factor(fs.subs(x, -1)))
G = sp.Matrix([[4, 0, 1], [0, -2, 0], [1, 0, -2]])   # Gram(H, alpha, C_+)
print("  Gram(H, alpha, C_+) =", G, " ; det =", G.det(),
      " ; 2x2 block [[4,1],[1,-2]] det =", sp.Matrix([[4, 1], [1, -2]]).det())
print("  C_+ + C_- = pi^*{x=1}, so 0 = (C_+ + C_-)^2 = 2 C_+^2 + 2 C_+ . C_-  gives"
      " C_+^2 = C_-^2 = -2 and C_+ . C_- = 2; and C_+ . H = 1.")
print("  (the facet class y is computed in section (4) below)")

print()
print("=" * 78)
print("(4) b*: the facet class y and its pairings, in the lattice basis (alpha, C+, e_b, f_b)")
print("=" * 78)
G = sp.Matrix([[-2, 0, 0, 0],      # alpha
               [0, -2, 0, 1],      # C+  (C+.f_b = 1)
               [0, 0, 0, 2],       # e_b (e_b.f_b = 2)
               [0, 1, 2, 0]])      # f_b
alpha, Cp, eb, fb = (sp.Matrix(v) for v in ([1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]))
H = eb + fb                        # H = e_b + f_b, H^2 = 4
dot = lambda u, v: (u.T * G * v)[0]
L = 2*H - alpha                    # L = 2H - alpha
y = L + Cp + eb                    # y = 2H - alpha + C+ + e_b
print("  H^2 =", dot(H,H), " H.alpha =", dot(H,alpha), " alpha.C+ =", dot(alpha,Cp),
      " C+.e_b =", dot(Cp,eb), " C+.f_b =", dot(Cp,fb), " C+^2 =", dot(Cp,Cp))
print("  L = 2H - alpha :  L^2 =", dot(L,L), " L.H =", dot(L,H), " L.alpha =", dot(L,alpha),
      " L.e_b =", dot(L,eb), " L.f_b =", dot(L,fb), " L.C+ =", dot(L,Cp))
print("  y = L + C+ + e_b :  y^2 =", dot(y,y), " y.H =", dot(y,H), " y.C+ =", dot(y,Cp),
      " y.alpha =", dot(y,alpha), " y.e_b =", dot(y,eb))
print("  C+^perp contains y (y.C+ = 0) and e_b (C+.e_b =", dot(Cp,eb), ")")
print("  rho = arcsinh(1/sqrt(2*y^2)) =", sp.N(sp.asinh(1/sp.sqrt(2*dot(y,y)))),
      "   (sinh rho = 1/sqrt(48) =", sp.N(1/sp.sqrt(48)), ")")
