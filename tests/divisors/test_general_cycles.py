r"""General algebraic cycles retain generic-point multiplicities."""

from dzack_research.preamble.all import QQ, ZZ, AffineSpace
from dzack_research.preamble.categories.divisors.chow_groups import AlgebraicCycleGroups
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)


def test_nonreduced_double_line_has_multiplicity_two_in_its_fundamental_cycle() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    double_line = plane.closed_subscheme(x**2)
    support = plane.underlying_space()(ring.ideal(x))

    cycle = double_line.fundamental_cycle()
    coefficients = module_coefficients(cycle, cycle.parent())

    assert cycle.parent() in AlgebraicCycleGroups(ZZ)
    assert cycle.parent().cycle_scheme() is plane
    assert cycle.parent().cycle_dimension() == 1
    assert coefficients == {support: ZZ(2)}
    assert support.generic_local_length(double_line.defining_ideal_owned()) == 2


def test_embedded_lower_dimensional_associated_prime_is_not_a_generic_component() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    # (x^2, x*y) has the line (x) plus an embedded point at the origin.
    thickened = plane.closed_subscheme((x**2, x * y))
    line = plane.underlying_space()(ring.ideal(x))
    origin = plane.underlying_space()(ring.ideal(x, y))

    cycle = thickened.fundamental_cycle()
    coefficients = module_coefficients(cycle, cycle.parent())

    assert line in coefficients
    assert origin not in coefficients
