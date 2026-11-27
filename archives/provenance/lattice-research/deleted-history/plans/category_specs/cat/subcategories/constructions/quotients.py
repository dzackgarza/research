r"""Quotient construction category for categories."""

from __future__ import annotations

from ... import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Quotient categories.

    Canonical chain: ``Cat().Quotients()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
