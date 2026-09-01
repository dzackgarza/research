from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.algebras import (
    DeRhamAlgebra,
    FinitelyPresentedAlgebra,
    SymmetricAlgebraOn,
    algebra_homset,
)
from dzack_research.preamble.categories.functors import (
    de_rham_cohomology_algebra_functor,
    cohomology_functor,
    de_rham_cohomology_functor,
)
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    CochainComplex,
    cochain_homset,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.static_types import cup, de_rham_class_view


def test_cohomology_is_functorial_on_cochain_maps() -> None:
    degree_zero = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    degree_one = BasedFreeModule(ZZ, finite_ordered_set(("f",)))
    differential = module_homset(degree_zero, degree_one)(
        {"e": 2 * degree_one.module_generator("f")}
    )
    complex_ = CochainComplex(
        ZZ,
        {0: degree_zero, 1: degree_one},
        {0: differential},
    )
    times_three = cochain_homset(complex_, complex_)(
        {
            0: module_homset(degree_zero, degree_zero)(
                {"e": 3 * degree_zero.module_generator("e")}
            ),
            1: module_homset(degree_one, degree_one)(
                {"f": 3 * degree_one.module_generator("f")}
            ),
        }
    )

    functor = cohomology_functor(ZZ, 1)
    h1 = functor(complex_)
    nonzero = h1.class_of_cycle(degree_one.module_generator("f"))
    induced = functor(times_three)

    assert nonzero != h1.zero()
    assert induced(nonzero) == nonzero


def test_algebraic_de_rham_cohomology_is_literal_functor_composition() -> None:
    field = GF(2)
    polynomial = SymmetricAlgebraOn(field, ("x",))
    x = polynomial.algebra_generator("x")
    algebra = FinitelyPresentedAlgebra(polynomial, [x**2])
    xbar = algebra.algebra_generator("x")
    collapse = algebra_homset(algebra, algebra)({"x": algebra.zero()})

    functor = de_rham_cohomology_functor(field, 1)
    h1 = functor(algebra)
    de_rham = DeRhamAlgebra(algebra)
    assert h1 is de_rham.cohomology(1)

    omega = de_rham.kahler_differentials()
    cycle = de_rham.graded_piece(1)(
        omega.scalar_multiple(xbar, omega.differential_generator("x"))
    )
    alpha = h1.class_of_cycle(cycle)
    assert alpha != h1.zero()
    assert functor(collapse)(alpha) == h1.zero()


def test_algebraic_de_rham_cohomology_ring_is_functorial() -> None:
    field = GF(2)
    polynomial = SymmetricAlgebraOn(field, ("x",))
    x = polynomial.algebra_generator("x")
    algebra = FinitelyPresentedAlgebra(polynomial, [x**2])
    xbar = algebra.algebra_generator("x")
    collapse = algebra_homset(algebra, algebra)({"x": algebra.zero()})

    functor = de_rham_cohomology_algebra_functor(field)
    cohomology = functor(algebra)
    de_rham = DeRhamAlgebra(algebra)
    assert cohomology.source_dga() is de_rham

    omega = de_rham.kahler_differentials()
    cycle = de_rham.graded_piece(1)(
        omega.scalar_multiple(xbar, omega.differential_generator("x"))
    )
    alpha_class = cohomology.graded_piece(1).class_of_cycle(cycle)
    alpha = cohomology.from_component(1, alpha_class)
    induced = functor(collapse)

    assert induced(cohomology.one()) == cohomology.one()
    assert induced(alpha) == cohomology.zero()
    assert induced(cohomology.one() * alpha) == (
        induced(cohomology.one()) * induced(alpha)
    )
    unit_view = de_rham_class_view(cohomology.one())
    alpha_view = de_rham_class_view(alpha)
    assert cup(unit_view, alpha_view) == cohomology.one() * alpha
