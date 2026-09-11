from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, assert_equal
L = Lattice.U()


def test_indefinite_lattice_signature_and_predicate_contract():
    """
    method: is_indefinite

    Indefinite-class contract:
    lattice reports indefinite signature and `is_indefinite()` is true.
    """
    assert_equal(L.signature(), (1, 1), "IndefiniteLattice.signature mismatch")
    assert_equal(L.is_indefinite(), True, "IndefiniteLattice.is_indefinite mismatch")


def test_indefinite_lattice_witt_index_contract():
    """
    method: witt_index

    Indefinite-class contract:
    hyperbolic plane has Witt index 1.
    """
    assert_equal(L.witt_index(), 1, "IndefiniteLattice.witt_index mismatch")
