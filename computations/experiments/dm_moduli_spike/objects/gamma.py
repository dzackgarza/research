r"""The finite category `\Gamma_{g,n}` of stable marked weighted graphs.

Objects are canonical skeletal stable graphs (isomorphism class representatives).
Morphisms are maps on vertices and half-edges compatible with contraction
semantics (Chan--Galatius--Payne, arXiv:1903.07187).

Every morphism factors as an edge contraction followed by an isomorphism.
"""

from __future__ import annotations

import builtins
from collections.abc import Iterator
from itertools import combinations
from typing import TYPE_CHECKING

from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .contractions import StableGraphContraction, contract_edges
from .isomorphisms import StableGraphIsomorphism, isomorphism_between
from .records import _GraphRecord
from .stable_graphs import StableGraph, StableGraphs

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset
    from sage.topology.simplicial_complex import SimplicialComplex

    from .delta_complex import SymmetricDeltaComplex

# Builtin ``object`` shadowed by :meth:`StableGraphCategory.object` inside the class body.
_Object = builtins.object


class StableGraphMorphism:
    r"""Morphism `f : G \to H` in `\Gamma_{g,n}`.

    Stores a vertex map `V(G)\to V(H)`, a half-edge map on surviving flags
    (`H(G)\to H(H)`, value `-1` on contracted flags), and the contracted
    flag set.  Derived from contractions and isomorphisms.
    """

    __slots__ = ("_domain", "_codomain", "_vertex_map", "_half_edge_map", "_contracted_flags")

    def __init__(
        self,
        domain: _GraphRecord,
        codomain: _GraphRecord,
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
    def from_isomorphism(iso: StableGraphIsomorphism) -> StableGraphMorphism:
        return StableGraphMorphism(
            iso.source,
            iso.target,
            iso.vertex_map,
            iso.flag_map,
            frozenset(),
        )

    def domain(self) -> _GraphRecord:
        return self._domain

    def codomain(self) -> _GraphRecord:
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
        return tuple(sorted((flag, involution[flag]) for flag in self._contracted_flags if flag < involution[flag]))

    def surviving_half_edge_injection(self) -> dict[int, int]:
        r"""Contravariant injection `H(H)\hookrightarrow H(G)`."""
        return {codomain_flag: domain_flag for domain_flag, codomain_flag in enumerate(self._half_edge_map) if codomain_flag >= 0}

    def vertex_fiber(self, codomain_vertex: int) -> frozenset[int]:
        return frozenset(domain_vertex for domain_vertex, image in enumerate(self._vertex_map) if image == codomain_vertex)

    def is_isomorphism(self) -> bool:
        if self._contracted_flags:
            return False
        n_v = self._domain.num_vertices()
        n_h = self._domain.num_flags()
        if self._codomain.num_vertices() != n_v or self._codomain.num_flags() != n_h:
            return False
        return sorted(self._vertex_map) == list(range(n_v)) and sorted(self._half_edge_map) == list(range(n_h))

    def is_contraction(self) -> bool:
        r"""True when this morphism contracts a (possibly empty) edge set onto its codomain."""
        if self.is_isomorphism():
            return True
        return bool(self._contracted_flags) and self._codomain.num_edges() == self._domain.num_edges() - len(self.contracted_edges())

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


class StableGraphHomset(UniqueRepresentation, Parent):
    r"""Finite hom-set `\operatorname{Hom}_{\Gamma_{g,n}}(G,H)`.

    Sage :class:`~sage.structure.parent.Parent` in :class:`~sage.categories.homsets.Homsets`
    (same pattern as :class:`~dm_moduli_spike.geometry.stacks.StackHomset`).
    Morphisms are plain combinatorial objects enumerated by this parent; they are
    not yet Sage ``Element`` instances.

    Do not name a method ``category`` here — that would shadow
    :meth:`Parent.category`.
    """

    def __init__(self, gamma: StableGraphCategory, domain: _GraphRecord, codomain: _GraphRecord) -> None:
        from sage.categories.homsets import Homsets

        self._gamma = gamma
        self._domain = domain
        self._codomain = codomain
        self._morphisms = tuple(gamma._enumerate_morphisms(domain, codomain))
        Parent.__init__(self, category=Homsets())

    def domain(self) -> _GraphRecord:
        return self._domain

    def codomain(self) -> _GraphRecord:
        return self._codomain

    def gamma(self) -> StableGraphCategory:
        r"""The combinatorial category `\Gamma_{g,n}` that owns this Hom-set."""
        return self._gamma

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
        self._graphs = StableGraphs(g, n)

    def _as_record(self, graph: object) -> _GraphRecord:
        if isinstance(graph, StableGraph):
            return graph.canonical_representative()
        if isinstance(graph, _GraphRecord):
            typed = self._graphs(graph)
            assert isinstance(typed, StableGraph), f"StableGraphs() must return StableGraph; found {type(typed)!r}"
            return typed.canonical_representative()
        raise TypeError(f"expected StableGraph or _GraphRecord; found {type(graph)}")

    def _canonical(self, graph: object) -> _GraphRecord:
        return self._as_record(graph)

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def objects(self) -> tuple[_GraphRecord, ...]:
        return tuple(gamma.canonical_representative() for gamma in self._graphs)

    def object(self, data: _GraphRecord | StableGraph) -> _GraphRecord:
        return self._canonical(data)

    def half_edges(self, graph: _GraphRecord | StableGraph) -> tuple[int, ...]:
        graph = self._canonical(graph)
        return tuple(range(graph.num_flags()))

    def edges(self, graph: _GraphRecord | StableGraph) -> tuple[tuple[int, int], ...]:
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

    def hom(self, domain: _GraphRecord | StableGraph, codomain: _GraphRecord | StableGraph) -> StableGraphHomset:
        return StableGraphHomset(self, self._canonical(domain), self._canonical(codomain))

    def end(self, graph: _GraphRecord | StableGraph) -> StableGraphHomset:
        graph = self._canonical(graph)
        return self.hom(graph, graph)

    def identity(self, graph: _GraphRecord | StableGraph) -> StableGraphMorphism:
        graph = self._canonical(graph)
        n_v = graph.num_vertices()
        n_h = graph.num_flags()
        return StableGraphMorphism(graph, graph, tuple(range(n_v)), tuple(range(n_h)), frozenset())

    def contract(self, graph: _GraphRecord | StableGraph, edges: tuple[tuple[int, int], ...]) -> StableGraphMorphism:
        graph = self._canonical(graph)
        _target_type, contraction = contract_edges(graph, edges)
        morph = StableGraphMorphism.from_contraction(contraction)
        # Land on skeletal object
        skeletal = self._canonical(morph.codomain())
        if morph.codomain() != skeletal:
            iso = StableGraphMorphism.from_isomorphism(isomorphism_between(morph.codomain(), skeletal))
            morph = iso.compose(morph)
        return morph

    def automorphism_group(self, graph: _GraphRecord | StableGraph, on: str = "vertices") -> _Object:
        r"""Sage permutation group of `\operatorname{Aut}(G)` acting on the requested set."""
        from ._automorphism_action import _GraphAutomorphismData

        graph = self._canonical(graph)
        action = _GraphAutomorphismData.from_graph(graph)
        if on == "vertices":
            return _permutation_group_from_images(action.on_vertices(), graph.num_vertices())
        if on in ("half_edges", "flags"):
            return _permutation_group_from_images(action.on_flags(), graph.num_flags())
        if on == "edges":
            return _permutation_group_from_images(action.on_edges(), graph.num_edges())
        raise ValueError(f"unknown automorphism action target {on!r}")

    def automorphism_morphisms(self, graph: _GraphRecord | StableGraph) -> tuple[StableGraphMorphism, ...]:
        graph = self._canonical(graph)
        units = [m for m in self.end(graph) if m.is_isomorphism()]
        return tuple(units)

    def codimension(self, graph: _GraphRecord | StableGraph) -> int:
        return self._canonical(graph).num_edges()

    def stratum_dimension(self, graph: _GraphRecord | StableGraph) -> int:
        graph = self._canonical(graph)
        total = 0
        for vertex in range(graph.num_vertices()):
            total += 3 * graph.vertex_genus(vertex) - 3 + graph.valence(vertex)
        return total

    def boundary_divisors(self) -> tuple[_GraphRecord, ...]:
        return tuple(g for g in self.objects() if g.num_edges() == 1)

    def strata_in_boundary(self) -> tuple[_GraphRecord, ...]:
        return tuple(g for g in self.objects() if g.num_edges() >= 1)

    def deepest_strata(self) -> tuple[_GraphRecord, ...]:
        objects = self.objects()
        if not objects:
            return ()
        max_e = max(g.num_edges() for g in objects)
        return tuple(g for g in objects if g.num_edges() == max_e)

    def clutching_source(self, graph: _GraphRecord | StableGraph) -> tuple[tuple[int, tuple[int, ...]], ...]:
        r"""Formal source `\prod_v \overline{\mathcal M}_{g(v),H(v)}` as `((g(v), H(v)))_v`."""
        graph = self._canonical(graph)
        factors: list[tuple[int, tuple[int, ...]]] = []
        for vertex in range(graph.num_vertices()):
            factors.append((graph.vertex_genus(vertex), graph.flags_at(vertex)))
        return tuple(factors)

    def node_pairings(self, graph: _GraphRecord | StableGraph) -> tuple[tuple[int, int], ...]:
        r"""Internal edges as two-element `\iota`-orbits (formal node gluings)."""
        return self._canonical(graph).internal_edges()

    def specialization_poset(self) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        objects = self.objects()
        # G <=_sp H iff Hom(H, G) nonempty (generic below special)
        relations: list[tuple[_GraphRecord, _GraphRecord]] = []
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

    def symmetric_delta_complex(self) -> SymmetricDeltaComplex:
        r"""Symmetric Δ-complex / cone complex attached to this `\Gamma_{g,n}`."""
        from .delta_complex import SymmetricDeltaComplex

        return SymmetricDeltaComplex(self)

    def order_complex(self) -> SimplicialComplex:
        r"""Thin boundary order complex (see :meth:`SymmetricDeltaComplex.order_complex`)."""
        return self.symmetric_delta_complex().order_complex()

    def truncate(self, max_codim: int) -> FinitePoset:
        from sage.combinat.posets.posets import Poset

        max_codim = int(max_codim)
        objects = tuple(g for g in self.objects() if g.num_edges() <= max_codim)
        full = self.specialization_poset()
        # induced subposet
        covers: list[tuple[_GraphRecord, _GraphRecord]] = []
        object_set = set(objects)
        for source in objects:
            for target in objects:
                if source is target:
                    continue
                if not full.is_less_than(source, target):
                    continue
                if any(mid is not source and mid is not target and mid in object_set and full.is_less_than(source, mid) and full.is_less_than(mid, target) for mid in objects):
                    continue
                covers.append((source, target))
        return Poset((objects, covers), cover_relations=True, facade=True)

    def _enumerate_morphisms(self, domain: _GraphRecord, codomain: _GraphRecord) -> tuple[StableGraphMorphism, ...]:
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

    def _isomorphism_endomorphisms(self, graph: _GraphRecord) -> tuple[StableGraphMorphism, ...]:
        from ._automorphism_action import _GraphAutomorphismData

        action = _GraphAutomorphismData.from_graph(graph)
        morphisms = [self.identity(graph)]
        # Expand Aut(Γ) via generator closure on flag/vertex permutations.
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

    def _endomorphism_units_and_id(self, graph: _GraphRecord) -> tuple[StableGraphMorphism, ...]:
        return self._isomorphism_endomorphisms(graph)

    def _repr_(self) -> str:
        return f"StableGraphCategory(Gamma_{self._g},{self._n})"


_PERM_GROUP_FROM_IMAGES: dict[tuple[object, ...], object] = {}


def _permutation_group_from_images(images: tuple[tuple[int, ...], ...], degree: int) -> object:
    r"""Return a shared Sage subgroup for identical generator images on ``degree`` letters."""
    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    key = (int(degree), tuple(tuple(int(x) for x in image) for image in images))
    cached = _PERM_GROUP_FROM_IMAGES.get(key)
    if cached is not None:
        return cached
    sym = SymmetricGroup(degree)
    if degree == 0:
        group = sym.subgroup([])
        _PERM_GROUP_FROM_IMAGES[key] = group
        return group
    gens = []
    for image in images:
        # Sage SymmetricGroup acts on {1,...,n}
        cycles_perm = sym([image[i] + 1 for i in range(degree)])
        gens.append(cycles_perm)
    group = sym.subgroup(gens) if gens else sym.subgroup([])
    _PERM_GROUP_FROM_IMAGES[key] = group
    return group


# Public alias matching mathematical notation.
Gamma_gn = StableGraphCategory
