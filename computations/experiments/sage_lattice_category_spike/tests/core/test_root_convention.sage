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
