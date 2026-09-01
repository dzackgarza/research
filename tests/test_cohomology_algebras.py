from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.algebras import (
    CohomologyAlgebra,
    CohomologyAlgebras,
    DeRhamAlgebra,
    FinitelyPresentedAlgebra,
    StrictlyGradedCommutativeAlgebras,
    SymmetricAlgebraOn,
)


def test_dga_cohomology_is_a_graded_algebra_with_descended_product() -> None:
    field = GF(2)
    polynomial = SymmetricAlgebraOn(field, ("x",))
    x = polynomial.algebra_generator("x")
    algebra = FinitelyPresentedAlgebra(polynomial, [x**2])
    xbar = algebra.algebra_generator("x")
    dga = DeRhamAlgebra(algebra)

    cohomology = CohomologyAlgebra(dga)
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

    assert alpha != cohomology.zero()
    assert cohomology.one() * alpha == alpha
    assert alpha * cohomology.one() == alpha
    assert alpha * alpha == cohomology.zero()
