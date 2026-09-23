r"""Torsion computed from its definition, not read off a decomposition.

Over an integral domain ``R`` with fraction field ``K``, the torsion submodule
of ``M`` is the kernel of the unit ``M -> K tensor_R M`` of scalar extension,
and ``M`` is torsion exactly when that generic fibre vanishes.  Both statements
hold over any domain; the invariant-factor reading of them is a principal
ideal domain's shortcut, not the definition.
"""

from dzack_research.preamble.all import (
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set






def test_a_finite_abelian_group_is_torsion_with_itself_as_torsion_submodule() -> None:
    free = ZZ.free_module(finite_ordered_set(("g",)))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    module = relations.module_category().Mor(relations, free)({"r": 6 * free.module_generator("g")}).cokernel()

    assert module.is_torsion()
    assert not module.is_torsion_free()
    assert module.generic_rank() == 0
    assert module.torsion_submodule().inclusion().is_surjective()


def test_the_generic_fibre_of_a_mixed_module_keeps_only_the_free_rank() -> None:
    free = ZZ.free_module(finite_ordered_set(("g", "h")))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    module = relations.module_category().Mor(relations, free)({"r": 6 * free.module_generator("g")}).cokernel()

    assert module.generic_rank() == 1
    assert not module.is_torsion()
    assert not module.is_torsion_free()
