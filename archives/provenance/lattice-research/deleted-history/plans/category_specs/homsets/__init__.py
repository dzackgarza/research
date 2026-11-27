r"""Generic hom, end, and aut category specs.

This package is a three-surface category root rather than a single category
class.  The initializer is the readable public index and type-package owner;
the root class definitions deliberately remain split by mathematical surface:

    homsets.py   -- ``HomCategory`` and ``HomCategoryOf``
    endsets.py   -- ``EndCategory`` and ``EndCategoryOf``
    autsets.py   -- ``AutCategory`` and ``AutCategoryOf``

That split follows the hom/end/aut ownership rule: endomorphism and
automorphism facts are not folded into the hom-category file, and the generic
aut construction remains in this subtree rather than being reimplemented by
individual category families.
"""

from __future__ import annotations

from .autsets import AutCategory, AutCategoryConstruction, AutCategoryOf, UniversalAutElementMethods, UniversalAutObjectMethods
from .endsets import EndCategory, EndCategoryConstruction, EndCategoryOf, UniversalEndElementMethods, UniversalEndObjectMethods
from .homsets import HomCategory, HomCategoryConstruction, HomCategoryOf, UniversalHomElementMethods, UniversalHomObjectMethods

GenericEndCategory = EndCategoryOf
GenericAutCategory = AutCategoryOf

HomCategoriesCategory = HomCategory
HomCategoriesObject = HomCategory.ParentMethods
HomCategoriesElement = HomCategory.ElementMethods
HomCategoriesMorphism = HomCategory.MorphismMethods

EndCategoriesCategory = EndCategory
EndCategoriesObject = EndCategory.ParentMethods
EndCategoriesElement = EndCategory.ElementMethods
EndCategoriesMorphism = EndCategory.MorphismMethods

AutCategoriesCategory = AutCategory
AutCategoriesObject = AutCategory.ParentMethods
AutCategoriesElement = AutCategory.ElementMethods
AutCategoriesMorphism = AutCategory.MorphismMethods
