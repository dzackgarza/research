r"""Subobject construction category for topological spaces."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import Category, SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Subset


class _Subobjects(SubobjectsCategory):
    r"""Topological subspaces with the induced topology.

    Canonical chain: ``TopologicalSpaces().Subobjects()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return project subobject categories without Sage axiom reapplication."""
        from ....sets import Sets

        return [
            self.base_category(),
            self.base_category().Subquotients(),
            Sets().Subobjects(),
        ]

    class ParentMethods:
        @abstractmethod
        def closure(self) -> Subset:
            r"""Return the closure of this subspace in its ambient space."""
            ...

        @abstractmethod
        def interior(self) -> Subset:
            r"""Return the interior of this subspace in its ambient space."""
            ...

        @abstractmethod
        def boundary(self) -> Subset:
            r"""Return the boundary of this subspace in its ambient space."""
            ...

        @abstractmethod
        def is_open(self) -> bool:
            r"""Return whether this subspace is open in its ambient space."""
            ...

        @abstractmethod
        def is_closed(self) -> bool:
            r"""Return whether this subspace is closed in its ambient space."""
            ...

    class ElementMethods: ...
