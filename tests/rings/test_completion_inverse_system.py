r"""Completion is the represented inverse limit, not a selected finite stage."""

from dzack_research.preamble.all import QQ, AdicallyCompleteRings, PowerSeriesRing


def test_power_series_constructor_retains_the_same_adic_completion_data() -> None:
    series = PowerSeriesRing(QQ, "t")
    assert series in AdicallyCompleteRings()
    source = series.completion_source()
    t = source.algebra_generator("t")
    assert series.ideal_of_definition().ring() is source
    assert series.completion_map().domain() is source
    assert series.completion_map().codomain() is series
    assert series.adic_projection(3)(series.completion_map()(t**3)) == series.adic_truncation(3).zero()
    assert series.adic_projection(4)(series.completion_map()(t**3)) != series.adic_truncation(4).zero()


def test_adic_transition_maps_compose_on_the_same_inverse_system() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    completion = plane.adic_completion(plane.ideal(x, y))
    fifth = completion.adic_truncation(5)
    fourth = completion.adic_truncation(4)
    completion.adic_truncation(2)
    five_to_four = completion.adic_transition_map(5, 4)
    four_to_two = completion.adic_transition_map(4, 2)
    five_to_two = completion.adic_transition_map(5, 2)
    value = fifth.quotient_map()(x**3 + y)

    assert five_to_four.domain() is fifth
    assert five_to_four.codomain() is fourth
    assert four_to_two(five_to_four(value)) == five_to_two(value)
