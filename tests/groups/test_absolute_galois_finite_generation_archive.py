r"""Archive reconciliation for algebraic finite generation of absolute Galois groups."""

from dzack_research.preamble.all import QQ, QuadraticField
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_rational_absolute_galois_group_is_not_algebraically_finitely_generated() -> None:
    group = AbsoluteGaloisGroup(QQ)

    assert group.is_finitely_generated() is False
    assert group.group_generators_are_computable() is False


def test_number_field_absolute_galois_group_is_not_algebraically_finitely_generated() -> None:
    field = QuadraticField(5, "a")
    group = AbsoluteGaloisGroup(field)

    assert group.is_finitely_generated() is False
    assert group.group_generators_are_computable() is False
