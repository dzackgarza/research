"""#759: the swap of roots 12 and 13 is not a direct-summand construction, and that is where it stops.

The pair that survives at cusp 5
--------------------------------
coble_759-lift-1314-run.txt proves that the cusp symmetry exchanging roots 13 and 14 lifts, so
those two classes are one Gamma_Co,2-orbit.  The only pair still undecided is (12, 13).

What this record settles
------------------------
The construction that settled (13, 14) cannot settle (12, 13).  There, the span S of all fourteen
roots met its orthogonal complement in index 1 and T_En = S + S^perp was an orthogonal direct sum,
so the desired action on S extended by the identity on S^perp.  Here the analogous span is

    P = sat.span(r12, r13, delta):  rank 3, det -8,   P^perp: rank 9, det -512,
    det P * det P^perp = 4096 = 4 * det T_En,        so [T_En : P + P^perp] = 2.

Index 2, not 1: P is not a direct summand, the swap of r12 with r13 does not extend by the
identity on P^perp, and an order-2 gluing obstructs the construction.

What it does not settle
-----------------------
Anything about the pair itself.  An obstruction to this one candidate is not an obstruction to
every isometry of T_En: an element of Gamma_Co,2 carrying the class of r12 to that of r13 need not
preserve the span P or act as this swap on it, and no proof of that kind is available here.  The
pair therefore rests where the library leaves it: on the orbit computation of
sage-extensions#370 (its call failing in this image as #389), as recorded in
coble_760-orbit-decision-probe-run.txt.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_759-swap-1213.py

Transcript: coble_759-swap-1213-run.txt.  Sage in the shared runtime, exact ZZ/QQ algebra.
"""
import sys
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
sys.stdout.reconfigure(line_buffering=True)
C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]
def ip(x, y): return int(vector(ZZ, x) * G * vector(ZZ, y))
delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j])); Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])

r12, r13, r14 = ROOTS[11], ROOTS[12], ROOTS[13]
print("pairings: r12.r13 = %d, r12.delta = %d, r13.delta = %d; each square %d"
      % (ip(r12, r13), ip(r12, delta), ip(r13, delta), ip(r12, r12)))

Pm = matrix(ZZ, [vector(ZZ, r12), vector(ZZ, r13), vector(ZZ, delta)]).saturation()
print("P = sat.span(r12, r13, delta): rank %d" % Pm.nrows())
GP = matrix(ZZ, Pm.nrows(), Pm.nrows(), lambda i, j: ip(Pm[i], Pm[j]))
F = Pm * G
K = matrix(ZZ, F.right_kernel_matrix()).saturation()
GK = matrix(ZZ, K.nrows(), K.nrows(), lambda i, j: ip(K[i], K[j]))
print("P^perp: rank %d, det %d;  det P = %d, det P * det P^perp = %d, det T_En = %d"
      % (K.nrows(), GK.det(), GP.det(), GP.det() * GK.det(), G.det()))
d2 = QQ(GP.det()) * QQ(GK.det()) / QQ(G.det())
print("index^2 of P + P^perp: %s -> index %s" % (d2, d2.sqrt() if d2.is_square() else "not a square"))
if d2 == 1:
    print()
    print("P is a direct summand: T_En = P + P^perp with index 1.  So the swap r12 <-> r13 on P,")
    print("extended by the identity on P^perp, is a well defined integral map.  Building it:")
    SB = matrix(QQ, Pm).transpose(); PB = matrix(QQ, K).transpose()
    Basis = SB.augment(PB); Binv = Basis.inverse()
    P_P = SB * Binv[0:Pm.nrows(), :]; P_R = PB * Binv[Pm.nrows():, :]
    # the swap as a matrix on the coordinates of P
    Ginv = matrix(QQ, GP).inverse()
    S = matrix(ZZ, Pm.nrows(), Pm.nrows(), [[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    TS = (SB * S * Ginv * SB.transpose() * G)      # the induced map on T_En restricted in P-coords
    M = TS + P_R
    Mi = matrix(ZZ, [[int(x) for x in M[k]] for k in range(N)]) if all(x in ZZ for x in M.list()) else None
    print("  M integral: %s" % (Mi is not None))
    if Mi is not None:
        print("  M^T G M == G: %s" % (Mi.transpose() * G * Mi == G))
        print("  M delta == delta: %s" % (Mi * vector(ZZ, delta) == vector(ZZ, delta)))
        print("  M r12 == r13: %s ; M r13 == r12: %s"
              % (Mi * vector(ZZ, r12) == vector(ZZ, r13), Mi * vector(ZZ, r13) == vector(ZZ, r12)))
        print("  M eta == eta: %s" % (Mi * vector(ZZ, eta) == vector(ZZ, eta)))
        ok = (Mi.transpose() * G * Mi == G and Mi * vector(ZZ, delta) == vector(ZZ, delta)
              and Mi * vector(ZZ, r12) == vector(ZZ, r13) and Mi * vector(ZZ, eta) == vector(ZZ, eta))
        print()
        if ok:
            print("RESULT: the swap LIFTS.  Roots 12 and 13 are one Gamma_Co,2-orbit as well, so all")
            print("three admissible roots at cusp 5 are one orbit and the conjecture's hypothesis is")
            print("never met there.")
        else:
            print("RESULT: a check failed; see above.")
else:
    print()
    print("RESULT: P is not a direct summand (index %s); the identity extension is not available and" % d2)
    print("the gluing question for this pair is open.")
print()
print("=== the same question inside the rank-10 span S of the fourteen roots")
print("T_En = S + S^perp with index 1 (coble_759-lift-1314-run.txt), so an isometry of S extends;")
print("the class of r12 maps to the class of r13 exactly, since S meets S^perp in 0 and eta lies")
print("in S^perp.  So the pair is decided by whether <r12, r13> is a direct summand of S:")
Sm = matrix(ZZ, [vector(ZZ, r) for r in ROOTS]).saturation()
GS = matrix(ZZ, Sm.nrows(), Sm.nrows(), lambda i, j: ip(Sm[i], Sm[j]))
P2 = matrix(ZZ, [vector(ZZ, r12), vector(ZZ, r13)]).saturation()
GP2 = matrix(ZZ, P2.nrows(), P2.nrows(), lambda i, j: ip(P2[i], P2[j]))
func = P2 * G * Sm.transpose()
K2 = matrix(ZZ, matrix(ZZ, func).right_kernel_matrix()).saturation()
basis2 = K2 * Sm
GK2 = matrix(ZZ, basis2.nrows(), basis2.nrows(), lambda i, j: ip(basis2[i], basis2[j]))
print("  S: rank %d, det %d;  P = sat.span(r12, r13): rank %d, det %d;  P^perp in S: rank %d, det %d"
      % (Sm.nrows(), GS.det(), P2.nrows(), GP2.det(), basis2.nrows(), GK2.det()))
d2S = QQ(GP2.det()) * QQ(GK2.det()) / QQ(GS.det())
print("  index^2 of P + P^perp in S: %s -> index %s" % (d2S, d2S.sqrt() if d2S.is_square() else "?"))
if d2S == 1:
    print("  RESULT: a direct summand of S; the swap extends inside S and hence to T_En.")
else:
    print("  RESULT: not a direct summand of S either, so the construction fails at rank 10 as well.")
    print("  What remains is a gluing extension inside S, or a transporter for a family with")
    print("  nontrivial pointwise orthogonal stabilizer, which the library does not provide")
    print("  (coble_759-transporter-1213-run.txt).")
print("PYEXIT=0")
