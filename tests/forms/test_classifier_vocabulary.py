import pytest

from dzack_research.preamble.all import Modules, NN, ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/forms/forms.sage",
    "live_owner": "src/dzack_research/preamble/categories/forms/forms.py",
    "owner_overrides": {
        "QuadraticMapMorphism": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormHomset": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormHomset.module": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.parent": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.module": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.lift_form": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.polar_form": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.b": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.gram_matrix": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.pullback": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.descends_along": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.values_matrix": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMorphism.image": "src/dzack_research/preamble/categories/modules/powers.py",
        "BilinearFormHomset": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormHomset.module": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.parent": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.module": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.gram_matrix": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.subdivide_gram_matrix": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.norm": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.polar_form": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.pullback": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.descends_along": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.values_matrix": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMorphism.image": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearForm": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "QuadraticForm": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_form_type_names_alias_the_universal_module_hom_owners() -> None:
    from dzack_research.preamble.categories.forms.forms import (
        BilinearFormHomset,
        BilinearFormMorphism,
        QuadraticFormHomset,
        QuadraticFormMorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        TensorProductModuleHomset,
        TensorProductModuleMorphism,
    )
    from dzack_research.preamble.categories.modules.powers import (
        QuadraticModuleHomset,
        QuadraticModuleMorphism,
    )

    assert BilinearFormHomset is TensorProductModuleHomset
    assert BilinearFormMorphism is TensorProductModuleMorphism
    assert QuadraticFormHomset is QuadraticModuleHomset
    assert QuadraticFormMorphism is QuadraticModuleMorphism


def test_quadratic_map_and_divided_square_classifier_are_inverse_presentations() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    def quadratic_value(value):
        coefficients = module.framing_coefficients(value)
        x_coefficient = coefficients.get("x", ZZ.zero())
        y_coefficient = coefficients.get("y", ZZ.zero())
        return (
            x_coefficient**2
            + 3 * x_coefficient * y_coefficient
            + 2 * y_coefficient**2
        )

    quadratic = module.quadratic_map(ZZ, quadratic_value)
    classifier = quadratic.classifying_morphism()
    recovered = module.quadratic_map_from_morphism(classifier)
    for value in (x, y, x + y, 2 * x - y):
        assert recovered(value) == quadratic(value)
    assert recovered.classifying_morphism().domain() is classifier.domain()
    for label in classifier.domain().module_generating_set():
        generator = classifier.domain().module_generator(label)
        assert recovered.classifying_morphism()(generator) == classifier(generator)


def test_archive_tautological_constructions_use_module_owned_adjunctions() -> None:
    bilinear = Modules(ZZ).bilinear_free_form_adjunction()
    quadratic = Modules(ZZ).quadratic_free_form_adjunction()
    assert bilinear.left_adjoint().domain() is quadratic.left_adjoint().domain()
    assert bilinear.right_adjoint().codomain() is quadratic.right_adjoint().codomain()


def test_forms_on_countable_free_modules_remain_callable_and_pull_back_lazily() -> None:
    module = ZZ.free_module(NN)

    def coefficients(element):
        return module.framing_coefficients(element)

    bilinear = module.bilinear_forms(ZZ)(
        lambda left, right: sum(
            (
                left_coefficient * coefficients(right).get(label, ZZ.zero())
                for label, left_coefficient in coefficients(left).items()
            ),
            ZZ.zero(),
        )
    )
    quadratic = module.quadratic_map(
        ZZ,
        lambda element: sum(
            (coefficient**2 for coefficient in coefficients(element).values()),
            ZZ.zero(),
        ),
    )
    identity = module.module_category().Mor(module, module)(module.module_generator)
    pulled_bilinear = bilinear.pullback(identity)
    pulled_quadratic = quadratic.pullback(identity)
    e1000 = module.module_generator(NN(1000))

    assert pulled_bilinear(e1000, e1000) == ZZ.one()
    assert pulled_quadratic(e1000) == ZZ.one()
    with pytest.raises(TypeError, match="no finite Gram tensor"):
        pulled_bilinear.gram_tensor()

    another_bilinear = module.bilinear_forms(ZZ)(
        lambda left, right: pulled_bilinear(left, right)
    )
    another_quadratic = module.quadratic_map(
        ZZ,
        lambda element: pulled_quadratic(element),
    )
    assert (pulled_bilinear == another_bilinear) is Unknown
    assert (pulled_quadratic == another_quadratic) is Unknown
