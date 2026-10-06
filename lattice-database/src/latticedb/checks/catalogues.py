"""Checks of the typed catalogues against the records that they name.

A catalogue file holds one record of its own kind under `slug/`. `load` reads
those records and never looks at what they name, so every reference from a
catalogue to a lattice, a morphism, a geometric object or another catalogue is
checked here.
"""

from collections.abc import Sequence

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
    objects = {entry.geometric.slug for entry in loaded.geometric}
    families = {entry.family.slug for entry in loaded.geometric_families}
    polytopes = {entry.value.slug: entry.value for entry in loaded.polytopes}
    toric = {entry.value.slug for entry in loaded.toric_varieties}
    maps = {entry.value.slug: entry.value for entry in loaded.geometric_maps}
    systems = {entry.value.slug: entry.value for entry in loaded.local_systems}
    lie_groups = {entry.value.slug: entry.value for entry in loaded.lie_groups}
    arithmetic_groups = {entry.value.slug: entry.value for entry in loaded.arithmetic_groups}

    for entry in loaded.lie_groups:
        group = entry.value
        for factor in group.maximal_compact_factors:
            if factor not in lie_groups:
                found.append(f"{entry.path}: maximal compact factor {factor} is not a Lie-group card")

    for entry in loaded.arithmetic_groups:
        arithmetic = entry.value
        lattice = lattices.get(arithmetic.lattice)
        path = str(entry.path)
        ambient = lie_groups.get(arithmetic.ambient_lie_group)
        if lattice is None:
            found.append(f"{path}: lattice {arithmetic.lattice} is not in the corpus")
            continue
        if ambient is None:
            found.append(f"{path}: ambient Lie group {arithmetic.ambient_lie_group} is not in the corpus")
        if arithmetic.parent_group is not None:
            parent = arithmetic_groups.get(arithmetic.parent_group)
            if parent is None or parent.lattice != arithmetic.lattice:
                found.append(f"{path}: parent arithmetic group must be a card on lattice {arithmetic.lattice}")
        group = arithmetic.data
        if group.defining_relators is not None and group.generator_morphisms is None:
            found.append(f"{path}: relators require the generator list they are words in")
        for name in group.generator_morphisms or ():
            names = {
                morphism.name
                for morphism in lattice.morphisms
                if morphism.target == lattice.tag and morphism.scale == 1
            }
            if name not in names:
                found.append(f"{path}: generator {name} is not a named self-isometry of {lattice.tag}")
        if group.stabilized is not None:
            kind, identifier = group.stabilized.kind, group.stabilized.identifier
            available = {
                "chamber": {lattice.tag},
                "geometric_object": objects,
                "geometric_family": families,
            }
            if kind in available and identifier not in available[kind]:
                found.append(f"{path}: stabilized {kind} {identifier} is not in the corpus")
        for orbit_data in group.orbits or ():
            for vector in orbit_data.representatives:
                if lattice.rank is None or len(vector) != lattice.rank:
                    found.append(f"{path}: orbit representative must have rank {lattice.rank} coordinates")
        chamber = group.chamber
        if chamber is not None:
            if (
                lattice.rank is None
                or len(chamber.interior_vector) != lattice.rank
                or any(len(wall) != lattice.rank for wall in chamber.wall_normals)
            ):
                found.append(f"{path}: chamber vectors must lie in its lattice")

    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.orthogonal_group is not None:
            group = arithmetic_groups.get(lattice.orthogonal_group)
            if group is None or group.lattice != lattice.tag or group.standard_name != "O":
                found.append(f"{entry.path}: orthogonal_group must name the O arithmetic-group card of this lattice")
        for slug in lattice.arithmetic_groups:
            group = arithmetic_groups.get(slug)
            if group is None or group.lattice != lattice.tag:
                found.append(f"{entry.path}: arithmetic group {slug} must be a card on this lattice")
        if lattice.orthogonal_group is not None and lattice.orthogonal_group not in lattice.arithmetic_groups:
            found.append(f"{entry.path}: orthogonal_group must also occur in arithmetic_groups")

    for entry in loaded.genera:
        genus = entry.value
        for tag in genus.representative_tags:
            if tag not in lattices:
                found.append(f"{entry.path}: representative {tag} is not a lattice card")
        if (
            genus.class_number is not None
            and len(genus.representative_tags) > genus.class_number
        ):
            found.append(
                f"{entry.path}: more representative tags than the genus class number"
            )
    for entry in loaded.polytopes:
        polytope = entry.value
        if polytope.metric_lattice is not None:
            if polytope.metric_lattice not in lattices:
                found.append(f"{entry.path}: metric lattice {polytope.metric_lattice} is not in the corpus")
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
                and group.cohomology_action not in arithmetic_groups
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
            if lattice is None:
                found.append(
                    f"{entry.path}: fiber lattice {system.fiber_lattice} is not in the corpus"
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
        if problem.arithmetic_subgroup is not None and problem.arithmetic_subgroup not in arithmetic_groups:
            found.append(f"{entry.path}: arithmetic subgroup {problem.arithmetic_subgroup} is not an arithmetic-group card")
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
        *slug_problems(loaded.lattice_families),
        *slug_problems(loaded.lie_groups),
        *slug_problems(loaded.arithmetic_groups),
        *reference_problems(loaded),
    ]
