"""Affine invariant quotients compare with scalar field extension under Reynolds hypotheses."""

from dzack_research.preamble.all import (
    QQ,
    AffineGSchemes,
    Groups,
    Algebras,
)


def _swap_action():
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
    return group, acted






def test_affine_invariant_family_map_descends_through_same_universal_quotient() -> None:
    _group, acted = _swap_action()
    target_algebra = QQ.polynomial_ring("t")
    target = (target_algebra).affine_spectrum()
    source_algebra = acted.coordinate_algebra()
    x = source_algebra.algebra_generator("x")
    y = source_algebra.algebra_generator("y")
    family = acted.Mor(target)(
        target_algebra.Mor(source_algebra)({"t": x + y})
    )
    descended = acted.descend_invariant_family(family)

    assert descended.domain() is acted.affine_quotient()
    assert descended.codomain() is target
    assert descended * acted.quotient_morphism() == family
