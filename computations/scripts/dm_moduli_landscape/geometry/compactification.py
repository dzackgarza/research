r"""Compactification as an open immersion into a proper object."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .morphisms import OpenImmersion

if TYPE_CHECKING:
    from ..moduli.problems import ModuliProblem
    from ..moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver
    from ..stratification.indexing import DualGraphType
    from ..stratification.stratified import BoundaryStack


class Compactification:
    r"""Compactification data `j : X \hookrightarrow \overline X` with proper codomain."""

    __slots__ = ("_domain", "_codomain", "_problem")

    def __init__(
        self,
        domain: DeligneMumfordModuliStack | DeligneMumfordModuliStackOver,
        codomain: DeligneMumfordModuliStack | DeligneMumfordModuliStackOver,
        problem: ModuliProblem,
    ) -> None:
        self._domain = domain
        self._codomain = codomain
        self._problem = problem

    def domain(self) -> DeligneMumfordModuliStack | DeligneMumfordModuliStackOver:
        return self._domain

    def codomain(self) -> DeligneMumfordModuliStack | DeligneMumfordModuliStackOver:
        return self._codomain

    def moduli_problem(self) -> ModuliProblem:
        return self._problem

    def open_immersion(self) -> OpenImmersion:
        return OpenImmersion(self._domain, self._codomain)

    def boundary(self, reduced: bool = True) -> BoundaryStack:
        from ..stratification.stratified import BoundaryStack

        return BoundaryStack(self, reduced=reduced)

    def stratify(self, by: DualGraphType, order: str = "specialization", backend: str = "auto") -> object:
        return self.boundary(reduced=True).stratify(by=by, order=order, backend=backend)
