r"""Coarse moduli spaces and morphisms."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.structure.unique_representation import UniqueRepresentation

from ..categories.schemes import AlgebraicSpaces, Varieties
from ..geometry.morphisms import CoarseModuliMap

if TYPE_CHECKING:
    from ..categories.base import ModuliBase
    from .stack import DeligneMumfordModuliStack


class CoarseModuliSpace(UniqueRepresentation):
    r"""Coarse moduli space `M_{g,n}` or `\overline M_{g,n}` for a moduli stack."""

    __slots__ = ("_g", "_n", "_base", "_compact")

    def __init__(self, g: int, n: int, base: ModuliBase, *, compact: bool) -> None:
        self._g = int(g)
        self._n = int(n)
        self._base = base
        self._compact = bool(compact)

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def base(self) -> ModuliBase:
        return self._base

    def is_compact(self) -> bool:
        return self._compact

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def category(self) -> object:
        return Varieties(self._base)

    def is_quasiprojective(self) -> bool:
        return not self._compact

    def is_normal(self) -> bool:
        return self._compact

    def is_projective(self) -> bool:
        return self._compact

    def boundary(self) -> CoarseBoundary:
        return CoarseBoundary(self)

    def _repr_(self) -> str:
        prefix = "Mbar" if self._compact else "M"
        return f"{prefix}({self._g}, {self._n}) over {self._base}"


class CoarseBoundary:
    r"""Boundary of a coarse moduli variety."""

    __slots__ = ("_coarse",)

    def __init__(self, coarse: CoarseModuliSpace) -> None:
        self._coarse = coarse

    def parent_space(self) -> CoarseModuliSpace:
        return self._coarse

    def stratify(self, by: object, order: str = "specialization") -> object:
        from ..stratification.stratified import StratifiedVariety
        from ..stratification.indexing import DualGraphType

        if not isinstance(by, DualGraphType):
            raise TypeError(f"expected DualGraphType; found {type(by)}")
        return StratifiedVariety(self._coarse, by, order=order)


def coarse_moduli_map(stack: DeligneMumfordModuliStack) -> CoarseModuliMap:
    coarse = stack.coarse_space()
    return CoarseModuliMap(stack, coarse)
