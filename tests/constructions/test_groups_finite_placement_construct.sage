r"""Group orbit and coset notions remain visible above the finite axiom."""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_group_orbit_and_coset_operations_are_sited_on_groups() -> None:
    group = Groups.Free(2)

    assert group in Groups()
    assert group not in Groups().Finite()

    with pytest.raises(AssertionError, match="conjugation action.*defined for every group"):
        group.conjugation_g_set()
    with pytest.raises(AssertionError, match="conjugacy classes.*defined for every group"):
        group.conjugacy_classes()
    with pytest.raises(AssertionError, match="conjugacy class.*defined"):
        group.conjugacy_class(group.one())
    with pytest.raises(AssertionError, match="left cosets.*defined"):
        group.left_cosets(group)
    with pytest.raises(AssertionError, match="right cosets.*defined"):
        group.right_cosets(group)
