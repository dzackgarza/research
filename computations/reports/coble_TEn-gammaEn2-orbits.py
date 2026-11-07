"""#654 step (iv): the Gamma_En,2-orbits of primitive isotropic vectors, rho-side count.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
    PYTHONPATH=/repo/.scratch/se-provider-15db925b/src \\
    .scratch/udocker_dir/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_TEn-gammaEn2-orbits.py

Gamma_En,2 = Stab_{O(T_En)}(h) with h = e + f in U(2) (slots 2-3), h^2 = 4, div(h) = 2, so its class
c = [h/2] has q = 1.  rho is onto O(q), so rho(Gamma_En,2) = Stab_{O(q)}(c), of order
|O(q)|/496 = 94 755 225 600.  Let H denote that subgroup.

The count computed here is the number of H-orbits on the isotropic classes of A_{T_En} = (Z/2)^10
other than zero.  It is a LOWER BOUND for the Gamma_En,2-orbit count of primitive isotropic vectors,
equal only when the fibres over the rho-double-cosets are single points -- which holds for Gamma_Co
(it contains ker rho) but not automatically here, since ker rho is not inside Stab(h).

How the orbits are computed, and why not by the provider's orbit call.  `A.orbits(group=H)` does not
walk the point set: it builds the represented G-set `FiniteGSets(H)(A.elements(), action)`, whose
constructor validates point closure by evaluating every generator at every one of the 1024 classes,
and whose `_orbit_labels` then builds the permutation representation G -> Sym(1024) the same way --
two million category-level element actions -- before GAP sees the generator images; that call ran for
over two hours without terminating.  The action here is therefore the closure of the 527 nonzero
isotropic classes under the generators of H directly, and to make the walk a walk in microseconds
each generator is first written as its 10 x 10 matrix over F_2 on a coordinate basis of A (ten
applications of the generator, then linear algebra on bit masks).  The matrices are exported to
`coble_TEn-gammaEn2-orbits-generators.txt` for the plane half, which walks the same group the same
way; both exports are verified against the provider's action on samples, below.

Run at pin 15db925b: |O(q)| in 36 s, H = G.stabilizer_of_element(c) in about 2190 s, the rest in
seconds.  Transcript: `coble_TEn-gammaEn2-orbits-run.txt`.
"""
import itertools
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

EXPORT = '/repo/computations/reports/coble_TEn-gammaEn2-orbits-generators.txt'
PUBLISHED = 5          # AEGS 2025, section 3.3, p. 590: "There are five 0-cusps ... 9 distinct 1-cusps"

print('provenance\n  Sage: %s\n  sage-extensions pin 15db925b\n' % SAGE_VERSION)
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
G_T = block_diagonal_matrix(U, 2 * U, 2 * E8)
T = Lattices(ZZ)([list(r) for r in G_T.rows()])
print('T_En: rank %d, det %s, signature %s' % (T.rank(), T.determinant(), T.signature_pair()))
h = T.basis_vector(2) + T.basis_vector(3)
print('h = slot2 + slot3: square %s, divisibility %s' % (h.q(), T.div(h)))
A = T.discriminant_quadratic_form()
els = list(A.elements())
iso = list(A.isotropic_elements())
print('|A| = %d, isotropic classes %d' % (int(A.cardinality()), len(iso)))
c = T.discriminant_class(T.primitive_dual(h))
print('c = [h/2]: q = %s' % A.q(c))
start = time.time()
G = A.orthogonal_group()
print('|O(q)| = %d   (%.0f s)' % (int(G.order()), time.time() - start))
print('H = G.stabilizer_of_element(c)  -- the expensive step')
start = time.time()
H = G.stabilizer_of_element(c)
print('|H| = %d   (%.0f s); expected |O(q)|/496 = %d'
      % (int(H.order()), time.time() - start, 46998591897600 // 496))
start = time.time()
Hp = G.subgroup_on(list(H.group_generators()))
gens = list(Hp.group_generators())
print("H' built   (%.0f s), generators %d" % (time.time() - start, len(gens)))

# ---------------------------------------------------------------- coordinates on A = (Z/2)^10
start = time.time()
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
assert len(basis) == 10 and len(coord) == 1024, (len(basis), len(coord))
assert all(coord[a + b] == (coord[a] ^ coord[b])
           for a, b in itertools.islice(itertools.combinations(els[:64], 2), 200))
print('coordinate basis of A: 10 classes, all %d elements labelled, addition is xor   (%.0f s)'
      % (len(coord), time.time() - start))

start = time.time()
mats = []
for g in gens:
    mats.append(tuple(coord[g(b)] for b in basis))       # columns: images of the basis
print('10 x 10 matrices of %d generators   (%.0f s)' % (len(mats), time.time() - start))


def act(cols, x):
    """Act by a matrix given its column bit masks on the coordinate vector x."""
    out, i = 0, 0
    while x:
        if x & 1:
            out ^= cols[i]
        x >>= 1
        i += 1
    return out


# the matrices must reproduce the provider's action, or the walk below means nothing
sample = els[::37][:28]
checked = list(zip(mats, gens))[:12]
bad = sum(1 for cols, g in checked for x in sample if coord[g(x)] != act(cols, coord[x]))
print('check: matrix action equals the provider action on %d elements x %d generators: %s'
      % (len(sample), len(checked), 'yes' if not bad else 'NO -- %d mismatches' % bad))
assert not bad

distinct = sorted(set(mats))
print('distinct matrices among the %d generators: %d' % (len(mats), len(distinct)))

# ---------------------------------------------------------------- the walk on the isotropic classes
iso_coord = {coord[e] for e in iso}
assert len(iso_coord) == 528, len(iso_coord)
assert 0 in iso_coord
target = iso_coord - {0}
print('isotropic classes %d, of which nonzero %d' % (len(iso_coord), len(target)))

start = time.time()
seen, orbits = set(), []
for seed in sorted(target):
    if seed in seen:
        continue
    orbit, frontier = {seed}, [seed]
    seen.add(seed)
    while frontier:
        x = frontier.pop()
        for cols in distinct:
            y = act(cols, x)
            if y not in orbit:
                orbit.add(y)
                seen.add(y)
                frontier.append(y)
    assert orbit <= target, 'the walk left the isotropic classes'
    orbits.append(orbit)
sizes = sorted((len(o) for o in orbits), reverse=True)
print('the walk: %d orbits, sizes %s   (%.0f s)' % (len(orbits), sizes, time.time() - start))
print('  sum of the orbit sizes: %d of %d' % (sum(sizes), len(target)))
assert sum(sizes) == len(target) == 527
assert len(seen) == 527

# ---------------------------------------------------------------- the export for the plane half
with open(EXPORT, 'w') as handle:
    handle.write('# generators of H = Stab_{O(q)}([h/2]) on A_{T_En}, as 10 x 10 matrices over F_2.\n')
    handle.write('# written by coble_TEn-gammaEn2-orbits.py; each line is the ten columns of one\n')
    handle.write('# matrix as bit masks, column i being the image of the i-th class of the\n')
    handle.write('# coordinate basis built there: the loop over A.elements() adding each class not\n')
    handle.write('# yet in the span, so coordinate 1 << i is basis[i].  Sage %s, pin 15db925b,\n'
                 % SAGE_VERSION)
    handle.write('# |O(q)| = %d, |H| = %d, %d generators, %d distinct.\n'
                 % (int(G.order()), int(H.order()), len(mats), len(distinct)))
    for cols in distinct:
        handle.write(' '.join(str(x) for x in cols) + '\n')
print('exported the %d distinct matrices to %s' % (len(distinct), EXPORT))
print('')

print('THE NUMBER')
print('  H-orbits on the nonzero isotropic classes of A_{T_En}: %d' % len(orbits))
print('  published (AEGS 2025, section 3.3, p. 590: five 0-cusps and nine 1-cusps): %d' % PUBLISHED)
print('')
if len(orbits) == PUBLISHED:
    print('AGREES with the published count.  Consequently, for THIS pair (Gamma_En,2 and its rho-image')
    print('H), the fibres of the rho-side count over the rho-double-cosets are single points: the')
    print('rho-side count and the Gamma_En,2-count coincide at %d.  That is a consequence of the' % PUBLISHED)
    print('published value, not of a general lemma -- ker rho is not inside Stab(h), so it does not')
    print('follow from the definition of rho as it does for Gamma_Co.')
else:
    print('DOES NOT agree with the published count; the rho-side method does not see the orbits,')
    print('and the lattice-side count (S_eta-orbits of square-4 divisibility-2 vectors, Eichler')
    print('inside the K-cosets) is the next thing to compute.')
