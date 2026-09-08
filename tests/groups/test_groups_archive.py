r"""Archive reconciliation for the generic owned group surface."""

from dzack_research.preamble.all import GF, Groups
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFiniteGeneratingSet,
    GroupsWithChosenFinitePresentation,
    OwnedFiniteGroups,
    OwnedFinitelyGeneratedGroups,
    OwnedFinitelyPresentedGroups,
)


def test_native_group_constructors_cross_into_owned_property_categories() -> None:
    linear = Groups.GL(2, GF(3))
    free = Groups.Free(2)

    assert linear in OwnedFiniteGroups()
    assert free in OwnedFinitelyGeneratedGroups()
    assert free in OwnedFinitelyPresentedGroups()
    assert free in GroupsWithChosenFiniteGeneratingSet()
    assert free in GroupsWithChosenFinitePresentation()
    assert free.is_finitely_generated() is True
    assert free.is_finitely_presented() is True


def test_generated_subgroup_retains_an_actual_inclusion_into_its_supergroup() -> None:
    group = Groups.S(3)
    generator = group.group_generators()[0]
    subgroup = group.subgroup((generator,))
    inclusion = subgroup.inclusion()

    assert subgroup.supergroup() is group
    assert inclusion.domain() is subgroup
    assert inclusion.codomain() is group
    assert inclusion.is_injective()
    assert inclusion(subgroup.group_generators()[0]) in group


def test_conjugation_is_a_group_morphism_into_the_automorphism_group() -> None:
    group = Groups.S(3)
    conjugation = group.conjugation_morphism()
    automorphisms = group.Aut()
    first, second = tuple(group.group_generators())[:2]

    assert conjugation.domain() is group
    assert conjugation.codomain() is automorphisms
    assert conjugation(first).parent() is automorphisms
    assert conjugation(first * second) == conjugation(first) * conjugation(second)


def test_endomorphisms_of_an_abelian_group_form_the_live_endomorphism_ring() -> None:
    group = Groups.Abelian([3])
    endomorphisms = group.endomorphism_ring()
    one = endomorphisms.one()
    zero = endomorphisms.zero()
    twice = one + one

    assert endomorphisms.domain() is group
    assert endomorphisms.codomain() is group
    for element in group:
        assert one(element) == element
        assert zero(element) == group.one()
        assert twice(element) == element * element
        assert (twice * twice)(element) == twice(twice(element))
