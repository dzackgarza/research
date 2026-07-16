r"""Morphism-siting proofs for the subobject substrate (issue #100).

A subobject is the pair ``(L, f: L -> M)``; every operation relating ``L`` to
``M`` composes ``f``. These tests pin the semantic contracts: the historical
``dual -> finite_quotient -> induced_map_on_quotient`` reproducer on a genuine
rank-deficient realization, the relation-preservation guard on quotients, and
index questions answered by the inclusion's cokernel rather than a numerical
proxy on two bare lattices.
"""

from __future__ import annotations

import pytest

from sage.all import ZZ, identity_matrix, matrix, oo

from sage_lattice_category_spike.lattice_categories import Lattice


def test_realized_root_sublattice_dual_chain_induces_negation_action():
    r"""The historical #100 reproducer, kept green: A2 realized as a genuine
    subobject of I_{0,3} (rank 2 strictly below the codomain rank 3), routed
    through ``dual -> finite_quotient -> induced_map_on_quotient``. This chain
    once threw ``ArithmeticError: vector is not in free module``."""
    A2 = Lattice("A2")
    realization = A2.bourbaki_embedding().image()
    assert realization.rank() == 2
    assert realization.inclusion().codomain().rank() == 3
    assert realization.gram_matrix() == A2.gram_matrix()

    L = realization.lattice()
    L_dual = L.dual()
    quotient = L_dual.finite_quotient(L)
    assert quotient.cardinality() == 3
    negation = L_dual.hom(-identity_matrix(ZZ, 2))
    induced = negation.induced_map_on_quotient(quotient)
    generator = quotient.gen(0)
    assert induced(generator) == -generator
    assert induced(generator) != generator  # negation is nontrivial on Z/3


def test_induced_action_on_a_genuine_subobject_relation_quotient():
    r"""The quotient machinery on a relation that is a genuine finite-index
    subobject (not the metric dual): the induced action of a cover isometry
    that preserves the relation is the correct action on the finite quotient."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    S = M.subobject([M([3, 0]), M([0, 1])], label="S")
    quotient = M.finite_quotient(S)
    assert quotient.cardinality() == 3
    reflect = M.hom(matrix(ZZ, [[-1, 0], [0, 1]]))  # preserves S
    induced = reflect.induced_map_on_quotient(quotient)
    generator = quotient.gen(0)
    assert induced(generator) == -generator
    assert induced(generator) != generator  # negation is nontrivial on Z/3


def test_induced_map_rejects_isometry_not_preserving_the_relation():
    r"""A morphism descends to the quotient exactly when the composite
    ``relation -> cover -> cover -> cover/relation`` is zero; an isometry of
    the cover that does not preserve the relation subobject is rejected."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    S = M.subobject([M([3, 0]), M([0, 1])], label="S")
    quotient = M.finite_quotient(S)
    swap = M.hom(matrix(ZZ, [[0, 1], [1, 0]]))  # isometry of M; swap does not preserve S
    with pytest.raises(AssertionError):
        swap.induced_map_on_quotient(quotient)


def test_isometry_subgroup_preserves_is_a_factorization_query_on_the_subobject():
    r"""``preserves`` asks whether each generator composed with the inclusion
    factors through the inclusion -- sited on the carried witness. The bare
    spelling was degenerate (membership in the full standard module, true for
    every endomorphism)."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    S = M.subobject([M([3, 0]), M([0, 1])], label="S")
    O_M = M.isometry_group()
    reflect = M.hom(matrix(ZZ, [[-1, 0], [0, 1]]))  # maps S into S
    swap = M.hom(matrix(ZZ, [[0, 1], [1, 0]]))  # maps e2 to e1, outside S
    assert O_M.subgroup([reflect]).preserves(S)
    assert not O_M.subgroup([swap]).preserves(S)


def test_index_is_the_cokernel_cardinality_of_the_inclusion():
    r"""The index ``[M : L]`` is BY DEFINITION the cardinality of the
    inclusion's cokernel -- asked on the morphism, total for every morphism
    (infinite when the image is not full rank)."""
    A2 = Lattice("A2")
    assert A2.dual_inclusion().index() == 3  # [A2# : A2] = |det A2| = 3

    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    S = M.subobject([M([2, 0]), M([0, 1])], label="S")
    assert S.index() == 2
    thin = M.subobject([M([2, 0])], label="S1")
    assert thin.index() == oo  # rank 1 in rank 2: the cokernel is infinite


def test_index_in_saturation_is_the_factorization_index_on_the_subobject():
    r"""``[L^sat : L]`` is the cokernel cardinality of the mono factorization
    ``L -> L^sat`` of the carried inclusion -- sited on the subobject, not on
    a bare lattice (which carries no witness to saturate against)."""
    M = Lattice(matrix(ZZ, [[-1, 0], [0, -1]]), label="M")
    full_rank = M.subobject([M([2, 0]), M([0, 1])], label="S")
    assert full_rank.index_in_saturation() == 2  # saturation is all of M

    thin = M.subobject([M([2, 0])], label="S1")  # rank 1, codomain rank 2
    assert thin.index_in_saturation() == 2  # saturation is spanned by e1
    assert thin.saturation_factorization().codomain() == thin.saturation().lattice()

    primitive = M.subobject([M([1, 0])], label="P")
    assert primitive.index_in_saturation() == 1
