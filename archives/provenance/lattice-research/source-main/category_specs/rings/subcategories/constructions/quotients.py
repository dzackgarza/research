r"""Ring quotients."""

from __future__ import annotations

from typing import final, override

from ....cat import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Ring quotients in the current ring category.

    Canonical chain: ``Rings().Quotients()``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"quotients of {self.base_category()._repr_object_names()}"

    class ParentMethods: ...

    class ElementMethods: ...
