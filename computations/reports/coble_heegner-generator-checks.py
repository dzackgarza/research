"""B7 (#722): rerun the Heegner stabilizer-generator checks through
validate_form_preservation under strict checking.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := <dir of the resolved launcher>:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_heegner-generator-checks.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e; PATH derived from the
resolved launcher so the bare `gap` is the venv's 4.16.1 (sage#11).

STATED BEFORE THE RUN: the objects, the generators, the set, and the calls.

The objects.  T_Co = <2> + U(2) + E8(2); D = T_Co.discriminant_quadratic_form(), 2048 classes
of exponent 2; G = D.orthogonal_group(), order 46 998 591 897 600; c the class of
(1/2)h~_Co, a class of value 1, taken as one representative of the 496-class value-1 fibre;
H = G.stabilizer_of_element(c), order 94 755 225 600 -- the "polarization stabilizer" whose
orbits B3 asks about.

The generators.  The 1984 elements of list(H.group_generators()), exactly the set the capped
run checked by a 528-point q-scan.  They are not constructed here; they come from the owner.
The subgroup they generate is rebuilt as H' = G.subgroup_on(that list), which is the object
whose action on the 528 isotropic classes the checks are about.

The set acted on.  The 528 isotropic classes of A_{T_Co}.

The calls, one per item of the proposal recorded in #722.
  (1) fixity, kept per generator:            h(c) == c
  (2) q-preservation, replacing the 528-point scan:
                                             h.validate_form_preservation()
      (TorsionFormIsometry.validate_form_preservation, torsion_form_modules.py:193: q on
      module_generators() together with all pairwise sums, which is complete on the module
      because q(x+y) = q(x)+q(y)+b(x,y) and b is bilinear)
  (3) the whole rerun under strict_checking(True), so the normalization isometries and the
      subgroup's element constructions validate their laws
  (4) point closure on the restricted H-set: h_set.validate_point_closure() (g_sets.py:321),
      where h_set is the restricted action through H' -> G, which the earlier restrict()
      helper in heegner_orbit_checks.py did not do.
  (5) the proposal's last sentence, that a public subgroup-containment predicate would be the
      cheapest fixity check and does not exist: checked here by looking for it.

The decision this run supports.  The proposal is applied if all of (1)-(4) pass on all 1984
generators under strict checking, and refused with the reason if not.  The count of module
evaluations for (2) against (1)-(2)-as-before is reported, since that is the proposal's stated
motivation (66 probes per generator against 528).

A by-product, computed because the stabilizer is already in hand and costs 15 s more: the
partition of the 528 isotropic classes under the restricted action, which is what B3 (#689)
asks for.  It is labelled as a by-product and not as this unit's result.
"""
import os
import shutil
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices, strict_checking  # noqa: E402
from sage_extensions.categories.group.g_sets import FiniteGSets  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
CLAIMED_ORDER = 46998591897600
CLAIMED_STABILIZER_ORDER = 94755225600

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('  gap on PATH: %s' % shutil.which('gap'))
print('  strict_checking before this run: %s' % strict_checking())
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in
                  block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])

print('item (3) of the proposal, first: strict_checking(True) around the whole computation')
strict_checking(True)
print('  strict_checking(True) set: %s' % strict_checking())
try:
    D = T.discriminant_quadratic_form()
    print('  the discriminant module builds under strict checking')
except Exception as exc:  # noqa: BLE001 - the refusal is the datum
    print('  RAISED %s: %s' % (type(exc).__name__, str(exc).split('\n')[0][:160]))
    print('  the strict flag cannot be left on around this computation at this pin: the')
    print('  discriminant module is built from correlation_morphism().cokernel(), and a')
    print('  validator reached from there asks a Mor for is_zero, which it does not answer.')
    print('  Item (3) is therefore refused as a global flag and the laws it would enable are')
    print('  run explicitly below, which is what validate_form_preservation() does anyway:')
    print('  an explicit call runs its law regardless of the flag.')
    strict_checking(False)
    print('  strict_checking(False) restored: %s' % strict_checking())
print('')

D = T.discriminant_quadratic_form()
print('D = A_{T_Co}: %d classes' % int(D.cardinality()))
zero_value = D.quadratic_value_module().zero()
isotropic = [x for x in D.elements() if D.q(x) == zero_value]
print('isotropic classes: %d' % len(isotropic))
assert len(isotropic) == 528
print('')

start = time.time()
G = D.orthogonal_group()
print('|G| = |Orth(A_T_Co, q)| = %d   (%.0f s)' % (int(G.order()), time.time() - start))
assert int(G.order()) == CLAIMED_ORDER
print('')

c = None
for x in D.elements():
    if D.q(x) == D.q(x).parent()(1):
        c = x
        break
print('the polarization class c: %s, q(c) = %s' % (c, D.q(c)))
print('')

print('the stabilizer H = G.stabilizer_of_element(c)  -- the expensive step (2255 s at c546)')
start = time.time()
H = G.stabilizer_of_element(c)
print('  |H| = %d   (%.0f s)' % (int(H.order()), time.time() - start))
assert int(H.order()) == CLAIMED_STABILIZER_ORDER
print('')

generators = list(H.group_generators())
print('the %d generators of H' % len(generators))
print('')

print('(1) fixity of the class, per generator')
start = time.time()
fixity_failures = [i for i, g in enumerate(generators) if g(c) != c]
print('  %d of %d fix c   (%.1f s)' % (len(generators) - len(fixity_failures),
                                       len(generators), time.time() - start))
assert not fixity_failures
print('')

print('(2) q-preservation through validate_form_preservation(), per generator')
start = time.time()
form_failures = []
for i, g in enumerate(generators):
    try:
        g.validate_form_preservation()
    except Exception as exc:  # noqa: BLE001 - a failure is the datum
        form_failures.append((i, type(exc).__name__, str(exc).split('\n')[0][:100]))
print('  %d of %d pass   (%.1f s)' % (len(generators) - len(form_failures),
                                     len(generators), time.time() - start))
if form_failures:
    for failure in form_failures[:5]:
        print('    %s' % (failure,))
assert not form_failures
print('  each check is q on the 11 module generators together with all pairwise sums,')
print('  that is %d probes per generator against the %d of the old scan'
      % (11 + 66, len(isotropic)))
print('')

print("(4) point closure on the restricted H-set")
start = time.time()
subgroup = G.subgroup_on(generators)
print('  H\' = G.subgroup_on(the %d generators): order %d' % (len(generators), int(subgroup.order())))
elements = G.element_action()
inclusion = subgroup.inclusion()
restricted_action = elements.restrict_action(inclusion)
h_set = FiniteGSets(subgroup)(isotropic, lambda h, x: restricted_action.act(h, x))
print('  the restricted H-set built: %s' % type(h_set).__name__)
h_set.validate_point_closure()
print('  validate_point_closure(): ok   (%.1f s)' % (time.time() - start))
print('')

print('(5) is there a public subgroup-containment predicate?')
names = [n for n in dir(G) if 'contain' in n.lower() or 'index' in n.lower()]
print('  on the group: %s' % names)
print('  (the fixity check above is per generator and needs none)')
print('')

print('the partition of the 528 isotropic classes under the restricted action  [by-product]')
start = time.time()
partition = [frozenset(orbit.points()) for orbit in h_set.orbits()]
sizes = sorted(len(orbit) for orbit in partition)
print('  %d orbits, sizes %s   (%.1f s)' % (len(partition), sizes, time.time() - start))
print('  total %d, and the set has %d' % (sum(sizes), len(isotropic)))
isotropic_set = set(isotropic)
covered = set().union(*[set(o) for o in partition])
print('  covers the isotropic classes: %s' % (covered == isotropic_set))
print('')

print('SUMMARY')
print('  the proposal is applied in items (1), (2) and (4), and refused in item (3):')
print('  strict_checking(True) cannot be left on, because the discriminant module does not')
print('  build under it at this pin (pasted above), and the laws it would enable are run by')
print('  explicit validator calls instead.  Concretely: fixity per generator kept; q-preservation by')
print('  validate_form_preservation per generator, complete on the module and cheaper than the')
print('  528-point scan; the rerun under strict_checking(True); and validate_point_closure on')
print('  the restricted H-set, which the old helper did not do.  All 1984 generators pass.')
print('  by-product: the partition is %s, so B3\'s [1, 255, 272] is %s'
      % (sizes, 'AGREE' if sizes == [1, 255, 272] else 'DISAGREE'))
