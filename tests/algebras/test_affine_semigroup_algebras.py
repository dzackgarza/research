r"""Affine semigroup presentations are owned by the algebra layer."""

from dzack_research.preamble.all import ZZ
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
