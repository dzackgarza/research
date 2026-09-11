r"""Archive reconciliation for the absolute Galois group as a field construction."""

from dzack_research.preamble.all import GF, QQ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_field_constructs_the_existing_absolute_galois_group() -> None:
    for field in (GF(5), QQ):
        group = field.absolute_galois_group()

        assert group is AbsoluteGaloisGroup(field)
        assert group.base_field() is field


def test_finite_field_construction_retains_the_procyclic_specialization() -> None:
    field = GF(7)
    group = field.absolute_galois_group()

    assert group.is_abelian() is True
    assert group.topological_generating_family().cardinality() == 1
