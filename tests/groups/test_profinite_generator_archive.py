"""Archive reconciliation for topological versus algebraic Galois generators."""


from dzack_research.preamble.all import GF
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


