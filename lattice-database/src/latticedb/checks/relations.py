"""Checks of the references that run between the records of the corpus.

`load` reads each file and stops at its own front matter, so it never compares
two records. Everything here is such a comparison: a tag against its file name,
a record against the families and the retired tags, a stored morphism against
its target record, a geometric object against the lattices, the graphs and the
other geometric objects that it names.
"""

from pathlib import Path

from latticedb import records
from latticedb.corpus import FAMILIES_FILE, Corpus
from latticedb.geometric import (
    ComplexManifold,
    GeometricFamily,
    ProjectiveComplexVariety,
    RiemannianSymmetricSpace,
)
from latticedb.graphs import WeightedGraph
from latticedb.model import GramTensor
from latticedb.relations import hyperbolic_index_bounds

SOURCE_DIRECTORY = "lattices/source"
"""Where `seed` reads rows that have not yet become permanent cards."""


def lattice_problems(loaded: Corpus, root: Path) -> list[str]:
    """The problems that concern more than one lattice record.

    A file name that is not its tag, a tag that a source row also reserves, a retired tag,
    a repeated name or Gram tensor, a definite card isometric to another in another basis,
    a family that `families.yaml` does not list, and a
    related or summand tag that is not in the corpus.
    """
    entries = loaded.entries
    retired = loaded.retired
    found: list[str] = []
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    source_paths = sorted((root / SOURCE_DIRECTORY).glob("*.md"))
    reserved = {path.stem for path in source_paths}
    found.extend(
        f"{path}: source card has not been seeded to a permanent lattice card"
        for path in source_paths
    )
    by_name: dict[str, Path] = {}
    by_components: dict[GramTensor, Path] = {}
    for entry in entries:
        lattice = entry.lattice
        if entry.path.stem != lattice.tag:
            found.append(f"{entry.path}: the file name must be the tag {lattice.tag}")
        if lattice.tag in reserved:
            found.append(f"{entry.path}: the tag is also assigned to a source card")
        if lattice.tag in retired:
            found.append(
                f"{entry.path}: the tag {lattice.tag} is retired ({retired[lattice.tag]})"
            )
        if lattice.name in by_name:
            found.append(
                f"{entry.path}: the name '{lattice.name}' is also the name of {by_name[lattice.name]}"
            )
        by_name.setdefault(lattice.name, entry.path)
        if lattice.gram_tensor is not None and lattice.gram_tensor in by_components:
            found.append(
                f"{entry.path}: the Gram tensor has the same components as that of {by_components[lattice.gram_tensor]}"
            )
        if lattice.gram_tensor is not None:
            by_components.setdefault(lattice.gram_tensor, entry.path)
        found.extend(
            f"{entry.path}: the family '{family}' is not in {FAMILIES_FILE}"
            for family in lattice.families
            if family not in loaded.families
        )
        for related in lattice.related:
            if related.tag == lattice.tag:
                found.append(f"{entry.path}: a record cannot be related to itself")
            elif related.tag not in by_tag:
                found.append(
                    f"{entry.path}: the related tag {related.tag} is not in the corpus"
                )
        found.extend(
            f"{entry.path}: {problem}"
            for problem in records.relational_admission_problems(lattice, by_tag)
        )
    isometric = records.definite_isometry_problems(
        tuple(entry.lattice for entry in entries)
    )
    found.extend(
        f"{entry.path}: {problem}"
        for entry in entries
        for problem in isometric.get(entry.lattice.tag, ())
    )
    return found


def morphism_problems(loaded: Corpus) -> list[str]:
    """Reference and preamble-backed mathematical problems of stored morphisms."""
    entries = loaded.entries
    retired = loaded.retired
    found: list[str] = []
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    for entry in entries:
        source = entry.lattice
        for morphism in source.morphisms:
            target = by_tag.get(morphism.target)
            if target is None:
                if morphism.target in retired:
                    found.append(
                        f"{entry.path}: morphism target {morphism.target} is retired ({retired[morphism.target]})"
                    )
                else:
                    found.append(f"{entry.path}: morphism target {morphism.target} is not in the corpus")
                continue
            found.extend(
                f"{entry.path}: morphisms.{morphism.name}: {problem}"
                for problem in records.morphism_problems(morphism, source, target)
            )
    for tag, bound in hyperbolic_index_bounds(entries).items():
        target = by_tag.get(tag)
        stored = (
            target.integral.hyperbolic_index
            if target is not None and target.integral is not None
            else None
        )
        if stored is not None and stored < bound:
            found.append(
                f"{tag}: integral.hyperbolic_index is {stored}, and a stored morphism embeds U^{bound} into it"
            )
    return found


def geometric_problems(loaded: Corpus) -> list[str]:
    """The problems of the graphs, the geometric families and the geometric objects.

    These are storage/reference checks only: slug uniqueness, named targets, and reciprocal
    links between records. Mathematical validity belongs to the corresponding preamble objects.
    """
    found: list[str] = []
    by_graph: dict[str, WeightedGraph] = {}
    for entry in loaded.graphs:
        if entry.path.stem != entry.graph.slug or entry.graph.slug in by_graph:
            found.append(
                f"{entry.path}: graph slug must be unique and match its file name"
            )
        by_graph[entry.graph.slug] = entry.graph
    by_family: dict[str, GeometricFamily] = {}
    for family_entry in loaded.geometric_families:
        family = family_entry.family
        if family_entry.path.stem != family.slug or family.slug in by_family:
            found.append(
                f"{family_entry.path}: geometric family slug must be unique and match its file name"
            )
        by_family[family.slug] = family
    seen_slugs: set[str] = set()
    by_tag = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    by_geometric = {entry.geometric.slug: entry.geometric for entry in loaded.geometric}
    for geometric_entry in loaded.geometric:
        record = geometric_entry.geometric
        if geometric_entry.path.stem != record.slug or record.slug in seen_slugs:
            found.append(
                f"{geometric_entry.path}: geometric object slug must be unique and match its file name"
            )
        seen_slugs.add(record.slug)
        if isinstance(record, ProjectiveComplexVariety) and record.family is not None:
            owning_family = by_family.get(record.family)
            if owning_family is None:
                found.append(
                    f"{geometric_entry.path}: geometric family {record.family} is not in the corpus"
                )
            elif (
                record.family_parameter is not None
                and record.family_parameter < owning_family.minimum
            ):
                found.append(
                    f"{geometric_entry.path}: family parameter is below {owning_family.minimum}"
                )
        if isinstance(record, ProjectiveComplexVariety):
            for link in record.cohomology_lattices:
                lattice = by_tag.get(link.tag)
                if lattice is None:
                    found.append(
                        f"{geometric_entry.path}: cohomology lattice tag {link.tag} is not in the corpus"
                    )
                elif lattice.rank != record.betti_number(link.degree):
                    found.append(
                        f"{geometric_entry.path}: H^{link.degree} has Betti number {record.betti_number(link.degree)}, but lattice {link.tag} has rank {lattice.rank}"
                    )
            if record.analytic_space is not None:
                analytic = by_geometric.get(record.analytic_space)
                if (
                    not isinstance(analytic, ComplexManifold)
                    or analytic.algebraic_model != record.slug
                    or analytic.complex_dimension != record.dimension
                ):
                    found.append(
                        f"{geometric_entry.path}: analytic space must name this variety back and have the same complex dimension"
                    )
        if isinstance(record, ComplexManifold) and record.algebraic_model is not None:
            algebraic = by_geometric.get(record.algebraic_model)
            if (
                not isinstance(algebraic, ProjectiveComplexVariety)
                or algebraic.analytic_space != record.slug
                or algebraic.dimension != record.complex_dimension
            ):
                found.append(
                    f"{geometric_entry.path}: algebraic model must name this analytic space back and have the same complex dimension"
                )
        if (
            isinstance(record, RiemannianSymmetricSpace)
            and record.compact_dual is not None
        ):
            dual = by_geometric.get(record.compact_dual)
            if (
                not isinstance(dual, RiemannianSymmetricSpace)
                or dual.noncompact_dual != record.slug
                or dual.real_dimension != record.real_dimension
            ):
                found.append(
                    f"{geometric_entry.path}: compact dual must be a symmetric space of the same dimension and name this space back"
                )
        if isinstance(record, RiemannianSymmetricSpace):
            for diagram in record.diagrams:
                if diagram not in by_graph:
                    found.append(
                        f"{geometric_entry.path}: diagram {diagram} is not in the corpus"
                    )
        if (
            isinstance(record, RiemannianSymmetricSpace)
            and record.noncompact_dual is not None
        ):
            dual = by_geometric.get(record.noncompact_dual)
            if (
                not isinstance(dual, RiemannianSymmetricSpace)
                or dual.compact_dual != record.slug
                or dual.real_dimension != record.real_dimension
            ):
                found.append(
                    f"{geometric_entry.path}: noncompact dual must be a symmetric space of the same dimension and name this space back"
                )
    return found


def problems(loaded: Corpus, root: Path) -> list[str]:
    """Every problem of the references that run between the records."""
    return [
        *lattice_problems(loaded, root),
        *morphism_problems(loaded),
        *geometric_problems(loaded),
    ]
