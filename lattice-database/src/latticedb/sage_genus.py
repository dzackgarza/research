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


def _orthogonal_group_data(lattice) -> dict[str, JsonValue]:
    """Serialize the preamble-owned ``O(L)`` and its selected generators."""
    group = lattice.orthogonal_group().select_group_resolution()
    return {
        "automorphism_group_order": int(group.cardinality()),
        "automorphism_group_generator_morphisms": [
            _matrix_rows(generator) for generator in group.group_generators()
        ],
    }


def _root_span_data(lattice) -> dict[str, JsonValue]:
    """Serialize roots of ``L`` that generate ``L``, with their norms ``b(r, r)``.

    ``root_module_generating_set`` returns only when the roots generate ``L``,
    which proves ``L = ZPhi(L)``; otherwise it runs until the job ends.
    """
    labels = tuple(lattice.module_generating_set())
    framing = lattice.framing_morphism()
    roots = tuple(lattice.root_module_generating_set())
    return {
        "roots": [[int(framing.lift(root)(label)) for label in labels] for root in roots],
        "norms": [int(root.q()) for root in roots],
    }


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


JOINT = (
    (
        frozenset({"automorphism_group_order", "automorphism_group_generator_morphisms"}),
        _orthogonal_group_data,
    ),
    (frozenset({"roots", "norms"}), _root_span_data),
)
"""Fields that one preamble computation answers together, with that computation."""


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
        joint_fields: set[str] = set()
        for fields, compute in JOINT:
            chosen = fields & set(request["fields"])
            if not chosen:
                continue
            _start(request["tag"], sorted(fields))
            # The answer is one computation, so every field of it is stored together.
            _emit(request["tag"], compute(lattice))
            joint_fields |= fields
        for field in request["fields"]:
            if field in joint_fields:
                continue
            _start(request["tag"], [field])
            _emit(request["tag"], {field: VALUES[field](lattice)})


if __name__ == "__main__":
    main()
