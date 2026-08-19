"""
Computational verification of Sterk (1991) cusp classification for
F_{(10,10,0)} = D(T_En) / O(T_En),  T_En = U ⊕ U(2) ⊕ E_8(2).

Test groups
-----------
Fixture-only (fast, no binary calls):
  TestSterkCuspFixtures   – structural properties of the stored cusp representatives.

Binary calls, under 2 min:
  TestSterkZeroCuspOrbits   – k=1 orbit count (~33s).
  TestSterkZeroCuspStabilizers – Stab(ℓ) for the div=2 cusp (~22s).

Binary calls, over 2 min  (marked slow, skipped by default):
  TestSterkZeroCuspStabilizerSlow  – Stab(ℓ) for the div=1 cusp (~4.5 min).
  TestSterkOneCuspOrbits           – k=2 orbit count (~47 min).
  TestSterkOneCuspStabilizers      – Stab(Π) for both 1-cusps.

References
----------
Sterk 1991: H. Sterk, "Compactifications of the period space of Enriques surfaces
            part II", Math. Z. 208 (1991) 1–36.
"""

from __future__ import annotations

import json
import math
import os

import pytest
from src.backends.external.py_polyhedral.binaries import (
    indefinite_form_isotropic_k_plane,
    indefinite_form_stabilizer_isotropic_line,
    indefinite_form_stabilizer_isotropic_plane_2d,
)
from src.lattices.lattices import Lattice

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "coble_literature_fixtures.json")


def _load_sterk_fixture():
    with open(_FIXTURE_PATH) as f:
        records = json.load(f)
    for rec in records:
        if rec.get("id") == "T_En_cusp_orbits_sterk":
            return rec["results"]
    raise KeyError("T_En_cusp_orbits_sterk record not found in fixture")


def _t_en_gram():
    U = Lattice.U()
    E8 = Lattice.E(8)
    T_En = U.direct_sum(U.twist(2)).direct_sum(E8.twist(2))
    G = T_En.inner_product_matrix()
    return [[int(G[i, j]) for j in range(12)] for i in range(12)]


def _quad(G, v):
    n = len(v)
    return sum(G[i][j] * v[i] * v[j] for i in range(n) for j in range(n))


def _inner(G, u, v):
    n = len(u)
    return sum(G[i][j] * u[i] * v[j] for i in range(n) for j in range(n))


def _div(G, v):
    """div(v) = gcd of entries of v G (inner products with standard basis)."""
    n = len(v)
    return math.gcd(*[sum(v[i] * G[i][j] for i in range(n)) for j in range(n)])


def _check_preserves_gram(gens, G, label):
    """All generators satisfy M G M^T = G (polyhedral_common row-vector convention)."""
    n = len(G)
    for idx, M in enumerate(gens):
        MGMt = [[sum(M[i][k] * G[k][m] * M[j][m] for k in range(n) for m in range(n)) for j in range(n)] for i in range(n)]
        assert MGMt == G, f"{label}: gen {idx} violates M G M^T = G"


def _check_stabilizes_line(gens, v, label):
    """All generators satisfy v * M = ±v (setwise stabilizer of span(v)).

    Source: INDEF_FORM_Stabilizer_IsotropicKplane uses TestEqualitySpaces on row spans.
    """
    n = len(v)
    nz = next(j for j in range(n) if v[j] != 0)
    for idx, M in enumerate(gens):
        vM = [sum(v[i] * M[i][j] for i in range(n)) for j in range(n)]
        c_num, c_den = vM[nz], v[nz]
        assert c_num % c_den == 0, f"{label}: gen {idx}: v*M not scalar multiple of v"
        c = c_num // c_den
        assert vM == [c * x for x in v], f"{label}: gen {idx}: v*M={vM} ≠ {c}*v"


def _check_stabilizes_plane(gens, v1, v2, label):
    """All generators preserve span(v1, v2) under right row action.

    Source: INDEF_FORM_Stabilizer_IsotropicKstuff_Kernel uses TestEqualitySpaces
    on the row space of the plane matrix after right-multiplying by each generator.
    """
    n = len(v1)
    # Find two independent pivot columns of the plane.
    b = [v1, v2]
    pivot_cols: list[int] = []
    for j in range(n):
        if len(pivot_cols) == 2:
            break
        if not pivot_cols:
            if b[0][j] != 0 or b[1][j] != 0:
                pivot_cols.append(j)
        else:
            j0 = pivot_cols[0]
            if b[0][j0] * b[1][j] - b[0][j] * b[1][j0] != 0:
                pivot_cols.append(j)
    assert len(pivot_cols) == 2, f"{label}: plane basis not independent"
    j0, j1 = pivot_cols

    for idx, M in enumerate(gens):
        for bi, bv in enumerate(b):
            img = [sum(bv[i] * M[i][j] for i in range(n)) for j in range(n)]
            det = b[0][j0] * b[1][j1] - b[0][j1] * b[1][j0]
            a_num = img[j0] * b[1][j1] - img[j1] * b[1][j0]
            bk_num = b[0][j0] * img[j1] - b[0][j1] * img[j0]
            assert a_num % det == 0 and bk_num % det == 0, f"{label}: gen {idx} maps basis row {bi} outside the plane span"
            a, bk = a_num // det, bk_num // det
            recon = [a * b[0][j] + bk * b[1][j] for j in range(n)]
            assert recon == img, f"{label}: gen {idx} span check failed for basis row {bi}"


# ---------------------------------------------------------------------------
# Fast fixture-only tests
# ---------------------------------------------------------------------------


class TestSterkCuspFixtures:
    """Structural properties of the stored cusp representatives — no binary calls."""

    @pytest.fixture(scope="class")
    def fixture(self):
        return _load_sterk_fixture()

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    def test_two_zero_cusps_in_fixture(self, fixture):
        assert fixture["zero_cusps"]["orbit_count"] == 2

    def test_two_one_cusps_in_fixture(self, fixture):
        assert fixture["one_cusps"]["orbit_count"] == 2

    def test_zero_cusp_reps_isotropic(self, fixture, G):
        for i, rep in enumerate(fixture["zero_cusps"]["representatives"]):
            v = rep[0]
            assert _quad(G, v) == 0, f"zero-cusp {i}: not isotropic"

    def test_zero_cusp_reps_primitive(self, fixture):
        for i, rep in enumerate(fixture["zero_cusps"]["representatives"]):
            v = rep[0]
            assert math.gcd(*v) == 1, f"zero-cusp {i}: not primitive"

    def test_zero_cusp_divisibilities_are_one_and_two(self, fixture, G):
        divs = {_div(G, rep[0]) for rep in fixture["zero_cusps"]["representatives"]}
        assert divs == {1, 2}, f"Expected divisibilities {{1,2}}, got {divs}"

    def test_one_cusp_reps_totally_isotropic(self, fixture, G):
        for i, rep in enumerate(fixture["one_cusps"]["representatives"]):
            v1, v2 = rep[0], rep[1]
            assert _quad(G, v1) == 0, f"one-cusp {i} v1: not isotropic"
            assert _quad(G, v2) == 0, f"one-cusp {i} v2: not isotropic"
            assert _inner(G, v1, v2) == 0, f"one-cusp {i}: plane not totally isotropic"

    def test_one_cusp_reps_primitive(self, fixture):
        for i, rep in enumerate(fixture["one_cusps"]["representatives"]):
            assert math.gcd(*rep[0]) == 1, f"one-cusp {i} v1: not primitive"


# ---------------------------------------------------------------------------
# Zero-cusp orbit count (~33s, not slow)
# ---------------------------------------------------------------------------


class TestSterkZeroCuspOrbits:
    """Verify exactly 2 zero-cusp orbits via live binary call.

    Runtime: ~33s (INDEF_FORM_GetOrbit_IsotropicKplane k=1 on T_En).
    """

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    @pytest.fixture(scope="class")
    def zero_cusp_reps(self, G):
        return indefinite_form_isotropic_k_plane(G, 1)

    def test_exactly_two_zero_cusps(self, zero_cusp_reps):
        assert len(zero_cusp_reps) == 2

    def test_zero_cusp_reps_isotropic(self, zero_cusp_reps, G):
        for i, rep in enumerate(zero_cusp_reps):
            assert _quad(G, rep[0]) == 0, f"zero-cusp {i}: not isotropic"

    def test_zero_cusp_reps_primitive(self, zero_cusp_reps):
        for i, rep in enumerate(zero_cusp_reps):
            assert math.gcd(*rep[0]) == 1, f"zero-cusp {i}: not primitive"

    def test_zero_cusp_divisibilities_are_one_and_two(self, zero_cusp_reps, G):
        divs = {_div(G, rep[0]) for rep in zero_cusp_reps}
        assert divs == {1, 2}


# ---------------------------------------------------------------------------
# Zero-cusp stabilizers: div=2 cusp (~22s, not slow)
# ---------------------------------------------------------------------------


class TestSterkZeroCuspStabilizers:
    """Stab_{O(T_En)}(ℓ) for the div=2 zero-cusp representative.

    Runtime: ~22s (INDEF_FORM_StabilizerIsotropicPlane on the U(2)-block vector).
    """

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    @pytest.fixture(scope="class")
    def div2_rep(self):
        fixture = _load_sterk_fixture()
        G = _t_en_gram()
        reps = fixture["zero_cusps"]["representatives"]
        for rep in reps:
            if _div(G, rep[0]) == 2:
                return rep[0]
        assert False, "No div=2 zero-cusp rep in fixture"

    @pytest.fixture(scope="class")
    def gens_div2(self, G, div2_rep):
        return indefinite_form_stabilizer_isotropic_line(G, div2_rep)

    def test_stabilizer_nonempty(self, gens_div2):
        assert len(gens_div2) > 0

    def test_stabilizer_preserves_gram(self, gens_div2, G):
        _check_preserves_gram(gens_div2, G, "Stab(ℓ_div2)")

    def test_stabilizer_fixes_line(self, gens_div2, G, div2_rep):
        _check_stabilizes_line(gens_div2, div2_rep, "Stab(ℓ_div2)")


# ---------------------------------------------------------------------------
# Slow: div=1 zero-cusp stabilizer (~4.5 min)
# ---------------------------------------------------------------------------


@pytest.mark.slow
class TestSterkZeroCuspStabilizerSlow:
    """Stab_{O(T_En)}(ℓ) for the div=1 zero-cusp representative.

    Runtime: ~271s (INDEF_FORM_StabilizerIsotropicPlane on the U-block vector;
    returns 1386 generators vs 33 for the div=2 cusp).
    """

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    @pytest.fixture(scope="class")
    def div1_rep(self):
        fixture = _load_sterk_fixture()
        G = _t_en_gram()
        reps = fixture["zero_cusps"]["representatives"]
        for rep in reps:
            if _div(G, rep[0]) == 1:
                return rep[0]
        assert False, "No div=1 zero-cusp rep in fixture"

    @pytest.fixture(scope="class")
    def gens_div1(self, G, div1_rep):
        return indefinite_form_stabilizer_isotropic_line(G, div1_rep)

    def test_stabilizer_nonempty(self, gens_div1):
        assert len(gens_div1) > 0

    def test_stabilizer_preserves_gram(self, gens_div1, G):
        _check_preserves_gram(gens_div1, G, "Stab(ℓ_div1)")

    def test_stabilizer_fixes_line(self, gens_div1, G, div1_rep):
        _check_stabilizes_line(gens_div1, div1_rep, "Stab(ℓ_div1)")


# ---------------------------------------------------------------------------
# Slow: one-cusp orbits (~47 min) and stabilizers
# ---------------------------------------------------------------------------


@pytest.mark.slow
class TestSterkOneCuspOrbits:
    """Verify exactly 2 one-cusp orbits via live binary call.

    Runtime: ~2807s (INDEF_FORM_GetOrbit_IsotropicKplane k=2 on T_En).
    """

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    @pytest.fixture(scope="class")
    def one_cusp_reps(self, G):
        return indefinite_form_isotropic_k_plane(G, 2)

    def test_exactly_two_one_cusps(self, one_cusp_reps):
        assert len(one_cusp_reps) == 2

    def test_one_cusp_reps_totally_isotropic(self, one_cusp_reps, G):
        for i, rep in enumerate(one_cusp_reps):
            v1, v2 = rep[0], rep[1]
            assert _quad(G, v1) == 0
            assert _quad(G, v2) == 0
            assert _inner(G, v1, v2) == 0, f"one-cusp {i}: plane not totally isotropic"

    def test_one_cusp_reps_primitive(self, one_cusp_reps):
        for i, rep in enumerate(one_cusp_reps):
            assert math.gcd(*rep[0]) == 1


@pytest.mark.slow
class TestSterkOneCuspStabilizers:
    """Stab_{O(T_En)}(Π) for each one-cusp representative.

    Runtime: unknown; expected to exceed 2 min each based on the div=1 zero-cusp
    stabilizer (~271s) as a lower bound.  Uses fixture representatives to avoid
    re-running the ~47 min orbit computation.
    """

    @pytest.fixture(scope="class")
    def G(self):
        return _t_en_gram()

    @pytest.fixture(scope="class")
    def one_cusp_fixture_reps(self):
        return _load_sterk_fixture()["one_cusps"]["representatives"]

    @pytest.fixture(scope="class")
    def all_stabilizers(self, G, one_cusp_fixture_reps):
        return [indefinite_form_stabilizer_isotropic_plane_2d(G, rep[0], rep[1]) for rep in one_cusp_fixture_reps]

    def test_stabilizers_nonempty(self, all_stabilizers):
        for i, gens in enumerate(all_stabilizers):
            assert len(gens) > 0, f"one-cusp {i}: empty stabilizer"

    def test_stabilizers_preserve_gram(self, all_stabilizers, G):
        for i, gens in enumerate(all_stabilizers):
            _check_preserves_gram(gens, G, f"Stab(Π_{i})")

    def test_stabilizers_fix_planes(self, all_stabilizers, G, one_cusp_fixture_reps):
        for i, (gens, rep) in enumerate(zip(all_stabilizers, one_cusp_fixture_reps)):
            _check_stabilizes_plane(gens, rep[0], rep[1], f"Stab(Π_{i})")
