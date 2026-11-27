"""
Verify generators of Stab_{O(T_En)}(h) where h = e+f in the U(2) block.

T_En = U (+) U(2) (+) E_8(2),  signature (2,10), rank 12.
h = [0,0,1,1,0,...,0], h^2 = 4.

Uses INDEF_FORM_StabilizerVector from polyhedral_common (Dutour-Sikiric).

Reference: Sterk 1991, vector stabilizer in the transcendental lattice.
"""

from __future__ import annotations

import pytest
from src.backends.external.py_polyhedral.binaries import indefinite_form_stabilizer_vector
from src.lattices.lattices import Lattice


def _gram_as_lists(L):
    n = L.rank()
    M = L.inner_product_matrix()
    return [[int(M[i][j]) for j in range(n)] for i in range(n)]


@pytest.fixture(scope="module")
def t_en():
    U = Lattice.U()
    E8 = Lattice.E(8)
    return U.direct_sum(U.twist(2)).direct_sum(E8.twist(2))


@pytest.fixture(scope="module")
def gram(t_en):
    return _gram_as_lists(t_en)


@pytest.fixture(scope="module")
def h_vector():
    """h = e+f in the U(2) block (positions 2,3 in 0-indexed basis)."""
    return [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]


@pytest.fixture(scope="module")
def stabilizer_gens(gram, h_vector):
    return indefinite_form_stabilizer_vector(gram, h_vector)


class TestSterkVectorStabilizer:
    """Verify Stab_{O(T_En)}(h) for h = e+f in U(2)."""

    def test_lattice_rank(self, t_en):
        assert t_en.rank() == 12

    def test_lattice_signature(self, t_en):
        assert t_en.signature_pair() == (2, 10)

    def test_h_squared_equals_four(self, gram, h_vector):
        h = h_vector
        h2 = sum(gram[i][j] * h[i] * h[j] for i in range(12) for j in range(12))
        assert h2 == 4

    def test_stabilizer_nonempty(self, stabilizer_gens):
        assert len(stabilizer_gens) > 0

    def test_generators_preserve_gram(self, stabilizer_gens, gram):
        n = 12
        for idx, M in enumerate(stabilizer_gens):
            MGMt = [[sum(M[i][k] * gram[k][m] * M[j][m] for k in range(n) for m in range(n)) for j in range(n)] for i in range(n)]
            assert MGMt == gram, f"Generator {idx} does not preserve Gram matrix"

    def test_generators_fix_h(self, stabilizer_gens, gram, h_vector):
        n = 12
        h = h_vector
        for idx, M in enumerate(stabilizer_gens):
            Mh = [sum(M[i][j] * h[j] for j in range(n)) for i in range(n)]
            assert Mh == h, f"Generator {idx} does not fix h: {Mh}"
