r"""Owned group constructions meet their mathematical categories without Sage joins."""

from dzack_research.preamble.categories.group.groups import (
    GroupAutomorphismGroups,
    OwnedFiniteGroups,
    OwnedGroups,
    Subgroups,
)
from dzack_research.preamble.categories.group.magmas import Monoids


def test_engine_backed_finite_group_keeps_owned_finite_placement() -> None:
    group = OwnedGroups().S(3)

    assert group in OwnedGroups()
    assert group in OwnedFiniteGroups()


def test_transported_subgroup_keeps_owned_subgroup_and_group_placement() -> None:
    group = OwnedGroups().S(3)
    generator = group.group_generators()[0]
    subgroup = group.subgroup((generator,))

    assert subgroup in OwnedGroups()
    assert subgroup in Subgroups(group)
    assert subgroup.supergroup() is group


def test_endomorphism_mor_and_automorphism_group_keep_owned_placements() -> None:
    group = OwnedGroups().S(3)
    endomorphisms = group.Mor(group)
    automorphisms = group.Aut()

    assert endomorphisms in Monoids()
    assert automorphisms in GroupAutomorphismGroups()
    assert automorphisms in OwnedFiniteGroups()


def test_catalogue_engines_are_not_categories_of_their_encodings() -> None:
    from dzack_research.preamble.categories.group.groups import GroupsWithChosenFreeBasis
    from dzack_research.preamble.categories.sets import NN

    for group in (OwnedGroups().S(3), OwnedGroups().Free(2), OwnedGroups().Free(index_set=NN)):
        assert group in OwnedGroups()
        assert group.one() * group.one() == group.one()
    free = OwnedGroups().Free(2)
    assert free in GroupsWithChosenFreeBasis()
    x, y = free.group_generators()
    identity = free.Mor(free)(free.free_generator)
    assert identity(x * y**-1 * x) == x * y**-1 * x


def test_subgroup_elements_and_inclusion_retain_the_ambient_group() -> None:
    group = OwnedGroups().S(3)
    subgroup = group.subgroup((group.group_generators()[0],))
    for element in subgroup:
        assert element.parent() is group
        assert subgroup.inclusion()(element) is element
        assert subgroup(element) is element
    assert subgroup.order() == subgroup.cardinality()
