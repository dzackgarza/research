"""Consuming test for the literature fixtures in tests/fixtures/coble_literature_fixtures.json.

The fixture stores literature-sourced expected values, each cited to a Zotero item +
markdown extraction attachment + line (per the `What A Test Cites` contract). This test
makes the fixture GATE something: it builds the object through the lattice DSL and asserts
it recovers the cited mathematical facts. A test passes only when the backend recovers the
fact; it is red while the backend is incomplete.

Exemplar entry: `K3_lattice_L` — the K3 lattice L = II_{3,19} = U^3 + E8^2, cited to
Conway/AEGS item LFKH3D95, extraction UXUDEAF4 line 197-198 ("L=II_{3,19}=U^3+E_8^2 ...
even, unimodular, signature (3,19)"). Signature is asserted unordered because the sign of
the E8 block is a convention (AEGS uses negative-definite E8; Sage's E8 is positive).
The remaining fixture entries follow this same pattern.
"""

from __future__ import annotations

import importlib
import json
import pathlib

from sage.all import ZZ

importlib.import_module("category_specs")
Lattices = importlib.import_module("category_specs.lattices").Lattices

_FIX = json.loads(
    (pathlib.Path(__file__).resolve().parents[1] / "fixtures" / "coble_literature_fixtures.json").read_text()
)
_BY_ID = {e["id"]: e for e in _FIX}


def _ctor():
    return Lattices(ZZ).Constructors()


class TestK3LatticeFixture:
    """L = U^3 + E8^2, cited to LFKH3D95 / UXUDEAF4:197-198."""

    def _build(self):
        C = _ctor()
        U = C.IntegralLattice(hyperbolic_plane="U")
        E8 = C.IntegralLattice(cartan_type="E8")
        return C.IntegralLatticeDirectSum(lattices=[U, U, U, E8, E8])

    def test_even_matches_fixture(self) -> None:
        assert self._build().is_even() is _BY_ID["K3_lattice_L"]["properties"]["even"]

    def test_unimodular_matches_fixture(self) -> None:
        assert self._build().is_unimodular() is _BY_ID["K3_lattice_L"]["properties"]["unimodular"]

    def test_signature_matches_fixture_unordered(self) -> None:
        L = self._build()
        pos, neg = L.signature_pair()
        assert sorted([pos, neg]) == sorted(_BY_ID["K3_lattice_L"]["properties"]["signature"])
