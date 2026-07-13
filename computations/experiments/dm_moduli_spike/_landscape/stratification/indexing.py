r"""Indexing systems for stratifications."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset

    from ...objects.graph_types import StableGraphTypes


class DualGraphType:
    r"""Stratification indexer: stable dual graphs of type `(g, n)`."""

    def stable_graphs(self, g: int, n: int) -> StableGraphTypes:
        from ...objects.graph_types import StableGraphTypes

        return StableGraphTypes(g, n)

    def thinification(self, g: int, n: int, order: str = "specialization", backend: str = "auto") -> FinitePoset:
        from ...objects.gamma import StableGraphCategory

        gamma = StableGraphCategory(g, n)
        if order == "specialization":
            return gamma.specialization_poset()
        if order == "closure":
            return gamma.closure_poset()
        raise ValueError(f"unknown order {order!r}")

    def __repr__(self) -> str:
        return "DualGraphType()"
