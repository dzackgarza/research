
from dzack_research.preamble.all import (
    CartesianProductMorphism,
    CartesianProductOfSets,
    CoproductMorphism,
    CoproductOfSets,
    Sets,
    cardinal,
)


def test_set_product_has_projection_and_pairing_universal_property() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    product = CartesianProductOfSets(x, y)
    assert product is CartesianProductOfSets(x, y)
    assert product.cardinality() == cardinal(6)

    source = Sets.Δ[2]
    f = Sets().hom(source, x)(lambda value: x(value % 2))
    g = Sets().hom(source, y)(lambda value: y(value))
    paired = product.from_maps(source, lambda index: f if index == 0 else g)
    for value in source:
        assert product.projection(0)(paired(value)) == f(value)
        assert product.projection(1)(paired(value)) == g(value)

    # Uniqueness: a map into a Set product is determined by every projection.
    competing = Sets().hom(source, product)(lambda value: product((f(value), g(value))))
    for value in source:
        assert competing(value) == paired(value)


def test_set_coproduct_has_injection_and_copairing_universal_property() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    coproduct = CoproductOfSets(x, y)
    assert coproduct is CoproductOfSets(x, y)
    assert coproduct.cardinality() == cardinal(5)

    target = Sets.Δ[3]
    f = Sets().hom(x, target)(lambda value: target(value))
    g = Sets().hom(y, target)(lambda value: target(value + 1))
    copaired = coproduct.from_maps(target, lambda index: f if index == 0 else g)
    for value in x:
        assert copaired(coproduct.injection(0)(value)) == f(value)
    for value in y:
        assert copaired(coproduct.injection(1)(value)) == g(value)


def test_product_and_coproduct_morphisms_act_componentwise() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    xx = CartesianProductOfSets(x, y)
    yy = CartesianProductOfSets(y, y)
    left = Sets().hom(x, y)(lambda value: y(value + 1))
    right = Sets().hom(y, y)(lambda value: y(2 - value))
    carried = CartesianProductMorphism(xx, yy, lambda index: left if index == 0 else right)
    element = xx((x(0), y(1)))
    assert carried(element)[0] == y(1)
    assert carried(element)[1] == y(1)

    source_sum = CoproductOfSets(x, y)
    target_sum = CoproductOfSets(y, y)
    carried_sum = CoproductMorphism(
        source_sum, target_sum, lambda index: left if index == 0 else right
    )
    image = carried_sum(source_sum.injection(0)(x(1)))
    assert image.summand_index() == 0
    assert image.summand_element() == y(2)
