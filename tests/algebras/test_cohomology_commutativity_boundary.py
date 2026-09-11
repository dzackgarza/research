r"""Cohomology algebra retains only commutativity justified by its source DGA."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.cohomology_algebras import (
    CohomologyAlgebra,
    CohomologyAlgebras,
    cohomology_algebra_homset,
)
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    Differential,
    DifferentialGradedAlgebras,
    dga_homset,
)
from dzack_research.preamble.categories.algebras.algebras import algebra_homset
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
    GradedCommutativeAlgebras,
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOf
from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.refine import refine


def _noncommutative_zero_differential_dga():
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    algebra = TensorAlgebraOf(module)
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
    cohomology = CohomologyAlgebra(dga)

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


def test_nonidentity_dga_map_induces_the_expected_noncommutative_cohomology_map() -> None:
    dga = _noncommutative_zero_differential_dga()
    x = dga.algebra_generator("x")
    y = dga.algebra_generator("y")
    swap_algebra = algebra_homset(dga, dga)({"x": y, "y": x})
    swap = dga_homset(dga, dga)(swap_algebra)

    cohomology = CohomologyAlgebra(dga)
    induced = cohomology_algebra_homset(cohomology, cohomology)(swap)
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
    assert induced(x_class * y_class) == y_class * x_class
    assert (induced * induced)(x_class) == x_class
    assert (induced * induced)(y_class) == y_class
