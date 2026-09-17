from dzack_research.preamble.all import (
    QQ,
    AdditiveGroups,
    Algebras,
    BilinearMap,
    Modules,
    finite_ordered_set,
)


def _rank_two_module():
    return QQ.free_module(finite_ordered_set(("one", "x")))


def _multiplication(module, square_of_x):
    one = module.module_generator("one")
    x = module.module_generator("x")
    return Modules(QQ).tensor_product((module, module)).from_bilinear(
        BilinearMap(
            module,
            module,
            module,
            {
                ("one", "one"): one,
                ("one", "x"): x,
                ("x", "one"): x,
                ("x", "x"): square_of_x,
            },
        )
    )


def test_two_multiplications_on_one_supplied_module_remain_distinct_structures() -> None:
    module = _rank_two_module()
    zero_square = _multiplication(module, module.zero())
    idempotent_square = _multiplication(module, module.module_generator("x"))

    dual_numbers = Algebras(QQ)(module, zero_square)
    idempotent_algebra = Algebras(QQ)(module, idempotent_square)

    assert dual_numbers is not idempotent_algebra
    assert dual_numbers.unformed_module() is module
    assert idempotent_algebra.unformed_module() is module
    assert dual_numbers.multiplication() is zero_square
    assert idempotent_algebra.multiplication() is idempotent_square

    dual_x = dual_numbers.module_generator("x")
    idempotent_x = idempotent_algebra.module_generator("x")
    assert dual_x * dual_x == dual_numbers.zero()
    assert idempotent_x * idempotent_x == idempotent_x


def test_noncommutative_regular_module_action_lands_in_additive_endomorphisms() -> None:
    ring = QQ.matrix_space(2)
    additive = AdditiveGroups().AdditiveCommutative()
    endomorphisms = additive.End(ring)
    action = ring.Mor(endomorphisms)(
        lambda scalar: endomorphisms.elementwise(
            lambda element: scalar * element,
        ),
    )
    regular = Modules(ring)(action)

    assert regular.base_ring() is ring
    assert regular.scalar_action() is action
    assert action.domain() is ring
    assert action.codomain() is endomorphisms

    left = ring([[0, 1], [0, 0]])
    right = ring([[0, 0], [1, 0]])
    assert left * right != right * left
    assert action(left)(right) == left * right
    assert action(right)(left) == right * left
