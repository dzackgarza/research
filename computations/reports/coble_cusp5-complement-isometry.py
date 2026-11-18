"""#759/#760: do the boundary-lattice invariants separate the three T_Co-roots at cusp 5?

The question
------------
At the marked 0-cusp 5 of F_En,2 with representative eta_5 and boundary lattice
K_5 = eta_5^perp / Z eta_5, the admissible T_Co-roots are Sterk's printed labels 12, 13, 14.
Distinct classes in K_5 are not distinct Gamma_Co,2-orbits, so inequivalence needs an argument
that is invariant under the group.  Gamma_Co,2 acts on K_5 by isometries; hence if r and r'
are in one orbit, the rank-9 lattices r^perp and r'^perp inside K_5 are isometric.  This
record computes, exactly, the isometry invariants of the three complements.

What the invariants decide
--------------------------
They decide *inequivalence* when they differ: two roots whose complements are not isometric
lie in different Gamma_Co,2-orbits.  When they agree the record decides nothing about the
orbits, and it says so.  What it does decide in that case is that no argument through the
isometry class of r^perp -- the only invariants of a marked class that the boundary lattice
itself supplies -- can separate the three roots.

The data
--------
T_En = U + U(2) + E8(2) with basis (e, f, e', f', a_1..a_8): e.f = 1, e'.f' = 2, and the a_i
have Gram matrix -2 cartan(E8).  delta = e - f is the Coble root (lem:coble-heegner-vector);
eta_5 = 2e + 2f + abar_0 is Sterk's representative (coble_cusp-admissibility.py); the fourteen
printed roots of cusp 5 are transcribed verbatim from the same record, whose provenance is
coble_sterk-root-lifts-run.txt.

The lattice K_5 is built as eta_5^perp modulo Z eta_5: a Z-basis of eta_5^perp, then a
unimodular change of basis carrying eta_5 to the first slot, from the Smith form of its
coordinate vector; the Gram of K_5 is the remaining 10 x 10 block, and a class is a vector of
those ten coordinates.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_cusp5-complement-isometry.py

Transcript: coble_cusp5-complement-isometry-run.txt.  Sage in the shared runtime, exact ZZ/QQ
linear algebra only; no GAP, no pari, no provider call.
"""
import sys
import time
import math

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, RDF, matrix, vector, block_diagonal_matrix, CartanMatrix
from sage.version import version as SAGE_VERSION

t0 = time.time()

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))])
        for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))])
         for i in range(8)]
eta = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
          2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
          et + ft + (abart[5] - abart[2]), et + ft + (abart[0] + abart[7] - abart[2]),
          et + ft + at[2]])


def funcs(vs):
    return matrix(ZZ, len(vs), N, [[ip(b, v) for b in BAS] for v in vs])


def kernel_basis(vs, rank_expected):
    """a Z-basis of {x in T_En : (x, v) = 0 for every v in vs}; a kernel is saturated"""
    K = funcs(vs).right_kernel_matrix()
    KZ = matrix(ZZ, K).saturation()
    assert KZ.nrows() == rank_expected, (KZ.nrows(), rank_expected)
    return KZ


print("the complements of the admissible roots 12, 13, 14 in the boundary lattice K_5")
print("Sage %s; exact ZZ/QQ linear algebra" % SAGE_VERSION)
print("T_En Gram determinant %d; delta^2 = %d; eta_5^2 = %d, div_TEn(eta_5) = %d"
      % (G.det(), ip(delta, delta), ip(eta, eta),
         math.gcd(*[ip(eta, b) for b in BAS])))
print()

# ---- the lattice K_5 = eta_5^perp / Z eta_5, with its Gram ---------------------------
B11 = kernel_basis([eta], 11)
NB = matrix(ZZ, 11, 11, lambda i, j: ip(B11[i], B11[j]))
cvec = matrix(QQ, B11).transpose().solve_right(vector(QQ, eta))
assert all(x in ZZ for x in cvec), list(cvec)
c = vector(ZZ, [int(x) for x in cvec])
assert math.gcd(*list(c)) == 1, list(c)
D, Usm, Vsm = matrix(ZZ, 1, 11, list(c)).smith_form()
assert list(D[0]) == [1] + [0] * 10, list(D[0])
F = matrix(ZZ, Vsm.inverse() if Usm[0, 0] == 1 else -Vsm.inverse())
if vector(ZZ, [int(x) for x in F[0]]) == -c:
    F = matrix(ZZ, [-1] + [0] * 10).stack(F[1:])
assert vector(ZZ, [int(x) for x in F[0]]) == c
assert abs(F.det()) == 1
N11 = F * NB * F.transpose()
assert vector(ZZ, (F * B11)[0]) == vector(ZZ, eta), "eta is not the first new basis vector"
GK = N11[1:, 1:]
EVK = GK.change_ring(RDF).eigenvalues()
print("K_5: rank %d, det %d, signature (%d, %d), even: %s"
      % (GK.nrows(), GK.det(), sum(1 for x in EVK if x > 1e-9),
         sum(1 for x in EVK if x < -1e-9), all(GK[i, i] % 2 == 0 for i in range(10))))
Finv = F.inverse().transpose()


def class_coords(v):
    """the coordinates of the class of v in the K_5 basis: the eta coordinate is dropped"""
    a = matrix(QQ, B11).transpose().solve_right(vector(QQ, v))
    b = Finv * a
    assert all(x in ZZ for x in b), list(b)
    return vector(ZZ, [int(x) for x in list(b)[1:]])


def disc_coparity(Gr):
    """delta of a 2-elementary lattice: 0 iff q(x) = x.x in Z for every x of the dual quotient

    The discriminant group of a 2-elementary lattice is 2-torsion, so its classes are the
    half-lattice points x = Gi.w/2 with w integral; q(x) = (w.Gi.w)/4 [@AEGS25, section 2.3].
    """
    d = Gr.nrows()
    Gi = matrix(QQ, Gr).inverse()
    vals = set()
    for v in __import__("itertools").product([0, 1], repeat=d):
        vv = vector(QQ, v)
        vals.add(QQ(vv * Gi * vv) / 4)
    return 0 if all(x in ZZ for x in vals) else 1


print()
print("=== the three admissible roots, their classes and the complements r^perp in K_5")
res = {}
for lab in (12, 13, 14):
    r = ROOTS[lab - 1]
    assert ip(r, delta) == 0 and ip(r, eta) == 0 and ip(r, r) == -2, lab
    cc = class_coords(r)
    sq = int(cc * GK * cc)
    assert sq == -2, (lab, sq)
    phi = matrix(ZZ, 1, 10, [int(x) for x in (cc * GK)])
    Kc = phi.right_kernel_matrix()
    Kc = matrix(ZZ, Kc).saturation()
    assert Kc.nrows() == 9, Kc.nrows()
    Gc = matrix(ZZ, 9, 9, lambda i, j: int(vector(ZZ, Kc[i]) * GK * vector(ZZ, Kc[j])))
    ev = Gc.change_ring(RDF).eigenvalues()
    res[lab] = dict(det=Gc.det(), smith=[abs(x) for x in Gc.smith_form()[0].diagonal()],
                    sig=(sum(1 for x in ev if x > 1e-9), sum(1 for x in ev if x < -1e-9)),
                    even=all(Gc[i, i] % 2 == 0 for i in range(9)), coparity=disc_coparity(Gc),
                    coords=list(cc)[:3])
    d = res[lab]
    print("label %2d: class coordinates %s..., class square %d" % (lab, d["coords"], sq))
    print("        r^perp: rank 9, det %d, signature %s, Smith %s, even %s, coparity delta %d"
          % (d["det"], d["sig"], d["smith"], d["even"], d["coparity"]))

print()
print("=== the verdict of the invariants")
dets = {res[l]["det"] for l in res}
sigs = {res[l]["sig"] for l in res}
smiths = {tuple(res[l]["smith"]) for l in res}
cosm = {(res[l]["even"], res[l]["coparity"]) for l in res}
print("determinants        %s: all equal %s" % (sorted(dets), len(dets) == 1))
print("signatures          %s: all equal %s" % (sorted(sigs), len(sigs) == 1))
print("Smith invariants    %s: all equal %s" % (sorted(smiths), len(smiths) == 1))
print("(even, coparity)    %s: all equal %s" % (sorted(cosm), len(cosm) == 1))
print()
if len(dets) == 1 and len(sigs) == 1 and len(smiths) == 1 and len(cosm) == 1:
    print("The three complements share every invariant of an even 2-elementary lattice: rank 9,")
    print("determinant %d, signature %s, and coparity %d.  An indefinite even 2-elementary lattice"
          % (list(dets)[0], list(sigs)[0], list(cosm)[0][1]))
    print("is determined by its signature and the triple (r, a, delta) [@AEGS25, section 2.3, printed")
    print("p. 586; Nikulin], so the three complements are isometric.  Hence:")
    print("  * no invariant of the boundary lattice separates the three classes, and this record")
    print("    proves no inequivalence;")
    print("  * the Gamma_Co,2-orbits of the three classes are NOT computed here, and inequivalence")
    print("    remains open.")
else:
    print("The invariants differ, so the three roots lie in pairwise different Gamma_Co,2-orbits.")
print("elapsed %d s" % round(time.time() - t0))
print("PYEXIT=0")
