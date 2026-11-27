r"""Subquotient construction category for topological spaces."""

from __future__ import annotations

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Topological spaces obtained as subspaces of quotients or quotients of subspaces.

    Canonical chain: ``TopologicalSpaces().Subquotients()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
