r"""A small Euclidean ball around a point of (mathbf Q^2) can contain one lattice point."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_square_lattice_close_vectors_at_radius_squared_one_eighth() -> None:
    lattice = Lattices(ZZ)(ZZ^2)
    first = lattice.basis_vector(0)
    close = lattice.close_vectors((QQ(3) / 4, QQ(1) / 4), QQ(1) / 8)

    assert close.cardinality() == cardinal(1)
    assert close[first] == QQ(1) / 8
