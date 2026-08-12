r"""General algebra nouns: rings, modules, linear algebra.

Declaration-only. Where the preamble does not redefine a concept, the
semantic noun is tied directly to the Sage implementation classes in play —
an alias when one class realizes it, an enumerated union when several do.
Extending a union is a one-line, catalogued change; never widen a noun to
``Any`` or shadow it with a hand protocol.
"""

from __future__ import annotations

from sage.categories.groups import Groups
from sage.categories.rings import Rings
from sage.modules.fg_pid.fgp_module import FGP_Module_class as TorsionModule
from sage.modules.free_module import FreeModule_generic as FreeModule
from sage.modules.free_module_element import FreeModuleElement as Vector
from sage.structure.element import (
    Element,
    Matrix,
    ModuleElement,
    RingElement,
)

__all__ = [
    "BaseRing",
    "Element",
    "FreeModule",
    "Group",
    "GroupElement",
    "Matrix",
    "Module",
    "ModuleElement",
    "Ring",
    "RingElement",
    "TorsionModule",
    "Vector",
]

Ring = Rings.ParentMethods
"""A ring parent, typed by its CATEGORY: every implementation class whose
stub declares the ``Rings.ParentMethods`` MRO edge (ZZ, QQ, ZZ/nZZ today; RR,
CC, ZZ_p, ... as their stubs land) is a ``Ring`` for free. Implementations
that fail to opt into their Sage category get a documented enumeration union
as fallback — none needed yet."""

type BaseRing = Ring
"""The ring a module or lattice is based over. The TYPE is any ring — a
grounding restriction to particular rings is a construction codec's runtime
contract, deliberately not baked into the vocabulary, so extending over
RR/CC/ZZ_p is a codec change, not a type migration."""

type Module = FreeModule | TorsionModule
"""R-module in play: free or finitely generated torsion."""

Group = Groups.ParentMethods
"""A group parent, typed by its CATEGORY like ``Ring`` and ``Set``: every
parent placed in ``Groups()`` is a ``Group``.

The archived spike enumerated instead — a union of its isometry groups, the
discriminant orthogonal group, and the GAP seams — which named that
implementation's own classes and so could not describe the finitely
presented groups, Galois groups and predicate subgroups the preamble builds.
The category is what those all share."""

GroupElement = Groups.ElementMethods
"""An element of a group parent, typed by its category."""
