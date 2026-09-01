from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.forms import (
    QuadraticMap,
    classifying_morphism,
    quadratic_map_from_morphism,
)
from dzack_research.preamble.categories.functors import (
    BilinearFormForgetfulAdjunction,
    BilinearFreeFormAdjunction,
    QuadraticFormForgetfulAdjunction,
    QuadraticFreeFormAdjunction,
    TautologicalBilinearFormFunctor,
    TautologicalQuadraticFormFunctor,
)
from dzack_research.preamble.categories.modules import BasedFreeModule
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_quadratic_map_and_divided_square_classifier_are_inverse_presentations() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    quadratic = QuadraticMap(module, ZZ, lambda value: value[0] ** 2 + 3 * value[0] * value[1] + 2 * value[1] ** 2)
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
