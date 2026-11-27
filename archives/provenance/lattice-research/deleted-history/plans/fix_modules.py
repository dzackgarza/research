import sys
import re

file_path = "/home/dzack/research/plans/category_specs/modules.py"

replacements = {
    r"\bModulesCategoryObject\b": "RModule",
    r"\bModuleElement\b": "RModuleElement",
    r"\bModulesMorphismObject\b": "RModHomsetElement",
    r"\bFreeModuleCategoryObject\b": "FreeModule",
    r"\bTorsionModuleCategoryObject\b": "TorsionModule",
    r"\bIdealSubmodulesCategoryObject\b": "Ideal",
    r"\bSubmoduleCategoryObject\b": "SubModule",
    r"\bQuotientModuleCategoryObject\b": "QuotientModule",
    r"\bDualModuleCategoryObject\b": "DualModule",
    r"\bProjectiveModuleCategoryObject\b": "ProjectiveModule",
    r"\bEndomorphismAlgebraCategoryObject\b": "RModEndset",
    r"\bEndomorphismAlgebraElement\b": "RModEndsetElement",
}

with open(file_path, "r") as f:
    content = f.read()

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

# Add TYPE_CHECKING block if it doesn't have the new imports
# The existing block is:
# if TYPE_CHECKING:
#     from .rings import ModuleBaseRingElement, ModuleBaseRingsCategoryObject

new_type_checking = """if TYPE_CHECKING:
    from .rings import ModuleBaseRingElement, ModuleBaseRingsCategoryObject
    from .types import (
        DualModule,
        DualModuleElement,
        FreeModule,
        Ideal,
        ProjectiveModule,
        QuotientModule,
        RModEndset,
        RModEndsetElement,
        RModHomsetElement,
        RModule,
        RModuleElement,
        SubModule,
        TorsionModule,
    )"""

old_type_checking = r"if TYPE_CHECKING:\n    from \.rings import ModuleBaseRingElement, ModuleBaseRingsCategoryObject"
content = re.sub(old_type_checking, new_type_checking, content)

with open(file_path, "w") as f:
    f.write(content)
