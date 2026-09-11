"""Archive reconciliation for the free-module/underlying-set adjunction.

``free_forgetful_adjunction.sage`` stated the unit, counit, Hom-set bijection,
and two triangle identities explicitly.  The live implementation factors those
responsibilities between ``FreeForgetfulAdjunction`` and the common
``Adjunction`` owner; these specimens identify that semantic replacement.
"""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.functors.free_forgetful import (
    free_forgetful_adjunction,
)
from dzack_research.preamble.categories.modules import BasedFreeModule, module_homset
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_archived_hom_bijection_is_the_live_adjunction_transpose() -> None:
    adjunction = free_forgetful_adjunction(ZZ)
    labels = finite_ordered_set(("x", "y"))
    module = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    free = adjunction.left_adjoint()(labels)
    morphism = module_homset(free, module)(
        {
            "x": module.module_generator("a") + module.module_generator("b"),
            "y": 3 * module.module_generator("a"),
        }
    )

    transpose = adjunction.hom_set_isomorphism_forward(morphism)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, module)

    assert transpose(labels("x")) == morphism(free.module_generator("x"))
    assert transpose(labels("y")) == morphism(free.module_generator("y"))
    assert recovered == morphism


def test_archived_triangle_identities_are_the_live_unit_and_counit() -> None:
    adjunction = free_forgetful_adjunction(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    labels = finite_ordered_set(("u", "v"))
    module = BasedFreeModule(ZZ, finite_ordered_set(("p", "q")))

    first_triangle = underlying(adjunction.counit(module)) * adjunction.unit(
        underlying(module)
    )
    for generator in module.module_generators():
        assert first_triangle(generator) == generator

    free_labels = free(labels)
    second_triangle = adjunction.counit(free_labels) * free(adjunction.unit(labels))
    for generator in free_labels.module_generators():
        assert second_triangle(generator) == generator
