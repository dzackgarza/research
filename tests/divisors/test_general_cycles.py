r"""General algebraic cycles retain generic-point multiplicities."""

from dzack_research.preamble.all import QQ, ZZ, AffineSpaces
from dzack_research.preamble.categories.divisors.chow_groups import AlgebraicCycleGroups


def test_nonreduced_double_line_has_multiplicity_two_in_its_fundamental_cycle() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    double_line = plane.closed_subscheme(x**2)
    support = plane.underlying_space()(ring.ideal(x))

    cycle = double_line.fundamental_cycle()
    coefficients = cycle.parent().framing_coefficients(cycle)

    assert cycle.parent() in AlgebraicCycleGroups(ZZ)
    assert cycle.parent().cycle_scheme() is plane
    assert cycle.parent().cycle_degree_construction().scheme() is plane
    assert cycle.parent().cycle_dimension() == 1
    assert "_preamble_cycle_scheme" not in cycle.parent().__dict__
    assert "_preamble_cycle_dimension" not in cycle.parent().__dict__
    assert "_preamble_cycle_prime_locus" not in cycle.parent().__dict__
    assert coefficients == {support: ZZ(2)}
    assert support.generic_local_length(double_line.defining_ideal_owned()) == 2


def test_embedded_lower_dimensional_associated_prime_is_not_a_generic_component() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    # (x^2, x*y) has the line (x) plus an embedded point at the origin.
    thickened = plane.closed_subscheme((x**2, x * y))
    line = plane.underlying_space()(ring.ideal(x))
    origin = plane.underlying_space()(ring.ideal(x, y))

    cycle = thickened.fundamental_cycle()
    coefficients = cycle.parent().framing_coefficients(cycle)

    assert line in coefficients
    assert origin not in coefficients
