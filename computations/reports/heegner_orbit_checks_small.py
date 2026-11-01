"""Drive the shared post-stabilizer path on a small maintained example.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/heegner_orbit_checks_small.py

The same helper the full run calls, on the order-4 discriminant form of U(2): the restriction route, the
Orbit -> points() conversion, disjointness, coverage, the q = 0 domain, the singleton being the zero class,
the sizes, and the generator-action checks.  Costs seconds; the point is that it fails or passes on
exactly the code that runs for A_{T_Co}.
"""
import os
import sys
import time

from sage.all import ZZ, matrix

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else
                '/repo/computations/reports')
sys.path.insert(0, '/repo/computations/reports')

from heegner_orbit_checks import check_generators, check_partition, check_values, restrict  # noqa: E402

L = Lattices(ZZ)([list(row) for row in (2 * matrix(ZZ, [[0, 1], [1, 0]])).rows()])
D = L.discriminant_quadratic_form()
G = D.orthogonal_group()
zero_value = D.quadratic_value_module().zero()
elements = list(D.elements())
isotropic = [x for x in elements if D.q(x) == zero_value]
zero_element = D.zero() if hasattr(D, 'zero') else elements[0] - elements[0]
print('small form: %d classes, %d isotropic, |Orth| = %s'
      % (len(elements), len(isotropic), int(G.order())))

# A proper subgroup, so the partition is not the trivial one.
generators = list(G.group_generators())
subgroup = G.subgroup_on(generators[:1]) if len(generators) > 1 else G.subgroup_on(generators)
print('subgroup: order %s' % int(subgroup.order()))

start = time.time()
partition = restrict(G, subgroup, isotropic)
print('restrict(): %d orbits in %.1fs, sizes %s'
      % (len(partition), time.time() - start, sorted(len(p) for p in partition)))

sizes = check_partition(partition, set(isotropic), zero_element, [len(p) for p in partition])
print('check_partition(): disjoint, covering, one singleton equal to {D.zero()}, sizes %s   AGREE' % sizes)

checked = check_values(D.q, isotropic, zero_value)
print('check_values(): %d points all have q = 0   AGREE' % checked)

count = check_generators(list(subgroup.group_generators()), isotropic[0], isotropic, D.q)
print('check_generators(): %d generators fix the chosen class and preserve q   AGREE' % count)
print()
print('the whole post-stabilizer path runs on this example, through the helper the full run imports')
