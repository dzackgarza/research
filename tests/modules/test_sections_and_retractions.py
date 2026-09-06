r"""One-sided inverses of module morphisms.

A section of an epimorphism chooses a preimage of each generator of the
codomain, and those choices assemble into a morphism when the codomain is
free.  A retraction of a monomorphism is built from a section of the quotient
by its image: every element differs from its chosen lift by something in the
image, and the monomorphism is injective there.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_a_projection_off_a_free_summand_has_a_section() -> None:
    plane = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    line = BasedFreeModule(ZZ, finite_ordered_set(("c",)))
    projection = module_homset(plane, line)(
        {"a": line.module_generator("c"), "b": line.zero()}
    )

    section = projection.section()

    assert section.domain() is line
    assert section.codomain() is plane
    assert projection(section(line.module_generator("c"))) == line.module_generator("c")
    assert projection(section(3 * line.module_generator("c"))) == 3 * line.module_generator("c")


def test_a_split_inclusion_has_a_retraction_that_is_the_identity_on_the_source() -> None:
    plane = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    line = BasedFreeModule(ZZ, finite_ordered_set(("c",)))
    inclusion = module_homset(line, plane)({"c": plane.module_generator("a")})

    retraction = inclusion.retraction()

    assert retraction.domain() is plane
    assert retraction.codomain() is line
    assert retraction(inclusion(line.module_generator("c"))) == line.module_generator("c")
    assert retraction(plane.module_generator("b")) == line.zero()


def test_the_cokernel_projection_kills_exactly_the_image() -> None:
    plane = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    line = BasedFreeModule(ZZ, finite_ordered_set(("c",)))
    inclusion = module_homset(line, plane)({"c": plane.module_generator("a")})

    projection = inclusion.cokernel_projection()

    assert projection.codomain() is inclusion.cokernel()
    assert projection(plane.module_generator("a")) == projection.codomain().zero()
    assert projection(plane.module_generator("b")) != projection.codomain().zero()


def test_a_presented_module_with_no_torsion_is_recognised_as_free() -> None:
    free = BasedFreeModule(ZZ, finite_ordered_set(("g", "h")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    torsion_free = FinitelyPresentedModule(
        module_homset(relations, free)({"r": free.module_generator("g")})
    )
    with_torsion = FinitelyPresentedModule(
        module_homset(relations, free)({"r": 6 * free.module_generator("g")})
    )

    assert torsion_free.is_free()
    assert not with_torsion.is_free()
