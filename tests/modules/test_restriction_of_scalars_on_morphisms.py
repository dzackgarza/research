r"""``Res_f`` acts on morphisms by the identity.

Restriction of scalars along ``f: R -> S`` changes which ring acts and never
the underlying map, so ``Res_f(g)`` is ``g``: it sends the reading of ``x`` in
``Res_f(M)`` to the reading of ``g(x)`` in ``Res_f(N)``.  This holds whether or
not the restricted module carries a framing, and ``Res(QQ^2)`` over ``ZZ``
carries none.

Unverified: written without running the suite.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FreeModule,
    Modules,
    module_homset,
)


def _swap_of_the_rational_plane():
    r"""``QQ^2`` and the endomorphism exchanging its two basis vectors."""
    plane = FreeModule(QQ, 2)
    e0, e1 = plane.module_generator(0), plane.module_generator(1)
    return plane, module_homset(plane, plane)({0: e1, 1: e0})


def test_restricting_a_rational_endomorphism_to_the_integers_keeps_its_action() -> None:
    r"""``Res(g)`` runs between the restricted parents and acts as ``g`` does."""
    plane, swap = _swap_of_the_rational_plane()
    e0, e1 = plane.module_generator(0), plane.module_generator(1)
    restriction = Modules(QQ).restriction_of_scalars(ZZ.Mor(QQ)(lambda element: QQ(element)))
    space = restriction(plane)

    restricted_swap = restriction(swap)

    assert restricted_swap.domain() is space
    assert restricted_swap.codomain() is space
    assert restricted_swap(space(e0)) == space(e1)
    assert restricted_swap(space(2 * e0 + 3 * e1)) == space(3 * e0 + 2 * e1)
    assert restricted_swap(space(plane.scalar_multiple(QQ(1) / 2, e0))) == space(
        plane.scalar_multiple(QQ(1) / 2, e1)
    )


def test_restricting_along_the_identity_keeps_the_action_of_the_endomorphism() -> None:
    r"""``Res_id(g)`` is ``g`` as well, on a restriction that does carry a framing."""
    plane, swap = _swap_of_the_rational_plane()
    e0, e1 = plane.module_generator(0), plane.module_generator(1)
    restriction = Modules(QQ).restriction_of_scalars(QQ.Mor(QQ)(lambda element: element))
    space = restriction(plane)

    restricted_swap = restriction(swap)

    assert restricted_swap.domain() is space
    assert restricted_swap.codomain() is space
    assert restricted_swap(space(e0)) == space(e1)
    assert restricted_swap(space(2 * e0 + 3 * e1)) == space(3 * e0 + 2 * e1)
