r"""Tier-4: StableGraphCategory (Gamma_{g,n}) core API."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset

from dm_moduli_spike import StableGraphCategory

from dm_moduli_spike.objects.model import DMCompactificationModel


def test_gamma_objects_and_homsets_M11():
    Gamma = StableGraphCategory(1, 1)
    objects = Gamma.objects()
    assert len(objects) == 2
    smooth, special = objects
    assert smooth.num_edges() == 0
    assert special.num_edges() == 1
    assert len(Gamma.hom(special, smooth)) >= 1
    assert len(Gamma.hom(smooth, special)) == 0
    ident = Gamma.identity(smooth)
    assert ident.is_isomorphism()


def test_gamma_specialization_poset_matches_enumerator_M11():
    Gamma = StableGraphCategory(1, 1)
    P = Gamma.specialization_poset()
    assert isinstance(P, FinitePoset)
    legacy = DMCompactificationModel(1, 1).stratification().specialization_poset()
    assert P.cardinality() == legacy.cardinality()
    assert P.is_isomorphic(legacy)
