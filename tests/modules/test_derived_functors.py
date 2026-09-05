r"""Tor and Ext over the integers and over a polynomial ring, from free resolutions.

``Tor_1(Z/6, Z/4) = Z/2``, ``Ext^1(Z/6, Z) = Z/6``, and both vanish beyond
the length of the resolution; over ``QQ[x]`` the annihilators say which
cyclic module came out.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    Ext,
    FinitelyPresentedModule,
    FreeModule,
    PolynomialRing,
    Tor,
    ring_as_module,
)


def _cyclic(ring, generator):
    r"""The cyclic module ``R / (generator)`` presented by one relation on one generator."""
    line = FreeModule(ring, 1)
    relations = FreeModule(ring, 1)
    return FinitelyPresentedModule(
        relations.Mor(line)({0: ring(generator) * line.module_generator(0)})
    )


def test_tor_over_the_integers_is_the_gcd_and_vanishes_above_the_resolution() -> None:
    six, four, integers = _cyclic(ZZ, 6), _cyclic(ZZ, 4), ring_as_module(ZZ)
    assert Tor(0, six, four).cardinality() == 2
    assert Tor(1, six, four).cardinality() == 2
    assert Tor(2, six, four).cardinality() == 1
    assert Tor(0, six, integers).cardinality() == 6
    assert Tor(1, six, integers).cardinality() == 1
    assert Tor(1, integers, six).cardinality() == 1


def test_ext_over_the_integers() -> None:
    six, four, integers = _cyclic(ZZ, 6), _cyclic(ZZ, 4), ring_as_module(ZZ)
    assert Ext(0, six, integers).cardinality() == 1
    assert Ext(1, six, integers).cardinality() == 6
    assert Ext(0, six, four).cardinality() == 2
    assert Ext(1, six, four).cardinality() == 2
    assert Ext(2, six, four).cardinality() == 1
    assert Ext(0, integers, six).cardinality() == 6
    assert Ext(1, integers, six).cardinality() == 1


def test_tor_remembers_the_tensored_resolution() -> None:
    six, four = _cyclic(ZZ, 6), _cyclic(ZZ, 4)
    tor = Tor(1, six, four)
    tensored = tor.cochain_complex()
    assert tor.cohomological_degree() == 0
    assert tensored.graded_piece(1).tensor_factor(0) is six.free_resolution().term(0)
    assert tensored.graded_piece(0).tensor_factor(0) is six.free_resolution().term(1)
    assert tensored.graded_piece(0).tensor_factor(1) is four
    assert Tor(0, six, four).cochain_complex() is tensored


def test_tor_and_ext_of_cyclic_modules_over_a_polynomial_ring() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    square, line = _cyclic(ring, x**2), _cyclic(ring, x)
    assert tuple(Tor(1, square, line).invariant_factors()) == (x,)
    assert tuple(Tor(0, square, line).invariant_factors()) == (x,)
    assert tuple(Ext(1, square, ring_as_module(ring)).invariant_factors()) == (x**2,)
    assert Ext(0, square, ring_as_module(ring)).invariant_factors().cardinality() == 0
    assert Ext(0, square, ring_as_module(ring)).rank() == 0
