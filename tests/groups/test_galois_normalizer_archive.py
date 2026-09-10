r"""Archive reconciliation for normalizers of open absolute-Galois subgroups."""

from dzack_research.preamble.all import NumberField, PolynomialRing, QQ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_nongalois_cubic_has_trivial_open_subgroup_normalizer_quotient() -> None:
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.gen()
    cubic = NumberField(x**3 - QQ(2), "a")
    absolute = AbsoluteGaloisGroup(QQ)
    subgroup = absolute.open_subgroup(cubic)
    quotient = subgroup.normalizer_quotient()

    assert subgroup.index() == 3
    assert not subgroup.is_normal()
    assert quotient.order() == 1
    assert quotient.one().action().domain() is cubic
    assert quotient.one().action().codomain() is cubic


def test_quadratic_open_subgroup_normalizer_quotient_is_its_galois_group() -> None:
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.gen()
    quadratic = NumberField(x**2 - QQ(5), "a")
    absolute = AbsoluteGaloisGroup(QQ)
    subgroup = absolute.open_subgroup(quadratic)
    quotient = subgroup.normalizer_quotient()

    assert subgroup.index() == 2
    assert subgroup.is_normal()
    assert quotient.order() == 2
    assert quotient.group_generators().cardinality() == 1
    generator = quotient.group_generators()[0]
    assert generator * generator == quotient.one()
