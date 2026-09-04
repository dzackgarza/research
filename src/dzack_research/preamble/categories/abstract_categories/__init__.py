r"""Lazy public aggregation for the owned abstract-category vocabulary.

The defining modules must remain independently importable.  Python executes a
package ``__init__`` before any submodule, so eager re-exports here create
artificial defining-module cycles.  Public names are resolved lazily instead.
"""

from importlib import import_module as _import_module

_EXPORTS = {
    'DirectSumDecomposition': ('dzack_research.preamble.categories.abstract_categories.direct_sum_objects', 'DirectSumDecomposition'),
    'DirectSumObjects': ('dzack_research.preamble.categories.abstract_categories.direct_sum_objects', 'DirectSumObjects'),
    'BiproductCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'BiproductCategory'),
    'Cocone': ('dzack_research.preamble.categories.abstract_categories.products', 'Cocone'),
    'CoconeCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'CoconeCategory'),
    'ColimitsOfCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'ColimitsOfCategory'),
    'Cone': ('dzack_research.preamble.categories.abstract_categories.products', 'Cone'),
    'ConeCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'ConeCategory'),
    'CoproductCoconeCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'CoproductCoconeCategory'),
    'CoproductsOfCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'CoproductsOfCategory'),
    'DiagramCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'DiagramCategory'),
    'DirectSumCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'DirectSumCategory'),
    'DirectedSystem': ('dzack_research.preamble.categories.abstract_categories.products', 'DirectedSystem'),
    'InverseSystem': ('dzack_research.preamble.categories.abstract_categories.products', 'InverseSystem'),
    'LimitsOfCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'LimitsOfCategory'),
    'ProductConeCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'ProductConeCategory'),
    'ProductsOfCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'ProductsOfCategory'),
    'TensorProductCategory': ('dzack_research.preamble.categories.abstract_categories.products', 'TensorProductCategory'),
    'ambient_category_of': ('dzack_research.preamble.categories.abstract_categories.products', 'ambient_category_of'),
    'coproduct_cocone_category': ('dzack_research.preamble.categories.abstract_categories.products', 'coproduct_cocone_category'),
    'product_cone_category': ('dzack_research.preamble.categories.abstract_categories.products', 'product_cone_category'),
    'Cat': ('dzack_research.preamble.categories.abstract_categories.cat', 'Cat'),
    'CategoryFunctorMorphism': ('dzack_research.preamble.categories.abstract_categories.cat', 'CategoryFunctorMorphism'),
    'CategoryObject': ('dzack_research.preamble.categories.abstract_categories.cat', 'CategoryObject'),
    'FunctorCategory': ('dzack_research.preamble.categories.abstract_categories.cat', 'FunctorCategory'),
    'NaturalTransformationMorphism': ('dzack_research.preamble.categories.abstract_categories.cat', 'NaturalTransformationMorphism'),
    'AutCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'AutCategoryConstruction'),
    'AutCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'AutCategoryOf'),
    'CategoricalHomset': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'CategoricalHomset'),
    'CategoryPacket': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'CategoryPacket'),
    'CategoryPacketMethods': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'CategoryPacketMethods'),
    'EndCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'EndCategoryConstruction'),
    'EndCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'EndCategoryOf'),
    'EpiCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'EpiCategoryConstruction'),
    'EpiCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'EpiCategoryOf'),
    'HomCategories': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'HomCategories'),
    'HomCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'HomCategoryConstruction'),
    'HomCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'HomCategoryOf'),
    'IsoCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'IsoCategoryConstruction'),
    'IsoCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'IsoCategoryOf'),
    'MonoCategoryConstruction': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'MonoCategoryConstruction'),
    'MonoCategoryOf': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'MonoCategoryOf'),
    'category_packet': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'category_packet'),
    'common_category': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'common_category'),
    'Isomorphism': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'Isomorphism'),
    'IsoArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'IsoArrowCategory'),
    'EndArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'EndArrowCategory'),
    'AutomorphismArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'AutomorphismArrowCategory'),
    'OppositeCategory': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'OppositeCategory'),
    'OppositeMorphism': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'OppositeMorphism'),
    'OppositeObject': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'OppositeObject'),
    'ProductCategory': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'ProductCategory'),
    'ProductMorphism': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'ProductMorphism'),
    'ProductObject': ('dzack_research.preamble.categories.abstract_categories.category_constructions', 'ProductObject'),
    'ArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'ArrowCategory'),
    'CategoricalIsomorphism': ('dzack_research.preamble.categories.abstract_categories.hom_categories', 'CategoricalIsomorphism'),
    'CommutativeSquare': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'CommutativeSquare'),
    'Core': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'Core'),
    'CoreCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'CoreCategory'),
    'CosliceCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'CosliceCategory'),
    'CosliceUnder': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'CosliceUnder'),
    'EpimorphismArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'EpimorphismArrowCategory'),
    'MonomorphismArrowCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'MonomorphismArrowCategory'),
    'SliceCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SliceCategory'),
    'SliceOver': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SliceOver'),
    'SubobjectCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SubobjectCategory'),
    'SubobjectHomset': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SubobjectHomset'),
    'SubobjectMorphism': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SubobjectMorphism'),
    'SubobjectsOf': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SubobjectsOf'),
    'SuperobjectCategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SuperobjectCategory'),
    'SuperobjectsOf': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'SuperobjectsOf'),
    'WideSubcategory': ('dzack_research.preamble.categories.abstract_categories.arrow_categories', 'WideSubcategory'),
    'Biproduct': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Biproduct'),
    'Coequalizer': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Coequalizer'),
    'CoequalizerOfFamily': ('dzack_research.preamble.categories.abstract_categories.constructions', 'CoequalizerOfFamily'),
    'Cokernel': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Cokernel'),
    'Coproduct': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Coproduct'),
    'Equalizer': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Equalizer'),
    'EqualizerOfFamily': ('dzack_research.preamble.categories.abstract_categories.constructions', 'EqualizerOfFamily'),
    'FiberProduct': ('dzack_research.preamble.categories.abstract_categories.constructions', 'FiberProduct'),
    'Kernel': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Kernel'),
    'Product': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Product'),
    'Pushout': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Pushout'),
    'Subobjects': ('dzack_research.preamble.categories.abstract_categories.constructions', 'Subobjects'),
    'TensorProduct': ('dzack_research.preamble.categories.abstract_categories.constructions', 'TensorProduct'),
    'TensorSquare': ('dzack_research.preamble.categories.abstract_categories.constructions', 'TensorSquare'),
}

__all__ = ['DirectSumDecomposition', 'DirectSumObjects', 'BiproductCategory', 'Cocone', 'CoconeCategory', 'ColimitsOfCategory', 'Cone', 'ConeCategory', 'CoproductCoconeCategory', 'CoproductsOfCategory', 'DiagramCategory', 'DirectSumCategory', 'DirectedSystem', 'InverseSystem', 'LimitsOfCategory', 'ProductConeCategory', 'ProductsOfCategory', 'TensorProductCategory', 'ambient_category_of', 'coproduct_cocone_category', 'product_cone_category', 'Cat', 'CategoryFunctorMorphism', 'CategoryObject', 'FunctorCategory', 'NaturalTransformationMorphism', 'AutCategoryConstruction', 'AutCategoryOf', 'CategoricalHomset', 'CategoryPacket', 'CategoryPacketMethods', 'EndCategoryConstruction', 'EndCategoryOf', 'EpiCategoryConstruction', 'EpiCategoryOf', 'HomCategories', 'HomCategoryConstruction', 'HomCategoryOf', 'IsoCategoryConstruction', 'IsoCategoryOf', 'MonoCategoryConstruction', 'MonoCategoryOf', 'category_packet', 'common_category', 'Isomorphism', 'IsoArrowCategory', 'EndArrowCategory', 'AutomorphismArrowCategory', 'OppositeCategory', 'OppositeMorphism', 'OppositeObject', 'ProductCategory', 'ProductMorphism', 'ProductObject', 'ArrowCategory', 'CategoricalIsomorphism', 'CommutativeSquare', 'Core', 'CoreCategory', 'CosliceCategory', 'CosliceUnder', 'EpimorphismArrowCategory', 'MonomorphismArrowCategory', 'SliceCategory', 'SliceOver', 'SubobjectCategory', 'SubobjectHomset', 'SubobjectMorphism', 'SubobjectsOf', 'SuperobjectCategory', 'SuperobjectsOf', 'WideSubcategory', 'Biproduct', 'Coequalizer', 'CoequalizerOfFamily', 'Cokernel', 'Coproduct', 'Equalizer', 'EqualizerOfFamily', 'FiberProduct', 'Kernel', 'Product', 'Pushout', 'Subobjects', 'TensorProduct', 'TensorSquare']

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
