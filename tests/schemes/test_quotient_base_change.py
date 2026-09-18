"""Affine invariant quotients compare with scalar field extension under Reynolds hypotheses."""

from dzack_research.preamble.all import (
    GF,
    QQ,
    AffineGSchemes,
    Groups,
    QuadraticField,
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


def test_invariant_quotient_base_change_has_canonical_comparison_and_reynolds_isomorphism() -> None:
    group, acted = _swap_action()
    field = QuadraticField(2, "s")
    extension = QQ.Mor(field)(lambda element: field(element))
    comparison = acted.quotient_base_change_comparison(extension)
    arrow = comparison.comparison_morphism()
    isomorphism = comparison.reynolds_isomorphism()

    assert arrow is comparison
    assert comparison.reynolds_hypothesis_holds()
    assert arrow.domain() is comparison.quotient_after_base_change()
    assert arrow.codomain() is comparison.base_change_after_quotient()
    assert isomorphism.forward() is arrow
    assert isomorphism.inverse().domain() is comparison.base_change_after_quotient()
    assert isomorphism.inverse().codomain() is comparison.quotient_after_base_change()
    assert comparison.base_changed_acted_scheme().scheme_base_ring() is field


def test_reynolds_base_change_hypothesis_refuses_modular_characteristic() -> None:
    group = Groups.C(2)
    field = GF(2)

    assert group.order_is_invertible_in(field) is False


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
