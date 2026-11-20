"""#759: the call the pair (12,13) needs, and the one the library refuses to make.

The question
------------
Roots 13 and 14 at cusp 5 are one Gamma_Co,2-orbit, proved by the explicit isometry of
coble_759-lift-1314-run.txt.  The pair that survives is (12, 13): is there an integral
isometry g of T_En with g(delta) = +-delta, g(eta_5) = +-eta_5 and g(r12) = +-r13 mod eta_5?

The call, and its refusal
-------------------------
The natural formulation is a transporter constrained to fix the two vectors that define the
group: the family {r12, delta, eta_5} onto {r13, delta, eta_5}, under O(T_En).  That call is
refused, and the refusal names the hypothesis that excludes it:

    AssertionError: the vectors of Generic morphism:
      From: {0,...,2}
      To:   Integral lattice of rank 12 and signature (2, 10)
    span a rational subspace of rank 3 of Integral lattice of rank 12 and signature (2, 10),
    of rank 12, with pairing rank 2: this computation requires the full space or an isotropic
    hyperplane, whose pointwise orthogonal stabilizer is trivial

Why the hypothesis cannot be met for this instance
--------------------------------------------------
The transporter is computed by solving for an isometry on the family's span; uniqueness needs
that span to be the whole space, or an isotropic hyperplane with trivial pointwise stabilizer.
This pair needs the opposite: the family pins delta and eta_5, and every vector whose image is
unknown is precisely what must be left free.  A family that spans would have to prescribe those
images, and a prescribed spanning family admits only the identity.  So the pair cannot be posed
as a spanning-family transporter at all.

The subgroup alternative, and why it does not close the question
---------------------------------------------------------------
The subgroup-restricted verdict is IsotropicVectorReductionImage.root_class_orbits, whose
results document (sage-extensions results/issue370-the-coble-root-orbits.md) records three
singleton orbits at cusp 5 and states that a singleton is not a proof of inequivalence, the
acting family not being certified complete.  That incompleteness is visible here: the family
separates roots 13 and 14, which coble_759-lift-1314-run.txt proves equivalent.

What is missing
---------------
A transporter, or an orbit-equality decision, for a family whose pointwise orthogonal stabilizer
is nontrivial -- the case the assertion above excludes.  Neither O(T_En).transporter nor
root_class_orbits provides it, and no such method exists in the library at the pin read here.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH PYTHONPATH=/repo/.scratch/se-main/src \\
       /sage/.venv/bin/python /repo/computations/reports/coble_759-transporter-1213.py'

Transcript: coble_759-transporter-1213-run.txt.  The library pin is the sage-extensions checkout
at .scratch/se-main (cf6ba0b2), which carries the #370 and #312 work.
"""
import sys
sys.stdout.reconfigure(line_buffering=True)
from sage_extensions.all import NamedLattices, Sets
from sage.all import QQ, ZZ, matrix, vector, block_diagonal_matrix, CartanMatrix

L = NamedLattices.TEn
print("L = %s" % L)
LABELS = ("e", "f", "ep", "fp", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8")
gens = [L.module_generator(lab) for lab in LABELS]
def elem(coords):
    v = None
    for c, b in zip(coords, gens):
        if c:
            v = c * b if v is None else v + c * b
    return v

C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: int(vector(ZZ, at[i]) * G * vector(ZZ, at[j])))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta_c = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])
r12, r13 = elem([int(c) for c in ROOTS[11]]), elem([int(c) for c in ROOTS[12]])
delta, eta = elem([int(c) for c in (e - f)]), elem([int(c) for c in eta_c])
print("r12^2 = %s, r13^2 = %s, delta^2 = %s, eta^2 = %s"
      % (r12 * r12, r13 * r13, delta * delta, eta * eta))
print()
I = Sets.Δ[2]
def fam(a):
    return Sets().Mor(I, L)(lambda i: (a, delta, eta)[int(i)])
print("call: O(L).transporter({r12, delta, eta_5}, {r13, delta, eta_5})")
try:
    wit = L.O().transporter(fam(r12), fam(r13))
    print("returned: %r" % (wit,))
except Exception as exc:
    print("REFUSED: %s: %s" % (type(exc).__name__, exc))
print()
print("control: the stabilizer call on a family that does span is accepted")
J = Sets.Δ[15]
allv = [elem([int(c) for c in r]) for r in ROOTS] + [delta, eta]
try:
    st = L.O().stabilizer(Sets().Mor(J, L)(lambda i: allv[int(i)]))
    print("  stabilizer of the fourteen walls with delta and eta: %s" % st)
except Exception as exc:
    print("  REFUSED: %s: %s" % (type(exc).__name__, exc))
print()
print("VERDICT: the pair (12,13) can be posed only as a transporter whose pointwise orthogonal")
print("stabilizer is nontrivial, which the library's spanning hypothesis excludes; the subgroup")
print("alternative returns singleton orbits under a family it does not certify complete.")
print("PYEXIT=0")
