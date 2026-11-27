r"""Compatibility imports for the forms-owned nondegenerate bilinear category."""

from ...forms.subcategories import nondegenerate as _nondegenerate
from ...forms.subcategories.nondegenerate import (
    NondegenerateBilinearModulesCategory as NondegenerateBilinearModulesCategory,
)
from ...forms.subcategories.nondegenerate import (
    NondegenerateBilinearModulesElement as NondegenerateBilinearModulesElement,
)
from ...forms.subcategories.nondegenerate import (
    NondegenerateBilinearModulesMorphism as NondegenerateBilinearModulesMorphism,
)
from ...forms.subcategories.nondegenerate import (
    NondegenerateBilinearModulesObject as NondegenerateBilinearModulesObject,
)

OverPIDNondegenerateBilinearModulesCategory = (
    _nondegenerate.OverPIDNondegenerateBilinearModulesCategory
)
OverPIDNondegenerateBilinearModulesElement = (
    _nondegenerate.OverPIDNondegenerateBilinearModulesElement
)
OverPIDNondegenerateBilinearModulesMorphism = (
    _nondegenerate.OverPIDNondegenerateBilinearModulesMorphism
)
OverPIDNondegenerateBilinearModulesObject = (
    _nondegenerate.OverPIDNondegenerateBilinearModulesObject
)
