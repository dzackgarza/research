r"""The catalogue realises Nikulin's classification.

`DEV-41`: the expected values are cited data in ``tests/fixtures``; this file is
a driver over them and contains no literal invariants.  The two sides come from
different places, which is what makes the assertion able to fail: the triples
are transcribed from the literature, and the invariants are computed from block
recipes by the preamble's own operations.
"""

import pytest

from dzack_research.preamble.all import (
    NegativeDefTwoElementary,
    TwoElementary,
    nikulin_invariants,
)
from tests.fixtures.lattices.two_elementary import (
    K3_INVOLUTION_TYPES,
    NEGATIVE_DEFINITE_TYPES,
)


def test_the_catalogue_carries_every_cited_k3_involution_type() -> None:
    assert TwoElementary.cardinality() == len(K3_INVOLUTION_TYPES.value)


@pytest.mark.parametrize("triple", K3_INVOLUTION_TYPES.value)
def test_each_cited_k3_involution_type_is_realised(triple) -> None:
    lattice = TwoElementary[triple]

    assert lattice.two_elementary_invariants() == nikulin_invariants(*triple)


def test_the_catalogue_carries_every_cited_negative_definite_type() -> None:
    assert NegativeDefTwoElementary.cardinality() == len(NEGATIVE_DEFINITE_TYPES.value)


@pytest.mark.parametrize("triple", NEGATIVE_DEFINITE_TYPES.value)
def test_each_cited_negative_definite_type_is_realised(triple) -> None:
    for lattice in NegativeDefTwoElementary[triple]:
        assert lattice.two_elementary_invariants() == nikulin_invariants(*triple)
