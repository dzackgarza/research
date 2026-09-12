r"""Serre's two-generator specimen for the live integral special linear group.

Serre, *Trees*, I.4.2 identifies ``SL_2(ZZ)`` with
``C_4 *_{C_2} C_6``.  The archive used the immediate consequences needed by
the preamble: this is an infinite arithmetic group with a selected pair of
generators.
"""

from dzack_research.preamble.all import ZZ, Groups
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFiniteGeneratingSet,
    OwnedFinitelyGeneratedGroups,
)


def test_sl2z_retains_serres_two_generator_arithmetic_specimen() -> None:
    group = Groups.SL(2, ZZ)

    assert group.is_finite() is False
    assert group in OwnedFinitelyGeneratedGroups()
    assert group in GroupsWithChosenFiniteGeneratingSet()
    assert group.number_of_group_generators() == 2
    assert group.group_generators().cardinality() == 2
