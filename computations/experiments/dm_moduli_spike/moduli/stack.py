r"""Deligne--Mumford moduli stacks as first-class geometric objects."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.integer_ring import ZZ
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.stacks import DeligneMumfordStacks
from ..moduli.coarse import CoarseModuliMap, CoarseModuliScheme, CoarseModuliSchemeOver, coarse_moduli_map
from ..moduli.families import FamiliesOver
from ..moduli.problems import ModuliProblem, SmoothPointedCurves, StablePointedCurves

if TYPE_CHECKING:
    from ..geometry.stacks import Compactification


class DeligneMumfordModuliStack(UniqueRepresentation):
    r"""Universal Deligne--Mumford stack `\mathcal M_{g,n} \to \mathrm{Spec}(\mathbb Z)`."""

    __slots__ = ("_g", "_n", "_proper", "_problem")

    def __init__(
        self,
        g: int,
        n: int,
        *,
        proper: bool = False,
        problem: ModuliProblem | None = None,
    ) -> None:
        g = int(g)
        n = int(n)
        assert g >= 0 and n >= 0, f"(g, n) must be nonnegative; (g, n)=({g}, {n})"
        assert 2 * g - 2 + n > 0, f"(g, n)=({g}, {n}) is not in the stable range 2g - 2 + n > 0"
        self._g = g
        self._n = n
        self._proper = bool(proper)
        if problem is None:
            problem = StablePointedCurves(g, n) if self._proper else SmoothPointedCurves(g, n)
        self._problem = problem

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def base_scheme(self) -> AffineScheme:
        r"""Target of the structure morphism: `\mathrm{Spec}(\mathbb Z)`."""
        return spec(ZZ)

    def is_proper(self) -> bool:
        return self._proper

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def is_smooth(self) -> bool:
        return True

    def is_irreducible(self) -> bool:
        return True

    def is_separated(self) -> bool:
        return True

    def category(self) -> object:
        return DeligneMumfordStacks(self.base_scheme())

    def moduli_problem(self) -> ModuliProblem:
        return self._problem

    def base_change(self, S: AffineScheme) -> DeligneMumfordModuliStackOver:
        r"""Pullback along canonical `S \to \mathrm{Spec}(\mathbb Z)`."""
        if not isinstance(S, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(S)}")
        check_z_scheme(S)
        return DeligneMumfordModuliStackOver(self, S)

    def s_points(self, S: AffineScheme) -> DeligneMumfordModuliStackOver:
        r"""`S`-points `\mathrm{Hom}(S, \mathcal M_{g,n})`; same data as :meth:`base_change`."""
        return self.base_change(S)

    def objects_over(self, S: AffineScheme) -> FamiliesOver:
        return FamiliesOver(self.base_change(S))

    def coarse_scheme(self) -> CoarseModuliScheme:
        return CoarseModuliScheme(self._g, self._n, compact=self._proper)

    def coarse_moduli_map(self) -> CoarseModuliMap:
        return coarse_moduli_map(self)

    def compactification(
        self,
        by: ModuliProblem | None = None,
        kind: str = "Deligne-Mumford",
    ) -> Compactification:
        from ..geometry.stacks import Compactification

        if self._proper:
            raise ValueError("already a compactified moduli stack")
        assert kind == "Deligne-Mumford", f"unsupported compactification kind {kind!r}"
        problem = by if by is not None else StablePointedCurves(self._g, self._n)
        codomain = DeligneMumfordModuliStack(self._g, self._n, proper=True, problem=problem)
        return Compactification(self, codomain, problem, kind=kind)

    def compactify(self, by: ModuliProblem | None = None, kind: str = "Deligne-Mumford") -> DeligneMumfordModuliStack:
        codomain = self.compactification(by=by, kind=kind).codomain()
        assert isinstance(codomain, DeligneMumfordModuliStack), f"compactification codomain must be DeligneMumfordModuliStack; found {type(codomain)!r}"
        return codomain

    def _repr_(self) -> str:
        name = "Mbar" if self._proper else "M"
        return f"DM stack {name}({self._g}, {self._n}) over Spec(ZZ)"


class DeligneMumfordModuliStackOver(UniqueRepresentation):
    r"""Base change of a universal stack along canonical `S \to \mathrm{Spec}(\mathbb Z)`."""

    __slots__ = ("_universal", "_over")

    def __init__(self, universal: DeligneMumfordModuliStack, over: AffineScheme) -> None:
        if not isinstance(universal, DeligneMumfordModuliStack):
            raise TypeError(f"expected DeligneMumfordModuliStack; found {type(universal)}")
        if not isinstance(over, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(over)}")
        check_z_scheme(over)
        self._universal = universal
        self._over = over

    def universal(self) -> DeligneMumfordModuliStack:
        return self._universal

    def over_scheme(self) -> AffineScheme:
        r"""The base `S` of the pullback (`\mathrm{Sch}/S`)."""
        return self._over

    def genus(self) -> int:
        return self._universal.genus()

    def number_of_markings(self) -> int:
        return self._universal.number_of_markings()

    def is_proper(self) -> bool:
        return self._universal.is_proper()

    def dimension(self) -> int:
        return self._universal.dimension()

    def is_smooth(self) -> bool:
        return self._universal.is_smooth()

    def is_irreducible(self) -> bool:
        return self._universal.is_irreducible()

    def is_separated(self) -> bool:
        return self._universal.is_separated()

    def category(self) -> object:
        return DeligneMumfordStacks(self._over)

    def moduli_problem(self) -> ModuliProblem:
        return self._universal.moduli_problem()

    def objects_over(self) -> FamiliesOver:
        return FamiliesOver(self)

    def coarse_scheme(self) -> CoarseModuliSchemeOver:
        return CoarseModuliSchemeOver(self._universal.coarse_scheme(), self._over)

    def coarse_moduli_map(self) -> CoarseModuliMap:
        return coarse_moduli_map(self._universal)

    def compactification(
        self,
        by: ModuliProblem | None = None,
        kind: str = "Deligne-Mumford",
    ) -> Compactification:
        from ..geometry.stacks import Compactification as CompactificationCls

        compact = self._universal.compactification(by=by, kind=kind)
        inner_codomain = compact.codomain()
        assert isinstance(inner_codomain, DeligneMumfordModuliStack), f"universal compactification codomain must be DeligneMumfordModuliStack; found {type(inner_codomain)!r}"
        codomain = DeligneMumfordModuliStackOver(inner_codomain, self._over)
        return CompactificationCls(self, codomain, compact.moduli_problem(), kind=kind)

    def compactify(self, by: ModuliProblem | None = None, kind: str = "Deligne-Mumford") -> DeligneMumfordModuliStackOver:
        codomain = self.compactification(by=by, kind=kind).codomain()
        assert isinstance(codomain, DeligneMumfordModuliStackOver), f"compactification codomain must be DeligneMumfordModuliStackOver; found {type(codomain)!r}"
        return codomain

    def _repr_(self) -> str:
        name = "Mbar" if self.is_proper() else "M"
        return f"DM stack {name}({self.genus()}, {self.number_of_markings()}) over {self._over}"
