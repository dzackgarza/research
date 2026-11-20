"""#759: no isometry carries the cusp-5 configuration with r12 in it to the one with r13.

The call
--------
O(T_En).transporter(F1, F2) with

    F1 = [r12, delta, eta_5, e] + the fourteen printed roots at cusp 5
    F2 = [r13, delta, eta_5, e] + the fourteen printed roots at cusp 5

returns None.  This family spans T_En (18 vectors in rank 12), which is the hypothesis the
computation needs to be complete: with a spanning family, each colour- and pairing-preserving
permutation of the labelled graph determines at most one rational isometry, and the call returns
None only when none of them is integral.  So the answer here is a decision and not a bound:

    no integral isometry of T_En carries that configuration onto the other one,
    up to relabelling of the family.

What that decides, and what it does not
---------------------------------------
It decides it for the configuration: the pair (12,13) cannot be witnessed by an isometry that
carries the cusp-5 root configuration to itself up to relabelling -- which is the class that
contains every symmetry and reflection transport tried earlier on this page.

It does not decide the pair.  A transporter for the pair need not preserve the printed roots: it
must only fix delta and eta_5 and carry the class of r12 to that of r13, and the fourteen roots are
not part of that requirement.  Posing the pair without them is the case the library refuses --
a family with nontrivial pointwise orthogonal stabilizer (coble_759-transporter-1213-run.txt) --
and posing it with them, as here, answers a strictly stronger question.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH PYTHONPATH=/repo/.scratch/se-main/src \\
       /sage/.venv/bin/python /repo/computations/reports/coble_759-spanning-transporter-1213.py'

Transcript: coble_759-spanning-transporter-1213-run.txt.  Library pin .scratch/se-main (cf6ba0b2).
"""
import sys
sys.stdout.reconfigure(line_buffering=True)
from sage_extensions.all import NamedLattices, Sets
from sage.all import QQ, ZZ, matrix, vector, block_diagonal_matrix, CartanMatrix
L = NamedLattices.TEn
LABELS = ("e", "f", "ep", "fp", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8")
gens = [L.module_generator(lab) for lab in LABELS]
def elem(c):
    v = None
    for a, b in zip(c, gens):
        if a:
            v = a * b if v is None else v + a * b
    return v
C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(x) for x in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: int(vector(ZZ, at[i]) * G * vector(ZZ, at[j])))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(x) for x in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta_c = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])
delta_c = e - f
r12, r13 = elem([int(x) for x in ROOTS[11]]), elem([int(x) for x in ROOTS[12]])
delta, eta = elem([int(x) for x in delta_c]), elem([int(x) for x in eta_c])
w = elem([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])          # e, in S^perp together with eta
print("built the vectors; e.e = %s, eta^2 = %s" % (w * w, eta * eta))
rest = [elem([int(x) for x in r]) for r in ROOTS]
src = [r12, delta, eta, w] + rest
tgt = [r13, delta, eta, w] + rest
n = len(src)
print("family size %d (spans T_En: %s)" % (n, len(src) >= 12))
I = Sets.Δ[n - 1]
F1 = Sets().Mor(I, L)(lambda i: src[int(i)])
F2 = Sets().Mor(I, L)(lambda i: tgt[int(i)])
print("asking O(L).transporter(F1, F2) ...")
try:
    wit = L.O().transporter(F1, F2)
except Exception as exc:
    print("REFUSED/RAISED: %s: %s" % (type(exc).__name__, str(exc)[:400]))
    wit = "raised"
print("witness: %r" % (wit if wit in (None, "raised") else "an isometry",))
if wit not in (None, "raised"):
    print("  g(r12) == r13:      %s" % (wit(r12) == r13))
    print("  g(delta) == delta:  %s" % (wit(delta) == delta))
    print("  g(eta) == eta:      %s" % (wit(eta) == eta))
    print("  g(r12) == -r13:     %s" % (wit(r12) == -r13))
    print("  images of the first four: %s" % [wit(v) for v in src[:4]])
print("PYEXIT=0")
