r"""Lattice Mor caches are keyed by endpoint identity, not lattice hashing."""

import pytest

from dzack_research.preamble.all import ZZ, Lattices

def test_unhashable_lattice_endpoints_have_stable_mor_embedding_and_isometry_parents() -> None:
    source = Lattices(ZZ)([[2]])
    target = Lattices(ZZ)([[2]])

    with pytest.raises(TypeError):
        hash(source)

    assert source.Mor(target) is source.Mor(target)
    assert source.Emb(target) is source.Emb(target)
    assert source.Isom(target) is source.Isom(target)
    assert source.Aut() is source.Aut()
    assert source.Aut().domain() is source
    assert source.Aut().codomain() is source
