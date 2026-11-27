r"""Quotient construction category for topological spaces."""

from __future__ import annotations

from typing import final, override

from ....cat import Category, QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Topological quotient spaces with the quotient topology.

    Canonical chain: ``TopologicalSpaces().Quotients()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return project quotient categories without Sage axiom reapplication."""
        from ....sets import Sets

        return [self.base_category(), Sets().Quotients()]

    class ParentMethods: ...

    class ElementMethods: ...
