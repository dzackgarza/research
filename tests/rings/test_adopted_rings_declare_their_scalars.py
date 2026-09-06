r"""A ring the preamble adopts answers for its scalars from its construction.

An adopted ring reaches the host initializer with no level above it to state
what it is a module over, so it states that itself.  The engine presents the
Gaussian field \(\mathbf{Q}(i)\) over \(\mathbf{Q}\) and the polynomial ring
\(\mathbf{Q}[x]\) over \(\mathbf{Q}\), and those are the scalars; \(\mathbf{Q}\)
is presented over nothing smaller, and a ring is free of rank one over its own
scalars, so it is its own base.

``base`` is the assertion that separates a threaded construction from a
re-derived one: it is what the host was told, so it answers only if the
construction told it.  ``base_ring`` then reads that declaration rather than
crossing back out to the engine to ask a second time.
"""

from dzack_research.preamble.all import (
    QQ,
    Algebras,
    Modules,
    PolynomialRing,
    QuadraticField,
)


def test_an_adopted_number_field_declares_the_rationals_as_its_scalars() -> None:
    gaussian = QuadraticField(-1, "i")

    assert gaussian.base() is QQ
    assert gaussian.base_ring() is QQ
    assert gaussian in Algebras(QQ)
    assert gaussian in Modules(QQ)


def test_an_adopted_polynomial_ring_declares_its_coefficient_ring() -> None:
    polynomials = PolynomialRing(QQ, "x")

    assert polynomials.base() is QQ
    assert polynomials.base_ring() is QQ
    assert polynomials in Modules(QQ)


def test_a_ring_presented_over_nothing_smaller_is_its_own_base() -> None:
    assert QQ.base() is QQ
    assert QQ.base_ring() is QQ
    assert QQ in Modules(QQ)
