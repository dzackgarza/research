r"""Scaffold guard: the feature spike's defining property is that it IMPORTS the
base parity spike ("call the spike an import for all future work") and that the
base is functionally live, not merely importable. This test fails if the import
wiring breaks or the base's public lattice surface disappears — the invariant the
directory scaffold exists to protect. It is NOT a placeholder: it exercises real
behavior of the imported base.
"""

from __future__ import annotations

import sage_lattice_category_spike
from sage.all import ZZ

import sage_lattice_feature_spike


def test_feature_spike_reexports_the_base_parity_spike():
    assert sage_lattice_feature_spike.base is sage_lattice_category_spike


def test_base_exposes_its_public_lattice_surface():
    for name in ("Lattices", "DiscriminantForms", "SyntheticLattice", "LatticeMorphism"):
        assert hasattr(sage_lattice_feature_spike.base, name), name


def test_base_is_live_over_ZZ_through_the_import():
    # A real construction over the imported base: build <2> and read its form.
    base = sage_lattice_feature_spike.base
    L = base.Lattices(ZZ).from_gram_matrix([[2]])
    v = L.gen(0)
    assert v.b(v) == 2
