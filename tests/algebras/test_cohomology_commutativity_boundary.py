r"""Cohomology algebra retains only commutativity justified by its source DGA."""
from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.cohomology_algebras import (
    CohomologyAlgebras,
)
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    CommutativeDifferentialGradedAlgebras,
    Differential,
    DifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
    GradedCommutativeAlgebras,
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.refine import refine


def _noncommutative_zero_differential_dga():
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    algebra = module.tensor_algebra()
    algebra._preamble_differential = Differential(
        algebra,
        lambda _element: algebra.zero(),
    )
    return refine(algebra, DifferentialGradedAlgebras(ZZ))


def test_general_cohomology_algebra_category_is_not_declared_commutative() -> None:
    category = CohomologyAlgebras(ZZ)

    assert category.is_subcategory(GradedAlgebras(ZZ))
    assert not category.is_subcategory(GradedCommutativeAlgebras(ZZ))
    assert not category.is_subcategory(StrictlyGradedCommutativeAlgebras(ZZ))


def test_noncommutative_zero_differential_dga_keeps_noncommutative_cohomology() -> None:
    dga = _noncommutative_zero_differential_dga()
    cohomology = dga.cohomology_algebra()

    assert cohomology in CohomologyAlgebras(ZZ)
    assert cohomology in GradedAlgebras(ZZ)
    assert cohomology not in GradedCommutativeAlgebras(ZZ)
    assert cohomology not in StrictlyGradedCommutativeAlgebras(ZZ)

    x = dga.algebra_generator("x")
    y = dga.algebra_generator("y")
    x_class = cohomology.from_component(
        1,
        cohomology.graded_piece(1).class_of_cycle(x.homogeneous_component(1)),
    )
    y_class = cohomology.from_component(
        1,
        cohomology.graded_piece(1).class_of_cycle(y.homogeneous_component(1)),
    )
    assert x_class * y_class != y_class * x_class


def test_degree_zero_cohomology_of_nonnegative_unital_dga_retains_the_unit() -> None:
    dga = _noncommutative_zero_differential_dga()
    cohomology = dga.cohomology_algebra()
    degree_zero = cohomology.graded_piece(0)
    unit_cycle = dga.one().homogeneous_component(0)
    unit_class = degree_zero.class_of_cycle(unit_cycle)

    assert dga.differential_component(-1).domain().module_rank() == 0
    assert degree_zero is dga.cohomology(0)
    assert cohomology.from_component(0, unit_class) == cohomology.one()


def test_characteristic_two_does_not_turn_graded_commutativity_into_odd_square_zero() -> None:
    field = GF(2)
    dga = field.free_module(("x",)).symmetric_algebra()
    dga._preamble_differential = Differential(dga, lambda _element: dga.zero())
    refine(dga, CommutativeDifferentialGradedAlgebras(field))
    x = dga.algebra_generator("x")

    assert x.degree() == 1
    assert x * x != dga.zero()
    assert dga in CommutativeDifferentialGradedAlgebras(field)
    assert dga not in StrictlyGradedCommutativeAlgebras(field)

    cohomology = dga.cohomology_algebra()
    x_class = cohomology.from_component(
        1,
        cohomology.graded_piece(1).class_of_cycle(x.homogeneous_component(1)),
    )
    assert cohomology in GradedCommutativeAlgebras(field)
    assert cohomology not in StrictlyGradedCommutativeAlgebras(field)
    assert x_class * x_class != cohomology.zero()


def test_nonidentity_dga_map_induces_the_expected_noncommutative_cohomology_map() -> None:
    dga = _noncommutative_zero_differential_dga()
    x = dga.algebra_generator("x")
    y = dga.algebra_generator("y")
    swap_algebra = Algebras(dga.base_ring()).Associative().Unital().Mor(dga, dga)({"x": y, "y": x})
    swap = DifferentialGradedAlgebras(dga.base_ring()).Mor(dga, dga)(swap_algebra)

    cohomology = dga.cohomology_algebra()
    functor = DifferentialGradedAlgebras(ZZ).cohomology_algebra()
    assert functor.domain() is DifferentialGradedAlgebras(ZZ)
    assert functor(dga) is cohomology
    induced = functor(swap)
    direct = CohomologyAlgebras(ZZ).Mor(cohomology, cohomology)(swap)
    x_class = cohomology.from_component(
        1,
        cohomology.graded_piece(1).class_of_cycle(x.homogeneous_component(1)),
    )
    y_class = cohomology.from_component(
        1,
        cohomology.graded_piece(1).class_of_cycle(y.homogeneous_component(1)),
    )

    assert induced(x_class) == y_class
    assert induced(y_class) == x_class
    assert induced(x_class) == direct(x_class)
    assert induced(x_class * y_class) == y_class * x_class
    assert (induced * induced)(x_class) == x_class
    assert (induced * induced)(y_class) == y_class


def test_graded_derivation_checks_degree_through_the_graded_algebra_owner() -> None:
    from dzack_research.preamble.categories.algebras.derivations import (
        GradedDerivation,
    )

    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    algebra = module.tensor_algebra()

    def euler(element):
        element = algebra(element)
        if element == algebra.zero():
            return algebra.zero()
        return algebra(ZZ(algebra.homogeneous_degree(element))) * element

    derivation = GradedDerivation(algebra.graded_derivations(algebra, shift=0), euler)
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    underlying = derivation.underlying_linear_morphism()

    assert underlying.derivation() is derivation
    assert underlying.degree_shift() == 0
    assert derivation.parent()(underlying) is derivation
    assert algebra.homogeneous_degree(derivation(x)) == 1
    assert derivation(x * y) == algebra(ZZ(2)) * x * y
