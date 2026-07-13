r"""Coarse moduli schemes and morphisms."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.integer_ring import ZZ
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, SchemeOver, spec
from ..categories.schemes import Varieties
from ..geometry.morphisms import CoarseModuliMap

if TYPE_CHECKING:
    from .stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver


class CoarseModuliScheme(UniqueRepresentation):
    r"""Universal coarse moduli scheme `M_{g,n} \to \mathrm{Spec}(\mathbb Z)`."""

    __slots__ = ("_g", "_n", "_compact")

    def __init__(
        self,
        g: int,
        n: int,
        *,
        compact: bool,
    ) -> None:
        self._g = int(g)
        self._n = int(n)
        self._compact = bool(compact)

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def base_scheme(self) -> AffineScheme:
        return spec(ZZ)

    def base_change(self, base: SchemeOver) -> CoarseModuliSchemeOver:
        if not isinstance(base, SchemeOver):
            raise TypeError(f"expected SchemeOver; found {type(base)}")
        return CoarseModuliSchemeOver(self, base)

    def is_compact(self) -> bool:
        return self._compact

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def category(self) -> object:
        return Varieties(self.base_scheme())

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
        return f"{prefix}({self._g}, {self._n}) over Spec(ZZ)"


class CoarseModuliSchemeOver(UniqueRepresentation):
    r"""Base change of a coarse moduli scheme to `S \in \mathrm{Sch}/B`."""

    __slots__ = ("_universal", "_base")

    def __init__(self, universal: CoarseModuliScheme, base: SchemeOver) -> None:
        if not isinstance(universal, CoarseModuliScheme):
            raise TypeError(f"expected CoarseModuliScheme; found {type(universal)}")
        if not isinstance(base, SchemeOver):
            raise TypeError(f"expected SchemeOver; found {type(base)}")
        self._universal = universal
        self._base = base

    def universal(self) -> CoarseModuliScheme:
        return self._universal

    def base(self) -> SchemeOver:
        return self._base

    def genus(self) -> int:
        return self._universal.genus()

    def number_of_markings(self) -> int:
        return self._universal.number_of_markings()

    def base_scheme(self) -> AffineScheme:
        return self._base.base()

    def is_compact(self) -> bool:
        return self._universal.is_compact()

    def dimension(self) -> int:
        return self._universal.dimension()

    def category(self) -> object:
        return Varieties(self.base_scheme())

    def is_quasiprojective(self) -> bool:
        return self._universal.is_quasiprojective()

    def is_normal(self) -> bool:
        return self._universal.is_normal()

    def is_projective(self) -> bool:
        return self._universal.is_projective()

    def boundary(self) -> CoarseBoundaryOver:
        return CoarseBoundaryOver(self)

    def _repr_(self) -> str:
        prefix = "Mbar" if self.is_compact() else "M"
        return f"{prefix}({self.genus()}, {self.number_of_markings()}) over {self._base}"


class CoarseBoundary:
    r"""Boundary of a coarse moduli scheme (positive-codimension strata)."""

    __slots__ = ("_coarse",)

    def __init__(self, coarse: CoarseModuliScheme) -> None:
        self._coarse = coarse

    def parent_scheme(self) -> CoarseModuliScheme:
        return self._coarse

    def stratify(self, by: object, order: str = "specialization") -> object:
        from ..stratification.indexing import DualGraphType
        from ..stratification.stratified import StratifiedVariety

        if not isinstance(by, DualGraphType):
            raise TypeError(f"expected DualGraphType; found {type(by)}")
        return StratifiedVariety(self._coarse, by, order=order)


class CoarseBoundaryOver:
    r"""Boundary of a base-changed coarse moduli scheme."""

    __slots__ = ("_coarse",)

    def __init__(self, coarse: CoarseModuliSchemeOver) -> None:
        self._coarse = coarse

    def parent_scheme(self) -> CoarseModuliSchemeOver:
        return self._coarse

    def stratify(self, by: object, order: str = "specialization") -> object:
        from ..stratification.indexing import DualGraphType
        from ..stratification.stratified import StratifiedVariety

        if not isinstance(by, DualGraphType):
            raise TypeError(f"expected DualGraphType; found {type(by)}")
        return StratifiedVariety(self._coarse.universal(), by, order=order)


def coarse_moduli_map(stack: DeligneMumfordModuliStack | DeligneMumfordModuliStackOver) -> CoarseModuliMap:
    from .stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver

    if isinstance(stack, DeligneMumfordModuliStackOver):
        coarse = stack.coarse_scheme()
        return CoarseModuliMap(stack.universal(), coarse.universal())
    coarse = stack.coarse_scheme()
    return CoarseModuliMap(stack, coarse)


CoarseModuliSpace = CoarseModuliScheme
