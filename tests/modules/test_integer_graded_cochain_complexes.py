from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.algebras import (
    DeRhamAlgebra,
    FinitelyPresentedAlgebra,
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.functors.cohomology import cohomology_functor
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    CochainComplex,
    cochain_homset,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _rank_one(label):
    return BasedFreeModule(ZZ, finite_ordered_set((label,)))


def test_shifted_complex_retains_integer_grading_and_boundary_cohomology() -> None:
    degree_minus_one = _rank_one("e")
    degree_zero = _rank_one("f")
    times_three = module_homset(degree_minus_one, degree_zero)(
        {"e": 3 * degree_zero.module_generator("f")}
    )
    complex_ = CochainComplex(
        ZZ,
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
    complex_ = CochainComplex(
        ZZ,
        {-1: degree_minus_one},
        {},
    )
    times_two = cochain_homset(complex_, complex_)(
        {
            -1: module_homset(degree_minus_one, degree_minus_one)(
                {"e": 2 * degree_minus_one.module_generator("e")}
            ),
        }
    )

    h_minus_one_functor = cohomology_functor(ZZ, -1)
    h_minus_one = h_minus_one_functor(complex_)
    generator_class = h_minus_one.class_of_cycle(
        degree_minus_one.module_generator("e")
    )
    assert generator_class != h_minus_one.zero()
    assert h_minus_one_functor(times_two)(generator_class) == 2 * generator_class


def test_nonnegative_dga_has_the_same_zero_incoming_complex_boundary() -> None:
    field = GF(2)
    polynomial = SymmetricAlgebraOn(field, ("x",))
    x = polynomial.algebra_generator("x")
    algebra = FinitelyPresentedAlgebra(polynomial, [x**2])
    dga = DeRhamAlgebra(algebra)

    incoming = dga.differential_component(-1)
    assert incoming.domain().is_zero()
    assert incoming.codomain() is dga.graded_piece(0)
    assert dga.cohomology(-1).is_zero()
    assert dga.cohomology(0).cochain_complex() is dga
