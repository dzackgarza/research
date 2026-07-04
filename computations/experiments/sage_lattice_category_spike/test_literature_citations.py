r"""Literature-cited computations the spike reproduces.

Every expected value here is taken verbatim from an authoritative source held in
the project Zotero library, NOT from the spike's own backing and NOT from memory.
A green test therefore proves the spike computes the *published* value; the Sage
backing is the reference implementation, and the literature is the independent
oracle it is checked against.

Sources (Zotero item key | Better-BibTeX key | markdown-extraction attachment key):

  - Conway & Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. (1999).
    Zotero T2WVLTDB | CS99 | extraction TCJKXU3D. Chapter 4 tabulates the root
    lattices A_n, D_n, E_6, E_7, E_8 with their determinants, minimal norms,
    kissing numbers (numbers of minimal vectors) and glue groups; Chapter 2 sec 2.4
    records that the glue group L^*/L has order det L.
  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). Zotero TTY9FFJS | Nik80 | extraction D7BP5F7Z.
    Theorem 1.3.3* is the signature-(mod 8) / Milgram relation for even lattices.

Written in the spike's public language: ``lc.Lattice(name)`` builds a root
lattice; a lattice answers ``determinant``/``minimum``/``roots``/``signature``;
``discriminant_group`` returns the finite quadratic form q_L, which answers
``invariants`` (its invariant factors) and ``brown_invariant`` (sign q_L mod 8).
"""

from __future__ import annotations

from math import prod

import sage_lattice_category_spike.lattice_categories as lc


def test_root_lattice_invariants_match_conway_sloane_chapter_4():
    r"""Determinant, minimal norm, and number of roots of the irreducible root
    lattices, pinned to Conway & Sloane, *SPLAG* Chapter 4 [CS99, Zotero
    T2WVLTDB]. For a root lattice the minimal vectors ARE the roots (minimal norm
    is 2), so the kissing number tau equals the number of roots:

      - A_n (sec 6.1): det = n+1, min norm 2, tau = n(n+1);
      - D_4 (sec 7.1): det = 4,   min norm 2, tau = 24;
      - E_6 (sec 8.3): det = 3,   min norm 2, tau = 72;
      - E_7 (sec 8.2): det = 2,   min norm 2, tau = 126;
      - E_8 (sec 8.1): det = 1,   min norm 2, tau = 240.
    """
    # (spike name, CS99 determinant, CS99 kissing number tau = #roots)
    cs99_chapter_4 = {
        "A1": (2, 2),    # A_n sec 6.1 with n = 1: det n+1 = 2, tau n(n+1) = 2
        "A2": (3, 6),    #                  n = 2: det 3,        tau 6
        "A3": (4, 12),   #                  n = 3: det 4,        tau 12
        "D4": (4, 24),   # D_n sec 7.1 with n = 4: det 4,        tau 2n(n-1) = 24
        "E6": (3, 72),   # E_6 sec 8.3: det 3, tau 72
        "E7": (2, 126),  # E_7 sec 8.2: det 2, tau 126
        "E8": (1, 240),  # E_8 sec 8.1: det 1, tau 240
    }
    for name, (determinant, kissing_number) in cs99_chapter_4.items():
        lattice = lc.Lattice(name)
        assert lattice.determinant() == determinant, name
        assert lattice.minimum() == 2, name
        assert len(lattice.roots()) == kissing_number, name


def test_root_lattice_discriminant_groups_are_the_conway_sloane_glue_groups():
    r"""The discriminant group L^*/L of a root lattice is the Conway-Sloane glue
    group. Its order equals det L [CS99 sec 2.4], and its invariant-factor
    structure is tabulated in [CS99 Chapter 4]:

      - A_n: cyclic C_{n+1}            (sec 6.1, "Glue group: cyclic C_{n+1}");
      - D_4: Klein four V_4 = (C_2)^2  (sec 7.1, "Glue group: Klein V_4 if n even");
      - E_6: C_3                       (sec 8.3; order = det = 3 forces cyclic);
      - E_7: C_2                       (sec 8.2, "Glue group C_2");
      - E_8: trivial                   (sec 8.1, "E_8^* = E_8, so there is no glue").
    """
    # (spike name, CS99 glue-group invariant factors)
    cs99_glue_groups = {
        "A1": (2,), "A2": (3,), "A3": (4,),   # cyclic C_{n+1}
        "D4": (2, 2),                          # Klein V_4
        "E6": (3,), "E7": (2,), "E8": (),      # C_3, C_2, trivial
    }
    for name, invariant_factors in cs99_glue_groups.items():
        lattice = lc.Lattice(name)
        discriminant_group = lattice.discriminant_group()
        assert tuple(discriminant_group.invariants()) == invariant_factors, name
        # |L^*/L| = det L  (CS99 sec 2.4); root lattices are positive definite so det > 0.
        assert prod(invariant_factors) == lattice.determinant(), name


def test_milgram_signature_mod_8_matches_nikulin_theorem_1_3_3():
    r"""Nikulin, Theorem 1.3.3* [Nik80, Zotero TTY9FFJS]: for an even lattice S of
    signature (t_+, t_-),

        t_+ - t_-  ==  sign(q_S)   (mod 8),

    where q_S is the discriminant quadratic form and sign(q_S) is its Brown
    invariant. ``L.signature()`` is t_+ - t_-, and ``q.brown_invariant()`` is
    sign(q_S). Checked across positive-definite, negative-definite, and indefinite
    even lattices, so the congruence is not an artifact of a single signature
    regime: A2 (2,0); E7 (7,0); E8 (8,0, q trivial); U (1,1, q trivial);
    A2(-1) (0,2); E8(-1) (0,8); A2 + U (3,1).
    """
    hyperbolic_plane = lc.Lattice("U")
    even_lattices = [
        lc.Lattice("A2"),
        lc.Lattice("E7"),
        lc.Lattice("E8"),
        hyperbolic_plane,
        lc.Lattice("A2").twist(-1),
        lc.Lattice("E8").twist(-1),
        lc.Lattice("A2").direct_sum(hyperbolic_plane),
    ]
    for lattice in even_lattices:
        assert lattice.is_even()  # hypothesis of Theorem 1.3.3*
        discriminant_form = lattice.discriminant_group()
        assert discriminant_form.brown_invariant() % 8 == lattice.signature() % 8
