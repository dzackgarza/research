r"""Archive reconciliation for the realized absolute-Galois parent."""

from dzack_research.preamble.all import GF, QQ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_the_base_embedding_is_the_geometric_point_of_the_realization() -> None:
    group = AbsoluteGaloisGroup(QQ)

    assert group.geometric_point() is group.base_embedding()
    assert group.geometric_point().domain() is QQ
    assert group.geometric_point().codomain() is group.algebraic_closure()


def test_finite_fields_have_the_canonical_frobenius_realization() -> None:
    group = AbsoluteGaloisGroup(GF(5))

    assert group.has_canonical_realization() is True
    assert tuple(group.topological_group_generators()) == (group.frobenius(),)


def test_general_fields_retain_a_chosen_not_canonical_realization() -> None:
    group = AbsoluteGaloisGroup(QQ)

    assert group.has_canonical_realization() is False
    assert group.base_embedding().domain() is QQ
    assert group.base_embedding().codomain() is group.algebraic_closure()
