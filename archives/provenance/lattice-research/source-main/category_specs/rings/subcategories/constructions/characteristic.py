r"""Rings of fixed characteristic."""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, final, override

from sage.rings.integer import Integer

from .parameterized import _Category_over_base_integer


class _CharacteristicRings(_Category_over_base_integer):
    r"""Canonical chain: ``Rings().Characteristic(n)``."""

    parameter_name = "characteristic"

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.characteristic() == self.characteristic()

    @final
    def characteristic(self) -> Integer:
        return self.base_integer()

    @override
    @final
    def _repr_object_names(self) -> str:
        return (
            f"{self.base_category()._repr_object_names()} "
            f"of characteristic {self.characteristic()}"
        )

    class ParentMethods:
        @abstractmethod
        def characteristic(self) -> Integer: ...

    class ElementMethods: ...
