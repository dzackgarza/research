"""Repro: the orbit partition of a 2048-point discriminant form does not return, though every piece
of it is cheap.  A specimen for the sage-extensions owner, not a certificate for any claim.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/se_orbit_partition_repro.py [seconds]

The optional argument is the bound in seconds on the call at issue (default 300); the stack of that
call is dumped by faulthandler when the bound is reached, and SIGALRM abandons it shortly after.

Pin.  sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee, on the research image's Sage
11.0.beta5 / Python 3.14.10, through the image's Julia bridge.  Every timing below is a wall clock on
a shared VM that also had another project's test suite running, so the numbers are upper bounds; the
contrast they measure is two orders of magnitude wide and is not an artefact of the load.

Construction, minimal.  B = <1> + U + E8(-1) is an odd unimodular lattice of rank 11 and signature
(2,9); T = B(2) is even of signature (2,9) with A_T = (Z/2)^11, 2048 classes; D is the discriminant
quadratic form the library returns for T, and G = D.orthogonal_group() the group the library returns
for D.  No hand-built Gram, no hand-built group.

What is cheap (measured):

    D.orthogonal_group()                0.01 s
    G.group_generators()                0.28 s   (4 generators)
    G.element_action()                  1.0  s
    one generator applied to one point  immediate
    closure of one orbit under those   3.3  s   (527 of the 528 singular classes)
    G.order()                          38    s

What does not return.  A.orthogonal_group().element_action().orbits() returns its object at once --
it is lazy -- and materialising it, len(...) or list(...), i.e. the whole orbit partition of the
2048-point set, does not return within 30 minutes.  This is also the only public route to a single
orbit, because

    TorsionFormOrthogonalGroup.orbit(x)  ==  self.element_action().orbits().orbit_of(x).points()

so G.orbit(x) pays for the whole partition as well.  There is no public single-orbit call at this
size.

The repeated path, from the frames faulthandler captured inside the call (elided to the loop):

    g_sets.py:_orbits -> __iter__ -> set_categories.py:_cardinality_decision -> __len__
    g_sets.py:_richcmp_ -> _decided_orbit_relation -> g_objects.py:in_same_orbit
    g_sets.py:_orbit_relation_decision -> _orbit_labels -> groups.py:group_generators
    groups.py:selected_group_resolution -> abstract_categories/objects.py:selected_resolution
    torsion_form_modules.py:_computed_group_generators -> _engine_group -> _engine_orthogonal_group
    lattice_engines.py:finite_form_isometry_group -> sage_julia_bridge/interface.py:call
    interface.py:_request -> _request_unlocked

Two things are visible there and both look addressable on the library side.  The partition is decided
by pairwise in_same_orbit decisions, so the point set is traversed quadratically.  And _orbit_labels,
which each decision calls, is not a lookup but a recomputation: two stacks captured in it show the
two halves of its work, one at g_sets.py:370 inside _permutation_from_point_map -> permutation_group
(images), constructing permutation-group elements through GAP (GapElement._check_contains), and one at
g_sets.py:359 in group_generators -> selected_group_resolution -> _computed_group_generators ->
_engine_group -> finite_form_isometry_group, resolving the group through the Julia bridge.  So every
relation decision rebuilds the permutation image of the group and can re-enter the group construction,
where four generators are already in hand.  Memoising _orbit_labels, or closing orbits under the
retained generators, is what the numbers above suggest would make orbit(x) and the partition usable at
this size.

Nothing here is a substitute for the computation the claim needs: this file exists so that the call
and its cost can be handed over as they stand.
"""
import faulthandler
import signal
import sys
import time

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 300


def timed(label, function):
    start = time.time()
    value = function()
    print('%-52s %8.2fs' % (label, time.time() - start), flush=True)
    return value


E8C = CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])

B = Lattices(ZZ)([list(row) for row in
                  block_diagonal_matrix(matrix(ZZ, [[1]]), U, -E8C).rows()])
T = B.twist(2)
D = timed('D = T.discriminant_quadratic_form()', lambda: T.discriminant_quadratic_form())
print('    A_T has %d classes' % int(D.cardinality()), flush=True)
elements = timed('elements()', lambda: list(D.elements()))
G = timed('G = D.orthogonal_group()', lambda: D.orthogonal_group())
order = timed('G.order()', lambda: int(G.order()))
generators = timed('G.group_generators()', lambda: list(G.group_generators()))
action = timed('A = G.element_action()', lambda: G.element_action())
print('    |G| = %d, %d generators' % (order, len(generators)), flush=True)

start = time.time()
generators[0](elements[1])
print('%-52s %8.2fs' % ('one generator applied to one point', time.time() - start), flush=True)

zero = D.quadratic_value_module().zero()
singular = [x for x in elements if D.q(x) == zero]
start = time.time()
seen, frontier = {singular[1]}, [singular[1]]
while frontier:
    following = []
    for point in frontier:
        for generator in generators:
            image = generator(point)
            if image not in seen:
                seen.add(image)
                following.append(image)
    frontier = following
print('%-52s %8.2fs   (%d of %d singular classes)'
      % ('closure of one orbit under the retained generators', time.time() - start,
         len(seen), len(singular)), flush=True)


class Expired(Exception):
    pass


def expired(signum, frame):
    raise Expired()


start = time.time()
orbits = action.orbits()
print('%-52s %8.3fs   (it is lazy: nothing is decided yet)'
      % ('A.orbits() returns its object', time.time() - start), flush=True)

print('materialising it -- len(...) -- bounded at %d s' % BUDGET, flush=True)
faulthandler.dump_traceback_later(BUDGET, repeat=False, file=sys.stderr)
signal.signal(signal.SIGALRM, expired)
signal.alarm(BUDGET + 5)
start = time.time()
try:
    count = len(orbits)
    print('%-52s %8.2fs   (%d orbits)'
          % ('len(A.orbits())', time.time() - start, count), flush=True)
except BaseException as exc:
    print('%-52s %8.2fs   (%s: abandoned)'
          % ('len(A.orbits())', time.time() - start, type(exc).__name__), flush=True)
finally:
    signal.alarm(0)
    faulthandler.cancel_dump_traceback_later()
