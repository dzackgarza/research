from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


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


def test_nonnegative_dga_has_the_same_zero_incoming_complex_boundary() -> None:
    field = GF(2)
    polynomial = field.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    dga = algebra.de_rham_algebra()

    incoming = dga.differential_component(-1)
    assert incoming.domain().is_zero()
    assert incoming.codomain() is dga.graded_piece(0)
    assert dga.cohomology(-1).is_zero()
    assert dga.cohomology(0).cochain_complex() is dga


def test_lazy_integer_complex_does_not_turn_unrequested_degrees_into_zero() -> None:
    degree_set = ZZ
    calls = []

    def piece(degree):
        degree = int(degree)
        calls.append(degree)
        return _rank_one(f"e{degree}")

    pieces = indexed_family(degree_set, piece, name="A rank-one module in every degree")

    def differential(degree):
        degree = int(degree)
        source = pieces(degree)
        target = pieces(degree + 1)
        return source.module_category().Mor(source, target)(
            {source.module_generating_set()[0]: target.zero()}
        )

    differentials = indexed_family(
        degree_set,
        differential,
        name="Zero differential in every degree",
    )
    complex_ = CochainComplexes(ZZ).from_family(pieces, differentials)

    assert not complex_.has_finite_support()
    assert complex_.degree_convention() == "cohomological"
    assert complex_.graded_piece(-7) is pieces(-7)
    assert -7 in calls
    assert complex_.differential_component(11).domain() is pieces(11)
    assert complex_.differential_component(11).codomain() is pieces(12)


def test_lazy_complex_identity_is_a_degree_indexed_cochain_map() -> None:
    degree_set = ZZ
    pieces = indexed_family(
        degree_set,
        lambda degree: _rank_one(f"e{int(degree)}"),
        name="A rank-one module in every degree",
    )
    def zero_differential(degree):
        source = pieces(degree)
        target = pieces(int(degree) + 1)
        return source.module_category().Mor(source, target)(
            {source.module_generating_set()[0]: target.zero()}
        )

    differentials = indexed_family(
        degree_set,
        zero_differential,
        name="Zero differential in every degree",
    )
    complex_ = CochainComplexes(ZZ).from_family(pieces, differentials)
    identity = CochainComplexes(ZZ).Mor(complex_, complex_).identity()

    source = pieces(-4)
    generator = source.module_generator(source.module_generating_set()[0])
    assert identity.component(-4)(generator) == generator
