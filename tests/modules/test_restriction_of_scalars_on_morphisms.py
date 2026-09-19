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
    Modules,
)


def _swap_of_the_rational_plane():
    r"""``QQ^2`` and the endomorphism exchanging its two basis vectors."""
    plane = QQ.free_module(2)
    e0, e1 = plane.module_generator(0), plane.module_generator(1)
    return plane, plane.module_category().Mor(plane, plane)({0: e1, 1: e0})


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



def test_finite_scalar_restriction_retains_selected_presentation_for_kernels_and_images() -> None:
    from dzack_research.preamble.all import (
        GF,
        ModulesWithChosenFinitePresentation,
    )

    prime = GF(2)
    presentation = prime.free_module(("x",)).symmetric_algebra()
    x = presentation.algebra_generator("x")
    extension = (presentation).quotient_by_relations((x**2,))
    ring_map = prime.Mor(extension)(lambda scalar: extension(scalar))
    line = extension.free_module(1)
    restricted = Modules(extension).restriction_of_scalars(ring_map)(line)

    assert restricted in ModulesWithChosenFinitePresentation(prime)
    assert restricted.presentation().codomain().base_ring() is prime

    identity = restricted.module_category().Mor(restricted, restricted).identity()
    kernel = identity.kernel()
    image = identity.image()

    assert kernel.is_zero()
    assert image.inclusion().codomain() is restricted

def test_finite_scalar_restriction_coefficients_keep_distinct_product_labels_under_addition() -> None:
    from dzack_research.preamble.all import GF

    prime = GF(2)
    presentation = prime.free_module(("x",)).symmetric_algebra()
    x = presentation.algebra_generator("x")
    extension = (presentation).quotient_by_relations((x**2,))
    ring_map = prime.Mor(extension)(lambda scalar: extension(scalar))
    line = extension.free_module(1)
    restricted = Modules(extension).restriction_of_scalars(ring_map)(line)
    labels = tuple(restricted.module_generating_set())

    framing = restricted.framing_morphism()
    assert restricted.framing_source().module_generating_set() is restricted.module_generating_set()
    assert restricted.framing_morphism() is framing
    assert framing.domain() is restricted.framing_source()
    assert framing.codomain() is restricted
    assert len(labels) == 2
    for label in labels:
        assert restricted.module_generator(label) == framing(
            restricted.framing_source().module_generator(label)
        )
    total = restricted.module_generator(labels[0]) + restricted.module_generator(labels[1])
    coefficients = restricted.framing_coefficients(total)

    assert len(coefficients) == 2
    assert coefficients[labels[0]] == prime.one()
    assert coefficients[labels[1]] == prime.one()
