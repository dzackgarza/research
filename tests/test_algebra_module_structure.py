from sage.categories.homset import Hom
from sage.categories.rings import Rings as SageRings
import pytest

from dzack_research.preamble.all import (
    Algebras,
    BasedFreeModule,
    BilinearMap,
    GradedAlgebras,
    GradedModules,
    MatrixSpace,
    Modules,
    QQ,
    QuadraticField,
    SymmetricAlgebraOn,
    TensorProduct,
    ZZ,
    algebra_underlying_module_functor,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _gaussian_integers():
    return QuadraticField(-1, "I").ring_of_integers()


def _multiplication_from_structure_constants(module, images):
    return TensorProduct(module, module).from_bilinear(
        BilinearMap(module, module, module, images)
    )


def test_algebra_structure_morphism_lands_in_the_center() -> None:
    order = _gaussian_integers()
    eta = order.algebra_structure_morphism()
    one, imag = tuple(order.module_generators())

    assert eta.domain() is ZZ
    assert eta.codomain() is order.ring_center()
    assert eta.codomain() is order
    assert eta.parent().homset_category().is_subcategory(SageRings())
    assert eta(ZZ(1)) == order.one()
    assert eta(ZZ(2)) * imag == imag * eta(ZZ(2))
    assert eta(ZZ(2)) * eta(ZZ(3)) == eta(ZZ(6))

    matrices = MatrixSpace(QQ, 2)
    matrix_eta = matrices.algebra_structure_morphism()
    assert matrix_eta.domain() is QQ
    assert matrix_eta.codomain() is matrices.ring_center()
    assert matrix_eta(QQ(3)) == 3 * matrices.one()

    polynomials = SymmetricAlgebraOn(QQ, ["x"])
    polynomial_eta = polynomials.algebra_structure_morphism()
    assert polynomial_eta.domain() is QQ
    assert polynomial_eta.codomain() is polynomials.ring_center()
    assert polynomial_eta.codomain() is polynomials


def test_forgetful_functor_sends_an_algebra_to_its_underlying_module() -> None:
    order = _gaussian_integers()
    underlying = algebra_underlying_module_functor(ZZ)

    assert underlying.domain() is Algebras(ZZ)
    assert underlying.codomain() is Modules(ZZ)
    assert underlying(order) is order
    assert order in Modules(ZZ)

    identity = Hom(order, order).identity()
    module_identity = underlying(identity)
    assert module_identity.domain() is order
    assert module_identity.codomain() is order
    assert module_identity.parent().Element is ModuleMorphism
    for label in order.module_generating_set():
        generator = order.module_generator(label)
        assert module_identity(generator) == generator

    polynomials = SymmetricAlgebraOn(QQ, ["x"])
    polynomial_underlying = algebra_underlying_module_functor(QQ)
    assert polynomial_underlying(polynomials) is polynomials
    assert polynomials in Modules(QQ)


def test_multiplication_morphism_is_the_module_map_out_of_the_tensor_product() -> None:
    order = _gaussian_integers()
    one, imag = tuple(order.module_generators())
    multiplication = order.multiplication_morphism()
    tensor = multiplication.domain()

    assert multiplication.codomain() is order
    assert multiplication.parent().Element is ModuleMorphism
    assert tensor.tensor_factors() == (order, order)
    assert multiplication(tensor.pure_tensor(one, imag)) == one * imag
    assert multiplication(tensor.pure_tensor(imag, imag)) == imag * imag
    assert multiplication(tensor.pure_tensor(one + imag, one - imag)) == (
        (one + imag) * (one - imag)
    )


def test_unframed_algebra_has_no_constructed_tensor_multiplication() -> None:
    polynomials = SymmetricAlgebraOn(QQ, ["x"])
    with pytest.raises(TypeError, match="finitely presented"):
        polynomials.multiplication_morphism()


def test_algebras_intern_a_module_from_its_multiplication_morphism() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set((0, 1)))
    one = module.module_generator(0)
    imag = module.module_generator(1)
    multiplication = _multiplication_from_structure_constants(
        module,
        {
            (0, 0): one,
            (0, 1): imag,
            (1, 0): imag,
            (1, 1): -one,
        },
    )

    algebra = Algebras(ZZ)(multiplication)
    unit = algebra.module_generator(0)
    generator = algebra.module_generator(1)
    eta = algebra.algebra_structure_morphism()
    stored = algebra.multiplication_morphism()

    assert algebra in Algebras(ZZ)
    assert algebra in Modules(ZZ)
    assert algebra.one() == unit
    assert unit * generator == generator
    assert generator * generator == -unit
    assert eta.domain() is ZZ
    assert eta.codomain() is algebra.ring_center()
    assert eta(ZZ(2)) == 2 * unit
    assert stored.codomain() is algebra
    assert stored.domain().tensor_factors() == (algebra, algebra)
    assert stored(stored.domain().pure_tensor(unit, generator)) == generator


def test_algebras_intern_the_multiplication_of_an_order() -> None:
    order = _gaussian_integers()
    one, imag = tuple(order.module_generators())
    algebra = Algebras(ZZ)(order.multiplication_morphism())
    unit = algebra.module_generator(0)
    generator = algebra.module_generator(1)

    assert algebra is not order
    assert algebra in Algebras(ZZ)
    assert unit * generator == generator
    assert generator * generator == -unit
    assert algebra.algebra_structure_morphism()(ZZ(1)) == algebra.one()


def test_graded_algebras_intern_a_graded_module_from_its_product() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set((0, 1)))
    refine(module, GradedModules(ZZ))
    one = module.module_generator(0)
    epsilon = module.module_generator(1)
    multiplication = _multiplication_from_structure_constants(
        module,
        {
            (0, 0): one,
            (0, 1): epsilon,
            (1, 0): epsilon,
            (1, 1): module.zero(),
        },
    )

    algebra = GradedAlgebras(ZZ)(multiplication)
    unit = algebra.module_generator(0)
    generator = algebra.module_generator(1)

    assert algebra in GradedAlgebras(ZZ)
    assert algebra in GradedModules(ZZ)
    assert algebra in Algebras(ZZ)
    assert algebra.grading_monoid() is ZZ
    assert unit * generator == generator
    assert generator * generator == algebra.zero()


def test_graded_algebras_refuse_an_ungraded_module() -> None:
    order = _gaussian_integers()
    with pytest.raises(TypeError, match="not a module graded"):
        GradedAlgebras(ZZ)(order.multiplication_morphism())
