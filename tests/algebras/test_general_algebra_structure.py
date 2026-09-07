r"""The equipped-object prerequisite for the general algebra node.

Two multiplication morphisms on one exact module must define two distinct
structured objects without refining or reconstructing that module. Their
morphisms are single module maps whose tensor-square image is forced as the
left edge of the multiplication square.
"""

import pytest

from dzack_research.preamble.all import (
    BasedFreeModule,
    BilinearMap,
    EndofunctorAlgebras,
    Functor,
    Modules,
    QQ,
    tensor_product_morphism,
)
from dzack_research.preamble.categories.abstract_categories import TensorSquare
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


class _TensorSquareFunctor(Functor):
    r"""``M |-> M tensor M`` on the represented ``QQ``-modules in this specimen."""

    def __init__(self) -> None:
        modules = Modules(QQ)
        super().__init__(modules, modules)

    def _apply_object(self, module):
        return TensorSquare(module)

    def _apply_morphism(self, morphism):
        return tensor_product_morphism(
            morphism,
            morphism,
            source=self(morphism.domain()),
            target=self(morphism.codomain()),
        )


def _two_products_on_one_module():
    module = BasedFreeModule(QQ, finite_ordered_set(("1", "x")))
    one = module.module_generator("1")
    x = module.module_generator("x")
    tensor_square = TensorSquare(module)

    dual_numbers = tensor_square.from_bilinear(
        BilinearMap(
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
    )
    split_idempotent = tensor_square.from_bilinear(
        BilinearMap(
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
    )
    return module, dual_numbers, split_idempotent


def test_two_products_retain_one_exact_supplied_module() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    tensor_square = _TensorSquareFunctor()
    structures = EndofunctorAlgebras(tensor_square)
    x = module.module_generator("x")
    x_tensor_x = TensorSquare(module).pure_tensor(x, x)

    dual = structures.algebra(module, dual_numbers)
    split = structures.algebra(module, split_idempotent)
    forget = structures.forgetful()

    assert dual_numbers(x_tensor_x) == module.zero()
    assert split_idempotent(x_tensor_x) == x
    assert dual is not split
    assert structures.carrier(dual) is module
    assert structures.carrier(split) is module
    assert structures.structure(dual) is dual_numbers
    assert structures.structure(split) is split_idempotent
    assert forget(dual) is module
    assert forget(split) is module


def test_nonidentity_map_uses_its_forced_tensor_square() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    tensor_square = _TensorSquareFunctor()
    structures = EndofunctorAlgebras(tensor_square)
    dual = structures.algebra(module, dual_numbers)
    split = structures.algebra(module, split_idempotent)
    one = module.module_generator("1")
    projection = module_homset(module, module)(
        {"1": one, "x": module.zero()}
    )

    structured_projection = structures.homomorphism(
        split,
        dual,
        projection,
    )

    assert structured_projection.right() is projection
    assert structured_projection.left() == tensor_square(projection)
    assert structures.forgetful()(structured_projection) is projection
    assert projection * split_idempotent == dual_numbers * tensor_square(projection)

    identity = module_homset(module, module).identity()
    with pytest.raises(ValueError, match="does not commute"):
        structures.homomorphism(split, dual, identity)
