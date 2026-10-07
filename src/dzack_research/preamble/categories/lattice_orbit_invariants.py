"""Primitive-vector and discriminant-action invariants of integral lattices.

This module owns the algorithms migrated from the former
``lattice-database/src/latticedb/sage_genus.py`` implementation.  The
orthogonal group itself is never recomputed here: definite orbit calculations
consume ``L.orthogonal_group().select_group_resolution().group_generators()``.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence, Sized
from functools import partial

from sage.groups.fqf_orthogonal import FqfIsometry
from sage.matrix.constructor import matrix
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.modules.torsion_quadratic_module import TorsionQuadraticModuleElement
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

ORBIT_NORM_BOUND = 4


def _gram_matrix(lattice) -> Matrix_integer_dense:
    rank = int(lattice.module_rank())
    gram = lattice.gram_tensor()
    return matrix(
        ZZ,
        [[int(gram[i, j]) for j in range(rank)] for i in range(rank)],
    )


def _element_coordinates(element) -> tuple[int, ...]:
    lattice = element.parent()
    labels = tuple(lattice.module_generating_set())
    coordinates = lattice.framing_morphism().lift(element)
    return tuple(int(coordinates(label)) for label in labels)


def _isometry_matrix(isometry) -> Matrix_integer_dense:
    domain = isometry.domain()
    codomain = isometry.codomain()
    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    rows = [
        [
            int(
                codomain.framing_morphism().lift(
                    isometry(domain.module_generator(source_label))
                )(target_label)
            )
            for source_label in source_labels
        ]
        for target_label in target_labels
    ]
    return matrix(ZZ, rows)


def _orthogonal_generator_matrices(lattice) -> list[Matrix_integer_dense]:
    return [
        _isometry_matrix(generator)
        for generator in lattice.orthogonal_group().select_group_resolution().group_generators()
    ]


def _discriminant_actions(
    gram: Matrix_integer_dense, generators: list[Matrix_integer_dense]
) -> tuple[list[int], list[Matrix_integer_dense]]:
    smith, left, _ = gram.smith_form()
    kept = [
        index
        for index in range(gram.nrows())
        if abs(smith[index, index]) > 1
    ]
    factors = [abs(int(smith[index, index])) for index in kept]
    left_inverse = left.inverse_of_unit()
    actions = []
    for generator in generators:
        action = left * generator.inverse_of_unit().transpose() * left_inverse
        actions.append(action.matrix_from_rows_and_columns(kept, kept))
    return factors, actions


def _orbit_counts(
    vectors: Matrix_integer_dense,
    generators: list[Matrix_integer_dense],
    quotient: list[list[int]],
    size: int,
) -> list[int]:
    columns = {tuple(column): index for index, column in enumerate(vectors.columns())}
    parent = list(range(len(columns) * size))

    def root(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for generator, multiply in zip(generators, quotient, strict=True):
        images = [columns[tuple(column)] for column in (generator * vectors).columns()]
        for vector_index, image in enumerate(images):
            for quotient_index in range(size):
                left = root(vector_index * size + quotient_index)
                right = root(image * size + multiply[quotient_index])
                if left != right:
                    parent[left] = right
    return [root(index * size) for index in range(len(columns))]


def _closure(
    identity: tuple[int, ...],
    generators: Sequence[Callable[[tuple[int, ...]], tuple[int, ...]]],
) -> list[tuple[int, ...]]:
    found = {identity: None}
    frontier = [identity]
    while frontier:
        element = frontier.pop()
        for generator in generators:
            image = generator(element)
            if image not in found:
                found[image] = None
                frontier.append(image)
    return list(found)


def _quotient_action(
    action: Matrix_integer_dense,
    factors: list[int],
    determinant: int,
    with_determinant: bool,
    with_discriminant: bool,
    element: tuple[int, ...],
) -> tuple[int, ...]:
    sign_part = element[0] * determinant if with_determinant else 1
    if not with_discriminant:
        return (sign_part,)
    order = len(factors)
    current = matrix(ZZ, order, order, list(element[1:])).transpose()
    product = action * current
    return (
        sign_part,
        *(
            int(product[i, j]) % factors[i]
            for j in range(order)
            for i in range(order)
        ),
    )


def primitive_orbit_series(lattice, bound: int = ORBIT_NORM_BOUND):
    definiteness = lattice.definiteness()
    match definiteness:
        case "positive_definite":
            sign = 1
        case "negative_definite":
            sign = -1
        case _:
            raise ValueError(f"primitive bounded orbit series requires a definite lattice, not {lattice}")
    gram = _gram_matrix(lattice)
    generators = _orthogonal_generator_matrices(lattice)
    primitive_coordinates = []
    norms = []
    for absolute_norm in range(1, int(bound) + 1):
        for vector in lattice.vectors_of_square(sign * absolute_norm):
            if vector.is_primitive():
                primitive_coordinates.append(_element_coordinates(vector))
                norms.append(absolute_norm)
    vectors = (
        matrix(ZZ, primitive_coordinates).transpose()
        if primitive_coordinates
        else matrix(ZZ, int(lattice.module_rank()), 0)
    )
    factors, actions = _discriminant_actions(gram, generators)
    determinants = [int(generator.det()) for generator in generators]
    discriminant_rank = len(factors)
    counts: dict[str, list[int]] = {}
    for group, flags in {
        "O": (False, False),
        "SO": (True, False),
        "Otilde": (False, True),
        "SOtilde": (True, True),
    }.items():
        with_determinant, with_discriminant = flags
        identity = (
            (
                1,
                *(
                    int(i == j)
                    for i in range(discriminant_rank)
                    for j in range(discriminant_rank)
                ),
            )
            if with_discriminant
            else (1,)
        )
        moves = [
            partial(
                _quotient_action,
                actions[index],
                factors,
                determinants[index],
                with_determinant,
                with_discriminant,
            )
            for index in range(len(generators))
        ]
        elements = _closure(identity, moves)
        positions = {element: position for position, element in enumerate(elements)}
        quotient = [
            [positions[move(element)] for element in elements] for move in moves
        ]
        roots = _orbit_counts(vectors, generators, quotient, len(elements))
        counts[group] = [
            len({roots[index] for index in range(len(norms)) if norms[index] == norm})
            for norm in range(1, int(bound) + 1)
        ]
    zeros = [0] * int(bound)
    plus = (
        {"O+": "SO", "SO+": "SO", "Otilde+": "SOtilde", "SOtilde+": "SOtilde"}
        if sign > 0
        else {"O+": "O", "SO+": "SO", "Otilde+": "Otilde", "SOtilde+": "SOtilde"}
    )
    counts |= {group: counts[source] for group, source in plus.items()}
    return {
        group: {
            "constant": 0,
            "z": values if sign > 0 else zeros,
            "w": zeros if sign > 0 else values,
        }
        for group, values in counts.items()
    }


def _orbits(
    elements: list[TorsionQuadraticModuleElement],
    generators: tuple[FqfIsometry, ...],
) -> list[list[TorsionQuadraticModuleElement]]:
    found: list[list[TorsionQuadraticModuleElement]] = []
    seen: set[TorsionQuadraticModuleElement] = set()
    for start in elements:
        if start in seen:
            continue
        orbit = [start]
        seen.add(start)
        for element in orbit:
            for generator in generators:
                image = generator(element)
                if image not in seen:
                    seen.add(image)
                    orbit.append(image)
        found.append(orbit)
    return found


def discriminant_orbit_series(lattice, bound: int = ORBIT_NORM_BOUND):
    gram = _gram_matrix(lattice)
    backend = IntegralLattice(gram)
    if not backend.is_even():
        raise ValueError(f"discriminant orbit series requires an even lattice, not {lattice}")
    discriminant = backend.discriminant_group()
    elements = list(discriminant)
    classes = {
        norm: [element for element in elements if element.q() == QQ(norm) / element.order() ** 2]
        for norm in range(-int(bound), int(bound) + 1)
    }
    generators = discriminant.orthogonal_group().gens()
    orbits = {norm: _orbits(values, generators) for norm, values in classes.items()}
    series: dict[str, Mapping[int, Sized]] = {
        "Otilde": classes, "SOtilde": classes, "Otilde+": classes, "SOtilde+": classes,
        "O": orbits, "SO": orbits, "O+": orbits, "SO+": orbits,
    }
    return {
        group: {
            "constant": len(counted[0]),
            "z": [len(counted[n]) for n in range(1, int(bound) + 1)],
            "w": [len(counted[-n]) for n in range(1, int(bound) + 1)],
        }
        for group, counted in series.items()
    }


def discriminant_sequence_data(lattice):
    gram = _gram_matrix(lattice)
    lattice_generators = _orthogonal_generator_matrices(lattice)
    module = IntegralLattice(gram).discriminant_group()
    factors = [int(order) for order in module.invariants()]
    group = module.orthogonal_group()
    basis = module.gens()

    def rows(action: Matrix_integer_dense) -> list[list[int]]:
        return [
            [int(action[i, j]) % factors[i] for j in range(len(factors))]
            for i in range(len(factors))
        ]

    def rational_rows(value: Matrix_rational_dense) -> list[list[str]]:
        return [[str(entry) for entry in row] for row in value.rows()]

    images = []
    for generator in lattice_generators:
        columns = [
            [int(coordinate) for coordinate in module(generator * element.lift())]
            for element in basis
        ]
        action = matrix(ZZ, columns).transpose() if columns else matrix(ZZ, 0, 0)
        images.append(group(action))
    image = group.subgroup(images)
    image_elements = list(image)
    group_elements = list(group)
    identity = group.one()
    remaining = set(group_elements)
    representatives = [identity]
    remaining.difference_update(identity * element for element in image_elements)
    while remaining:
        representative = min(remaining, key=lambda element: rows(element.matrix()))
        representatives.append(representative)
        remaining.difference_update(representative * element for element in image_elements)
    normal = all(
        conjugator * element * ~conjugator in image
        for conjugator in group.gens()
        for element in images
    )
    coset_index = {
        frozenset(representative * element for element in image_elements): index
        for index, representative in enumerate(representatives)
    }

    def coset_of(element: FqfIsometry) -> int:
        return coset_index[frozenset(element * member for member in image_elements)]

    orthogonal_order = int(lattice.orthogonal_group().cardinality())
    image_order = int(image.order())
    return {
        "discriminant_factors": factors,
        "discriminant_basis_lifts": [[str(coordinate) for coordinate in element.lift()] for element in basis],
        "discriminant_quadratic_gram": rational_rows(module.gram_matrix_quadratic()),
        "discriminant_group_order": int(group.order()),
        "discriminant_generators": [rows(generator.matrix()) for generator in group.gens()],
        "image_generators": [rows(element.matrix()) for element in images],
        "image_order": image_order,
        "kernel_order": orthogonal_order // image_order,
        "coset_representatives": [rows(element.matrix()) for element in representatives],
        "mm_trivial": len(representatives) == 1,
        "image_normal": normal,
        "quotient_generator_cosets": [coset_of(generator) for generator in group.gens()] if normal else None,
        "quotient_multiplication": [[coset_of(left * right) for right in representatives] for left in representatives] if normal else None,
    }
