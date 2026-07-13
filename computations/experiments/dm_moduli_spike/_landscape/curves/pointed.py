r"""Pointed curves and the dual-graph bridge."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...objects.graph_types import StableGraphType
    from ...objects.records import StableGraph


class PointedCurve:
    r"""Base pointed curve over a field."""

    __slots__ = ("_g", "_n")

    def __init__(self, g: int, n: int) -> None:
        self._g = int(g)
        self._n = int(n)

    def arithmetic_genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n


class SmoothPointedCurve(PointedCurve):
    r"""Smooth pointed curve of type `(g, n)`."""

    def is_smooth(self) -> bool:
        return True

    def is_nodal(self) -> bool:
        return False

    def indexes_smooth_stratum(self) -> bool:
        return True


class StablePointedCurve(PointedCurve):
    r"""Stable pointed curve; carries a dual graph when nodal."""

    __slots__ = ("_g", "_n", "_graph_type")

    def __init__(self, g: int, n: int, graph_type: StableGraphType | None = None) -> None:
        super().__init__(g, n)
        self._graph_type = graph_type

    def is_stable(self) -> bool:
        return True

    def is_nodal(self) -> bool:
        return self._graph_type is not None and self._graph_type.num_edges() > 0

    def is_smooth(self) -> bool:
        return self._graph_type is None or self._graph_type.num_edges() == 0

    def dual_graph(self) -> StableGraph:
        from ...objects.graph_types import StableGraphTypes

        if self._graph_type is not None:
            return self._graph_type.canonical_representative()
        parent = StableGraphTypes(self._g, self._n)
        return parent.smooth().canonical_representative()
