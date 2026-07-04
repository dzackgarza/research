r"""Literature-cited genus theory the spike reproduces: per-prime local genus
symbols, the Conway-Sloane p-adic invariants (Jordan-constituent tuples,
p-excess / 2-adic oddity, level), and Nikulin's theorem that an even lattice's
genus is fixed by its signature and discriminant form.

The spike is the reference implementation; the literature is the *independent*
oracle. Every expected number below is BOTH (a) verified against the running
spike and (b) either quoted from, or derived from a formula quoted from, a
cited source held in the project Zotero library. Nothing is from memory.

Sources (Zotero item key | Better-BibTeX key | markdown-extraction attachment):

  - J. H. Conway & N. J. A. Sloane, *Sphere Packings, Lattices and Groups*,
    3rd ed. (1999). T2WVLTDB | CS10 | TCJKXU3D. Chapter 15 is the genus /
    p-adic-symbol chapter used throughout:
      * sec 5.1  -- the p-signature, the *oddity* (= 2-signature), the
                    p-excess = (p-signature - dimension) for p>=3 and
                    (dimension - 2-signature) for p=2, and the "p-adic
                    antisquare" p^odd * u_- (p>=3) / 2^odd * u_{+-3} (p=2);
      * sec 7.1  -- the Jordan decomposition f = f_1 (+) p f_p (+) ...; q is the
                    *scale* of the constituent q f_q, n_q = dim f_q;
      * sec 7.2  -- the p-adic symbol (odd p): a product of factors
                    q^{eps_q n_q}, eps_q = (det f_q / p) the Legendre sign;
      * sec 7.4  -- the 2-adic symbol: factors q_{t_q}^{eps_q n_q} carry a type
                    (I / II) and an oddity marker t_q;
      * sec 7.6  -- the *canonical* 2-adic symbol is "absolutely unique"; the
                    raw det-class / oddity are presentation-dependent (oddity
                    fusion, sign walking), so only canonical data is pinnable;
      * sec 7.7  -- the existence conditions: the determinant condition
                    (product of eps_q equals the Legendre symbol of the unit
                    part of det), and the excess formulae
                        p-excess ≡ sum_q n_q (q-1) + 4 k_p   (p>=3),
                        oddity   ≡ sum_q t_q       + 4 k_2   (p=2),
                    where k_p counts the antisquare constituents.
  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). TTY9FFJS | Nik80 | D7BP5F7Z.
      * Thm 1.3.3*  -- Gauss-Milgram: an even lattice of signature (t_+, t_-)
                       has Br(q_L) ≡ t_+ - t_- (mod 8); hence a genus with
                       discriminant form q and signature (t_+, t_-) can exist
                       only if t_+ - t_- ≡ Br(q) (mod 8) (necessary condition).
      * Thm 1.10.1 / Cor 1.9.4 -- the genus of an even lattice is determined by
                       its signature (t_+, t_-) together with its discriminant
                       quadratic form q_L.

Spike language (see ``test_literature_citations.py`` for the lattice-invariant
half, which this module does NOT duplicate): ``L = lc.Lattice(name_or_gram)``;
``g = L.genus()`` answers ``local_symbol_tuples(p)`` (canonical Conway-Sloane
constituent tuples), ``local_excess(p)`` (p-excess; oddity at p=2),
``local_level(p)``, ``local_rank(p)``, ``local_determinant(p)``,
``is_locally_even(p)``; a discriminant form ``q`` answers ``is_genus((t_+,t_-))``
and ``genus((t_+,t_-))``. The gated ``class_number`` / ``representative(s)`` /
``is_unique_class`` (unimplemented, assert False) are NOT touched here.
"""

from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc
from sage.all import ZZ, kronecker, matrix


def _u_plus_2():
    r"""U (+) <2>: even, indefinite, rank-3 lattice with the Gram matrix
    ``matrix(ZZ, 3, [0,1,0, 1,0,0, 0,0,2])`` (hyperbolic plane plus a norm-2
    vector). Nontrivial 2-adic symbol with both a type-II and a type-I
    Jordan constituent."""
    return lc.Lattice(matrix(ZZ, 3, [0, 1, 0, 1, 0, 0, 0, 0, 2]))


def _cs99_local_excess(tuples, p):
    r"""The p-excess (p>=3) / oddity (p=2) computed *independently from the
    canonical Jordan symbol* via the Conway-Sloane existence formulae
    [CS10 Ch.15 sec 7.7]:

        p-excess ≡ sum_q n_q (q - 1) + 4 k_p   (mod 8)   for p >= 3,
        oddity   ≡ sum_q t_q         + 4 k_2   (mod 8)   for p  = 2,

    where a canonical constituent tuple is ``(v, n, eps)`` at odd p and
    ``(v, n, eps, type, t)`` at p=2, the scale is q = p**v [CS10 sec 7.1],
    and k_p counts the p-adic *antisquare* constituents [CS10 sec 5.1]: those
    with q not a square (v odd) and sign eps = -1.

    This is the non-circular core: the value is derived from CS10's formula and
    checked against the spike's ``local_excess``.
    """
    running_total = 0
    antisquares = 0
    for constituent in tuples:
        valuation, dimension, sign = constituent[0], constituent[1], constituent[2]
        scale = p ** valuation                       # q, the Jordan scale (sec 7.1)
        if valuation % 2 == 1 and sign == -1:        # antisquare (sec 5.1)
            antisquares += 1
        if p == 2:
            running_total += constituent[4]          # oddity marker t_q (sec 7.4)
        else:
            running_total += dimension * (scale - 1)  # n_q (q - 1)  (sec 7.7, p>=3)
    return (running_total + 4 * antisquares) % 8


# One row per (nontrivial lattice, prime): the canonical Conway-Sloane symbol
# tuples and every scalar invariant, ALL oracle-verified against the spike and
# reconstructable from CS10 Ch.15. Cheap lattice basics (rank / signature_pair
# / determinant / even / unimodular) are pinned alongside the genus content.
#
# columns: name, lattice, p, canonical tuples,
#          det, rank, sig_pair, even, unimodular, local_det, excess, level
_ROWS = [
    # --- p = 2 (the 2-adic symbol; canonical, sec 7.6) -----------------------
    ("A1", lc.Lattice("A1"), 2, ((1, 1, 1, 1, 1),),
     2, 1, (1, 0), True, False, 2, 1, 2),
    ("A2", lc.Lattice("A2"), 2, ((0, 2, -1, 0, 0),),
     3, 2, (2, 0), True, False, 1, 0, 1),          # canonical det-class -1 (raw 3)
    ("A3", lc.Lattice("A3"), 2, ((0, 2, -1, 0, 0), (2, 1, -1, 1, 3)),
     4, 3, (3, 0), True, False, 4, 3, 4),
    ("D4", lc.Lattice("D4"), 2, ((0, 2, -1, 0, 0), (1, 2, -1, 0, 0)),
     4, 4, (4, 0), True, False, 4, 4, 2),          # oddity 4 from the antisquare term
    ("E7", lc.Lattice("E7"), 2, ((0, 6, 1, 0, 0), (1, 1, 1, 1, 7)),
     2, 7, (7, 0), True, False, 2, 7, 2),
    ("E8", lc.Lattice("E8"), 2, ((0, 8, 1, 0, 0),),
     1, 8, (8, 0), True, True, 1, 0, 1),
    ("U", lc.Lattice("U"), 2, ((0, 2, 1, 0, 0),),
     -1, 2, (1, 1), True, True, 1, 0, 1),
    ("U+<2>", _u_plus_2(), 2, ((0, 2, 1, 0, 0), (1, 1, 1, 1, 1)),
     -2, 3, (2, 1), True, False, 2, 1, 2),         # canonical det-class +1 (raw 3)
    ("E8+E8", lc.Lattice("E8").direct_sum(lc.Lattice("E8")), 2, ((0, 16, 1, 0, 0),),
     1, 16, (16, 0), True, True, 1, 0, 1),
    # --- p = 3 (the odd-p symbol, sec 7.2) -----------------------------------
    ("A2", lc.Lattice("A2"), 3, ((0, 1, -1), (1, 1, -1)),
     3, 2, (2, 0), True, False, 3, 6, 3),
    ("E6", lc.Lattice("E6"), 3, ((0, 5, 1), (1, 1, 1)),
     3, 6, (6, 0), True, False, 3, 2, 3),
    ("A2+A2", lc.Lattice("A2").direct_sum(lc.Lattice("A2")), 3, ((0, 2, 1), (1, 2, 1)),
     9, 4, (4, 0), True, False, 9, 4, 3),
    ("E8", lc.Lattice("E8"), 3, ((0, 8, 1),),
     1, 8, (8, 0), True, True, 1, 0, 1),
    # --- p = 5 (a prime not dividing the determinant: trivial symbol) --------
    ("E8", lc.Lattice("E8"), 5, ((0, 8, 1),),
     1, 8, (8, 0), True, True, 1, 0, 1),
]


def test_local_genus_symbols_and_p_adic_invariants_match_conway_sloane_ch15():
    r"""Per-prime local genus symbols and p-adic invariants against
    Conway-Sloane, *SPLAG* Ch.15 [CS10], across positive-definite root
    lattices, an even unimodular lattice (E_8, E_8^2), the hyperbolic plane U,
    and the indefinite U (+) <2>.

    For each (lattice, p) the test pins the CANONICAL Jordan symbol tuples
    (sec 7.6: canonical is "absolutely unique"; the raw det-class is
    presentation-dependent, e.g. A_2 at p=2 canonically carries det-class -1
    while the raw symbol shows 3) and then checks the derived invariants:

      * local rank = sum of constituent dimensions = rank L (sec 7.1);
      * v_p(local determinant) = sum_q v * n_q  (Jordan scales, sec 7.1);
      * determinant condition (sec 7.7, p>=3): product of the signs eps_q
        equals the Legendre symbol of the prime-to-p part of the determinant;
      * local level = p^(max scale exponent) (highest Jordan scale);
      * p-excess / oddity re-derived from CS10's sec-7.7 excess formula
        (``_cs99_local_excess``) and matched against the spike, so the
        agreement is not merely the spike checked against itself.

    Cheap lattice basics (rank, signature pair, determinant, even, unimodular)
    are asserted for every lattice alongside the genus content.
    """
    for (name, lattice, p, tuples, determinant, rank, sig_pair, even,
         unimodular, local_det, excess, level) in _ROWS:
        tag = f"{name} @ p={p}"

        # cheap lattice basics (characterization, always asserted)
        assert lattice.rank() == rank, tag
        assert lattice.signature_pair() == sig_pair, tag
        assert lattice.determinant() == determinant, tag
        assert lattice.is_even() is even, tag
        assert lattice.is_unimodular() is unimodular, tag

        genus = lattice.genus()

        # (1) canonical Conway-Sloane symbol tuples, pinned exactly (sec 7.2/7.4/7.6)
        assert genus.local_symbol_tuples(p) == tuples, tag

        # (2) local rank = rank; local level = p^(largest Jordan scale)  (sec 7.1)
        assert genus.local_rank(p) == rank, tag
        assert genus.local_level(p) == p ** max(t[0] for t in tuples), tag

        # (3) determinant: pinned value + valuation = sum of scale*dim  (sec 7.1)
        assert genus.local_determinant(p) == local_det, tag
        assert ZZ(local_det).valuation(p) == sum(t[0] * t[1] for t in tuples), tag

        # (4) determinant condition, odd p (sec 7.7): prod eps_q = (unit part | p)
        if p != 2:
            sign_product = 1
            for t in tuples:
                sign_product *= t[2]
            unit_part = local_det // p ** ZZ(local_det).valuation(p)
            assert sign_product == kronecker(unit_part, p), tag

        # (5) p-excess / oddity: CS10 sec-7.7 formula == spike == pinned value
        assert _cs99_local_excess(tuples, p) == genus.local_excess(p) % 8 == excess, tag

        # (6) even type: an even lattice is 2-adically even (type II unimodular
        #     part); at odd p the symbol is always even-typed  (sec 7.3)
        assert genus.is_locally_even(p) == (lattice.is_even() if p == 2 else True), tag


def test_genus_determined_by_signature_and_discriminant_form_nikulin_1_10_1():
    r"""Nikulin, Thm 1.10.1 / Cor 1.9.4 [Nik80]: the genus of an even lattice is
    determined by its signature (t_+, t_-) together with its discriminant
    quadratic form q_L. Demonstrated through ``same_genus`` / genus equality and
    the reconstruction of a lattice's genus from (q_L, signature).

      * A_2 in two Gram presentations ([[2,-1],[-1,2]] and [[2,1],[1,2]], both
        det 3): SAME signature and SAME discriminant form => same genus.
      * A_2 vs A_1 (+) A_1: same signature (2,0) but discriminant forms C_3 vs
        (C_2)^2 => DIFFERENT genus.
      * A_2 vs A_2(-1): |disc| equal but signatures (2,0) vs (0,2) differ =>
        DIFFERENT genus (both invariants are needed).
      * A_2, A_2 (+) U, A_2 (+) U^2 share the discriminant form q_{A_2} (U is
        unimodular) across signatures (2,0), (3,1), (4,2): each lattice's genus
        is exactly ``q_{A_2}.genus(signature)``.
    """
    A2 = lc.Lattice("A2")
    A2_other_basis = lc.Lattice(matrix(ZZ, 2, [2, 1, 1, 2]))  # det 3, isometric to A2
    A1A1 = lc.Lattice("A1").direct_sum(lc.Lattice("A1"))
    A2m = A2.twist(-1)
    U = lc.Lattice("U")

    # cheap basics of the participating lattices
    assert (A2.rank(), A2.signature_pair(), A2.determinant()) == (2, (2, 0), 3)
    assert A2.is_even() and not A2.is_unimodular()
    assert (A2_other_basis.rank(), A2_other_basis.signature_pair(),
            A2_other_basis.determinant()) == (2, (2, 0), 3)
    assert A2_other_basis.is_even() and not A2_other_basis.is_unimodular()
    assert (A1A1.rank(), A1A1.signature_pair(), A1A1.determinant()) == (2, (2, 0), 4)
    assert A1A1.is_even() and not A1A1.is_unimodular()
    assert (A2m.rank(), A2m.signature_pair(), A2m.determinant()) == (2, (0, 2), 3)
    assert A2m.is_even() and not A2m.is_unimodular()

    # same (signature, discriminant form) => same genus  [Nik80 Thm 1.10.1]
    assert A2.same_genus(A2_other_basis)
    assert A2.genus() == A2_other_basis.genus()

    # same signature, different discriminant form => different genus
    assert not A2.same_genus(A1A1)
    assert A2.genus() != A1A1.genus()

    # opposite signature, same |disc| => different genus (signature matters too)
    assert not A2.same_genus(A2m)
    assert A2.genus() != A2m.genus()

    # genus reconstructed from (q_L, signature) equals the lattice's own genus
    q = A2.discriminant_group()
    assert q.genus((2, 0)) == A2.genus()

    # witnesses sharing q_{A2} across signatures (U is unimodular, so adding it
    # leaves the discriminant form unchanged)  [Nik80 Thm 1.10.1]
    w31 = A2.direct_sum(U)          # signature (3, 1)
    w42 = w31.direct_sum(U)         # signature (4, 2)
    assert w31.signature_pair() == (3, 1) and w31.determinant() == -3
    assert w42.signature_pair() == (4, 2) and w42.determinant() == 3
    assert w31.discriminant_group().is_isomorphic(q, kind="quadratic")
    assert w42.discriminant_group().is_isomorphic(q, kind="quadratic")
    assert q.genus((3, 1)) == w31.genus()
    assert q.genus((4, 2)) == w42.genus()


def test_is_genus_respects_gauss_milgram_signature_congruence_nikulin_1_3_3():
    r"""``q.is_genus((t_+, t_-))`` decides whether an even lattice with
    discriminant form q_{A_2} (group C_3, Brown/Gauss-sum invariant 2) and the
    given signature exists. The decisions are oracle-pinned, and the necessary
    Gauss-Milgram condition [Nik80 Thm 1.3.3*: an even lattice has
    t_+ - t_- ≡ Br(q) (mod 8)] is enforced: whenever the signature fails that
    congruence, no genus can exist, so ``is_genus`` must return False
    (contrapositive of the necessary condition).

    The three admissible signatures are witnessed by actual even lattices with
    discriminant form q_{A_2}: (2,0) by A_2, (3,1) by A_2 (+) U, (4,2) by
    A_2 (+) U^2 (see the Nikulin 1.10.1 test).
    """
    A2 = lc.Lattice("A2")
    q = A2.discriminant_group()

    # cheap basics of the carrier lattice
    assert A2.rank() == 2 and A2.determinant() == 3
    assert A2.is_even() and A2.signature_pair() == (2, 0)
    assert tuple(q.invariants()) == (3,)  # discriminant group C_3

    brown = q.brown_invariant()
    assert brown == 2  # Gauss-sum invariant of q_{A_2}, oracle-pinned

    # (signature) -> genus exists? -- oracle-verified decisions
    existence = {
        (2, 0): True,   # 2 ≡ 2   -- witnessed by A_2
        (0, 2): False,  # -2 ≡ 6  -- congruence fails
        (3, 1): True,   # 2 ≡ 2   -- witnessed by A_2 (+) U
        (1, 3): False,  # -2 ≡ 6  -- congruence fails
        (6, 0): False,  # 6 ≡ 6   -- congruence fails
        (4, 2): True,   # 2 ≡ 2   -- witnessed by A_2 (+) U^2
    }
    for signature, exists in existence.items():
        assert q.is_genus(signature, even=True) == exists, signature
        congruent = (signature[0] - signature[1]) % 8 == brown % 8
        # Nik80 Thm 1.3.3* (contrapositive): congruence-failure forbids a genus
        if not congruent:
            assert not exists, signature
            assert not q.is_genus(signature, even=True), signature
        else:
            assert exists, signature  # here congruence is also sufficient
