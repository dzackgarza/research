r"""The finite category `\Gamma_{g,n}` of stable marked weighted graphs.

Objects are canonical skeletal stable graphs (isomorphism class representatives).
Morphisms are set maps `f : X(G) \to X(H)` on vertices and half-edges, compatible
with incidence, involution, markings, and contraction semantics.

References: Chan--Galatius--Payne, arXiv:1903.07187.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

from sage.structure.unique_representation import UniqueRepresentation

from .canonical import automorphism_group
from .graph_types import StableGraphType, StableGraphTypes
from .records import StableGraph

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


class StableGraphMorphism:
    r"""Morphism in `\Gamma_{g,n}` as a map on `X(G)=V(G)\sqcup H(G)`."""

    __slots__ = ("_domain", "_codomain", "_on_vertices", "_on_half_edges", "_contracted_edges")

    def __init__(
        self,
        domain: StableGraph,
        codomain: StableGraph,
        on_vertices: tuple[int, ...],
        on_half_edges: tuple[int, ...],
        contracted_edges: frozenset[int],
    ) -> None:
        self._domain = domain
        self._codomain = codomain
        self._on_vertices = on_vertices
        self._on_half_edges = on_half_edges
        self._contracted_edges = contracted_edges

    def domain(self) -> StableGraph:
        return self._domain

    def codomain(self) -> StableGraph:
        return self._codomain

    def on_vertices(self) -> tuple[int, ...]:
        return self._on_vertices

    def on_half_edges(self) -> tuple[int, ...]:
        return self._on_half_edges

    def contracted_edges(self) -> frozenset[int]:
        return self._contracted_edges

    def is_isomorphism(self) -> bool:
        return len(self._contracted_edges) == 0 and len(set(self._on_vertices)) == len(self._on_vertices)

    def compose(self, other: StableGraphMorphism) -> StableGraphMorphism:
        if other.codomain() != self._domain:
            raise ValueError("compose requires other.codomain() == self.domain()")
        vertices = tuple(self._on_vertices[other._on_vertices[v]] for v in range(other.domain().num_vertices()))
        half_edges = tuple(self._on_half_edges[other._on_half_edges[h]] for h in range(other.domain().num_flags()))
        contracted = other._contracted_edges | frozenset(
            h for h in range(other.domain().num_flags()) if self._on_half_edges[h] != h
        )
        return StableGraphMorphism(other.domain(), self.codomain(), vertices, half_edges, contracted)


class StableGraphHomset(UniqueRepresentation):
    r"""Finite hom-set `\operatorname{Hom}_{\Gamma_{g,n}}(G,H)`."""

    __slots__ = ("_category", "_domain", "_codomain", "_morphisms")

    def __init__(self, category: StableGraphCategory, domain: StableGraph, codomain: StableGraph) -> None:
        self._category = category
        self._domain = domain
        self._codomain = codomain
        self._morphisms = tuple(category._enumerate_morphisms(domain, codomain))

    def domain(self) -> StableGraph:
        return self._domain

    def codomain(self) -> StableGraph:
        return self._codomain

    def __iter__(self) -> Iterator[StableGraphMorphism]:
        yield from self._morphisms

    def __len__(self) -> int:
        return len(self._morphisms)

    def an_element(self) -> StableGraphMorphism:
        if not self._morphisms:
            raise ValueError("empty hom-set")
        return self._morphisms[0]


class StableGraphCategory(UniqueRepresentation):
    r"""Finite skeletal category `\Gamma_{g,n}`."""

    def __init__(self, g: int, n: int) -> None:
        g = int(g)
        n = int(n)
        assert g >= 0 and n >= 0
        assert 2 * g - 2 + n > 0
        self._g = g
        self._n = n
        self._types = StableGraphTypes(g, n)

    def _canonical(self, graph: StableGraph | StableGraphType) -> StableGraph:
        if isinstance(graph, StableGraphType):
            return graph.canonical_representative()
        if isinstance(graph, StableGraph):
            return self._types(graph).canonical_representative()
        raise TypeError(f"expected StableGraph or StableGraphType; found {type(graph)}")

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def objects(self) -> tuple[StableGraph, ...]:
        return tuple(gamma.canonical_representative() for gamma in self._types)

    def object(self, data: StableGraph | StableGraphType) -> StableGraph:
        return self._canonical(data)

    def hom(self, domain: StableGraph | StableGraphType, codomain: StableGraph | StableGraphType) -> StableGraphHomset:
        domain = self._canonical(domain)
        codomain = self._canonical(codomain)
        return StableGraphHomset(self, domain, codomain)

    def identity(self, graph: StableGraph | StableGraphType) -> StableGraphMorphism:
        graph = self._canonical(graph)
        n_v = graph.num_vertices()
        n_h = graph.num_flags()
        return StableGraphMorphism(
            graph,
            graph,
            tuple(range(n_v)),
            tuple(range(n_h)),
            frozenset(),
        )

    def automorphism_group(self, graph: StableGraph | StableGraphType) -> object:
        return automorphism_group(self._canonical(graph))

    def specialization_poset(self) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        objects = self.objects()
        covers: list[tuple[StableGraph, StableGraph]] = []
        for source in objects:
            for target in objects:
                if source is target:
                    continue
                if len(self.hom(target, source)) > 0:
                    if any(
                        mid is not source
                        and mid is not target
                        and len(self.hom(mid, source)) > 0
                        and len(self.hom(target, mid)) > 0
                        for mid in objects
                    ):
                        continue
                    covers.append((source, target))
        return Poset((objects, covers), cover_relations=True)

    def _enumerate_morphisms(self, domain: StableGraph, codomain: StableGraph) -> tuple[StableGraphMorphism, ...]:
        from .contractions import contract_edges

        domain = self._canonical(domain)
        codomain = self._canonical(codomain)
        if domain == codomain:
            return (self.identity(domain),)

        morphisms: list[StableGraphMorphism] = []
        edges = domain.internal_edges()
        from itertools import combinations

        edge_diff = domain.num_edges() - codomain.num_edges()
        if edge_diff <= 0:
            return ()
        for subset in combinations(range(len(edges)), edge_diff):
            chosen = tuple(edges[i] for i in subset)
            target_type, contraction = contract_edges(domain, chosen)
            if self._canonical(target_type) != codomain:
                continue
            # Record morphism via contraction data (upgrade to full X(G)->X(H) map in stage 4)
            flags = frozenset(contraction.contracted_flags())
            morphisms.append(
                StableGraphMorphism(
                    domain,
                    codomain,
                    tuple(range(codomain.num_vertices())),
                    tuple(range(codomain.num_flags())),
                    flags,
                )
            )
        return tuple(morphisms)

    def _repr_(self) -> str:
        return f"StableGraphCategory(Gamma_{self._g},{self._n})"


# Public alias matching mathematical notation.
Gamma_gn = StableGraphCategory
