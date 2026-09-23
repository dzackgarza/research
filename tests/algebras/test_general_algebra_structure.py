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
    Functor,
    GF,
    Modules,
    QQ,
)
from dzack_research.preamble.categories.algebras.algebras import (
    _unit_morphism_from_element,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


class _TensorSquareFunctor(Functor):
    r"""``M |-> M tensor M`` on the represented ``QQ``-modules in this specimen."""

    def __init__(self) -> None:
        modules = Modules(QQ)
        super().__init__(modules, modules)

    def _apply_object(self, module):
        return Modules(QQ).tensor_product((module, module))

    def _apply_morphism(self, morphism):
        return morphism.tensor_product_map(
            morphism,
            source=self(morphism.domain()),
            target=self(morphism.codomain()),
        )


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


def test_two_products_retain_one_exact_supplied_module() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    tensor_square = _TensorSquareFunctor()
    structures = tensor_square.algebras()
    x = module.module_generator("x")
    x_tensor_x = Modules(QQ).tensor_product((module, module)).pure_tensor(x, x)

    dual = structures.algebra(module, dual_numbers)
    split = structures.algebra(module, split_idempotent)
    forget = structures.forgetful()

    assert dual_numbers(x_tensor_x) == module.zero()
    assert split_idempotent(x_tensor_x) == x
    assert dual is not split
    assert structures.underlying_object(dual) is module
    assert structures.underlying_object(split) is module
    assert structures.structure(dual) is dual_numbers
    assert structures.structure(split) is split_idempotent
    assert forget(dual) is module
    assert forget(split) is module


def test_nonidentity_map_uses_its_forced_tensor_square() -> None:
    module, dual_numbers, split_idempotent = _two_products_on_one_module()
    tensor_square = _TensorSquareFunctor()
    structures = tensor_square.algebras()
    dual = structures.algebra(module, dual_numbers)
    split = structures.algebra(module, split_idempotent)
    one = module.module_generator("1")
    projection = module.module_category().Mor(module, module)(
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

    identity = module.module_category().Mor(module, module).identity()
    with pytest.raises(ValueError, match="does not commute"):
        structures.homomorphism(split, dual, identity)


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


def test_lie_admission_in_characteristic_two_checks_alternation() -> None:
    field = GF(2)
    module = field.free_module(finite_ordered_set(("x",)))
    x = module.module_generator("x")
    diagonal = BilinearMap(
        module,
        module,
        module,
        {("x", "x"): x},
    )

    # In characteristic two, the skew equation on this diagonal value is
    # vacuous: b(x,x) + b(x,x) = 0.  A Lie bracket still requires the stronger
    # alternating law b(x,x)=0.
    assert diagonal(x, x) + diagonal(x, x) == module.zero()
    with pytest.raises(AssertionError, match="alternation"):
        Algebras(field).Lie()(module, diagonal)


def test_algebra_axioms_refine_the_algebra_node_inside_modules() -> None:
    algebras = Algebras(QQ)

    assert algebras.is_subcategory(Modules(QQ))
    assert Algebras(QQ).Associative().is_subcategory(algebras)
    assert algebras.Associative().Unital().is_subcategory(algebras.Unital())
    assert Algebras(QQ).Associative().Unital().Commutative().is_subcategory(
        algebras.Associative().Unital()
    )
    assert Algebras(QQ).Associative().Unital().Commutative().is_subcategory(algebras.Commutative())


def test_unital_refinement_retains_eta_and_strengthens_the_mor() -> None:
    module, dual_numbers, _split_idempotent = _two_products_on_one_module()
    one = module.module_generator("1")
    scalar_module = Algebras(QQ).underlying_module()(QQ)
    assert scalar_module is QQ
    eta = _unit_morphism_from_element(module, one, QQ)
    unital = Algebras(QQ).Unital()(module, dual_numbers, one)

    assert unital.underlying_module() is unital
    assert unital.unit_morphism().codomain() is unital
    assert unital.unit_morphism()(scalar_module(QQ(3))) == 3 * unital.one()
    assert unital.one() == unital.module_generator("1")
    x = unital.module_generator("x")
    assert unital.one() * x == x
    assert x * unital.one() == x

    zero = unital.module_category().Mor(unital, unital)(
        {"1": unital.zero(), "x": unital.zero()}
    )
    general = Algebras(QQ)(module, dual_numbers)
    general_zero = general.module_category().Mor(general, general)(
        {"1": general.zero(), "x": general.zero()}
    )
    assert Algebras(QQ).Mor(general, general)(general_zero).underlying_morphism() is general_zero
    with pytest.raises(AssertionError, match="preserve the unit"):
        Algebras(QQ).Unital().Mor(unital, unital)(zero)


def test_tensor_cube_is_not_accepted_as_binary_multiplication():
    module = QQ.free_module(1)
    cube = Modules(QQ).tensor_product((module, module, module))
    ternary = cube.Mor(module)(lambda label: module.module_generator(0))
    with pytest.raises(AssertionError, match="tensor square"):
        Algebras(QQ)(module, ternary)


def test_native_ring_root_data_and_self_structure_are_initialized():
    assert QQ.unformed_module() is QQ
    assert QQ.multiplication()(QQ(2), QQ(3)) == QQ(6)
    assert QQ.algebra_structure_morphism() is QQ.Mor(QQ).identity()
    assert QQ.Mor(QQ).identity().as_algebra() is QQ
    assert QQ.associativity_decision() is True
    assert QQ.unit_laws_decision() is True
    assert QQ.commutativity_decision() is True


def test_unframed_algebra_classifies_its_product_and_preserves_unknown_map_equality() -> None:
    from sage.misc.unknown import Unknown
    from dzack_research.preamble.categories.modules.general_modules import GeneralModules
    from dzack_research.preamble.categories.sets.set_categories import Set

    module = GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x,
    )
    bilinear = module.bilinear_forms(module)(
        lambda x, y: module(x.underlying_element() * y.underlying_element())
    )
    multiplication = bilinear.classifying_morphism()
    algebra = Algebras(QQ)(module, multiplication)
    three, four = algebra(module(QQ(3))), algebra(module(QQ(4)))

    assert algebra.unformed_module() is module
    assert module(three * four) == module(QQ(12))
    classifier = algebra.multiplication_morphism()
    assert classifier(classifier.domain().pure_tensor(three, four)) == three * four


def test_kahler_computation_requires_a_selected_commutative_presentation() -> None:
    from dzack_research.preamble.categories.modules.general_modules import GeneralModules
    from dzack_research.preamble.categories.sets.set_categories import Set

    module = GeneralModules(QQ).from_operations(
        Set(QQ),
        addition=lambda x, y: x + y,
        zero=QQ.zero(),
        negation=lambda x: -x,
        scalar_action=lambda r, x: r * x,
    )
    tensor = Modules(QQ).tensor_product((module, module))
    product = tensor.from_bilinear_map(
        module,
        lambda x, y: module(x.underlying_element() * y.underlying_element()),
    )
    algebra = Algebras(QQ).Associative().Unital().Commutative()(
        module, product, module(QQ.one())
    )

    with pytest.raises(AssertionError):
        algebra.kahler_differentials()
    linear = algebra.module_category().Mor(algebra, algebra).elementwise(
        lambda x: x,
    )
    assert linear.linearity_decision() is Unknown
    conditional = Algebras(QQ).Mor(algebra, algebra)(linear)
    assert conditional.underlying_morphism() is linear
    assert conditional.linearity_decision() is Unknown
    assert conditional.is_multiplicative() is Unknown
    identity = Algebras(QQ).Mor(algebra, algebra).identity()
    assert identity(three) == three
    assert identity.is_multiplicative() is Unknown
    another_linear = algebra.module_category().Mor(algebra, algebra).elementwise(
        lambda x: x,
    )
    assert (linear == another_linear) is Unknown
    assert (linear != another_linear) is Unknown


def test_zero_field_endomorphism_is_multiplicative_but_not_unital() -> None:
    zero = QQ.module_category().Mor(QQ, QQ).zero()
    multiplicative = Algebras(QQ).Mor(QQ, QQ)(zero)

    assert multiplicative.linearity_decision() is True
    assert multiplicative.is_multiplicative() is True
    with pytest.raises(AssertionError, match="preserve the unit"):
        Algebras(QQ).Unital().Mor(QQ, QQ)(zero)


def test_unframed_unital_and_lie_entries_use_the_same_root_constructor() -> None:
    from sage.misc.unknown import Unknown
    from dzack_research.preamble.categories.modules.general_modules import GeneralModules
    from dzack_research.preamble.categories.sets.set_categories import Set

    module = GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x,
    )
    tensor = Modules(QQ).tensor_product((module, module))
    product = tensor.from_bilinear_map(
        module, lambda x, y: module(x.underlying_element() * y.underlying_element()),
    )
    commutative = Algebras(QQ).Associative().Unital().Commutative()(
        module, product, module(QQ.one()),
    )
    bracket = tensor.from_bilinear_map(module, lambda x, y: module.zero())
    lie = Algebras(QQ).Lie()(module, bracket)

    assert commutative.unformed_module() is module
    assert lie.unformed_module() is module
    assert commutative.one() * commutative(module(QQ(3))) == commutative(module(QQ(3)))
    assert lie(module(QQ(3))) * lie(module(QQ(4))) == lie.zero()
    assert lie not in Algebras(QQ).Unital()
    assert commutative.multiplication() is product
    assert lie.multiplication() is bracket
    assert commutative.associativity_decision() is Unknown
    assert commutative.unit_laws_decision() is Unknown
    assert commutative.commutativity_decision() is Unknown
    assert lie.alternation_decision() is Unknown
    assert lie.jacobi_decision() is Unknown
