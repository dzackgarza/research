"""#654 step (iv), plane half: the orbits of Stab_{O(q)}([h/2]) on the plane classes of A_{T_En}.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
    PYTHONPATH=/repo/.scratch/se-provider-15db925b/src \\
    .scratch/udocker_dir/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_TEn-gammaEn2-planes.py

The plane classes are the order-4 totally isotropic subgroups of A_{T_En} that are images of primitive
isotropic planes of T_En; on A_{T_En} = (Z/2)^10 they are the 2-dimensional totally singular
subspaces, and over F_2 a 2-space spanned by u, v is totally singular exactly when u, v and u+v are
isotropic (the bilinear form is then q(u)+q(v)+q(u+v) = 0 automatically).

NOT RUN.  The vector half came out at 2 H-orbits against the published 5, and the rule for this
step is to stop and report when the rho-side count falls below the published one; the plane walk is
therefore kept ready but has no transcript.  The number it would decide is the number of
Gamma_En,2-orbits of primitive isotropic planes, which AEGS 2025, section 3.3, p. 590 states as nine.

The group this script would have to act with is Gamma_En,2, and the generators exported by the
vector half belong to Stab_{O(q_T)}([h/2]), which is 136 times larger and is not Gamma_En,2 (see the
correction in coble_TEn-gammaEn2-orbits-run.txt).  So this script is not runnable as it stands: it
needs the nine additive generators of im(Stab_{O(S_En)}(h)) for the correct group, which
coble_gammaEn2-card.py builds, and it needs the primitive isotropic planes of T_En stratified by
their image in A_{T_En} -- dimension 0, 1 and 2 -- of which only the 2-dimensional stratum is a
finite-form datum.  On that stratum the group has 5 orbits of the 23715 totally singular 2-spaces
(coble_gammaEn2-card-run.txt), against the published 9 one-cusps; the two lower strata are the
lattice-level part of the obligation.  It
loads the export, checks that its matrices preserve the quadratic form and that they generate a group
of the recorded order |H|, and then walks the plane classes under them.  The count is printed beside
the published 9: AEGS 2025, section 3.3, p. 590, "There are five 0-cusps ... There are also 9 distinct
1-cusps", the 1-cusps being in bijection with the primitive isotropic planes of T_En modulo the
group.  As in the vector half, the rho-side count is a lower bound for the Gamma_En,2 count.

Transcript: `coble_TEn-gammaEn2-planes-run.txt`.
"""
import itertools
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, libgap, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

EXPORT = '/repo/computations/reports/coble_TEn-gammaEn2-orbits-generators.txt'
PUBLISHED = 9          # AEGS 2025, section 3.3, p. 590: nine distinct 1-cusps

print('provenance\n  Sage: %s\n  sage-extensions pin 15db925b\n' % SAGE_VERSION)
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
A = T.discriminant_quadratic_form()
els = list(A.elements())
iso = list(A.isotropic_elements())
print('|A| = %d, isotropic classes %d' % (int(A.cardinality()), len(iso)))

# the same coordinate basis as the vector half, by the same deterministic loop
zero = els[0]
basis, coord = [], {zero: 0}
for e in els:
    if e in coord:
        continue
    shift = len(basis)
    coord.update({s + e: m | (1 << shift) for s, m in coord.items()})
    basis.append(e)
    if len(basis) == 10:
        break
assert len(basis) == 10 and len(coord) == 1024
element_at = {m: e for e, m in coord.items()}
print('coordinate basis of A rebuilt: 10 classes, all %d elements labelled' % len(coord))

# ---------------------------------------------------------------- the exported generators of H
lines = [line for line in open(EXPORT).read().splitlines() if line.strip()]
header = [line for line in lines if line.startswith('#')]
data = [[int(x) for x in line.split()] for line in lines if not line.startswith('#')]
recorded_order = int([line for line in header if '|H|' in line][0].split('|H| = ')[1].split(',')[0])
mats = [tuple(row) for row in data]
print('loaded %d matrices of H from %s' % (len(mats), EXPORT))
print('  recorded |H| = %d, recorded pin line: %s'
      % (recorded_order, [line for line in header if 'pin' in line][0].lstrip('# ')))


def act(cols, x):
    """Act by a matrix given its column bit masks on the coordinate vector x."""
    out, i = 0, 0
    while x:
        if x & 1:
            out ^= cols[i]
        x >>= 1
        i += 1
    return out


# the loaded matrices must be isometries, and must generate all of H
start = time.time()
probe = els[::29][:36]
checked = 0
for cols in mats[::max(1, len(mats) // 40)]:
    for x in probe:
        assert A.q(element_at[act(cols, coord[x])]) == A.q(x), 'a loaded matrix does not preserve q'
        checked += 1
print('check: q preserved by %d loaded matrices on %d classes (%d tests)   (%.0f s)'
      % (len(mats[::max(1, len(mats) // 40)]), len(probe), checked, time.time() - start))

start = time.time()
perms = [libgap.PermList([act(cols, x) + 1 for x in range(1024)]) for cols in mats]
order = int(libgap.Size(libgap.Group(perms)))
print('check: the %d matrices generate a group of order %d in Sym(1024)   (%.0f s)'
      % (len(mats), order, time.time() - start))
assert order == recorded_order, (order, recorded_order)

# A certified small generating set: a random subset whose generated order is the whole |H|.  The
# certificate is that order, not the sampling.
import random  # noqa: E402
random.seed(20261107)
chosen = None
for count in (8, 16, 32, 64, 128, len(mats)):
    if count > len(mats):
        continue
    idx = sorted(random.sample(range(len(mats)), count))
    if int(libgap.Size(libgap.Group([perms[i] for i in idx]))) == recorded_order:
        chosen = idx
        print('  a random subset of %d of the %d generators already generates all of H' % (count, len(mats)))
        break
assert chosen is not None, 'no sampled subset generated all of H'
walk_perms = [[int(p) for p in libgap.ListPerm(perms[i], 1024)] for i in chosen]
assert all(sorted(p) == list(range(1, 1025)) for p in walk_perms), 'a recovered permutation is not bijective'

# ---------------------------------------------------------------- the totally singular 2-spaces
iso_coord = {coord[e] for e in iso}
target = iso_coord - {0}
start = time.time()
planes = set()
for u, v in itertools.combinations(sorted(target), 2):
    w = u ^ v
    if w in iso_coord:
        planes.add(tuple(sorted((u, v, w))))
print('totally singular 2-spaces: %d   (%.0f s)' % (len(planes), time.time() - start))
print('  each is {u, v, u+v} with all three isotropic; the bilinear form then vanishes too')

# ---------------------------------------------------------------- the walk on the plane classes
start = time.time()
seen, orbits = set(), []
for seed in sorted(planes):
    if seed in seen:
        continue
    orbit, frontier = {seed}, [seed]
    seen.add(seed)
    while frontier:
        plane = frontier.pop()
        a, b, _ = plane
        for perm in walk_perms:
            ia, ib = perm[a] - 1, perm[b] - 1
            image = tuple(sorted((ia, ib, ia ^ ib)))
            if image not in orbit:
                orbit.add(image)
                seen.add(image)
                frontier.append(image)
    assert orbit <= planes, 'the walk left the totally singular 2-spaces'
    orbits.append(orbit)
sizes = sorted((len(o) for o in orbits), reverse=True)
print('the walk with %d of the generators: %d orbits, sizes %s   (%.0f s)'
      % (len(walk_perms), len(orbits), sizes, time.time() - start))
print('  sum of the orbit sizes: %d of %d' % (sum(sizes), len(planes)))
assert sum(sizes) == len(planes) and len(seen) == len(planes)
print('')

print('THE NUMBER')
print('  H-orbits on the totally singular 2-spaces of A_{T_En}: %d' % len(orbits))
print('  published (AEGS 2025, section 3.3, p. 590: nine distinct 1-cusps): %d' % PUBLISHED)
print('')
if len(orbits) == PUBLISHED:
    print('AGREES with the published count, and the fibres over the rho-double-cosets are single')
    print('points on this side as they are on the vector side.')
else:
    print('DOES NOT agree with the published count.  The rho-side count is a lower bound for the')
    print('Gamma_En,2 count of primitive isotropic planes; the shortfall is the fibre defect, and the')
    print('lattice-side count is what decides it.')
