r"""Stratified stacks and varieties built from compactifications."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ...categories.membership import _object_base
from ...categories.stratified import StratifiedSpaces, StratifiedStacks
from ...objects.gamma import StableGraphCategory
from .indexing import DualGraphType

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from ..geometry.compactification import Compactification
    from ..moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver
    from ..moduli.stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver
    from ...objects.graph_types import StableGraphTypes


class BoundaryStack:
    r"""Boundary `\partial \overline X` of a compactification."""

    __slots__ = ("_compactification", "_reduced")

    def __init__(self, compactification: Compactification, reduced: bool = True) -> None:
        self._compactification = compactification
        self._reduced = bool(reduced)

    def compactification(self) -> Compactification:
        return self._compactification

    def parent_stack(self) -> DeligneMumfordModuliStack | DeligneMumfordModuliStackOver:
        return self._compactification.codomain()

    def is_reduced(self) -> bool:
        return self._reduced

    def category(self) -> object:
        return StratifiedStacks(_object_base(self.parent_stack()))

    def stratify(
        self,
        by: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> StratifiedStack:
        return StratifiedStack(self.parent_stack(), by, order=order, backend=backend)


class StratifiedStack:
    r"""Stratified stack with dual-graph indexing via `\Gamma_{g,n}`."""

    __slots__ = ("_stack", "_indexer", "_order", "_backend", "_gamma")

    def __init__(
        self,
        stack: DeligneMumfordModuliStack | DeligneMumfordModuliStackOver,
        indexer: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> None:
        assert order in ("specialization", "closure"), f"unknown order {order!r}"
        self._stack = stack
        self._indexer = indexer
        self._order = order
        self._backend = backend
        self._gamma = StableGraphCategory(stack.genus(), stack.number_of_markings())

    def parent_stack(self) -> DeligneMumfordModuliStack | DeligneMumfordModuliStackOver:
        return self._stack

    def indexing_category(self) -> StableGraphTypes:
        return self._indexer.stable_graphs(self._stack.genus(), self._stack.number_of_markings())

    def category(self) -> object:
        return StratifiedStacks(_object_base(self._stack))

    def stratification_poset(self, order: str | None = None) -> FinitePoset:
        order = self._order if order is None else order
        if order == "specialization":
            return self._gamma.specialization_poset()
        if order == "closure":
            return self._gamma.closure_poset()
        raise ValueError(f"unknown order {order!r}")

    def combinatorial_stratification(self) -> StableGraphCategory:
        return self._gamma


class StratifiedVariety:
    r"""Stratified coarse moduli variety (incidence poset matches stack side)."""

    __slots__ = ("_coarse", "_indexer", "_order", "_backend")

    def __init__(
        self,
        coarse: CoarseModuliScheme | CoarseModuliSchemeOver,
        indexer: DualGraphType,
        order: str = "specialization",
        backend: str = "auto",
    ) -> None:
        self._coarse = coarse
        self._indexer = indexer
        self._order = order
        self._backend = backend

    def parent_scheme(self) -> CoarseModuliScheme | CoarseModuliSchemeOver:
        return self._coarse

    def indexing_category(self) -> StableGraphTypes:
        return self._indexer.stable_graphs(self._coarse.genus(), self._coarse.number_of_markings())

    def category(self) -> object:
        return StratifiedSpaces(_object_base(self._coarse))

    def stratification_poset(self, order: str | None = None) -> FinitePoset:
        from ..moduli.instances import Mbar_gn

        stack = Mbar_gn(self._coarse.genus(), self._coarse.number_of_markings())
        stack_side = StratifiedStack(stack, self._indexer, order=order or self._order, backend=self._backend)
        return stack_side.stratification_poset(order=order)
