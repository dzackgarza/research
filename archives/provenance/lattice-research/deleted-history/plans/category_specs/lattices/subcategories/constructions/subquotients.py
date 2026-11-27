r"""Subquotient construction category for lattices."""

from __future__ import annotations

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Lattice objects obtained as subobjects of quotients or quotients of subobjects.

    Canonical chain: ``Lattices(R).Subquotients()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
