r"""L: multigenerator adic completions of represented singular local quotients."""

from dzack_research.preamble.all import (
    CompleteLocalRings,
    FinitelyPresentedAlgebra,
    PolynomialRing,
    QQ,
)


def test_cusp_maximal_adic_completion_retains_source_map_and_two_generators() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    cusp = FinitelyPresentedAlgebra(plane, (y**2 - x**3,))
    xbar = cusp.algebra_generator("x")
    ybar = cusp.algebra_generator("y")
    maximal = cusp.ideal(xbar, ybar)
    completion = cusp.adic_completion(maximal, precision=6)

    assert completion in CompleteLocalRings()
    assert completion.completion_source() is cusp
    assert completion.ideal_of_definition() == maximal
    assert completion.computation_precision() == 6
    assert completion.completion_map().domain() is cusp
    assert completion.completion_map().codomain() is completion
    assert len(completion.maximal_ideal().ideal_generators()) == 2
    assert completion.residue_field().characteristic() == 0


def test_multivariable_origin_completion_uses_the_requested_artin_precision() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    completion = plane.adic_completion(plane.ideal(x, y), precision=4)

    xhat = completion.completion_map()(x)
    yhat = completion.completion_map()(y)
    assert xhat**4 == completion.zero()
    assert yhat**4 == completion.zero()
    assert xhat**3 != completion.zero()
