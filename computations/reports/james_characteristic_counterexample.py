"""Why the odd transitivity statement is not a statement about all odd unimodular lattices.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/james_characteristic_counterexample.py

James' theorem extends an isometry between primitive sublattices only when it preserves characteristic
status, and an isometry of the lattice always preserves that status.  So the rank-one transitivity of
prop:odd-unimodular-rank-one-transitivity can only hold for a lattice in which no primitive isotropic
vector is characteristic.  The hypothesis r(L) - |s(L)| >= 4 does not force that, and I_(2,2) is the
counterexample: rank 4, signature (2,2), so r - |s| = 4, yet it has a characteristic isotropic vector and
an ordinary one, hence two O-orbits.

In I_(2,9) the obstruction is absent for a congruence reason: a characteristic vector of I_(p,q) has all
coordinates odd, hence square congruent to p - q mod 8, and 2 - 9 = -7 = 1 mod 8 is not 0.
"""
from sage.all import ZZ, diagonal_matrix, matrix

from sage_extensions.all import Lattices


def lattice(signature):
    p, q = signature
    return Lattices(ZZ)([list(row) for row in diagonal_matrix(ZZ, [1] * p + [-1] * q).rows()])


def element(L, coefficients):
    ring = L.base_ring()
    return L.linear_combination({index: ring(int(value)) for index, value in enumerate(coefficients)
                                 if value != 0})


def is_characteristic(L, vector):
    """a.b == b^2 (mod 2) for every b, checked on the basis."""
    basis = [element(L, [1 if i == j else 0 for i in range(int(L.module_rank()))])
             for j in range(int(L.module_rank()))]
    return all(int(vector.b(b)) % 2 == int(b.b(b)) % 2 for b in basis)


def report(name, L, coefficients):
    v = element(L, coefficients)
    square = int(v.b(v))
    print('   %-18s square %3d   primitive %s   characteristic %s'
          % (name, square, int(L.div(v)) == 1, is_characteristic(L, v)))
    return v


print('I_(2,2): rank %d, signature %s, r - |s| = %d'
      % (lattice((2, 2)).module_rank(), tuple(int(x) for x in lattice((2, 2)).signature_pair()),
         int(lattice((2, 2)).module_rank()) - abs(2 - 2)))
L22 = lattice((2, 2))
c = report('(1,1,1,1)', L22, [1, 1, 1, 1])
v = report('(1,0,1,0)', L22, [1, 0, 1, 0])
assert int(c.b(c)) == 0 and int(v.b(v)) == 0
assert is_characteristic(L22, c) and not is_characteristic(L22, v)
print('   both isotropic and primitive; one characteristic, one not, so no isometry carries one to the')
print('   other and O(I_(2,2)) is NOT transitive on primitive isotropic vectors.')

print()
print('I_(2,9): rank 11, signature %s, r - |s| = 11 - 7 = %d'
      % (tuple(int(x) for x in lattice((2, 9)).signature_pair()),
         int(lattice((2, 9)).module_rank()) - abs(2 - 9)))
L29 = lattice((2, 9))
all_ones = element(L29, [1] * 11)
print('   the all-ones vector: square %d, characteristic %s, isotropic %s'
      % (int(all_ones.b(all_ones)), is_characteristic(L29, all_ones), int(all_ones.b(all_ones)) == 0))
assert int(all_ones.b(all_ones)) == -7 and is_characteristic(L29, all_ones)
assert int(all_ones.b(all_ones)) % 8 == 1
print('   a characteristic vector has square = p - q = -7 = 1 (mod 8), and 0 != 1 (mod 8),')
print('   so no characteristic vector of I_(2,9) is isotropic and the clause is vacuous there.')
