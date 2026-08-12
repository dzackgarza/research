r"""Root convention for issue #5: roots are defined by integral reflection
(``s_v \in O(L)``), not by norm ``\pm 2``; named root lattices are
negative definite by construction (the AG convention).

These are owned-behavior proofs: the assertions pin the *sign* and the
*reflective* root definition, so they are not sign-invariant and cannot go
green under the pre-#5 norm-based, positive-default kernel.
"""
from __future__ import annotations

import pytest

import sage_lattice_category_spike.lattice_categories as lc


def test_named_root_lattices_are_negative_definite_by_default():
    r"""The AG convention: unmarked named root lattices are negative definite,
    roots of square -2. E8 has signature (0, 8)."""
    E8 = lc.Lattice("E8")
    assert E8.signature() == (0, 8)
    assert E8.is_negative_definite()
    assert len(E8.roots()) == 240
    assert all(root.q() == -2 for root in E8.roots())
    assert E8.cartan_type() == ("E", 8)
    A2 = lc.Lattice("A2")
    assert A2.signature() == (0, 2)
    assert A2.is_negative_definite()


def test_minus_one_spelling_is_the_positive_twist_with_provenance():
    r"""E8(-1) MEANS positive definite: it is the -1 twist of the negative
    default, equal to Lattice("E8").twist(-1), and it keeps its Cartan
    provenance (the twist(-1) provenance-drop defect is fixed)."""
    e8_positive = lc.Lattice("E8(-1)")
    assert e8_positive == lc.Lattice("E8").twist(-1)
    assert e8_positive.signature() == (8, 0)
    assert e8_positive.is_positive_definite()
    assert all(root.q() == 2 for root in e8_positive.roots())
    assert e8_positive.cartan_type() == ("E", 8)
    assert lc.Lattice("E8").twist(-1).cartan_type() == ("E", 8)


def test_there_is_no_boolean_sign_flag():
    r"""The sign is carried by the twist, never a boolean mode flag (policy)."""
    with pytest.raises(TypeError):
        lc.Lattice("E8", negative=True)


def test_root_lattice_is_a_sublattice_of_a_unimodular_lattice_via_embedding():
    r"""Issue #5's required realization: a root lattice is a genuine sublattice
    of the unimodular lattice I_{0,m} (m the Bourbaki ambient dimension),
    witnessed by an explicit embedding morphism e_i |-> r_i sending the
    generators to the simple-root vectors. The identity of the lattice is still
    (base_ring, Gram); the embedding is a first-class form-preserving morphism."""
    A2 = lc.Lattice("A2")
    emb = A2.bourbaki_embedding()
    ambient = emb.codomain()
    assert emb.domain() is A2
    assert ambient.is_unimodular()
    assert ambient.signature_pair() == (0, 3)                 # I_{0,3}, negative definite
    # the generators map to roots of square -2, form preserved
    assert emb(A2.gen(0)).q() == A2.gen(0).q() == -2
    assert emb.is_primitive_embedding()                       # A_n is primitive in I_{0,n+1}
    # the positive twist embeds into the positive unimodular lattice I_{3,0}
    assert lc.Lattice("A2(-1)").bourbaki_embedding().codomain().signature_pair() == (3, 0)


def test_e8_bourbaki_embedding_realizes_the_half_integral_roots():
    r"""E8's simple roots live in (1/2)ZZ^8, so the embedding into I_{0,8} is
    through its rational span (E8 is even unimodular, not a ZZ-sublattice of the
    odd I_{0,8}); the morphism is still form-preserving with root images of
    square -2."""
    E8 = lc.Lattice("E8")
    emb = E8.bourbaki_embedding()
    assert emb.domain() == E8.base_extend(QQ)
    assert emb.domain().base_ring() is QQ
    assert emb.codomain().base_ring() is QQ
    assert emb.codomain().rank() == 8
    assert all(emb(emb.domain().gen(i)).q() == -2 for i in range(8))


def test_is_root_is_reflection_integrality_not_norm_pm2():
    r"""``<-4>`` has a generator that is a root (its reflection ``-1`` is
    integral) yet has square ``-4``, so the norm-``\pm 2`` enumeration misses
    it. Pins ``is_root`` to the reflective definition."""
    L = lc.Lattice([[-4]])
    v = L.gen(0)
    assert v.q() == -4
    assert L.is_root(v)
    assert v not in L.roots()


def test_is_root_rejects_isotropic_and_non_reflective_vectors():
    r"""``is_root`` is the reflection predicate: a scalar multiple that stays
    integral shares its reflection (``s_{2v} = s_v``), so primitivity is not
    part of the definition. A genuine non-root is one whose reflection leaves
    the lattice: ``(1, 3)`` in ``A2`` has square 14 and non-integral ``s_v``."""
    A2 = lc.Lattice("A2")
    assert not A2.is_root(A2.zero())          # q = 0 is not anisotropic
    assert not A2.is_root(A2([1, 3]))          # reflection s_v is not integral => not a root


def test_simple_roots_are_roots():
    A2 = lc.Lattice("A2")
    assert A2.is_root(A2.gen(0))
    assert A2.is_root(A2.gen(1))
