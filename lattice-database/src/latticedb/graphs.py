"""Finite weighted graph cards with mathematical interpretation delegated to the preamble."""

from __future__ import annotations

from typing import Annotated, Self

from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import Record, Slug, Yaml


class GraphVertex(Record):
    id: str = Field(min_length=1)
    weight: Yaml = None


class GraphEdge(Record):
    id: str = Field(min_length=1)
    source: str = Field(min_length=1)
    target: str = Field(min_length=1)
    relation: str = Field(min_length=1)
    directed: bool = False
    weight: Yaml = None


class WeightedGraph(Record):
    """One graph card; diagram mathematics is owned by the research preamble."""

    slug: Slug
    name: str = Field(min_length=1)
    vertices: Annotated[tuple[GraphVertex, ...], Field(strict=False)]
    edges: Annotated[tuple[GraphEdge, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_incidence(self) -> Self:
        ids = [vertex.id for vertex in self.vertices]
        if len(ids) != len(set(ids)):
            raise PydanticCustomError(
                "graph_vertex_duplicate", "graph vertex identifiers must be unique"
            )
        edge_ids = [edge.id for edge in self.edges]
        if len(edge_ids) != len(set(edge_ids)):
            raise PydanticCustomError(
                "graph_edge_duplicate", "graph edge identifiers must be unique"
            )
        if any(edge.source not in ids or edge.target not in ids for edge in self.edges):
            raise PydanticCustomError(
                "graph_endpoint", "each edge endpoint must be a vertex of the graph"
            )
        return self

    def _invariants(self):
        from dzack_research.preamble.categories.weighted_graph_invariants import (
            WeightedEdgeData,
            WeightedGraphInvariants,
            WeightedVertexData,
        )

        return WeightedGraphInvariants(
            tuple(WeightedVertexData(v.id, v.weight) for v in self.vertices),
            tuple(
                WeightedEdgeData(
                    e.id, e.source, e.target, e.relation, e.directed, e.weight
                )
                for e in self.edges
            ),
        )

    def is_coxeter(self) -> bool:
        return self._invariants().is_coxeter()

    def cartan_matrix(self) -> tuple[tuple[int, ...], ...] | None:
        return self._invariants().cartan_matrix()

    def is_dynkin(self) -> bool:
        return self._invariants().is_dynkin()

    def is_simply_laced(self) -> bool:
        return self._invariants().is_simply_laced()

    def is_rational_coxeter_vinberg(self) -> bool:
        return self._invariants().is_rational_coxeter_vinberg()

    def is_satake(self) -> bool:
        return self._invariants().is_satake()

    def properties(self) -> tuple[str, ...]:
        """The names of the diagram classes the card belongs to, in the order the site lists them."""
        invariants = self._invariants()
        classes = (
            ("Coxeter", invariants.is_coxeter()),
            ("Dynkin", invariants.is_dynkin()),
            ("simply laced", invariants.is_simply_laced()),
            ("Satake", invariants.is_satake()),
            ("rational Coxeter–Vinberg", invariants.is_rational_coxeter_vinberg()),
        )
        return tuple(name for name, holds in classes if holds)
