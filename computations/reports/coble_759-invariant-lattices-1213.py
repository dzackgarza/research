"""#759: the invariant lattices of the pair (12,13) -- the reliable half of the comparison.

If g is an integral isometry of T_En with g(delta) = +-delta, g(eta_5) = +-eta_5 and
g(r12) = +-r13 + k*eta_5, then it carries the lattice

    L(r) = (r^perp cap delta^perp cap eta_5^perp) / Z eta_5          (rank 8)

for r = r12 onto the one for r = r13.  This record computes both: determinant, Smith normal
form of the Gram, signature and parity.  They agree, so this test separates nothing.

What this record does NOT do
----------------------------
It does not compare the discriminant forms, which is the finer invariant.  That comparison was
attempted in the same session and abandoned: the version written here failed its own
basis-independence control (the multiset of q-values changed when the basis changed, so the
representative construction was wrong), and the library's own discriminant form wants a bilinear
form object rather than a Gram matrix, which was not resolved in the time available.  A failed
control is not evidence, so nothing is claimed from it -- in particular the pair is NOT reported
as inequivalent on that basis.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_759-invariant-lattices-1213.py

Transcript: coble_759-invariant-lattices-1213-run.txt.  Sage in the shared runtime.
"""
import sys, itertools
from collections import Counter
from sage.all import ZZ, QQ, RDF, matrix, vector, block_diagonal_matrix, CartanMatrix, floor
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
r12, r13 = ROOTS[11], ROOTS[12]

def lattice_of(vs):
    """(r^perp cap delta^perp cap eta^perp) modulo Z eta, with its Gram: rank 8, nondegenerate"""
    import math
    func = matrix(ZZ, len(vs), N, [[ip(b, v) for b in BAS] for v in vs])
    B = matrix(ZZ, func.right_kernel_matrix()).saturation()
    assert B.nrows() == 9, B.nrows()
    NB = matrix(ZZ, 9, 9, lambda i, j: ip(B[i], B[j]))
    cvec = matrix(QQ, B).transpose().solve_right(vector(QQ, eta))
    assert all(x in ZZ for x in cvec), list(cvec)
    c = vector(ZZ, [int(x) for x in cvec])
    assert math.gcd(*list(c)) == 1
    D, Usm, Vsm = matrix(ZZ, 1, 9, list(c)).smith_form()
    assert list(D[0]) == [1] + [0] * 8, list(D[0])
    Fm = matrix(ZZ, Vsm.inverse() if Usm[0, 0] == 1 else -Vsm.inverse())
    if vector(ZZ, [int(x) for x in Fm[0]]) == -c:
        Fm = matrix(ZZ, [-1] + [0] * 8).stack(Fm[1:])
    assert vector(ZZ, [int(x) for x in Fm[0]]) == c
    N9 = Fm * NB * Fm.transpose()
    assert vector(ZZ, (Fm * B)[0]) == vector(ZZ, eta), "eta is not the first basis vector"
    return (Fm * B)[1:], N9[1:, 1:]


res = {}
for lab, r in ((12, r12), (13, r13)):
    K, GB = lattice_of([r, delta, eta])
    assert K.nrows() == 8, K.nrows()
    ev = GB.change_ring(RDF).eigenvalues()
    res[lab] = dict(det=GB.det(), smith=[abs(x) for x in GB.smith_form()[0].diagonal()],
                    sig=(sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9)),
                    even=all(GB[i, i] % 2 == 0 for i in range(8)), GB=GB)
    d = res[lab]
    print("label %2d: rank 8, det %d, Smith %s, signature %s, even %s"
          % (lab, d["det"], d["smith"], d["sig"], d["even"]))

print()
same = {k: res[12][k] == res[13][k] for k in ("det", "smith", "sig", "even")}
print("invariants equal:", same)
print()
if all(same.values()):
    print("RESULT: the two invariant lattices agree in determinant, Smith invariants, signature and")
    print("parity, so this test does not separate the pair.  The finer comparison, of the")
    print("discriminant forms, was attempted and discarded: this record's version of it failed its")
    print("own basis-independence control, so no difference it showed is reported as evidence.")
else:
    print("RESULT: an invariant differs, so no isometry of T_En fixes delta and eta and carries")
    print("r12 to r13 mod eta: the pair (12,13) is INEQUIVALENT.")
print("PYEXIT=0")
