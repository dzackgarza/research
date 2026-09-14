r"""Owned group constructions meet their mathematical categories without Sage joins."""

from dzack_research.preamble.categories.group.groups import (
    GroupAutomorphismGroups,
    OwnedFiniteGroups,
    OwnedGroups,
    Subgroups,
    group_homset,
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


def test_endomorphism_hom_and_automorphism_group_keep_owned_placements() -> None:
    group = OwnedGroups().S(3)
    endomorphisms = group_homset(group, group)
    automorphisms = group.Aut()

    assert endomorphisms in Monoids()
    assert automorphisms in GroupAutomorphismGroups()
    assert automorphisms in OwnedFiniteGroups()
