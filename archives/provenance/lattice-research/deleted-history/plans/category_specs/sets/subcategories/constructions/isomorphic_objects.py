r"""Isomorphic-object construction category for sets."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import IsomorphicObjectsCategory

if TYPE_CHECKING:
    from ....types import Set, SetElement, SetMorphism


class _IsomorphicObjects(IsomorphicObjectsCategory):
    r"""Sets transported along a distinguished isomorphism.

    Canonical chain: ``Sets().IsomorphicObjects()``.
    """

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Set:
            r"""Return the set from which structure is transported."""
            ...

        @abstract_method
        def lift(self, x: SetElement) -> SetElement:
            r"""Apply the inverse isomorphism into the ambient set."""
            ...

        @abstract_method
        def retract(self, x: SetElement) -> SetElement:
            r"""Apply the distinguished isomorphism from the ambient set."""
            ...

        @abstract_method
        def isomorphism(self) -> SetMorphism:
            r"""Return the distinguished isomorphism defining this object."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
