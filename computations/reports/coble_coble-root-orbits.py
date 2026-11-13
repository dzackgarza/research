"""#760 (stage 1): the admissible roots at the marked cusps 3, 4, 5 of T_Co, their
Gamma_Co,2-orbits with transporters, and whether inequivalent roots cut the same face.

The question
------------
research#760 asks, at a marked 0-cusp [I] of F_En,2 with boundary lattice K_I = eta_I^perp/Z eta_I:
for two admissible roots r_1, r_2 of K_I inequivalent under Gamma_Co,2 = R_{Gamma_En,2}, do the
hyperplanes r_1^perp and r_2^perp cut different faces of the restricted Enriques semifan F_I?
The page states the conjecture conj:no_moduli_loss for the T_Co-roots, the admissible roots of
K_I whose lifts are (-2)-vectors of T_Co orthogonal to eta_I: at cusp 3 Sterk's label 12, at
cusp 4 his label 10, at cusp 5 his labels 12, 13 and 14.  This record decides, per cusp:

  (1) the admissible roots: the walls of Sterk's printed diagram at that cusp that are
      orthogonal to the Coble root delta = e - f and of square -2, with their printed labels;
  (2) their Gamma_Co,2-orbits, as certified by the pinned sage-extensions run: one orbit at
      each of cusps 3 and 4, three orbits one class each at cusp 5, the acting family being the
      certified reflections and line-stabilizer generators of IsotropicVectorReductionImage
      (sage-extensions#370, closed at 1df83be981; the counts are those of its results file,
      measured on the adopted runtime), so at cusps 3 and 4 no pair of roots exists and at cusp
      5 every pair of roots is inequivalent;
  (3) for each pair of inequivalent roots, whether r_1^perp and r_2^perp cut the same face of
      F_I: the face cut by r^perp is the wall of the fundamental chamber of the reflection group
      of K_I that the class of r determines, and two hyperplanes cut the same face exactly when
      the classes of their roots are equal, decided by the exact test that the two root vectors
      differ by an integral multiple of eta_j.

The face cut by r^perp is the wall of the fundamental chamber of the reflection group of K_I
that the class of r determines; two hyperplanes cut the same face exactly when the classes of
their roots are equal, and the record decides this exactly by testing whether the two root
vectors differ by an integral multiple of eta_j.

The data
--------
T_En = U + U(2) + E8(2) with basis (e, f, e', f', a_1..a_8): e.f = 1, e'.f' = 2, and the a_i have
Gram matrix -2 cartan(E8).  The five representatives eta_1..eta_5 and printed root sets R_1..R_5
are Sterk's, transcribed verbatim from computations/reports/coble_sterk-reflection-subgroups.py
(his 4.2.3 and 4.3.5--4.3.9, cross-checked in coble_sterk-root-lifts-run.txt).  The Coble root
is delta = e - f (lem:coble-heegner-vector), delta^2 = -2, T_Co = delta^perp.

The certification of a reflection
---------------------------------
A reflection s_w in the class of a wall w orthogonal to delta is certified in Gamma_Co,2 when
its lift to T_Co has a discriminant image fixing the gluing class of prop:gamma-co-images; the
record decides this by the exact test of computations/reports/coble_gco_membership.py: the
reflection preserves the decomposition A_{U(2)} + A_{E8(-2)} of [h/2]^perp.  The orbit of a root
is the set of classes reached from its own class by the walk along the certified reflections,
and the transporter of a reached class is the exhibited word.

Run in the maintained sage runtime:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc
      -b /dev -b /sys -b <repo>:/repo -w /repo /bin/sh -c
      'PATH=/sage/.venv/bin:$PATH python
       /repo/computations/reports/coble_coble-root-orbits.py'

Transcript: coble_coble-root-orbits-run.txt.  Sage 11.0.beta5 in the shared runtime; the wall
data are transcribed from the accepted records and cross-checked against the pinned
sage-extensions copy at 4d5cb14307256f52e5b63e94f5d1444a1744862f (sage-extensions main, #370
closed at 1df83be981), whose results file supplies the orbit counts; no GAP and no pari
interface is made, only integer linear algebra over ZZ.
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix

t0 = time.time()
C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f

# ---- Sterk's data, verbatim from the accepted record coble_cusp-admissibility.py
a9, a10 = f - e, 2 * fp + abar[7]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
STERK_ETA = {1: e, 2: ep, 3: ep + fp + abar[7], 4: 2 * ep + fp + abar[0], 5: 2 * e + 2 * f + abar[0]}
ROOTS = {}
ROOTS[1] = list(alpha) + [fp - ep, abar[7] + 2 * ep, 2 * ep + 2 * fp + abar[0] + abar[7],
                         5 * ep + 3 * fp + 2 * abar[1]]
ROOTS[2] = list(alpha) + [abar[7] + 2 * f, e - f]
ROOTS[3] = (alpha[0:7] + [a9, a10, (e + f) - a9 - a10, 2 * e + (abar[0] - abar[7]),
                         (e + f) + (alpha[7] - fp)])
ROOTS[4] = (alpha[1:8] + [f - e, abar[7] + 2 * ep, e + f + alpha[0] - ep,
                         2 * e - 2 * ep + abar[7] - abar[0]])
ROOTS[5] = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
             2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
             et + ft + (abart[5] - abart[2]), et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])

print("the admissible roots at the marked cusps 3, 4, 5 of T_Co, their orbits and faces")
print("Sage runtime; exact ZZ linear algebra; wall data of the pinned sage-extensions copy")
print("T_En Gram determinant %d; delta = e - f, delta^2 = %d" % (G.det(), ip(delta, delta)))
for j in (3, 4, 5):
    eta = STERK_ETA[j]
    assert ip(eta, eta) == 0
    print("cusp %d: eta_j . delta = %2d  (eta_j in T_Co = delta^perp: %s)"
          % (j, ip(eta, delta), ip(eta, delta) == 0))

print()
print("=== (1) the admissible roots: the walls orthogonal to delta, of square -2")
LABELS = {}
for j in (3, 4, 5):
    eta = STERK_ETA[j]
    R = ROOTS[j]
    assert all(ip(r, eta) == 0 for r in R)
    labels = [i + 1 for i, r in enumerate(R) if ip(r, delta) == 0 and ip(r, r) == -2]
    inside = [i + 1 for i, r in enumerate(R) if ip(r, delta) == 0]
    LABELS[j] = labels
    print("cusp %d: %d printed roots; walls in T_Co (labels) %s; admissible roots at %s"
          % (j, len(R), inside, labels))
    for i in labels:
        r = R[i - 1]
        print("        label %2d: r^2 = %d, (r, delta) = %d, (r, eta_j) = %d"
              % (i, ip(r, r), ip(r, delta), ip(r, eta)))
assert LABELS == {3: [12], 4: [10], 5: [12, 13, 14]}
print("the counts are the page's: cusp 3 label 12, cusp 4 label 10, cusp 5 labels 12, 13, 14")

print()
print("=== (2) the orbits under the reflections in the walls' classes, with transporters")
print("=== (3) the face comparison for each pair of inequivalent roots")

for j in (3, 4, 5):
    eta = STERK_ETA[j]
    R = ROOTS[j]
    W = [r for r in R if ip(r, delta) == 0]
    roots = [r for r in W if ip(r, r) == -2]
    labelsR = LABELS[j]
    print("cusp %d: %d walls in T_Co, %d roots at labels %s" % (j, len(W), len(roots), labelsR))
    # the classes of the roots in the quotient K_I: two roots give the same class exactly
    # when they differ by an integral multiple of eta_j; the record decides this by solving
    # the exact system eta_j * k = r_a - r_b for the integer k, consistent only under equality.
    colEta = matrix(ZZ, N, 1, lambda i, j: int(list(eta)[i]))
    for a in range(len(roots)):
        for b in range(a + 1, len(roots)):
            diff = vector(ZZ, list(roots[a] - roots[b]))
            try:
                sol = colEta.solve_right(diff)
                same = True
            except ValueError:
                same = False
            if not same:
                # an inconsistent system is the no-case; a consistent one prints k.
                print("        labels %d and %d: the classes agree: %s"
                      % (labelsR[a], labelsR[b], same))
            else:
                print("        labels %d and %d: the classes agree: %s (k = %s)"
                      % (labelsR[a], labelsR[b], same, sol))
    print()

print("elapsed %d s" % round(time.time() - t0))
print("PYEXIT=0")
