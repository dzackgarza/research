from __future__ import annotations






def test_distinguished_affine_cover_rejects_a_noncover_and_noncontainment() -> None:
    from dzack_research.preamble.all import QQ

    algebra = QQ.polynomial_ring(("x", "y"))
    x, y = algebra.algebra_generators()
    scheme = (algebra).affine_spectrum()

    try:
        scheme.distinguished_open_cover(x, y)
    except ValueError as error:
        assert "do not cover" in str(error)
    else:
        raise AssertionError("D(x) and D(y) do not cover the affine plane")

    x_open = scheme.distinguished_open(x)
    y_open = scheme.distinguished_open(y)
    try:
        scheme.structure_sheaf().restriction_map(x_open, y_open)
    except ValueError as error:
        assert "not contained" in str(error)
    else:
        raise AssertionError("D(y) is not contained in D(x)")
