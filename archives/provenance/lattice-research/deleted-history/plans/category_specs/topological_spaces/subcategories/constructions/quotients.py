r"""Quotient construction category for topological spaces."""

from __future__ import annotations

from ....cat import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Topological quotient spaces with the quotient topology.

    Canonical chain: ``TopologicalSpaces().Quotients()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
