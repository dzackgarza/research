r"""Indexing systems for stratifications."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from ..objects.graph_types import StableGraphTypes


class DualGraphType:
    r"""Stratification indexer: stable dual graphs of type `(g, n)`."""

    def stable_graphs(self, g: int, n: int) -> StableGraphTypes:
        from ..objects.graph_types import StableGraphTypes

        return StableGraphTypes(g, n)

    def thinification(self, g: int, n: int, order: str = "specialization", backend: str = "auto") -> FinitePoset:
        from ..stratification.stratified import StratifiedStack
        from ..moduli.instances import Mbar_gn

        stack = Mbar_gn(g, n)
        boundary = stack.compactification().boundary()
        stratified = boundary.stratify(by=self, order=order, backend=backend)
        return stratified.stratification_poset(order=order)

    def __repr__(self) -> str:
        return "DualGraphType()"
