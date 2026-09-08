r"""Archive reconciliation for the category of realized absolute Galois groups."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)


def test_realized_absolute_galois_group_retains_basepoint_coslice_data() -> None:
    field = GF(5)
    group = AbsoluteGaloisGroup(field)
    embedding = group.base_embedding()
    extension_object = group.extension_object()

    assert group in OwnedGroups()
    assert group in AbsoluteGaloisGroups()
    assert group in ProfiniteGroups()
    assert group.base_field() is field
    assert embedding.domain() is field
    assert embedding.codomain() is group.algebraic_closure()
    assert extension_object.category() is group.slice_category()


def test_absolute_galois_element_is_the_automorphism_square_of_the_slice_object() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    square = group.slice_automorphism(frobenius)

    assert square.domain() is group.extension_object()
    assert square.codomain() is group.extension_object()
    left, right = square.components()
    assert left.domain() is group.base_field()
    assert left.codomain() is group.base_field()
    assert right == frobenius.as_morphism()


def test_finite_field_absolute_galois_group_refines_to_procyclic_specialization() -> None:
    group = AbsoluteGaloisGroup(GF(5))

    assert group in AbsoluteGaloisGroupsOfFiniteFields()
    assert group.is_profinite() is True
    assert group.is_abelian() is True
    assert group.is_finite() is False
    assert tuple(group.topological_group_generators()) == (group.frobenius(),)
