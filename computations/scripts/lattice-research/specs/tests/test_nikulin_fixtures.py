"""
Fixture-driven tests for Nikulin (r, a, delta) invariant computations.

Tests load verified constructions from JSON fixtures and assert that
Sage's discriminant_group() + discriminant-form integrality check
reproduce the recorded (r, a, delta) exactly.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from sage.all import QQ, ZZ, vector
from src.lattices.lattices import Lattice

FIXTURES = Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build(s: str):
    """Build a lattice from a canonical from_string expression."""
    return Lattice.from_string(s)


def _build_from_root_and_glue(root_label: str, rational_glue: list[list[str]]):
    L = Lattice.from_string(root_label)
    if rational_glue:
        glue_vecs = [vector(QQ, [QQ(x) for x in row]) for row in rational_glue]
        L = L.overlattice(glue_vecs)
    return L


def _rad(L):
    dg = L.discriminant_group()
    invs = dg.invariants()
    assert all(i == 2 for i in invs), f"Not 2-elementary: invariants = {invs}"
    a = len(invs)
    delta = 0
    for v in dg:
        if v.q() not in ZZ:
            delta = 1
            break
    return (L.rank(), a, delta)


# ---------------------------------------------------------------------------
# Indefinite 75-lattice fixture
# ---------------------------------------------------------------------------


def _load_nikulin_75():
    with open(FIXTURES / "nikulin_lattices.json") as f:
        return json.load(f)["lattices"]


@pytest.mark.parametrize("entry", _load_nikulin_75(), ids=lambda e: f"({e['r']},{e['a']},{e['delta']})")
def test_nikulin_indefinite_construction(entry):
    L = _build(entry["construction"])
    assert _rad(L) == (entry["r"], entry["a"], entry["delta"])


# ---------------------------------------------------------------------------
# Negative-definite unstarred fixture
# ---------------------------------------------------------------------------


def _load_neg_def_unstarred():
    with open(FIXTURES / "nikulin_neg_def_table2.json") as f:
        return json.load(f)["lattices"]


@pytest.mark.parametrize(
    "entry", _load_neg_def_unstarred(), ids=lambda e: f"({e['r']},{e['a']},{e['delta']})-{e['construction']}"
)
def test_nikulin_neg_def_unstarred(entry):
    L = _build(entry["construction"])
    assert _rad(L) == (entry["r"], entry["a"], entry["delta"])


# ---------------------------------------------------------------------------
# Starred overlattice fixture
# ---------------------------------------------------------------------------


def _load_neg_def_starred():
    with open(FIXTURES / "nikulin_neg_def_starred.json") as f:
        return json.load(f)["lattices"]


@pytest.mark.parametrize("entry", _load_neg_def_starred(), ids=lambda e: f"({e['r']},{e['a']},{e['delta']})-{e['root_lattice']}")
def test_nikulin_neg_def_starred(entry):
    L = _build_from_root_and_glue(
        entry["root_lattice"],
        entry["rational_glue_vectors"] or [],
    )
    assert _rad(L) == (entry["r"], entry["a"], entry["delta"])
