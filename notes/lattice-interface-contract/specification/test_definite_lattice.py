from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from sage.all import ZZ, matrix

from .conftest import Lattice, assert_equal


def test_definite_lattice_constructor_and_signature_contract():
    """
    method: from_gram

    Definite-class contract:
    `Lattice.from_gram(G)` accepts positive-definite Gram data and returns a definite lattice.
    """
    G = matrix(ZZ, ((2, 1), (1, 2)))
    L = Lattice.from_gram(G)
    assert_equal(L.signature(), (2, 0), "Lattice.signature mismatch on positive-definite gram")


def test_definite_lattice_minimum_is_finite_positive():
    """
    method: minimum

    Definite-class contract:
    `minimum()` is finite and positive on nonzero vectors.
    """
    L = Lattice.from_gram(matrix(ZZ, ((2, 0), (0, 2))))
    assert_equal(L.minimum(), 2, "Lattice.minimum mismatch on positive-definite gram")


def test_definite_lattice_shortest_vector_matches_minimum():
    """
    method: shortest_vector

    Definite-class contract:
    `shortest_vector()` returns an element whose norm equals `minimum()`.
    """
    L = Lattice.from_gram(matrix(ZZ, ((2, 0), (0, 2))))
    v = L.shortest_vector()
    assert_equal(
        L.norm(v),
        L.minimum(),
        f"Lattice.shortest_vector norm mismatch on positive-definite gram: v={v}",
    )
