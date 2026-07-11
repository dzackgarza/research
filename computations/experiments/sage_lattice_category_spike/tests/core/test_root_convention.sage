r"""Root convention for issue #5: roots are defined by integral reflection
(``s_v \in O(L)``), not by norm ``\pm 2``; named root lattices are
negative definite by construction (the AG convention).

These are owned-behavior proofs: the assertions pin the *sign* and the
*reflective* root definition, so they are not sign-invariant and cannot go
green under the pre-#5 norm-based, positive-default kernel.
"""
from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc


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
