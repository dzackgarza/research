"""Checks of the typed catalogues against the records that they name.

A catalogue file holds one record of its own kind under `slug/`. `load` reads
those records and never looks at what they name, so every reference from a
catalogue to a lattice, a morphism, a geometric object or another catalogue is
checked here.
"""

from collections.abc import Sequence
from fractions import Fraction
from math import gcd

from latticedb import arithmetic
from latticedb.corpus import CatalogueEntry, Corpus
from latticedb.geometric import ProjectiveComplexVariety, ToricHypersurfaceConstruction


def slug_problems(entries: Sequence[CatalogueEntry]) -> list[str]:
    """The problems of the file names of `entries`: each must be the slug of its own record, and each slug once."""
    found: list[str] = []
    slugs: set[str] = set()
    for entry in entries:
        directory = entry.path.parent.name
        if entry.path.stem != entry.value.slug or entry.value.slug in slugs:
            found.append(
                f"{entry.path}: {directory} slug must be unique and match its file name"
            )
        slugs.add(entry.value.slug)
    return found


def reference_problems(loaded: Corpus) -> list[str]:
    """Check references between the typed catalogues and the lattice and geometric records."""
    found: list[str] = []
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    morphisms = {
        (entry.morphisms.source, entry.morphisms.target): entry.morphisms
        for entry in loaded.morphisms
    }
    objects = {entry.geometric.slug for entry in loaded.geometric}
    families = {entry.family.slug for entry in loaded.geometric_families}
    groups = {entry.value.slug: entry.value for entry in loaded.orthogonal_subgroups}
    orbits = {entry.value.slug for entry in loaded.vector_orbits}
    chambers = {entry.value.slug for entry in loaded.chambers}
    polytopes = {entry.value.slug: entry.value for entry in loaded.polytopes}
    toric = {entry.value.slug for entry in loaded.toric_varieties}
    maps = {entry.value.slug: entry.value for entry in loaded.geometric_maps}
    systems = {entry.value.slug: entry.value for entry in loaded.local_systems}
    duals = {entry.value.lattice: entry.value for entry in loaded.dual_isometries}

    for entry in loaded.orthogonal_subgroups:
        group = entry.value
        lattice = lattices.get(group.lattice)
        if lattice is None:
            found.append(f"{entry.path}: lattice {group.lattice} is not in the corpus")
            continue
        if group.parent is not None and (
            group.parent not in groups or groups[group.parent].lattice != group.lattice
        ):
            found.append(
                f"{entry.path}: parent subgroup {group.parent} must act on lattice {group.lattice}"
            )
        self_maps = morphisms.get((group.lattice, group.lattice))
        names = (
            {m.name for m in self_maps.morphisms if m.scale == 1}
            if self_maps is not None
            else set()
        )
        for name in group.generator_morphisms or []:
            if name not in names:
                found.append(
                    f"{entry.path}: generator {name} is not a named self-isometry of {group.lattice}"
                )
        if group.stabilized is not None:
            kind, identifier = group.stabilized.kind, group.stabilized.identifier
            available = {
                "vector_orbit": orbits,
                "chamber": chambers,
                "geometric_object": objects,
                "geometric_family": families,
            }
            if kind in available and identifier not in available[kind]:
                found.append(
                    f"{entry.path}: stabilized {kind} {identifier} is not in the corpus"
                )
        full_order = (
            lattice.definite.automorphism_group_order
            if lattice.definite is not None
            else None
        )
        if (
            full_order is not None
            and group.order is not None
            and group.index_in_orthogonal_group is not None
        ):
            if group.order * group.index_in_orthogonal_group != full_order:
                found.append(
                    f"{entry.path}: subgroup order times index must equal |O({group.lattice})| = {full_order}"
                )

    for entry in loaded.vector_orbits:
        orbit = entry.value
        lattice = lattices.get(orbit.lattice)
        group = groups.get(orbit.subgroup)
        if lattice is None or group is None or group.lattice != orbit.lattice:
            found.append(
                f"{entry.path}: vector orbit needs its lattice and a subgroup of that lattice"
            )
            continue
        vector = orbit.representative
        if len(vector) != lattice.rank or gcd(*vector) != 1:
            found.append(
                f"{entry.path}: representative must be a primitive vector of rank {lattice.rank}"
            )
            continue
        square = sum(
            (
                vector[i] * lattice.gram_tensor[i][j] * vector[j]
                for i in range(lattice.rank)
                for j in range(lattice.rank)
            ),
            Fraction(),
        )
        if square != orbit.square:
            found.append(
                f"{entry.path}: representative has square {square}, not {orbit.square}"
            )
        if orbit.divisibility is not None:
            pairings = [
                sum(
                    (
                        lattice.gram_tensor[i][j] * vector[j]
                        for j in range(lattice.rank)
                    ),
                    Fraction(),
                )
                for i in range(lattice.rank)
            ]
            if (
                lattice.integral is None
                or any(pairing.denominator != 1 for pairing in pairings)
                or gcd(*(int(pairing) for pairing in pairings)) != orbit.divisibility
            ):
                found.append(
                    f"{entry.path}: divisibility does not match the representative and Gram tensor"
                )
        if orbit.geometric_object is not None and orbit.geometric_object not in objects:
            found.append(
                f"{entry.path}: geometric object {orbit.geometric_object} is not in the corpus"
            )
        if (
            orbit.geometric_family is not None
            and orbit.geometric_family not in families
        ):
            found.append(
                f"{entry.path}: geometric family {orbit.geometric_family} is not in the corpus"
            )

    for entry in loaded.chambers:
        chamber = entry.value
        lattice = lattices.get(chamber.lattice)
        if (
            lattice is None
            or len(chamber.interior_vector) != lattice.rank
            or any(len(wall) != lattice.rank for wall in chamber.wall_normals)
        ):
            found.append(f"{entry.path}: chamber vectors must lie in its lattice")
        elif min(lattice.signature) != 1 or max(lattice.signature) != lattice.rank - 1:
            found.append(
                f"{entry.path}: a hyperbolic chamber requires signature (1,n) or (n,1)"
            )
        if (
            chamber.reflection_group is not None
            and chamber.reflection_group not in groups
        ):
            found.append(
                f"{entry.path}: reflection group {chamber.reflection_group} is not in the corpus"
            )

    for entry in loaded.genera:
        genus = entry.value
        representatives = []
        for tag in genus.representative_tags:
            lattice = lattices.get(tag)
            if (
                lattice is None
                or lattice.integral is None
                or lattice.signature != genus.signature
                or lattice.determinant != genus.determinant
                or lattice.integral.parity != genus.parity
            ):
                found.append(
                    f"{entry.path}: representative {tag} does not have the genus signature, determinant and parity"
                )
            else:
                representatives.append(lattice)
                if (
                    lattice.integral.genus_symbol is not None
                    and lattice.integral.genus_symbol != genus.symbol
                ):
                    found.append(
                        f"{entry.path}: representative {tag} has a different genus symbol"
                    )
        if (
            genus.class_number is not None
            and len(genus.representative_tags) > genus.class_number
        ):
            found.append(
                f"{entry.path}: more representative tags than the genus class number"
            )
        if (
            genus.representatives_complete
            and genus.mass is not None
            and len(representatives) == len(genus.representative_tags)
        ):
            orders = [
                member.definite.automorphism_group_order
                if member.definite is not None
                else None
                for member in representatives
            ]
            if (
                all(order is not None for order in orders)
                and sum(
                    (Fraction(1, order) for order in orders if order is not None),
                    Fraction(),
                )
                != genus.mass
            ):
                found.append(
                    f"{entry.path}: mass differs from the sum of reciprocal automorphism-group orders"
                )

    for entry in loaded.dual_isometries:
        dual = entry.value
        lattice = lattices.get(dual.lattice)
        if (
            lattice is None
            or lattice.integral is None
            or lattice.integral.modular_scale != dual.scale
            or not arithmetic.is_dual_isometry(
                lattice.gram_tensor, dual.scale, dual.matrix
            )
        ):
            found.append(
                f"{entry.path}: matrix must give the stated isometry L -> L*(k) for lattice {dual.lattice}"
            )
    for tag, lattice in lattices.items():
        if (
            lattice.integral is not None
            and lattice.integral.modular_scale is not None
            and tag not in duals
        ):
            found.append(
                f"{tag}: integral.modular_scale requires a dual-isometry morphism"
            )

    for entry in loaded.polytopes:
        polytope = entry.value
        if polytope.metric_lattice is not None:
            metric = lattices.get(polytope.metric_lattice)
            if (
                metric is None
                or metric.rank != polytope.ambient_rank
                or metric.definiteness != "positive_definite"
            ):
                found.append(
                    f"{entry.path}: Delaunay metric lattice must be positive definite with the ambient rank"
                )
            elif (
                polytope.delaunay_center is not None
                and polytope.delaunay_radius_squared is not None
            ):
                center = polytope.delaunay_center
                for vertex in polytope.vertices:
                    displacement = [
                        vertex[i] - center[i] for i in range(polytope.ambient_rank)
                    ]
                    square = sum(
                        (
                            displacement[i] * metric.gram_tensor[i][j] * displacement[j]
                            for i in range(metric.rank)
                            for j in range(metric.rank)
                        ),
                        Fraction(),
                    )
                    if square != polytope.delaunay_radius_squared:
                        found.append(
                            f"{entry.path}: vertex {vertex} is not on the stated Delaunay sphere"
                        )
        if polytope.polar is not None:
            polar = polytopes.get(polytope.polar)
            if (
                polar is None
                or polar.ambient_rank != polytope.ambient_rank
                or polar.polar != polytope.slug
            ):
                found.append(
                    f"{entry.path}: polar polytope must name this polytope back and have the same rank"
                )
    for entry in loaded.toric_varieties:
        if entry.value.polytope not in polytopes:
            found.append(
                f"{entry.path}: polytope {entry.value.polytope} is not in the corpus"
            )
    for entry in loaded.geometric:
        record = entry.geometric
        if isinstance(record, ProjectiveComplexVariety):
            construction = record.construction
            if (
                isinstance(construction, ToricHypersurfaceConstruction)
                and construction.toric_variety not in toric
            ):
                found.append(
                    f"{entry.path}: toric variety {construction.toric_variety} is not in the corpus"
                )
            group = record.automorphism_identity_component
            if (
                group is not None
                and group.cohomology_action is not None
                and group.cohomology_action not in groups
            ):
                found.append(
                    f"{entry.path}: cohomology action {group.cohomology_action} is not in the corpus"
                )
    for entry in loaded.geometric_families:
        construction = entry.family.construction
        if (
            isinstance(construction, ToricHypersurfaceConstruction)
            and construction.toric_variety not in toric
        ):
            found.append(
                f"{entry.path}: toric variety {construction.toric_variety} is not in the corpus"
            )

    targets = {"object": objects, "family": families, "toric_variety": toric}
    for entry in loaded.geometric_maps:
        map_record = entry.value
        for endpoint in (
            map_record.source,
            map_record.target,
            map_record.generic_fiber,
        ):
            if endpoint is not None and endpoint.slug not in targets[endpoint.kind]:
                found.append(
                    f"{entry.path}: {endpoint.kind} {endpoint.slug} is not in the corpus"
                )
    for entry in loaded.local_systems:
        system = entry.value
        if system.family not in families:
            found.append(
                f"{entry.path}: geometric family {system.family} is not in the corpus"
            )
        fibration = maps.get(system.fibration)
        if (
            fibration is None
            or fibration.kind != "fibration"
            or fibration.source.kind != "family"
            or fibration.source.slug != system.family
        ):
            found.append(
                f"{entry.path}: fibration {system.fibration} must have {system.family} as its source family"
            )
        if system.fiber_lattice is not None:
            lattice = lattices.get(system.fiber_lattice)
            if lattice is None or lattice.rank != system.rank:
                found.append(
                    f"{entry.path}: fiber lattice must have the local system rank {system.rank}"
                )
            else:
                for generator in system.monodromy_generators:
                    columns = tuple(
                        tuple(row[i] for row in generator.matrix)
                        for i in range(system.rank)
                    )
                    if (
                        arithmetic.restriction(lattice.gram_tensor, columns)
                        != lattice.gram_tensor
                    ):
                        found.append(
                            f"{entry.path}: monodromy around {generator.loop} does not preserve the fiber lattice"
                        )
    for entry in loaded.operators:
        for realization in entry.value.realizations:
            if realization.family not in families:
                found.append(
                    f"{entry.path}: geometric family {realization.family} is not in the corpus"
                )
            if realization.local_system is not None:
                system = systems.get(realization.local_system)
                if (
                    system is None
                    or system.family != realization.family
                    or system.degree != realization.cohomology_degree
                ):
                    found.append(
                        f"{entry.path}: local system {realization.local_system} must belong to the stated family and degree"
                    )
    for entry in loaded.moduli_problems:
        problem = entry.value
        if problem.geometric_family not in families:
            found.append(
                f"{entry.path}: geometric family {problem.geometric_family} is not in the corpus"
            )
        if (
            problem.polarization_orbit is not None
            and problem.polarization_orbit not in orbits
        ):
            found.append(
                f"{entry.path}: polarization orbit {problem.polarization_orbit} is not in the corpus"
            )
        if (
            problem.arithmetic_subgroup is not None
            and problem.arithmetic_subgroup not in groups
        ):
            found.append(
                f"{entry.path}: arithmetic subgroup {problem.arithmetic_subgroup} is not in the corpus"
            )
    return found


def problems(loaded: Corpus) -> list[str]:
    """The problems of the typed catalogues: their file names, and every record that they name."""
    return [
        *slug_problems(loaded.orthogonal_subgroups),
        *slug_problems(loaded.vector_orbits),
        *slug_problems(loaded.chambers),
        *slug_problems(loaded.genera),
        *slug_problems(loaded.polytopes),
        *slug_problems(loaded.toric_varieties),
        *slug_problems(loaded.geometric_maps),
        *slug_problems(loaded.local_systems),
        *slug_problems(loaded.operators),
        *slug_problems(loaded.moduli_problems),
        *slug_problems(loaded.dual_isometries),
        *reference_problems(loaded),
    ]
