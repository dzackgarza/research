r"""Contractions as first-class morphisms between labeled stable graphs."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

from .canonical import canonical_key, canonical_record
from .isomorphisms import canonicalize, remap_vertex_fibres
from .records import StableGraph, intern_graph

if TYPE_CHECKING:
    from .graph_types import StableGraphType
    from .isomorphisms import StableGraphIsomorphism


class StableGraphContraction:
    r"""A contraction morphism ``domain -> codomain`` between labeled graphs."""

    __slots__ = (
        "_domain",
        "_codomain",
        "_target_type",
        "_contracted_flags",
        "_vertex_fibres",
        "_domain_flag_of_codomain_flag",
    )

    def __init__(
        self,
        domain: StableGraph,
        codomain: StableGraph,
        target_type: StableGraphType,
        contracted_flags: frozenset[int],
        vertex_fibres: tuple[frozenset[int], ...],
        domain_flag_of_codomain_flag: tuple[tuple[int, int], ...],
    ) -> None:
        self._domain = domain
        self._codomain = codomain
        self._target_type = target_type
        self._contracted_flags = contracted_flags
        self._vertex_fibres = vertex_fibres
        self._domain_flag_of_codomain_flag = domain_flag_of_codomain_flag
        _validate_contraction(self)

    def domain(self) -> StableGraph:
        return self._domain

    def codomain(self) -> StableGraph:
        return self._codomain

    def target_type(self) -> StableGraphType:
        return self._target_type

    def domain_flag_of_codomain_flag(self) -> dict[int, int]:
        return dict(self._domain_flag_of_codomain_flag)

    def contracted_flags(self) -> frozenset[int]:
        return self._contracted_flags

    def contracted_edges(self) -> tuple[tuple[int, int], ...]:
        involution = self._domain.flag_involution
        return tuple(sorted((flag, involution[flag]) for flag in self._contracted_flags if flag < involution[flag]))

    def num_contracted_edges(self) -> int:
        return len(self._contracted_flags) // 2

    def vertex_fibres(self) -> tuple[frozenset[int], ...]:
        return self._vertex_fibres

    def is_identity(self) -> bool:
        return len(self._contracted_flags) == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StableGraphContraction):
            return NotImplemented
        return (
            self._domain == other._domain
            and self._codomain == other._codomain
            and self._target_type == other._target_type
            and self._contracted_flags == other._contracted_flags
            and self._vertex_fibres == other._vertex_fibres
            and self._domain_flag_of_codomain_flag == other._domain_flag_of_codomain_flag
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._domain,
                self._codomain,
                self._target_type,
                self._contracted_flags,
                self._vertex_fibres,
                self._domain_flag_of_codomain_flag,
            )
        )

    def with_endpoints(
        self,
        domain: StableGraph,
        codomain: StableGraph,
        *,
        alpha: StableGraphIsomorphism | None = None,
        beta: StableGraphIsomorphism | None = None,
    ) -> StableGraphContraction:
        r"""Deprecated: pass explicit isomorphisms or use :func:`transport_contraction`."""
        warnings.warn(
            "StableGraphContraction.with_endpoints is deprecated; "
            "use transport_contraction(q, alpha, beta) or "
            "transport_contraction_via_canonical_relabeling(q, domain=..., codomain=...)",
            DeprecationWarning,
            stacklevel=2,
        )
        from .isomorphisms import identity_isomorphism, transport_contraction, transport_contraction_via_canonical_relabeling

        if alpha is not None and beta is not None:
            return transport_contraction(self, alpha, beta)
        if domain is self._domain and codomain is self._codomain:
            return self
        if domain is self._domain:
            beta_iso = beta if beta is not None else identity_isomorphism(codomain)
            assert beta_iso.source == self._codomain
            alpha_iso = identity_isomorphism(domain)
            return transport_contraction(self, alpha_iso, beta_iso)
        if codomain is self._codomain:
            alpha_iso = alpha if alpha is not None else identity_isomorphism(domain)
            assert alpha_iso.source == self._domain
            beta_iso = identity_isomorphism(codomain)
            return transport_contraction(self, alpha_iso, beta_iso)
        return transport_contraction_via_canonical_relabeling(self, domain=domain, codomain=codomain)

    def compose(self, other: StableGraphContraction) -> StableGraphContraction:
        assert self._codomain == other._domain, (
            "composition requires the codomain graph of the first contraction to be the same labeled representative as the domain graph of the second"
        )
        pullback = dict(self._domain_flag_of_codomain_flag)
        pulled_back = {pullback[flag] for flag in other._contracted_flags}
        total_flags = self._contracted_flags | frozenset(pulled_back)
        return _contract_flag_set(self._domain, total_flags)

    def __repr__(self) -> str:
        return f"Contraction of {self.num_contracted_edges()} edge(s): {self._domain!r} -> {self._codomain!r}"


def _validate_contraction(contraction: StableGraphContraction) -> None:
    domain = contraction._domain
    codomain = contraction._codomain
    target_type = contraction._target_type
    contracted_flags = contraction._contracted_flags
    vertex_fibres = contraction._vertex_fibres
    domain_flag_of_codomain_flag = contraction._domain_flag_of_codomain_flag

    involution = domain.flag_involution
    for flag in contracted_flags:
        assert involution[flag] != flag, f"cannot contract a leg (flag {flag})"
        assert involution[flag] in contracted_flags, f"contracted flags must form whole edges; partner of {flag} missing"

    surviving = [flag for flag in range(domain.num_flags()) if flag not in contracted_flags]
    assert len(domain_flag_of_codomain_flag) == len(surviving), "domain_flag_of_codomain_flag must biject surviving flags"
    codomain_flags = {codomain_flag for codomain_flag, _domain_flag in domain_flag_of_codomain_flag}
    domain_flags = {domain_flag for _codomain_flag, domain_flag in domain_flag_of_codomain_flag}
    assert codomain_flags == set(range(codomain.num_flags())), "codomain flags must be fully covered"
    assert domain_flags == set(surviving), "surviving domain flags must be fully covered"

    assert len(vertex_fibres) == codomain.num_vertices(), f"|fibres|={len(vertex_fibres)} != |V(codomain)|={codomain.num_vertices()}"
    covered_vertices: set[int] = set()
    for fibre in vertex_fibres:
        for vertex in fibre:
            assert 0 <= vertex < domain.num_vertices(), f"vertex {vertex} out of range in fibre"
            assert vertex not in covered_vertices, f"vertex {vertex} appears in multiple fibres"
            covered_vertices.add(vertex)
    assert covered_vertices == set(range(domain.num_vertices())), "vertex fibres must partition domain vertices"

    for component, fibre in enumerate(vertex_fibres):
        genus_sum = sum(domain.vertex_genera[v] for v in fibre)
        contracted_in_component = sum(1 for flag in contracted_flags if flag < involution[flag] and domain.flag_vertex[flag] in fibre)
        b1 = contracted_in_component - (len(fibre) - 1)
        expected_genus = genus_sum + b1
        assert codomain.vertex_genera[component] == expected_genus, (
            f"genus formula failed at codomain vertex {component}: expected {expected_genus}, got {codomain.vertex_genera[component]}"
        )

    from .canonical import canonical_key

    assert canonical_key(codomain) == target_type.canonical_key(), "target_type must match codomain type"
    assert target_type.parent().genus() == domain.genus()
    assert target_type.parent().number_of_markings() == domain.num_markings()


def _union_find_parent(size: int) -> list[int]:
    return list(range(size))


def _find(parent: list[int], node: int) -> int:
    root = node
    while parent[root] != root:
        root = parent[root]
    while parent[node] != root:
        parent[node], node = root, parent[node]
    return root


def _markings_at_vertex(record: StableGraph, vertex: int) -> tuple[int, ...]:
    return tuple(sorted(record.markings_at(vertex)))


def _side_signature(record: StableGraph, vertex: int) -> tuple[int, tuple[int, ...]]:
    return (record.vertex_genera[vertex], _markings_at_vertex(record, vertex))


def _edge_signature(record: StableGraph, edge: tuple[int, int]) -> tuple[object, ...]:
    u = record.flag_vertex[edge[0]]
    v = record.flag_vertex[edge[1]]
    su = _side_signature(record, u)
    sv = _side_signature(record, v)
    if u == v:
        return ("loop", su)
    return ("edge", tuple(sorted((su, sv))))


def flag_map(source: StableGraph, target: StableGraph) -> dict[int, int]:
    r"""Deprecated heuristic flag alignment; use :func:`~dm_moduli_spike.objects.isomorphisms.isomorphism_between`."""
    assert canonical_key(source) == canonical_key(target)
    mapping: dict[int, int] = {}
    for marking in range(1, source.num_markings() + 1):
        mapping[source.marking_to_flag[marking - 1]] = target.marking_to_flag[marking - 1]
    used_target_edges: set[tuple[int, int]] = set()
    for source_edge in source.internal_edges():
        signature = _edge_signature(source, source_edge)
        match: tuple[int, int] | None = None
        for target_edge in target.internal_edges():
            if target_edge in used_target_edges:
                continue
            if _edge_signature(target, target_edge) == signature:
                match = target_edge
                break
        assert match is not None, f"could not align internal edge {source_edge} between graphs"
        used_target_edges.add(match)
        mapping[source_edge[0]] = match[0]
        mapping[source_edge[1]] = match[1]
    return mapping


def _contract_flag_set(domain: StableGraph, contracted_flags: frozenset[int]) -> StableGraphContraction:
    from .graph_types import StableGraphTypes

    record = domain
    involution = record.flag_involution
    flag_vertex = record.flag_vertex

    for flag in contracted_flags:
        assert involution[flag] != flag, f"cannot contract a leg (flag {flag} is a marking, not an edge)"
        assert involution[flag] in contracted_flags, f"contracted flags must form whole edges; flag {flag}'s partner {involution[flag]} is missing"

    num_vertices = record.num_vertices()
    parent = _union_find_parent(num_vertices)
    contracted_edges: list[tuple[int, int]] = []
    for flag in contracted_flags:
        partner = involution[flag]
        if flag < partner:
            contracted_edges.append((flag, partner))
            u, v = flag_vertex[flag], flag_vertex[partner]
            if u != v:
                root_u, root_v = _find(parent, u), _find(parent, v)
                if root_u != root_v:
                    parent[root_u] = root_v

    component_of_root: dict[int, int] = {}
    for vertex in range(num_vertices):
        root = _find(parent, vertex)
        if root not in component_of_root:
            component_of_root[root] = len(component_of_root)
    new_vertex_of_old = tuple(component_of_root[_find(parent, vertex)] for vertex in range(num_vertices))
    num_new_vertices = len(component_of_root)

    fibre_sets: list[set[int]] = [set() for _ in range(num_new_vertices)]
    for vertex in range(num_vertices):
        fibre_sets[new_vertex_of_old[vertex]].add(vertex)

    contracted_edges_in_component = [0] * num_new_vertices
    for flag, partner in contracted_edges:
        contracted_edges_in_component[new_vertex_of_old[flag_vertex[flag]]] += 1
    new_genera = []
    for component in range(num_new_vertices):
        vertices = fibre_sets[component]
        genus_sum = sum(record.vertex_genera[v] for v in vertices)
        b1 = contracted_edges_in_component[component] - (len(vertices) - 1)
        new_genera.append(genus_sum + b1)

    surviving = [flag for flag in range(record.num_flags()) if flag not in contracted_flags]
    new_flag_of_old = {old: new for new, old in enumerate(surviving)}
    new_flag_vertex = tuple(new_vertex_of_old[flag_vertex[old]] for old in surviving)
    new_flag_involution = tuple(new_flag_of_old[involution[old]] for old in surviving)
    new_marking_to_flag = tuple(new_flag_of_old[flag] for flag in record.marking_to_flag)

    image = StableGraph(
        vertex_genera=tuple(new_genera),
        flag_vertex=new_flag_vertex,
        flag_involution=new_flag_involution,
        marking_to_flag=new_marking_to_flag,
    )
    codomain = intern_graph(canonical_record(image))
    cert = canonicalize(image)
    raw_to_canonical = {flag: cert.flag_map[flag] for flag in range(image.num_flags())}

    parent_types = StableGraphTypes(record.genus(), record.num_markings())
    target_type = parent_types(codomain)
    domain_flag_of_codomain_flag = tuple(sorted((raw_to_canonical[new_flag], old_flag) for old_flag, new_flag in new_flag_of_old.items()))
    raw_vertex_fibres = tuple(frozenset(fibre_sets[component]) for component in range(num_new_vertices))
    identity_domain = tuple(range(record.num_vertices()))
    vertex_fibres = remap_vertex_fibres(raw_vertex_fibres, cert.vertex_map, identity_domain)
    return StableGraphContraction(
        domain=domain,
        codomain=codomain,
        target_type=target_type,
        contracted_flags=contracted_flags,
        vertex_fibres=vertex_fibres,
        domain_flag_of_codomain_flag=domain_flag_of_codomain_flag,
    )


def contract_edge(graph: StableGraph, edge: tuple[int, int]) -> tuple[StableGraphType, StableGraphContraction]:
    flag, partner = edge
    involution = graph.flag_involution
    assert involution[flag] == partner and involution[partner] == flag, f"{edge} is not an internal edge of {graph!r}"
    contraction = _contract_flag_set(graph, frozenset({flag, partner}))
    return contraction.target_type(), contraction


def contract_edges(graph: StableGraph, edges: tuple[tuple[int, int], ...]) -> tuple[StableGraphType, StableGraphContraction]:
    flags: set[int] = set()
    involution = graph.flag_involution
    for flag, partner in edges:
        assert involution[flag] == partner, f"{(flag, partner)} is not an internal edge of {graph!r}"
        flags.add(flag)
        flags.add(partner)
    contraction = _contract_flag_set(graph, frozenset(flags))
    return contraction.target_type(), contraction
