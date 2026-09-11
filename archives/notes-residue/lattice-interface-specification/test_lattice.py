from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from sage.all import ZZ, matrix

from .conftest import Lattice, assert_equal


def test_lattice_from_gram_rank_and_gram_roundtrip():
    """
    method: from_gram

    Base-class contract:
    `Lattice.from_gram(G)` constructs a lattice with rank and Gram matrix determined by `G`.
    """
    G = matrix(ZZ, ((2, 1), (1, 2)))
    L = Lattice.from_gram(G)

    assert_equal(L.rank(), 2, "Lattice.from_gram rank mismatch")
    assert_equal(L.gram(), G, "Lattice.from_gram gram mismatch")


def test_lattice_root_a2_constructor_contract():
    """
    method: A

    RootLattice contract:
    `Lattice.A(2)` produces the finite root lattice A2 with known invariants.
    """
    lattice = Lattice.A(2)
    assert_equal(
        (lattice.rank(), lattice.signature(), lattice.minimum(), lattice.determinant()),
        (2, (2, 0), 2, 3),
        "Lattice.A(2) invariant mismatch",
    )


def test_lattice_root_d4_constructor_contract():
    """
    method: D

    RootLattice contract:
    `Lattice.D(4)` produces D4 with known invariants.
    """
    lattice = Lattice.D(4)
    assert_equal(
        (lattice.rank(), lattice.signature(), lattice.minimum(), lattice.determinant()),
        (4, (4, 0), 2, 4),
        "Lattice.D(4) invariant mismatch",
    )


def test_lattice_root_e8_constructor_contract():
    """
    method: E

    RootLattice contract:
    `Lattice.E(8)` produces E8 as even unimodular positive-definite rank-8 lattice.
    """
    lattice = Lattice.E(8)
    assert_equal(
        (lattice.rank(), lattice.signature(), lattice.minimum(), lattice.determinant()),
        (8, (8, 0), 2, 1),
        "Lattice.E(8) invariant mismatch",
    )
