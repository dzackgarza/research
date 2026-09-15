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
    "ColimitsOfCategory": ("dzack_research.preamble.categories.abstract_categories.products", "ColimitsOfCategory"),
    "CoproductsOfCategory": ("dzack_research.preamble.categories.abstract_categories.products", "CoproductsOfCategory"),
    "DiagramCategory": ("dzack_research.preamble.categories.abstract_categories.products", "DiagramCategory"),
    "DirectSumCategory": ("dzack_research.preamble.categories.abstract_categories.products", "DirectSumCategory"),
    "DirectedSystem": ("dzack_research.preamble.categories.abstract_categories.products", "DirectedSystem"),
    "FiniteOrdinalCategory": ("dzack_research.preamble.categories.abstract_categories.products", "FiniteOrdinalCategory"),
    "FiniteSequenceDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "FiniteSequenceDiagram"),
    "InverseSystem": ("dzack_research.preamble.categories.abstract_categories.products", "InverseSystem"),
    "LimitsOfCategory": ("dzack_research.preamble.categories.abstract_categories.products", "LimitsOfCategory"),
    "ParallelPairCategory": ("dzack_research.preamble.categories.abstract_categories.products", "ParallelPairCategory"),
    "ParallelPairDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "ParallelPairDiagram"),
    "PosetCategory": ("dzack_research.preamble.categories.abstract_categories.products", "PosetCategory"),
    "ProductsOfCategory": ("dzack_research.preamble.categories.abstract_categories.products", "ProductsOfCategory"),
    "RestrictedDiagram": ("dzack_research.preamble.categories.abstract_categories.products", "RestrictedDiagram"),
    "SelectedColimitConstruction": ("dzack_research.preamble.categories.abstract_categories.products", "SelectedColimitConstruction"),
    "SelectedLimitConstruction": ("dzack_research.preamble.categories.abstract_categories.products", "SelectedLimitConstruction"),
    "TensorProductCategory": ("dzack_research.preamble.categories.abstract_categories.products", "TensorProductCategory"),
    "Cat": ("dzack_research.preamble.categories.abstract_categories.cat", "Cat"),
    "CategoryFunctorMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryFunctorMorphism"),
    "CategoryObject": ("dzack_research.preamble.categories.abstract_categories.cat", "CategoryObject"),
    "NaturalTransformationMorphism": ("dzack_research.preamble.categories.abstract_categories.cat", "NaturalTransformationMorphism"),
    "AutCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "AutCategoryConstruction"),
    "CategoricalHomset": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoricalHomset"),
    "CategoryPacket": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoryPacket"),
    "CategoryPacketMethods": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoryPacketMethods"),
    "EndCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "EndCategoryConstruction"),
    "EpiCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "EpiCategoryConstruction"),
    "HomCategories": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "HomCategories"),
    "HomCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "HomCategoryConstruction"),
    "IsoCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "IsoCategoryConstruction"),
    "MonoCategoryConstruction": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "MonoCategoryConstruction"),
    "Isomorphism": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "Isomorphism"),
    "IsoArrowCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "IsoArrowCategory"),
    "EndArrowCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "EndArrowCategory"),
    "AutomorphismArrowCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "AutomorphismArrowCategory"),
    "OppositeMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "OppositeMorphism"),
    "ProductMorphism": ("dzack_research.preamble.categories.abstract_categories.category_constructions", "ProductMorphism"),
    "CategoricalIsomorphism": ("dzack_research.preamble.categories.abstract_categories.hom_categories", "CategoricalIsomorphism"),
    "CommutativeSquare": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "CommutativeSquare"),
    "CoreCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "CoreCategory"),
    "EpimorphismArrowCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "EpimorphismArrowCategory"),
    "MonomorphismArrowCategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "MonomorphismArrowCategory"),
    "SubobjectHomset": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectHomset"),
    "SubobjectMorphism": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "SubobjectMorphism"),
    "WideSubcategory": ("dzack_research.preamble.categories.abstract_categories.arrow_categories", "WideSubcategory"),
}

__all__ = [
    "FunctorImageForgetfulFunctor",
    "FunctorImageMorphism",
    "ImageOfFunctor",
    "DirectSumObjects",
    "BiproductCategory",
    "ColimitsOfCategory",
    "CoproductsOfCategory",
    "DiagramCategory",
    "DirectSumCategory",
    "DirectedSystem",
    "FiniteOrdinalCategory",
    "FiniteSequenceDiagram",
    "InverseSystem",
    "LimitsOfCategory",
    "ParallelPairCategory",
    "ParallelPairDiagram",
    "PosetCategory",
    "ProductsOfCategory",
    "RestrictedDiagram",
    "SelectedColimitConstruction",
    "SelectedLimitConstruction",
    "TensorProductCategory",
    "Cat",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "NaturalTransformationMorphism",
    "AutCategoryConstruction",
    "CategoricalHomset",
    "CategoryPacket",
    "CategoryPacketMethods",
    "EndCategoryConstruction",
    "EpiCategoryConstruction",
    "HomCategories",
    "HomCategoryConstruction",
    "IsoCategoryConstruction",
    "MonoCategoryConstruction",
    "Isomorphism",
    "IsoArrowCategory",
    "EndArrowCategory",
    "AutomorphismArrowCategory",
    "OppositeMorphism",
    "ProductMorphism",
    "CategoricalIsomorphism",
    "CommutativeSquare",
    "CoreCategory",
    "EpimorphismArrowCategory",
    "MonomorphismArrowCategory",
    "SubobjectHomset",
    "SubobjectMorphism",
    "WideSubcategory",
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
