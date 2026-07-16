# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Any, Literal

from typing_extensions import Self

from sage.graphs.graph_plot import GraphPlot
from sage.groups.perm_gps.permgroup import PermutationGroup_generic

type GraphOption = (
    bool
    | int
    | float
    | str
    | list[str]
    | dict[Hashable, Sequence[float]]
    | dict[Hashable, str]
    | dict[int, str]
    | dict[int, Sequence[float]]
)
type GraphEdge = tuple[Hashable, Hashable, str | int | float | None]

class Graph:
    def __init__(self, *args: Any, **kwds: Any) -> None: ...
    def vertices(self, sort: bool = ...) -> list[Any]: ...
    def edges(self, sort: bool = ..., labels: bool = ...) -> list[Any]: ...
    def is_connected(self) -> bool: ...
    def is_isomorphic(self, other: Graph) -> bool: ...
    def connected_components(self, sort: bool = ...) -> list[list[Any]]: ...
    def __len__(self) -> int: ...
    def add_edge(
        self,
        u: Hashable,
        v: Hashable | None = ...,
        label: Hashable | None = ...,
    ) -> None: ...
    def add_vertex(self, name: Hashable | None = ...) -> None: ...
    def edges_incident(
        self,
        vertices: Hashable | Iterable[Hashable] | None = ...,
        labels: bool = ...,
        sort: bool = ...,
    ) -> Sequence[GraphEdge]: ...
    def graphplot(self, **options: GraphOption) -> GraphPlot: ...
    def canonical_label(
        self,
        partition: Sequence[Sequence[Hashable]] | None = ...,
        certificate: Literal[True] = ...,
        edge_labels: bool = ...,
        algorithm: str | None = ...,
        return_graph: bool = ...,
    ) -> tuple[Self, dict[Hashable, int]]: ...
    def automorphism_group(
        self,
        partition: Sequence[Sequence[Hashable]] | None = ...,
        verbosity: int = ...,
        edge_labels: bool = ...,
        order: Literal[False] = ...,
        return_group: Literal[True] = ...,
        orbits: Literal[False] = ...,
        algorithm: str | None = ...,
    ) -> PermutationGroup_generic: ...
    def get_pos(self, dim: int = ...) -> dict[Hashable, Sequence[float]] | None: ...
    def num_verts(self) -> int: ...
    def relabel(self, perm: Sequence[int], inplace: bool = ...) -> Self: ...
    def subgraph(
        self,
        vertices: Hashable | Iterable[Hashable] | None = ...,
        edges: GraphEdge | Iterable[GraphEdge] | None = ...,
        inplace: bool = ...,
        vertex_property: Callable[[Hashable], bool] | None = ...,
        edge_property: Callable[[GraphEdge], bool] | None = ...,
        algorithm: str | None = ...,
        immutable: bool | None = ...,
    ) -> Self: ...
