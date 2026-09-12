r"""Quadratic versus bilinear finite-form distinctions retained from the archive.

Nikulin and Miranda--Morrison distinguish a finite quadratic form from its
polar bilinear form.  The rank-one sign pair and the elementary forms ``u_1``
and ``v_1`` are small specimens where the underlying finite groups and
bilinear forms agree while the quadratic refinements do not.
"""

from dzack_research.preamble.all import ZZ, Lattices


def test_rank_one_sign_pair_is_bilinearly_isomorphic_but_not_quadratically() -> None:
    positive = Lattices(ZZ)([[2]]).discriminant_group()
    negative = Lattices(ZZ)([[-2]]).discriminant_group()

    assert tuple(positive.invariants()) == tuple(negative.invariants()) == (2,)
    assert positive.associated_bilinear_form().is_isomorphic(
        negative.associated_bilinear_form()
    )
    assert not positive.is_isomorphic(negative)
    assert positive.is_anti_isometric(negative)


def test_u1_and_v1_share_the_bilinear_form_but_not_the_quadratic_refinement() -> None:
    u1 = Lattices(ZZ)([[0, 2], [2, 0]]).discriminant_group()
    v1 = Lattices.D4.discriminant_group()

    assert tuple(u1.invariants()) == tuple(v1.invariants()) == (2, 2)
    assert u1.associated_bilinear_form().is_isomorphic(
        v1.associated_bilinear_form()
    )
    assert not u1.is_isomorphic(v1)
    assert (u1.brown_invariant(), v1.brown_invariant()) == (0, 4)
