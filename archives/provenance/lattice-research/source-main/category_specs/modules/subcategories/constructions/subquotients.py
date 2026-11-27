r"""Subquotient construction category for modules."""

from __future__ import annotations

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Module objects obtained as subobjects of quotients or quotients of subobjects.

    Canonical chain: ``Modules(R).Subquotients()``.
    """

    class ParentMethods: ...

    class ElementMethods: ...
