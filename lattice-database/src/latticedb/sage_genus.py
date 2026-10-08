"""Thin Sage-process adapter for lattice invariants owned by the research preamble.

This module contains no lattice mathematics. It reads JSON requests from
``latticedb certify``, constructs the corresponding preamble lattice, invokes
preamble-owned operations, serializes their returned values, and writes each completed value as one
JSON line.
"""

import json
import sys
from typing import TypedDict

from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
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
    group = lattice.orthogonal_group().select_group_resolution()
    generators = [_matrix_rows(generator) for generator in group.group_generators()]
    return int(group.cardinality()), generators


def _reflective(lattice) -> bool | None:
    """Serialize the preamble's answer to whether ``W(L)`` has finite index in ``O(L)``.

    ``is_reflective`` answers ``True`` when Vinberg's algorithm completes and
    otherwise returns the undecided proposition, which certifies nothing.
    """
    match HyperbolicLattices(OWNED_ZZ)(lattice).is_reflective():
        case True:
            return True
        case _:
            return None


def _irregular(answer) -> bool | None:
    """Serialize a regularity semi-decision, whose only definite answer is ``False``."""
    match answer:
        case False:
            return False
        case _:
            return None


def _modular_scale(lattice) -> int | bool:
    """Serialize the preamble's \\(k\\) with \\(L\\cong L^*(k)\\), or ``False`` when there is none."""
    scale = lattice.modular_scale()
    return False if scale is None else int(scale)


GROUP_FIELDS = {"automorphism_group_order", "automorphism_group_generator_morphisms"}


VALUES = {
    "genus_symbol": lambda lattice: str(lattice.conway_sloane_genus_symbol()),
    "genus_class_count": lambda lattice: int(lattice.genus_class_number()),
    "overlattice_count": lambda lattice: int(
        lattice.integral_overlattice_inclusions().cardinality()
    ),
    "spinor_genus_count": lambda lattice: int(lattice.spinor_genus_count()),
    "spinor_genera": lambda lattice: [
        int(value) for value in lattice.spinor_genus_class_numbers()
    ],
    "hyperbolic_index": lambda lattice: int(lattice.integral_hyperbolic_index()),
    "discriminant_sequence": lambda lattice: lattice.discriminant_sequence_data(),
    "primitive_orbits": lambda lattice: lattice.primitive_orbit_series(),
    "discriminant_orbits": lambda lattice: lattice.discriminant_orbit_series(),
    "reflective": _reflective,
    "modular_scale": _modular_scale,
    "regular": lambda lattice: _irregular(lattice.is_regular()),
    "spinor_regular": lambda lattice: _irregular(lattice.is_spinor_regular()),
}


def _start(tag: str, fields: list[str]) -> None:
    """Announce the computation of `fields`, so a run that ends during it can log it."""
    print(json.dumps({"tag": tag, "started": fields}), flush=True)


def _emit(tag: str, values: dict[str, JsonValue]) -> None:
    """Write one completed computation, so a run that ends early keeps every finished value."""
    print(json.dumps({"tag": tag, "by": "research preamble", **values}), flush=True)


def main() -> None:
    task = json.load(sys.stdin)
    lattices: list[Request] = task["lattices"]
    for request in lattices:
        ring = OWNED_ZZ if request["integral"] else OWNED_QQ
        lattice = Lattices(ring)(request["gram"])
        group_fields = GROUP_FIELDS & set(request["fields"])
        if group_fields:
            _start(request["tag"], sorted(group_fields))
            order, generators = _orthogonal_group_data(lattice)
            group_data = {
                "automorphism_group_order": order,
                "automorphism_group_generator_morphisms": generators,
            }
            _emit(request["tag"], {field: group_data[field] for field in group_fields})
        for field in request["fields"]:
            if field in group_fields:
                continue
            _start(request["tag"], [field])
            _emit(request["tag"], {field: VALUES[field](lattice)})


if __name__ == "__main__":
    main()
