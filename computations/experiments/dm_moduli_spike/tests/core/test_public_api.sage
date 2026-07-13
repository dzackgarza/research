r"""Tier-4: public API surface for geometric ontology + Γ."""

from __future__ import annotations

import dm_moduli_spike as spike
from dm_moduli_spike import M_gn, StableGraphCategory, spec
from sage.rings.rational_field import QQ


def test_public_all_includes_moduli_and_gamma():
    for name in ["M_gn", "Mbar_gn", "StableGraphCategory", "ModuliStacks", "Stacks", "spec"]:
        assert name in spike.__all__
    for name in [
        "DMCompactificationModel",
        "ModuliFactor",
        "DMStratum",
        "StableGraphTypes",
        "StableGraphStratification",
        "StableGraphStratificationEnumerator",
        "AutomorphismAction",
    ]:
        assert name not in spike.__all__


def test_gamma_still_public():
    Gamma = StableGraphCategory(1, 1)
    assert Gamma.specialization_poset().cardinality() == 2


def test_m_gn_public():
    XS = M_gn(0, 4, base=spec(QQ))
    assert XS.dimension() == 1
