r"""Technical Sage-interop nouns (dev-facing).

Declaration-only (INVENTORY.md II.5). A ``Sage*`` spelling exists exactly
where Sage's object is distinct from (or must be distinguished from) the
repo's semantic object of the same mathematical kind. Semantic nouns whose
only realization is Sage's class (Matrix, Vector, Integer, ...) live in
``algebra``/``foundations`` under their bare names and get no doppelganger
here (naming rule IV.3).
"""

from __future__ import annotations

from sage.categories.category_types import Category_over_base_ring as SageCategory
from sage.combinat.root_system.cartan_matrix import CartanMatrix as SageCartanMatrix
from sage.groups.additive_abelian.qmodnz import QmodnZ as SageQmodnZ
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric as SageLattice,
)
from sage.modules.torsion_quadratic_module import (
    TorsionQuadraticModule as SageDiscriminantForm,
)
from sage.quadratic_forms.genera.genus import (
    Genus_Symbol_p_adic_ring as SageLocalGenusSymbol,
)
from sage.quadratic_forms.genera.genus import (
    GenusSymbol_global_ring as SageGenus,
)
from sage.quadratic_forms.quadratic_form import QuadraticForm as SageQuadraticForm
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent as SageParent

__all__ = [
    "SageCartanMatrix",
    "SageCategory",
    "SageDiscriminantForm",
    "SageElement",
    "SageFreeModule",
    "SageGenus",
    "SageInfinity",
    "SageLattice",
    "SageLocalGenusSymbol",
    "SageParent",
    "SageQmodnZ",
    "SageQuadraticForm",
]

type SageInfinity = PlusInfinity | MinusInfinity
"""The unsigned-infinity endpoints returned by minimum/maximum vocabulary."""

type SageFreeModule = FreeModule_generic | FGP_Module_class
"""Dev-facing union over Sage's module implementation classes, as flexible as
the seams require (extend with CombinatorialFreeModule etc. on first use).
``FreeModule_generic`` is Sage implementation vocabulary — user-facing
signatures say ``algebra.FreeModule``; this name exists for seams that must
accept whichever implementation Sage hands back."""
