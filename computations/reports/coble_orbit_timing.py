"""What each stage of the A_{T_Co} orbit computation costs, and where the cost is not.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_orbit_timing.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee on this project's bind.

This is a timing certificate, not the certificate for a claim: the claims are in
coble_isotropic_orbits.py.  It exists because the natural public route to an orbit here does not
return, and a reader is entitled to see which call that is before accepting a different route.

The stages are timed one at a time -- lattice, twist, discriminant form, element enumeration, group
construction, group order, generators, the represented action, one application, one orbit closure --
so that the group construction, its order, its generators, the action and the orbit computation are
not conflated.

The full orbit partition is not run here, because it does not return inside half an hour.  To
reproduce that, set ORBITS=1 and bound the run from outside; the stacked frames captured with
faulthandler are quoted in GAPS.  The two public entry points involved are

    A_{T_Co}.orthogonal_group().element_action().orbits()   -- the whole partition
    A_{T_Co}.orthogonal_group().orbit(x)                    -- which calls the above and selects

so there is no public single-orbit call, and the closure over retained generators is what
coble_isotropic_orbits.py uses instead.
"""
import os
import sys
import time

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices


def stage(name):
    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self

        def __exit__(self, *exception):
            print('%-46s %8.2fs' % (name, time.time() - self.start), flush=True)
            return False
    return Timer()


E8C = CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])

with stage('lattice B = <1> + U + E8(-1)'):
    B = Lattices(ZZ)([list(row) for row in
                      block_diagonal_matrix(matrix(ZZ, [[1]]), U, -E8C).rows()])
with stage('twist B -> T_Co = B(2)'):
    T = B.twist(2)
with stage('discriminant_quadratic_form'):
    D = T.discriminant_quadratic_form()
with stage('cardinality'):
    cardinality = int(D.cardinality())
with stage('elements(): enumerate the classes'):
    elements = list(D.elements())
with stage('orthogonal_group(): construct'):
    G = D.orthogonal_group()
with stage('order()'):
    order = int(G.order())
with stage('group_generators()'):
    generators = list(G.group_generators())
with stage('element_action(): construct the represented action'):
    action = G.element_action()
with stage('one generator applied to one point'):
    image = generators[0](elements[1])

print('classes %d, group order %d, generators %d' % (cardinality, order, len(generators)),
      flush=True)
assert cardinality == 2 ** 11
assert order == 2 ** 21 * 3 ** 5 * 5 ** 2 * 7 * 17 * 31
assert image is not None

zero = D.quadratic_value_module().zero()
singular = [x for x in elements if D.q(x) == zero]
start = time.time()
seed = singular[1]
seen = {seed}
frontier = [seed]
while frontier:
    following = []
    for point in frontier:
        for generator in generators:
            image = generator(point)
            if image not in seen:
                seen.add(image)
                following.append(image)
    frontier = following
print('%-46s %8.2fs  (%d points)' % ('closure from one nonzero singular vector',
                                      time.time() - start, len(seen)), flush=True)
assert len(seen) == len(singular) - 1

if os.environ.get('ORBITS') == '1':
    print('attempting the public full partition; bound this from outside', flush=True)
    start = time.time()
    action.orbits()
    print('the partition returned in %.1fs' % (time.time() - start), flush=True)
else:
    print('the public full partition is not attempted here (set ORBITS=1 to attempt it); '
          'it did not return within thirty minutes when it was tried', flush=True)
