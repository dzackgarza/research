r"""Literature-cited computations the spike reproduces.

Every expected value here is taken from an authoritative source held in the
project Zotero library, NOT from the spike's own backing and NOT from memory. A
green test proves the spike computes the *published* value; Sage is the reference
implementation, and the literature is the independent oracle it is checked
against. Only convention-independent data is pinned (determinants, root counts,
discriminant-group structure, isometry relations, signatures) — raw q(x) values
carry a sign/normalization convention and are deliberately not pinned to a stated
number.

Sources (Zotero item key | Better-BibTeX key | markdown-extraction attachment):

  - Conway & Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. (1999).
    T2WVLTDB | CS99 | TCJKXU3D. Ch. 4 tabulates the root lattices A_n, D_n, E_6,
    E_7, E_8 (determinant, minimal norm, kissing number, glue group); Ch. 2
    sec 2.4: the glue group L^*/L has order det L.
  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). TTY9FFJS | Nik80 | D7BP5F7Z. Thm 1.3.3* is the
    Gauss-Milgram signature-(mod 8) relation; Cor 1.6.2 is the orthogonal-
    complement anti-isometry q_S = -q_K.
  - S. Kondo, *K3 Surfaces* (EMS, 2020). F288JVXK | Kon20. Example 1.4 (U);
    Cor 1.26 (even unimodular => p - q divisible by 8); Thm 1.25 (classification
    L = U^q + E8(-1)^{(p-q)/8}); the K3 lattice H^2(X,Z) has rank 22.

Written in the spike's public language: ``lc.Lattice(name)`` builds a root
lattice or a named unimodular piece; a lattice answers determinant / minimum /
roots / signature(_pair) / is_even / is_unimodular / twist / direct_sum;
``discriminant_group`` returns the finite quadratic form q_L, which answers
invariants, is_isomorphic, and brown_invariant.
"""

from __future__ import annotations

from functools import reduce
from math import prod

import sage_lattice_category_spike.lattice_categories as lc


def _direct_sum(*lattices):
    return reduce(lambda a, b: a.direct_sum(b), lattices)


def test_irreducible_root_lattice_invariants_match_conway_sloane_chapter_4():
    r"""Determinant, minimal norm, and number of roots of every irreducible root
    lattice, pinned to Conway & Sloane, *SPLAG* Chapter 4 [CS99]. For a root
    lattice the minimal vectors ARE the roots (minimal norm 2), so the kissing
    number tau equals the number of roots:

      - A_n (sec 6.1): det = n+1, min norm 2, tau = n(n+1);
      - D_n (sec 7.1): det = 4,   min norm 2, tau = 2n(n-1);
      - E_6 (sec 8.3): det = 3,   min norm 2, tau = 72;
      - E_7 (sec 8.2): det = 2,   min norm 2, tau = 126;
      - E_8 (sec 8.1): det = 1,   min norm 2, tau = 240.
    """
    # (spike name, CS99 determinant, CS99 kissing number = number of roots)
    cs99 = {}
    for n in range(1, 9):
        cs99[f"A{n}"] = (n + 1, n * (n + 1))            # sec 6.1
    for n in range(4, 9):
        cs99[f"D{n}"] = (4, 2 * n * (n - 1))            # sec 7.1
    cs99["E6"] = (3, 72)                                # sec 8.3
    cs99["E7"] = (2, 126)                               # sec 8.2
    cs99["E8"] = (1, 240)                               # sec 8.1
    for name, (determinant, tau) in cs99.items():
        lattice = lc.Lattice(name)
        assert lattice.determinant() == determinant, name
        assert lattice.minimum() == 2, name
        assert len(lattice.roots()) == tau, name


def test_root_lattice_discriminant_groups_are_the_conway_sloane_glue_groups():
    r"""The discriminant group L^*/L of a root lattice is the Conway-Sloane glue
    group: order = det L [CS99 sec 2.4], with invariant-factor structure from
    [CS99 Ch. 4]:

      - A_n: cyclic C_{n+1}                       (sec 6.1);
      - D_n: Klein four V_4 = (C_2)^2 if n even,
             cyclic C_4 if n odd                  (sec 7.1);
      - E_6: C_3;  E_7: C_2;  E_8: trivial         (secs 8.1-8.3;
             "E_8^* = E_8, so there is no glue").
    """
    expected = {}
    for n in range(1, 9):
        expected[f"A{n}"] = (n + 1,)                          # cyclic C_{n+1}
    for n in range(4, 9):
        expected[f"D{n}"] = (2, 2) if n % 2 == 0 else (4,)    # V_4 (even) / C_4 (odd)
    expected["E6"], expected["E7"], expected["E8"] = (3,), (2,), ()
    for name, invariant_factors in expected.items():
        lattice = lc.Lattice(name)
        discriminant_group = lattice.discriminant_group()
        assert tuple(discriminant_group.invariants()) == invariant_factors, name
        order = prod(invariant_factors)   # prod(()) == 1 for E8
        assert order == lattice.determinant(), name          # |L^*/L| = det L


def test_nikulin_orthogonal_complement_anti_isometry_corollary_1_6_2():
    r"""Nikulin, Corollary 1.6.2 [Nik80]: an even lattice S has an even lattice K
    as its orthogonal complement in SOME even unimodular lattice if and only if
    q_S = -q_K (isomorphic finite quadratic forms). Equivalently, for S and K
    orthogonal complements inside an even unimodular lattice, q_K = -q_S; here
    -q_S is the discriminant form of S(-1) (``S.twist(-1)``).

    Verified on genuine complementary pairs inside E_8 (even unimodular):
    A_1^perp = E_7, A_2^perp = E_6, A_4^perp = A_4, D_4^perp = D_4. The negative
    control A_1/A_1 shows the criterion discriminates: q_{A_1} = <1/2> is NOT
    isomorphic to -q_{A_1} = <3/2> on Z/2, so A_1 is not self-complementary in an
    even unimodular lattice (indeed A_1 + A_1 has no even unimodular overlattice
    with A_1^perp = A_1).
    """
    def anti_isometric(s_name, k_name):
        q_s = lc.Lattice(s_name).discriminant_group()
        minus_q_k = lc.Lattice(k_name).twist(-1).discriminant_group()
        return q_s.is_isomorphic(minus_q_k, kind="quadratic")

    # complementary pairs in E_8 => q_S = -q_K holds
    for s_name, k_name in [("E7", "A1"), ("E6", "A2"), ("A4", "A4"), ("D4", "D4")]:
        assert anti_isometric(s_name, k_name), f"{s_name} perp {k_name}"
    # non-complementary: A_1 is not self-complementary (q_{A1} != -q_{A1})
    assert not anti_isometric("A1", "A1")


def test_gauss_milgram_signature_congruence_nikulin_theorem_1_3_3():
    r"""Gauss-Milgram / Milgram's formula (Milnor-Husemoller App. 4; CS99 Ch. 15;
    exactly Nikulin Thm 1.3.3* [Nik80]).

    The Brown invariant Br(q) of a finite quadratic form q on a group D is DEFINED
    (Sage's own definition) as the element of Z/8 with
        exp(2*pi*i/8 * Br(q)) = (1/sqrt|D|) * sum_{x in D} exp(i*pi*q(x)),
    i.e. the argument of the Gauss sum of q — a property of the finite form alone,
    computed with no reference to any lattice signature. Milgram's THEOREM states
    that when q = q_L is the discriminant form of an even lattice L of signature
    (t_+, t_-),
        Br(q_L)  ==  t_+ - t_-   (mod 8).
    The test is thus non-circular: it computes a Gauss-sum invariant of the finite
    discriminant form and checks it against the lattice signature. Checked across
    positive-definite, negative-definite, and indefinite even lattices so the
    congruence is not an artifact of one signature regime.
    """
    U = lc.Lattice("U")
    E8 = lc.Lattice("E8")
    even_lattices = [
        lc.Lattice("A2"),                 # (2, 0)
        lc.Lattice("E7"),                 # (7, 0)
        E8,                               # (8, 0), q trivial
        U,                                # (1, 1), q trivial
        lc.Lattice("A2").twist(-1),       # (0, 2)
        E8.twist(-1),                     # (0, 8)
        lc.Lattice("A2").direct_sum(U),   # (3, 1)
        _direct_sum(U, U, E8.twist(-1)),  # (2, 10)
    ]
    for lattice in even_lattices:
        assert lattice.is_even()  # hypothesis of Milgram's theorem
        gauss_sum_invariant = lattice.discriminant_group().brown_invariant()
        assert gauss_sum_invariant % 8 == lattice.signature() % 8


def test_even_unimodular_lattices_and_the_k3_lattice_match_kondo():
    r"""Even unimodular lattices in the K3/Enriques setting [Kon20].

      - U is the even unimodular lattice of signature (1, 1) (Example 1.4).
      - Every even unimodular lattice L of signature (p, q) has p - q divisible by
        8 (Corollary 1.26).
      - The classification (Theorem 1.25): for p <= q an even unimodular lattice
        of signature (p, q) is U^{+p} + E_8(-1)^{+(q-p)/8}. So the K3 lattice
        H^2(X, Z), which has rank 22 and signature (3, 19), is U^3 + E_8(-1)^2 --
        even, unimodular, rank 22; and the Enriques-relevant E_10 = U + E_8(-1)
        is the even unimodular lattice of signature (1, 9).
    """
    U = lc.Lattice("U")
    E8m = lc.Lattice("E8").twist(-1)   # E_8(-1), negative definite (AG convention)

    # U: even unimodular of signature (1, 1)  [Kon20 Example 1.4]
    assert U.is_even() and U.is_unimodular()
    assert U.signature_pair() == (1, 1)

    # named even unimodular lattices, all satisfying p - q == 0 (mod 8)  [Kon20 Cor 1.26]
    e10 = U.direct_sum(E8m)                                   # signature (1, 9)
    k3 = _direct_sum(U, U, U, E8m, E8m)                       # signature (3, 19)
    e8_squared = lc.Lattice("E8").direct_sum(lc.Lattice("E8"))  # signature (16, 0)
    for L in [U, lc.Lattice("E8"), e10, k3, e8_squared]:
        assert L.is_even() and L.is_unimodular()
        p, q = L.signature_pair()
        assert (p - q) % 8 == 0

    # E_10 = U + E_8(-1): even unimodular, signature (1, 9), rank 10
    assert e10.signature_pair() == (1, 9) and e10.rank() == 10

    # the K3 lattice U^3 + E_8(-1)^2: even, unimodular, rank 22, signature (3, 19)
    assert k3.rank() == 22
    assert k3.signature_pair() == (3, 19)
    assert k3.is_even() and k3.is_unimodular()


def test_e8_is_the_even_unimodular_root_lattice_of_rank_8():
    r"""E_8 [CS99 sec 8.1]: the unique even unimodular lattice of rank 8 -- det 1,
    minimal norm 2, kissing number 240, and self-dual (E_8^* = E_8), so its
    discriminant group L^*/L is trivial. It is the rank-8 case of the even
    unimodular signature condition (Kon20 Cor 1.26: 8 - 0 = 8).
    """
    e8 = lc.Lattice("E8")
    assert e8.rank() == 8
    assert e8.determinant() == 1
    assert e8.is_even() and e8.is_unimodular()
    assert e8.minimum() == 2
    assert len(e8.roots()) == 240
    assert tuple(e8.discriminant_group().invariants()) == ()   # self-dual: no glue
