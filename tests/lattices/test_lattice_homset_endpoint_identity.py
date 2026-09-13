r"""Lattice Hom caches are keyed by endpoint identity, not lattice hashing."""

import pytest

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.lattice_morphisms import (
    lattice_embedding_homset,
    lattice_homset,
    lattice_isometry_homset,
)


def test_unhashable_lattice_endpoints_have_stable_hom_embedding_and_isometry_parents() -> None:
    source = Lattices(ZZ)([[2]])
    target = Lattices(ZZ)([[2]])

    with pytest.raises(TypeError):
        hash(source)

    assert lattice_homset(source, target) is lattice_homset(source, target)
    assert lattice_embedding_homset(source, target) is lattice_embedding_homset(
        source, target
    )
    assert lattice_isometry_homset(source, target) is lattice_isometry_homset(
        source, target
    )
    assert source.Aut() is source.Aut()
    assert source.Aut().domain() is source
    assert source.Aut().codomain() is source
