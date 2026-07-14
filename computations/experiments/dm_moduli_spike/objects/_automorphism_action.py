r"""Automorphism group actions on a stable graph's combinatorial data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .canonical import _incidence_graph, flag_to_node, node_to_flag

if TYPE_CHECKING:
    from sage.groups.perm_gps.permgroup import PermutationGroup_generic

    from .records import _GraphRecord


def _is_identity_permutation(image: tuple[int, ...]) -> bool:
    return all(image[index] == index for index in range(len(image)))


class _GraphAutomorphismData:
    r"""The action of :math:`\operatorname{Aut}(\Gamma)` on vertices, flags, edges,
    and moduli-factor indices of a stable graph."""

    __slots__ = (
        "_group",
        "_vertex_perms",
        "_flag_perms",
        "_edge_perms",
        "_marking_perms",
    )

    def __init__(
        self,
        group: PermutationGroup_generic,
        vertex_perms: tuple[tuple[int, ...], ...],
        flag_perms: tuple[tuple[int, ...], ...],
        edge_perms: tuple[tuple[int, ...], ...],
        marking_perms: tuple[tuple[int, ...], ...],
    ) -> None:
        self._group = group
        self._vertex_perms = vertex_perms
        self._flag_perms = flag_perms
        self._edge_perms = edge_perms
        self._marking_perms = marking_perms

    def group(self) -> PermutationGroup_generic:
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

    @staticmethod
    def from_graph(graph: _GraphRecord) -> _GraphAutomorphismData:
        incidence, partition, color_of = _incidence_graph(graph)
        group = incidence.automorphism_group(partition=partition)
        vertex_nodes = sorted(
            (node for node in color_of if node[0] == "V"),
            key=lambda node: node[1],
        )
        vertex_index = {node: index for index, node in enumerate(vertex_nodes)}
        edge_nodes = sorted(
            (node for node in color_of if node[0] == "E"),
            key=lambda node: node[1],
        )
        edge_index = {node: index for index, node in enumerate(edge_nodes)}
        marking_domain = list(range(1, graph.num_markings() + 1))

        vertex_perms: list[tuple[int, ...]] = []
        edge_perms: list[tuple[int, ...]] = []
        flag_perms: list[tuple[int, ...]] = []
        marking_perms: list[tuple[int, ...]] = []

        vertex_domain = list(range(len(vertex_nodes)))
        edge_domain = list(range(len(edge_nodes)))
        flag_domain = list(range(graph.num_flags()))

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
            for flag in flag_domain:
                image_node = generator(flag_to_node(graph, flag))
                flag_image[flag] = node_to_flag(graph, image_node)
            flag_perms.append(tuple(flag_image))

            marking_image = list(marking_domain)
            for label in marking_domain:
                node = ("M", label)
                image_node = generator(node)
                marking_image[label - 1] = image_node[1]
            marking_perms.append(tuple(marking_image))

        return _GraphAutomorphismData(
            group,
            tuple(vertex_perms),
            tuple(flag_perms),
            tuple(edge_perms),
            tuple(marking_perms),
        )
