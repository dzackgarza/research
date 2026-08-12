r"""Method-placement proofs (issue #100, ratified enforcement design).

Every operation lives on the categorical entity whose data it consumes:
morphism-sited geometry (saturation triangle, restriction, preservation,
orthogonal complement, quotient descent) on ``LatticeMorphism``, and
existence/classification questions on the homset parents ``Isom(L, M)`` and
``Emb(L, M)``. Each fixed site is exercised through a genuine
rank < codomain-rank witness where the operation admits one.
"""

from __future__ import annotations

import pytest

from sage.all import QQ, ZZ, matrix, oo

from sage_lattice_category_spike.lattice_categories import Lattice


def test_mono_factors_through_its_saturation():
    r"""The saturation triangle on a genuine index-2 mono: ``iota = (S^sat ->
    M) . (S -> S^sat)`` with ``[S^sat : S] = 2``, all three arrows morphisms.
    Witness: S = span(2e1, e2) inside M = diag(-1, -1) (rank 2 = codomain
    rank; the factorization is nontrivial), and the rank-1 line 3e1 inside M
    (rank 1 < codomain rank 2)."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    inclusion = M.subobject([M([2, 0]), M([0, 1])], "S").inclusion()
    factor = inclusion.saturation_factorization()
    assert factor.index() == 2
    assert inclusion.saturation().is_primitive()
    assert inclusion.saturation().inclusion() * factor == inclusion

    line = M.subobject([M([3, 0])], "line").inclusion()
    line_factor = line.saturation_factorization()
    assert line_factor.index() == 3
    assert line.index() == oo  # not full rank: the cokernel is infinite
    assert line.saturation().inclusion() * line_factor == line


def test_primitive_embedding_has_identity_saturation_factorization():
    A2 = Lattice("A2")
    bourbaki = A2.bourbaki_embedding()
    assert bourbaki.is_primitive_embedding()
    assert bourbaki.saturation_factorization().index() == 1


def test_restrict_is_precomposition_and_preserves_is_factorization():
    r"""A reflection preserves the line it reflects and its orthogonal
    complement, and ``restrict`` to a stable line is the morphism computing
    the +-1 action there; an isometry moving the line is refused nothing --
    ``preserves`` just answers False."""
    A2 = Lattice("A2")
    root = A2.gen(0)
    sigma = A2.reflection(root)
    line = A2.subobject([root], "line")
    assert sigma.preserves(line)
    restricted = sigma.restrict(line)
    assert restricted(line.lattice().gen(0)) == -A2.gen(0)  # s_v(v) = -v in A2

    complement = line.inclusion().orthogonal_complement()
    assert sigma.preserves(complement)

    # The Weyl rotation of order 3 moves every line: preserves answers False.
    rotation = A2.reflection(A2.gen(0)) * A2.reflection(A2.gen(1))
    assert rotation.order() == 3
    assert not rotation.preserves(line)


def test_orthogonal_complement_is_the_kernel_of_the_composed_pairing():
    r"""On the rank < codomain-rank witness A2 c I_{0,3}: the complement of
    the realized A2 is the rank-1 primitive line pairing to zero with it."""
    A2 = Lattice("A2")
    realization = A2.bourbaki_embedding()
    complement = realization.orthogonal_complement()
    assert complement.rank() == 1
    assert complement.is_primitive()
    codomain_form = realization.codomain()
    for i in range(2):
        assert codomain_form.b(realization(A2.gen(i)), complement.inclusion()(complement.lattice().gen(0))) == 0


def test_radical_is_the_complement_of_the_identity():
    r"""The radical as morphism-sited vocabulary: ``radical()`` IS the
    orthogonal complement of the identity morphism -- the subobject pairing
    to zero with everything. Witness: diag(0, -2) has rank-1 primitive
    radical and negative-definite radical quotient."""
    degenerate = Lattice(matrix(ZZ, [[0, 0], [0, -2]]), label="degenerate")
    radical = degenerate.radical()
    assert radical.rank() == 1
    assert radical.is_primitive()
    assert radical.lattice().gram_matrix() == matrix(ZZ, [[0]])
    assert radical.inclusion().matrix() == degenerate.identity_morphism().orthogonal_complement().inclusion().matrix()
    assert degenerate.radical_quotient().gram_matrix() == matrix(ZZ, [[-2]])

    A2 = Lattice("A2")
    assert A2.radical().rank() == 0
    assert A2.radical_quotient() is A2

    # A skew radical off the coordinate axes: diag-embedded (v, v) pairing.
    skew = Lattice(matrix(ZZ, [[-1, -1], [-1, -1]]), label="skew")
    skew_radical = skew.radical()
    assert skew_radical.rank() == 1
    assert skew.b(skew_radical.inclusion()(skew_radical.lattice().gen(0)), skew.gen(0)) == 0
    assert skew.radical_quotient().rank() == 1


def test_isometry_existence_is_the_homset_emptiness_question():
    r"""``Isom(L, M)`` is a parent: emptiness owns the G1 decision,
    ``is_isometric`` is its router, and the nonempty homset enumerates as an
    ``O(M)``-torsor."""
    A2 = Lattice("A2")
    other = Lattice(matrix(ZZ, [[-2, 1], [1, -2]]), label="A2-clone")
    isometries = A2.Isom(other)
    assert not isometries.is_empty()
    assert A2.is_isometric(other)
    witness = isometries.an_element()
    assert witness in isometries
    assert witness.is_isometry()

    # |Isom(A2, clone)| = |O(A2)| = 12 (the torsor structure).
    assert isometries.cardinality() == 12
    enumerated = tuple(isometries)
    assert len(enumerated) == 12
    assert len(set(enumerated)) == 12
    assert all(isometry in isometries for isometry in enumerated)


def test_empty_isometry_homset_and_the_router_agree():
    A2 = Lattice("A2")
    square = Lattice(matrix(ZZ, [[-2, 0], [0, -2]]), label="square")
    isometries = A2.Isom(square)
    assert isometries.is_empty()  # det 3 vs det 4
    assert not A2.is_isometric(square)
    assert isometries.cardinality() == 0
    assert tuple(isometries) == ()
    with pytest.raises(AssertionError):
        isometries.an_element()


def test_isometry_homset_cardinality_fails_under_its_own_name_when_ungrounded():
    r"""``Isom(L, M).cardinality()`` on a NONEMPTY homset whose ``O(M)``
    carries no grounded finiteness answer (indefinite rank 3: the odd
    unimodular diag(1, 1, -1), a single-spinor-genus genus so emptiness IS
    decided) must fail under the cardinality contract's own name -- not deep
    inside the group engine's grounding assert -- and must never invent an
    answer (no computation grounds ``+Infinity`` any more than it grounds a
    finite order)."""
    gram = matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    left = Lattice(gram, label="odd-2-1-left")
    right = Lattice(gram, label="odd-2-1-right")
    isometries = left.Isom(right)
    assert not isometries.is_empty()  # existence IS decided (Eichler)
    with pytest.raises(AssertionError, match=r"routes through its O\(M\)-torsor structure"):
        isometries.cardinality()


def test_embedding_homset_enumerates_by_generator_patterns():
    r"""``Emb(L, M)`` on definite codomains: A1(-1) = diag(-2) has exactly
    six embeddings into A2 (one per root -- rank 1 < codomain rank 2), and
    each is recognized by the homset."""
    A1 = Lattice(matrix(ZZ, [[-2]]), label="A1")
    A2 = Lattice("A2")
    embeddings = A1.Emb(A2)
    assert not embeddings.is_empty()
    enumerated = tuple(embeddings)
    assert len(enumerated) == 6  # the six roots of A2
    assert all(embedding in embeddings for embedding in enumerated)
    assert all(embedding.is_primitive_embedding() for embedding in enumerated)
    assert embeddings.an_element() in embeddings


def test_embedding_homset_is_empty_when_no_vector_represents_the_square():
    r"""diag(-10) does not embed into A2: x^2 - xy + y^2 = 5 has no integer
    solutions, so the generator has no candidate image."""
    diag10 = Lattice(matrix(ZZ, [[-10]]), label="diag-10")
    A2 = Lattice("A2")
    embeddings = diag10.Emb(A2)
    assert embeddings.is_empty()
    with pytest.raises(AssertionError):
        embeddings.an_element()


def test_embedding_homset_finds_the_index_two_sublattice():
    r"""A full-rank non-primitive embedding is still an embedding: span(2e1,
    e2) in M = diag(-1,-1) is found by the enumeration with index 2."""
    S = Lattice(matrix(ZZ, [[-4, 0], [0, -1]]), label="S")
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    embeddings = tuple(S.Emb(M))
    assert embeddings  # nonempty
    assert any(embedding.index() == 2 for embedding in embeddings)
    assert all(not embedding.is_primitive_embedding() for embedding in embeddings)


def test_embedding_homset_owns_its_integral_definite_regime():
    r"""``Emb(L, M)`` names its supported regime at its own boundary. A
    NON-integral definite codomain (gram diag(1/2, 1/2)) is refused by the
    homset's own gating assert -- not by an incidental assert deep in the
    short-vector engine -- so a future engine widening cannot silently turn
    the iterator into an incomplete enumeration presented as the full
    homset. A non-integral domain square into an integral codomain is
    honest emptiness (an integral form represents only integers), not a
    crash."""
    half = Lattice(matrix(QQ, [[1 / 2, 0], [0, 1 / 2]]), label="half")
    gen2 = Lattice(matrix(ZZ, [[2]]), label="gen2")
    embeddings = gen2.Emb(half)
    with pytest.raises(AssertionError, match="INTEGRAL definite codomains"):
        tuple(embeddings)
    with pytest.raises(AssertionError, match="INTEGRAL definite codomains"):
        embeddings.is_empty()

    A2 = Lattice("A2")
    half_line = Lattice(matrix(QQ, [[-1 / 2]]), label="half-line")
    assert half_line.Emb(A2).is_empty()  # -1/2 is not an integral value


def test_subobject_sum_and_intersection_carry_their_inclusions():
    r"""The subobject algebra inside a common codomain (#100 T4, burden
    transferred from the deleted bare-lattice sum/intersection): joins and
    meets return subobjects, whose indices and saturations are asked of
    their carried inclusions. In M = diag(-1,-1): span(2e1) + span(3e1) =
    span(e1) (gcd) and their meet is span(6e1) (lcm)."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    two = M.subobject([M([2, 0])], "2e1")
    three = M.subobject([M([3, 0])], "3e1")
    total = two.sum(three)
    assert total.rank() == 1
    assert total.inclusion().saturation_factorization().index() == 1  # span(e1) is primitive
    meet = two.intersection(three)
    assert meet.rank() == 1
    assert meet.inclusion().saturation_factorization().index() == 6  # span(6e1)

    left = M.subobject([M([2, 0]), M([0, 1])], "left")
    right = M.subobject([M([1, 0]), M([0, 2])], "right")
    assert left.sum(right).index() == 1  # together they span all of M
    assert left.intersection(right).index() == 4  # span(2e1, 2e2)

    first_axis = M.subobject([M([1, 0])], "e1")
    second_axis = M.subobject([M([0, 1])], "e2")
    assert first_axis.sum(second_axis).index() == 1
    assert first_axis.intersection(second_axis).rank() == 0


def test_quotient_descent_is_asked_of_the_morphism():
    r"""The morphism-sited descent on the genuine finite-index subobject
    relation: negation descends to M/span(3e1, e2), the swap isometry (which
    does not preserve the relation) is refused."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    S = M.subobject([M([3, 0]), M([0, 1])], "S")
    quotient = M.finite_quotient(S)
    assert quotient.cardinality() == 3
    negation = M.hom(matrix(ZZ, [[-1, 0], [0, -1]]))
    induced = negation.induced_map_on_quotient(quotient)
    generator = quotient.gen(0)
    assert induced(generator) == -generator
    swap = M.hom(matrix(ZZ, [[0, 1], [1, 0]]))
    with pytest.raises(AssertionError):
        swap.induced_map_on_quotient(quotient)
