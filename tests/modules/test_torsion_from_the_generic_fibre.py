r"""Torsion computed from its definition, not read off a decomposition.

Over an integral domain ``R`` with fraction field ``K``, the torsion submodule
of ``M`` is the kernel of the unit ``M -> K tensor_R M`` of scalar extension,
and ``M`` is torsion exactly when that generic fibre vanishes.  Both statements
hold over any domain; the invariant-factor reading of them is a principal
ideal domain's shortcut, not the definition.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    QQ,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_the_fraction_field_map_is_the_localization_at_the_nonzero_scalars() -> None:
    inclusion = ZZ.fraction_field_map()

    assert inclusion.domain() is ZZ
    assert inclusion.codomain() is QQ
    assert inclusion(ZZ(3)) == QQ(3)
    assert QQ.fraction_field_map()(QQ(3)) == QQ(3)


def test_a_free_module_has_zero_torsion_submodule() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))

    assert module.generic_fibre_map().domain() is module
    assert module.generic_fibre_map().is_injective()
    assert module.torsion_submodule().module_rank() == 0
    assert module.is_torsion_free()
    assert not module.is_torsion()


def test_a_finite_abelian_group_is_torsion_with_itself_as_torsion_submodule() -> None:
    free = BasedFreeModule(ZZ, finite_ordered_set(("g",)))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    module = FinitelyPresentedModule(
        module_homset(relations, free)({"r": 6 * free.module_generator("g")})
    )

    assert module.is_torsion()
    assert not module.is_torsion_free()
    assert module.generic_rank() == 0
    assert module.torsion_submodule().inclusion().is_surjective()


def test_the_generic_fibre_of_a_mixed_module_keeps_only_the_free_rank() -> None:
    free = BasedFreeModule(ZZ, finite_ordered_set(("g", "h")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    module = FinitelyPresentedModule(
        module_homset(relations, free)({"r": 6 * free.module_generator("g")})
    )

    assert module.generic_rank() == 1
    assert not module.is_torsion()
    assert not module.is_torsion_free()
