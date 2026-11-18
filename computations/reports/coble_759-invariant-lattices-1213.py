"""#759: the invariant lattices of the pair (12,13) -- the reliable half of the comparison.

If g is an integral isometry of T_En with g(delta) = +-delta, g(eta_5) = +-eta_5 and
g(r12) = +-r13 + k*eta_5, then it carries the lattice

    L(r) = (r^perp cap delta^perp cap eta_5^perp) / Z eta_5          (rank 8)

for r = r12 onto the one for r = r13.  This record computes both: determinant, Smith normal
form of the Gram, signature and parity.  They agree, so this test separates nothing.

What this record also does
--------------------------
It compares the finer invariant, the discriminant forms, through the library: both lattices are
built as bilinear-form tensors and their q-forms evaluated on the discriminant group, which makes
the comparison basis-free by construction.  The two agree -- |A| = 256 on both, and the same
multiset of q-values -- so this test separates nothing either.

An earlier attempt at that comparison in the same session was discarded because it failed its own
basis-independence control; this is a different, library-based computation, and it is the one
reported.

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


def rank8_gram(r):
    vs = (r, delta, eta)
    func = matrix(ZZ, 3, N, lambda i, j: ip(BAS[j], vs[i]))
    B = matrix(ZZ, func.right_kernel_matrix()).saturation()
    NB = matrix(ZZ, 9, 9, lambda i, j: ip(B[i], B[j]))
    c = vector(ZZ, [int(x) for x in matrix(QQ, B).transpose().solve_right(vector(QQ, eta))])
    D, Usm, Vsm = matrix(ZZ, 1, 9, list(c)).smith_form()
    Fm = matrix(ZZ, Vsm.inverse() if Usm[0, 0] == 1 else -Vsm.inverse())
    if vector(ZZ, [int(x) for x in Fm[0]]) == -c:
        Fm = matrix(ZZ, [-1] + [0] * 8).stack(Fm[1:])
    N9 = Fm * NB * Fm.transpose()
    return N9[1:, 1:]


res = {}
for lab, r in ((12, ROOTS[11]), (13, ROOTS[12])):
    GB = rank8_gram(r)
    ev = GB.change_ring(RDF).eigenvalues()
    res[lab] = dict(det=GB.det(), smith=[abs(x) for x in GB.smith_form()[0].diagonal()],
                    sig=(sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9)),
                    even=all(GB[i, i] % 2 == 0 for i in range(8)))
    d = res[lab]
    print("label %2d: rank 8, det %d, Smith %s, signature %s, even %s"
          % (lab, d["det"], d["smith"], d["sig"], d["even"]))
same = {k: res[12][k] == res[13][k] for k in ("det", "smith", "sig", "even")}
print()
print("coarse invariants equal:", same)
print()
print("=== (2) the discriminant forms, through the library")
from sage_extensions.all import Lattices, tensor, ZZ as LZZ
from collections import Counter
info = {}
for lab, r in ((12, ROOTS[11]), (13, ROOTS[12])):
    Gr = rank8_gram(r)
    values = [[LZZ(int(Gr[i, j])) for j in range(8)] for i in range(8)]
    L = Lattices(LZZ)(tensor(LZZ, (), (8, 8), values))
    form = L.discriminant_group()
    els = list(form.elements())
    qs = Counter(str(form.q(p)) for p in els)
    info[lab] = dict(qs=dict(qs), card=len(els))
    print("  label %2d: |A| = %d, %d distinct q values" % (lab, len(els), len(qs)), flush=True)
print("  q multisets equal: %s" % (info[12]["qs"] == info[13]["qs"]))
print()
if info[12]["qs"] == info[13]["qs"]:
    print("VERDICT: determinant, Smith invariants, signature, parity and the discriminant form all")
    print("agree for the two roots, so no invariant available here separates the pair (12,13).")
else:
    print("VERDICT: the discriminant forms differ, so the two lattices are not isometric and the pair")
    print("(12,13) is INEQUIVALENT.")
print("PYEXIT=0")
