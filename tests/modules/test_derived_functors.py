r"""Tor and Ext over the integers and over a polynomial ring, from free resolutions.

``Tor_1(Z/6, Z/4) = Z/2``, ``Ext^1(Z/6, Z) = Z/6``, and both vanish beyond
the length of the resolution; over ``QQ[x]`` the annihilators say which
cyclic module came out.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
)


def _cyclic(ring, generator):
    r"""The cyclic module ``R / (generator)`` presented by one relation on one generator."""
    line = ring.free_module(1)
    relations = ring.free_module(1)
    return relations.Mor(line)({0: ring(generator) * line.module_generator(0)}).cokernel()


def test_tor_over_the_integers_is_the_gcd_and_vanishes_above_the_resolution() -> None:
    six, four, integers = _cyclic(ZZ, 6), _cyclic(ZZ, 4), ZZ.regular_module()
    assert six.tor(four, degree=0).cardinality() == 2
    assert six.tor(four, degree=1).cardinality() == 2
    assert six.tor(four, degree=2).cardinality() == 1
    assert six.tor(integers, degree=0).cardinality() == 6
    assert six.tor(integers, degree=1).cardinality() == 1
    assert integers.tor(six, degree=1).cardinality() == 1


def test_ext_over_the_integers() -> None:
    six, four, integers = _cyclic(ZZ, 6), _cyclic(ZZ, 4), ZZ.regular_module()
    assert six.ext(integers, degree=0).cardinality() == 1
    assert six.ext(integers, degree=1).cardinality() == 6
    assert six.ext(four, degree=0).cardinality() == 2
    assert six.ext(four, degree=1).cardinality() == 2
    assert six.ext(four, degree=2).cardinality() == 1
    assert integers.ext(six, degree=0).cardinality() == 6
    assert integers.ext(six, degree=1).cardinality() == 1


def test_tor_remembers_the_tensored_resolution() -> None:
    six, four = _cyclic(ZZ, 6), _cyclic(ZZ, 4)
    tor = six.tor(four, degree=1)
    tensored = tor.cochain_complex()
    assert tor.cohomological_degree() == 0
    assert tensored.graded_piece(1).tensor_factor(0) is six.free_resolution().term(0)
    assert tensored.graded_piece(0).tensor_factor(0) is six.free_resolution().term(1)
    assert tensored.graded_piece(0).tensor_factor(1) is four
    assert six.tor(four, degree=0).cochain_complex() is tensored


def test_tor_and_ext_of_cyclic_modules_over_a_polynomial_ring() -> None:
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    square, line = _cyclic(ring, x**2), _cyclic(ring, x)
    assert tuple(square.tor(line, degree=1).invariant_factors()) == (x,)
    assert tuple(square.tor(line, degree=0).invariant_factors()) == (x,)
    assert tuple(square.ext(ring.regular_module(), degree=1).invariant_factors()) == (x**2,)
    assert square.ext(ring.regular_module(), degree=0).invariant_factors().cardinality() == 0
    assert square.ext(ring.regular_module(), degree=0).module_rank() == 0


def test_tor_and_ext_are_functorial_in_the_resolved_argument() -> None:
    six = _cyclic(ZZ, 6)
    three = _cyclic(ZZ, 3)
    two = _cyclic(ZZ, 2)
    quotient = six.Mor(three)({0: three.module_generator(0)})

    tor_source = six.tor(two, degree=1)
    tor_target = three.tor(two, degree=1)
    tor_map = quotient.tor_map(two, degree=1)
    cycle_module = tor_source.cochain_complex().graded_piece(tor_source.degree())
    cycle_label = next(iter(cycle_module.module_generating_set()))
    tor_class = tor_source.class_of_cycle(cycle_module.module_generator(cycle_label))
    assert tor_map.domain() is tor_source
    assert tor_map.codomain() is tor_target
    assert tor_map(tor_class).parent() is tor_target

    integers = ZZ.regular_module()
    ext_source = three.ext(integers, degree=1)
    ext_target = six.ext(integers, degree=1)
    ext_map = quotient.ext_map(integers, degree=1)
    assert ext_map.domain() is ext_source
    assert ext_map.codomain() is ext_target
