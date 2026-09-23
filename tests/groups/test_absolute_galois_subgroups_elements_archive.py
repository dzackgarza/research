r"""Archive reconciliation for absolute-Galois elements and open subgroups.

The archive realized an element progressively from finite stages.  The live
owner strengthens that invariant: an element has a globally exact action (or
the canonical finite-field Frobenius action), while compatible finite
coordinates may still be retained and restricted.  Open subgroups retain the
same Galois-correspondence data and actual inclusion maps.
"""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)




def test_open_subgroup_is_the_actual_subgroup_fixing_its_extension() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    subgroup = group.open_subgroup(group.finite_extension(2))

    assert subgroup.supergroup() is group
    assert subgroup.index() == 2
    assert subgroup.is_normal()
    assert subgroup.fixed_field() is subgroup.fixed_extension().field()
    assert frobenius not in subgroup
    assert frobenius**2 in subgroup

    inclusion = subgroup.inclusion()
    assert inclusion.domain() is subgroup
    assert inclusion.codomain() is group
    assert inclusion.is_injective()
    assert inclusion(subgroup.frobenius()) == frobenius**2


def test_open_subgroup_intersection_and_conjugacy_class_follow_field_correspondence() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    index_two = group.open_subgroup(group.finite_extension(2))
    index_three = group.open_subgroup(group.finite_extension(3))
    intersection = index_two.intersection(index_three)

    assert intersection.index() == 6
    assert intersection <= index_two
    assert intersection <= index_three

    conjugacy_class = index_two.conjugacy_class()
    assert conjugacy_class.supergroup() is group
    assert conjugacy_class.index() == 2
    assert conjugacy_class.representative().index() == 2
    assert conjugacy_class == group.open_subgroup_class(index_two.fixed_field())
