r"""Literature-cited computations for the finite discriminant quadratic form q_L.

For an even lattice L, the discriminant form is the finite quadratic form
q_L : A_L = L^*/L -> Q/2Z,  q_L(t + L) = t.t + 2Z   (Nik80 D7BP5F7Z .md:176-182).
This module pins the *finite-form* structure that the sibling
``test_literature_citations.py`` does not: the Gauss-Milgram / Brown invariant
of the Miranda-Morrison elementary 2-adic forms u_k, v_k; the p-primary
splitting q = (+)_p q_p; the quadratic vs bilinear vs group refinement of
finite-form isomorphism; form negation -q via twist(-1); and the bijection
between isotropic subgroups and even overlattices.

Only convention-independent finite-form data is pinned (Brown invariants,
isomorphism classes, primary structure, isotropic/overlattice glue); raw q(x)
values carry a sign/normalization convention and are deliberately not asserted.
Every expected value is either read off the running spike (the oracle) or taken
from a Zotero-held source and quoted with file+line; each was confirmed against
the oracle before being pinned. Sources (Zotero attachment markdown):

  - V. V. Nikulin, *Integral symmetric bilinear forms and some of their
    applications* (1980). Zotero TTY9FFJS, attachment D7BP5F7Z. Cited by line of
    ".../D7BP5F7Z/[Nikulin 1980] INTEGRAL SYMMETRIC BILINEAR FORMS ...md".
  - R. Miranda & D. Morrison, *Embeddings of integral quadratic forms* (2009).
    Zotero ACX7WF7L. Cited by line of
    ".../ACX7WF7L/[Miranda 2009] Embeddings of integral quadratic forms.md".
  - J. H. Conway & N. J. A. Sloane, *SPLAG*, 3rd ed. (1999). Zotero T2WVLTDB,
    attachment TCJKXU3D. Cited by line of the Ch. 15 markdown.

IMPORTANT (rule 4): the Brown invariant Br(q) in Z/8 is *defined* as the argument
of the normalized Gauss sum of the finite form q, gamma_q(1) = exp(pi*i*Br/4)
(MM09 ACX7WF7L .md:2584 Thm 5.1: gamma_L(1) = exp(pi*i*s/4)). It is a property of
the finite form alone. That Br(q_L) equals the lattice signature mod 8 is
*Milgram's theorem*, exactly Nik80 D7BP5F7Z .md:204-208 Thm 1.3.3*
(t_+ - t_- == sign q_S (mod 8)); the Milgram congruence is therefore checked as a
theorem, never used as the definition of Br.
"""

from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc
from sage.all import ZZ, matrix


def _U(scale):
    r"""U(2^k): the even lattice with Gram [[0, 2^k],[2^k, 0]]. This is exactly the
    Miranda-Morrison module U_k (MM09 ACX7WF7L .md:562: "matrix ((0,2^k),(2^k,0))
    ... denoted by U_k"), whose discriminant form is the elementary 2-adic form u_k.
    """
    return lc.Lattice(matrix(ZZ, 2, [0, scale, scale, 0]))


def test_elementary_2adic_forms_u_and_v_gauss_milgram_signature():
    r"""Brown/Gauss-sum invariant of the Miranda-Morrison elementary 2-adic forms.

    u_k is the discriminant form of U_k = [[0,2^k],[2^k,0]] (MM09 .md:562); v_1 is
    the anisotropic type realized here by D_4 (MM09 .md:564 defines V_k by
    Q = 2^k(a1^2+a1a2+a2^2); q_{D4} is the exponent-2 anisotropic even form).

    Gauss-sum values (finite-form facts, no lattice signature used):
      - gamma_{u_k}(1) = 1              (MM09 .md:2461 Prop 2.7)  => Br(u_k) == 0,
      - gamma_{v_k}(1) = (-1)^k         (MM09 .md:2461 Prop 2.7)  => Br(v_1) == 4,
    via gamma_q(1) = exp(pi*i*Br/4) (MM09 .md:2584 Thm 5.1). Independently Nikulin
    tabulates the same signatures (D7BP5F7Z .md:655):
      sign u_+^(2)(2^k) == 0 (mod 8),  sign v_+^(2)(2^k) == 4k (mod 8).

    Anisotropy is the Miranda-Morrison dichotomy: U_k carries a nonzero isotropic
    vector (MM09 .md:576 (7.7.1)), V_k has none (MM09 .md:578 (7.7.2)); so
    is_anisotropic is False on every u_k and True on v_1.

    Milgram's THEOREM (Nik80 .md:204-208 Thm 1.3.3*) is then cross-checked:
    Br(q_L) == signature(L) (mod 8) -- U(2^k) has signature (1,1) -> 0, D4 -> 4.
    """
    # u_k = q_{U(2^k)}, k = 1,2,3 : Br == 0, anisotropic False. (is_metabolic on
    # U(8) enumerates 2^6 subgroups and costs ~90s, so it is not exercised here.)
    for k in (1, 2, 3):
        L = _U(2 ** k)
        q = L.discriminant_group()
        # cheap basics of the underlying lattice, as characterization
        assert L.rank() == 2
        assert L.is_even()
        assert not L.is_unimodular()
        assert L.signature_pair() == (1, 1)
        assert L.determinant() == -(4 ** k)          # disc(U_k) = -2^{2k}, MM09 .md:566
        # finite-form content
        assert tuple(q.invariants()) == (2 ** k, 2 ** k)
        assert q.cardinality() == 4 ** k
        assert q.brown_invariant() == 0              # gamma_{u_k}=1 => Br 0
        assert q.is_anisotropic() is False           # MM09 (7.7.1): U_k has isotropic vector
        assert q.brown_invariant() % 8 == L.signature() % 8   # Milgram, Thm 1.3.3*

    # v_1 = q_{D4} : Br == 4, anisotropic True.
    D4 = lc.Lattice("D4")
    q = D4.discriminant_group()
    assert D4.rank() == 4
    assert D4.is_even()
    assert not D4.is_unimodular()
    assert D4.signature_pair() == (4, 0)
    assert D4.determinant() == 4
    assert tuple(q.invariants()) == (2, 2)
    assert q.cardinality() == 4
    assert q.brown_invariant() == 4                  # gamma_{v_1}=(-1)^1 => Br 4
    assert q.is_anisotropic() is True                # MM09 (7.7.2): V_k anisotropic
    assert q.brown_invariant() % 8 == D4.signature() % 8   # Milgram, Thm 1.3.3*


def test_signature_mod8_is_a_homomorphism_over_primary_parts():
    r"""q = (+)_p q_p and Br is additive over the primary parts.

    Nik80 D7BP5F7Z .md:156 Prop 1.2.2: q = (+)_p q_p is an orthogonal splitting of
    the finite form over the p-primary parts A_p of A_L. Nik80 .md:204-208 Thm
    1.3.3* makes "signature (mod 8)" a homomorphism on the semigroup qu(Z), so it
    is additive over that splitting; the same 2-adic component is the *oddity* in
    Conway-Sloane's language (CS10 TCJKXU3D .md:11902: "The 2-signature ... is also
    called the oddity", a p-adic invariant defined mod 8).

    A_5 has A_L = Z/6 = Z/2 (+) Z/3, so the split, the per-block Brown invariants,
    and the additive congruence Br(q) == Br(q_2) + Br(q_3) (mod 8) are all
    exercised on a genuinely non-prime-power group. Per-block values (7 on the
    2-part, 6 on the 3-part) are oracle-read; their sum-mod-8 identity and the
    Milgram identity Br(q) == sign(A_5) (mod 8) are the cited theorems.
    """
    A5 = lc.Lattice("A5")
    q = A5.discriminant_group()
    # cheap basics
    assert A5.rank() == 5
    assert A5.is_even()
    assert not A5.is_unimodular()
    assert A5.signature_pair() == (5, 0)
    assert A5.determinant() == 6
    assert tuple(q.invariants()) == (6,)

    # primary splitting matches the prime factorization of |A_L| = 6  (Prop 1.2.2)
    parts = {p: q.primary_part(p) for p in (2, 3)}
    assert tuple(q_p.cardinality() for q_p in (parts[2], parts[3])) == (2, 3)
    assert sorted(tuple(P.invariants()) for P in q.primary_decomposition()) == [(2,), (3,)]

    # per-block Brown invariants (oracle-read), consistent with primary_part
    br2, br3 = parts[2].brown_invariant(), parts[3].brown_invariant()
    assert (br2, br3) == (7, 6)
    per_block = {p: br for (p, _gram, br) in q.brown_invariant_per_block()}
    assert per_block == {2: 7, 3: 6}

    # signature (mod 8) is additive over the primary parts (Thm 1.3.3* homomorphism)
    assert q.brown_invariant() % 8 == (br2 + br3) % 8
    # ... and equals the lattice signature mod 8 (Milgram, Thm 1.3.3*)
    assert q.brown_invariant() % 8 == A5.signature() % 8


def test_quadratic_isomorphism_refines_bilinear_and_group_isomorphism():
    r"""u_1 and v_1 share group and bilinear form but are distinct quadratic forms.

    q_{U(2)} = u_1 and q_{D4} = v_1 both live on (Z/2)^2, so they are isomorphic as
    groups. Their *bilinear* forms are isomorphic too: Nik80 D7BP5F7Z .md:673 Prop
    1.8.2 gives u_-^(2)(2) ~= v_-^(2)(2) (the bilinear forms of u_1 and v_1). Yet
    they are NOT isomorphic as quadratic forms:
      - Nik80 .md:659 Thm 1.11.3: two finite quadratic forms with isomorphic
        bilinear forms are isomorphic iff sign_1 == sign_2 (mod 8); here Br differs
        (0 vs 4);
      - MM09 ACX7WF7L .md:566 / .md:580 (7.7.3): disc(U_k)=-2^{2k} with (2/-1)=+1
        while disc(V_k)=3*2^{2k} with (2/3)=-1, so U_k !~= V_k, hence u_1 !~= v_1.

    This exercises is_isomorphic across kind="group"/"bilinear"/"quadratic",
    demonstrating that the quadratic refinement is strictly finer.
    """
    U2, D4 = _U(2), lc.Lattice("D4")
    qu, qv = U2.discriminant_group(), D4.discriminant_group()
    # cheap basics of both underlying lattices
    assert U2.is_even() and not U2.is_unimodular() and U2.signature_pair() == (1, 1)
    assert D4.is_even() and not D4.is_unimodular() and D4.signature_pair() == (4, 0)
    assert tuple(qu.invariants()) == (2, 2) and tuple(qv.invariants()) == (2, 2)

    assert qu.is_isomorphic(qv, kind="group") is True        # same (Z/2)^2
    assert qu.is_isomorphic(qv, kind="bilinear") is True      # Nik80 1.8.2: u_- ~= v_-
    assert qu.is_isomorphic(qv, kind="quadratic") is False    # Br 0 vs 4; MM09 7.7.3
    assert (qu.brown_invariant(), qv.brown_invariant()) == (0, 4)


def test_rank_one_2adic_form_separates_bilinear_and_quadratic_orthogonal_groups():
    r"""For the rank-one even lattice <8>, A_L is cyclic of order eight.

    Nikulin's 2-adic rank-one forms distinguish the bilinear pairing from the
    quadratic refinement: every unit u with u^2 = 1 mod 8 preserves the bilinear
    form, while preserving q narrows the unit action to u = +-1.  This pins the
    public kind="bilinear" and kind="quadratic" orthogonal-group surfaces on a
    nontrivial cyclic 2-primary form.
    """
    lattice = lc.Lattice(matrix(ZZ, 1, 1, [8]))
    q = lattice.discriminant_group()
    generator = q.gen(0)

    assert lattice.rank() == 1
    assert lattice.is_even()
    assert lattice.signature_pair() == (1, 0)
    assert lattice.determinant() == 8
    assert tuple(q.invariants()) == (8,)
    assert q.cardinality() == 8
    assert q.brown_invariant() == 1
    assert q.brown_invariant() % 8 == lattice.signature() % 8

    assert q.automorphism_group().order() == 4
    assert sorted(
        tuple(action(generator).coefficient_vector())
        for action in q.automorphism_group()
    ) == [(1,), (3,), (5,), (7,)]
    assert q.orthogonal_group(kind="bilinear").order() == 4
    assert sorted(
        tuple(action(generator).coefficient_vector())
        for action in q.orthogonal_group(kind="bilinear")
    ) == [(1,), (3,), (5,), (7,)]
    assert q.orthogonal_group(kind="quadratic").order() == 2
    assert sorted(
        tuple(action(generator).coefficient_vector())
        for action in q.orthogonal_group(kind="quadratic")
    ) == [(1,), (7,)]


def test_form_negation_via_twist_matches_miranda_morrison_negation_rules():
    r"""-q_L = q_{L(-1)}, and MM09's negation rules classify when q ~= -q.

    Negating a lattice negates its discriminant form: q.twist(-1) equals
    q_{L.twist(-1)} (the "-q_L" of the task). MM09 ACX7WF7L .md:660 lists the
    negation rules for the elementary forms:
      -u_k ~= u_k,  -v_k ~= v_k,   but   -w_{p,k}^eps ~= w_{p,k}^{-eps}.
    So the even 2-adic forms are self-negative (q ~= -q), while the rank-1 form
    w_{2,1}^eps of q_{E7} is not (eps != -eps): here Br(q_{E7}) = 7 while
    Br(-q_{E7}) = 1, and 7 != 1 (mod 8) confirms non-isomorphism (Nik80 Thm 1.11.3).
    """
    # -q_L computed at the form level equals -q_L computed on the twisted lattice
    D4 = lc.Lattice("D4")
    q = D4.discriminant_group()
    assert q.twist(-1).is_isomorphic(D4.twist(-1).discriminant_group(), kind="quadratic")

    # v_1 = q_{D4} is self-negative:  -v_1 ~= v_1   (MM09 .md:660)
    assert D4.is_even() and D4.determinant() == 4 and tuple(q.invariants()) == (2, 2)
    assert q.is_isomorphic(q.twist(-1), kind="quadratic") is True

    # w_{2,1}^eps = q_{E7} is NOT self-negative:  -w ~= w^{-eps} != w   (MM09 .md:660)
    E7 = lc.Lattice("E7")
    qe = E7.discriminant_group()
    assert E7.is_even() and E7.determinant() == 2 and tuple(qe.invariants()) == (2,)
    assert qe.is_isomorphic(qe.twist(-1), kind="quadratic") is False
    assert (qe.brown_invariant(), qe.twist(-1).brown_invariant()) == (7, 1)


def test_isotropic_subgroups_are_even_overlattices_nikulin_prop_1_4_1():
    r"""Isotropic subgroups of q_L <-> even overlattices of L (Nikulin Prop 1.4.1).

    Nik80 D7BP5F7Z .md:216-220 Prop 1.4.1: H |-> S' is a bijection between isotropic
    subgroups H of A_S (q_S|H = 0) and even overlattices S' of S, with
    |H^perp| = |A_S| * |H|^{-1} (Nik80 .md:230). A maximal isotropic H with
    |H|^2 = |A_S| is Lagrangian and yields a *unimodular* even overlattice.

    q_{U(2)} = u_1 is metabolic: it has two Lagrangian subgroups of order 2, each
    giving an even *unimodular* rank-2 overlattice (= U, det -1). By contrast
    q_{A2} is anisotropic (Z/3, no nonzero isotropic element), so its only
    isotropic subgroup is {0} and A_2 admits no proper even overlattice.
    """
    # U(2): metabolic, Lagrangian subgroups give even unimodular overlattices
    U2 = _U(2)
    q = U2.discriminant_group()
    assert U2.is_even() and not U2.is_unimodular()
    assert U2.signature_pair() == (1, 1) and tuple(q.invariants()) == (2, 2)
    assert q.is_metabolic() is True

    maximal = q.maximal_isotropic_subgroups()
    assert len(maximal) == 2
    lagrangian_orders = sorted(H.cardinality() for H in q.lagrangian_subgroups())
    assert lagrangian_orders == [2, 2]                       # |H|^2 = |A_S| = 4
    for H in maximal:
        assert q.is_isotropic_subgroup(H) is True
        assert q.is_maximal_isotropic(H) is True
        assert q.is_lagrangian(H) is True
        assert H.cardinality() ** 2 == q.cardinality()      # Lagrangian: Nik80 .md:230
        M = q.overlattice_from_isotropic_subgroup(H)
        assert M.rank() == 2 and M.is_even() and M.is_unimodular()   # Prop 1.4.1

    # A2: anisotropic => only the trivial isotropic subgroup, no proper overlattice
    A2 = lc.Lattice("A2")
    qa = A2.discriminant_group()
    assert A2.is_even() and not A2.is_unimodular()
    assert A2.signature_pair() == (2, 0) and tuple(qa.invariants()) == (3,)
    assert qa.is_anisotropic() is True
    assert [H.cardinality() for H in qa.isotropic_subgroups()] == [1]
    only = qa.maximal_isotropic_subgroups()
    assert len(only) == 1 and only[0].cardinality() == 1
    assert qa.overlattice_from_isotropic_subgroup(only[0]).determinant() == 3   # = A2 itself
