r"""Affine group schemes and their scheme-theoretic actions."""


from dzack_research.preamble.all import (
    QQ,
    AffineGroupSchemes,
    Grp,
    Schemes,
)








def test_additive_and_multiplicative_group_schemes_use_internal_group_objects() -> None:
    additive = AffineGroupSchemes(QQ).additive_group()
    multiplicative = AffineGroupSchemes(QQ).multiplicative_group()

    assert additive.internal_group_object() in Grp(Schemes(QQ).Affine())
    assert multiplicative.internal_group_object() in Grp(Schemes(QQ).Affine())

    x = additive.scheme().coordinate_algebra().algebra_generator("x")
    additive_square = additive.multiplication().domain()
    additive_pullback = additive.multiplication().coordinate_algebra_morphism()
    assert additive_pullback(x) == (
        additive_square.projection(0).coordinate_algebra_morphism()(x)
        + additive_square.projection(1).coordinate_algebra_morphism()(x)
    )

    u = multiplicative.scheme().coordinate_algebra().algebra_generator("u")
    multiplicative_square = multiplicative.multiplication().domain()
    multiplicative_pullback = multiplicative.multiplication().coordinate_algebra_morphism()
    assert multiplicative_pullback(u) == (
        multiplicative_square.projection(0).coordinate_algebra_morphism()(u)
        * multiplicative_square.projection(1).coordinate_algebra_morphism()(u)
    )
    assert multiplicative.inverse_morphism().coordinate_algebra_morphism()(u) == u**-1




