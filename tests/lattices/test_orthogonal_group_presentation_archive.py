r"""Finite orthogonal-group presentations retained from the archive gap map.

The archived known-mathematics suite uses ``O(A4)`` as the finite arithmetic
group specimen.  Conway--Sloane gives its order ``240``; the live lattice
engine already supplies four selected isometry generators.  A finite group is
finitely presented, and Sage's finite matrix-group engine constructs an FP
group from the corresponding permutation generators, so the owned orthogonal
group retains an actual chosen presentation rather than only the theorem that
some presentation exists.
"""

from dzack_research.preamble.all import Lattices
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFinitePresentation,
    OwnedFinitelyPresentedGroups,
)


def test_o_a4_retains_a_chosen_finite_presentation_on_its_selected_generators() -> None:
    orthogonal_group = Lattices.A4.Aut()
    selected_generators = orthogonal_group.group_generators()

    assert orthogonal_group.order() == 240
    assert selected_generators.cardinality() == 4
    assert orthogonal_group in OwnedFinitelyPresentedGroups()
    assert orthogonal_group in GroupsWithChosenFinitePresentation()

    presenting = orthogonal_group.presenting_free_group()
    relations = orthogonal_group.defining_relations()
    assert presenting.group_generators().cardinality() == selected_generators.cardinality()
    assert relations.cardinality() > 0
