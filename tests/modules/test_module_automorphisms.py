r"""An automorphism is an element of the automorphism group, not a kind of map.

The Mor packet already gives every object its endomorphism ring and its
automorphism group, so a module reaches them the way a group and a lattice do.
An invertible endomorphism becomes an element of that group by supplying the
inverse it constructs, and the inverse is the section construction with nothing
left to choose.
"""

from dzack_research.preamble.all import (
    ZZ,
    Modules,
)

from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/module_morphisms/module_morphisms.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    "owner_overrides": {
        "FramedAutomorphismSubgroup": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "AutomorphismSubgroup": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "ModuleAutomorphismGroups": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
        "ModuleAutomorphismGroup": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
        "ModuleAutomorphism.cyclic_subgroup": "src/dzack_research/preamble/categories/group/groups.py",
        "GroupAction": "src/dzack_research/preamble/categories/modules/group_modules/group_modules.py",
        "GroupActionHomsets": "src/dzack_research/preamble/categories/modules/group_modules/group_modules.py",
        "GroupActionHomset": "src/dzack_research/preamble/categories/modules/group_modules/group_modules.py",
        "group_action_homset": "src/dzack_research/preamble/categories/modules/group_modules/group_modules.py",
        "AutomorphismSubgroupInclusion": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
    },
    "disposition": "reconciled-live-owner",
}


def _plane():
    return ZZ.free_module(finite_ordered_set(("a", "b")))


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
    swap = plane.module_category().Mor(plane, plane)(
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
    doubling = plane.module_category().Mor(plane, plane)(
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


def test_a_nonidentity_module_automorphism_generates_the_generic_cyclic_subgroup() -> None:
    plane = _plane()
    swap = plane.module_category().Mor(plane, plane)(
        {"a": plane.module_generator("b"), "b": plane.module_generator("a")}
    ).as_automorphism()
    generated = swap.cyclic_subgroup()

    assert generated.supergroup() is plane.Aut()
    assert generated.selected_generator() is swap
    assert generated.order() == 2
    assert swap in generated
    assert plane.Aut().identity_automorphism() in generated


def test_a_finite_presented_module_automorphism_uses_actual_finite_preimages() -> None:
    free = ZZ.free_module(finite_ordered_set(("g",)))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    quotient = relations.module_category().Mor(relations, free)({"r": 3 * free.module_generator("g")}).cokernel()
    generator = quotient.module_generator("g")
    negation = quotient.module_category().Mor(quotient, quotient)({"g": -generator}).as_automorphism()

    assert negation.parent() is quotient.Aut()
    assert negation(generator) == -generator
    assert negation.inverse() == negation
    assert negation * negation == quotient.Aut().one()
