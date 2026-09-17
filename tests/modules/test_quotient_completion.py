r"""Noetherian quotient/completion comparison through the canonical maps."""

from dzack_research.preamble.all import (
    QQ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _nodal_plane_comparison(precision=6):
    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    node = plane.quotient_ring(plane.ideal(x * y))
    comparison = node.completion_comparison(
        plane.ideal(x, y),
        precision=precision,
    )
    return plane, x, y, node, comparison


def test_complete_nodal_quotient_agrees_with_quotient_of_completion() -> None:
    plane, x, y, node, comparison = _nodal_plane_comparison()
    direct = comparison.completed_quotient()
    quotient_after = comparison.quotient_after_completion()
    source_completion = comparison.source_completion()
    node_map = node.quotient_map()
    direct_map = direct.completion_map()
    quotient_map = quotient_after.quotient_map()
    source_map = source_completion.completion_map()

    for generator in (x, y):
        left = comparison.forward()(direct_map(node_map(generator)))
        right = quotient_map(source_map(generator))
        assert left == right
        assert comparison.inverse()(right) == direct_map(node_map(generator))

    assert direct_map(node_map(x * y)) == direct.zero()
    assert quotient_map(source_map(x * y)) == quotient_after.zero()


def test_quotient_completion_comparison_retains_both_source_maps() -> None:
    plane, x, y, node, comparison = _nodal_plane_comparison()
    direct = comparison.completed_quotient()
    quotient_after = comparison.quotient_after_completion()
    source_completion = comparison.source_completion()

    assert comparison.source_quotient() is node
    assert comparison.source_ideal() == plane.ideal(x, y)
    assert comparison.extended_defining_ideal().ring() is source_completion
    assert comparison.forward().domain() is direct
    assert comparison.forward().codomain() is quotient_after
    assert comparison.inverse().domain() is quotient_after
    assert comparison.inverse().codomain() is direct


def test_finite_stages_match_through_the_explicit_comparison() -> None:
    _plane, x, y, node, comparison = _nodal_plane_comparison(precision=7)
    direct = comparison.completed_quotient()
    direct_map = direct.completion_map()
    node_map = node.quotient_map()

    x_hat = direct_map(node_map(x))
    y_hat = direct_map(node_map(y))
    round_trip_x = comparison.inverse()(comparison.forward()(x_hat))
    round_trip_y = comparison.inverse()(comparison.forward()(y_hat))
    for exponent in (1, 2, 3, 5):
        projection = direct.adic_projection(exponent)
        assert projection(round_trip_x) == projection(x_hat)
        assert projection(round_trip_y) == projection(y_hat)


def test_module_cokernel_completion_is_an_explicit_isomorphism() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = ring.free_module(finite_ordered_set(("g",)))
    multiplication = free.module_category().Mor(free, free)(
        {"g": free.scalar_multiple(x, free.module_generator("g"))}
    )
    comparison = multiplication.completion_cokernel_comparison(
        ring.ideal(x),
        precision=6,
    )
    left = comparison.domain()
    right = comparison.codomain()

    assert comparison.forward().domain() is left
    assert comparison.forward().codomain() is right
    assert comparison.inverse().domain() is right
    assert comparison.inverse().codomain() is left
    left_generator = left.module_generator(left.module_generating_set()[0])
    right_generator = comparison.forward()(left_generator)
    assert comparison.inverse()(right_generator) == left_generator
