"""Thin Sage-process adapter for lattice invariants owned by the research preamble.

This module contains no lattice mathematics. It reads JSON requests from
``latticedb certify``, constructs the corresponding preamble lattice, invokes
preamble-owned operations, serializes their returned values, and writes each completed value as one
JSON line.
"""

import json
import sys
from fractions import Fraction
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
    series_bound: int


JsonValue = object


def _matrix_rows(morphism) -> list[list[int]]:
    """Serialize a preamble morphism in the selected domain/codomain framings."""
    domain = morphism.domain()
    codomain = morphism.codomain()
    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    return [
        [int(codomain.framing_morphism().lift(morphism(domain.module_generator(source_label)))(target_label)) for source_label in source_labels]
        for target_label in target_labels
    ]


def _orthogonal_group_data(lattice) -> dict[str, JsonValue]:
    """Serialize the preamble-owned ``O(L)`` and its selected generators."""
    group = lattice.orthogonal_group().select_group_resolution()
    return {
        "automorphism_group_order": int(group.cardinality()),
        "automorphism_group_generator_morphisms": [_matrix_rows(generator) for generator in group.group_generators()],
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


def _decided(answer) -> bool | None:
    """Serialize a regularity answer: ``True`` or ``False`` when decided, and otherwise nothing."""
    match answer:
        case True:
            return True
        case False:
            return False
        case _:
            return None


def _modular_scale(lattice) -> int | bool:
    """Serialize the preamble's \\(k\\) with \\(L\\cong L^*(k)\\), or ``False`` when there is none."""
    scale = lattice.modular_scale()
    return False if scale is None else int(scale)


def _rational(value) -> int | str:
    """Serialize a preamble rational number as an integer or a string `p/q`."""
    number = Fraction(str(value))
    return number.numerator if number.denominator == 1 else f"{number.numerator}/{number.denominator}"


def _coefficients(series, bound: int) -> list[int | str]:
    """Serialize the coefficients of `q^0, ..., q^bound` of a preamble power series."""
    return [_rational(series[exponent]) for exponent in range(bound + 1)]


def _local_densities(lattice, bound: int) -> list[dict[str, JsonValue]]:
    """Serialize the preamble's local densities `beta_p(L, m)`, `m = 1, ..., bound`, at each prime dividing `2 det L`."""
    genus = lattice.genus()
    return [
        {"prime": int(prime), "densities": [_rational(genus.local_density(prime, value)) for value in range(1, bound + 1)]}
        for prime in lattice.bad_reduction_primes()
    ]


def _anisotropic_primes(lattice) -> list[int]:
    """Serialize the primes dividing `2 det L` at which the preamble's genus is anisotropic."""
    anisotropic = lattice.genus().anisotropic_primes()
    return [int(prime) for prime in lattice.bad_reduction_primes() if prime in anisotropic]


def _local_representations(lattice) -> list[dict[str, JsonValue]]:
    """Serialize the preamble's least represented valuation of each square class, at each prime dividing `2 det L` where it is not every class."""
    representations = lattice.genus().local_representations()
    exceptional = representations.index_set()
    return [
        {
            "prime": int(prime),
            "classes": [
                {"representative": int(representative), "least_valuation": int(valuation)}
                for representative, valuation in representations.value(prime).items()
            ],
        }
        for prime in lattice.bad_reduction_primes()
        if prime in exceptional
    ]


SERIES = {
    "genus_theta_series": lambda lattice, bound: _coefficients(lattice.genus().theta_series(precision=bound + 1), bound),
    "theta_series_cuspidal_component": lambda lattice, bound: _coefficients(lattice.theta_series_cuspidal_component(precision=bound + 1), bound),
    "local_densities": _local_densities,
    "siegel_eisenstein_coefficients": lambda lattice, bound: _coefficients(lattice.genus().siegel_eisenstein_series(precision=bound + 1), bound)[1:],
}
"""Fields whose value is a prefix of a series, computed through the request's `series_bound`."""


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
    "overlattice_count": lambda lattice: int(lattice.integral_overlattice_inclusions().cardinality()),
    "spinor_genus_count": lambda lattice: int(lattice.spinor_genus_count()),
    "spinor_genera": lambda lattice: [int(value) for value in lattice.spinor_genus_class_numbers()],
    "hyperbolic_index": lambda lattice: int(lattice.integral_hyperbolic_index()),
    "discriminant_sequence": lambda lattice: lattice.discriminant_sequence_data(),
    "primitive_orbits": lambda lattice: lattice.primitive_orbit_series(),
    "discriminant_orbits": lambda lattice: lattice.discriminant_orbit_series(),
    "reflective": _reflective,
    "modular_scale": _modular_scale,
    "regular": lambda lattice: _decided(lattice.is_regular()),
    "spinor_regular": lambda lattice: _decided(lattice.is_spinor_regular()),
    "anisotropic_primes": _anisotropic_primes,
    "local_representations": _local_representations,
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
            value = SERIES[field](lattice, request["series_bound"]) if field in SERIES else VALUES[field](lattice)
            _emit(request["tag"], {field: value})


if __name__ == "__main__":
    main()
