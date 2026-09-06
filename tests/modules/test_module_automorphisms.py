r"""An automorphism is an element of the automorphism group, not a kind of map.

The Hom packet already gives every object its endomorphism ring and its
automorphism group, so a module reaches them the way a group and a lattice do.
An invertible endomorphism becomes an element of that group by supplying the
inverse it constructs, and the inverse is the section construction with nothing
left to choose.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    Modules,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _plane():
    return BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))


def test_a_module_reaches_its_endomorphism_ring_and_automorphism_group() -> None:
    plane = _plane()

    assert plane.End() is Modules(ZZ).End(plane)
    assert plane.Aut() is Modules(ZZ).Aut(plane)


def test_the_identity_automorphism_fixes_every_generator() -> None:
    plane = _plane()

    identity = plane.Aut().identity_automorphism()

    assert identity(plane.module_generator("a")) == plane.module_generator("a")
    assert identity(plane.module_generator("b")) == plane.module_generator("b")


def test_a_swap_is_its_own_inverse_and_is_an_element_of_the_automorphism_group() -> None:
    plane = _plane()
    swap = module_homset(plane, plane)(
        {"a": plane.module_generator("b"), "b": plane.module_generator("a")}
    )

    inverse = swap.inverse()

    assert inverse(plane.module_generator("a")) == plane.module_generator("b")
    assert swap(inverse(plane.module_generator("a"))) == plane.module_generator("a")

    automorphism = swap.as_automorphism()

    assert automorphism.parent() is plane.Aut()
    assert automorphism(plane.module_generator("a")) == plane.module_generator("b")
    assert (automorphism * automorphism)(
        plane.module_generator("a")
    ) == plane.module_generator("a")


def test_a_non_invertible_endomorphism_has_no_inverse() -> None:
    plane = _plane()
    doubling = module_homset(plane, plane)(
        {
            "a": 2 * plane.module_generator("a"),
            "b": 2 * plane.module_generator("b"),
        }
    )

    try:
        doubling.inverse()
    except AssertionError as error:
        assert "two-sided inverse" in str(error)
    else:
        raise AssertionError("doubling is not surjective on a free ZZ-module")
