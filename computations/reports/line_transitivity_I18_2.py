"""Isotropic lines of I_{1,8}(2): what the discriminant decides, and what it leaves open.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/line_transitivity_I18_2.py

Provider c546077d.  The obligation this addresses: plane transitivity of T_Co reduces to line
transitivity in l^perp/l = I_{1,8}(2), and neither Wall nor James reaches that lattice (r - |s| = 2).

What is decided here is an *invariant* statement, and it is decided in one direction only.  For a primitive
isotropic vector v of divisibility 2, the class v* = v/2 mod L in A_L is preserved by every isometry, so
vectors whose classes lie in different Orth(q)-orbits cannot be isometric: if Orth(q) has more than one
orbit on the isotropic classes, transitivity of Orth(L) on primitive isotropic vectors FAILS, for the full
group and hence for each of its subgroups.  If it has exactly one orbit, nothing follows about lines --
that is the Eichler-type step which this file does not supply.
"""
import sys

from sage.all import ZZ, diagonal_matrix

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

# I_{1,8}(2): the twist of the odd unimodular lattice diag(1, -1, ..., -1).
GRAM = 2 * diagonal_matrix(ZZ, [1] + [-1] * 8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
D = L.discriminant_quadratic_form()
print('I_(1,8)(2): rank %d, signature %s, det %s, |A| = %d'
      % (L.module_rank(), tuple(int(x) for x in L.signature_pair()), int(L.determinant()),
         int(D.cardinality())))
G = D.orthogonal_group()
print('|Orth(q)| = %d' % int(G.order()))

zero_value = D.quadratic_value_module().zero()
elements = list(D.elements())
isotropic = [x for x in elements if D.q(x) == zero_value]
print('classes: %d, isotropic classes: %d' % (len(elements), len(isotropic)))

# D.orbits() on the module yields point sets; a G-set's orbits() yields Orbit objects.  Handle both.
def points_of(orbit):
    return frozenset(orbit.points()) if hasattr(orbit, 'points') else frozenset(orbit)


partition = [points_of(orbit) for orbit in D.orbits()]
inside = [orbit for orbit in partition if set(orbit) <= set(isotropic)]
sizes = sorted(len(orbit) for orbit in inside)
print('Orth(q) orbits on all classes: %d, sizes %s' % (len(partition),
                                                       sorted(len(o) for o in partition)))
print('orbits contained in the isotropic classes: %d, sizes %s' % (len(inside), sizes))
assert sum(sizes) == len(isotropic)
# The two orbits are the zero class and the 135 nonzero ones.  A *primitive* isotropic vector of
# I_(1,8)(2) has divisibility 2, so v/2 is not in L and its class is nonzero: the zero class is not
# attained by any primitive vector.  Hence the discriminant separates nothing among the vectors this
# question is about, and it cannot decide line transitivity either way.
zero_element = D.zero() if hasattr(D, 'zero') else elements[0] - elements[0]
singleton = [orbit for orbit in inside if len(orbit) == 1][0]
assert set(singleton) == {zero_element}, 'the singleton isotropic class-orbit is not the zero class'
assert sizes == [1, 135], sizes
print()
print('the two orbits are {0} and the 135 nonzero isotropic classes.')
print('a primitive isotropic vector has divisibility 2, so v/2 is not in L and its class is nonzero:')
print('the zero class-orbit is not attained by any primitive vector, and every primitive isotropic')
print('vector has its class in the SINGLE 135-element orbit.  So the discriminant imposes no separation')
print('here, and line transitivity in I_(1,8)(2) is NOT decided by it: what is missing is the')
print('Eichler-type step at r - |s| = 2, which neither Wall nor James provides.')
