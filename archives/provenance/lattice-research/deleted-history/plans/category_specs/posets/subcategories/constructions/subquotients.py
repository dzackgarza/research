r"""Subquotient construction category for posets."""

from __future__ import annotations

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Posets obtained as subposets of quotients or quotients of subposets.

    Canonical chain: ``Posets().Subquotients()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
