"""Shared fixtures for the Coxeter specification corpus.

The preamble is installed process-wide by ``tests/conftest.py`` one level up;
nothing here repeats that.  What remains is the literature data the corpus
asserts against, which belongs to no single subtree.

Removed with the migration onto the owned surface: the mock-Sage plumbing, the
``src``/``project_root`` path fixtures pointing at directories the retired
clone owned, the ``matrix_factories`` factory whose Gram constructor raised
``NotImplementedError``, the floating ``numerical_tolerance`` (the preamble
computes Gram invariants exactly, over $\\mathbb Z$ and $\\mathbb Q$), the
``exact_fields`` table, and the ``literature_sources`` URL metadata now owned
by ``literature/citations/``.
"""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Directory holding the corpus's CoxIter input files."""
    return Path(__file__).parent / "data"


@pytest.fixture
def expected_finite_orders() -> dict[tuple[str, int], int]:
    """Orders of the finite Coxeter groups, by type.

    Oracle: ``literature/wikipedia/finite_coxeter_group_invariants.md`` in
    this corpus, which tabulates the order of every finite Coxeter group
    alongside its bracket notation, number of reflections, and Coxeter
    number.

    ``('I', m)`` is the dihedral group $I_2(m)$, of order $2m$.  $B_n$ and
    $C_n$ have the same Coxeter graph and therefore the same order.
    """
    return {
        ('A', 1): 2,
        ('A', 2): 6,
        ('A', 3): 24,
        ('A', 4): 120,
        ('B', 2): 8,
        ('B', 3): 48,
        ('B', 4): 384,
        ('C', 2): 8,
        ('C', 3): 48,
        ('C', 4): 384,
        ('D', 4): 192,
        ('D', 5): 1920,
        ('E', 6): 51840,
        ('E', 7): 2903040,
        ('E', 8): 696729600,
        ('F', 4): 1152,
        ('G', 2): 12,
        ('H', 3): 120,
        ('H', 4): 14400,
        ('I', 3): 6,
        ('I', 4): 8,
        ('I', 5): 10,
        ('I', 6): 12,
    }
