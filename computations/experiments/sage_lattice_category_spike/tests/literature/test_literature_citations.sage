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
    T2WVLTDB | CS10 | TCJKXU3D. Ch. 4 tabulates the root lattices A_n, D_n, E_6,
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
from math import factorial, prod

from sage.all import QQ, ZZ, identity_matrix, matrix
import sage_lattice_category_spike.lattice_categories as lc


def _direct_sum(*lattices):
    return reduce(lambda a, b: a.direct_sum(b), lattices)


def _coefficient_rows(elements):
    return sorted(tuple(element.coefficient_vector()) for element in elements)


def _local_symbol_rows(genus):
    return {
        ZZ(symbol.prime()): {
            "canonical_symbol": tuple(tuple(row) for row in symbol.canonical_symbol()),
            "determinant": ZZ(symbol.determinant()),
            "excess": ZZ(symbol.excess()),
            "level": ZZ(symbol.level()),
            "rank": ZZ(symbol.rank()),
        }
        for symbol in genus.local_symbols()
    }


def test_irreducible_root_lattice_invariants_match_conway_sloane_chapter_4():
    r"""Determinant, minimal norm, and number of roots of every irreducible root
    lattice, pinned to Conway & Sloane, *SPLAG* Chapter 4 [CS10]. For a root
    lattice the minimal vectors ARE the roots (minimal norm 2), so the kissing
    number tau equals the number of roots:

      - A_n (sec 6.1): det = n+1, min norm 2, tau = n(n+1);
      - D_n (sec 7.1): det = 4,   min norm 2, tau = 2n(n-1);
      - E_6 (sec 8.3): det = 3,   min norm 2, tau = 72;
      - E_7 (sec 8.2): det = 2,   min norm 2, tau = 126;
      - E_8 (sec 8.1): det = 1,   min norm 2, tau = 240.
    """
    # (spike name, CS10 determinant, CS10 kissing number = number of roots)
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
    group: order = det L [CS10 sec 2.4], with invariant-factor structure from
    [CS10 Ch. 4]:

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


def test_small_root_lattice_automorphism_orders_match_conway_sloane_chapter_4():
    r"""Conway-Sloane Ch. 4 describes root-lattice automorphism groups via the
    Weyl group G_0 and diagram automorphisms G_1, with |G(L)| = g_0 g_1
    [CS10 Ch. 4 sec. 2 and the summary lines in secs. 6.1, 7.1].

      - A_n: G_0 = S_{n+1}; G_1 has order 2 except for A_1.
      - D_4: g_0 = 2^3 * 4! and g_1 = 3! (triality).

    This pins the spike's GAP/Sage-backed isometry_group().order() against a
    published group order, not just against the existence of form-preserving
    matrices. E_8 is intentionally excluded here: its order is citable but slow
    enough to belong in a later CI/slow tranche.
    """
    expected_orders = {
        "A1": 2,
        "A2": 2 * factorial(3),
        "A3": 2 * factorial(4),
        "D4": (2**3) * factorial(4) * factorial(3),
    }
    for name, order in expected_orders.items():
        lattice = lc.Lattice(name)
        assert lattice.is_even()            # root-lattice setup guard
        assert lattice.minimum() == 2       # roots are the minimal vectors
        group = lattice.isometry_group()
        assert group.is_finite()
        assert group.order() == order
        assert all(generator.is_isometry() for generator in group.gens())


def test_nikulin_primary_decomposition_of_finite_quadratic_forms():
    r"""Nikulin Prop. 1.2.2 [Nik80]: a finite quadratic form decomposes as the
    orthogonal direct sum of its p-primary restrictions q_p. The fixture is a
    deliberately small mixed-primary form with 2-, 3-, and 5-primary factors, so
    the test exercises the finite-form vocabulary directly rather than a lattice
    determinant read.
    """
    form = lc.TorsionQuadraticForm(
        matrix.diagonal(QQ, [QQ(1) / 2, QQ(2) / 3, QQ(4) / 5])
    )

    assert form.invariants() == (2, 3, 5)
    assert form.cardinality() == 30
    primary_parts = form.primary_decomposition()
    assert tuple(part.invariants() for part in primary_parts) == ((2,), (3,), (5,))
    assert prod(part.cardinality() for part in primary_parts) == form.cardinality()
    for prime, primary_part in zip((2, 3, 5), primary_parts):
        assert ZZ(primary_part.annihilator()).prime_divisors() == [prime]
        assert primary_part.primary_decomposition()[0].is_isomorphic(
            primary_part,
            kind="quadratic",
        )


def test_nikulin_rank_obstruction_for_genus_of_finite_quadratic_form():
    r"""Nikulin Thm. 1.10.1 [Nik80] gives the rank and local-generator
    obstructions for realizing a finite quadratic form as the discriminant form
    of an even lattice with prescribed signature. The 2-elementary form
    ``diag(1/2, 1/2, 1/2)`` has Brown invariant 3 and needs enough lattice rank:
    it is realized by a positive rank-3 lattice, but not by the listed too-small
    or parity-incompatible signatures.
    """
    form = lc.TorsionQuadraticForm(identity_matrix(QQ, 3) / 2)

    assert form.invariants() == (2, 2, 2)
    assert form.cardinality() == 8
    assert form.rank_p(2) == 3
    assert form.brown_invariant() == 3
    assert form.is_genus((3, 0))
    for signature in ((1, 1), (4, 0), (5, 0), (3, 1)):
        assert not form.is_genus(signature)


def test_watson_split_genus_local_symbols_match_conway_sloane_chapter_15():
    r"""Conway-Sloane Ch. 15 sec. 9 [CS10] gives Watson's split genus example:
    the ternary positive-definite lattices with Gram matrices
    ``[[2,1,0],[1,2,0],[0,0,18]]`` and
    ``[[6,3,0],[3,6,0],[0,0,2]]`` have the same genus but are not isometric.
    The citable content is the p-adic genus-symbol data at 2 and 3, not just a
    determinant/signature guard.
    """
    first = lc.Lattice(matrix(ZZ, [[2, 1, 0], [1, 2, 0], [0, 0, 18]]))
    second = lc.Lattice(matrix(ZZ, [[6, 3, 0], [3, 6, 0], [0, 0, 2]]))

    for lattice in (first, second):
        assert lattice.rank() == 3
        assert lattice.is_even()
        assert lattice.signature_pair() == (3, 0)
        assert lattice.determinant() == 54

    first_genus = first.genus()
    second_genus = second.genus()
    assert first_genus == second_genus
    assert first.same_genus(second)
    assert not first.is_isometric(second)
    assert _local_symbol_rows(first_genus) == {
        ZZ(2): {
            "canonical_symbol": ((0, 2, -1, 0, 0), (1, 1, 1, 1, 1)),
            "determinant": 2,
            "excess": 1,
            "level": 2,
            "rank": 3,
        },
        ZZ(3): {
            "canonical_symbol": ((0, 1, -1), (1, 1, -1), (2, 1, -1)),
            "determinant": 27,
            "excess": 6,
            "level": 9,
            "rank": 3,
        },
    }
    assert _local_symbol_rows(second_genus) == _local_symbol_rows(first_genus)


def test_nikulin_even_overlattices_of_U2_are_isotropic_subgroups():
    r"""Nikulin Prop. 1.4.1 [Nik80]: even overlattices S' of an even lattice S
    correspond to isotropic subgroups H of A_S, and the discriminant form of S'
    is q_{S'} = (q_S | H^perp) / H. For S = U(2), A_S = (Z/2)^2 has exactly two
    nonzero isotropic elements; each generated subgroup is Lagrangian, and the
    corresponding even overlattice is unimodular with trivial discriminant form.
    """
    lattice = lc.Lattice("U").twist(2)
    discriminant_form = lattice.discriminant_group()

    assert lattice.is_even()                 # Nikulin Prop. 1.4.1 hypothesis
    assert lattice.signature_pair() == (1, 1)
    assert lattice.determinant() == -4       # setup guard for |A_S| = 4
    assert discriminant_form.invariants() == (2, 2)
    assert _coefficient_rows(discriminant_form.isotropic_elements()) == [
        (0, 0),
        (0, 1),
        (1, 0),
    ]

    nontrivial_isotropic_subgroups = [
        subgroup
        for subgroup in discriminant_form.isotropic_subgroups()
        if subgroup.cardinality() == 2
    ]
    assert [
        _coefficient_rows(subgroup.elements())
        for subgroup in nontrivial_isotropic_subgroups
    ] == [[(0, 0), (0, 1)], [(0, 0), (1, 0)]]

    for subgroup in nontrivial_isotropic_subgroups:
        orthogonal = discriminant_form.orthogonal(subgroup)
        quotient_form = discriminant_form.orthogonal_quotient(subgroup)
        overlattice = discriminant_form.overlattice_from_isotropic_subgroup(subgroup)
        overlattice_form = discriminant_form.discriminant_form_of_overlattice(subgroup)

        assert _coefficient_rows(orthogonal.elements()) == _coefficient_rows(
            subgroup.elements()
        )
        assert quotient_form.invariants() == ()
        assert overlattice_form.is_isomorphic(quotient_form, kind="quadratic")
        assert overlattice.discriminant_group().invariants() == ()
        assert overlattice.is_even() and overlattice.is_unimodular()
        assert overlattice.signature_pair() == lattice.signature_pair()
        assert abs(ZZ(lattice.determinant() / overlattice.determinant())) == 4


def test_a2_e6_isotropic_glue_reconstructs_the_e8_root_lattice():
    r"""Conway-Sloane Ch. 4 describes E_6 as the complement of an A_2 sublattice
    in E_8, and Nikulin Prop. 1.4.1 identifies even overlattices with isotropic
    subgroups of the discriminant form. The anti-isometry q_{A_2} = -q_{E_6}
    therefore gives a Lagrangian order-3 subgroup in A_{A_2} + A_{E_6}; gluing
    along it reconstructs the even unimodular root lattice E_8.
    """
    ambient = lc.Lattice("A2").direct_sum(lc.Lattice("E6"))
    discriminant_form = ambient.discriminant_group()

    assert ambient.is_even()
    assert ambient.determinant() == 9
    assert discriminant_form.invariants() == (3, 3)
    subgroup = discriminant_form.subgroup_generated_by(
        [discriminant_form.gen(0) + 2 * discriminant_form.gen(1)]
    )
    assert subgroup.cardinality() == 3
    assert discriminant_form.is_isotropic_subgroup(subgroup)
    assert discriminant_form.orthogonal_quotient(subgroup).invariants() == ()

    glued = discriminant_form.overlattice_from_isotropic_subgroup(subgroup)
    assert glued.is_even() and glued.is_unimodular()
    assert glued.minimum() == 2
    assert len(glued.roots()) == 240
    assert glued.discriminant_group().invariants() == ()
    assert glued.is_isometric(lc.Lattice("E8"))


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
    r"""Gauss-Milgram / Milgram's formula (Milnor-Husemoller App. 4; CS10 Ch. 15;
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
        pos, neg = lattice.signature()
        assert gauss_sum_invariant % 8 == (pos - neg) % 8


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
    r"""E_8 [CS10 sec 8.1]: the unique even unimodular lattice of rank 8 -- det 1,
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
