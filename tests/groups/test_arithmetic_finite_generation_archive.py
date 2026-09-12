r"""Arithmetic finite-generation facts retained from the archive gap map.

Hua--Reiner give finite generating sets for the integral general linear and
symplectic groups; Borel--Harish-Chandra places these examples in the general
finite-generation theorem for arithmetic groups.  The owned category records
that theorem-level property independently of whether a chosen generator list
is currently materialized.
"""

from dzack_research.preamble.all import ZZ, Groups
from dzack_research.preamble.categories.group.groups import (
    OwnedFinitelyGeneratedGroups,
)


def test_integral_classical_groups_are_arithmetic_and_finitely_generated() -> None:
    groups = (
        Groups.SL(2, ZZ),
        Groups.GL(3, ZZ),
        Groups.GL(4, ZZ),
        Groups.Sp(4, ZZ),
    )

    for group in groups:
        assert group.is_arithmetic_group() is True
        assert group in OwnedFinitelyGeneratedGroups()
        assert group.is_finitely_generated() is True
