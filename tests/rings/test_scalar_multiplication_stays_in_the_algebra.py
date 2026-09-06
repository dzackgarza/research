r"""A scalar times an element of an algebra over it answers in the algebra.

For an algebra \(A\) over \(R\) with structure map \(\eta\), the product
\(r\cdot a\) is \(\eta(r)a\), an element of \(A\).  This is the case the
registered scalar action does not reach: the coercion model finds that action
only when the scalar's own multiplication defers, and it cannot defer for an
element the scalar ring can name.  The identity of the Gaussian field and the
constant polynomials are exactly such elements, so the assertion is the parent
of the product.

Multiplying by a generator would not distinguish the two answers -- the scalar
ring cannot name \(i\), so it defers there and the product is Gaussian either
way.  The identity is the specimen that separates them.
"""

from dzack_research.preamble.all import (
    QQ,
    PolynomialRing,
    QuadraticField,
)


def test_a_rational_times_the_identity_of_the_gaussian_field_is_gaussian() -> None:
    gaussian = QuadraticField(-1, "i")
    product = QQ(3) * gaussian.one()

    assert product.parent() is gaussian
    assert product == gaussian(3)


def test_a_rational_times_a_constant_polynomial_is_a_polynomial() -> None:
    polynomials = PolynomialRing(QQ, "x")
    product = QQ(3) * polynomials.one()

    assert product.parent() is polynomials
    assert product == polynomials(3)
