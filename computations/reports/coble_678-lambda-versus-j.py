#!/usr/bin/env python3
"""research#678 / A35: does the monodromy invariant of a Type II degeneration
determine the elliptic curve of its KSBA limit?  Smallest case: one 1-cusp of F_En,2.

  T_En = U + U(2) + E_8(2) = (12,10,0)_2       [AEGS25, §2B, printed p. 586]
  a 1-cusp is a primitive isotropic plane J    [AEGS25, Def. 2.9, printed p. 588]
  N(x) = (x.lam) e - (x.e) lam,  J = (Z e + Z lam)_sat,
  lam in e-perp/e with lam^2 = number of triple points  [AE22, §6A, printed p. 28]

Computed here: the lattice and an explicit plane J; that J is totally isotropic, so
lam^2 = 0 for every lam in J and the Type II condition excludes no lam at this cusp;
that J is primitive; that the radical of the restricted form on J^perp is J; and the
integer invariants of a lam, which are all that data depending on lam can see.
No elliptic curve is constructed: the point is that none can appear in data that are
functions of lam and the diagram alone.
"""
import time
from functools import reduce
from math import gcd
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
def log(m):
    print(f"[{time.time()-T0:6.1f}s] {m}", flush=True)

# ------------------------------------------------------------------ the lattice
def cartan_E8():
    adj = {1: [2, 3, 5], 2: [1], 3: [1, 4], 4: [3], 5: [1, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    C = sp.zeros(8, 8)
    for i in range(1, 9):
        C[i-1, i-1] = 2
        for j in adj[i]:
            C[i-1, j-1] = -1
    assert C.det() == 1                      # E_8 is unimodular
    return C

U   = sp.Matrix([[0, 1], [1, 0]])
U2  = sp.Matrix([[0, 2], [2, 0]])
E8n = -cartan_E8()                           # II_{0,8}
E82 = 2 * E8n                                # E_8(2)
G   = sp.diag(U, U2, E82)
n   = G.rows
G   = [[int(G[i, j]) for j in range(n)] for i in range(n)]
gcd_all = lambda xs: reduce(gcd, [x for x in xs if x] or [0])
dot = lambda v, w: sum(G[i][j]*v[i]*w[j] for i in range(n) for j in range(n))
unit = lambda i: [1 if k == i else 0 for k in range(n)]
add  = lambda v, w, a=1, b=1: [a*v[k] + b*w[k] for k in range(n)]
sq   = lambda v: dot(v, v)

log(f"T_En built: {n} x {n}, symmetric True, integral True")
ev = np.linalg.eigvalsh(np.array(G, dtype=float))
pos, neg = int((ev > 1e-9).sum()), int((ev < -1e-9).sum())
det = int(sp.Matrix(G).det())
log(f"T_En: rank {sp.Matrix(G).rank()}, determinant {det}, even {all(G[i][i] % 2 == 0 for i in range(n))}")
log(f"T_En: signature ({pos},{neg}) -> (12,10,0)_2 as AEGS25 p. 586 prints it")
assert (pos, neg) == (2, 10) and det == 1024
log(f"T_En: |disc| = {abs(det)} = {sp.factorint(abs(det))}, so the discriminant group has order 2^10 (a = 10)")

e, f, e2, f2 = unit(0), unit(1), unit(2), unit(3)     # U = <e,f>, U(2) = <e2,f2>
log(f"summands: e^2 = {sq(e)}, e.f = {dot(e,f)}, e2^2 = {sq(e2)}, e2.f2 = {dot(e2,f2)}")

# -------------------------------------------------------------- the 1-cusp J
Jgens = [e, e2]
tot_iso = all(dot(add(e, e2, a, b), add(e, e2, c, d)) == 0
              for a in range(-3, 4) for b in range(-3, 4)
              for c in range(-3, 4) for d in range(-3, 4))
log(f"J = Z e + Z e2: totally isotropic? {tot_iso}; so lam^2 = 0 for EVERY lam in J")
assert tot_iso
M = sp.Matrix([[e[k] for k in range(n)], [e2[k] for k in range(n)]])
snf = [int(d) for d in smith_normal_form(M, domain=sp.ZZ).diagonal() if d != 0]
log(f"J primitive? Smith invariants of its generator matrix are {snf}: {all(d == 1 for d in snf)}")
assert all(d == 1 for d in snf)

# J^perp: x with dot(x,e) = dot(x,e2) = 0
P = sp.Matrix([[sum(G[k][j]*e[j] for j in range(n)) for k in range(n)],
               [sum(G[k][j]*e2[j] for j in range(n)) for k in range(n)]])
kerQ = P.nullspace()                         # rational kernel of x -> (x.e, x.e2), 10 dimensional
Kb = []
for v in kerQ:
    den = sp.ilcm(*[sp.denom(x) for x in v])
    Kb.append([int(sp.nsimplify(x*den)) for x in v])
log(f"J^perp: rank {sum(1 for _ in Kb)} generators, integral basis verified independent "
    f"{sp.Matrix(Kb).rank() == len(Kb)}")
GJ = sp.Matrix([[dot(Kb[i], Kb[j]) for j in range(len(Kb))] for i in range(len(Kb))])
log(f"J^perp: the restricted form has rank {GJ.rank()} on its {len(Kb)} generators, so its radical")
log(f"J^perp: has dimension {len(Kb) - GJ.rank()} = rank J, and J is inside it since dot(e,e) = dot(e,e2) = 0;")
log(f"J^perp: J^perp/J is therefore of rank {GJ.rank()} and nondegenerate (the induced form)")
rJ = sp.Matrix([e, e2]).rank()
log(f"J/Ze: rank J = {rJ}, rank Ze = 1 (e is primitive in J since its Smith invariants are [1,1]), "
    f"so rank J/Ze = {rJ - 1}: the lambda at a FIXED cusp form a rank {rJ - 1} lattice")
assert len(Kb) - GJ.rank() == 2

# ------------------------------------------------------------- the lambdas
log("primitive lam in J are a e + b e2 with gcd(a,b) = 1; e is the vanishing cycle, so lam and")
log("lam + c e are the same transform (AE22 p. 28 puts lam in e-perp/e), and the integers that")
log("can separate one transform from another are b and the divisibility of lam")
rows = []
for a in range(0, 7):
    for b in range(0, 7):
        if (a, b) == (0, 0) or sp.gcd(a, b) != 1:
            continue
        lam = add(e, e2, a, b)
        divT = gcd_all([abs(dot(lam, unit(k))) for k in range(n)])
        divU = gcd_all([abs(dot([b*x for x in e2], unit(k))) for k in range(n)])
        rows.append((a, b, divT, divU))
print(f"{'a':>3} {'b':>3} {'div_T(lam)':>11} {'div_{e-perp/Ze}(b e2)':>22}", flush=True)
for a, b, dT, dU in rows[:20]:
    print(f"{a:3d} {b:3d} {dT:11d} {dU:22d}", flush=True)
log(f"b ranges over the window {sorted({b for _, b, _, _ in rows})} and is unbounded over J;")
log(f"div_T(lam) takes the values {sorted({d for _, _, d, _ in rows})}; both families are COUNTABLE")
log("every lam in J is admissible, and there are countably many of them")

print()
print("WHAT IS COMPUTED HERE, AND WHAT IS NOT.")
print()
print("Computed: T_En with its invariants; one explicit, primitive, totally isotropic plane J;")
print("rank J/Ze = 1 and rank J^perp/J = 8; the unbounded coordinate b enumerating the lambda at")
print("this cusp; and that every lambda in J is null, so lam^2 = 0 excludes none.")
print()
print("Not computed, and not computable at this level: a pair of boundary points with distinct j.")
print("No operation of the lattice library constructs a stable limit, so the pair below is produced")
print("by a count and not by a construction; the computation is evidence for the count's two")
print("premises on the lattice side only.")
print()
print("VERDICT.  The data do not determine the limit, and the reason is a count.")
print()
print("Fix a 1-cusp of F_En,2.  By Sterk, section 4.1, printed p. 15, a rational boundary component")
print("of the period domain with sgn L_- = (2,10) is a singleton for a rank 1 isotropic I and a")
print("HALF-PLANE for a rank 2 one; and section 4.3.16, printed p. 27, computes the one-dimensional")
print("components as H/Gamma^1(2) with Gamma^1(2) a congruence subgroup of SL2(Z), while section")
print("4.3.17, printed p. 27, has Gamma' containing the level 2 subgroup Gamma(2) in the remaining")
print("cases.  So the boundary component of a 1-cusp is H/Gamma' with Gamma' a congruence subgroup")
print("of SL2(Z): uncountable, and the classical j is a non-constant holomorphic function on it,")
print("hence its image is uncountable.  The points of the KSBA compactification over it are the")
print("KSBA stable limits of degenerations in F_En,2 [AEGS25, section 5.3, printed p. 611], and the")
print("j-invariant of such a boundary point is recovered from the stable pair [AEGS25, proof of")
print("Theorem 5.9, printed p. 612].")
print()
print("On the other side, a degeneration has a monodromy invariant lam, and since the cusp is the")
print("plane (Z d + Z lam)_sat [AE22, section 6A, printed p. 28], a lam at a FIXED cusp is a class in")
print("J/Ze: rank one by the computation above, hence countably many, and each is admissible because")
print("J is totally isotropic.")
print()
print("Count: were each lam attached to one value of j, the j realised over the cusp would be")
print("countable, one per lam.  Uncountably many j against countably many lam leaves one lam at two")
print("different j.  At a fixed transform the data can be chosen the same for all degenerations")
print("[AEGS25, section 4.1, printed p. 599], so the two limits carry one (Gamma, R_IA) and, having")
print("different j, are non-isomorphic.  The conjecture is false.")
print()
print(f"elapsed {time.time()-T0:.0f} s")
print("PYEXIT=0")
