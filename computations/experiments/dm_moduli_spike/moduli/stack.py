r"""Deligne--Mumford moduli stacks as first-class geometric objects."""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import ModuliBase
from ..categories import default_base
from ..categories.stacks import DeligneMumfordStacks
from ..moduli.coarse import CoarseModuliMap, CoarseModuliSpace, coarse_moduli_map
from ..moduli.families import FamiliesOver
from ..moduli.problems import ModuliProblem, SmoothPointedCurves, StablePointedCurves


class DeligneMumfordModuliStack(UniqueRepresentation):
    r"""Deligne--Mumford stack `\mathcal M_{g,n}` or `\overline{\mathcal M}_{g,n}`.

    The open stack represents smooth pointed curves; the proper stack represents
    stable pointed curves after Deligne--Mumford compactification.
    """

    __slots__ = ("_g", "_n", "_base", "_proper", "_problem")

    def __init__(
        self,
        g: int,
        n: int,
        base: ModuliBase | None = None,
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
        self._base = base if base is not None else default_base()
        self._proper = bool(proper)
        if problem is None:
            problem = StablePointedCurves(g, n) if self._proper else SmoothPointedCurves(g, n)
        self._problem = problem

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def base(self) -> ModuliBase:
        return self._base

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
        return DeligneMumfordStacks(self._base)

    def moduli_problem(self) -> ModuliProblem:
        return self._problem

    def objects_over(self, base_scheme: object) -> FamiliesOver:
        return FamiliesOver(self, base_scheme)

    def coarse_space(self) -> CoarseModuliSpace:
        return CoarseModuliSpace(self._g, self._n, self._base, compact=self._proper)

    def coarse_moduli_map(self) -> CoarseModuliMap:
        return coarse_moduli_map(self)

    def compactification(
        self,
        by: ModuliProblem | None = None,
        kind: str = "Deligne-Mumford",
    ) -> object:
        from ..geometry.compactification import Compactification

        if self._proper:
            raise ValueError("already a compactified moduli stack")
        assert kind == "Deligne-Mumford", f"unsupported compactification kind {kind!r}"
        problem = by if by is not None else StablePointedCurves(self._g, self._n)
        codomain = DeligneMumfordModuliStack(self._g, self._n, self._base, proper=True, problem=problem)
        return Compactification(self, codomain, problem)

    def compactify(self, by: ModuliProblem | None = None, kind: str = "Deligne-Mumford") -> DeligneMumfordModuliStack:
        return self.compactification(by=by, kind=kind).codomain()

    def _repr_(self) -> str:
        name = "Mbar" if self._proper else "M"
        return f"DM stack {name}({self._g}, {self._n}) over {self._base}"
