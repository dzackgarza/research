"""The [1, 255, 272] decomposition of the 528 isotropic classes under the polarization stabilizer.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_heegner_stabilizer_orbits.py

sage-extensions at provider c546077dce79a76eb32e92d080aa9c44e4c67552 (and 9dc89ac1 earlier), exported read-only from the
image's clone into .scratch/se-provider and bound per process; no rootfs write and no hand closure.

The claim.  the-heegner-line-and-the-coble-arithmetic-group.md states that the finite stabilizer
Stab_{Orth(q_{T_Co})}(1/2 h~_Co) of the class of the transported polarization has order 94,755,225,600
and acts on the same 528 isotropic classes with orbit lengths [1, 255, 272].

Which class, and what the chosen element is.  The manuscript's polarization is h_Co = F_1 + F_2 of
square 2, whose pullback h~_Co = f^* h_Co has square 4; the half-class 1/2 h~_Co is dual, and under the
discriminant convention q(1/2 x) = x^2/4 it has q = 4/4 = 1.  The gluing anti-isometry A_{S_Co} ->
A_{T_Co} sends q to -q, and -1 = 1 in QQ/2ZZ, so the value is 1 on either side.  What this file selects is
therefore a *representative of the conjugacy class of stabilizers* of value-1 classes, NOT the specific
geometric transported class: the transport from A_{S_Co} to A_{T_Co} is not constructed here, and no
statement below should be read as being about that particular class.  The choice inside the fiber is
immaterial exactly when Orth(q) is transitive on it, which is asserted here -- one orbit of size 496,
checked before anything is concluded -- so the stabilizers of any two value-1 classes are conjugate and
their orbit lengths agree.  The counts that follow -- 496, 94,755,225,600, [1, 255, 272] -- are
assertions to be tested, never inputs selecting the class.

What is not done, and must not be substituted.  The full orthogonal group is not used as a stand-in for
the stabilizer, the polarization is not changed to make a count come out, and the zero class is kept
separate from the 527 nonzero ones throughout.
"""
import sys
import time

# line-buffered so a long run reports its phase instead of nothing (the first copy's transcript was
# empty for exactly this reason)
sys.stdout.reconfigure(line_buffering=True)

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])

T = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
D = T.discriminant_quadratic_form()
G = D.orthogonal_group()
order = int(G.order())
print('|Orth(A_{T_Co}, q)| = %d, classes %d' % (order, int(D.cardinality())))
assert order == 46_998_591_897_600

CLAIMED_STABILIZER_ORDER = 94_755_225_600
assert order % CLAIMED_STABILIZER_ORDER == 0
print('the claimed stabilizer order divides it, with quotient %d'
      % (order // CLAIMED_STABILIZER_ORDER))
assert order // CLAIMED_STABILIZER_ORDER == 496

# The class with q = 1: how many are there, and what is the shape of one.
value_one = [x for x in D.elements() if str(D.q(x).lift()).replace('(', '').replace(')', '') == '1']
print('classes of value q = 1: %d   (prop:coble-q-fibers says 496)' % len(value_one))
assert len(value_one) == 496
polarization = value_one[0]
# The choice inside the value-1 fiber is immaterial: one Orth(q)-orbit (asserted below, size 496) means
# the stabilizers of two such classes are conjugate, so the orbit lengths do not depend on the choice.
print('chosen class 1/2 h~_Co: q = %s, doubling gives the zero class: %s'
      % (str(D.q(polarization).lift()).replace('(', '').replace(')', ''),
         (polarization + polarization) == D.zero() if hasattr(D, 'zero') else 'not checked'))

start = time.time()
orbit = G.orbit(polarization)
print('its Orbit-orbit has %d classes (%.1fs), so the stabilizer has order %d'
      % (len(orbit), time.time() - start, order // len(orbit)))
assert len(orbit) == 496

start = time.time()
stabilizer = G.stabilizer_of_element(polarization)
stabilizer_order = int(stabilizer.order())
print('Stab_{Orth(q)}(1/2 h~_Co) has order %d (%.1fs)' % (stabilizer_order, time.time() - start))
assert stabilizer_order == CLAIMED_STABILIZER_ORDER

# Orbits of the stabilizer itself on the isotropic classes.
zero_value = D.quadratic_value_module().zero()
isotropic = [x for x in D.elements() if D.q(x) == zero_value]
print('isotropic classes: %d' % len(isotropic))
assert len(isotropic) == 528

# A subgroup object does not carry an orbit partition.  The needed object is its ACTION on the module,
# obtained by restricting the ambient action through the inclusion H -> G; the interface constructs that
# from an action map with FiniteGSets(H)(points, action), and it accepts a proper subset of the module.
# Both facts are verified on a small form in se_subgroup_action_route.py, not assumed here.
from sage_extensions.categories.group.g_sets import FiniteGSets

subgroup = G.subgroup_on(list(stabilizer.group_generators()))
print('stabilizer rebuilt inside Orth(q): order %d' % int(subgroup.order()), flush=True)
assert int(subgroup.order()) == CLAIMED_STABILIZER_ORDER

# The maintained restriction route, as published in provider c546077d:
#   elements = G.element_action(); inclusion = H.inclusion(); restricted = elements.restrict_action(inclusion)
# with restricted.act(h, x) = elements.act(inclusion(h), x).  The isotropic subset is presented explicitly
# through FiniteGSets(H)(points, action); no H.orbits convenience is needed or used.
elements = G.element_action()
inclusion = subgroup.inclusion()
restricted_action = elements.restrict_action(inclusion)
print('restricted the ambient action through H -> G: %s' % type(restricted_action).__name__,
      flush=True)

start = time.time()
isotropic_action = FiniteGSets(subgroup)(isotropic, lambda h, x: restricted_action.act(h, x))
restricted = [frozenset(orbit.points()) for orbit in isotropic_action.orbits()]
print('the restricted action gives %d orbits on the %d isotropic classes (%.1fs)'
      % (len(restricted), len(isotropic), time.time() - start), flush=True)
isotropic_set = set(isotropic)
sizes = sorted(len(orbit) for orbit in restricted)
print('orbits inside the isotropic classes: %d, of sizes %s' % (len(restricted), sizes))
assert sizes == [1, 255, 272], sizes
assert sum(sizes) == 528
assert set().union(*[set(orbit) for orbit in restricted]) == isotropic_set, 'not a cover'
total = sum(len(orbit) for orbit in restricted)
assert total == 528, 'orbits are not disjoint'
singleton = [orbit for orbit in restricted if len(orbit) == 1][0]
zero_element = D.zero() if hasattr(D, 'zero') else polarization - polarization
assert zero_element + zero_element == zero_element, 'the zero element is not idempotent under addition'
assert set(singleton) == {zero_element}, 'the singleton orbit is not the zero class'
print('the singleton orbit is exactly {D.zero()}: asserted, not inferred')

# 3. the returned stabilizer must actually fix the chosen class and preserve q.
generators = list(stabilizer.group_generators())
print('stabilizer generators: %d' % len(generators))
assert generators
for generator in generators:
    assert generator(polarization) == polarization, 'a stabilizer generator moves the chosen class'
for generator in generators:
    for x in isotropic:
        assert D.q(generator(x)) == D.q(x), 'a stabilizer generator does not preserve q on the isotropic set'
print('every stabilizer generator fixes the chosen class and preserves q on the 528 isotropic classes')
print()
print('claimed [1, 255, 272]   computed %s   AGREE' % sizes)
print('the three orbits are disjoint, cover the 528 isotropic classes, and every element has q = 0:')
print('   q-values present: %s' % sorted({str(D.q(x).lift()).replace('(', '').replace(')', '') for x in isotropic_set}))
