r"""Equalizers, coequalizers, pullbacks and empty (co)products, computed."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_equalizer_of_the_two_coordinate_projections_is_the_diagonal() -> None:
    r"""``eq(pr_x, pr_y : Z^2 -> Z) = Z(x + y)``; ``t |-> x + y`` factors through it."""
    plane = Modules(ZZ)(ZZ**2)
    line = Modules(ZZ)(ZZ**1)
    probe = Modules(ZZ)(ZZ**1)
    x, y = plane.basis()
    (z,) = line.basis()
    (t,) = probe.basis()
    first = plane.Mor(line)({x: z, y: line.zero()})
    second = plane.Mor(line)({x: line.zero(), y: z})

    equalizer = Modules(ZZ).equalizer(first, second)
    inclusion = equalizer.inclusion()
    (generator,) = equalizer.basis()
    diagonal = probe.Mor(plane)({t: x + y})
    factor = equalizer.lift(diagonal)

    assert equalizer.module_rank() == 1
    assert inclusion(generator) in (x + y, -x - y)
    assert first * inclusion == second * inclusion
    assert inclusion * factor == diagonal


def test_coequalizer_of_the_two_basis_inclusions_is_Z_through_which_summation_factors() -> None:
    r"""``coeq(t |-> x, t |-> y) = Z^2 / Z(x - y) = Z``; the sum map ``Z^2 -> Z`` descends."""
    source = Modules(ZZ)(ZZ**1)
    plane = Modules(ZZ)(ZZ**2)
    target = Modules(ZZ)(ZZ**1)
    (t,) = source.basis()
    x, y = plane.basis()
    (z,) = target.basis()
    first = source.Mor(plane)({t: x})
    second = source.Mor(plane)({t: y})
    summation = plane.Mor(target)({x: z, y: z})

    coequalizer = Modules(ZZ).coequalizer(first, second)
    projection = coequalizer.projection()
    factor = coequalizer.desc(summation)

    assert coequalizer.is_free()
    assert coequalizer.module_rank() == 1
    assert projection(x) == projection(y)
    assert projection(x - y) == coequalizer.zero()
    assert factor * projection == summation
    assert factor.is_isomorphism()


def test_zero_and_times_two_on_Z_have_zero_equalizer_and_coequalizer_Z_mod_2() -> None:
    r"""On ``Z``: ``eq(0, 2) = ker 2 = 0`` and ``coeq(0, 2) = coker 2 = Z/2``."""
    line = Modules(ZZ)(ZZ**1)
    (e,) = line.basis()
    zero = line.Mor(line)({e: line.zero()})
    twice = line.Mor(line)({e: 2 * e})

    assert Modules(ZZ).equalizer(zero, twice).cardinality() == 1
    assert Modules(ZZ).coequalizer(zero, twice).cardinality() == 2


def test_twice_and_zero_on_Z_mod_4_have_the_order_two_equalizer_submodule() -> None:
    r"""On ``Z/4``: ``eq(2, 0) = ker 2 = 2Z/4``, the submodule of order 2."""
    line = Modules(ZZ)(ZZ**1)
    (e,) = line.basis()
    cyclic_four = line / line.span((4 * e,))
    a = cyclic_four.projection()(e)
    twice = cyclic_four.Mor(cyclic_four)({a: 2 * a})
    zero = cyclic_four.Mor(cyclic_four)({a: cyclic_four.zero()})

    equalizer = Modules(ZZ).equalizer(twice, zero)
    inclusion = equalizer.inclusion()

    assert equalizer.cardinality() == 2
    assert 2 * a in inclusion.image()
    assert a not in inclusion.image()
    assert twice * inclusion == zero * inclusion


def test_empty_product_is_a_point_and_empty_coproduct_is_empty() -> None:
    r"""The terminal set is the empty product; the initial set is the empty coproduct."""
    product = Sets().product(())
    coproduct = Sets().coproduct(())
    probe = Sets()(("a", "b"))

    assert product.cardinality() == 1
    assert coproduct.cardinality() == 0
    assert probe.Mor(product).cardinality() == 1
    assert coproduct.Mor(probe).cardinality() == 1
    assert probe.Mor(coproduct).cardinality() == 0


def test_pullback_of_two_and_three_on_Z_is_Z_spanned_by_three_two() -> None:
    r"""``Z x_{2, Z, 3} Z = {(a, b) : 2a = 3b} = Z(3, 2)``; the cone ``(3, 2)`` factors."""
    line = Modules(ZZ)(ZZ**1)
    probe = Modules(ZZ)(ZZ**1)
    (e,) = line.basis()
    (t,) = probe.basis()
    twice = line.Mor(line)({e: 2 * e})
    thrice = line.Mor(line)({e: 3 * e})

    pullback = Modules(ZZ).pullback(twice, thrice)
    left, right = pullback.left_projection(), pullback.right_projection()
    (generator,) = pullback.basis()
    to_left = probe.Mor(line)({t: 3 * e})
    to_right = probe.Mor(line)({t: 2 * e})
    factor = pullback.lift(to_left, to_right)

    assert pullback.module_rank() == 1
    assert (left(generator), right(generator)) in ((3 * e, 2 * e), (-3 * e, -2 * e))
    assert twice * left == thrice * right
    assert left * factor == to_left
    assert right * factor == to_right
