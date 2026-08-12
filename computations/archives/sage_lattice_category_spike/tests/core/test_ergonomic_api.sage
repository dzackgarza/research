r"""Ergonomic API items absorbed into issue #5 (originally #10/#14/#16/#17):
variadic/operator direct sums, the identity morphism, the standard
``invariant_factors`` name on discriminant groups, and an informative repr.

Assertions are sign-agnostic (rank/det/parity/disc), so they hold both before
and after the AG negative-definite default flip.
"""
from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc
from sage.all import ZZ, identity_matrix


def test_identity_morphism_is_the_identity_isometry():
    A2 = lc.Lattice("A2")
    idm = A2.identity_morphism()
    assert idm.domain() is A2
    assert idm.codomain() is A2
    assert idm.matrix() == identity_matrix(ZZ, 2)


def test_discriminant_group_invariant_factors_names_the_invariants():
    D4 = lc.Lattice("D4")
    group = D4.discriminant_group()
    assert group.invariant_factors() == group.invariants()
    assert group.invariant_factors() == (2, 2)


def test_direct_sum_is_variadic_and_agrees_with_operators():
    U = lc.Lattice("U")
    variadic = U.direct_sum(U, U)
    operator = U + U + U
    reduced = sum([U, U, U])
    assert variadic.rank() == 6
    assert operator.gram_matrix() == variadic.gram_matrix()
    assert reduced.gram_matrix() == variadic.gram_matrix()


def test_signature_returns_the_pair_p_q_not_the_integer():
    r"""#9: ``signature()`` is the pair ``(p, q)`` (positive index, negative
    index), not the integer ``p - q`` it inherited from Sage. The classical
    integer ``p - q`` is derived, never the name of the method."""
    A2 = lc.Lattice("A2")
    sig = A2.signature()
    assert isinstance(sig, tuple) and len(sig) == 2
    assert sig == A2.signature_pair()
    assert sig != sig[0] - sig[1]   # a pair, not the old integer p - q


def test_repr_shows_mathematical_invariants_not_just_rank_and_ring():
    E8 = lc.Lattice("E8")
    text = repr(E8)
    assert "rank 8" in text
    assert "det 1" in text
    assert "even" in text
    assert "unimodular" in text
    a2_text = repr(lc.Lattice("A2"))
    assert "rank 2" in a2_text
    assert "det 3" in a2_text
    assert "disc (3,)" in a2_text
