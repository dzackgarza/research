r"""Isomorphic-object construction category for sets."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ....cat import IsomorphicObjectsCategory

if TYPE_CHECKING:
    from ....types import Set, SetElement, SetMorphism


class _IsomorphicObjects(IsomorphicObjectsCategory):
    r"""Sets transported along a distinguished isomorphism.

    Canonical chain: ``Sets().IsomorphicObjects()``.
    """

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Set:
            r"""Return the set from which structure is transported."""
            ...

        @abstractmethod
        def lift(self, x: SetElement) -> SetElement:
            r"""Apply the inverse isomorphism into the ambient set."""
            ...

        @abstractmethod
        def retract(self, x: SetElement) -> SetElement:
            r"""Apply the distinguished isomorphism from the ambient set."""
            ...

        @abstractmethod
        def isomorphism(self) -> SetMorphism:
            r"""Return the distinguished isomorphism defining this object."""
            ...

    class ElementMethods: ...
