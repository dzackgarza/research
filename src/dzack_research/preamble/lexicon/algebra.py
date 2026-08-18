r"""General algebra nouns: rings, modules, linear algebra.

Declaration-only. Where the preamble does not redefine a concept, the
semantic noun is tied directly to the Sage implementation classes in play —
an alias when one class realizes it, an enumerated union when several do.
Extending a union is a one-line, catalogued change; never widen a noun to
``Any`` or shadow it with a hand protocol.

Names for Sage's own objects (``Ring``, ``Module``, ``Group``, ``Set``,
``GroupElement``, ``Vector``, ...) do NOT belong here: they are Sage typing
and live in the stub tree (``typings/sage/categories/``). This module holds
only the preamble's own nouns and the re-exports its code draws on.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.structure.element import (
    Element,
    Matrix,
    ModuleElement,
    RingElement,
)

if TYPE_CHECKING:
    # The canonical short name for "a ring parent", declared in the stub
    # tree (sage/categories/rings.pyi); resolved only at type-check time.
    from sage.categories.rings import Ring

__all__ = [
    "BaseRing",
    "Element",
    "Matrix",
    "ModuleElement",
    "RingElement",
]

type BaseRing = Ring
"""The ring a module or lattice is based over. The TYPE is any ring — a
grounding restriction to particular rings is a construction codec's runtime
contract, deliberately not baked into the vocabulary, so extending over
RR/CC/ZZ_p is a codec change, not a type migration."""
