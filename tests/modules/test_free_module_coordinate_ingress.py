r"""Coordinate ingress for framed free modules over owned scalar rings."""

from dzack_research.preamble.all import Zp, finite_ordered_set


def test_coordinate_sequences_take_precedence_over_scalar_ingress() -> None:
    ring = Zp(5)
    labels = finite_ordered_set(("x", "y"))
    module = ring.free_module(labels)
    two = ring(2)
    three = ring(3)
    element = module((two, three))

    assert module(0) == module.zero()
    coefficients = element.monomial_coefficients()
    assert coefficients["x"] is two
    assert coefficients["y"] is three
