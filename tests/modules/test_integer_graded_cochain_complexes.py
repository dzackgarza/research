from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _rank_one(label):
    return ZZ.free_module(finite_ordered_set((label,)))


def test_shifted_complex_retains_integer_grading_and_boundary_cohomology() -> None:
    degree_minus_one = _rank_one("e")
    degree_zero = _rank_one("f")
    times_three = degree_minus_one.module_category().Mor(degree_minus_one, degree_zero)(
        {"e": 3 * degree_zero.module_generator("f")}
    )
    complex_ = CochainComplexes(ZZ)(
        {-1: degree_minus_one, 0: degree_zero},
        {-1: times_three},
    )

    assert complex_.graded_piece(-1) is degree_minus_one
    assert complex_.differential_component(-2).domain().is_zero()
    assert complex_.differential_component(-2).codomain() is degree_minus_one
    assert complex_.cohomology(-1).is_zero()

    h0 = complex_.cohomology(0)
    invariant_factors = h0.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(3)


def test_negative_degree_cohomology_is_functorial_on_shifted_complexes() -> None:
    degree_minus_one = _rank_one("e")
    complex_ = CochainComplexes(ZZ)(
        {-1: degree_minus_one},
        {},
    )
    times_two = CochainComplexes(ZZ).Mor(complex_, complex_)(
        {
            -1: degree_minus_one.module_category().Mor(degree_minus_one, degree_minus_one)(
                {"e": 2 * degree_minus_one.module_generator("e")}
            ),
        }
    )

    h_minus_one_functor = CochainComplexes(ZZ).cohomology(-1)
    h_minus_one = h_minus_one_functor(complex_)
    generator_class = h_minus_one.class_of_cycle(
        degree_minus_one.module_generator("e")
    )
    assert generator_class != h_minus_one.zero()
    assert h_minus_one_functor(times_two)(generator_class) == 2 * generator_class






