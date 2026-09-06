r"""Regular elements and the total quotient ring.

A scalar is regular when it kills nothing nonzero, so regularity is the
vanishing of the colon ideal ``(0 : r)``.  Inverting the regular elements gives
the total quotient ring, the ring a rational function and a Cartier divisor are
stated in, which over an integral domain is the fraction field.
"""

from dzack_research.preamble.all import (
    Fields,
    GF,
    PolynomialRing,
    QQ,
    QuotientRing,
    ZZ,
)


def test_regularity_over_a_domain_is_being_nonzero() -> None:
    assert ZZ(6).is_regular()
    assert not ZZ.zero().is_regular()

    polynomial = PolynomialRing(QQ, "x")
    x = polynomial.algebra_generator("x")

    assert (x**2 - 1).is_regular()


def test_a_zero_divisor_in_a_nonreduced_quotient_is_not_regular() -> None:
    polynomial = PolynomialRing(GF(5), "x,y")
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    quotient = QuotientRing(polynomial, polynomial.ideal(x * y))

    assert not quotient(x).is_regular()
    assert not quotient(y).is_regular()
    assert quotient(x + y).is_regular()


def test_the_total_quotient_ring_of_a_domain_inverts_every_regular_scalar() -> None:
    total = ZZ.total_quotient_ring()

    assert total is ZZ.fraction_field()
    assert total in Fields()
    assert total(ZZ(6)).is_unit()

    polynomial = PolynomialRing(QQ, "x")
    x = polynomial.algebra_generator("x")
    rational_functions = polynomial.total_quotient_ring()

    assert rational_functions(x).is_unit()
