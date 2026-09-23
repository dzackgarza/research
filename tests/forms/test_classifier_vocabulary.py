
from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/forms/forms.sage",
    "live_owner": "src/dzack_research/preamble/categories/forms/forms.py",
    "owner_overrides": {
        "QuadraticMapMorphism": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMor": "src/dzack_research/preamble/categories/modules/powers.py",
        "QuadraticFormMor.module": "src/dzack_research/preamble/categories/modules/powers.py",
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
        "BilinearFormMor": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "BilinearFormMor.module": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
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




