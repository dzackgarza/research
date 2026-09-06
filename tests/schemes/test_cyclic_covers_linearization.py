r"""The deck linearization of a cyclic cover and its fibres over the base.

Pushing the structure sheaf of a cyclic cover forward gives the ``O_X``-module
``pi_* O_Y = ⊕_{i<n} L^{-i}`` together with the deck action, and the grading of
the cover algebra is that action's eigen-decomposition.  The specimens here
read it off two covers.

The double cover ``z^2 = x^4 - 1`` of the affine line over the rationals is the
affine chart of a genus-one curve.  Its deck involution fixes the summand
``A``, negates the summand ``A z``, and the fibre over a root of the branch
section is where the two sheets collide: exactly the points at which the deck
action is no longer free.

The degree-three cover ``z^3 = x`` over ``GF(7)`` separates the two candidate
actions on sections, which the involution cannot.  Pullback along the deck
automorphism scales ``z`` by ``zeta``, while the left action of the same group
element on sections is pullback along its inverse and scales ``z`` by
``zeta^{-1}``.  For ``n = 2`` those agree; for ``n = 3`` they do not, so a
construction that composed pullbacks the wrong way round is visible here.
"""

from dzack_research.preamble.all import GF, PolynomialRing, QQ
from dzack_research.preamble.categories.schemes.cyclic_covers import CyclicCovers
from dzack_research.preamble.categories.schemes.quotients import (
    AffineSectionModuleFunctor,
)


def test_the_deck_action_splits_the_cover_sections_by_the_powers_of_z() -> None:
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    covers = CyclicCovers(algebra, 2)
    cover = covers(x**4 - algebra.one())
    generator = covers.deck_group().group_generators()[0]
    sections = AffineSectionModuleFunctor(
        covers.deck_group(),
        algebra,
    ).object_image(cover)

    trivial_summand = sections.module_generator(0)
    sign_summand = sections.module_generator(1)

    assert sections.base_ring() is algebra
    assert sections.act(generator, trivial_summand) == trivial_summand
    assert sections.act(generator, sign_summand) == -sign_summand
    assert sections.act(generator, sections.act(generator, sign_summand)) == sign_summand


def test_the_action_on_sections_is_pullback_along_the_inverse() -> None:
    algebra = PolynomialRing(GF(7), "x")
    x = algebra.algebra_generator("x")
    covers = CyclicCovers(algebra, 3)
    cover = covers(x)
    generator = covers.deck_group().group_generators()[0]
    root_of_unity = covers.deck_root_of_unity()
    sections_functor = AffineSectionModuleFunctor(covers.deck_group(), algebra)
    sections = sections_functor.object_image(cover)

    deck = cover.Mor(cover)(cover.action_of(generator))
    pullback = sections_functor.morphism_image(deck)
    sign_summand = sections.module_generator(1)

    assert root_of_unity**3 == root_of_unity.parent().one()
    assert root_of_unity != root_of_unity.parent().one()
    assert pullback(sign_summand) == sections.scalar_multiple(
        algebra(root_of_unity),
        sign_summand,
    )
    assert sections.act(generator, sign_summand) == sections.scalar_multiple(
        algebra(root_of_unity**2),
        sign_summand,
    )
    assert sections.act(generator, sign_summand) != pullback(sign_summand)


def test_the_fibre_over_a_branch_point_carries_the_collided_sheets() -> None:
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    cover = CyclicCovers(algebra, 2)(x**4 - algebra.one())
    cover_algebra = cover.coordinate_algebra()

    ramified = cover_algebra.base_change(algebra.Mor(QQ)({"x": QQ(1)}))
    unramified = cover_algebra.base_change(algebra.Mor(QQ)({"x": QQ(0)}))

    # The branch section vanishes at x = 1, so z is a nonzero nilpotent in the
    # fibre: the two sheets have collided at the deck fixed point.
    assert ramified.algebra_generator("z") ** 2 == ramified.zero()
    assert ramified.algebra_generator("z") != ramified.zero()
    # At x = 0 the branch section is the unit -1, so z^2 = -1 is a unit and the
    # deck involution exchanges two distinct points of the fibre.
    assert unramified.algebra_generator("z") ** 2 == -unramified.one()
