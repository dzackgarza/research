r"""Archive reconciliation for finitely presented groups.

The archive conflated finite presentability with carrying one chosen finite
presentation.  The live owner separates those notions while retaining the
presenting free group and defining relators on objects that actually carry the
chosen presentation.
"""

from dzack_research.preamble.all import (
    Groups,
    GroupsWithChosenFinitePresentation,
    OwnedFinitelyPresentedGroups,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/finitely_presented_groups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "disposition": "reconciled-live-owner",
}


def test_finite_presentability_and_chosen_presentation_are_distinct_properties() -> None:
    group = Groups.S(3)

    assert group in OwnedFinitelyPresentedGroups()
    assert group not in GroupsWithChosenFinitePresentation()
    assert group.is_finitely_presented() is True
    assert not hasattr(group, "presenting_free_group")

    presented = group.presentation()
    assert presented is group
    assert presented in GroupsWithChosenFinitePresentation()
    assert presented.presentation() is presented


def test_chosen_presentation_retains_presenting_free_group_and_relators() -> None:
    free = Groups.Free(2)
    first, second = tuple(free.group_generators())
    quotient = free.quotient_by_relators((first**2, second**3, first * second * ~first * ~second))

    assert quotient in GroupsWithChosenFinitePresentation()
    presenting = quotient.presenting_free_group()
    relations = tuple(quotient.defining_relations())

    assert presenting.group_generators().cardinality() == 2
    assert len(relations) == 3
    assert all(relation.parent() is presenting for relation in relations)


def test_native_finite_group_can_retain_a_chosen_finite_presentation() -> None:
    cyclic = Groups.C(2)

    assert cyclic in OwnedFinitelyPresentedGroups()
    assert cyclic not in GroupsWithChosenFinitePresentation()
    presented = cyclic.presentation()
    assert presented in GroupsWithChosenFinitePresentation()
    assert presented.presenting_free_group().group_generators().cardinality() == 1
    assert tuple(relation.Tietze() for relation in presented.defining_relations()) == ((1, 1),)
