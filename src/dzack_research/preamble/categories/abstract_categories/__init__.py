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
    "Cat": ("dzack_research.preamble.categories.abstract_categories.cat", "Cat"),
    "CategoryFunctorMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryFunctorMorphism"),
    "CategoryObject": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryObject"),
    "NaturalTransformationMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "NaturalTransformationMorphism"),
    "CategoricalMor": ("dzack_research.preamble.categories.abstract_categories.mor_categories", "CategoricalMor"),
    "CategoryPacketMethods": ("dzack_research.preamble.categories.abstract_categories.mor_categories", "CategoryPacketMethods"),
    "MorCategories": ("dzack_research.preamble.categories.abstract_categories.mor_categories", "MorCategories"),
    "OppositeMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "OppositeMorphism"),
    "ProductMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "ProductMorphism"),
    "CategoricalIsomorphism": ("dzack_research.preamble.categories.abstract_categories.mor_categories", "CategoricalIsomorphism"),
    "CommutativeSquare": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "CommutativeSquare"),
    "SubobjectMor": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectMor"),
    "SubobjectMorphism": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectMorphism"),
    "Coverage": ("dzack_research.preamble.categories.abstract_categories.presheaves", "Coverage"),
    "CoveringFamilies": ("dzack_research.preamble.categories.abstract_categories.presheaves", "CoveringFamilies"),
    "DescentData": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentData"),
    "DescentDataOnCover": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentDataOnCover"),
    "DescentEqualizer": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentEqualizer"),
    "DescentEqualizerComparison": ("dzack_research.preamble.categories.abstract_categories.presheaves", "DescentEqualizerComparison"),
    "Sheaves": ("dzack_research.preamble.categories.abstract_categories.presheaves", "Sheaves"),
    "TrivialCoveringFamilies": ("dzack_research.preamble.categories.abstract_categories.presheaves", "TrivialCoveringFamilies"),
    "trivial_coverage": ("dzack_research.preamble.categories.abstract_categories.presheaves", "trivial_coverage"),
    "ResolutionMorphism": ("dzack_research.preamble.categories.abstract_categories.resolutions", "ResolutionMorphism"),
    "Resolutions": ("dzack_research.preamble.categories.abstract_categories.resolutions", "Resolutions"),
}

__all__ = [
    "FunctorImageForgetfulFunctor",
    "FunctorImageMorphism",
    "ImageOfFunctor",
    "DirectSumObjects",
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
    "Cat",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "NaturalTransformationMorphism",
    "CategoricalMor",
    "CategoryPacketMethods",
    "MorCategories",
    "OppositeMorphism",
    "ProductMorphism",
    "CategoricalIsomorphism",
    "CommutativeSquare",
    "SubobjectMor",
    "SubobjectMorphism",
    "Coverage",
    "CoveringFamilies",
    "DescentData",
    "DescentDataOnCover",
    "DescentEqualizer",
    "DescentEqualizerComparison",
    "Sheaves",
    "TrivialCoveringFamilies",
    "trivial_coverage",
    "ResolutionMorphism",
    "Resolutions",
]


def __getattr__(name):
    # Python's module attribute protocol: a name this package does not
    # export is an AttributeError.
    if name not in _EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attribute = _EXPORTS[name]
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value


def __dir__():
    return sorted((*globals(), *__all__))
