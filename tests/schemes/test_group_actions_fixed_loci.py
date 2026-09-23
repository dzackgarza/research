r"""Affine group actions and their scheme-theoretic fixed loci."""


from dzack_research.preamble.all import (
    QQ,
    AffineGSchemes,
    Groups,
    Algebras,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_fixed_loci.sage",
    "live_owner": "tests/schemes/test_group_actions_fixed_loci.py",
    "disposition": "reconciled-live-owner",
}


def _coordinate_swap_action() -> tuple:
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
    return group, algebra, x, y, scheme, acted






def test_coordinate_swap_fixed_subscheme_is_the_diagonal_equalizer() -> None:
    group, algebra, x, y, _scheme, acted = _coordinate_swap_action()
    generator = group.group_generators()[0]

    assert acted.fixed_ideal() == algebra.ideal(x - y)

    fixed = acted.fixed_subscheme()
    inclusion = fixed.inclusion()
    quotient = inclusion.coordinate_algebra_morphism()

    assert fixed.inclusion().codomain() is acted
    assert inclusion.domain() is fixed
    assert inclusion.codomain() is acted
    assert quotient(x) == quotient(y)
    assert acted.action_of(generator) * inclusion == inclusion






def test_projective_product_sign_and_swap_fixed_loci_keep_archive_dimensions() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x0", "x1"))
    product = line.product_with(line)
    x0, x1 = line.coordinate_ring().gens()
    sign = line.projective_morphism_from_coordinates(line, (x0, -x1))

    diagonal_sign = product.from_product_cone(
        (sign * product.projection(0), sign * product.projection(1))
    )
    fixed_sign = diagonal_sign.fixed_subscheme()
    assert fixed_sign.dimension() == 0
    assert len(fixed_sign.rational_points()) == 4

    factor_swap = product.from_product_cone(
        (product.projection(1), product.projection(0))
    )
    fixed_swap = factor_swap.fixed_subscheme()
    assert fixed_swap.dimension() == 1
    assert factor_swap * factor_swap == product.categorical_identity_morphism()
