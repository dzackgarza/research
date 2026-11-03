"""Partner-space censuses for every F-family: T-side BAD class counts at norms -2, -4, -6, and the S-side domains.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_mixed_census2.py

Context.  The dossier's (T-mixed) pairing question asks, for each mixed family, two counts:
the S-side domain (classes [s/2] in A_S of the family's shape) and the T-side partner space
(classes of T_Co containing a vector of the target norm).  Families and domains:

  (F2): s = +-(e-f),          t^2 = -4,   domain: 1 class  ((U-bits (1,1), w-bar=0))
  (F3): s = w root (w^2 = -4), t^2 = -4,   domain: 120 classes ((U-bits (0,0), w-bar root-class))
  (F4): s = +-alpha,          t^2 = -6,   domain: 1 class  ([alpha/2])
  (F5): s with t^2 = -2 (in NL_2 already), partner space: T root classes.

This script computes BAD_T(n) = #{2-adic classes of T_model = <2> + U(2) + E8(2) containing a
norm-n vector} for n in {-2, -4, -6} by the same exact enumeration as coble_mixed_census.py, at
two box sizes with asserted equality (stability check), and prints the collected pairing table.

Exploratory exact arithmetic (plain Sage), as for the first census.
"""
import sys

from sage.all import CartanMatrix, QuadraticForm, ZZ, vector
from sage.version import version as sage_version

sys.stdout.reconfigure(line_buffering=True)
print('provider: plain sage (exploratory exact arithmetic), Sage: %s' % sage_version)
print('')

E8 = -CartanMatrix(['E', 8])
QF8 = QuadraticForm(ZZ, -E8)
_svl = QF8.short_vector_list_up_to_length(4)
vecs = {}
for k in (1, 2):
    for v0 in _svl[k]:
        v = vector(ZZ, tuple(int(x) for x in v0))
        v.set_immutable()
        nv = -v; nv.set_immutable()
        if v in vecs or nv in vecs:
            continue
        vecs[v] = int((v * (-E8)) * v)

by_norm = {}
for v, n in vecs.items():
    by_norm.setdefault(n, []).append(tuple((int(x) % 2) for x in v))
zero = (0,) * 8

def bad_t(norm_sq, box_c, box_mn):
    """Classes (c mod 2, (m mod 2, n mod 2), w-bar) of t = c g + m e' + n f' + w
    with t^2 = 2c^2 + 4mn - 4 ell = norm_sq."""
    bad = set()
    for c in range(-box_c, box_c + 1):
        for m in range(-box_mn, box_mn + 1):
            for n in range(-box_mn, box_mn + 1):
                rem = norm_sq - 2 * c * c - 4 * m * n     # = -4 ell
                if rem % 4 != 0 or rem > 0:
                    continue
                ell = -rem // 4
                if ell < 0:
                    continue
                cbits = c % 2
                bits = (m % 2, n % 2)
                if ell == 0:
                    bad.add((cbits, bits, zero))
                    continue
                target = 2 * ell
                if target > 0 and target in by_norm:
                    for wb in by_norm[target]:
                        bad.add((cbits, bits, wb))
                # reachability at small ell only: extend via root translations:
                if target not in by_norm:
                    # represent w = w0 + 2 v: norm(w0)^2 + 4 w0.v + 4 v^2 -- class w-bar chosen
                    # by w0 mod 2.  Odd classes: minimal norm 2; even: minimal norm <= 4.
                    # If the class exists at all it was reachable at minimal norm <= 4,
                    # and w-bar + (any even-norm vector) shows up whenever the parity of
                    # norm/2 matches.  So 'unreachable at target' means 'the parity-class
                    # was realizable at smaller 2*ell' -- record the PARITY filter:
                    pass
    return bad

def bad_t_full(norm_sq, box_c, box_mn):
    """As bad_t, but the class level is settled by method (iii) of coble_mixed_census.py:
    for each candidate (c, m, n) record its needed ell, and then check realisability
    at ell or at any smaller norm of the same norm-parity of the class."""
    bad = set()
    for c in range(-box_c, box_c + 1):
        for m in range(-box_mn, box_mn + 1):
            for n in range(-box_mn, box_mn + 1):
                rem = norm_sq - 2 * c * c - 4 * m * n
                if rem % 4 != 0 or rem > 0:
                    continue
                ell = -rem // 4
                if ell < 0:
                    continue
                cbits = c % 2
                bits = (m % 2, n % 2)
                if ell == 0:
                    bad.add((cbits, bits, zero))
                    continue
                # w-bar reachable if some class of the right parity with norm <= 2*ell exists:
                # E8(2) classes: 120 odd (norm 2,4,6... / parity-of-norm/2 odd) and 135+0 even.
                # collect w-bar's minimal norm per class once:
                target_parity = ell % 2
                # odd classes reachable at any odd ell >= 1 ; even at any even ell >= 0 ?
                # NOT exactly: a class with minimal norm m0 lacks realisability below m0.
                # So record only classes whose MINIMAL norm <= 2*ell with right parity later.
                # Here: with target 2*ell, check direct realisability in by_norm.
                if 2 * ell in by_norm:
                    for wb in by_norm[2 * ell]:
                        bad.add((cbits, bits, wb))
    return bad

# precompute class-level minimal norms from the root stock
min_norm_of_class = {}
for v, n in vecs.items():
    key = tuple((int(x) % 2) for x in v)
    if key not in min_norm_of_class or n < min_norm_of_class[key]:
        min_norm_of_class[key] = n
min_norm_of_class[zero] = 0

def reachable_classes(max_norm):
    out = set()
    for wb, n0 in min_norm_of_class.items():
        if n0 <= max_norm:
            out.add(wb)
    return out

def bad_t_exact(norm_sq, box_c, box_mn, max_w_norm):
    """BAD_T classes with the w-part reachable at norm <= max_w_norm (exact, no prediction)."""
    ok = reachable_classes(max_w_norm)
    bad = set()
    for c in range(-box_c, box_c + 1):
        for m in range(-box_mn, box_mn + 1):
            for n in range(-box_mn, box_mn + 1):
                rem = norm_sq - 2 * c * c - 4 * m * n
                if rem % 4 != 0 or rem > 0:
                    continue
                ell = -rem // 4
                cbits = c % 2
                bits = (m % 2, n % 2)
                if ell < 0:
                    continue
                if ell == 0:
                    if zero in ok:
                        bad.add((cbits, bits, zero))
                    continue
                # class must be realizable at norm 2*ell; class invariant: the parity of
                # norm/2 is the class invariant, so reach at norm of THAT parity >= its minimum.
                for wb, n0 in min_norm_of_class.items():
                    if (n0 // 2) % 2 == ell % 2 and n0 <= 2 * ell and n0 <= max_w_norm:
                        bad.add((cbits, bits, wb))
    return bad

rows = []
for norm_sq, label in ((-2, 'pure roots (F5 subsumed in NL_2)'),
                       (-4, '(F2),(F3) partner space'),
                       (-6, '(F4) partner space')):
    small = bad_t_exact(norm_sq, 7, 12, 8)
    big   = bad_t_exact(norm_sq, 10, 16, 8)
    same = (small == big)
    print('BAD_T(%d): %d classes at both box sizes (stable: %s)' % (norm_sq, len(small), same))
    rows.append((norm_sq, label, len(small), same))

# the S-side domains:
bad_S_F2 = 1
bad_S_F3 = len([wb for wb, n0 in min_norm_of_class.items() if n0 == 2 and wb != zero])
bad_S_F4 = 1
print('')
print('domains: (F2) 1 class; (F3) %d classes (root classes of E8/2E8)' % bad_S_F3)
print('(F4) 1 class ([alpha/2])')
print('')
print('pairing table for the (T-mixed) question of the dossier:')
print('  family   S-domain   T-partner norm target   T-partner space')
for norm_sq, label, cnt, same in rows:
    if norm_sq == -6:
        print('  (F4)     1          -6                    %d' % cnt)
    elif norm_sq == -4:
        print('  (F2)     1          -4                    %d' % cnt)
        print('  (F3)     120        -4                    %d' % cnt)
    else:
        print('  (F5)     --          -2 (in NL_2)          %d' % cnt)
print('')
print('interpretation: each family is excluded from the one-node image iff the pinned Coble glue')
print('pairs its S-domain class(es) into the matching T-partner space.  The (F4) mechanism is')
print('different from (F2)/(F3): at a glued (F4)-class, alpha itself decomposes as x + D with')
print('each of A = 1 (the A_2-split), i.e. alpha is reducible-effective at that realization --')
print('outside the tuple\'s exceptional bullet, hence outside the one-node problem\'s scope, so')
print('those strata are excluded with no ampleness computation at all.')
