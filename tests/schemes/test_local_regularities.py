r"""Affine schemes delegate regularity to their represented local rings."""

from dzack_research.preamble.all import AffineSpace, QQ


def test_affine_plane_and_cusp_use_the_same_pointwise_regularity_owner() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    ring = plane.coordinate_algebra()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    origin = plane.underlying_space()(ring.ideal(x, y))

    assert plane.is_regular_at(origin)
    assert not plane.is_singular_at(origin)
    assert plane.is_locally_factorial_at(origin)

    cusp = plane.closed_subscheme(y**2 - x**3)
    cusp_ring = cusp.coordinate_algebra()
    cx = cusp_ring.algebra_generator("x")
    cy = cusp_ring.algebra_generator("y")
    cusp_origin = cusp.underlying_space()(cusp_ring.ideal(cx, cy))

    assert cusp.is_singular_at(cusp_origin)
    assert not cusp.is_regular_at(cusp_origin)
