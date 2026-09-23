r"""The equipped-object prerequisite for the general algebra node.

Two multiplication morphisms on one exact module must define two distinct
structured objects without refining or reconstructing that module. Their
morphisms are single module maps whose tensor-square image is forced as the
left edge of the multiplication square.
"""

import pytest

from dzack_research.preamble.all import (
    Algebras,
    BilinearMap,
    Modules,
    QQ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set




def _two_products_on_one_module():
    module = QQ.free_module(finite_ordered_set(("1", "x")))
    one = module.module_generator("1")
    x = module.module_generator("x")
    dual_numbers = BilinearMap(
        module,
        module,
        module,
        {
            ("1", "1"): one,
            ("1", "x"): x,
            ("x", "1"): x,
            ("x", "x"): module.zero(),
        },
    )
    split_idempotent = BilinearMap(
        module,
        module,
        module,
        {
            ("1", "1"): one,
            ("1", "x"): x,
            ("x", "1"): x,
            ("x", "x"): x,
        },
    )
    return module, dual_numbers, split_idempotent






def test_general_algebra_node_builds_one_module_per_product() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    algebras = Algebras(QQ)
    dual = algebras(module, dual_numbers)
    split = algebras(module, split_idempotent)
    forget = Algebras(QQ).underlying_module()

    assert dual is not split
    assert dual in algebras
    assert split in algebras
    assert dual in Modules(QQ)
    assert dual not in algebras.Associative().Unital()
    assert split not in algebras.Associative().Unital()
    assert forget(dual) is dual
    assert dual.underlying_module() is dual
    assert dual.unformed_module() is module
    assert dual.multiplication() is dual_numbers
    assert split.multiplication() is split_idempotent

    one = dual.module_generator("1")
    x = dual.module_generator("x")
    assert dual.scalar_multiple(QQ(2), x) == x + x
    assert x * x == dual.zero()
    assert one * x == x
    y = split.module_generator("x")
    assert y * y == y
    assert dual(module.module_generator("x")) == x
    assert module(x) == module.module_generator("x")
    multiplication = dual.multiplication_morphism()
    assert multiplication.codomain() is dual
    assert multiplication(multiplication.domain().pure_tensor(x, x)) == dual.zero()

    projection = split.module_category().Mor(split, dual)(
        {"1": one, "x": dual.zero()}
    )
    structured_projection = algebras.Mor(split, dual)(projection)

    assert structured_projection.underlying_morphism() is projection
    assert forget(structured_projection) is projection
    assert structured_projection(split.module_generator("x")) == dual.zero()
    assert structured_projection(split.module_generator("1")) == one
    assert projection * split.multiplication_morphism() == (
        multiplication * structured_projection.tensor_square_morphism()
    )

    renaming = split.module_category().Mor(split, dual)({"1": one, "x": x})
    with pytest.raises(AssertionError, match="preserve the multiplication"):
        algebras.Mor(split, dual)(renaming)


def test_general_algebra_node_does_not_impose_associativity_or_unit() -> None:
    module = QQ.free_module(finite_ordered_set(("a", "b")))
    a = module.module_generator("a")
    b = module.module_generator("b")
    multiplication = BilinearMap(
        module,
        module,
        module,
        {
            ("a", "a"): b,
            ("b", "a"): a,
            ("a", "b"): module.zero(),
            ("b", "b"): module.zero(),
        },
    )
    algebra = Algebras(QQ)(module, multiplication)
    a = algebra.module_generator("a")
    b = algebra.module_generator("b")

    assert b * a == a
    assert a * b == algebra.zero()
    assert (a * a) * a == a
    assert a * (a * a) == algebra.zero()
    assert algebra.underlying_module() is algebra
    assert algebra.multiplication() is multiplication
    assert algebra not in Algebras(QQ).Associative().Unital()


















