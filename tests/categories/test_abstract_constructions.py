
from dzack_research.preamble.all import Cat, Sets


def test_opposite_category_reverses_arrows_and_composition() -> None:
    a = Sets.Δ[2]
    b = Sets.Δ[1]
    c = Sets.Δ[0]
    f = Sets().Mor(a, b)(lambda x: b(min(int(x), 1)))
    g = Sets().Mor(b, c)(lambda _x: c(0))

    opposite = Sets().opposite()
    op_a = opposite(a)
    op_b = opposite(b)
    op_c = opposite(c)
    op_f = opposite.Mor(op_b, op_a)(f)
    op_g = opposite.Mor(op_c, op_b)(g)

    composite = op_f * op_g
    assert composite.domain() is op_c
    assert composite.codomain() is op_a
    for element in a:
        assert composite.underlying_arrow()(element) == g(f(element))
    identity = opposite.identity(op_a)
    assert (identity * op_f).underlying_arrow()(a(2)) == f(a(2))


def test_product_category_has_componentwise_homs_identities_and_composition() -> None:
    category = Cat().product([Sets(), Sets()])
    left = category(Sets.Δ[2], Sets.Δ[1])
    middle = category(Sets.Δ[1], Sets.Δ[2])
    right = category(Sets.Δ[0], Sets.Δ[0])

    f1 = Sets().Mor(left.first(), middle.first())(lambda x: middle.first()(min(int(x), 1)))
    f2 = Sets().Mor(left.second(), middle.second())(lambda x: middle.second()(int(x) + 1))
    g1 = Sets().Mor(middle.first(), right.first())(lambda _x: right.first()(0))
    g2 = Sets().Mor(middle.second(), right.second())(lambda _x: right.second()(0))

    f = category.Mor(left, middle)(f1, f2)
    g = category.Mor(middle, right)(g1, g2)
    composite = g * f
    assert composite.domain() is left
    assert composite.codomain() is right
    assert composite.first()(left.first()(2)) == right.first()(0)
    assert composite.second()(left.second()(1)) == right.second()(0)
    identity = category.identity(left)
    assert identity.first()(left.first()(2)) == left.first()(2)
    assert identity.second()(left.second()(1)) == left.second()(1)


def test_arrow_subcategories_and_isomorphism_constructor_have_the_expected_objects() -> None:
    from dzack_research.preamble.all import (
        Sets,
        WideSubcategory,
    )

    x = Sets.Δ[2]
    y = Sets.Δ[4]
    inclusion = Sets().Mono(x, y)(lambda value: y(int(value) + 1))
    arrows = Sets().ArrowCategory()
    inclusion_object = arrows(inclusion)
    assert inclusion_object in arrows
    assert Cat().join((x.category(), y.category())).is_subcategory(Sets())

    end = Sets().Mor(x, x)(lambda value: x(2 - int(value)))
    end_object = Sets().EndArrowCategory()(end)
    assert end_object in Sets().EndArrowCategory()

    inverse = end
    isomorphism = Sets().Core().Mor(x, x)(end, inverse)
    core = Sets().Core()
    assert isomorphism in core.Mor(x, x)
    iso_object = Sets().IsoArrowCategory()(isomorphism)
    aut_object = Sets().AutomorphismArrowCategory()(isomorphism)
    assert iso_object in Sets().IsoArrowCategory()
    assert aut_object in Sets().AutomorphismArrowCategory()

    injections = WideSubcategory(Sets(), Sets().MonomorphismArrowCategory())
    assert injections.admits(inclusion)
