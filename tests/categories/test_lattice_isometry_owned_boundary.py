r"""Lattice isometry Mor parents use the owned group category graph."""

from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFinitePresentation,
    OwnedFiniteGroups,
    OwnedGroups,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects


def test_definite_orthogonal_group_has_owned_finite_group_placement() -> None:
    integers = session_ring_objects()["ZZ"]
    orthogonal_group = Lattices(integers)("A2").Aut()

    assert orthogonal_group in OwnedGroups()
    assert orthogonal_group in OwnedFiniteGroups()
    assert orthogonal_group not in GroupsWithChosenFinitePresentation()
    assert orthogonal_group.presentation() in GroupsWithChosenFinitePresentation()


def test_indefinite_orthogonal_group_is_owned_without_false_finiteness() -> None:
    integers = session_ring_objects()["ZZ"]
    orthogonal_group = Lattices(integers)("U").Aut()

    assert orthogonal_group in OwnedGroups()
    assert orthogonal_group not in OwnedFiniteGroups()
    assert orthogonal_group not in GroupsWithChosenFinitePresentation()
