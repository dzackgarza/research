"""Archive reconciliation for open absolute-Galois subgroup ambient data."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/absolute_galois_group_subgroup.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
    "disposition": "reconciled-live-owner",
}


def test_open_subgroup_retains_the_archived_ambient_absolute_galois_group() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    extension = group.finite_extension(2)
    subgroup = group.open_subgroup(extension)

    assert subgroup.ambient() is group
    assert subgroup.supergroup() is group
    assert subgroup.fixed_field() is extension.field()
    assert subgroup.index() == 2


def test_open_subgroup_conjugacy_class_retains_the_same_ambient_group() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    extension = group.finite_extension(3)
    conjugacy_class = group.open_subgroup_class(extension)
    representative = conjugacy_class.representative()

    assert conjugacy_class in Sets()
    assert representative in conjugacy_class
    assert conjugacy_class.ambient() is group
    assert conjugacy_class.supergroup() is group
    assert representative.ambient() is group
    assert representative.conjugacy_class() == conjugacy_class
