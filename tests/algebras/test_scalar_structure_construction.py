r"""Distinct scalar maps define distinct algebra structures without changing the ring."""

from dzack_research.preamble.all import Algebras, OwnedRings, QQ, ZZ


def test_two_scalar_maps_retain_their_actual_actions_and_original_base() -> None:
    parameter = QQ.polynomial_ring("t")
    polynomials = QQ.polynomial_ring("x")
    t = parameter.algebra_generator("t")
    x = polynomials.algebra_generator("x")
    first = parameter.Mor(polynomials)({"t": x}).as_algebra()
    shifted = parameter.Mor(polynomials)({"t": x + polynomials.one()}).as_algebra()

    assert first is not shifted
    assert first.base_ring() is parameter
    assert shifted.base_ring() is parameter
    assert polynomials.base_ring() is QQ
    assert first in Algebras(parameter)
    assert first not in Algebras(first)
    assert first not in Algebras(ZZ)
    assert first.scalar_multiple(t, first.one()) == first(x)
    assert shifted.scalar_multiple(t, shifted.one()) == shifted(x + polynomials.one())
    assert first.algebra_structure_morphism()(t) == first(x)
    assert shifted.algebra_structure_morphism()(t) == shifted(x + polynomials.one())
    underlying = first.unformed_module()
    shifted_underlying = shifted.unformed_module()
    assert underlying is not first
    assert underlying.base_ring() is parameter
    assert underlying.underlying_set() is polynomials
    assert underlying.scalar_multiple(t, underlying(polynomials.one())) == underlying(x)
    assert shifted_underlying.scalar_multiple(t, shifted_underlying(polynomials.one())) == shifted_underlying(x + polynomials.one())
    assert underlying(first(x)) == underlying(x)
    assert first(underlying(x)) == first(x)
    assert first.multiplication()(underlying(x), underlying(x)) == underlying(x**2)
    assert first.multiplication_morphism()(first(x), first(x)) == first(x**2)


def test_relative_ring_self_algebra_does_not_replace_its_original_scalars() -> None:
    polynomials = QQ.polynomial_ring("x")
    x = polynomials.algebra_generator("x")
    identity = OwnedRings().Mor(polynomials, polynomials).identity()
    regular = identity.as_algebra()

    assert regular.base_ring() is polynomials
    assert polynomials.base_ring() is QQ
    assert regular.scalar_multiple(x, regular.one()) == regular(x)
    assert regular.algebra_structure_morphism()(x) == regular(x)
    assert regular.unit_morphism().domain() is regular
    assert regular.unit_morphism()(regular(x)) == regular(x)
