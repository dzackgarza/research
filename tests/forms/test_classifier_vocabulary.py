import pytest

from dzack_research.preamble.all import NN, ZZ
from dzack_research.preamble.categories.forms import (
    BilinearForms,
    QuadraticForms,
    QuadraticMap,
    classifying_morphism,
    quadratic_map_from_morphism,
)
from dzack_research.preamble.categories.functors.free_forms import (
    BilinearFormForgetfulAdjunction,
    BilinearFreeFormAdjunction,
    QuadraticFormForgetfulAdjunction,
    QuadraticFreeFormAdjunction,
    TautologicalBilinearFormFunctor,
    TautologicalQuadraticFormFunctor,
)
from dzack_research.preamble.categories.modules import BasedFreeModule, FreeModuleOn, module_homset
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_quadratic_map_and_divided_square_classifier_are_inverse_presentations() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    def quadratic_value(value):
        coefficients = module_coefficients(value, module)
        x_coefficient = coefficients.get("x", ZZ.zero())
        y_coefficient = coefficients.get("y", ZZ.zero())
        return (
            x_coefficient**2
            + 3 * x_coefficient * y_coefficient
            + 2 * y_coefficient**2
        )

    quadratic = QuadraticMap(module, ZZ, quadratic_value)
    classifier = classifying_morphism(quadratic)
    recovered = quadratic_map_from_morphism(module, classifier)
    for value in (x, y, x + y, 2 * x - y):
        assert recovered(value) == quadratic(value)
    assert classifying_morphism(recovered).domain() is classifier.domain()
    for label in classifier.domain().module_generating_set():
        generator = classifier.domain().module_generator(label)
        assert classifying_morphism(recovered)(generator) == classifier(generator)


def test_archive_tautological_names_are_the_live_classifier_adjunctions() -> None:
    assert TautologicalBilinearFormFunctor is not None
    assert TautologicalQuadraticFormFunctor is not None
    assert BilinearFormForgetfulAdjunction is BilinearFreeFormAdjunction
    assert QuadraticFormForgetfulAdjunction is QuadraticFreeFormAdjunction


def test_forms_on_countable_free_modules_remain_callable_and_pull_back_lazily() -> None:
    module = FreeModuleOn(ZZ, NN)

    def coefficients(element):
        return module_coefficients(element, module)

    bilinear = BilinearForms(module, ZZ)(
        lambda left, right: sum(
            (
                left_coefficient * coefficients(right).get(label, ZZ.zero())
                for label, left_coefficient in coefficients(left).items()
            ),
            ZZ.zero(),
        )
    )
    quadratic = QuadraticMap(
        module,
        ZZ,
        lambda element: sum(
            (coefficient**2 for coefficient in coefficients(element).values()),
            ZZ.zero(),
        ),
    )
    identity = module_homset(module, module)(module.module_generator)
    pulled_bilinear = bilinear.pullback(identity)
    pulled_quadratic = quadratic.pullback(identity)
    e1000 = module.module_generator(NN(1000))

    assert pulled_bilinear(e1000, e1000) == ZZ.one()
    assert pulled_quadratic(e1000) == ZZ.one()
    with pytest.raises(TypeError, match="no finite Gram tensor"):
        pulled_bilinear.gram_tensor()

    another_bilinear = BilinearForms(module, ZZ)(
        lambda left, right: pulled_bilinear(left, right)
    )
    another_quadratic = QuadraticMap(
        module, ZZ, lambda element: pulled_quadratic(element)
    )
    with pytest.raises(NotImplementedError, match="not decidable"):
        _ = pulled_bilinear == another_bilinear
    with pytest.raises(NotImplementedError, match="not decidable"):
        _ = pulled_quadratic == another_quadratic
