r"""Scalar-linearity of an elementwise map is decided on a ring generating set.

An additive map already commutes with every integer, and the scalars it
commutes with are closed under sums and products, so they form a subring.  A
generating set of the ring therefore decides scalar-linearity, and the scalar
ring itself need not be finite.

The witness is Frobenius on ``GF(3)[x]/(x^3-1)``, read as a module over
``GF(3)[x]``.  Cubing is additive in characteristic three and fixes every
constant, so every check available before this one accepts it.  It is not
``x``-linear: it sends ``x`` to ``x^3 = 1`` while ``x`` times its value at one
is ``x``.
"""

from dzack_research.preamble.all import (
    GF,
    GeneralModule,
    PolynomialRing,
    Set,
    module_homset,
)


def _group_algebra_of_the_cyclic_group_of_order_three():
    r"""Return ``GF(3)[x]`` and ``GF(3)[x]/(x^3-1)`` as a module over it."""
    ring = PolynomialRing(GF(3), "x")
    x = ring.algebra_generator("x")
    quotient = ring.quotient_ring(ring.ideal(x**3 - ring.one()))
    project = quotient.quotient_map()
    module = GeneralModule(
        ring,
        Set(quotient),
        addition=lambda left, right: left + right,
        zero=quotient.zero(),
        negation=lambda value: -value,
        scalar_action=lambda scalar, value: project(scalar) * value,
    )
    return ring, quotient, module


def test_a_scalar_multiple_is_linear_over_the_infinite_ring() -> None:
    _ring, quotient, module = _group_algebra_of_the_cyclic_group_of_order_three()

    doubling = module_homset(module, module).elementwise(
        lambda element: module(quotient(2) * element.underlying_element())
    )

    assert doubling(module(quotient.one())) == module(quotient(2))


def test_frobenius_is_additive_but_is_rejected_as_not_x_linear() -> None:
    _ring, quotient, module = _group_algebra_of_the_cyclic_group_of_order_three()

    try:
        module_homset(module, module).elementwise(
            lambda element: module(element.underlying_element() ** 3)
        )
    except ValueError as error:
        assert "not scalar-linear" in str(error)
    else:
        raise AssertionError(
            "cubing is additive and fixes the constants, so only the check on x rejects it"
        )
