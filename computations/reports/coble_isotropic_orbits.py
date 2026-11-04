"""The two orbits of Orth(A_{T_Co}, q) on the 528 isotropic classes, at the maintained action.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_isotropic_orbits.py

sage-extensions at provider 9dc89ac1d9e4ab074da8872386aaf5b9df290f63, exported read-only from the image's
clone into .scratch/se-provider and bound per process; nothing in the shared rootfs is touched and no
orbit is closed by hand here.

What is checked.  thm:coble-isotropic-class-orbits states that Orth(A_{T_Co}, q_{T_Co}) has exactly two
orbits on the 528 isotropic classes, {0} and the 527 nonzero ones, and prop:coble-discriminant-group
states |Orth| = 2^21*3^5*5^2*7*17*31 = 46998591897600.  Both are checked here on the same lattice as
coble_528_isotropic_classes.py, using the library's own orbit partition of the whole group.

The trap this file is written around.  The full partition has more than two orbits, and two of them have
the *same size* 527.  They are not both isotropic: the fibers of q have sizes 528, 528, 496, 496, so a
527-orbit in the q = 1/2 fiber has the same cardinality as the 527-orbit of nonzero isotropic classes.
Every orbit is therefore classified by the value of q on it, and the isotropic statement is made only
after restricting to D.isotropic_elements().
"""
import time

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import EvenTwoElementaryLattices, Lattices

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])

T = Lattices(ZZ)([list(row) for row in
                  block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
assert tuple(int(v) for v in T.signature_pair()) == (2, 9) and T.is_even()
D = T.discriminant_quadratic_form()
assert int(D.cardinality()) == 2 ** 11
print('T_Co: rank %d, det %s, A has %d classes' % (T.module_rank(), int(T.determinant()),
                                                   int(D.cardinality())))

G = D.orthogonal_group()
order = int(G.order())
print('|Orth(A_{T_Co}, q)| = %d' % order)
assert order == 2 ** 21 * 3 ** 5 * 5 ** 2 * 7 * 17 * 31
print('   claimed 2^21*3^5*5^2*7*17*31 = %d   AGREE' % (2 ** 21 * 3 ** 5 * 5 ** 2 * 7 * 17 * 31))

start = time.time()
orbits = list(D.orbits())
elapsed = time.time() - start
sizes = sorted(int(orbit.cardinality()) for orbit in orbits)
print('the maintained orbit partition materialised in %.1fs: %d orbits, sizes %s'
      % (elapsed, len(orbits), sizes))
assert sum(sizes) == 2048

# Every orbit carries a single value of q; classify before concluding anything.
zero = D.quadratic_value_module().zero()
table = []
for orbit in orbits:
    points = list(orbit)
    values = {str(D.q(point).lift()).replace('(', '').replace(')', '') for point in points}
    assert len(values) == 1, 'an orbit mixes values of q'
    table.append((len(points), values.pop()))
print('orbit (size, q):', sorted(table))

isotropic = D.isotropic_elements()
isotropic_set = set(isotropic)
print('isotropic classes: %d' % len(isotropic_set))
assert len(isotropic_set) == 528

isotropic_orbits = [orbit for orbit in orbits if set(orbit) <= isotropic_set]
sizes_iso = sorted(int(orbit.cardinality()) for orbit in isotropic_orbits)
print('orbits contained in the isotropic classes: %d, of sizes %s' % (len(isotropic_orbits), sizes_iso))
assert sizes_iso == [1, 527], sizes_iso
assert set().union(*[set(orbit) for orbit in isotropic_orbits]) == isotropic_set, \
    'the isotropic classes are not the union of those orbits'
fixed = [orbit for orbit in isotropic_orbits if int(orbit.cardinality()) == 1][0]
assert len(list(fixed)) == 1
print('   {0} and one orbit of 527, whose union is exactly D.isotropic_elements()   AGREE')
print('   the other 527-orbit carries q = %s and is NOT isotropic'
      % [value for size, value in table if size == 527 and value != '0'])

# The two-elementary type of the lattice the group acts on, for the record.
invariants = EvenTwoElementaryLattices(T.base_ring())(T).two_elementary_invariants()
print('T_Co two_elementary_invariants: %s' % (tuple(int(x) for x in invariants),))
