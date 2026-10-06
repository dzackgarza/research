"""Finite weighted graph cards.

A graph card stores vertices, edges, arbitrary decorations and any cited
classification labels. Mathematical recognition of Coxeter, Dynkin, Satake,
Vinberg or other diagram classes belongs to the research preamble; latticedb
does not derive those labels from the decorations.
"""

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
    """One weighted-graph card with stored classification labels."""

    slug: Slug
    name: str = Field(min_length=1)
    properties: Annotated[tuple[str, ...], Field(strict=False)] = ()
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
        if len(self.properties) != len(set(self.properties)):
            raise PydanticCustomError(
                "graph_property_duplicate", "graph property labels must be unique"
            )
        return self
