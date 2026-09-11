r"""Absolute-Galois realizations use the owned category graph for placement."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import ProfiniteGroups


def test_finite_field_absolute_galois_parent_retains_owned_category_and_geometric_point() -> None:
    field = GF(5)
    group = AbsoluteGaloisGroup(field)

    assert group in AbsoluteGaloisGroups()
    assert group in AbsoluteGaloisGroupsOfFiniteFields()
    assert group in ProfiniteGroups()
    assert group.base_field() is field
    assert group.geometric_point() is group.base_embedding()
    assert group.geometric_point().domain() is field
    assert group.geometric_point().codomain() is group.algebraic_closure()
