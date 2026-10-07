"""Reflective-root and root-system computations owned by framed lattices.

This module owns the algorithms formerly implemented in
``lattice-database/src/latticedb/roots.py`` and ``root_systems.py``.  The public
surface is exposed on lattice objects by ``categories.lattices``; database code
only serializes the returned values.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


def _fraction(value) -> Fraction:
    if isinstance(value, (int, Fraction)):
        return Fraction(value)
    return Fraction(int(value.numerator()), int(value.denominator()))


@dataclass(frozen=True)
class RootSystemComponentData:
    """One irreducible reflective-root component in the selected lattice basis."""

    type: str
    scale: Fraction
    simple_roots: tuple[tuple[int, ...], ...]


def _simple_roots(positive: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    sums = {
        tuple(a + b for a, b in zip(left, right, strict=True))
        for left, right in combinations(positive, 2)
    }
    return [root for root in positive if root not in sums]


def _irreducible_components(lattice, base: list[tuple[int, ...]]) -> list[list[tuple[int, ...]]]:
    components: list[list[tuple[int, ...]]] = []
    for coordinates in base:
        root = lattice(coordinates)
        linked = [
            component
            for component in components
            if any(root.b(lattice(other)) != 0 for other in component)
        ]
        components = [component for component in components if component not in linked]
        components.append([*(other for component in linked for other in component), coordinates])
    return components


def _typed_component(lattice, base: list[tuple[int, ...]]) -> RootSystemComponentData:
    from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams
    from dzack_research.preamble.categories.lattices import Lattices

    norms = [_fraction(lattice(root).q()) for root in base]
    sign = -1 if min(norms, key=abs) < 0 else 1
    oriented = lattice if sign < 0 else lattice.twist(-1)
    diagram = CoxeterDiagrams().from_roots(tuple(oriented(root) for root in base))
    recognized = diagram.scaled_cartan_type()
    if recognized is None:
        raise RuntimeError(f"no irreducible root-system type matches the base {base}")
    cartan, positive_scale = recognized
    letter, rank = str(cartan.type()), int(cartan.rank())
    root_type = "B2" if letter == "C" and rank == 2 else f"{letter}{rank}"
    reference = Lattices.root_lattice(letter, rank).twist(positive_scale)
    reference_diagram = CoxeterDiagrams().from_roots(
        tuple(reference.module_generators())
    )
    isomorphic, certificate = diagram.root_intersection_graph().is_isomorphic(
        reference_diagram.root_intersection_graph(),
        edge_labels=True,
        certificate=True,
    )
    if not isomorphic:
        raise ArithmeticError(
            f"{diagram} was recognized as {cartan} at scale {positive_scale}, "
            "but its rooted intersection graph has no isomorphism to the canonical model"
        )
    by_reference = {
        int(reference_vertex): int(source_vertex)
        for source_vertex, reference_vertex in certificate.items()
    }
    return RootSystemComponentData(
        root_type,
        Fraction(sign) * _fraction(positive_scale),
        tuple(base[by_reference[index]] for index in range(rank)),
    )


def _components(lattice, positive: list[tuple[int, ...]]) -> tuple[RootSystemComponentData, ...]:
    base = _simple_roots(positive)
    components = [
        _typed_component(lattice, component)
        for component in _irreducible_components(lattice, base)
    ]
    return tuple(
        sorted(
            components,
            key=lambda component: (-len(component.simple_roots), component.type, component.simple_roots),
        )
    )


def reflective_root_system_components(lattice) -> tuple[RootSystemComponentData, ...]:
    """Return all reflective roots of a definite lattice as irreducible components."""
    labels = tuple(lattice.module_generating_set())
    positive = []
    for root in lattice.reflective_roots():
        coordinates = root.to_vector()
        vector = tuple(int(coordinates(label)) for label in labels)
        if next(coefficient for coefficient in vector if coefficient) > 0:
            positive.append(vector)
    return _components(lattice, positive)


