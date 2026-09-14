"""Archive reconciliation for topological versus algebraic Galois generators."""

from dzack_research.preamble.all import GF, QQ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_finite_field_frobenius_is_owned_topological_not_algebraic_generation() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    generators = group.topological_group_generators()
    family = group.topological_generating_family()

    assert generators.cardinality() == 1
    assert tuple(generators) == (group.frobenius(),)
    assert family.cardinality() == 1
    assert tuple(family) == tuple(generators)
    assert group.is_finitely_generated() is False
    assert group.group_generators_are_computable() is False
    assert group.has_computed_group_generators() is False


def test_general_absolute_galois_group_does_not_fabricate_topological_generators() -> None:
    group = AbsoluteGaloisGroup(QQ)

    assert group.group_generators_are_computable() is False
    assert group.has_computed_group_generators() is False
    try:
        group.topological_generating_family()
    except NotImplementedError:
        pass
    else:
        raise AssertionError("G_Q must not fabricate a selected topological generating family")
