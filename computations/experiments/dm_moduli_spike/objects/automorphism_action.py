r"""Automorphism group actions on a stable graph's combinatorial data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .canonical import _incidence_graph
from .records import StableGraph

if TYPE_CHECKING:
    from sage.groups.perm_gps.permgroup import PermutationGroup


class AutomorphismAction:
    r"""The action of :math:`\operatorname{Aut}(\Gamma)` on vertices, flags, edges,
    and moduli-factor indices of a stable graph."""

    __slots__ = (
        "_group",
        "_vertex_perms",
        "_flag_perms",
        "_edge_perms",
        "_marking_perms",
        "_local_marking_perms",
    )

    def __init__(
        self,
        group: PermutationGroup,
        vertex_perms: tuple[tuple[int, ...], ...],
        flag_perms: tuple[tuple[int, ...], ...],
        edge_perms: tuple[tuple[int, ...], ...],
        marking_perms: tuple[tuple[int, ...], ...],
        local_marking_perms: tuple[tuple[tuple[int, ...], ...], ...],
    ) -> None:
        self._group = group
        self._vertex_perms = vertex_perms
        self._flag_perms = flag_perms
        self._edge_perms = edge_perms
        self._marking_perms = marking_perms
        self._local_marking_perms = local_marking_perms

    def group(self) -> PermutationGroup:
        return self._group

    def on_vertices(self) -> tuple[tuple[int, ...], ...]:
        r"""Generator images as permutations of ``0, ..., |V|-1``."""
        return self._vertex_perms

    def on_flags(self) -> tuple[tuple[int, ...], ...]:
        r"""Generator images as permutations of ``0, ..., |H|-1``."""
        return self._flag_perms

    def on_edges(self) -> tuple[tuple[int, ...], ...]:
        r"""Generator images as permutations of internal edge indices ``0, ..., |E|-1``."""
        return self._edge_perms

    def on_markings(self) -> tuple[tuple[int, ...], ...]:
        r"""Generator images as permutations of ``1, ..., n``."""
        return self._marking_perms

    def on_factors(self) -> tuple[tuple[int, ...], ...]:
        r"""The same vertex permutations, acting on moduli-factor indices."""
        return self._vertex_perms

    def on_local_markings(self) -> tuple[tuple[tuple[int, ...], ...], ...]:
        r"""Generator images as per-vertex permutations of local marking slots.

        For generator ``i`` and vertex ``v``, ``on_local_markings()[i][v]`` is a
        permutation of ``0, ..., n_v-1`` where ``n_v`` is the number of markings
        on ``v``.  When ``on_vertices()[i]`` fixes ``v``, this records the
        induced slot permutation; when ``v`` is moved, slots are tracked on the
        image vertex after transport.
        """
        return self._local_marking_perms

    @staticmethod
    def from_graph(graph: StableGraph) -> AutomorphismAction:
        incidence, partition, color_of = _incidence_graph(graph)
        group = incidence.automorphism_group(partition=partition)
        vertex_nodes = sorted(node for node in color_of if node[0] == "V")
        vertex_index = {node: index for index, node in enumerate(vertex_nodes)}
        edge_nodes = sorted(node for node in color_of if node[0] == "E")
        edge_index = {node: index for index, node in enumerate(edge_nodes)}
        flag_nodes = sorted(
            (node for node in color_of if node[0] in ("M", "F")),
            key=lambda node: (node[0], node[1]),
        )
        flag_index = {node: index for index, node in enumerate(flag_nodes)}
        marking_domain = list(range(1, graph.num_markings() + 1))

        vertex_perms: list[tuple[int, ...]] = []
        edge_perms: list[tuple[int, ...]] = []
        flag_perms: list[tuple[int, ...]] = []
        marking_perms: list[tuple[int, ...]] = []
        local_marking_perms: list[tuple[tuple[int, ...], ...]] = []

        vertex_domain = list(range(len(vertex_nodes)))
        edge_domain = list(range(len(edge_nodes)))
        flag_domain = list(range(len(flag_nodes)))
        markings_by_vertex = tuple(graph.markings_at(vertex) for vertex in range(graph.num_vertices()))

        for generator in group.gens():
            vertex_image = list(vertex_domain)
            for node in vertex_nodes:
                image_node = generator(node)
                vertex_image[vertex_index[node]] = vertex_index[image_node]
            vertex_perms.append(tuple(vertex_image))

            edge_image = list(edge_domain)
            for node in edge_nodes:
                image_node = generator(node)
                edge_image[edge_index[node]] = edge_index[image_node]
            edge_perms.append(tuple(edge_image))

            flag_image = list(flag_domain)
            for node in flag_nodes:
                image_node = generator(node)
                flag_image[flag_index[node]] = flag_index[image_node]
            flag_perms.append(tuple(flag_image))

            marking_image = list(marking_domain)
            for label in marking_domain:
                node = ("M", label)
                image_node = generator(node)
                marking_image[label - 1] = image_node[1]
            marking_perms.append(tuple(marking_image))

            per_vertex: list[tuple[int, ...]] = []
            for vertex in range(graph.num_vertices()):
                labels = markings_by_vertex[vertex]
                image_vertex = vertex_image[vertex]
                image_labels = markings_by_vertex[image_vertex]
                slot_perm = list(range(len(labels)))
                for slot, label in enumerate(labels):
                    transported = marking_image[label - 1]
                    slot_perm[slot] = image_labels.index(transported)
                per_vertex.append(tuple(slot_perm))
            local_marking_perms.append(tuple(per_vertex))

        return AutomorphismAction(
            group,
            tuple(vertex_perms),
            tuple(flag_perms),
            tuple(edge_perms),
            tuple(marking_perms),
            tuple(local_marking_perms),
        )
