"""Checks of the typed catalogues against the records that they name.

A catalogue file holds one record of its own kind under `slug/`. `load` reads
those records and never looks at what they name, so every reference from a
catalogue to a lattice, a morphism, a geometric object or another catalogue is
checked here.
"""

from collections.abc import Sequence
from fractions import Fraction
from math import gcd

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb.corpus import CatalogueEntry, Corpus
from latticedb.geometric import ProjectiveComplexVariety, ToricHypersurfaceConstruction

_SESSION_RINGS = session_ring_objects()
ZZ = _SESSION_RINGS["ZZ"]


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
    polytopes = {entry.value.slug: entry.value for entry in loaded.polytopes}
    toric = {entry.value.slug for entry in loaded.toric_varieties}
    maps = {entry.value.slug: entry.value for entry in loaded.geometric_maps}
    systems = {entry.value.slug: entry.value for entry in loaded.local_systems}
    duals = {entry.value.lattice: entry.value for entry in loaded.dual_isometries}

    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.groups is None:
            continue
        for key, group in lattice.groups.items():
            path = f"{entry.path}: groups.{key}"
            for name in group.generator_morphisms or ():
                self_maps = morphisms.get((lattice.tag, lattice.tag))
                names = (
                    {m.name for m in self_maps.morphisms if m.scale == 1}
                    if self_maps is not None
                    else set()
                )
                if name not in names:
                    found.append(
                        f"{path}: generator {name} is not a named self-isometry of {lattice.tag}"
                    )
            if group.stabilized is not None:
                kind, identifier = group.stabilized.kind, group.stabilized.identifier
                available = {
                    "chamber": {lattice.tag},
                    "geometric_object": objects,
                    "geometric_family": families,
                }
                if kind in available and identifier not in available[kind]:
                    found.append(
                        f"{path}: stabilized {kind} {identifier} is not in the corpus"
                    )
            full_order = (
                lattice.definite.automorphism_group_order
                if lattice.definite is not None
                else None
            )
            if (
                full_order is not None
                and isinstance(group.cardinality, int)
                and group.index_in_orthogonal_group is not None
                and group.cardinality * group.index_in_orthogonal_group != full_order
            ):
                found.append(
                    f"{path}: subgroup order times index must equal |O({lattice.tag})| = {full_order}"
                )
            for orbit_data in group.orbits or ():
                n = orbit_data.square
                for vector in orbit_data.representatives:
                    if lattice.rank is None or len(vector) != lattice.rank:
                        found.append(
                            f"{path}: orbit representative must have rank {lattice.rank} coordinates"
                        )
                        continue
                    if gcd(*vector) != 1:
                        found.append(f"{path}: orbit representative must be primitive")
                        continue
                    square = sum(
                        (
                            vector[i] * lattice.gram_tensor[i][j] * vector[j]
                            for i in range(lattice.rank)
                            for j in range(lattice.rank)
                        ),
                        Fraction(),
                    )
                    if square != n:
                        found.append(
                            f"{path}: representative has square {square}, not {n}"
                        )
            chamber = group.chamber
            if chamber is not None:
                if (
                    lattice.rank is None
                    or len(chamber.interior_vector) != lattice.rank
                    or any(len(wall) != lattice.rank for wall in chamber.wall_normals)
                ):
                    found.append(f"{path}: chamber vectors must lie in its lattice")
                elif (
                    lattice.signature is None
                    or min(lattice.signature) != 1
                    or max(lattice.signature) != lattice.rank - 1
                ):
                    found.append(
                        f"{path}: a hyperbolic chamber requires signature (1,n) or (n,1)"
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
        valid = False
        if (
            lattice is not None
            and lattice.integral is not None
            and lattice.integral.modular_scale == dual.scale
        ):
            source = Lattices(ZZ)(lattice.gram_tensor)
            twisted_dual = source.dual_lattice().twist(dual.scale)
            try:
                target = Lattices(ZZ)(twisted_dual.gram_tensor())
                images = tuple(
                    target(vector)
                    for vector in zip(*dual.matrix, strict=True)
                )
                source.Isom(target)(images)
                valid = True
            except (AssertionError, TypeError, ValueError):
                valid = False
        if not valid:
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
                owned_lattice = Lattices(ZZ)(lattice.gram_tensor)
                for generator in system.monodromy_generators:
                    columns = tuple(
                        tuple(row[i] for row in generator.matrix)
                        for i in range(system.rank)
                    )
                    try:
                        owned_lattice.Aut()(
                            tuple(owned_lattice(column) for column in columns)
                        )
                    except ValueError:
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
    return found


def problems(loaded: Corpus) -> list[str]:
    """The problems of the typed catalogues: their file names, and every record that they name."""
    return [
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
