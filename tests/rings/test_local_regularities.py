r"""Local dimension and embedding dimension determine regularity."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import QQ


def test_affine_plane_origin_has_dimension_and_embedding_dimension_two() -> None:
    ring = QQ.polynomial_ring("x", "y")
    x, y = (ring.algebra_generator(name) for name in ("x", "y"))
    origin = ring.spectrum()(ring.ideal(x, y))

    assert origin.height() == 2
    assert origin.embedding_dimension() == 2
    assert origin.is_regular()
    assert origin.is_locally_factorial()


def test_cusp_origin_has_embedding_dimension_two_but_local_dimension_one() -> None:
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = (polynomial.algebra_generator(name) for name in ("x", "y"))
    cusp = polynomial.quotient_ring(polynomial.ideal(y**2 - x**3))
    cx, cy = (cusp(cusp.quotient_source().algebra_generator(name)) for name in ("x", "y"))
    origin = cusp.spectrum()(cusp.ideal(cx, cy))

    assert origin.height() == 1
    assert origin.embedding_dimension() == 2
    assert not origin.is_regular()
    assert origin.is_locally_factorial() is Unknown
