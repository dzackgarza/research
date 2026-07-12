r"""Root-lattice shell/dual/LLL arithmetic pinned to Conway & Sloane, *SPLAG*.

Every expected value here is (a) quoted from an authoritative source held in the
project Zotero library and (b) independently reproduced by running the spike as
the reference implementation. The spike is checked against the *published*
number; nothing is asserted from memory.

Zotero source (all identifiers confirmed against the live local API at
``http://127.0.0.1:23119`` on 2026-07-04):

  - Conway & Sloane, *Sphere Packings, Lattices and Groups* (3rd ed.).
    Zotero item key ``T2WVLTDB``; Better-BibTeX citation key ``CS10`` (the
    library item is the 2010 softcover reprint of the 1999 3rd edition). The
    markdown extraction indexed by the line numbers below is attachment
    ``TCJKXU3D`` (``Conway and Sloane - 1999 - Sphere Packings, Lattices and
    Groups.md``).

Theme (deliberately disjoint from ``test_literature_citations.py``, which already
pins per-lattice determinant / minimal norm / root count and the glue-group
invariant factors): the *higher* theta-series shell counts N(4), N(6), the dual
lattice determinant det(L^*) = 1/det(L), and the fact that LLL/reduced_basis is a
determinant-, discriminant-, and theta-preserving reduction. Cheap basics (rank,
signature, determinant, even, unimodular) are asserted in every test as the
lattice's characterization, alongside — never instead of — the significant
content.

Spike language: ``lc.Lattice(name)`` builds the named root lattice; a lattice
answers ``rank`` / ``signature_pair`` / ``determinant`` / ``is_even`` /
``is_unimodular`` / ``minimum`` / ``maximum`` / ``roots`` / ``vectors_of_square``
/ ``short_vectors`` / ``dual`` / ``LLL`` / ``reduced_basis``, and
``discriminant_group().invariants()`` returns the glue-group structure.
"""

from __future__ import annotations

from sage.all import QQ, Infinity
import pytest

import sage_lattice_category_spike.lattice_categories as lc


# (name, rank, det, is_unimodular, [N(0), N(2), N(4), N(6)], CS10 theta-series location)
# Every lattice below is even and positive definite, so signature_pair == (rank, 0)
# and the only nonzero shells among norms 0..6 sit at the even norms.
_THETA = [
    # A_2 (hexagonal): Theta_{A_2} = 1 + 6 q^2 + 6 q^6      [CS10 sec 6.2, line 4744]
    ("A2", 2, 3, False, [1, 6, 0, 6]),
    # E_6: 1 + 72 q^2 + 270 q^4 + 720 q^6                   [CS10 sec 8.3, line 5196]
    ("E6", 6, 3, False, [1, 72, 270, 720]),
    # E_7: 1 + 126 q^2 + 756 q^4 + 2072 q^6                 [CS10 sec 8.2, line 5131]
    ("E7", 7, 2, False, [1, 126, 756, 2072]),
    # E_8: 1 + 240 q^2 + 2160 q^4 + ...,  N_m = 240 sigma_3(m/2)
    #   => N(6) = 240 * sigma_3(3) = 240 * 28 = 6720        [CS10 sec 8.1, line 5049]
    ("E8", 8, 1, True, [1, 240, 2160, 6720]),
]


@pytest.mark.parametrize("name, rank, det, unimodular, shells", _THETA)
def test_theta_series_low_shells_match_conway_sloane(name, rank, det, unimodular, shells):
    r"""[CS10 / Zotero T2WVLTDB] SPLAG Ch. 4 prints the theta series of A_2
    (sec 6.2), E_6, E_7, E_8 (secs 8.1-8.3) explicitly; the coefficient of q^m is
    N(m), the number of lattice vectors of norm m. This pins the *shell census*
    N(0), N(2), N(4), N(6) -- the norm-4 and norm-6 shells go beyond the kissing
    number N(2) already pinned in test_literature_citations. The two enumeration
    entry points must agree with each other and with the published series:
    vectors_of_square(m) reports one shell, short_vectors(k) reports shells for
    norms 0..k-1, and minimum/maximum bound the census.
    """
    L = lc.Lattice(f"{name}(-1)")   # Conway-Sloane root lattices are positive definite; the AG default is negative

    # cheap basics: the lattice's characterization
    assert L.rank() == rank
    assert L.signature_pair() == (rank, 0)
    assert L.determinant() == det
    assert L.is_even()
    assert L.is_unimodular() is unimodular

    # significant content: the CS10 theta-series shell counts
    N0, N2, N4, N6 = shells
    assert len(L.vectors_of_square(0)) == N0
    assert len(L.vectors_of_square(2)) == N2
    assert len(L.vectors_of_square(4)) == N4
    assert len(L.vectors_of_square(6)) == N6

    # short_vectors(7) gives shells for norms 0..6; even lattice => odd norms empty
    assert [len(shell) for shell in L.short_vectors(7)] == [N0, 0, N2, 0, N4, 0, N6]

    # enumerator min/max agree with the census (first nonzero shell is norm 2)
    assert L.minimum() == 2
    assert L.maximum() is Infinity


# (name, rank, det, dual_det, CS10 dual-section location)
_DUAL = [
    # A_n^* : det = 1/(n+1)                                 [CS10 sec 6.6, line 4845]
    ("A2", 2, 3, QQ(1) / 3),
    ("A4", 4, 5, QQ(1) / 5),
    # D_n^* : det = 1/4                                     [CS10 sec 7.4, line 4998]
    ("D5", 5, 4, QQ(1) / 4),
    ("D6", 6, 4, QQ(1) / 4),
    # E_6^* : det = 1/3                                     [CS10 sec 8.3, line 5219]
    ("E6", 6, 3, QQ(1) / 3),
    # E_7^* : det = 1/2                                     [CS10 sec 8.2, line 5148]
    ("E7", 7, 2, QQ(1) / 2),
    # E_8^* = E_8 : det = 1                                 [CS10 sec 8.1, line 5034]
    ("E8", 8, 1, QQ(1)),
]


@pytest.mark.parametrize("name, rank, det, dual_det", _DUAL)
def test_dual_lattice_determinants_match_conway_sloane(name, rank, det, dual_det):
    r"""[CS10 / Zotero T2WVLTDB] SPLAG Ch. 4 tabulates each dual lattice: A_n^*
    has det 1/(n+1) (sec 6.6), D_n^* has det 1/4 (sec 7.4), E_6^* has det 1/3
    (sec 8.3), E_7^* has det 1/2 (sec 8.2), and E_8^* = E_8 with det 1 (sec 8.1).
    The spike's dual carries Gram G^{-1}, so det(L^*) = 1/det(L); this checks that
    identity against the published dual determinants. E_8 is self-dual, so its
    dual is again integral with minimal norm 2 (E_8^* = E_8).
    """
    L = lc.Lattice(f"{name}(-1)")   # Conway-Sloane root lattices are positive definite; the AG default is negative

    # cheap basics
    assert L.rank() == rank
    assert L.signature_pair() == (rank, 0)
    assert L.determinant() == det
    assert L.is_even()

    # significant content: published dual determinant
    dual = L.dual()
    assert dual.determinant() == dual_det
    assert dual.determinant() == QQ(1) / L.determinant()

    # E_8 alone is self-dual: its dual is integral and unimodular with minimum 2
    if name == "E8":
        assert L.is_unimodular()
        assert dual.determinant() == 1
        assert dual.minimum() == 2
    else:
        assert not L.is_unimodular()


# (name, rank, det, glue invariant factors, root count, CS10 location)
_LLL = [
    ("E6", 6, 3, (3,), 72),    # [CS10 sec 8.3, lines 5185/5191/5196]
    ("E7", 7, 2, (2,), 126),   # [CS10 sec 8.2, lines 5122/5128/5131]
    ("E8", 8, 1, (), 240),     # [CS10 sec 8.1, lines 5034/5049]
    ("D6", 6, 4, (2, 2), 60),  # [CS10 sec 7.1, lines 4910/4919]
]


@pytest.mark.parametrize("name, rank, det, glue, tau", _LLL)
def test_lll_reduction_preserves_conway_sloane_invariants(name, rank, det, glue, tau):
    r"""[CS10 / Zotero T2WVLTDB] LLL / reduced_basis change the generating basis
    but not the lattice, so they must preserve every isometry invariant published
    in SPLAG Ch. 4: the determinant, the glue group L^*/L (secs 6.1/7.1/8.1-8.3),
    and the theta series -- in particular the kissing number N(2) = number of
    roots. This pins L.LLL() invariants back to the CS10 values and asserts they
    equal L's own (the reduction is invariant-preserving). reduced_basis returns
    exactly rank vectors.
    """
    L = lc.Lattice(f"{name}(-1)")   # Conway-Sloane root lattices are positive definite; the AG default is negative

    # cheap basics on the input lattice
    assert L.rank() == rank
    assert L.signature_pair() == (rank, 0)
    assert L.determinant() == det
    assert L.is_even()

    reduced = L.LLL()

    # significant content: LLL preserves the CS10 invariants
    assert reduced.determinant() == det == L.determinant()
    assert reduced.discriminant_group().invariants() == glue
    assert reduced.discriminant_group().invariants() == L.discriminant_group().invariants()
    assert len(reduced.roots()) == tau == len(L.roots())
    assert reduced.is_even() == L.is_even()
    assert reduced.is_unimodular() == L.is_unimodular()
    assert len(L.reduced_basis()) == rank
