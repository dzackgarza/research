"""Concrete bilinear module morphism wrappers.

BilinearMorphism — a linear map between formed modules that preserves
or relates the form structure. Wraps a Sage module morphism with
form-awareness for kernel/image/cokernel computation.
"""

from __future__ import annotations

from typing import Any

from sage.categories.morphism import Morphism


class BilinearMorphism(Morphism):
    """Morphism between formed modules — linear map with form preservation."""

    def __init__(self, parent: object, underlying: Any) -> None:
        self._underlying = underlying
        Morphism.__init__(self, parent)

    def _call_(self, x: Any) -> Any:
        return self._underlying(x)

    def domain(self) -> Any:
        return self._underlying.domain()

    def codomain(self) -> Any:
        return self._underlying.codomain()

    def is_injective(self) -> bool:
        return bool(self._underlying.is_injective())

    def is_surjective(self) -> bool:
        return bool(self._underlying.is_surjective())

    def kernel(self) -> Any:
        return self._underlying.kernel()

    def image(self) -> Any:
        return self._underlying.image()

    def cokernel(self) -> Any:
        return self._underlying.cokernel()

    def matrix(self) -> Any:
        if hasattr(self._underlying, "matrix"):
            return self._underlying.matrix()
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"morphism({self.domain()} -> {self.codomain()})"
