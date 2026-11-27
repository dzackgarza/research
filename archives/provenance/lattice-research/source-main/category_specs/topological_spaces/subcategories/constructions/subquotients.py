r"""Subquotient construction category for topological spaces."""

from __future__ import annotations

from typing import final, override

from ....cat import Category, SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Topological spaces obtained as subspaces of quotients or quotients of subspaces.

    Canonical chain: ``TopologicalSpaces().Subquotients()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return project subquotient categories without Sage axiom reapplication."""
        from ....sets import Sets

        return [self.base_category(), Sets().Subquotients()]

    class ParentMethods: ...

    class ElementMethods: ...
