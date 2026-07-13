r"""Stratified stacks and varieties built from compactifications."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..categories.stratified import StratifiedSpaces, StratifiedStacks
from ..objects.model import DMCompactificationModel
from .indexing import DualGraphType

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from ..geometry.compactification import Compactification
    from ..moduli.coarse import CoarseModuliSpace
    from ..moduli.stack import DeligneMumfordModuliStack
    from ..objects.graph_types import StableGraphTypes


class BoundaryStack:
    r"""Boundary `\partial \overline X` of a compactification."""

    __slots__ = ("_compactification", "_reduced")

    def __init__(self, compactification: Compactification, reduced: bool = True) -> None:
        self._compactification = compactification
        self._reduced = bool(reduced)

    def compactification(self) -> Compactification:
        return self._compactification

    def parent_stack(self) -> DeligneMumfordModuliStack:
        return self._compactification.codomain()

    def is_reduced(self) -> bool:
        return self._reduced

    def category(self) -> object:
        return StratifiedStacks(self.parent_stack().base().sage_ring())

    def stratify(
        self,
        by: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> StratifiedStack:
        return StratifiedStack(self.parent_stack(), by, order=order, backend=backend)


class StratifiedStack:
    r"""Stratified stack with dual-graph indexing category."""

    __slots__ = ("_stack", "_indexer", "_order", "_backend", "_combinatorial")

    def __init__(
        self,
        stack: DeligneMumfordModuliStack,
        indexer: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> None:
        assert order in ("specialization", "closure"), f"unknown order {order!r}"
        self._stack = stack
        self._indexer = indexer
        self._order = order
        self._backend = backend
        self._combinatorial = DMCompactificationModel(stack.genus(), stack.number_of_markings()).stratification(
            backend=backend
        )

    def parent_stack(self) -> DeligneMumfordModuliStack:
        return self._stack

    def indexing_category(self) -> StableGraphTypes:
        return self._indexer.stable_graphs(self._stack.genus(), self._stack.number_of_markings())

    def category(self) -> object:
        return StratifiedStacks(self._stack.base())

    def stratification_poset(self, order: str | None = None) -> FinitePoset:
        order = self._order if order is None else order
        if order == "specialization":
            return self._combinatorial.specialization_poset().sage_poset()
        if order == "closure":
            return self._combinatorial.closure_poset().sage_poset()
        raise ValueError(f"unknown order {order!r}")

    def combinatorial_stratification(self) -> object:
        return self._combinatorial


class StratifiedVariety:
    r"""Stratified coarse moduli variety (incidence poset matches stack side)."""

    __slots__ = ("_coarse", "_indexer", "_order", "_backend")

    def __init__(
        self,
        coarse: CoarseModuliSpace,
        indexer: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> None:
        self._coarse = coarse
        self._indexer = indexer
        self._order = order
        self._backend = backend

    def parent_space(self) -> CoarseModuliSpace:
        return self._coarse

    def indexing_category(self) -> StableGraphTypes:
        return self._indexer.stable_graphs(self._coarse.genus(), self._coarse.number_of_markings())

    def category(self) -> object:
        return StratifiedSpaces(self._coarse.base())

    def stratification_poset(self, order: str | None = None) -> FinitePoset:
        from ..moduli.instances import Mbar_gn

        stack_side = StratifiedStack(
            Mbar_gn(self._coarse.genus(), self._coarse.number_of_markings(), self._coarse.base()),
            self._indexer,
            order=order or self._order,
            backend=self._backend,
        )
        return stack_side.stratification_poset(order=order)
