from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.algebras import (
    CohomologyAlgebras,
    StrictlyGradedCommutativeAlgebras,
)


def test_dga_cohomology_is_a_graded_algebra_with_descended_product() -> None:
    field = GF(2)
    polynomial = field.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    xbar = algebra.algebra_generator("x")
    dga = algebra.de_rham_algebra()

    cohomology = dga.cohomology_algebra()
    assert cohomology in CohomologyAlgebras(dga.base_ring())
    assert cohomology in StrictlyGradedCommutativeAlgebras(dga.base_ring())
    assert cohomology.source_dga() is dga
    assert cohomology.graded_piece(1) is dga.cohomology(1)

    omega = dga.kahler_differentials()
    cycle = dga.graded_piece(1)(
        omega.scalar_multiple(xbar, omega.differential_generator("x"))
    )
    alpha_class = cohomology.graded_piece(1).class_of_cycle(cycle)
    alpha = cohomology.from_component(1, alpha_class)

    boundary = dga.d(dga.from_component(0, xbar)).homogeneous_component(1)
    assert boundary != dga.graded_piece(1).zero()
    assert cohomology.graded_piece(1).class_of_cycle(boundary) == cohomology.graded_piece(1).zero()
    changed_cycle = cycle + boundary
    changed_class = cohomology.graded_piece(1).class_of_cycle(changed_cycle)
    changed_alpha = cohomology.from_component(1, changed_class)

    assert alpha != cohomology.zero()
    assert changed_class == alpha_class
    assert changed_alpha == alpha
    assert cohomology.one() * alpha == alpha
    assert alpha * cohomology.one() == alpha
    assert cohomology.one() * changed_alpha == cohomology.one() * alpha
    assert alpha * alpha == cohomology.zero()

    # The product descends from the already constructed direct sum of the
    # cycle quotients; those pieces and their exact quotient maps are kept.
    module = cohomology.unformed_module()
    assert module is not cohomology
    assert module.base_ring() is field
    assert module.graded_piece(1) is dga.cohomology(1)
    assert module(alpha).homogeneous_component(1) == alpha_class
    assert cohomology(module(alpha)) == alpha
    multiplication = cohomology.multiplication()
    assert multiplication.codomain() is module
    assert multiplication.domain().tensor_factor(0) is module
    assert multiplication.domain().tensor_factor(1) is module
    assert multiplication(module(cohomology.one()), module(alpha)) == module(alpha)
    assert module.projection(1)(module(alpha)) == alpha_class
    assert module.injection(1)(alpha_class) == module(alpha)
