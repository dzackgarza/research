"""Archive reconciliation for absolute-Galois element realization semantics."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/absolute_galois_group_element.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
    "disposition": "reconciled-live-owner",
}


def test_finite_stage_action_is_exposed_as_an_exact_restriction_coordinate() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    stage = group.finite_extension(2)
    frobenius = group.frobenius()
    restriction = frobenius.restrict(stage)

    assert restriction.parent() is group.finite_quotient(stage)
    assert restriction == group.restriction_map(stage)(frobenius)
    assert frobenius.parent() is group
    assert frobenius.domain() is group.algebraic_closure()
    assert frobenius.codomain() is group.algebraic_closure()


def test_element_conjugacy_class_retains_the_archived_ambient_group() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    conjugacy_class = frobenius.conjugacy_class()

    assert conjugacy_class in Sets().Subobjects(group)
    assert conjugacy_class.inclusion().codomain() is group
    assert conjugacy_class.ambient() is group
    assert conjugacy_class.supergroup() is group
    assert conjugacy_class.representative() is frobenius
