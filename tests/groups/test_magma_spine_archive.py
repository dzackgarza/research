r"""Archive reconciliation for the owned multiplicative/additive operation spines."""

from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMagmas,
    AdditiveMonoids,
    AdditiveSemigroups,
    Magmas,
    Monoids,
    Semigroups,
)
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/magmas.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/magmas.py",
    "disposition": "reconciled-live-owner",
}


def test_owned_groups_flow_through_the_multiplicative_operation_spine() -> None:
    group = OwnedGroups().C(5)
    generator = group.group_generators()[0]

    assert group in OwnedGroups()
    assert group in Monoids()
    assert group in Semigroups()
    assert group in Magmas()
    assert group in Sets()
    assert generator**3 == generator * generator * generator


def test_the_additive_operation_spine_keeps_each_structural_level() -> None:
    assert AdditiveGroups().is_subcategory(AdditiveMonoids())
    assert AdditiveMonoids().is_subcategory(AdditiveSemigroups())
    assert AdditiveSemigroups().is_subcategory(AdditiveMagmas())
    assert AdditiveMagmas().is_subcategory(Sets())


def test_monoid_identity_morphism_is_an_actual_owned_map() -> None:
    group = OwnedGroups().C(5)
    identity = Monoids().Mor(group, group).identity()
    generator = group.group_generators()[0]

    assert identity.domain() is group
    assert identity.codomain() is group
    assert identity(generator) == generator
