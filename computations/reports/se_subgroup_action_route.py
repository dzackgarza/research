"""The route for the orbit partition of a *subgroup* of a formed-module orthogonal group.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/se_subgroup_action_route.py

Provider 9dc89ac1d9e4ab074da8872386aaf5b9df290f63.

Why this file exists.  The ambient group has the action -- TorsionFormOrthogonalGroup.element_action(),
whose orbits() works after the owner's repair -- but a subgroup object alone does not specify an orbit
partition: what is needed is the subgroup's action on the module, obtained by restricting the ambient
action through H -> G.  H.orbits() does not exist and element_action() is not inherited, so this file
records what the interface actually offers, at a scale that costs seconds rather than the hours the real
lattice costs: whether FiniteGSets(H)(point_set, action) is that construction, and whether it accepts a
proper subset of the module rather than only the natural points.

What is established here is the *mechanics* on a small form.  The real computation on A_{T_Co} is not
performed and nothing about [1, 255, 272] is inferred from it.
"""
import sys
import time

from sage.all import ZZ, matrix

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

# A small 2-elementary form: the discriminant form of U(2) has order 4.
L = Lattices(ZZ)([list(row) for row in (2 * matrix(ZZ, [[0, 1], [1, 0]])).rows()])
D = L.discriminant_quadratic_form()
G = D.orthogonal_group()
print('small form: %d classes, |Orth| = %s' % (int(D.cardinality()), int(G.order())))

elements = list(D.elements())
action = G.element_action()
print('ambient action type: %s' % type(action).__name__)
start = time.time()
ambient_orbits = list(action.orbits())
print('ambient orbits: %s (%.1fs)' % ([int(o.cardinality()) for o in ambient_orbits], time.time() - start))

# A proper subgroup of the ambient group, and the three things one might try on it.
generators = list(G.group_generators())
H = G.subgroup_on(generators[:1]) if len(generators) > 1 else G.subgroup_on(generators)
print('subgroup H: order %s, type %s' % (int(H.order()), type(H).__name__))
print('   H has orbits(): %s' % hasattr(H, 'orbits'))
print('   H has element_action(): %s' % hasattr(H, 'element_action'))

# The route the interface documents: a G-set built from an action map.
subset = elements[:3]
try:
    from sage_extensions.categories.group.g_sets import FiniteGSets

    restricted = FiniteGSets(H)(subset, lambda h, x: h(x))
    print('FiniteGSets(H)(subset, lambda h, x: h(x)) constructed: %s' % type(restricted).__name__)
    restricted_orbits = list(restricted.orbits())
    print('   its orbits on a 3-element subset: %s' % [int(o.cardinality()) for o in restricted_orbits])
    full = FiniteGSets(H)(elements, lambda h, x: h(x))
    print('   its orbits on all %d classes: %s'
          % (len(elements), [int(o.cardinality()) for o in full.orbits()]))
    print('   ROUTE AVAILABLE: restricting the ambient action through H -> G is constructible, and it')
    print('   accepts a proper subset, which is what the isotropic-only partition needs.')
except Exception as exc:
    print('   FiniteGSets route failed: %r' % (exc,))
    print('   MISSING CONTRACT: the action of a subgroup on a subset of the module is not constructible')
    print('   through the documented interface; the shortest repro is above.')
