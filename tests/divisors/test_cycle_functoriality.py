r"""Proper closed pushforward and flat open pullback of affine cycles."""

from dzack_research.preamble.all import QQ, ZZ, AffineCycleGroup, AffineSpace
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)


def test_closed_immersion_pushes_prime_cycle_to_same_support_with_same_multiplicity() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    axis = plane.closed_subscheme(x)
    axis_ring = axis.coordinate_algebra()
    generic = axis.underlying_space()(axis_ring.ideal(axis_ring.zero()))
    source = AffineCycleGroup(axis, 1)
    cycle = ZZ(3) * source.prime_cycle(generic)

    pushed = axis.proper_pushforward_cycle(cycle)
    ambient_generic = plane.underlying_space()(ring.ideal(x))

    assert pushed.parent().cycle_scheme() is plane
    assert pushed.parent().cycle_dimension() == 1
    assert module_coefficients(pushed, pushed.parent()) == {ambient_generic: ZZ(3)}


def test_distinguished_open_flat_pullback_drops_disjoint_component_and_preserves_the_other() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    cycle_group = AffineCycleGroup(plane, 1)
    x_axis = plane.underlying_space()(ring.ideal(y))
    y_axis = plane.underlying_space()(ring.ideal(x))
    cycle = ZZ(2) * cycle_group.prime_cycle(x_axis) + ZZ(5) * cycle_group.prime_cycle(y_axis)
    away_from_y_axis = plane.distinguished_open(x)

    pulled = away_from_y_axis.flat_pullback_cycle(cycle)
    coefficients = module_coefficients(pulled, pulled.parent())

    assert pulled.parent().cycle_scheme() is away_from_y_axis
    assert pulled.parent().cycle_dimension() == 1
    assert len(coefficients) == 1
    assert next(iter(coefficients.values())) == ZZ(2)
