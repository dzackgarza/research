
from dzack_research.preamble.all import (
    CartesianProductMorphism,
    CartesianProductOfSets,
    CoproductMorphism,
    CoproductOfSets,
    Sets,
    cardinal,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import (
    CartesianProductsOfSets,
    CoproductsOfSets,
)


def test_set_product_has_projection_and_pairing_universal_property() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    product = CartesianProductOfSets(x, y)
    assert product is CartesianProductOfSets(x, y)
    assert product.cardinality() == cardinal(6)

    source = Sets.Δ[2]
    f = Sets().Mor(source, x)(lambda value: x(value % 2))
    g = Sets().Mor(source, y)(lambda value: y(value))
    paired = product.from_maps(source, lambda index: f if index == 0 else g)
    for value in source:
        assert product.projection(0)(paired(value)) == f(value)
        assert product.projection(1)(paired(value)) == g(value)

    # Uniqueness: a map into a Set product is determined by every projection.
    competing = Sets().Mor(source, product)(lambda value: product((f(value), g(value))))
    for value in source:
        assert competing(value) == paired(value)


def test_set_coproduct_has_injection_and_copairing_universal_property() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    coproduct = CoproductOfSets(x, y)
    assert coproduct is CoproductOfSets(x, y)
    assert coproduct.cardinality() == cardinal(5)

    target = Sets.Δ[3]
    f = Sets().Mor(x, target)(lambda value: target(value))
    g = Sets().Mor(y, target)(lambda value: target(value + 1))
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
    left = Sets().Mor(x, y)(lambda value: y(value + 1))
    right = Sets().Mor(y, y)(lambda value: y(2 - value))
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


def test_dependent_product_and_coproduct_have_category_owned_constructors() -> None:
    labels = Sets.Δ[1]
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    family = indexed_family(
        labels,
        lambda index: left if int(index) == 0 else right,
    )

    product = CartesianProductsOfSets()(labels, family)
    coproduct = CoproductsOfSets()(labels, family)

    assert product.index_set() is labels
    assert product.factor(labels[0]) is left
    assert product.factor(labels[1]) is right
    assert coproduct.index_set() is labels
    assert coproduct.cofactor(labels[0]) is left
    assert coproduct.cofactor(labels[1]) is right


def test_finite_enumerated_product_exposes_its_mixed_radix_ranking_map() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    product = CartesianProductOfSets(left, right)
    ranking = product.ranking_map()
    expected = (
        (left(0), right(0)),
        (left(0), right(1)),
        (left(0), right(2)),
        (left(1), right(0)),
        (left(1), right(1)),
        (left(1), right(2)),
    )

    for position, coordinates in enumerate(expected):
        point = product(coordinates)
        assert int(ranking(point)) == position
        assert ranking.inverse()(position) == point


def test_finite_enumerated_product_equality_uses_the_selected_ranking() -> None:
    from sage.misc.unknown import Unknown

    class TriValuedLabel:
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            if self is other:
                return True
            return Unknown

        def __hash__(self):
            return hash(self.name)

    labels = Sets.Δ[1]
    left_value = TriValuedLabel("left")
    right_value = TriValuedLabel("right")
    factor = finite_ordered_image(
        labels,
        lambda index: left_value if int(index) == 0 else right_value,
        index_of=lambda value: labels[0] if value is left_value else labels[1] if value is right_value else None,
    )
    product = CartesianProductOfSets(factor, factor)
    first = product((left_value, right_value))
    same = product((left_value, right_value))
    different = product((right_value, left_value))

    assert first == same
    assert first != different
    assert {first: "same"}[same] == "same"


def test_equal_product_points_hash_identically_across_constructor_forms() -> None:
    left = Sets.Δ[1]
    right = Sets.Δ[2]
    product = CartesianProductOfSets(left, right)
    positional = product((left[1], right[2]))
    def component(index):
        match int(index):
            case 0:
                return left[1]
            case 1:
                return right[2]
            case _:
                raise ValueError("the binary product has only two components")

    functional = product(component)

    assert positional == functional
    assert hash(positional) == hash(functional)
    assert {positional: "same point"}[functional] == "same point"


def test_finite_product_equality_uses_component_equality_before_inverse_ranking() -> None:
    labels = Sets.Δ[1]
    inverse_calls = []

    def inverse_lookup(value):
        inverse_calls.append(value)
        return labels[int(value)]

    factor = finite_ordered_image(
        labels,
        lambda index: int(index),
        index_of=inverse_lookup,
    )
    product = CartesianProductOfSets(factor, factor)
    left = product((factor[0], factor[1]))
    same = product((factor[0], factor[1]))
    different = product((factor[1], factor[0]))
    inverse_calls.clear()

    assert left == same
    assert left != different
    assert inverse_calls == []
