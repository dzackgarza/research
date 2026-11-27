r"""Subquotient construction category for sets.

A set subquotient is represented constructively by an ambient set, a lift into
that ambient set, and a retract back to the represented set. Subobjects and
quotients are special cases of this construction.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ....cat import SubquotientsCategory

if TYPE_CHECKING:
    from ....types import Set, SetElement


class _Subquotients(SubquotientsCategory):
    r"""Constructive subquotients of sets.

    Canonical chain: ``Sets().Subquotients()``.
    """

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Set:
            r"""Return the ambient set in which this subquotient is represented."""
            ...

        @abstractmethod
        def lift(self, x: SetElement) -> SetElement:
            r"""Lift an element to the ambient set."""
            ...

        @abstractmethod
        def retract(self, x: SetElement) -> SetElement:
            r"""Retract an ambient element to this set."""
            ...

    class ElementMethods:
        @abstractmethod
        def lift(self) -> SetElement:
            r"""Lift this element to the ambient set of its parent."""
            ...
