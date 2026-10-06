"""Thin Sage-process adapter for lattice invariants owned by the research preamble.

This module contains no lattice mathematics. It reads JSON requests from
``latticedb certify``, constructs the corresponding preamble lattice, invokes
preamble-owned operations, serializes their returned values, and enforces the
per-computation wall-clock alarm.
"""

import json
import sys
from collections.abc import Callable
from typing import TypedDict

from cysignals.alarm import alarm, cancel_alarm
from cysignals.signals import AlarmInterrupt

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

_RINGS = session_ring_objects()
OWNED_ZZ = _RINGS["ZZ"]
OWNED_QQ = _RINGS["QQ"]


class Request(TypedDict):
    tag: str
    gram: list[list[int | str]]
    integral: bool
    fields: list[str]


JsonValue = object


def within(seconds: int, compute: Callable[[], JsonValue]) -> JsonValue | None:
    """Return ``compute()`` or ``None`` when the process-local alarm fires."""
    alarm(seconds)
    try:
        value = compute()
    except AlarmInterrupt:
        return None
    finally:
        cancel_alarm()
    return value


def _matrix_rows(morphism) -> list[list[int]]:
    """Serialize a preamble morphism in the selected domain/codomain framings."""
    domain = morphism.domain()
    codomain = morphism.codomain()
    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    return [
        [
            int(
                codomain.framing_morphism().lift(
                    morphism(domain.module_generator(source_label))
                )(target_label)
            )
            for source_label in source_labels
        ]
        for target_label in target_labels
    ]


def _orthogonal_group_data(lattice) -> tuple[int, list[list[list[int]]]]:
    """Serialize the preamble-owned ``O(L)`` and its selected generators."""
    group = lattice.orthogonal_group().framing()
    generators = [_matrix_rows(generator) for generator in group.group_generators()]
    return int(group.cardinality()), generators


def main() -> None:
    task = json.load(sys.stdin)
    seconds: int = task["seconds"]
    lattices: list[Request] = task["lattices"]
    for request in lattices:
        ring = OWNED_ZZ if request["integral"] else OWNED_QQ
        lattice = Lattices(ring)(request["gram"])
        requested = set(request["fields"])
        line: dict[str, JsonValue | None] = {
            "tag": request["tag"],
            "by": "research preamble",
        }

        group_data = None
        if requested & {
            "automorphism_group_order",
            "automorphism_group_generator_morphisms",
        }:
            group_data = within(seconds, lambda: list(_orthogonal_group_data(lattice)))
        if "automorphism_group_order" in requested:
            line["automorphism_group_order"] = (
                int(group_data[0]) if isinstance(group_data, list) else None
            )
        if "automorphism_group_generator_morphisms" in requested:
            line["automorphism_group_generator_morphisms"] = (
                group_data[1] if isinstance(group_data, list) else None
            )

        computations: dict[str, Callable[[], JsonValue]] = {
            "genus_symbol": lambda: str(lattice.conway_sloane_genus_symbol()),
            "genus_class_count": lambda: int(lattice.genus_class_number()),
            "overlattice_count": lambda: int(
                lattice.integral_overlattice_inclusions().cardinality()
            ),
            "spinor_genus_count": lambda: int(lattice.spinor_genus_count()),
            "spinor_genera": lambda: [
                int(value) for value in lattice.spinor_genus_class_numbers()
            ],
            "hyperbolic_index": lambda: int(lattice.integral_hyperbolic_index()),
            "discriminant_sequence": lambda: lattice.discriminant_sequence_data(),
            "primitive_orbits": lambda: lattice.primitive_orbit_series(),
            "discriminant_orbits": lambda: lattice.discriminant_orbit_series(),
        }
        for field in request["fields"]:
            if field in {
                "automorphism_group_order",
                "automorphism_group_generator_morphisms",
            }:
                continue
            line[field] = within(seconds, computations[field])
        print(json.dumps(line), flush=True)


if __name__ == "__main__":
    main()
