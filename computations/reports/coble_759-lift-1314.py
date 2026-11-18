"""#759/#760: the cusp-5 symmetry exchanging roots 13 and 14 lifts to Gamma_Co,2.

The question
------------
coble_760-cusp-symmetry-run.txt records that exactly one symmetry of the labelled cusp-5 Gram
fixes the Coble root's label 11 and exchanges labels 13 and 14, and that a lift of it would make
those two roots Gamma_Co,2-equivalent.  This record settles the lift: it is YES, and the witness
is explicit.

Why it is decidable
-------------------
delta lies in S = sat.span(the fourteen roots), which has rank 10, so any lift restricts to the
map the permutation induces on S -- well defined because the permutation is a Gram automorphism
of the fourteen roots -- and that map fixes delta exactly, not merely its line.  The lattice
orthogonal complement is then computed, not guessed: with S saturated and T_En of determinant
1024,

    S^perp has rank 2, Gram [[0,2],[2,4]], determinant -4,   det S * det S^perp = 1024,

so S + S^perp has index 1 in T_En and T_En = S + S^perp is an orthogonal direct sum.  In that
situation no gluing obstruction can occur: tau on S together with the identity on S^perp is a
well defined integral map, and it is the required lift.

The witness
-----------
M = tau on S, identity on S^perp, constructed as M = tau.P_S + P_perp from the projections of
T_En onto the two summands.  The record checks all four conditions and prints them: M integral,
M^T G M = G, M(delta) = delta, and M r_i = r_{sigma(i)} for all fourteen printed roots, with
det M = -1.

Consequence
-----------
The classes of roots 13 and 14 at cusp 5 are one Gamma_Co,2-orbit.  They are equivalent, so that
pair cannot witness a failure of conj:no_moduli_loss, and the only pair at cusp 5 whose
equivalence is undecided is (12, 13).

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_759-lift-1314.py

Transcript: coble_759-lift-1314-run.txt.  Sage in the shared runtime, exact ZZ/QQ algebra.
"""
import sys, itertools
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
SIG = [8, 6, 5, 4, 3, 2, 7, 1, 9, 10, 11, 12, 14, 13]

# S = saturated span of the roots, and a 12x12 integral basis with S first
Sm = matrix(ZZ, [vector(ZZ, r) for r in ROOTS]).saturation()
r = Sm.nrows()
print("S = sat.span(roots): rank %d; delta in S: %s" % (r, (matrix(QQ, Sm).transpose().solve_right(vector(QQ, delta)) is not None)))
W = Sm.stack(matrix(ZZ, 2, N))            # placeholder, filled below
# complete the S rows to a unimodular-in-QQ 12x12 basis by adding standard vectors greedily
rows = [vector(ZZ, s) for s in Sm]
for b in BAS:
    if matrix(QQ, rows + [b]).rank() > len(rows):
        rows.append(vector(ZZ, b))
    if len(rows) == N:
        break
WB = matrix(ZZ, rows)
assert WB.rank() == N
c1, c2 = WB[r], WB[r + 1]
print("complement vectors c1 = %s..., c2 = %s...; index [T_En : S + Zc] = %s"
      % (list(c1)[:4], list(c2)[:4], abs(WB.det())))

# M on S: the permutation's action, as before
Mt, rhs = [], []
for i in range(14):
    src = vector(ZZ, ROOTS[i]); tgt = vector(ZZ, ROOTS[SIG[i] - 1])
    for k in range(N):
        row = [0] * (N * N)
        for j in range(N):
            row[k * N + j] = src[j]
        Mt.append(row); rhs.append(int(tgt[k]))
A = matrix(QQ, Mt); b = vector(QQ, rhs)
Msol = matrix(QQ, N, N, list(A.solve_right(b)))
assert (Msol * vector(QQ, delta)) == vector(QQ, delta)
print("M on S: fixes delta exactly; M s = sigma(s) on the fourteen roots")

F = Sm * G                      # rows are the functionals x |-> (s . x)
K = F.right_kernel_matrix()
Ka = matrix(ZZ, K).saturation()
GS = matrix(ZZ, r, r, lambda i, j: ip(Sm[i], Sm[j]))
GP = matrix(ZZ, Ka.nrows(), Ka.nrows(), lambda i, j: ip(Ka[i], Ka[j]))
print("S^perp: rank %d, Gram %s, det %d;  det S * det S^perp = %d, det T_En = %d"
      % (Ka.nrows(), [[int(GP[i, j]) for j in range(GP.nrows())] for i in range(GP.nrows())],
         GP.det(), GS.det() * GP.det(), G.det()))
d2 = QQ(GS.det()) * QQ(GP.det()) / QQ(G.det())
print("index^2 of S + S^perp in T_En: %s  -> index %s" % (d2, d2.sqrt() if d2.is_square() else "not a square"))
if d2 != 1:
    print("RESULT: the sum is not the whole lattice, so the direct-sum construction does not apply.")
    print("PYEXIT=0"); raise SystemExit()

# T_En = S + S^perp with index 1, so every x is x_S + x_perp with both integral, and
# M = tau on S, identity on S^perp is a well defined integral isometry.
SB = matrix(QQ, Sm).transpose()                  # 12 x 10, columns a basis of S
PB = matrix(QQ, Ka).transpose()                  # 12 x 2, columns a basis of S^perp
Basis = SB.augment(PB)                           # 12 x 12, invertible over QQ
Binv = Basis.inverse()
P_S = SB * Binv[0:r, :]                          # projection onto S along S^perp
P_P = PB * Binv[r:, :]                           # projection onto S^perp along S
M = Msol * P_S + P_P
print("M = tau on S, identity on S^perp: integral %s" % all(x in ZZ for x in M.list()))
Mi = matrix(ZZ, [[int(x) for x in M[k]] for k in range(N)])
print("  M^T G M == G: %s" % (Mi.transpose() * G * Mi == G))
print("  M delta == delta: %s" % (Mi * vector(ZZ, delta) == vector(ZZ, delta)))
print("  M r_i == r_sigma(i) for all fourteen roots: %s"
      % all(Mi * vector(ZZ, ROOTS[i]) == vector(ZZ, ROOTS[SIG[i] - 1]) for i in range(14)))
print("  det M: %d" % Mi.det())
ok = (all(x in ZZ for x in M.list()) and Mi.transpose() * G * Mi == G
      and Mi * vector(ZZ, delta) == vector(ZZ, delta)
      and all(Mi * vector(ZZ, ROOTS[i]) == vector(ZZ, ROOTS[SIG[i] - 1]) for i in range(14)))
print()
if ok:
    print("RESULT: the permutation LIFTS.  M = tau on S and the identity on S^perp is an integral")
    print("isometry of T_En fixing delta and exchanging labels 13 and 14.  Hence the classes of")
    print("roots 13 and 14 are one Gamma_Co,2-orbit, and (12, 13) is the only pair left at cusp 5.")
else:
    print("RESULT: the direct-sum map fails a check; see the lines above.")
print("PYEXIT=0")
