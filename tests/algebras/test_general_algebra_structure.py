r"""The equipped-object prerequisite for the general algebra node.

Two multiplication morphisms on one exact module must define two distinct
structured objects without refining or reconstructing that module. Their
morphisms are single module maps whose tensor-square image is forced as the
left edge of the multiplication square.
"""

import pytest

from dzack_research.preamble.all import (
    Algebras,
    AssociativeAlgebras,
    BasedFreeModule,
    BilinearMap,
    CommutativeAlgebras,
    EndofunctorAlgebras,
    Functor,
    Modules,
    QQ,
    tensor_product_morphism,
)
from dzack_research.preamble.categories.algebras.algebras import (
    _unit_morphism_from_element,
)
from dzack_research.preamble.categories.abstract_categories import TensorSquare
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
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


def test_general_algebra_node_uses_exact_carriers_and_common_hom() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    algebras = Algebras(QQ)
    dual = algebras(module, dual_numbers)
    split = algebras(module, split_idempotent)
    forget = algebra_underlying_module_functor(QQ)

    assert dual is not split
    assert dual in algebras
    assert split in algebras
    assert dual not in algebras.Associative().Unital()
    assert split not in algebras.Associative().Unital()
    assert dual.underlying_module() is module
    assert split.underlying_module() is module
    assert dual.multiplication_morphism() is dual_numbers
    assert split.multiplication_morphism() is split_idempotent
    assert forget(dual) is module
    assert forget(split) is module
    x = module.module_generator("x")
    assert dual.scalar_multiple(QQ(2), x).underlying_element() == module.scalar_multiple(QQ(2), x)
    assert dual.product(x, x).underlying_element() == module.zero()
    assert split.product(x, x).underlying_element() == x

    one = module.module_generator("1")
    projection = module_homset(module, module)(
        {"1": one, "x": module.zero()}
    )
    structured_projection = algebras.Mor(split, dual)(projection)

    assert structured_projection.right() is projection
    assert forget(structured_projection) is projection
    assert (
        structured_projection(split(module.module_generator("x"))).underlying_element()
        == module.zero()
    )
    assert projection * split_idempotent == dual_numbers * structured_projection.left()

    identity = module_homset(module, module).identity()
    with pytest.raises(ValueError, match="does not commute"):
        algebras.Mor(split, dual)(identity)


def test_general_algebra_node_does_not_impose_associativity_or_unit() -> None:
    module = BasedFreeModule(QQ, finite_ordered_set(("a", "b")))
    a = module.module_generator("a")
    b = module.module_generator("b")
    tensor_square = TensorSquare(module)
    multiplication = tensor_square.from_bilinear(
        BilinearMap(
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
    )
    algebra = Algebras(QQ)(module, multiplication)

    assert multiplication(tensor_square.pure_tensor(b, a)) == a
    assert multiplication(tensor_square.pure_tensor(a, b)) == module.zero()
    assert algebra.underlying_module() is module
    assert algebra.multiplication_morphism() is multiplication
    assert algebra not in Algebras(QQ).Associative().Unital()


def test_algebra_axiom_placement_and_module_forgetting_are_distinct() -> None:
    algebras = Algebras(QQ)

    assert not algebras.is_subcategory(Modules(QQ))
    assert AssociativeAlgebras(QQ).is_subcategory(algebras)
    assert algebras.Associative().Unital().is_subcategory(algebras.Unital())
    assert CommutativeAlgebras(QQ).is_subcategory(
        algebras.Associative().Unital()
    )
    assert CommutativeAlgebras(QQ).is_subcategory(algebras.Commutative())


def test_unital_refinement_retains_eta_and_strengthens_the_hom() -> None:
    module, dual_numbers, _split_idempotent = _two_products_on_one_module()
    one = module.module_generator("1")
    scalar_module = algebra_underlying_module_functor(QQ)(QQ)
    assert scalar_module in Modules(QQ)
    eta = _unit_morphism_from_element(module, one, QQ)
    unital = Algebras(QQ).Unital()(module, dual_numbers, eta)

    assert unital.underlying_module() is module
    assert unital.unit_morphism() is eta
    assert unital.one().underlying_element() == one
    x = unital(module.module_generator("x"))
    assert unital.one() * x == x
    assert x * unital.one() == x

    zero = module_homset(module, module)(
        {"1": module.zero(), "x": module.zero()}
    )
    general = Algebras(QQ)(module, dual_numbers)
    assert Algebras(QQ).Mor(general, general)(zero).right() is zero
    with pytest.raises(ValueError, match="does not preserve the unit"):
        Algebras(QQ).Unital().Mor(unital, unital)(zero)
