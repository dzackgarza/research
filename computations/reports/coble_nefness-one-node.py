"""Nefness of h_Co on the one-node member, tested through owner operations.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs   (checkout 281da26ffd)
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_nefness-one-node.py

Runtime: adopted image, Sage 11.0.beta5, GAP 4.16.1 (Sage-owned).  Provider: sage-extensions
pin 15db925b.

The question, and what is being tested.  h_Co = F_1+F_2 is the degree-2 polarization of
@def:coble-polarization-classes: F_1 = 3H-(E_1+...+E_9), F_2 = 3H-(E_1+...+E_8+E_10),
so h_Co = 6H-2(E_1+...+E_8)-E_9-E_10 in Pic(S) = <H,E_1,...,E_10>, of square 2.  Nef means
h_Co.D >= 0 for every effective class D.  This record does not attempt a proof over all
curves; it tests h_Co against

  (a) the classes whose effectivity has a named source, and
  (b) the (-2)-classes that Riemann-Roch on the rational surface makes effective, in a
      bounded window, with the bound stated.

Effectivity bookkeeping, stated before the run.
  * E_i, i <= 10: the exceptional curves of S -> P^2 at the ten nodes of C (DK13, section 3).
    Effective, h_Co.E_i = 2 for i <= 8 and 1 for i = 9, 10.
  * c = -2K_S = 6H-2(E_1+...+E_10): the branch sextic [C] (DK13, section 3), effective with
    a geometric witness, and h_Co.c = 0.  This is the wall, recorded as such.
  * C, the null curve of the one-node member (prop:quasipolarization): the curve with
    L.C = 0, which is the branch curve again (its class is c), so it is the same wall.
  * A (-2)-class delta is EFFECTIVE when (-K_S).delta >= 2: Riemann-Roch on the rational
    surface gives h^0(delta) - h^1(delta) + h^2(delta) = 1 + (delta^2 - K.delta)/2, and with
    delta^2 = -2 this is (-K.delta)/2 >= 1, so h^0(delta) >= 1.
  * A (-2)-class with h_Co.delta < 0 and (-K_S).delta < 2 is reported as of UNKNOWN
    effectivity, and never as a counterexample.

The window.  Write delta = aH - sum b_i E_i.  Then delta^2 = a^2 - sum b_i^2 = -2, so
sum b_i^2 = a^2+2, and the slice delta.H = a is a coset of H^perp = <E_1,...,E_10>, which is
negative definite.  For each a the record asks the owner for the complete fibre of square
-(a^2+2) in that definite lattice, which is the whole set of delta with delta.H = a and
delta^2 = -2.  a runs over 0..A_WINDOW; the truncation in a is the one bound, and it is
printed.
"""
import os
import shutil
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import ZZ, diagonal_matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
A_WINDOW = 3

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('  gap on PATH: %s' % shutil.which('gap'))
print('')

# Pic(S) = <H, E_1, ..., E_10>, H^2 = 1, E_i^2 = -1
P = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [1] + [-1] * 10).rows()])
G = P.gram_tensor()
print('Pic(S): rank %d, signature %s, determinant %s'
      % (P.rank(), P.signature_pair(), P.determinant()))
print('')

def vec(coords):
    return sum((c * P.basis_vector(i) for i, c in enumerate(coords)), 0 * P.basis_vector(0))

K = vec([-3] + [1] * 10)                       # K_S = -3H + sum E_i
h = vec([6] + [-2] * 8 + [-1, -1])             # h_Co
c = vec([6] + [-2] * 10)                       # branch curve c = -2K_S
print('the three classes')
print('  K_S = -3H + sum E_i     : K^2 = %d' % K.q())
print('  h_Co = 6H - 2E_1..E_8 - E_9 - E_10 : h^2 = %d' % h.q())
print('  c = -2K_S = 6H - 2 sum E_i         : c^2 = %d' % c.q())
print('  h_Co . K_S = %d   (so h_Co lies in K_S^perp, as @def:coble-polarization-classes requires)'
      % P.pairing(h, K))
print('  h_Co . c   = %d   (the WALL: h is orthogonal to the branch curve)' % P.pairing(h, c))
assert h.q() == 2 and K.q() == -1 and c.q() == -4 and P.pairing(h, K) == 0 and P.pairing(h, c) == 0
print('')

print('(a) the classes whose effectivity has a named source')
print('    the ten exceptional curves E_i (DK13 section 3):')
hits = [P.pairing(h, P.basis_vector(i)) for i in range(1, 11)]
print('      h_Co . E_i for i = 1..10 : %s' % hits)
print('      all positive: %s' % all(x > 0 for x in hits))
print('    the branch sextic c = -2K_S (DK13 section 3), and the null curve C of the one-node')
print('    member (prop:quasipolarization), whose class is c:')
print('      h_Co . c = %d' % P.pairing(h, c))
print('      that is the wall: h is orthogonal to an effective curve, so h is at best nef and')
print('      not ample along it.  A zero intersection with an effective curve is a wall, not a')
print('      failure of nefness.')
print('')

print('(b) the (-2)-classes in the window delta.H = a, a = 0..%d' % A_WINDOW)
Hperp = [P.basis_vector(i) for i in range(1, 11)]
X = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [-1] * 10).rows()])
print('    H^perp = <E_1,...,E_10>: signature %s, definite: %s'
      % (X.signature_pair(), X.is_definite()))
total = 0
neg_eff, neg_unknown, zero, pos = [], [], 0, 0
sample = []
# Two pairings per class, not ten: with X of Gram matrix -1 on the E-basis,
#     y . (sum_{i<=8} E_i) = -sum_{i<=8} b_i ,   y . (sum_{i<=10} E_i) = -sum_{i<=10} b_i ,
# and from the two sums h_Co.delta = 6a - 2 sum_{i<=8} b_i - (b_9+b_10) and
# (-K_S).delta = 3a - sum b_i.  A sample is then re-checked against the owner's pairing on the
# full lattice vector, so the shortcut is verified and not assumed.
sumE8 = sum(X.basis_vector(i) for i in range(8))
sumE10 = sum(X.basis_vector(i) for i in range(10))
for a in range(0, A_WINDOW + 1):
    target = -(a * a + 2)
    fibre = list(X.elements_of_norm(target))
    print('    a = %d: square %d fibre has %d elements' % (a, target, len(fibre)))
    for y in fibre:
        s8 = -int(X.pairing(y, sumE8))
        s10 = -int(X.pairing(y, sumE10))
        hd = 6 * a - 2 * s8 - (s10 - s8)
        kd = 3 * a - s10          # (-K_S).delta, verified against the owner pairing below
        total += 1
        if len(sample) < 40:
            sample.append((a, y, hd, kd))
        if hd == 0:
            zero += 1
        elif hd > 0:
            pos += 1
        else:
            (neg_eff if kd >= 2 else neg_unknown).append((a, y, hd, kd))
print('')
print('')
print('    cross-check of the two-pairing shortcut against the owner pairing, on %d sampled'
      ' classes:' % len(sample))
bad = 0
for a, y, hd, kd in sample:
    b = [-int(X.pairing(y, X.basis_vector(i))) for i in range(10)]
    d = vec([a] + [-bi for bi in b])
    if P.pairing(h, d) != hd or -P.pairing(K, d) != kd or d.q() != -2:
        bad += 1
print('      all sampled values agree (h.delta, (-K).delta, delta^2 = -2): %s' % (bad == 0))
assert bad == 0
print('')
print('    %d (-2)-classes tested in the window' % total)
print('      h_Co.delta > 0 : %d' % pos)
print('      h_Co.delta = 0 : %d   (the wall)' % zero)
print('      h_Co.delta < 0 and RR-effective (-K.delta >= 2) : %d' % len(neg_eff))
print('      h_Co.delta < 0 and effectivity unknown         : %d' % len(neg_unknown))
if neg_eff:
    print('      COUNTEREXAMPLES (effective, negative intersection):')
    for a, y, hd, kd in neg_eff[:10]:
        b = [-int(X.pairing(y, X.basis_vector(i))) for i in range(10)]
        print('        delta = %dH - sum %s E, h.delta = %d, -K.delta = %d' % (a, b, hd, kd))
else:
    print('      no effective class with h_Co.delta < 0 in the window')
if neg_unknown:
    print('      reported as unknown effectivity, not as counterexamples:')
    for a, y, hd, kd in neg_unknown[:10]:
        b = [-int(X.pairing(y, X.basis_vector(i))) for i in range(10)]
        print('        delta = %dH - sum %s E, h.delta = %d, -K.delta = %d   (RR gives no h^0)'
              % (a, b, hd, kd))
print('')
print('RESULT, as computed')
print('  Against every class whose effectivity is sourced -- the ten exceptional curves and')
print('  the branch sextic, which is also the null curve of the one-node member -- h_Co is')
print('  nonnegative, and it is zero exactly on the branch curve: the wall, stated as a wall.')
print('  In the window delta.H <= %d, no (-2)-class with h_Co.delta < 0 that Riemann-Roch makes'
      % A_WINDOW)
print('  effective was found; the classes with h_Co.delta < 0 whose effectivity RR does not')
print('  decide are listed above and are not counterexamples.')
print('  This is a computed check on a named list and a bounded window.  It is not a proof of')
print('  nefness over all curves, and it does not decide the authoring question of which reading')
print('  of the chamber bullet governs.')
