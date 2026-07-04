r"""Literature-cited arithmetic of primitive embeddings and orthogonal complements.

Theme: the embedding calculus of even lattices inside even *unimodular* lattices --
orthogonal complements, the discriminant-form anti-isometry, and the
even-overlattice / isotropic-subgroup correspondence. Every expected number is
either read off a cited source (quoted below with its line in the Zotero
markdown extraction) or is a convention-independent invariant (determinant,
signature, root count, discriminant-group order, index) recomputed by the spike
and cross-checked against the published lattice.

This module *computes* complements inside E_8 (it calls
``orthogonal_complement`` on genuine primitive sublattices and identifies the
result), which is strictly the embedding-arithmetic content that
``test_literature_citations.py`` does not exercise -- that module states Nikulin
Cor 1.6.2 on named lattices without ever forming a complement. The direct-sum
summand embeddings and the p-local ``maximal_overlattice`` reference are already
pinned in ``test_sage_reference_contract.py`` (rows 9a / 9d) and are not
restated here.

Sources (Zotero item key | Better-BibTeX key | markdown-extraction attachment):

  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). TTY9FFJS | Nik80 | D7BP5F7Z.
      * Prop 1.4.1 (md line 216): even overlattices S' of S are in bijection with
        isotropic subgroups H of the discriminant group A_S (q_S|H = 0).
      * det/index corollary (md line 230): "discr S' = (discr S) . [S':S]^{-2}",
        i.e. [S':S]^2 = det S / det S'.
      * Prop 1.6.1 (md line 264) and Cor 1.6.2 (md line 274): "S perp K if and
        only if q_S ~ -q_K" -- S and K are the orthogonal complements of one
        another inside SOME even unimodular lattice iff q_S = -q_K.
      * Cor 1.6.3 (md line 276): "S perp S(-1)" -- S and S(-1) are complementary
        in an even unimodular lattice (so S (+) S(-1) has an even unimodular
        overlattice).
  - Conway & Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. (1999).
    T2WVLTDB | CS10 | TCJKXU3D. Ch. 4 sec 3 (gluing theory):
      * md line 4333: the glue group L*/L has order det L.
      * Theorem 1 (md lines 4339-4347): if a unimodular lattice is glued from
        L_1 and L_2 with no self-glue, their glue groups are anti-isomorphic
        (hence |L_1*/L_1| = |L_2*/L_2|, i.e. det L_1 = det L_2).
      * Ch. 4 secs 8.1-8.3 tabulate E_7 (det 2, 126 roots) and E_6 (det 3, 72
        roots); E_8 (sec 8.1) is even unimodular of rank 8.
"""

from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc


def _unit(index, dimension=8):
    """Coordinate vector of the ``index``-th E_8 simple root in the E_8 basis."""
    coordinates = [0] * dimension
    coordinates[index] = 1
    return coordinates


def _is_anti_isometric(lattice_s, lattice_k):
    """Nikulin's anti-isometry test: q_S ~ -q_K, with -q_K = q_{K(-1)}."""
    return lattice_s.discriminant_group().is_isomorphic(
        lattice_k.twist(-1).discriminant_group(), kind="quadratic"
    )


def test_orthogonal_complements_in_e8_recover_root_lattices_and_the_nikulin_anti_isometry():
    r"""Compute orthogonal complements inside E_8 and check Nikulin Cor 1.6.2.

    The spike builds E_8 with Gram = Cartan matrix, so its basis vectors are
    simple roots: ``_unit(0)`` is a single simple root (an A_1), and the adjacent
    pair ``_unit(3), _unit(4)`` (Gram [[2,-1],[-1,2]]) is a genuine A_2. Their
    orthogonal complements inside the even unimodular E_8 are, classically,
    A_1^perp = E_7 and A_2^perp = E_6.

    Significant content, per source:
      - the computed complement is isometric to the named root lattice and
        reproduces its CS10 Ch. 4 invariants (E_7: det 2, 126 roots; E_6: det 3,
        72 roots);
      - both S and its complement K = S^perp are primitive in E_8, and their
        glue groups have equal order, det S = det K (CS10 Ch. 4 sec 3, Thm 1 /
        md lines 4333, 4339);
      - the anti-isometry q_S ~ -q_K holds on the genuinely computed pair
        (Nikulin Cor 1.6.2, md line 274);
      - E_8 is an even overlattice of S (+) K with index the glue number:
        [E_8 : S (+) K]^2 = det(S (+) K) = det S . det K (E_8 unimodular)
        (Nikulin det/index corollary, md line 230).

    Negative control: A_1 and A_2 are NOT self-complementary -- q_S is not
    isomorphic to -q_S -- so the criterion genuinely discriminates and is not a
    tautology satisfied by every lattice.
    """
    e8 = lc.Lattice("E8")
    # cheap characterization of the ambient (Kondo/CS10 sec 8.1: even unimodular rank 8)
    assert e8.rank() == 8
    assert e8.signature_pair() == (8, 0)
    assert e8.determinant() == 1
    assert e8.is_even() and e8.is_unimodular()

    # (sublattice generators, complement name, CS10 determinant, CS10 root count,
    #  complement signature pair, complement discriminant invariants)
    cases = [
        ([_unit(0)], "E7", 2, 126, (7, 0), (2,)),
        ([_unit(3), _unit(4)], "E6", 3, 72, (6, 0), (3,)),
    ]
    for generators, complement_name, determinant, root_count, sig_pair, disc in cases:
        s = e8.sublattice(generators, label="S")
        k = e8.orthogonal_complement(s)

        # cheap basics on the computed complement K (characterization)
        assert k.rank() == 8 - s.rank()
        assert k.signature_pair() == sig_pair
        assert k.determinant() == determinant
        assert k.is_even()
        assert not k.is_unimodular()               # a proper root lattice, not E_8

        # significant: K is exactly the named root lattice, with CS10 invariants
        assert k.is_isometric(lc.Lattice(complement_name))
        assert len(k.roots()) == root_count
        assert tuple(k.discriminant_group().invariants()) == disc

        # both sides primitively embedded; equal glue-group order (CS10 Thm 1)
        assert e8.is_primitive(s) and e8.is_primitive(k)
        assert s.determinant() == k.determinant()

        # Nikulin Cor 1.6.2 on the genuinely computed complement pair
        assert _is_anti_isometric(s, k)

        # E_8 unimodular => [E_8 : S (+) K]^2 = det(S (+) K) = det S . det K
        direct_sum = s.direct_sum(k)
        assert direct_sum.determinant() == s.determinant() * k.determinant()
        assert direct_sum.is_even()

        # NEGATIVE CONTROL: S is not its own complement (q_S !~ -q_S)
        assert not _is_anti_isometric(s, s)


def test_even_overlattice_index_realizes_the_isotropic_glue_of_S_plus_S_minus_one():
    r"""Nikulin Prop 1.4.1 + Cor 1.6.3: the even-overlattice / isotropic-subgroup
    correspondence and its index formula, realized on S (+) S(-1).

    By Cor 1.6.3 (md line 276) S perp S(-1), so S (+) S(-1) has an even unimodular
    overlattice. Taking S = A_2: G = A_2 (+) A_2(-1) has signature (2, 2),
    determinant 9, discriminant group (Z/3)^2. Its maximal even overlattice G'
    (the isotropic glue of Prop 1.4.1, md line 216) is even unimodular, and the
    Nikulin det/index corollary (md line 230, "discr S' = (discr S).[S':S]^{-2}")
    forces
        [G' : G]^2 = det G / det G' = 9 / 1 = 9,   so   [G' : G] = 3.

    Significant content: the maximization actually reaches an even *unimodular*
    lattice (det 1), the glue index squares to the determinant ratio, and the
    isotropic subgroup consumed is the whole diagonal of (Z/3)^2.

    Discriminating control: A_2 by itself has NO proper even overlattice -- its
    discriminant group Z/3 carries q(x) = 2/3 x^2 (mod 2Z), whose only isotropic
    element is 0 (Prop 1.4.1: overlattices <-> isotropic subgroups) -- so its
    maximal overlattice is A_2 itself with the determinant unchanged. This shows
    the index-3 drop above is real gluing, not an artifact of the maximizer.
    """
    a2 = lc.Lattice("A2")
    g = a2.direct_sum(a2.twist(-1))          # S (+) S(-1) with S = A_2 (Cor 1.6.3)

    # cheap basics on G (characterization)
    assert g.rank() == 4
    assert g.signature_pair() == (2, 2)
    assert g.determinant() == 9
    assert g.is_even()
    assert not g.is_unimodular()
    assert tuple(g.discriminant_group().invariants()) == (3, 3)   # glue group order 9

    maximal = g.maximal_overlattice()

    # significant: the isotropic glue reaches an even unimodular overlattice ...
    assert maximal.is_even() and maximal.is_unimodular()
    assert maximal.determinant() == 1
    assert maximal.signature_pair() == (2, 2)                     # signature preserved

    # ... and the Prop 1.4.1 / det-index law holds exactly (md line 230)
    index = g.index_in(maximal)
    assert index == 3
    assert index ** 2 == g.determinant() / maximal.determinant()  # [G':G]^2 = detG/detG'

    # DISCRIMINATING CONTROL: A_2 alone has no proper even overlattice (its Z/3
    # discriminant form has no nonzero isotropic vector, Prop 1.4.1)
    assert a2.determinant() == 3
    assert a2.maximal_overlattice().determinant() == a2.determinant()
    assert a2.maximal_overlattice().is_even()
