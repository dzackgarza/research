r"""Ring subobjects."""

from __future__ import annotations

from typing import final, override

from ....cat import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Ring subobjects: subrings in the current ring category.

    Canonical chain: ``Rings().Subobjects()``.
    """

    @override
    @final
    def _repr_object_names(self):
        return f"subobjects of {self.base_category()._repr_object_names()}"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
