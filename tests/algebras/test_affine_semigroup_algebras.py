r"""Affine semigroup presentations are owned by the algebra layer."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebras,
)


def test_affine_semigroup_algebra_retains_its_selected_binomial_presentation() -> None:
    owner = AffineSemigroupAlgebras(ZZ)
    algebra = owner(
        ((1, 0), (0, 1), (1, 1)),
        names=("x", "y", "z"),
    )
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    z = algebra.algebra_generator("z")

    assert algebra in owner
    assert algebra.category().is_subcategory(owner)
    assert z == x * y
    coordinates = algebra.affine_semigroup_generator_coordinates()
    assert tuple(tuple(int(entry) for entry in point) for point in coordinates) == (
        (1, 0),
        (0, 1),
        (1, 1),
    )
    assert "_preamble_affine_semigroup_generator_coordinates" not in algebra.__dict__


