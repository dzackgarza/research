from dzack_research.preamble.all import (
    QQ,
    Algebras,
    BilinearMap,
    finite_ordered_set,
)


def _rank_two_module():
    return QQ.free_module(finite_ordered_set(("one", "x")))


def _multiplication(module, square_of_x):
    one = module.module_generator("one")
    x = module.module_generator("x")
    return BilinearMap(
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


