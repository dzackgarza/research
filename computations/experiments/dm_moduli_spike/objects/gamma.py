r"""The finite category `\Gamma_{g,n}` of stable marked weighted graphs.

Objects are canonical skeletal stable graphs (isomorphism class representatives).
Morphisms are maps on vertices and half-edges compatible with contraction
semantics (Chan--Galatius--Payne, arXiv:1903.07187).

Every morphism factors as an edge contraction followed by an isomorphism.
"""

from __future__ import annotations

from collections.abc import Iterator
from itertools import combinations
from typing import TYPE_CHECKING

from sage.structure.unique_representation import UniqueRepresentation

from .canonical import automorphism_group
from .contractions import StableGraphContraction, contract_edges
from .graph_types import StableGraphType, StableGraphTypes
from .isomorphisms import isomorphism_between
from .records import StableGraph

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


class StableGraphMorphism:
    r"""Morphism `f : G \to H` in `\Gamma_{g,n}`.

    Stores a vertex map `V(G)\to V(H)`, a half-edge map on surviving flags
    (`H(G)\to H(H)`, value `-1` on contracted flags), and the contracted
    flag set.  Derived from contractions and isomorphisms.
    """

    __slots__ = ("_domain", "_codomain", "_vertex_map", "_half_edge_map", "_contracted_flags")

    def __init__(
        self,
        domain: StableGraph,
        codomain: StableGraph,
        vertex_map: tuple[int, ...],
        half_edge_map: tuple[int, ...],
        contracted_flags: frozenset[int],
    ) -> None:
        assert len(vertex_map) == domain.num_vertices()
        assert len(half_edge_map) == domain.num_flags()
        self._domain = domain
        self._codomain = codomain
        self._vertex_map = vertex_map
        self._half_edge_map = half_edge_map
        self._contracted_flags = frozenset(contracted_flags)

    @staticmethod
    def from_contraction(contraction: StableGraphContraction) -> StableGraphMorphism:
        domain = contraction.domain()
        codomain = contraction.codomain()
        vertex_map = [0] * domain.num_vertices()
        for codomain_vertex, fibre in enumerate(contraction.vertex_fibres()):
            for domain_vertex in fibre:
                vertex_map[domain_vertex] = codomain_vertex
        half_edge_map = [-1] * domain.num_flags()
        for codomain_flag, domain_flag in contraction.domain_flag_of_codomain_flag().items():
            half_edge_map[domain_flag] = codomain_flag
        return StableGraphMorphism(
            domain,
            codomain,
            tuple(vertex_map),
            tuple(half_edge_map),
            contraction.contracted_flags(),
        )

    @staticmethod
    def from_isomorphism(iso: object) -> StableGraphMorphism:
        return StableGraphMorphism(
            iso.source,
            iso.target,
            iso.vertex_map,
            iso.flag_map,
            frozenset(),
        )

    def domain(self) -> StableGraph:
        return self._domain

    def codomain(self) -> StableGraph:
        return self._codomain

    def vertex_map(self) -> tuple[int, ...]:
        return self._vertex_map

    def half_edge_map(self) -> tuple[int, ...]:
        r"""Domain flag → codomain flag, or `-1` if contracted."""
        return self._half_edge_map

    def contracted_flags(self) -> frozenset[int]:
        return self._contracted_flags

    def contracted_edges(self) -> tuple[tuple[int, int], ...]:
        involution = self._domain.flag_involution
        return tuple(
            sorted((flag, involution[flag]) for flag in self._contracted_flags if flag < involution[flag])
        )

    def surviving_half_edge_injection(self) -> dict[int, int]:
        r"""Contravariant injection `H(H)\hookrightarrow H(G)`."""
        return {
            codomain_flag: domain_flag
            for domain_flag, codomain_flag in enumerate(self._half_edge_map)
            if codomain_flag >= 0
        }

    def vertex_fiber(self, codomain_vertex: int) -> frozenset[int]:
        return frozenset(
            domain_vertex
            for domain_vertex, image in enumerate(self._vertex_map)
            if image == codomain_vertex
        )

    def is_isomorphism(self) -> bool:
        if self._contracted_flags:
            return False
        n_v = self._domain.num_vertices()
        n_h = self._domain.num_flags()
        if self._codomain.num_vertices() != n_v or self._codomain.num_flags() != n_h:
            return False
        return sorted(self._vertex_map) == list(range(n_v)) and sorted(self._half_edge_map) == list(range(n_h))

    def inverse(self) -> StableGraphMorphism:
        if not self.is_isomorphism():
            raise ValueError("morphism is not an isomorphism")
        inv_v = [0] * len(self._vertex_map)
        for source, target in enumerate(self._vertex_map):
            inv_v[target] = source
        inv_h = [0] * len(self._half_edge_map)
        for source, target in enumerate(self._half_edge_map):
            inv_h[target] = source
        return StableGraphMorphism(
            self._codomain,
            self._domain,
            tuple(inv_v),
            tuple(inv_h),
            frozenset(),
        )

    def compose(self, other: StableGraphMorphism) -> StableGraphMorphism:
        r"""Return ``self ∘ other`` (other first): ``other.domain → self.codomain``."""
        if other.codomain() != self._domain:
            raise ValueError("compose requires other.codomain() == self.domain()")
        vertices = tuple(self._vertex_map[other._vertex_map[v]] for v in range(other.domain().num_vertices()))
        half_edges: list[int] = []
        contracted: set[int] = set()
        for flag in range(other.domain().num_flags()):
            mid = other._half_edge_map[flag]
            if mid < 0 or flag in other._contracted_flags:
                half_edges.append(-1)
                contracted.add(flag)
                continue
            image = self._half_edge_map[mid]
            if image < 0 or mid in self._contracted_flags:
                half_edges.append(-1)
                contracted.add(flag)
            else:
                half_edges.append(image)
        return StableGraphMorphism(
            other.domain(),
            self.codomain(),
            vertices,
            tuple(half_edges),
            frozenset(contracted),
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StableGraphMorphism):
            return NotImplemented
        return (
            self._domain == other._domain
            and self._codomain == other._codomain
            and self._vertex_map == other._vertex_map
            and self._half_edge_map == other._half_edge_map
            and self._contracted_flags == other._contracted_flags
        )

    def __hash__(self) -> int:
        return hash((self._domain, self._codomain, self._vertex_map, self._half_edge_map, self._contracted_flags))

    def __repr__(self) -> str:
        return f"StableGraphMorphism({self._domain!r} -> {self._codomain!r}, |E_c|={len(self.contracted_edges())})"


class StableGraphHomset(UniqueRepresentation):
    r"""Finite hom-set `\operatorname{Hom}_{\Gamma_{g,n}}(G,H)`.

    Sage-style finite Hom container: morphisms are its elements (iterate /
    ``an_element`` / ``__contains__`` / ``cardinality``).
    """

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

    def category(self) -> StableGraphCategory:
        return self._category

    def __iter__(self) -> Iterator[StableGraphMorphism]:
        yield from self._morphisms

    def __len__(self) -> int:
        return len(self._morphisms)

    def cardinality(self) -> int:
        return len(self._morphisms)

    def __contains__(self, morph: object) -> bool:
        return isinstance(morph, StableGraphMorphism) and morph in self._morphisms

    def an_element(self) -> StableGraphMorphism:
        if not self._morphisms:
            raise ValueError("empty hom-set")
        return self._morphisms[0]

    def list(self) -> list[StableGraphMorphism]:
        return list(self._morphisms)


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

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def objects(self) -> tuple[StableGraph, ...]:
        return tuple(gamma.canonical_representative() for gamma in self._types)

    def object(self, data: StableGraph | StableGraphType) -> StableGraph:
        return self._canonical(data)

    def half_edges(self, graph: StableGraph | StableGraphType) -> tuple[int, ...]:
        graph = self._canonical(graph)
        return tuple(range(graph.num_flags()))

    def edges(self, graph: StableGraph | StableGraphType) -> tuple[tuple[int, int], ...]:
        return self._canonical(graph).internal_edges()

    def half_edge_map(self, morphism: StableGraphMorphism) -> dict[int, int]:
        r"""Contravariant map on half-edges: `H(\mathrm{cod})\hookrightarrow H(\mathrm{dom})`."""
        return morphism.surviving_half_edge_injection()

    def edge_map(self, morphism: StableGraphMorphism) -> dict[tuple[int, int], tuple[int, int]]:
        r"""Contravariant map on edges induced by the half-edge injection."""
        injection = morphism.surviving_half_edge_injection()
        codomain = morphism.codomain()
        result: dict[tuple[int, int], tuple[int, int]] = {}
        for cod_edge in codomain.internal_edges():
            a, b = cod_edge
            da, db = injection[a], injection[b]
            if da > db:
                da, db = db, da
            result[cod_edge] = (da, db)
        return result

    def hom(self, domain: StableGraph | StableGraphType, codomain: StableGraph | StableGraphType) -> StableGraphHomset:
        return StableGraphHomset(self, self._canonical(domain), self._canonical(codomain))

    def end(self, graph: StableGraph | StableGraphType) -> StableGraphHomset:
        graph = self._canonical(graph)
        return self.hom(graph, graph)

    def identity(self, graph: StableGraph | StableGraphType) -> StableGraphMorphism:
        graph = self._canonical(graph)
        n_v = graph.num_vertices()
        n_h = graph.num_flags()
        return StableGraphMorphism(graph, graph, tuple(range(n_v)), tuple(range(n_h)), frozenset())

    def contract(self, graph: StableGraph | StableGraphType, edges: tuple[tuple[int, int], ...]) -> StableGraphMorphism:
        graph = self._canonical(graph)
        _target_type, contraction = contract_edges(graph, edges)
        morph = StableGraphMorphism.from_contraction(contraction)
        # Land on skeletal object
        skeletal = self._canonical(morph.codomain())
        if morph.codomain() != skeletal:
            iso = StableGraphMorphism.from_isomorphism(isomorphism_between(morph.codomain(), skeletal))
            morph = iso.compose(morph)
        return morph

    def automorphism_group(self, graph: StableGraph | StableGraphType, on: str = "vertices") -> object:
        r"""Sage permutation group of `\operatorname{Aut}(G)` acting on the requested set."""
        from .automorphism_action import AutomorphismAction

        graph = self._canonical(graph)
        action = AutomorphismAction.from_graph(graph)
        if on == "vertices":
            return _permutation_group_from_images(action.on_vertices(), graph.num_vertices())
        if on in ("half_edges", "flags"):
            return _permutation_group_from_images(action.on_flags(), graph.num_flags())
        if on == "edges":
            return _permutation_group_from_images(action.on_edges(), graph.num_edges())
        raise ValueError(f"unknown automorphism action target {on!r}")

    def automorphism_morphisms(self, graph: StableGraph | StableGraphType) -> tuple[StableGraphMorphism, ...]:
        graph = self._canonical(graph)
        units = [m for m in self.end(graph) if m.is_isomorphism()]
        return tuple(units)

    def codimension(self, graph: StableGraph | StableGraphType) -> int:
        return self._canonical(graph).num_edges()

    def stratum_dimension(self, graph: StableGraph | StableGraphType) -> int:
        graph = self._canonical(graph)
        total = 0
        for vertex in range(graph.num_vertices()):
            valence = sum(1 for flag in range(graph.num_flags()) if graph.flag_vertex[flag] == vertex)
            total += 3 * graph.vertex_genera[vertex] - 3 + valence
        return total

    def boundary_divisors(self) -> tuple[StableGraph, ...]:
        return tuple(g for g in self.objects() if g.num_edges() == 1)

    def strata_in_boundary(self) -> tuple[StableGraph, ...]:
        return tuple(g for g in self.objects() if g.num_edges() >= 1)

    def deepest_strata(self) -> tuple[StableGraph, ...]:
        objects = self.objects()
        if not objects:
            return ()
        max_e = max(g.num_edges() for g in objects)
        return tuple(g for g in objects if g.num_edges() == max_e)

    def clutching_source(self, graph: StableGraph | StableGraphType) -> tuple[tuple[int, tuple[int, ...]], ...]:
        r"""Formal source `\prod_v \overline{\mathcal M}_{g(v),H(v)}` as `((g(v), H(v)))_v`."""
        graph = self._canonical(graph)
        factors: list[tuple[int, tuple[int, ...]]] = []
        for vertex in range(graph.num_vertices()):
            flags = tuple(flag for flag in range(graph.num_flags()) if graph.flag_vertex[flag] == vertex)
            factors.append((graph.vertex_genera[vertex], flags))
        return tuple(factors)

    def node_pairings(self, graph: StableGraph | StableGraphType) -> tuple[tuple[int, int], ...]:
        r"""Internal edges as two-element `\iota`-orbits (formal node gluings)."""
        return self._canonical(graph).internal_edges()

    def specialization_poset(self) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        objects = self.objects()
        # G <=_sp H iff Hom(H, G) nonempty (generic below special)
        relations: list[tuple[StableGraph, StableGraph]] = []
        nonempty: dict[tuple[int, int], bool] = {}
        indexed = list(objects)
        for i, source in enumerate(indexed):
            for j, target in enumerate(indexed):
                if i == j:
                    continue
                key = (j, i)  # Hom(target, source)
                if key not in nonempty:
                    nonempty[key] = len(self.hom(target, source)) > 0
                if nonempty[key]:
                    # cover if no mid
                    is_cover = True
                    for k, mid in enumerate(indexed):
                        if k in (i, j):
                            continue
                        key_ms = (k, i)
                        key_tm = (j, k)
                        if key_ms not in nonempty:
                            nonempty[key_ms] = len(self.hom(mid, source)) > 0
                        if key_tm not in nonempty:
                            nonempty[key_tm] = len(self.hom(target, mid)) > 0
                        if nonempty[key_ms] and nonempty[key_tm]:
                            is_cover = False
                            break
                    if is_cover:
                        relations.append((source, target))
        return Poset((objects, relations), cover_relations=True, facade=True)

    def closure_poset(self) -> FinitePoset:
        return self.specialization_poset().dual()

    def truncate(self, max_codim: int) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        max_codim = int(max_codim)
        objects = tuple(g for g in self.objects() if g.num_edges() <= max_codim)
        full = self.specialization_poset()
        # induced subposet
        covers: list[tuple[StableGraph, StableGraph]] = []
        object_set = set(objects)
        for source in objects:
            for target in objects:
                if source is target:
                    continue
                if not full.is_less_than(source, target):
                    continue
                if any(
                    mid is not source and mid is not target and mid in object_set and full.is_less_than(source, mid) and full.is_less_than(mid, target)
                    for mid in objects
                ):
                    continue
                covers.append((source, target))
        return Poset((objects, covers), cover_relations=True, facade=True)

    def _enumerate_morphisms(self, domain: StableGraph, codomain: StableGraph) -> tuple[StableGraphMorphism, ...]:
        domain = self._canonical(domain)
        codomain = self._canonical(codomain)

        if domain == codomain:
            return self._endomorphism_units_and_id(domain)

        edge_diff = domain.num_edges() - codomain.num_edges()
        if edge_diff <= 0:
            return ()

        morphisms: list[StableGraphMorphism] = []
        edges = domain.internal_edges()
        seen: set[StableGraphMorphism] = set()

        for subset in combinations(range(len(edges)), edge_diff):
            chosen = tuple(edges[i] for i in subset)
            target_type, contraction = contract_edges(domain, chosen)
            if self._canonical(target_type) != codomain:
                continue
            base = StableGraphMorphism.from_contraction(contraction)
            if base.codomain() != codomain:
                iso = StableGraphMorphism.from_isomorphism(isomorphism_between(base.codomain(), codomain))
                base = iso.compose(base)
            # Left-compose Aut(codomain)
            for auto in self._isomorphism_endomorphisms(codomain):
                morph = auto.compose(base)
                if morph not in seen:
                    seen.add(morph)
                    morphisms.append(morph)
        return tuple(morphisms)

    def _isomorphism_endomorphisms(self, graph: StableGraph) -> tuple[StableGraphMorphism, ...]:
        from .automorphism_action import AutomorphismAction

        action = AutomorphismAction.from_graph(graph)
        morphisms = [self.identity(graph)]
        # Build group elements from generator permutations on flags/vertices via Sage group
        group = action.group()
        # Fall back: use incidence aut to produce flag perms for each group element is expensive.
        # Use generator closure via on_flags / on_vertices images of gens, expand small groups.
        flag_gens = action.on_flags()
        vertex_gens = action.on_vertices()
        n_h = graph.num_flags()
        n_v = graph.num_vertices()
        # BFS generate all products of generators as maps
        id_f = tuple(range(n_h))
        id_v = tuple(range(n_v))
        queue = [(id_v, id_f)]
        seen = {(id_v, id_f)}
        while queue:
            cur_v, cur_f = queue.pop()
            for gv, gf in zip(vertex_gens, flag_gens, strict=True):
                new_v = tuple(gv[cur_v[i]] for i in range(n_v))
                new_f = tuple(gf[cur_f[i]] for i in range(n_h))
                key = (new_v, new_f)
                if key not in seen:
                    seen.add(key)
                    queue.append(key)
        for vertex_map, flag_map in seen:
            morphisms.append(StableGraphMorphism(graph, graph, vertex_map, flag_map, frozenset()))
        # Deduplicate
        unique: dict[StableGraphMorphism, None] = {}
        for morph in morphisms:
            unique[morph] = None
        return tuple(unique)

    def _endomorphism_units_and_id(self, graph: StableGraph) -> tuple[StableGraphMorphism, ...]:
        return self._isomorphism_endomorphisms(graph)

    def _repr_(self) -> str:
        return f"StableGraphCategory(Gamma_{self._g},{self._n})"


def _permutation_group_from_images(images: tuple[tuple[int, ...], ...], degree: int) -> object:
    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    sym = SymmetricGroup(degree)
    if degree == 0:
        return sym.subgroup([])
    gens = []
    for image in images:
        # Sage SymmetricGroup acts on {1,...,n}
        cycles_perm = sym([image[i] + 1 for i in range(degree)])
        gens.append(cycles_perm)
    return sym.subgroup(gens) if gens else sym.subgroup([])


# Public alias matching mathematical notation.
Gamma_gn = StableGraphCategory

# Backward-compatible name used while demoting DMCompactificationModel.
StableGraphStratification = StableGraphCategory
