"""Archive reconciliation for explicit absolute-Galois realization data."""

from dzack_research.preamble.all import GF, QQ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_realization_choice_data_is_exactly_the_retained_closure_and_embedding() -> None:
    group = AbsoluteGaloisGroup(QQ)
    data = group.choice_data()

    assert set(data) == {"closure", "embedding"}
    assert data["closure"] is group.algebraic_closure()
    assert data["embedding"] is group.base_embedding()
    assert group.geometric_point() is group.base_embedding()
    assert group.has_canonical_realization() is False


def test_finite_field_realization_keeps_the_same_data_but_is_canonical() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    data = group.choice_data()

    assert data["closure"] is group.algebraic_closure()
    assert data["embedding"] is group.base_embedding()
    assert group.has_canonical_realization() is True
