from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.static_types import cup, de_rham_class_view


def test_cohomology_is_functorial_on_cochain_maps() -> None:
    degree_zero = ZZ.free_module(finite_ordered_set(("e",)))
    degree_one = ZZ.free_module(finite_ordered_set(("f",)))
    differential = degree_zero.module_category().Mor(degree_zero, degree_one)(
        {"e": 2 * degree_one.module_generator("f")}
    )
    complex_ = CochainComplexes(ZZ)(
        {0: degree_zero, 1: degree_one},
        {0: differential},
    )
    times_three = CochainComplexes(ZZ).Mor(complex_, complex_)(
        {
            0: degree_zero.module_category().Mor(degree_zero, degree_zero)(
                {"e": 3 * degree_zero.module_generator("e")}
            ),
            1: degree_one.module_category().Mor(degree_one, degree_one)(
                {"f": 3 * degree_one.module_generator("f")}
            ),
        }
    )

    functor = CochainComplexes(ZZ).cohomology(1)
    h1 = functor(complex_)
    nonzero = h1.class_of_cycle(degree_one.module_generator("f"))
    induced = functor(times_three)

    assert nonzero != h1.zero()
    assert induced(nonzero) == nonzero


def test_algebraic_de_rham_cohomology_is_literal_functor_composition() -> None:
    field = GF(2)
    polynomial = field.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    xbar = algebra.algebra_generator("x")
    collapse = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra)({"x": algebra.zero()})

    functor = Algebras(field).Associative().Unital().Commutative().de_rham_cohomology(1)
    h1 = functor(algebra)
    de_rham = algebra.de_rham_algebra()
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
    polynomial = field.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    xbar = algebra.algebra_generator("x")
    collapse = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra)({"x": algebra.zero()})

    functor = Algebras(field).Associative().Unital().Commutative().de_rham_cohomology_algebra()
    cohomology = functor(algebra)
    de_rham = algebra.de_rham_algebra()
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
