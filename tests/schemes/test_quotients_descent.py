r"""Descent of equivariant morphisms through an affine quotient.

The specimen is the coordinate swap of the affine plane over the rationals,
whose quotient is the spectrum of the symmetric invariants.  The diagonal
translation ``(x, y) -> (x + 1, y + 1)`` commutes with the swap, so it is an
equivariant automorphism, and it descends to the automorphism of the quotient
that sends the first symmetric function ``x + y`` to ``x + y + 2``.
"""

from dzack_research.preamble.all import (
    QQ,
    AffineGSchemes,
    GObjects,
    Groups,
    Schemes,
    Algebras,
)


def _swapped_plane():
    group = Groups.C(2)
    algebra = QQ.polynomial_ring(("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = (algebra).affine_spectrum()
    swap = Algebras(QQ).Associative().Unital().Commutative().spectrum()(algebra.Mor(algebra)({"x": y, "y": x}))
    identity = scheme.categorical_identity_morphism()
    acted = AffineGSchemes(group, QQ)(
        scheme,
        lambda element: identity if element == group.one() else swap,
    )
    return group, algebra, x, y, acted


def _label_of_the_first_symmetric_function(acted, x, y):
    invariant_algebra = acted.invariant_algebra()
    inclusion = acted.invariant_algebra_inclusion()
    return next(
        label
        for label in invariant_algebra.algebra_generating_set()
        if inclusion(invariant_algebra.algebra_generator(label)) == x + y
    )


def test_an_equivariant_translation_descends_to_the_symmetric_quotient() -> None:
    group, algebra, x, y, acted = _swapped_plane()
    one = algebra.one()
    translation = Algebras(QQ).Associative().Unital().Commutative().spectrum()(
        algebra.Mor(algebra)({"x": x + one, "y": y + one})
    )
    equivariant = GObjects(group, Schemes(QQ)).Mor(acted, acted)(translation)
    quotient_functor = GObjects(group, Schemes(QQ)).affine_quotient_functor()

    descended = quotient_functor(equivariant)
    quotient = acted.affine_quotient()
    assert quotient_functor(acted) is quotient
    assert descended.domain() is quotient
    assert descended.codomain() is quotient

    label = _label_of_the_first_symmetric_function(acted, x, y)
    invariant_algebra = acted.invariant_algebra()
    inclusion = acted.invariant_algebra_inclusion()
    image = descended.coordinate_algebra_morphism()(
        invariant_algebra.algebra_generator(label)
    )
    assert inclusion(image) == x + y + one + one


