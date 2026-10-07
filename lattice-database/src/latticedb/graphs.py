"""Finite weighted graph cards, read as presentations of preamble objects.

A card's decorations present a mathematical object, and every property the site
lists is answered by that object's category:

- root lengths on the vertices and Cartan pairs on the bonds present a root basis
  of a generalized Cartan matrix: the free module on the simple roots with the
  invariant form `b(alpha_i, alpha_i) = q_i`, `b(alpha_i, alpha_j) = a_ij q_i / 2`
  (Kac, *Infinite dimensional Lie algebras*, section 2.1);
- norms on the vertices and Gram entries on the bonds present a family of mirror
  normals with its Gram form (Vinberg, *Hyperbolic reflection groups*, section 2).

Either Gram form determines the Vinberg invariant matrix of the mirrors, and that
matrix determines the Coxeter diagram.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Annotated, Self

from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from dzack_research.preamble.categories.vinberg_invariants import (
    VinbergInvariantMatrices,
)
from dzack_research.preamble.rings import session_ring_objects

from latticedb.model import GramTensor, Record, Slug, Yaml, rational

_SESSION_RINGS = session_ring_objects()
ZZ = _SESSION_RINGS["ZZ"]
QQ = _SESSION_RINGS["QQ"]


class GraphVertex(Record):
    id: str = Field(min_length=1)
    weight: Yaml = None

    def datum(self, key: str) -> Yaml:
        """The decoration `key` of this vertex, or None when the vertex does not state it."""
        match self.weight:
            case dict() if key in self.weight:
                return self.weight[key]
            case _:
                return None


class GraphEdge(Record):
    id: str = Field(min_length=1)
    source: str = Field(min_length=1)
    target: str = Field(min_length=1)
    relation: str = Field(min_length=1)
    directed: bool = False
    weight: Yaml = None

    def datum(self, key: str) -> Yaml:
        """The decoration `key` of this edge, or None when the edge does not state it."""
        match self.weight:
            case dict() if key in self.weight:
                return self.weight[key]
            case _:
                return None


class WeightedGraph(Record):
    """One graph card; the object its decorations present is a preamble object."""

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

    def _bonds(self) -> tuple[GraphEdge, ...]:
        """The edges that join mirrors; a Satake pairing is not a bond."""
        return tuple(edge for edge in self.edges if edge.relation != "satake_pair")

    def _states(self, vertex_key: str, bond_key: str) -> bool:
        """Whether every vertex states `vertex_key` and every edge is a bond stating `bond_key`."""
        return (
            bool(self.vertices)
            and all(vertex.datum(vertex_key) is not None for vertex in self.vertices)
            and all(
                edge.relation == "bond" and edge.datum(bond_key) is not None
                for edge in self._bonds()
            )
        )

    def _presents_root_basis(self) -> bool:
        return self._states("root_length_squared", "cartan")

    def _presents_mirrors(self) -> bool:
        return self._states("norm_squared", "gram")

    def _gram(self, square_key: str, pairing) -> GramTensor:
        """The Gram tensor with the stated squares on the diagonal and `pairing(bond)` off it."""
        position = {vertex.id: index for index, vertex in enumerate(self.vertices)}
        rows = [
            [
                rational(vertex.datum(square_key)) if column == row else 0
                for column in range(len(self.vertices))
            ]
            for row, vertex in enumerate(self.vertices)
        ]
        for bond in self._bonds():
            source, target = position[bond.source], position[bond.target]
            assert not bond.directed and source != target and rows[source][target] == 0, (
                f"{self.slug}: the bond {bond.id} is not one undirected bond between two "
                f"distinct mirrors, so the card states no Gram form"
            )
            rows[source][target] = rows[target][source] = pairing(bond)
        return tuple(tuple(rational(entry) for entry in row) for row in rows)

    def _root_pairing(self, bond: GraphEdge) -> Fraction:
        """`b(alpha_i, alpha_j) = a_ij q_i / 2` for the Cartan pair `(a_ij, a_ji)` of the bond."""
        squares = {vertex.id: rational(vertex.datum("root_length_squared")) for vertex in self.vertices}
        forward, backward = bond.datum("cartan")
        pairing = forward * squares[bond.source] / 2
        assert pairing == backward * squares[bond.target] / 2, (
            f"{self.slug}: the Cartan pair {bond.datum('cartan')} of the bond {bond.id} is not "
            f"symmetrized by the root lengths {squares[bond.source]} and {squares[bond.target]}, "
            f"so the card states no invariant form on its simple roots"
        )
        return pairing

    def _mirror_pairing(self, bond: GraphEdge) -> Fraction:
        return rational(bond.datum("gram"))

    def _gram_form(self):
        """The presented Gram form: the root basis with its invariant form, or the mirror normals.

        None when the decorations present neither.
        """
        match (self._presents_root_basis(), self._presents_mirrors()):
            case (True, _):
                gram = self._gram("root_length_squared", self._root_pairing)
            case (_, True):
                gram = self._gram("norm_squared", self._mirror_pairing)
            case _:
                return None
        return ZZ.free_module(len(gram)).equip_bilinear_form(QQ, gram)

    def cartan_matrix(self) -> tuple[tuple[int, ...], ...] | None:
        """The generalized Cartan matrix the card states, or None when it states none."""
        if not self._presents_root_basis():
            return None
        position = {vertex.id: index for index, vertex in enumerate(self.vertices)}
        rows = [
            [2 if column == row else 0 for column in range(len(self.vertices))]
            for row in range(len(self.vertices))
        ]
        for bond in self._bonds():
            forward, backward = bond.datum("cartan")
            rows[position[bond.source]][position[bond.target]] = int(forward)
            rows[position[bond.target]][position[bond.source]] = int(backward)
        return tuple(tuple(row) for row in rows)

    def properties(self) -> tuple[str, ...]:
        """The names of the diagram classes the card belongs to, in the order the site lists them.

        Every class is answered by a preamble object the card presents:

        - Coxeter: the Coxeter diagram of the mirrors' Vinberg invariant matrix exists;
        - Dynkin: the root basis generates a root system of finite type, that is, its
          Weyl group, the Coxeter group of the diagram, is finite (Kac, Proposition 4.9);
        - simply laced: every bond of the diagram is 2 or 3;
        - Satake: a finite-type root basis whose simple roots carry Satake marks;
        - rational Coxeter–Vinberg: rational mirror normals whose Gram form has negative
          index of inertia one, so that the mirrors bound a polytope in hyperbolic space.
        """
        form = self._gram_form()
        if form is None:
            return ()
        invariants = VinbergInvariantMatrices().from_root_gram(
            form.gram_tensor(), index_set=tuple(vertex.id for vertex in self.vertices)
        )
        # The Coxeter diagram is constructed here, so the card is a Coxeter card; an
        # angle that is not pi/m refuses the construction instead of answering False.
        diagram = invariants.coxeter_diagram()
        dynkin =self._presents_root_basis() and diagram.is_elliptic()
        satake = dynkin and any(vertex.datum("satake") is not None for vertex in self.vertices)
        hyperbolic = self._presents_mirrors() and int(form.signature_pair().second()) == 1
        classes = (
            ("Coxeter", True),
            ("Dynkin", dynkin),
            ("simply laced", invariants.is_simply_laced()),
            ("Satake", satake),
            ("rational Coxeter–Vinberg", hyperbolic),
        )
        return tuple(name for name, holds in classes if holds)
