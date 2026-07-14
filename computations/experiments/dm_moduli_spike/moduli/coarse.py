r"""Coarse moduli schemes and morphisms."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.integer_ring import ZZ
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.schemes import Varieties

if TYPE_CHECKING:
    from ..geometry.stratification import StratifiedSpace
    from .instances import ModuliStack


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

    def base_change(self, S: AffineScheme) -> CoarseModuliSchemeOver:
        if not isinstance(S, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(S)}")
        check_z_scheme(S)
        return CoarseModuliSchemeOver(self, S)

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
    r"""Base change of a coarse moduli scheme along canonical `S \to \mathrm{Spec}(\mathbb Z)`."""

    __slots__ = ("_universal", "_over")

    def __init__(self, universal: CoarseModuliScheme, over: AffineScheme) -> None:
        if not isinstance(universal, CoarseModuliScheme):
            raise TypeError(f"expected CoarseModuliScheme; found {type(universal)}")
        if not isinstance(over, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(over)}")
        check_z_scheme(over)
        self._universal = universal
        self._over = over

    def universal(self) -> CoarseModuliScheme:
        return self._universal

    def over_scheme(self) -> AffineScheme:
        return self._over

    def genus(self) -> int:
        return self._universal.genus()

    def number_of_markings(self) -> int:
        return self._universal.number_of_markings()

    def base_scheme(self) -> AffineScheme:
        return self._over

    def is_compact(self) -> bool:
        return self._universal.is_compact()

    def dimension(self) -> int:
        return self._universal.dimension()

    def category(self) -> object:
        return Varieties(self._over)

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
        return f"{prefix}({self.genus()}, {self.number_of_markings()}) over {self._over}"


def _coarse_stratified_space(coarse: CoarseModuliScheme, by: object, order: str) -> StratifiedSpace:
    from ..geometry.stratification import (
        StableDualGraph,
        StratifiedSpace,
        build_dual_graph_stratification,
    )
    from .instances import M_gn, Mbar_gn

    if not isinstance(by, StableDualGraph):
        raise TypeError(f"expected StableDualGraph; found {type(by)}")
    if order not in ("specialization", "closure"):
        raise ValueError(f"unknown order {order!r}")
    g, n = coarse.genus(), coarse.number_of_markings()
    stack = Mbar_gn(g, n) if coarse.is_compact() else M_gn(g, n)
    Sigma = build_dual_graph_stratification(stack, compact=coarse.is_compact())
    return StratifiedSpace(coarse, Sigma)


class CoarseBoundary:
    r"""Boundary of a coarse moduli scheme (positive-codimension strata)."""

    __slots__ = ("_coarse",)

    def __init__(self, coarse: CoarseModuliScheme) -> None:
        self._coarse = coarse

    def parent_scheme(self) -> CoarseModuliScheme:
        return self._coarse

    def stratify(self, by: object, order: str = "specialization") -> StratifiedSpace:
        return _coarse_stratified_space(self._coarse, by, order)


class CoarseBoundaryOver:
    r"""Boundary of a base-changed coarse moduli scheme."""

    __slots__ = ("_coarse",)

    def __init__(self, coarse: CoarseModuliSchemeOver) -> None:
        self._coarse = coarse

    def parent_scheme(self) -> CoarseModuliSchemeOver:
        return self._coarse

    def stratify(self, by: object, order: str = "specialization") -> StratifiedSpace:
        return _coarse_stratified_space(self._coarse.universal(), by, order)


def coarse_moduli_map(stack: ModuliStack) -> object:
    r"""Coarse moduli morphism; delegates to :meth:`ModuliStack.coarse_moduli_morphism`."""
    return stack.coarse_moduli_morphism()


CoarseModuliSpace = CoarseModuliScheme
