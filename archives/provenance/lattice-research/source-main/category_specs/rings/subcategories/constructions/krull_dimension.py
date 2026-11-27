r"""Rings of fixed Krull dimension."""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, final, override

from sage.rings.integer import Integer

from .parameterized import _Category_over_base_integer


class _KrullDimension(_Category_over_base_integer):
    r"""Canonical chain: ``Rings().KrullDimension(n)``."""

    parameter_name = "Krull dimension"

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.krull_dimension() == self.dimension()

    @final
    def dimension(self) -> Integer:
        return self.base_integer()

    @override
    @final
    def _repr_object_names(self) -> str:
        return (
            f"{self.base_category()._repr_object_names()} "
            f"of Krull dimension {self.dimension()}"
        )

    class ParentMethods:
        @abstractmethod
        def krull_dimension(self) -> Integer: ...

    class ElementMethods: ...
