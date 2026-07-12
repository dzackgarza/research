r"""Factor-local special-point coordinates on stable graphs."""

from __future__ import annotations

from dataclasses import dataclass

from .records import StableGraph


@dataclass(frozen=True, slots=True)
class FactorSlot:
    r"""One local special point on a moduli factor ``\overline{\mathcal M}_{g,n_v}``."""

    vertex: int
    local_index: int
    flag: int


def _branch_sort_key(record: StableGraph, flag: int) -> tuple[int, int, int]:
    partner = record.flag_involution[flag]
    partner_vertex = record.flag_vertex[partner]
    return (partner_vertex, min(flag, partner), flag)


def factor_slots(record: StableGraph) -> tuple[tuple[FactorSlot, ...], ...]:
    r"""Ordered local slots on each vertex: external legs then node branches."""
    by_vertex: list[list[FactorSlot]] = [[] for _ in range(record.num_vertices())]
    for vertex in range(record.num_vertices()):
        leg_flags = sorted(
            (record.marking_to_flag[label - 1] for label in record.markings_at(vertex)),
            key=lambda flag: record.marking_to_flag.index(flag),
        )
        branch_flags = sorted(
            (flag for flag in record.flags_at(vertex) if record.flag_involution[flag] != flag),
            key=lambda flag: _branch_sort_key(record, flag),
        )
        ordered_flags = leg_flags + branch_flags
        assert len(ordered_flags) == record.valence(vertex), f"vertex {vertex} valence {record.valence(vertex)} != {len(ordered_flags)} incident flags"
        by_vertex[vertex] = [FactorSlot(vertex=vertex, local_index=slot, flag=flag) for slot, flag in enumerate(ordered_flags)]
    return tuple(tuple(slots) for slots in by_vertex)


def external_marking_slot_map(record: StableGraph) -> tuple[FactorSlot, ...]:
    r"""Assignment of each external label ``1, ..., n`` to a :class:`FactorSlot`."""
    slots_by_vertex = factor_slots(record)
    assignment: list[FactorSlot | None] = [None] * record.num_markings()
    for vertex_slots in slots_by_vertex:
        for slot in vertex_slots:
            if record.flag_involution[slot.flag] == slot.flag:
                label = record.marking_to_flag.index(slot.flag) + 1
                assignment[label - 1] = slot
    assert all(entry is not None for entry in assignment), "incomplete external marking slot assignment"
    return tuple(entry for entry in assignment if entry is not None)


def node_pairings(record: StableGraph) -> tuple[tuple[FactorSlot, FactorSlot], ...]:
    r"""Each internal edge as a pair of :class:`FactorSlot` branch coordinates."""
    slot_by_flag = {slot.flag: slot for vertex_slots in factor_slots(record) for slot in vertex_slots}
    pairings: list[tuple[FactorSlot, FactorSlot]] = []
    for flag, partner in record.internal_edges():
        pairings.append((slot_by_flag[flag], slot_by_flag[partner]))
    return tuple(pairings)
