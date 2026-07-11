r"""General algebra nouns: rings, groups, modules, linear algebra.

Declaration-only (INVENTORY.md II.2). Where the repo does not redefine a
concept, the semantic noun is tied directly to the Sage implementation
classes in play — an alias when one class realizes it, an enumerated union
when several do. Extending a union is a one-line, catalogued change; never
widen a noun to ``Any`` or shadow it with a hand protocol (INVENTORY.md I.2).
"""

from __future__ import annotations

from sage.categories.fields import Fields
from sage.categories.rings import Rings
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap as MatrixGroup,
)
from sage.groups.perm_gps.permgroup import (
    PermutationGroup_generic as PermutationGroup,
)
from sage.modules.fg_pid.fgp_module import FGP_Module_class as TorsionModule
from sage.modules.free_module import (
    FreeModule_generic as FreeModule,
)
from sage.modules.free_module import (
    FreeModule_generic_field as VectorSpace,
)
from sage.modules.free_module_element import FreeModuleElement as Vector
from sage.rings.finite_rings.integer_mod_ring import (
    IntegerModRing_generic as QuotientRing,
)
from sage.structure.element import (
    Matrix,
    ModuleElement,
    MultiplicativeGroupElement,
    RingElement,
)

from ..algebra.domain_algebra import (
    DiscriminantAction,
    DiscriminantOrthogonalGroup,
    FiniteAbelianGroup,
    LatticeCokernel,
    IsometryGroup,
    IsometrySubgroup,
    LatticeMorphism,
)

__all__ = [
    "AbelianGroup",
    "BaseRing",
    "Field",
    "FiniteAbelianGroup",
    "LatticeCokernel",
    "FreeModule",
    "Group",
    "GroupElement",
    "Matrix",
    "MatrixGroup",
    "Module",
    "ModuleElement",
    "PermutationGroup",
    "QuotientRing",
    "Ring",
    "RingElement",
    "TorsionModule",
    "Vector",
    "VectorSpace",
]

Ring = Rings.ParentMethods
"""A ring parent, typed by its CATEGORY (INVENTORY.md Part III): every
implementation class whose stub declares the ``Rings.ParentMethods`` MRO edge
(ZZ, QQ, ZZ/nZZ today; RR, CC, ZZ_p, ... as their stubs land) is a ``Ring``
for free. Implementations that fail to opt into their Sage category get a
documented enumeration union as fallback — none needed yet."""

Field = Fields.ParentMethods
"""A field parent, typed by its category (QQ today; RR, CC, QQ_p as their
stubs land)."""

type BaseRing = Ring
"""The ring a lattice is based over. The TYPE is any ring — the v1 grounding
restriction to ZZ/QQ is the construction codec's runtime contract
(``parse_base_ring``), deliberately not baked into the vocabulary, so
extending lattices over RR/CC/ZZ_p is a codec change, not a type migration."""

type Module = FreeModule | TorsionModule
"""R-module in play: free or finitely generated torsion."""

type AbelianGroup = TorsionModule | QmodnZ
"""Additive abelian group realized by Sage; the repo's own finite quotients
are ``FiniteAbelianGroup``."""


type Group = IsometryGroup | IsometrySubgroup | DiscriminantOrthogonalGroup | MatrixGroup | PermutationGroup
"""Group object in play: the owned isometry-side groups and the GAP seams."""

type GroupElement = LatticeMorphism | DiscriminantAction | MultiplicativeGroupElement
"""Element of a group in play."""
