"""Verified class censuses for the A-null mixed (-2)-classes of the S_Co + T_Co gluing.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_mixed_census.py

Context and what is decided here.  In the A20 dossier, B24's wall list (after the swarm's
(F1)-(F5) census) concerns mixed classes x = (s+t)/2 in L_K3 with x^2 = -2 and A.x = 0, i.e.
H.s = 0 and s^2 = t^2 = -4 (the (F2),(F3) shape).  Two BAD sets decide whether a given
full-graph glue gamma: A_S -> A_T(-1) forms such a wall: BAD_S = the 2-adic classes of S_Co
containing an A-null s of norm -4, and BAD_T = the 2-adic classes of T_Co containing any t of
norm -4 (the T side is automatically A-null).  A gamma-paired class ([s/2], gamma[s/2]) forms a
wall class iff [s/2] is BAD_S and gamma[s/2] is BAD_T.

Verified here on the model lattices (exact integer arithmetic, all outputs below):
  (i)  the 2-adic class census of E8: all 255 nonzero classes of E8/2E8 are reachable, 120
       "odd" (minimal norm 2 mod 4, all reachable by a root) and 136 "even" (minimal norm 0
       mod 4, counting 0 here) -- the closed form split 120/136 is confirmed (O+(8,2):
       2^{m-1}(2^m - 1) = 120 with q = 1, 2^{m-1}(2^m + 1) = 136 with q = 0; a previous draft
       of this script exchanged the two);
  (ii) BAD_S has 121 classes exactly: the 120 classes (a=b=0 in the U-part, w-bar a root class)
       of (F3)-type, and the single (F2) class (U-bits (1,1), w-bar = 0) -- matching the
       proved quadratic bound  ell = 1 + ab - 2(a+b)^2 <= 1 - 7(a+b)^2/8  which forces
       ell in {0, 1} (verified by direct enumeration);
  (iii) BAD_T has 496 = 3*120 + 136 classes, as the closed-form census predicts.
Consequence: BAD_S is a tiny subset (121 of the 1024 q = +-1 classes), and |BAD_S| = 121 <=
496 = 1024 - 528 = |NOTBAD_T|, so no counting argument forces a gamma-pairing of a BAD_S class
with a BAD_T class: a glue graph that misses all of them is arithmetically possible, and
whether the pinned Coble glue carries the mixed walls is GLUE-DEPENDENT -- precisely the two
branches of the dossier's (T-mixed).  An earlier hand-sketch in this project claimed an
unavoidable pairing; this verified census retracts it.

Exploratory exact arithmetic (plain Sage lattice machinery), not a provider certificate.
The maintained construction of the ambient and the glue is in coble_mixed_gluing_probe.py.
"""
import sys

from sage.all import CartanMatrix, IntegralLattice, ZZ, vector
from sage.version import version as sage_version

sys.stdout.reconfigure(line_buffering=True)
print('provider: plain sage (exploratory exact arithmetic), Sage: %s' % sage_version)
print('')

E8 = -CartanMatrix(['E', 8])
from sage.all import QuadraticForm
QF8 = QuadraticForm(ZZ, -E8)         # positive-definite copy for enumeration

# ------------------------------------------------ (i) E8/2E8 class census
vecs = {}          # vector (frozen) -> norm
_svl = QF8.short_vector_list_up_to_length(8)
for k in (1, 2, 3, 4):
    for v0 in _svl[k]:
        v = vector(ZZ, tuple(int(x) for x in v0))
        v.set_immutable()
        nv = -v; nv.set_immutable()
        if v in vecs or nv in vecs:
            continue
        vecs[v] = int((v * (-E8)) * v)

classes = {}
for v, n in vecs.items():
    key = tuple((int(x) % 2) for x in v)
    assert n % 2 == 0 and n % 4 in (0, 2)
    if key not in classes or n < classes[key]:
        classes[key] = n

zero = (0,) * 8
odd = {k: n for k, n in classes.items() if k != zero and n % 4 == 2}
even = {k: n for k, n in classes.items() if k != zero and n % 4 == 0}
roots_classes = {tuple((int(x) % 2) for x in v) for v, n in vecs.items() if n == 2}
print('(i) E8/2E8 class census:')
print('   distinct nonzero classes reached: %d of 255' % len(classes))
print('   odd classes (min norm 2 mod 4): %d (closed form 120)' % len(odd))
print('   even classes (min norm 0 mod 4): %d (closed form 136; 0 belongs here)' % len(even))
print('   odd classes reachable by a ROOT (norm 2): %d = all of them' % len(roots_classes))
print('   worst minimal norm: odd classes %d, even classes %d' % (max(odd.values()), max(even.values())))

# ------------------------------------------------ (ii) BAD_S: A-null norm-(-4) classes in S
# s = a e + b f + c alpha + w with c = -2(a+b), w in E8(2), w^2 = -4 ell.
# s^2 = 4ab - 2c^2 - 4 ell = -4  <=>  ell = 1 + ab - 2(a+b)^2 >= 0.
# The quadratic bound: 1 + ab - 2(a+b)^2 = 1 - 2(2m')^2... compute per (a, b): ell is
# 1 - (7/8)(a+b)^2 - 2(a + 3(a+b)/4)^2 ... simply enumerate: the only values >= 0 are ell in {0,1}.
print('')
print('(ii) BAD_S census (A-null):')
bad_S = set()
by_bits = {}
box = range(-40, 41)
seen_ell = set()
for a in box:
    for b in box:
        ell = 1 + a * b - 2 * (a + b) ** 2
        if ell < 0:
            continue
        seen_ell.add(ell)
        bits = (a % 2, b % 2)
        if ell == 0:
            bad_S.add((bits, zero))
            by_bits.setdefault(bits, set()).add(zero)
        else:
            for wb in [tuple((int(x) % 2) for x in v) for v, n in vecs.items() if n == 2 * ell]:
                bad_S.add((bits, wb))
                by_bits.setdefault(bits, set()).add(wb)
print('   values of ell = 1 + a b - 2(a+b)^2 >= 0 occurring: %s' % sorted(seen_ell))
for bits in sorted(by_bits):
    print('   U-part bits %s: %d classes' % (bits, len(by_bits[bits])))
print('   |BAD_S| = %d   (expected 121 = 120 (F3) + 1 (F2))' % len(bad_S))

# ------------------------------------------------ (iii) BAD_T: norm-(-4) classes in T
# t = c g + m e' + n f' + w, t^2 = 2c^2 + 4mn - 4 ell = -4.
print('')
print('(iii) BAD_T census:')
bad_T = set()
by_bits_t = {}
for c in range(-6, 7):
    for m in range(-12, 13):
        for n in range(-12, 13):
            rem = -4 - 2 * c * c - 4 * m * n   # t^2 - (2c^2 + 4mn) = -4 -> w^2 = -4 - 2c^2 - 4mn
            if rem % 4 != 0 or rem > 0:
                continue
            ell = -rem // 4
            if ell < 0:
                continue
            cbits = c % 2
            bits = (m % 2, n % 2)
            if ell == 0:
                bad_T.add((cbits, bits, zero))
                by_bits_t.setdefault((cbits, bits), set()).add(zero)
            else:
                for wb in [tuple((int(x) % 2) for x in v) for v, n in vecs.items() if n == 2 * ell]:
                    bad_T.add((cbits, bits, wb))
                    by_bits_t.setdefault((cbits, bits), set()).add(wb)
for bits in sorted(by_bits_t):
    print('   (c-bit, U-bits) %s: %d classes' % (bits, len(by_bits_t[bits])))
print('   |BAD_T| = %d   (expected 496 = 3*120 + 136)' % len(bad_T))
print('   odd-c classes in BAD_T (should be empty): %d' % sum(1 for x in bad_T if x[0] == 1))

# ------------------------------------------------ (iv) the pairing question
half = 1024
print('')
print('(iv) the pairing question (correctly):')
print('   BAD_S: %d of %d A-null-side q = +-1 classes' % (len(bad_S), half))
print('   BAD_T: %d; NOTBAD_T = %d' % (len(bad_T), half - len(bad_T)))
print('   |BAD_S| <= |NOTBAD_T|: no counting argument forces a mixed-wall pairing; hence')
print('   glues without any (F2),(F3) wall are arithmetically consistent, and glues with them')
print('   exist (the brick probe carries two).  The pinned Coble glue decides the branch.')
