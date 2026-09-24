r"""Isometry of lattices presented in different bases."""

from dzack_research.preamble.all import *


def test_a_change_of_basis_of_the_odd_unimodular_plane_is_isometric_to_it() -> None:
    r"""In \(\langle 1\rangle\oplus\langle -1\rangle\) the basis \((e, 2e + f)\) has Gram
    \(\begin{pmatrix}1&2\\2&3\end{pmatrix}\); an isometry to it preserves norms."""
    source = Lattices(ZZ)([[1, 0], [0, -1]])
    target = Lattices(ZZ)([[1, 2], [2, 3]])

    assert source.is_isometric_to(target)
    isometry = source.isometry_to(target)
    first, second = source.module_generators()
    for vector in (first, second, first + second):
        assert isometry(vector).q() == vector.q()
    assert isometry(first).b(isometry(second)) == 0
