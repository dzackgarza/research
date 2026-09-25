r"""Base change of a scheme to the completion preserves its relative geometry."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_affine_line_base_changes_to_the_completed_local_base() -> None:
    local = ZZ.localize_at_prime(5)
    line = AffineSpaces(local)(1)
    completed = line.base_change_to_completion()
    special = completed.special_fiber()

    assert completed.scheme_base_ring() in CompleteLocalRings()
    assert completed.relative_dimension() == 1
    assert special.relative_dimension() == 1
    assert special.point_count() == 5
