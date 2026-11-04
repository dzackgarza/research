"""Defect 2 (contraction/facet chain): independent verification of the data used.

Two blocks:
  A. the geometric data of the two tracked witnesses of the corpus
     (f_0 = member b_0, f_* = bitangent member b_star), re-computed from the
     polynomials printed in computations/reports/sm57_proof-m5.md sections 6;
  B. the lattice arithmetic of the contraction hypothesis: the class y sits in
     C_+^perp, has positive square, and pairs >= 1 with every effective (-2)-class
     not supported on C_+ (the last is a THEOREM, not a computation: see proof.md;
     here only the integrality bookkeeping is checked).

Run: python3 verify_defect2.py   (exact arithmetic, sympy, seconds)
"""
import sympy as sp

x, y = sp.symbols("x y")

# ---------------------------------------------------------------- block A
f0 = (5*x**4*y**4 - 2*x**4*y**2 + 3*x**4 + x**3*y**3 - 4*x**3*y + 2*x**2*y**4
      + x**2*y**2 + 2*x**2 - 3*x*y**3 + 7*x*y - y**4 - 5*y**2)
fstar = (8*x**4*y**4 + 7*x**4*y**2 + 6*x**4 + 5*x**3*y**3 + 4*x**3*y
         + 3*x**2*y**4 + 2*x**2*y**2 + 3*x**2 - 13*x*y**3 - 28*x*y
         - 10*y**4 + 13*y**2)


def node_report(f, name):
    P = sp.Poly(f, x, y)
    quad = sum(c*x**i*y**j for (i, j), c in zip(P.monoms(), P.coeffs()) if i + j == 2)
    Q = sp.Poly(quad, x, y)
    a, b, c = Q.coeff_monomial(x**2), Q.coeff_monomial(x*y), Q.coeff_monomial(y**2)
    print(f"[{name}] tau-invariant (only i+j even):", all((i + j) % 2 == 0 for i, j in P.monoms()))
    print(f"[{name}] f(0,0) =", f.subs({x: 0, y: 0}), " quadratic part =", sp.expand(quad),
          " discriminant =", b**2 - 4*a*c)


node_report(f0, "b0")
node_report(fstar, "b_star")

# member b_0: ruling discriminants
for f, name in ((f0, "b0"), (fstar, "b_star")):
    dx = sp.factor(sp.discriminant(sp.Poly(f, y).as_expr(), y))
    dy = sp.factor(sp.discriminant(sp.Poly(f, x).as_expr(), x))
    print(f"[{name}] disc_y(f) =", dx)
    print(f"[{name}] disc_x(f) =", dy)

# b_star: the bitangent ruling {x = 1}
print("[b_star] f(1,y) =", sp.factor(fstar.subs(x, 1)))
print("[b_star] f(0,y) =", sp.factor(fstar.subs(x, 0)))
# b_0: the node's ruling {x = 0}
print("[b0] f(0,y) =", sp.factor(f0.subs(x, 0)))

# ---------------------------------------------------------------- block B
# lattice of section 1.1: basis (e_b, f_b, alpha_b), Gram G; a split component
# C_+ over a ruling line of class h_1 has C_+.e_b = h_1.h_1 = 0, C_+.f_b = h_1.h_2 = 1,
# C_+.alpha_b = 0, C_+^2 = -2.  Check the resulting rank-4 lattice is integral, even,
# of signature (1,3), and that y = A + (A.C_+/2) C_+ for A = H - t alpha has the
# advertised pairings (no effective-root enumeration is claimed here).
G = sp.Matrix([[0, 2, 0], [2, 0, 0], [0, 0, -2]])          # e, f, alpha
print("[lattice] Gram of <e,f,alpha> =", G.tolist(), " det =", G.det(),
      " signature =", sp.Matrix(G).eigenvals())
ev = sp.Matrix([[0, 2, 0, 0],      # e
                [2, 0, 1, 0],      # f      (f.C_+ = 1)
                [0, 0, -2, 0],     # alpha
                [0, 0, 0, -2]])    # C_+    (row/col order e,f,alpha,C_+)
# careful: the (f,C_+) entry sits in row f, column C_+ -> rebuild properly
L = sp.zeros(4, 4)
idx = {"e": 0, "f": 1, "a": 2, "C": 3}
pairs = {("e", "e"): 0, ("e", "f"): 2, ("e", "a"): 0, ("e", "C"): 0,
         ("f", "f"): 0, ("f", "a"): 0, ("f", "C"): 1,
         ("a", "a"): -2, ("a", "C"): 0, ("C", "C"): -2}
for (i, j), v in pairs.items():
    L[idx[i], idx[j]] = v
    L[idx[j], idx[i]] = v
print("[lattice] Gram of <e,f,alpha,C_+> =", L.tolist(), " det =", L.det())
print("[lattice] all norms even (Grams of basis vectors):",
      all(L[i, i] % 2 == 0 for i in range(4)))
evs = [complex(sp.N(r)) for r in L.eigenvals()]
print("[lattice] signature (counting +):", sum(1 for z in evs if z.real > 1e-12 and abs(z.imag) < 1e-9),
      " (counting -):", sum(1 for z in evs if z.real < -1e-12 and abs(z.imag) < 1e-9))

# squarefreeness of the degree-22 cofactor of the ruling discriminant of b_0
d0 = sp.expand(sp.discriminant(sp.Poly(f0, y).as_expr(), y))
q0 = sp.simplify(d0/x**2)
q0 = sp.Poly(q0, x).as_expr()
print("[b0] q(x) =", sp.factor(q0), " deg =", sp.degree(q0, x),
      " squarefree:", sp.gcd(sp.Poly(q0, x), sp.Poly(sp.diff(q0, x), x)).as_expr() == 1)

vE = sp.Matrix([1, 0, 0, 0])
vF = sp.Matrix([0, 1, 0, 0])


def ip(u, v):
    return sp.nsimplify((u.T * L * v)[0])


vA = sp.Matrix([0, 0, 1, 0])
vC = sp.Matrix([0, 0, 0, 1])
H = vE + vF
print("[lattice] H^2 =", ip(H, H), " H.alpha =", ip(H, vA), " H.C_+ =", ip(H, vC),
      " e.C_+ =", ip(vE, vC), " f.C_+ =", ip(vF, vC), " alpha.C_+ =", ip(vA, vC))


def trace(name, M):
    print(f"[lattice] {name}: square =", sp.nsimplify(ip(M, M)), " pairing with C_+ =", sp.nsimplify(ip(M, vC)),
          " e:", sp.nsimplify(ip(M, vE)), " f:", sp.nsimplify(ip(M, vF)), " alpha:", sp.nsimplify(ip(M, vA)))


for t in (sp.Rational(1, 2), sp.Rational(3, 4)):
    A = H - t*vA
    trace(f"A = H - {t} alpha", A)
    yv = A + sp.Rational(1, 2)*ip(A, vC)*vC
    trace(f"y = A + (A.C_+/2) C_+", yv)
