r"""Public Sage import surface for the research workspace."""

from __future__ import annotations


def test_research_package_exposes_the_base_and_feature_spikes():
    r"""Both public routes construct the same A2 lattice and its order-three form."""
    from dzack_research import feature, lattice

    base_lattice = lattice.Lattice("A2")
    feature_lattice = feature.base.Lattice("A2")

    assert base_lattice.gram_matrix() == feature_lattice.gram_matrix()
    assert base_lattice.discriminant_group().cardinality() == 3
