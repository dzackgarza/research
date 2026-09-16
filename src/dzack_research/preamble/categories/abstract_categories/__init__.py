r"""Lazy public aggregation for the owned abstract-category vocabulary.

The defining modules must remain independently importable.  Python executes a
package ``__init__`` before any submodule, so eager re-exports here create
artificial defining-module cycles.  Public names are resolved lazily instead.
"""

from importlib import import_module as _import_module

_EXPORTS = {
    "FunctorImageForgetfulFunctor": ("dzack_research.preamble.categories.abstract_categories.functor_images", "FunctorImageForgetfulFunctor"),
    "FunctorImageMorphism": ("dzack_research.preamble.categories.abstract_categories.functor_images", "FunctorImageMorphism"),
    "ImageOfFunctor": ("dzack_research.preamble.categories.abstract_categories.functor_images", "ImageOfFunctor"),
    "DirectSumObjects": ("dzack_research.preamble.categories.abstract_categories.direct_sum_objects", "DirectSumObjects"),
    "BiproductCategory": ("dzack_research.preamble.categories.abstract_categories.products", "BiproductCategory"),
    "DirectSumCategory": ("dzack_research.preamble.categories.abstract_categories.products", "DirectSumCategory"),
    "DirectedSystem": ("dzack_research.preamble.categories.abstract_categories.products", "DirectedSystem"),
    "FiniteOrdinalCategory": ("dzack_research.preamble.categories.abstract_categories.products", "FiniteOrdinalCategory"),
    "FiniteSequenceDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "FiniteSequenceDiagram"),
    "InverseSystem": ("dzack_research.preamble.categories.abstract_categories.products", "InverseSystem"),
    "ParallelPairCategory": ("dzack_research.preamble.categories.abstract_categories.products", "ParallelPairCategory"),
    "ParallelPairDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "ParallelPairDiagram"),
    "PosetCategory": ("dzack_research.preamble.categories.abstract_categories.products", "PosetCategory"),
    "RestrictedDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "RestrictedDiagram"),
    "SelectedColimitConstruction": ("dzack_research.preamble.categories.abstract_categories.products", "SelectedColimitConstruction"),
    "SelectedLimitConstruction": ("dzack_research.preamble.categories.abstract_categories.products", "SelectedLimitConstruction"),
    "TensorProductCategory": ("dzack_research.preamble.categories.abstract_categories.products", "TensorProductCategory"),
    "Cat": ("dzack_research.preamble.categories.abstract_categories.cat", "Cat"),
    "CategoryFunctorMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryFunctorMorphism"),
    "CategoryObject": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryObject"),
    "NaturalTransformationMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "NaturalTransformationMorphism"),
    "CategoricalHomset": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoricalHomset"),
    "CategoryPacketMethods": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoryPacketMethods"),
    "HomCategories": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "HomCategories"),
    "OppositeMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "OppositeMorphism"),
    "ProductMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "ProductMorphism"),
    "CategoricalIsomorphism": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoricalIsomorphism"),
    "CommutativeSquare": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "CommutativeSquare"),
    "SubobjectHomset": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectHomset"),
    "SubobjectMorphism": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectMorphism"),
    "Coverage": ("dzack_research.preamble.categories.abstract_categories.presheaves", "Coverage"),
    "CoveringFamilies": ("dzack_research.preamble.categories.abstract_categories.presheaves", "CoveringFamilies"),
    "CoveringFamily": ("dzack_research.preamble.categories.abstract_categories.presheaves", "CoveringFamily"),
    "CoveringOverlap": ("dzack_research.preamble.categories.abstract_categories.presheaves", "CoveringOverlap"),
    "DescentData": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentData"),
    "DescentDataOnCover": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentDataOnCover"),
    "DescentEqualizer": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentEqualizer"),
    "DescentEqualizerComparison": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentEqualizerComparison"),
    "SheafObject": ("dzack_research.preamble.categories.abstract_categories.presheaves", "SheafObject"),
    "Sheaves": ("dzack_research.preamble.categories.abstract_categories.presheaves", "Sheaves"),
    "TrivialCoveringFamilies": ("dzack_research.preamble.categories.abstract_categories.presheaves", "TrivialCoveringFamilies"),
    "trivial_coverage": ("dzack_research.preamble.categories.abstract_categories.presheaves", "trivial_coverage"),
}

__all__ = [
    "FunctorImageForgetfulFunctor",
    "FunctorImageMorphism",
    "ImageOfFunctor",
    "DirectSumObjects",
    "BiproductCategory",
    "DirectSumCategory",
    "DirectedSystem",
    "FiniteOrdinalCategory",
    "FiniteSequenceDiagram",
    "InverseSystem",
    "ParallelPairCategory",
    "ParallelPairDiagram",
    "PosetCategory",
    "RestrictedDiagram",
    "SelectedColimitConstruction",
    "SelectedLimitConstruction",
    "TensorProductCategory",
    "Cat",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "NaturalTransformationMorphism",
    "CategoricalHomset",
    "CategoryPacketMethods",
    "HomCategories",
    "OppositeMorphism",
    "ProductMorphism",
    "CategoricalIsomorphism",
    "CommutativeSquare",
    "SubobjectHomset",
    "SubobjectMorphism",
    "Coverage",
    "CoveringFamilies",
    "CoveringFamily",
    "CoveringOverlap",
    "DescentData",
    "DescentDataOnCover",
    "DescentEqualizer",
    "DescentEqualizerComparison",
    "SheafObject",
    "Sheaves",
    "TrivialCoveringFamilies",
    "trivial_coverage",
]


def __getattr__(name):
    try:
        module_name, attribute = _EXPORTS[name]
    except KeyError as error:
        raise AttributeError(name) from error
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value


def __dir__():
    return sorted((*globals(), *__all__))
