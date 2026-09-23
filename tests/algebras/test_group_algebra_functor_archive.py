r"""Archive reconciliation for the group-ring and underlying-module functors."""

from dzack_research.preamble.all import ZZ, Groups














def test_group_algebra_commutativity_is_available_before_ring_refinement() -> None:
    cyclic_algebra = Groups().group_algebra(ZZ)(Groups.C(2))
    symmetric_algebra = Groups().group_algebra(ZZ)(Groups.S(3))

    assert cyclic_algebra.is_commutative() is True
    assert symmetric_algebra.is_commutative() is False


