r"""Contractions as first-class morphisms of stable curve types.

Contracting a set of internal edges collapses every connected component ``C`` of
the contracted subgraph to a single vertex of weight

.. math::

    w'(C) = \sum_{v \in V(C)} w(v) + b_1(C).

For a single edge this specialises to:

* a non-loop edge joining distinct ``u, v`` merges them with
  :math:`w' = w(u) + w(v)`;
* a loop at ``v`` is removed with :math:`w'(v) = w(v) + 1`.

Total genus and stability are preserved.  A contraction is retained as a typed
morphism (domain, codomain, contracted flags, vertex fibres) rather than a bare
Boolean relation, so distinct contractions with the same endpoints remain
distinguishable.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .records import StableGraphRecord

if TYPE_CHECKING:
    from .curve_types import StableCurveType


class StableGraphContraction:
    r"""A contraction morphism ``domain -> codomain``.

    The morphism collapses ``contracted_flags`` (a set of edge-flags forming
    whole internal edges of the domain); ``vertex_fibres[j]`` is the set of
    domain vertices that map to codomain vertex ``j``.
    """

    __slots__ = (
        "_domain",
        "_codomain",
        "_contracted_flags",
        "_vertex_fibres",
        "_domain_flag_of_codomain_flag",
    )

    def __init__(
        self,
        domain: StableCurveType,
        codomain: StableCurveType,
        contracted_flags: frozenset[int],
        vertex_fibres: tuple[frozenset[int], ...],
        domain_flag_of_codomain_flag: dict[int, int],
    ) -> None:
        self._domain = domain
        self._codomain = codomain
        self._contracted_flags = contracted_flags
        self._vertex_fibres = vertex_fibres
        self._domain_flag_of_codomain_flag = domain_flag_of_codomain_flag

    def domain(self) -> StableCurveType:
        return self._domain

    def codomain(self) -> StableCurveType:
        return self._codomain

    def contracted_flags(self) -> frozenset[int]:
        return self._contracted_flags

    def contracted_edges(self) -> tuple[tuple[int, int], ...]:
        involution = self._domain.record().flag_involution
        return tuple(sorted((flag, involution[flag]) for flag in self._contracted_flags if flag < involution[flag]))

    def num_contracted_edges(self) -> int:
        return len(self._contracted_flags) // 2

    def vertex_fibres(self) -> tuple[frozenset[int], ...]:
        return self._vertex_fibres

    def is_identity(self) -> bool:
        return len(self._contracted_flags) == 0

    def compose(self, other: StableGraphContraction) -> StableGraphContraction:
        r"""The composite ``other ∘ self`` : ``self.domain() -> other.codomain()``.

        Requires ``self.codomain()`` to be ``other.domain()`` (as the same
        object obtained by chaining ``.contract()``), so that ``other``'s
        contracted flags -- which live in the shared record -- can be pulled back
        to the original domain and contracted together.
        """
        assert self._codomain is other._domain or self._codomain.record() is other._domain.record(), (
            "composition requires the codomain of the first contraction to be the domain of the second "
            "(chain them via .contract()); different isomorphic representatives are not composable in this spike"
        )
        pulled_back = {self._domain_flag_of_codomain_flag[flag] for flag in other._contracted_flags}
        total_flags = self._contracted_flags | frozenset(pulled_back)
        return _contract_flag_set(self._domain, total_flags)

    def __repr__(self) -> str:
        return f"Contraction of {self.num_contracted_edges()} edge(s): {self._domain!r} -> {self._codomain!r}"


def _union_find_parent(size: int) -> list[int]:
    return list(range(size))


def _find(parent: list[int], node: int) -> int:
    root = node
    while parent[root] != root:
        root = parent[root]
    while parent[node] != root:
        parent[node], node = root, parent[node]
    return root


def _contract_flag_set(gamma: StableCurveType, contracted_flags: frozenset[int]) -> StableGraphContraction:
    record = gamma.record()
    involution = record.flag_involution
    flag_vertex = record.flag_vertex

    # Sanity: the contracted flags come in whole internal-edge pairs.
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

    # Components of the contracted subgraph, in a stable order.
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

    # Component genus: sum of vertex genera + b_1 of the contracted subgraph
    # within the component, where b_1 = (contracted edges inside C) - (|C| - 1).
    contracted_edges_in_component = [0] * num_new_vertices
    for flag, partner in contracted_edges:
        contracted_edges_in_component[new_vertex_of_old[flag_vertex[flag]]] += 1
    new_genera = []
    for component in range(num_new_vertices):
        vertices = fibre_sets[component]
        genus_sum = sum(record.vertex_genera[v] for v in vertices)
        b1 = contracted_edges_in_component[component] - (len(vertices) - 1)
        new_genera.append(genus_sum + b1)

    # Surviving flags keep their original order; renumber to 0, 1, ....
    surviving = [flag for flag in range(record.num_flags()) if flag not in contracted_flags]
    new_flag_of_old = {old: new for new, old in enumerate(surviving)}
    new_flag_vertex = tuple(new_vertex_of_old[flag_vertex[old]] for old in surviving)
    new_flag_involution = tuple(new_flag_of_old[involution[old]] for old in surviving)
    new_marking_to_flag = tuple(new_flag_of_old[flag] for flag in record.marking_to_flag)

    image_record = StableGraphRecord(
        vertex_genera=tuple(new_genera),
        flag_vertex=new_flag_vertex,
        flag_involution=new_flag_involution,
        marking_to_flag=new_marking_to_flag,
    )
    codomain = gamma.parent().from_record(image_record)

    vertex_fibres = tuple(frozenset(fibre_sets[component]) for component in range(num_new_vertices))
    domain_flag_of_codomain_flag = {new: old for old, new in new_flag_of_old.items()}
    return StableGraphContraction(
        domain=gamma,
        codomain=codomain,
        contracted_flags=contracted_flags,
        vertex_fibres=vertex_fibres,
        domain_flag_of_codomain_flag=domain_flag_of_codomain_flag,
    )


def contract_edge(gamma: StableCurveType, edge: tuple[int, int]) -> tuple[StableCurveType, StableGraphContraction]:
    r"""Contract a single internal edge, returning ``(codomain, contraction)``."""
    flag, partner = edge
    involution = gamma.record().flag_involution
    assert involution[flag] == partner and involution[partner] == flag, f"{edge} is not an internal edge of {gamma!r}"
    contraction = _contract_flag_set(gamma, frozenset({flag, partner}))
    return contraction.codomain(), contraction


def contract_edges(gamma: StableCurveType, edges: tuple[tuple[int, int], ...]) -> tuple[StableCurveType, StableGraphContraction]:
    r"""Contract several internal edges at once."""
    flags: set[int] = set()
    involution = gamma.record().flag_involution
    for flag, partner in edges:
        assert involution[flag] == partner, f"{(flag, partner)} is not an internal edge of {gamma!r}"
        flags.add(flag)
        flags.add(partner)
    contraction = _contract_flag_set(gamma, frozenset(flags))
    return contraction.codomain(), contraction
