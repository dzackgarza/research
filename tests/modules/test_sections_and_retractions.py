r"""One-sided inverses of module morphisms.

A section of an epimorphism chooses a preimage of each generator of the
codomain, and those choices assemble into a morphism when the codomain is
free.  A retraction of a monomorphism is built from a section of the quotient
by its image: every element differs from its chosen lift by something in the
image, and the monomorphism is injective there.
"""

from dzack_research.preamble.all import (
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set








def test_a_presented_module_with_no_torsion_is_recognised_as_free() -> None:
    free = ZZ.free_module(finite_ordered_set(("g", "h")))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    torsion_free = relations.module_category().Mor(relations, free)({"r": free.module_generator("g")}).cokernel()
    with_torsion = relations.module_category().Mor(relations, free)({"r": 6 * free.module_generator("g")}).cokernel()

    assert torsion_free.is_free()
    assert not with_torsion.is_free()
