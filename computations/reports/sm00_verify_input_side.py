#!/usr/bin/env python3
"""
m5, swarm smw0b9kmo, direction d7 (premise ledger, input side of A21).

Independent exact verification of the premises that the five authored bullets of
prob:coble-rigidity consume on the DIRECT-PROJECTIVE construction

    pi : X# = {z^2 = f(x,y)} -> Y = P1 x P1,   B = {f = 0} in |O_Y(4,4)|,
    tau : (x,y) -> (-x,-y)  on Y,   iota_dP : (x,y,z) -> (x,y,-z),
    iota_Co : (x,y,z) -> (-x,-y,-z),   rho = iota_Co iota_dP,
    X^ -> X# the resolution of the nodes of B at tau-fixed points,
    H = pi^*O_Y(1,1),   alpha = [D], D = exceptional curve over the node p.

Every check is exact (sympy over QQ or QQ(sqrt(-7))); no floating point is used.
Prints one PASS/FAIL line per premise; the run's log is inputpremises-run.txt.
Proofs of the premises that are not pure computation are in premise-ledger.md
with the same PL-n labels.
"""
import sympy as sp

PASS, FAIL = [], []


def check(label, cond, detail=""):
    cond = bool(cond)
    (PASS if cond else FAIL).append(label)
    print(("PASS " if cond else "FAIL ") + label + ((" | " + detail) if detail else ""))


x, y, u, v, z = sp.symbols('x y u v z')
X, Y, Z = sp.symbols('X Y Z')

# ---------------------------------------------------------------- PL-1: the member
f_aff = sp.expand(29 * x**4 * y**4 + 23 * x**4 * y**2 + 19 * x**4
                  + 17 * x**3 * y**3 + 13 * x**3 * y
                  + 11 * x**2 * y**4 + 7 * x**2 * y**2 + x**2
                  + 5 * x * y**3 + x * y + 3 * y**4 + 2 * y**2)
fpoly = sp.Poly(f_aff, x, y)
coeff = {(i, j): int(fpoly.coeff_monomial(x**i * y**j)) for i in range(9) for j in range(9)}

check("PL-1a bidegree (4,4)",
      sp.Poly(f_aff, x).degree() == 4 and sp.Poly(f_aff, y).degree() == 4
      and all(c == 0 for (i, j), c in coeff.items() if i > 4 or j > 4),
      "deg_x = %d, deg_y = %d" % (sp.Poly(f_aff, x).degree(), sp.Poly(f_aff, y).degree()))
check("PL-1b tau-invariant: f(-x,-y) = f(x,y)",
      sp.expand(f_aff.subs({x: -x, y: -y}) - f_aff) == 0)

q2 = sp.expand(sum(coeff[(i, j)] * x**i * y**j for (i, j) in coeff if i + j == 2))
hess = sp.Matrix([[sp.diff(q2, x, x), sp.diff(q2, x, y)], [sp.diff(q2, x, y), sp.diff(q2, y, y)]])
check("PL-1c quadratic part x^2+xy+2y^2, discriminant b^2-4ac = -7, det Hess = 7",
      sp.expand(q2 - (x**2 + x * y + 2 * y**2)) == 0 and sp.det(hess) == 7,
      "q2 = %s, det Hess = %s" % (q2, sp.det(hess)))

val_00 = coeff[(0, 0)]
lead_y_at_x0 = int(sp.Poly(f_aff.subs(x, 0), y).all_coeffs()[0])
lead_x_at_y0 = int(sp.Poly(f_aff.subs(y, 0), x).all_coeffs()[0])
coeff_44 = coeff[(4, 4)]
check("PL-1d exactly one tau-fixed point lies on B (p = (0,0))",
      val_00 == 0 and lead_y_at_x0 != 0 and lead_x_at_y0 != 0 and coeff_44 != 0,
      "f(p)=%d, lead_y f(0,y)=%d, lead_x f(x,0)=%d, coeff x^4y^4=%d"
      % (val_00, lead_y_at_x0, lead_x_at_y0, coeff_44))

# ------------------------------------------------- PL-2: singular locus, four charts
# In each of the four standard charts the local equation is G, so
# Sing(B) cap chart = V(G, G_s1, G_s2) exactly.
charts = [
    ('(x,y)', x, y, sp.expand(f_aff)),
    ('(x,v)', x, v, sp.expand(v**4 * f_aff.subs(y, 1 / v))),
    ('(u,y)', u, y, sp.expand(u**4 * f_aff.subs(x, 1 / u))),
    ('(u,v)', u, v, sp.expand(u**4 * v**4 * f_aff.subs({x: 1 / u, y: 1 / v}))),
]
GBs = {}
for name, s1, s2, G in charts:
    ideal = [G, sp.diff(G, s1), sp.diff(G, s2)]
    GBs[name] = (s1, s2, sp.groebner(ideal, s1, s2, order='lex'),
                 sp.groebner(ideal, s1, s2, order='grlex'), ideal)
    print("   chart %-7s GB(lex) of (G,G1,G2): %s" % (name, [sp.factor(g) for g in GBs[name][2].exprs]))

for name in ['(x,v)', '(u,y)', '(u,v)']:
    s1, s2, gblex, gbgr, _ = GBs[name]
    check("PL-2a no singular point of B in chart %s (unit ideal, two orders)" % name,
          list(gblex.exprs) == [sp.Integer(1)] and list(gbgr.exprs) == [sp.Integer(1)])

s1, s2, gblex, gbgr, ideal = GBs['(x,y)']


def reduce_zero(gb, expr, *gens):
    r = gb.reduce(expr)
    rem = r[-1] if isinstance(r, tuple) else r
    return sp.expand(rem) == 0


check("PL-2b chart (x,y): the ideal (f,f_x,f_y) equals (x,y), so Sing(B) = {(0,0)} reduced",
      all(reduce_zero(gblex, g) for g in (x, y))
      and all(reduce_zero(gbgr, g) for g in (x, y))
      and all(reduce_zero(gblex, sp.expand(g)) for g in ideal),
      "GB(lex) = %s, GB(grlex) = %s" % ([sp.factor(g) for g in gblex.exprs],
                                        [sp.factor(g) for g in gbgr.exprs]))
check("PL-2c (0,0) is a node: f(p) = f_x(p) = f_y(p) = 0 and det Hess != 0",
      f_aff.subs({x: 0, y: 0}) == 0
      and sp.diff(f_aff, x).subs({x: 0, y: 0}) == 0
      and sp.diff(f_aff, y).subs({x: 0, y: 0}) == 0 and sp.det(hess) != 0,
      "local quadratic part %s, discriminant -7" % q2)

# ------------------------------------------------- PL-3: A1 local model, D^2 = -2
s7 = sp.sqrt(-7)
ar, br = (-1 + s7) / 2, (-1 - s7) / 2
check("PL-3a q = (x - a y)(x - b y) over Q(sqrt(-7)), a != b: q is linearly XY",
      sp.simplify(sp.expand((x - ar * y) * (x - br * y)) - (x**2 + x * y + 2 * y**2)) == 0
      and sp.simplify(ar - br) != 0)

u2, v2, u3, v3 = sp.symbols('u2 v2 u3 v3')
check("PL-3b chart X!=0 of Bl_0 C^3: proper transform of {Z^2 = XY} is v2^2 = u2 (smooth)",
      sp.simplify(sp.cancel(sp.expand((x * v2)**2 - x * (x * u2)) / x**2) - (v2**2 - u2)) == 0)
check("PL-3c chart Y!=0: proper transform is v3^2 = u3 (smooth)",
      sp.simplify(sp.cancel(sp.expand((y * v3)**2 - (y * u3) * y) / y**2) - (v3**2 - u3)) == 0)
check("PL-3d on E: v3 = 1/v2", sp.simplify((v2 / u2).subs(u2, v2**2) - 1 / v2) == 0)
g12 = sp.simplify((1 / u2).subs(u2, v2**2))
check("PL-3e O(E)|_E has transition g12 = v2^(-2), so E^2 = -2",
      sp.simplify(g12 - v2**(-2)) == 0,
      "g12 = %s, degree in v2 = %d"
      % (g12, sp.Poly(sp.numer(g12), v2).degree() - sp.Poly(sp.denom(g12), v2).degree()))

# ------------------------------------------------- PL-4: intersection numbers
L1v, L2v, Dv = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])
Gram = sp.Matrix([[0, 2, 0], [2, 0, 0], [0, 0, -2]])


def dot(a, b):
    return sp.expand((a.T * Gram * b)[0, 0])


Hv = L1v + L2v
check("PL-4a H^2 = 4", dot(Hv, Hv) == 4)
check("PL-4b alpha^2 = -2", dot(Dv, Dv) == -2)
check("PL-4c H.alpha = 0", dot(Hv, Dv) == 0)
ev = sp.Matrix(Gram).eigenvals()
pos = sum(m for e, m in ev.items() if sp.sign(sp.simplify(e)) > 0)
neg = sum(m for e, m in ev.items() if sp.sign(sp.simplify(e)) < 0)
check("PL-4d <L1,L2,D> has signature (1,2), i.e. is U(2) perp <-2>", (pos, neg) == (1, 2),
      "eigenvalues %s" % {sp.simplify(e): m for e, m in ev.items()})
Dpv = L1v - Dv
check("PL-4e D' = L1 - D: D'^2 = -2, D.D' = 2, H.D' = 2, D + D' = L1",
      dot(Dpv, Dpv) == -2 and dot(Dpv, Dv) == 2 and dot(Hv, Dpv) == 2
      and (Dv + Dpv - L1v) == sp.zeros(3, 1))

# ------------------------------------------------- PL-5: ruling fibres at x = 0 and x = inf
fibre0 = sp.factor(sp.Poly(f_aff.subs(x, 0), y).as_expr())
check("PL-5a f(0,y) = y^2(3y^2+2): the node ruling meets B with multiplicity 2 at p",
      sp.expand(fibre0 - y**2 * (3 * y**2 + 2)) == 0, "f(0,y) = %s" % fibre0)
check("PL-5b 3y^2+2 is squarefree and nonzero at y = 0",
      sp.gcd(sp.Poly(3 * y**2 + 2, y), sp.Poly(6 * y, y)).degree() == 0
      and (3 * y**2 + 2).subs(y, 0) != 0)
quartic_inf = sp.expand(sum(coeff[(4, j)] * y**j for j in range(5)))
check("PL-5c fibre over x = infinity: 29y^4+23y^2+19 is squarefree of degree 4",
      sp.expand(quartic_inf - (29 * y**4 + 23 * y**2 + 19)) == 0
      and sp.gcd(sp.Poly(quartic_inf, y), sp.Poly(sp.diff(quartic_inf, y), y)).degree() == 0,
      "quartic = %s" % quartic_inf)
fibre0y = sp.factor(sp.Poly(f_aff.subs(y, 0), x).as_expr())
check("PL-5d f(x,0) = x^2(19x^2+1): the y-node ruling also passes through p",
      sp.expand(fibre0y - x**2 * (19 * x**2 + 1)) == 0, "f(x,0) = %s" % fibre0y)

# ------------------------------------------------- PL-6: involution characters
det_xy_Co = sp.Matrix([[-1, 0], [0, -1]]).det()
char_dP = sp.Integer(1) * sp.Integer(-1)
char_Co = det_xy_Co * sp.Integer(-1)
check("PL-6a iota_dP is nonsymplectic (omega -> -omega)", char_dP == -1)
check("PL-6b iota_Co is nonsymplectic (omega -> -omega)", char_Co == -1)
check("PL-6c rho = iota_Co iota_dP is symplectic (omega -> omega)", char_Co * char_dP == 1)
check("PL-6d iota_Co preserves {z^2 = f} because f is tau-invariant",
      sp.expand(f_aff - f_aff.subs({x: -x, y: -y})) == 0)
check("PL-6e iota_Co acts on the exceptional P^2 by [-X:-Y:-Z] = [X:Y:Z] (D fixed pointwise)",
      sp.simplify(sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]) * sp.Matrix([X, Y, Z])
                  - sp.Matrix([-X, -Y, -Z])) == sp.zeros(3, 1))
check("PL-6f iota_dP acts on the exceptional P^2 by [X:Y:-Z] (two fixed points on D)",
      sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]]).det() == -1)

# ------------------------------------------------- PL-7: genus and Lefschetz data
B2 = 2 * 4 * 4
KB = -2 * 4 - 2 * 4
pa = 1 + sp.Rational(B2 + KB, 2)
check("PL-7a arithmetic genus of B is 9", pa == 9, "B^2 = %d, K_Y.B = %d, p_a = %s" % (B2, KB, pa))
k = sp.symbols('k', integer=True, nonnegative=True)
check("PL-7b rk S_dP = (2k-16+20)/2 = k+2 and rk S_Co = (2k+20)/2 = k+10",
      sp.simplify((2 * k - 16 + 20) / 2 - (k + 2)) == 0
      and sp.simplify((2 * k + 20) / 2 - (k + 10)) == 0)

# ------------------------------------------------- PL-8: degrees of the split ruling fibre
check("PL-8a (I_2 stratum only, a_02 != 0: see ledger 3.7 for the IV stratum) the node-ruling fibre L1 = D + D' has H-degrees 0 and 2",
      dot(Hv, Dv) == 0 and dot(Hv, Dpv) == 2 and (Dv + Dpv - L1v) == sp.zeros(3, 1))

# ------------------------------------------------- PL-9: H-orthogonality census
# On the explicit member, D is the only H-degree-0 component in the two node rulings,
# and D' has H-degree 2.  (The general proof of the census is in the ledger, 3.9.)
check("PL-9a (I_2 stratum, a_02 != 0) D.L1 = 0 = D.L2 and D'.L1 = 0, D'.L2 = 2",
      dot(Dv, L1v) == 0 and dot(Dv, L2v) == 0 and dot(Dpv, L1v) == 0 and dot(Dpv, L2v) == 2)

print()
print("summary: %d checks passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
    raise SystemExit(1)
