r"""Affine semigroup presentations are owned by the algebra layer."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebra,
    AffineSemigroupAlgebras,
)


def test_affine_semigroup_algebra_retains_its_selected_binomial_presentation() -> None:
    algebra = AffineSemigroupAlgebra(
        ((1, 0), (0, 1), (1, 1)),
        ZZ,
        names=("x", "y", "z"),
    )
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    z = algebra.algebra_generator("z")

    assert algebra in AffineSemigroupAlgebras(ZZ)
    assert z == x * y
    assert algebra._preamble_affine_semigroup_generator_coordinates == (
        (1, 0),
        (0, 1),
        (1, 1),
    )


def test_affine_semigroup_membership_requires_the_selected_lattice_presentation() -> None:
    presentation = PolynomialRing(ZZ, ("x", "y", "z"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    z = presentation.algebra_generator("z")
    ordinary = FinitelyPresentedAlgebra(presentation, (z - x * y,))

    assert ordinary not in AffineSemigroupAlgebras(ZZ)
