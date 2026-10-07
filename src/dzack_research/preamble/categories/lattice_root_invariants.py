"""Reflective-root and root-system computations owned by framed lattices.

This module owns the algorithms formerly implemented in
``lattice-database/src/latticedb/roots.py`` and ``root_systems.py``.  The public
surface is exposed on lattice objects by ``categories.lattices``; database code
only serializes the returned values.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ

def _fraction(value) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, Fraction):
        return value
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


def norm_two_root_types(lattice) -> tuple[str, ...]:
    """Return the ADE type of the square-2 roots (square -2 when negative definite)."""
    labels = tuple(lattice.module_generating_set())
    positive: list[tuple[int, ...]] = []
    for root in lattice.reflective_roots():
        square = _fraction(root.q())
        if abs(square) != 2:
            continue
        coordinates = root.to_vector()
        vector = tuple(int(coordinates(label)) for label in labels)
        if next(coefficient for coefficient in vector if coefficient) > 0:
            positive.append(vector)
    types = []
    for component in _components(lattice, positive):
        if component.type[0] not in "ADE" or abs(component.scale) != 1:
            raise RuntimeError(
                f"the square-two roots of {lattice} produced {component.type} at scale {component.scale}"
            )
        types.append(component.type)
    return tuple(types)


def small_coordinate_roots(lattice, max_support: int = 3) -> tuple[tuple[int, ...], ...]:
    """Return roots with coordinates in ``{-1,0,1}`` and bounded support."""
    rank = int(lattice.module_rank())
    roots = []
    for size in range(1, min(rank, max_support) + 1):
        for support in combinations(range(rank), size):
            for signs in product((1, -1), repeat=size - 1):
                coefficients = dict(zip(support, (1, *signs), strict=True))
                vector = tuple(coefficients.get(index, 0) for index in range(rank))
                if lattice(vector).is_root():
                    roots.append(vector)
    return tuple(roots)


def generating_root_subset(lattice, roots) -> tuple[tuple[int, ...], ...]:
    """Choose a basis of roots when possible, otherwise a generating sublist."""
    roots = tuple(tuple(int(entry) for entry in root) for root in roots)
    rank = int(lattice.module_rank())
    ambient = lattice.base_ring().free_module(rank)
    basis: list[tuple[int, ...]] = []
    for root in roots:
        candidate = ambient.subobject_on(tuple(ambient(vector) for vector in (*basis, root)))
        if int(candidate.module_rank()) == len(basis) + 1 and candidate.is_primitive():
            basis.append(root)
    if len(basis) == rank:
        return tuple(basis)
    taken: list[tuple[int, ...]] = []
    for root in roots:
        span = ambient.subobject_on(tuple(ambient(vector) for vector in taken))
        if ambient(root) not in span:
            taken.append(root)
    return tuple(taken)


def small_root_span(lattice, max_support: int = 3) -> tuple[tuple[int, ...], ...] | None:
    """Return a generating root subset when the bounded coordinate search spans the lattice."""
    roots = small_coordinate_roots(lattice, max_support=max_support)
    rank = int(lattice.module_rank())
    ambient = lattice.base_ring().free_module(rank)
    span = ambient.subobject_on(tuple(ambient(root) for root in roots))
    if any(
        ambient.module_generator(label) not in span
        for label in ambient.module_generating_set()
    ):
        return None
    return generating_root_subset(lattice, roots)


def integral_reflection_model(formed):
    """Return an integral lattice with the same reflective vectors and its positive scale multiplier.

    ``formed`` is a finite free integral module with a rational-valued bilinear
    form. Multiplying the form by the denominator of its scale ideal makes it
    integral without changing which primitive vectors define integral reflections.
    """
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.rings import session_ring_objects

    integers = session_ring_objects()["ZZ"]
    scale_generator = formed.scale_submodule().principal_generator()
    multiplier = integers(int(scale_generator.denominator()))
    gram = formed.twist(multiplier).gram_tensor().change_ring(integers)
    return Lattices(integers)(gram), int(multiplier)


def standard_theta_series_prefix(lattice, minimum=None, existing_length: int = 0) -> tuple[int, ...]:
    """Return the historical bounded theta-series prefix used by the lattice catalogue.

    The default bound is 12 in rank at most 4, 8 in rank at most 8, 6 in
    rank at most 12, and 4 thereafter, never below the minimum.  An existing
    stored prefix can request a longer bound through ``existing_length``.
    """
    rank = int(lattice.module_rank())
    if minimum is None:
        minimum = abs(lattice.minimum())
    minimum_int = int(minimum)
    match rank:
        case _ if rank <= 4:
            default = 12
        case _ if rank <= 8:
            default = 8
        case _ if rank <= 12:
            default = 6
        case _:
            default = 4
    bound = max(minimum_int, default, max(0, existing_length - 1))
    series = lattice.theta_series(precision=bound + 1)
    return tuple(int(series[index]) for index in range(bound + 1))


def root_sublattice_data(lattice, roots_with_norms) -> tuple[tuple[int, ...], tuple[Fraction, ...] | None]:
    """Return invariant factors and, for a root lattice, generating root norms."""
    items = tuple((tuple(int(entry) for entry in root), _fraction(norm)) for root, norm in roots_with_norms)
    rank = int(lattice.module_rank())
    rows = [root for root, _norm in items]
    factors = (
        tuple(
            abs(int(factor))
            for factor in matrix(SageZZ, rows).elementary_divisors()
            if factor != 0
        )
        if rows
        else ()
    )
    if factors != (1,) * rank:
        return factors, None
    norms = sorted({norm for _root, norm in items}, key=lambda norm: (abs(norm), norm))
    ambient = lattice.base_ring().free_module(rank)
    selected = next(
        subset
        for size in range(1, len(norms) + 1)
        for subset in combinations(norms, size)
        if all(
            ambient.module_generator(label)
            in ambient.subobject_on(
                tuple(ambient(root) for root, norm in items if norm in subset)
            )
            for label in ambient.module_generating_set()
        )
    )
    return factors, tuple(selected)
