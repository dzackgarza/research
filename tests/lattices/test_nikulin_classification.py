r"""Every row of Nikulin's classification is realised by the catalogue.

A K3 surface with a non-symplectic involution has invariant lattice determined
up to isometry by \((r, a, \delta)\): the rank, the length of the discriminant
group, and Nikulin's parity invariant.  There are 75 such triples.

The catalogue keys a block recipe by each triple.  The two sides of the
assertion therefore come from different places: the triple is transcribed from
the literature, and the invariants are computed from the blocks by the
preamble's own operations -- Sylvester's inertia, the discriminant length, and
delta from the discriminant quadratic form.

One case per row, so a run names every row that fails.  The whole-table
validators raise on the first and report nothing about the rest.
"""

import pytest

from dzack_research.preamble.all import (
    NegativeDefTwoElementary,
    TwoElementary,
    nikulin_invariants,
)


def _name(triple) -> str:
    r"""Name a case by its triple, so a failing row reports which row it is."""
    rank, length, delta = triple
    return f"r{rank}-a{length}-d{delta}"


def test_nikulins_classification_has_seventy_five_types() -> None:
    assert TwoElementary.cardinality() == 75


@pytest.mark.parametrize("triple", tuple(TwoElementary), ids=_name)
def test_each_hyperbolic_type_is_realised(triple) -> None:
    lattice = TwoElementary[triple]

    assert lattice.two_elementary_invariants() == nikulin_invariants(*triple)


@pytest.mark.parametrize("triple", tuple(NegativeDefTwoElementary), ids=_name)
def test_each_negative_definite_type_is_realised(triple) -> None:
    for lattice in NegativeDefTwoElementary[triple]:
        assert lattice.two_elementary_invariants() == nikulin_invariants(*triple)
