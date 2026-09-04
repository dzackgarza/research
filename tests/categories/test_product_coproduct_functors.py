
from dzack_research.preamble.all import BasedFreeModule, Sets, ZZ, module_homset
from dzack_research.preamble.categories.abstract_categories.functors import (
    CoproductFunctor,
    DiagonalFunctor,
    ProductFunctor,
)
from dzack_research.preamble.categories.modules import FinitelyPresentedModules
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_binary_set_product_coproduct_and_diagonal_are_functorial() -> None:
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    z = Sets.Δ[3]
    product = ProductFunctor(Sets())
    coproduct = CoproductFunctor(Sets())
    diagonal = DiagonalFunctor(Sets())

    pair = product.domain()(x, y)
    product_xy = product(pair)
    coproduct_xy = coproduct(pair)
    assert product_xy.cardinality() == 6
    assert coproduct_xy.cardinality() == 5

    fx = Sets().mor(x, y)(lambda value: y(int(value) + 1))
    fy = Sets().mor(y, z)(lambda value: z(int(value) + 1))
    target_pair = product.domain()(y, z)
    pair_map = product.domain().mor(pair, target_pair)(fx, fy)
    carried = product(pair_map)
    element = product_xy((x(0), y(1)))
    assert carried(element)[0] == y(1)
    assert carried(element)[1] == z(2)

    carried_sum = coproduct(pair_map)
    assert carried_sum(coproduct_xy.injection(0)(x(1))).summand_element() == y(2)

    diagonal_map = diagonal(fx)
    assert diagonal_map.first() is fx
    assert diagonal_map.second() is fx


def test_module_product_and_coproduct_reuse_the_same_biproduct_object() -> None:
    category = FinitelyPresentedModules(ZZ)
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    product = ProductFunctor(category)
    coproduct = CoproductFunctor(category)
    pair = product.domain()(left, right)
    product_object = product(pair)
    coproduct_object = coproduct(pair)
    assert product_object is coproduct_object

    left_map = module_homset(left, left)({"x": 2 * left.module_generator("x")})
    right_map = module_homset(right, right)({"y": 3 * right.module_generator("y")})
    pair_map = product.domain().mor(pair, pair)(left_map, right_map)
    carried = product(pair_map)
    assert product_object.left_projection()(
        carried(product_object.left_inclusion()(left.module_generator("x")))
    ) == 2 * left.module_generator("x")


def test_infinite_dependent_product_accepts_callable_sections_without_enumeration() -> None:
    from dzack_research.preamble.categories.sets import CartesianProductOfFamily, NN

    bit = Sets.Δ[1]
    product = CartesianProductOfFamily(NN, lambda _index: bit)
    section = product(lambda index: bit(int(index) % 2))

    assert section[NN(0)] == bit(0)
    assert section[NN(1000)] == bit(0)
    assert "Section of" in repr(section)
    try:
        product((bit(0), bit(1)))
    except TypeError as error:
        assert "callable section" in str(error)
    else:
        raise AssertionError("an infinite product must not interpret a finite sequence as a total section")


def test_infinite_free_module_biproduct_uses_tagged_lazy_framing() -> None:
    from dzack_research.preamble.categories.abstract_categories import Biproduct
    from dzack_research.preamble.categories.sets import NN

    left = BasedFreeModule(ZZ, NN)
    right = BasedFreeModule(ZZ, NN)
    direct_sum = Biproduct(left, right)
    e5 = left.module_generator(NN(5))
    f7 = right.module_generator(NN(7))

    assert direct_sum.left_projection()(direct_sum.left_inclusion()(e5)) == e5
    assert direct_sum.right_projection()(direct_sum.right_inclusion()(f7)) == f7
    assert direct_sum.left_projection()(direct_sum.right_inclusion()(f7)) == left.zero()
