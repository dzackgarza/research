r"""Subobject construction category for posets."""

from __future__ import annotations

from ....cat import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Subposets with the induced order.

    Canonical chain: ``Posets().Subobjects()``.
    """

    class ParentMethods: ...

    class ElementMethods: ...
