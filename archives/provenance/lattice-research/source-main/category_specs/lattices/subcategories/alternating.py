r"""Compatibility imports for the forms-owned alternating bilinear category."""

from ...forms.subcategories import alternating as _alternating
from ...forms.subcategories.alternating import (
    AlternatingBilinearModulesCategory as AlternatingBilinearModulesCategory,
)
from ...forms.subcategories.alternating import (
    AlternatingBilinearModulesElement as AlternatingBilinearModulesElement,
)
from ...forms.subcategories.alternating import (
    AlternatingBilinearModulesMorphism as AlternatingBilinearModulesMorphism,
)
from ...forms.subcategories.alternating import (
    AlternatingBilinearModulesObject as AlternatingBilinearModulesObject,
)

OverPIDAlternatingBilinearModulesCategory = (
    _alternating.OverPIDAlternatingBilinearModulesCategory
)
OverPIDAlternatingBilinearModulesElement = (
    _alternating.OverPIDAlternatingBilinearModulesElement
)
OverPIDAlternatingBilinearModulesMorphism = (
    _alternating.OverPIDAlternatingBilinearModulesMorphism
)
OverPIDAlternatingBilinearModulesObject = (
    _alternating.OverPIDAlternatingBilinearModulesObject
)
