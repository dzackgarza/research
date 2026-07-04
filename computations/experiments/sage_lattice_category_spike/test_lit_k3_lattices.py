r"""K3/Enriques lattice theory the spike reproduces, checked against the literature.

Every expected value below is BOTH pinned to an authoritative source in the
project Zotero library AND verified against the spike as the reference
implementation (the literature is the independent oracle). Cheap linear-algebra
data (rank / signature_pair / determinant / is_even / is_unimodular) is asserted
throughout as *characterization*, but is never the content of a test on its own:
"L_K3 is even unimodular of signature (3, 19)" is linear algebra, so each test
carries it alongside genuinely arithmetic K3-lattice facts -- discriminant-form
anti-isometries of orthogonal complements, primitive embeddings into the K3
lattice, transcendental/Neron-Severi splitting of a polarized K3, and isometry
decisions that see the whole genus.

Sources (Zotero item key | markdown-extraction attachment | cited location):

  - S. Kondo, *K3 Surfaces* (EMS, 2020). F288JVXK.
      * Example 1.4: U is the even unimodular lattice of signature (1, 1).
      * Corollary 1.26: an even unimodular lattice of signature (p, q) has
        p - q divisible by 8.
      * Theorem 1.27: the indefinite even unimodular lattice of signature (p, q)
        is unique; for p <= q it is U^p (+) E8(-1)^{(q-p)/8} (AG sign
        convention). So H^2(K3) = U^3 (+) E8(-1)^2 (rank 22, sig (3, 19)) and
        the Enriques-relevant E10 = U (+) E8(-1) (sig (1, 9)) are each the unique
        even unimodular lattice of their signature.
      * Definition 6.4: a polarized K3 (X, H) has H primitive in NS(X) and
        H^2 = 2d the degree of polarization.
      * p. (period section, around the L_{2d} definition): for a primitive
        h in L with h^2 = 2d, the orthogonal complement L_{2d} = h^perp has
        signature (2, 19), independent of h (Lemma 1.45).
      * Ch. 8 (action on the transcendental lattice): for a projective K3 with
        rank(NS) = r, sig(NS) = (1, r-1) and sig(T) = (2, 20-r); r = 1 gives the
        general degree-2d transcendental lattice of signature (2, 19).
      * Introduction: an Enriques surface has Picard number 10, and a K3 surface
        is its universal double cover; the Enriques period theory fixes a
        rank-10 sublattice of H^2(K3, Z) (vs. the rank-1 ZH of the polarized
        case).
  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). TTY9FFJS / D7BP5F7Z.
      * 6 (orthogonality of lattices): S _|_ K means S embeds primitively into
        some even unimodular lattice with orthogonal complement K.
      * Corollary 1.6.2: S _|_ K if and only if q_S ~ -q_K (isomorphic finite
        quadratic forms). Corollary 1.6.3: S _|_ S(-1).
  - I. Dolgachev, *Enriques Surfaces II* (2024). 7RZTF9AQ.
      * Section 1.5 / 9.2: the Enriques lattice E10 = U (+) E8(-1), the rank-10
        even unimodular hyperbolic lattice of an Enriques surface.

Written in the spike's public language: ``lc.Lattice(name)`` / ``lc.Lattice(matrix)``
build named or Gram-given lattices; ``L.twist(-1)``, ``L.direct_sum(M)``,
``L.sublattice(gens)``, ``L.orthogonal_complement(S)``, ``L.is_isometric(M)``,
``L.is_primitive(S)``; ``L.discriminant_group()`` returns the finite quadratic
form q_L, which answers ``invariants`` and ``is_isomorphic(other, kind="quadratic")``.
"""

from __future__ import annotations

from functools import reduce

import sage_lattice_category_spike.lattice_categories as lc
from sage.all import ZZ, matrix


def _direct_sum(*lattices):
    return reduce(lambda a, b: a.direct_sum(b), lattices)


def _U():
    return lc.Lattice("U")


def _E8m():
    # E_8(-1): negative definite, the K3/AG sign convention [Kon20 Thm 1.27]
    return lc.Lattice("E8").twist(-1)


def _rank_one(n):
    # the rank-1 lattice with Gram [n]
    return lc.Lattice(matrix(ZZ, 1, [n]))


def _k3_lattice():
    # L_K3 = H^2(K3, Z) = U^3 (+) E8(-1)^2  [Kon20 Thm 1.27]
    return _direct_sum(_U(), _U(), _U(), _E8m(), _E8m())


def _anti_isometric(s, k):
    r"""Nikulin Cor 1.6.2 predicate: q_S ~ -q_K, tested as
    q_S ~ q_{K(-1)} on finite quadratic forms."""
    return s.discriminant_group().is_isomorphic(
        k.twist(-1).discriminant_group(), kind="quadratic"
    )


def test_k3_lattice_is_even_unimodular_and_isometry_ignores_summand_order():
    r"""The K3 lattice H^2(X, Z) = U^3 (+) E8(-1)^2 [Kon20 Thm 1.27], and the
    fact that its isometry class does not depend on how the orthogonal summands
    are ordered.

    Cheap characterization (linear algebra): rank 22, signature (3, 19), even,
    unimodular, det -1 [Kon20 Cor 1.26: 3 - 19 = -16 is divisible by 8].

    Significant content (arithmetic): ``is_isometric`` decides equality of the
    whole genus, so three genuinely different block orderings of U^3 (+) E8(-1)^2
    -- and the regrouping (U (+) E8(-1)) twice plus U -- are all isometric,
    witnessing the uniqueness half of Theorem 1.27 rather than merely matching
    invariants.
    """
    k3 = _k3_lattice()
    # cheap characterization, kept but never the whole story
    assert k3.rank() == 22
    assert k3.signature_pair() == (3, 19)
    assert k3.is_even() and k3.is_unimodular()
    assert k3.determinant() == -1

    reordered = _direct_sum(_E8m(), _E8m(), _U(), _U(), _U())
    interleaved = _direct_sum(_U(), _E8m(), _U(), _E8m(), _U())
    regrouped = _direct_sum(
        _U().direct_sum(_E8m()), _U().direct_sum(_E8m()), _U()
    )  # (E10) (+) (E10) (+) U
    for other in (reordered, interleaved, regrouped):
        assert other.rank() == 22 and other.signature_pair() == (3, 19)
        assert other.is_even() and other.is_unimodular()
        assert k3.is_isometric(other)


def test_degree_two_polarization_neron_severi_transcendental_anti_isometry():
    r"""Transcendental / Neron-Severi splitting of a degree-2 (d = 1) polarized
    K3 [Kon20 Def 6.4, Ch. 8, period section; Nik80 Cor 1.6.2].

    A general degree-2d K3 has Neron-Severi lattice ZH = <2d> (rank 1, Gram
    [2d]) primitive in L_K3, and transcendental lattice T = H^perp. For d = 1
    the abstract transcendental lattice is T = U^2 (+) E8(-1)^2 (+) <-2>, of rank
    21 and signature (2, 19) [Kon20: sig(T) = (2, 20 - r) with r = 1]. Because
    <2> and T are orthogonal complements inside the even unimodular L_K3,
    Nikulin's Corollary 1.6.2 forces q_T ~ -q_{<2>} (both finite quadratic forms
    on Z/2).

    Cheap characterization: rank/signature/parity/determinant of L_K3, <2>, and
    T. Significant content: the anti-isometry checked both abstractly and on the
    genuine in-lattice orthogonal complement of a primitively embedded degree-2
    class, the isometry of that concrete complement with the abstract T, and the
    index-2 direct-sum bookkeeping (rank and signature add up to L_K3, but
    <2> (+) T has determinant 4 -- it sits in L_K3 with index 2, it is not a
    direct summand).
    """
    k3 = _k3_lattice()
    ns = _rank_one(2)                                   # <2> = ZH, H^2 = 2
    transcendental = _direct_sum(_U(), _U(), _E8m(), _E8m(), _rank_one(-2))

    # cheap characterization of the three abstract lattices
    assert (k3.rank(), k3.signature_pair(), k3.is_unimodular()) == (22, (3, 19), True)
    assert (ns.rank(), ns.signature_pair(), ns.is_even(), ns.determinant()) == (1, (1, 0), True, 2)
    assert transcendental.rank() == 21
    assert transcendental.signature_pair() == (2, 19)          # [Kon20 sig(T)=(2,20-r), r=1]
    assert transcendental.is_even() and transcendental.determinant() == -2

    # abstract anti-isometry q_T ~ -q_{<2>}  [Nik80 Cor 1.6.2]
    assert tuple(transcendental.discriminant_group().invariants()) == (2,)
    assert tuple(ns.discriminant_group().invariants()) == (2,)
    assert _anti_isometric(transcendental, ns)

    # genuine primitive embedding of <2> in L_K3: v = e + f in the first U, v^2 = 2
    embedded = k3.sublattice([[1, 1] + [0] * 20], label="NS<2>")
    assert embedded.gram_matrix().list() == [2] and k3.is_primitive(embedded)
    complement = k3.orthogonal_complement(embedded)
    assert complement.rank() == 21 and complement.signature_pair() == (2, 19)
    assert complement.is_even() and complement.determinant() == -2
    assert _anti_isometric(complement, embedded)                # q_{H^perp} ~ -q_{<2>}
    assert complement.is_isometric(transcendental)             # H^perp ~ abstract T

    # rank/signature bookkeeping: <2> (+) T has the numerics of L_K3 but is the
    # index-2 sublattice, not a summand (det 4, not unimodular)
    glued = ns.direct_sum(transcendental)
    assert glued.rank() == k3.rank()
    assert glued.signature_pair() == k3.signature_pair()
    assert glued.is_even() and not glued.is_unimodular()
    assert glued.determinant() == -4                            # 2 * |det T|, index-2 glue


def test_degree_four_polarization_transcendental_has_order_four_discriminant():
    r"""Degree-4 (d = 2) polarized K3: the transcendental lattice carries a
    Z/4 discriminant form, distinguishing it from the degree-2 case
    [Kon20 Def 6.4, period section; Nik80 Cor 1.6.2].

    NS = <4> primitively embeds in L_K3 (via h = 2e + f in a hyperbolic plane,
    h^2 = 4); its orthogonal complement T_4 = h^perp has signature (2, 19) and
    discriminant group Z/4, and q_{T_4} ~ -q_{<4>}. The Z/4 vs Z/2 discriminant
    groups certify that the two polarization degrees give non-isomorphic
    transcendental discriminant forms -- content the shared signature (2, 19)
    cannot see.
    """
    k3 = _k3_lattice()
    ns4 = _rank_one(4)
    assert (ns4.rank(), ns4.signature_pair(), ns4.determinant()) == (1, (1, 0), 4)
    assert tuple(ns4.discriminant_group().invariants()) == (4,)

    embedded = k3.sublattice([[2, 1] + [0] * 20], label="NS<4>")
    assert embedded.gram_matrix().list() == [4] and k3.is_primitive(embedded)
    t4 = k3.orthogonal_complement(embedded)
    assert t4.rank() == 21 and t4.signature_pair() == (2, 19)
    assert t4.is_even() and t4.determinant() == -4
    assert tuple(t4.discriminant_group().invariants()) == (4,)
    assert _anti_isometric(t4, ns4)                             # q_{T_4} ~ -q_{<4>}

    # degree-4 transcendental disc form (Z/4) differs from degree-2 (Z/2)
    t2 = k3.orthogonal_complement(k3.sublattice([[1, 1] + [0] * 20]))
    assert not t4.discriminant_group().is_isomorphic(
        t2.discriminant_group(), kind="quadratic"
    )


def test_minus_two_root_class_primitively_embedded_in_k3_and_its_complement():
    r"""A (-2)-class (root) primitively embedded in the K3 lattice and its
    orthogonal complement [Nik80 Cor 1.6.2, 1.6.3].

    On a K3 the effective roots have square -2, so the rank-1 root lattice
    A_1(-1) = <-2> (the class r = e - f, r^2 = -2) embeds primitively in L_K3.
    Its orthogonal complement has signature (3, 18) (removing a negative-definite
    line) and determinant 2, and Nikulin's Corollary 1.6.2 gives the
    anti-isometry q_{r^perp} ~ -q_{<-2>} on Z/2. This is the primitive-embedding
    / complement pattern realized inside the K3 lattice itself, distinct from the
    E8-internal complements pinned elsewhere.
    """
    k3 = _k3_lattice()
    root = k3.sublattice([[1, -1] + [0] * 20], label="root<-2>")
    assert root.gram_matrix().list() == [-2]                    # A_1(-1)
    assert root.signature_pair() == (0, 1) and k3.is_primitive(root)

    complement = k3.orthogonal_complement(root)
    assert complement.rank() == 21
    assert complement.signature_pair() == (3, 18)               # (3, 19) - (0, 1)
    assert complement.is_even() and complement.determinant() == 2
    assert tuple(complement.discriminant_group().invariants()) == (2,)
    assert _anti_isometric(complement, root)                    # q_{r^perp} ~ -q_{<-2>}


def test_enriques_lattice_e10_is_a_unimodular_summand_of_the_k3_lattice():
    r"""The Enriques lattice E10 = U (+) E8(-1) and its relation to the K3
    lattice [Kon20 Cor 1.26, Thm 1.27, introduction; Dol24 E10; Nik80 Cor 1.6.2].

    E10 is the even unimodular lattice of signature (1, 9): rank 10 = the Picard
    number of an Enriques surface, whose universal double cover is a K3 surface.
    The Enriques period theory fixes a rank-10 sublattice of H^2(K3, Z), and
    since E10 is unimodular it splits off as an orthogonal summand:
    L_K3 = U^3 (+) E8(-1)^2 ~ E10 (+) (U^2 (+) E8(-1)). The isometry
    L_K3 ~ E10 (+) E10^perp is decided over the whole genus (not just matching
    signatures), and the anti-isometry q_{E10} ~ -q_{E10^perp} is the unimodular
    (both trivial) instance of Nikulin's Corollary 1.6.2.

    Cheap characterization: rank/signature/parity/unimodularity/determinant of
    E10. Significant content: the genus-level isometry witnessing E10 as a
    primitive unimodular rank-10 summand of L_K3, and the trivial-form
    anti-isometry of the complementary summand.
    """
    e10 = _U().direct_sum(_E8m())
    # cheap characterization [Kon20 Cor 1.26: 1 - 9 = -8 divisible by 8]
    assert e10.rank() == 10
    assert e10.signature_pair() == (1, 9)
    assert e10.is_even() and e10.is_unimodular()
    assert e10.determinant() == -1

    k3 = _k3_lattice()
    e10_perp = _direct_sum(_U(), _U(), _E8m())                  # U^2 (+) E8(-1)
    assert e10_perp.rank() == 12 and e10_perp.signature_pair() == (2, 10)
    assert e10_perp.is_even() and e10_perp.is_unimodular()

    # E10 is a primitive unimodular rank-10 summand of the K3 lattice
    assert e10.direct_sum(e10_perp).is_isometric(k3)
    # unimodular case of Nikulin Cor 1.6.2: both discriminant forms trivial
    assert tuple(e10.discriminant_group().invariants()) == ()
    assert tuple(e10_perp.discriminant_group().invariants()) == ()
    assert _anti_isometric(e10, e10_perp)
