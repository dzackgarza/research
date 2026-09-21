r"""Archive reconciliation for fraction-field module base change.

The archived ``BaseChangeFunctor`` and ``fraction_field_base_change`` are the
live scalar-extension functor along ``R -> Frac(R)`` and its
extension/restriction adjunction.  The mathematical construction is retained
under the scalar-change vocabulary rather than by restoring a second functor.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def _free_rank_two():
    integers = _own_ring(SageZZ)
    module = integers.free_module(finite_ordered_set(("e", "f")))
    labels = tuple(module.module_generating_set())
    morphism = module.module_category().Mor(module, module)(
        {
            labels[0]: module.scalar_multiple(
                integers(2), module.module_generator(labels[0])
            ),
            labels[1]: module.module_generator(labels[0])
            + module.module_generator(labels[1]),
        }
    )
    return integers, module, morphism


def test_fraction_field_base_change_is_live_scalar_extension_on_objects_and_maps() -> None:
    integers, module, morphism = _free_rank_two()
    ring_map = integers.fraction_field_map()
    rationals = ring_map.codomain()
    extension = Modules(integers).scalar_extension(ring_map)

    changed = extension(module)
    carried = extension(morphism)

    assert extension.domain() == Modules(integers)
    assert extension.codomain() == Modules(rationals)
    assert changed.base_ring() is rationals
    assert carried.domain() is changed
    assert carried.codomain() is changed
    carried_matrix = carried.matrix()
    source_matrix = morphism.matrix()
    assert carried_matrix == source_matrix.change_ring(rationals)


def test_fraction_field_base_change_has_the_extension_restriction_unit() -> None:
    integers, module, _morphism = _free_rank_two()
    ring_map = integers.fraction_field_map()
    adjunction = Modules(integers).base_change_adjunction(ring_map)

    unit = adjunction.unit(module)
    extended = adjunction.left_adjoint()(module)
    restricted = adjunction.right_adjoint()(extended)

    assert unit.domain() is module
    assert unit.codomain() is restricted
    for label in module.module_generating_set():
        image = unit(module.module_generator(label))
        assert image.underlying_element() == extended.module_generator(label)
