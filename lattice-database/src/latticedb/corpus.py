"""The corpus: every `lattices/<TAG>.md` and the families of `families.yaml`, read and validated as one database.

A file is YAML front matter, which holds the record of one lattice, and then
prose in Markdown. The corpus is static: `records` computes and checks each
value once, when the record is written. `load` reads the stored values,
checks that each record has the shape of the schema, and checks the
references between records, families, retired tags and file names.

A tag is permanent. `retired-tags.yaml` lists each tag whose record the corpus
no longer admits, with the lattice that was there and why it is not a record;
no record takes a retired tag, and `next_tag` counts them.

`morphisms/<S>-<T>.md` holds morphisms from the lattice with tag `S` to the
lattice with tag `T`: YAML front matter, a `Morphisms` record, and notes in
Markdown. `records.morphism_problems` checks a morphism when it is written.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb import arithmetic
from latticedb.arithmetic import GramTensor
from latticedb.catalogues import (
    CatalogueRecord,
    Chamber,
    DualIsometry,
    GeometricMap,
    IntegralLocalSystem,
    LatticeGenus,
    LatticePolytope,
    ModuliProblem,
    OrthogonalSubgroup,
    PicardFuchsOperator,
    ToricVariety,
    VectorOrbit,
)
from latticedb.geometric import GeometricFamily, GeometricObject, ToricHypersurfaceConstruction
from latticedb.model import Family, Lattice, Morphisms, Tag, Yaml

TAG_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def front_matter(document: frontmatter.Post) -> dict[str, Yaml]:
    """The YAML mapping at the head of a record file, validated as YAML data."""
    return TypeAdapter(dict[str, Yaml]).validate_python(document.metadata)


Families = dict[Family, str]
"""Each family that a record may name, with one line of its meaning."""

FAMILIES_FILE = "families.yaml"

Retired = dict[Tag, str]
"""Each tag that no record may take again, with the lattice that was there and why it is not a record."""

RETIRED_FILE = "retired-tags.yaml"


@dataclass(frozen=True)
class Entry:
    lattice: Lattice
    prose: str
    path: Path


@dataclass(frozen=True)
class MorphismEntry:
    morphisms: Morphisms
    prose: str
    path: Path


@dataclass(frozen=True)
class GeometricEntry:
    geometric: GeometricObject
    prose: str
    path: Path


@dataclass(frozen=True)
class GeometricFamilyEntry:
    family: GeometricFamily
    prose: str
    path: Path


@dataclass(frozen=True)
class CatalogueEntry[Value: CatalogueRecord]:
    value: Value
    prose: str
    path: Path


@dataclass(frozen=True)
class Corpus:
    entries: tuple[Entry, ...]
    families: Families
    retired: Retired
    morphisms: tuple[MorphismEntry, ...]
    geometric: tuple[GeometricEntry, ...]
    geometric_families: tuple[GeometricFamilyEntry, ...]
    orthogonal_subgroups: tuple[CatalogueEntry[OrthogonalSubgroup], ...]
    vector_orbits: tuple[CatalogueEntry[VectorOrbit], ...]
    chambers: tuple[CatalogueEntry[Chamber], ...]
    genera: tuple[CatalogueEntry[LatticeGenus], ...]
    polytopes: tuple[CatalogueEntry[LatticePolytope], ...]
    toric_varieties: tuple[CatalogueEntry[ToricVariety], ...]
    geometric_maps: tuple[CatalogueEntry[GeometricMap], ...]
    local_systems: tuple[CatalogueEntry[IntegralLocalSystem], ...]
    operators: tuple[CatalogueEntry[PicardFuchsOperator], ...]
    moduli_problems: tuple[CatalogueEntry[ModuliProblem], ...]
    dual_isometries: tuple[CatalogueEntry[DualIsometry], ...]


Matrix = tuple[tuple[int, ...], ...]
Held = dict[tuple[Tag, Tag], tuple[tuple[Matrix, int], ...]]
"""For each pair (source, target) with a morphism file, the matrix and the scale of each of its morphisms."""


def held(corpus: Corpus) -> Held:
    """The matrices and scales of the morphism files of `corpus`."""
    return {(entry.morphisms.source, entry.morphisms.target): tuple((morphism.matrix, morphism.scale) for morphism in entry.morphisms.morphisms) for entry in corpus.morphisms}


class CorpusInvalid(Exception):
    """Raised with every problem of the corpus, one line each."""

    def __init__(self, problems: tuple[str, ...]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


def problems(entries: list[Entry], families: Families, retired: Retired) -> list[str]:
    """The problems that concern more than one record, the families or the retired tags.

    A file name that is not its tag, a retired tag, a repeated name or Gram tensor,
    a family that `families.yaml` does not list, and a related or summand tag that is not in the corpus.
    """
    found = []
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    by_name: dict[str, Path] = {}
    by_components: dict[GramTensor, Path] = {}
    for entry in entries:
        lattice = entry.lattice
        if entry.path.stem != lattice.tag:
            found.append(f"{entry.path}: the file name must be the tag {lattice.tag}")
        if lattice.tag in retired:
            found.append(f"{entry.path}: the tag {lattice.tag} is retired ({retired[lattice.tag]})")
        if lattice.name in by_name:
            found.append(f"{entry.path}: the name '{lattice.name}' is also the name of {by_name[lattice.name]}")
        by_name.setdefault(lattice.name, entry.path)
        if lattice.gram_tensor in by_components:
            found.append(f"{entry.path}: the Gram tensor has the same components as that of {by_components[lattice.gram_tensor]}")
        by_components.setdefault(lattice.gram_tensor, entry.path)
        found.extend(f"{entry.path}: the family '{family}' is not in {FAMILIES_FILE}" for family in lattice.families if family not in families)
        for related in lattice.related:
            if related.tag == lattice.tag:
                found.append(f"{entry.path}: a record cannot be related to itself")
            elif related.tag not in by_tag:
                found.append(f"{entry.path}: the related tag {related.tag} is not in the corpus")
        span = lattice.root_span
        if span is not None and span.summands is not None:
            found.extend(f"{entry.path}: the summand tag {summand.tag} is not in the corpus" for summand in span.summands if summand.tag not in by_tag)
    return found


def hyperbolic_planes(lattice: Lattice) -> int | None:
    """The n with `lattice` isometric to U^n: the n >= 1 for an even unimodular lattice of signature (n, n), else None.

    The even unimodular lattice of signature (n, n) is U^n (the theory page `overlattices`, section `hyperbolic-index`).
    """
    positive, negative = lattice.signature
    if lattice.integral is None or lattice.integral.parity != "even" or abs(lattice.determinant) != 1 or positive != negative or positive == 0:
        return None
    return positive


def hyperbolic_index_bounds(morphisms: Sequence[MorphismEntry], entries: Sequence[Entry]) -> dict[Tag, int]:
    """For each target of a morphism U^n -> T of scale 1, the largest such n: a lower bound for the hyperbolic index of T.

    A morphism of scale 1 from the nondegenerate U^n is an embedding, and the hyperbolic index of an integral T is the largest n with an embedding U^n -> T.
    """
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    bounds: dict[Tag, int] = {}
    for entry in morphisms:
        record = entry.morphisms
        source = by_tag.get(record.source)
        planes = hyperbolic_planes(source) if source is not None else None
        if planes is not None and any(morphism.scale == 1 for morphism in record.morphisms):
            bounds[record.target] = max(planes, bounds.get(record.target, 0))
    return bounds


def morphism_problems(morphisms: list[MorphismEntry], entries: list[Entry], retired: Retired) -> list[str]:
    """The problems of the morphism files.

    A file name that is not `<source>-<target>`, a tag that is not in the corpus or is retired, two files for one pair,
    and a stored hyperbolic index that is less than the n of an embedding U^n -> T.
    """
    found = []
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    pairs: dict[tuple[str, str], Path] = {}
    for entry in morphisms:
        record = entry.morphisms
        pair = (record.source, record.target)
        if entry.path.stem != f"{record.source}-{record.target}":
            found.append(f"{entry.path}: the file name must be {record.source}-{record.target}")
        if pair in pairs:
            found.append(f"{entry.path}: {pairs[pair]} also holds morphisms {record.source} -> {record.target}")
        pairs.setdefault(pair, entry.path)
        missing = [tag for tag in pair if tag not in by_tag]
        found.extend(f"{entry.path}: the tag {tag} is retired ({retired[tag]})" for tag in missing if tag in retired)
        found.extend(f"{entry.path}: the tag {tag} is not in the corpus" for tag in missing if tag not in retired)
    for tag, bound in hyperbolic_index_bounds(morphisms, entries).items():
        target = by_tag.get(tag)
        stored = target.integral.hyperbolic_index if target is not None and target.integral is not None else None
        if stored is not None and stored < bound:
            found.append(f"{tag}: integral.hyperbolic_index is {stored}, and a morphism file embeds U^{bound} into it")
    return found


def _record_problems(path: Path, error: ValidationError) -> list[str]:
    return [f"{path}: {'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]" for problem in error.errors()]


def _catalogue[Value: CatalogueRecord](root: Path, directory: str, schema: type[Value], found: list[str]) -> tuple[CatalogueEntry[Value], ...]:
    entries: list[CatalogueEntry[Value]] = []
    slugs: set[str] = set()
    for path in sorted((root / directory).glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            value = schema.model_validate(document.metadata)
        except ValidationError as error:
            found.extend(_record_problems(path, error))
            continue
        if path.stem != value.slug or value.slug in slugs:
            found.append(f"{path}: {directory} slug must be unique and match its file name")
        slugs.add(value.slug)
        entries.append(CatalogueEntry(value, document.content, path))
    return tuple(entries)


def catalogue_problems(loaded: Corpus) -> list[str]:
    """Check references between the typed catalogues and the lattice and geometric records."""
    found: list[str] = []
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    morphisms = {(entry.morphisms.source, entry.morphisms.target): entry.morphisms for entry in loaded.morphisms}
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
        if group.parent is not None and (group.parent not in groups or groups[group.parent].lattice != group.lattice):
            found.append(f"{entry.path}: parent subgroup {group.parent} must act on lattice {group.lattice}")
        self_maps = morphisms.get((group.lattice, group.lattice))
        names = {m.name for m in self_maps.morphisms if m.scale == 1} if self_maps is not None else set()
        for name in group.generator_morphisms or []:
            if name not in names:
                found.append(f"{entry.path}: generator {name} is not a named self-isometry of {group.lattice}")
        if group.stabilized is not None:
            kind, identifier = group.stabilized.kind, group.stabilized.identifier
            available = {"vector_orbit": orbits, "chamber": chambers, "geometric_object": objects, "geometric_family": families}
            if kind in available and identifier not in available[kind]:
                found.append(f"{entry.path}: stabilized {kind} {identifier} is not in the corpus")
        full_order = lattice.definite.automorphism_group_order if lattice.definite is not None else None
        if full_order is not None and group.order is not None and group.index_in_orthogonal_group is not None:
            if group.order * group.index_in_orthogonal_group != full_order:
                found.append(f"{entry.path}: subgroup order times index must equal |O({group.lattice})| = {full_order}")

    for entry in loaded.vector_orbits:
        orbit = entry.value
        lattice = lattices.get(orbit.lattice)
        group = groups.get(orbit.subgroup)
        if lattice is None or group is None or group.lattice != orbit.lattice:
            found.append(f"{entry.path}: vector orbit needs its lattice and a subgroup of that lattice")
            continue
        vector = orbit.representative
        if len(vector) != lattice.rank or gcd(*vector) != 1:
            found.append(f"{entry.path}: representative must be a primitive vector of rank {lattice.rank}")
            continue
        square = sum((vector[i] * lattice.gram_tensor[i][j] * vector[j] for i in range(lattice.rank) for j in range(lattice.rank)), Fraction())
        if square != orbit.square:
            found.append(f"{entry.path}: representative has square {square}, not {orbit.square}")
        if orbit.divisibility is not None:
            pairings = [sum((lattice.gram_tensor[i][j] * vector[j] for j in range(lattice.rank)), Fraction()) for i in range(lattice.rank)]
            if lattice.integral is None or any(pairing.denominator != 1 for pairing in pairings) or gcd(*(int(pairing) for pairing in pairings)) != orbit.divisibility:
                found.append(f"{entry.path}: divisibility does not match the representative and Gram tensor")
        if orbit.geometric_object is not None and orbit.geometric_object not in objects:
            found.append(f"{entry.path}: geometric object {orbit.geometric_object} is not in the corpus")
        if orbit.geometric_family is not None and orbit.geometric_family not in families:
            found.append(f"{entry.path}: geometric family {orbit.geometric_family} is not in the corpus")

    for entry in loaded.chambers:
        chamber = entry.value
        lattice = lattices.get(chamber.lattice)
        if lattice is None or len(chamber.interior_vector) != lattice.rank or any(len(wall) != lattice.rank for wall in chamber.wall_normals):
            found.append(f"{entry.path}: chamber vectors must lie in its lattice")
        elif min(lattice.signature) != 1 or max(lattice.signature) != lattice.rank - 1:
            found.append(f"{entry.path}: a hyperbolic chamber requires signature (1,n) or (n,1)")
        if chamber.reflection_group is not None and chamber.reflection_group not in groups:
            found.append(f"{entry.path}: reflection group {chamber.reflection_group} is not in the corpus")

    for entry in loaded.genera:
        genus = entry.value
        representatives = []
        for tag in genus.representative_tags:
            lattice = lattices.get(tag)
            if lattice is None or lattice.integral is None or lattice.signature != genus.signature or lattice.determinant != genus.determinant or lattice.integral.parity != genus.parity:
                found.append(f"{entry.path}: representative {tag} does not have the genus signature, determinant and parity")
            else:
                representatives.append(lattice)
                if lattice.integral.genus_symbol is not None and lattice.integral.genus_symbol != genus.symbol:
                    found.append(f"{entry.path}: representative {tag} has a different genus symbol")
        if genus.class_number is not None and len(genus.representative_tags) > genus.class_number:
            found.append(f"{entry.path}: more representative tags than the genus class number")
        if genus.representatives_complete and genus.mass is not None and len(representatives) == len(genus.representative_tags):
            orders = [member.definite.automorphism_group_order if member.definite is not None else None for member in representatives]
            if all(order is not None for order in orders) and sum((Fraction(1, order) for order in orders if order is not None), Fraction()) != genus.mass:
                found.append(f"{entry.path}: mass differs from the sum of reciprocal automorphism-group orders")

    for entry in loaded.dual_isometries:
        dual = entry.value
        lattice = lattices.get(dual.lattice)
        if lattice is None or lattice.integral is None or lattice.integral.modular_scale != dual.scale or not arithmetic.is_dual_isometry(lattice.gram_tensor, dual.scale, dual.matrix):
            found.append(f"{entry.path}: matrix must give the stated isometry L -> L*(k) for lattice {dual.lattice}")
    for tag, lattice in lattices.items():
        if lattice.integral is not None and lattice.integral.modular_scale is not None and tag not in duals:
            found.append(f"{tag}: integral.modular_scale requires a dual-isometry morphism")

    for entry in loaded.polytopes:
        polytope = entry.value
        if polytope.metric_lattice is not None:
            metric = lattices.get(polytope.metric_lattice)
            if metric is None or metric.rank != polytope.ambient_rank or metric.definiteness != "positive_definite":
                found.append(f"{entry.path}: Delaunay metric lattice must be positive definite with the ambient rank")
            elif polytope.delaunay_center is not None and polytope.delaunay_radius_squared is not None:
                center = polytope.delaunay_center
                for vertex in polytope.vertices:
                    displacement = [vertex[i] - center[i] for i in range(polytope.ambient_rank)]
                    square = sum((displacement[i] * metric.gram_tensor[i][j] * displacement[j] for i in range(metric.rank) for j in range(metric.rank)), Fraction())
                    if square != polytope.delaunay_radius_squared:
                        found.append(f"{entry.path}: vertex {vertex} is not on the stated Delaunay sphere")
        if polytope.polar is not None:
            polar = polytopes.get(polytope.polar)
            if polar is None or polar.ambient_rank != polytope.ambient_rank or polar.polar != polytope.slug:
                found.append(f"{entry.path}: polar polytope must name this polytope back and have the same rank")
    for entry in loaded.toric_varieties:
        if entry.value.polytope not in polytopes:
            found.append(f"{entry.path}: polytope {entry.value.polytope} is not in the corpus")
    for entry in loaded.geometric:
        construction = entry.geometric.construction
        if isinstance(construction, ToricHypersurfaceConstruction) and construction.toric_variety not in toric:
            found.append(f"{entry.path}: toric variety {construction.toric_variety} is not in the corpus")
        group = entry.geometric.automorphism_identity_component
        if group is not None and group.cohomology_action is not None and group.cohomology_action not in groups:
            found.append(f"{entry.path}: cohomology action {group.cohomology_action} is not in the corpus")
    for entry in loaded.geometric_families:
        construction = entry.family.construction
        if isinstance(construction, ToricHypersurfaceConstruction) and construction.toric_variety not in toric:
            found.append(f"{entry.path}: toric variety {construction.toric_variety} is not in the corpus")

    targets = {"object": objects, "family": families, "toric_variety": toric}
    for entry in loaded.geometric_maps:
        map_record = entry.value
        for endpoint in (map_record.source, map_record.target, map_record.generic_fiber):
            if endpoint is not None and endpoint.slug not in targets[endpoint.kind]:
                found.append(f"{entry.path}: {endpoint.kind} {endpoint.slug} is not in the corpus")
    for entry in loaded.local_systems:
        system = entry.value
        if system.family not in families:
            found.append(f"{entry.path}: geometric family {system.family} is not in the corpus")
        fibration = maps.get(system.fibration)
        if fibration is None or fibration.kind != "fibration" or fibration.source.kind != "family" or fibration.source.slug != system.family:
            found.append(f"{entry.path}: fibration {system.fibration} must have {system.family} as its source family")
        if system.fiber_lattice is not None:
            lattice = lattices.get(system.fiber_lattice)
            if lattice is None or lattice.rank != system.rank:
                found.append(f"{entry.path}: fiber lattice must have the local system rank {system.rank}")
            else:
                for generator in system.monodromy_generators:
                    columns = tuple(tuple(row[i] for row in generator.matrix) for i in range(system.rank))
                    if arithmetic.restriction(lattice.gram_tensor, columns) != lattice.gram_tensor:
                        found.append(f"{entry.path}: monodromy around {generator.loop} does not preserve the fiber lattice")
    for entry in loaded.operators:
        for realization in entry.value.realizations:
            if realization.family not in families:
                found.append(f"{entry.path}: geometric family {realization.family} is not in the corpus")
            if realization.local_system is not None:
                system = systems.get(realization.local_system)
                if system is None or system.family != realization.family or system.degree != realization.cohomology_degree:
                    found.append(f"{entry.path}: local system {realization.local_system} must belong to the stated family and degree")
    for entry in loaded.moduli_problems:
        problem = entry.value
        if problem.geometric_family not in families:
            found.append(f"{entry.path}: geometric family {problem.geometric_family} is not in the corpus")
        if problem.polarization_orbit is not None and problem.polarization_orbit not in orbits:
            found.append(f"{entry.path}: polarization orbit {problem.polarization_orbit} is not in the corpus")
        if problem.arithmetic_subgroup is not None and problem.arithmetic_subgroup not in groups:
            found.append(f"{entry.path}: arithmetic subgroup {problem.arithmetic_subgroup} is not in the corpus")
    return found


def load(root: Path) -> Corpus:
    """The families, the retired tags, every entry of `root/lattices` in tag order, and every file of `root/morphisms`.

    Raises `CorpusInvalid` with all problems when a record or the corpus is not well defined.
    """
    entries: list[Entry] = []
    found: list[str] = []
    families: Families = {}
    retired: Retired = {}
    families_path = root / FAMILIES_FILE
    retired_path = root / RETIRED_FILE
    # Pydantic reports the problems of a value only through this exception.
    try:
        families = TypeAdapter(Families).validate_python(yaml.safe_load(families_path.read_text()))
    except ValidationError as error:
        found.extend(_record_problems(families_path, error))
    try:
        retired = TypeAdapter(Retired).validate_python(yaml.safe_load(retired_path.read_text()) or {})
    except ValidationError as error:
        found.extend(_record_problems(retired_path, error))
    directory = root / "lattices"
    paths = sorted(directory.glob("*.md"))
    source_tags = {path.stem for path in (directory / "source").glob("*.md")}
    if not paths:
        found.append(f"{directory}: no records")
    for path in paths:
        document = frontmatter.load(str(path))
        if path.stem in source_tags:
            found.append(f"{path}: the tag is also assigned to a source card")
        try:
            entries.append(Entry(Lattice.model_validate(document.metadata), document.content, path))
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    morphisms: list[MorphismEntry] = []
    for path in sorted((root / "morphisms").glob("*.md")):
        document = frontmatter.load(str(path))
        # Pydantic reports the problems of a morphism file only through this exception.
        try:
            morphisms.append(MorphismEntry(Morphisms.model_validate(document.metadata), document.content, path))
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    found.extend(problems(entries, families, retired))
    found.extend(morphism_problems(morphisms, entries, retired))
    geometric: list[GeometricEntry] = []
    for path in sorted((root / "geometric-objects").glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            geometric.append(GeometricEntry(GeometricObject.model_validate(document.metadata), document.content, path))
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    geometric_families: list[GeometricFamilyEntry] = []
    for path in sorted((root / "geometric-families").glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            geometric_families.append(GeometricFamilyEntry(GeometricFamily.model_validate(document.metadata), document.content, path))
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    by_family: dict[str, GeometricFamily] = {}
    for family_entry in geometric_families:
        family = family_entry.family
        if family_entry.path.stem != family.slug or family.slug in by_family:
            found.append(f"{family_entry.path}: geometric family slug must be unique and match its file name")
        by_family[family.slug] = family
    seen_slugs: set[str] = set()
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    for geometric_entry in geometric:
        record = geometric_entry.geometric
        if geometric_entry.path.stem != record.slug or record.slug in seen_slugs:
            found.append(f"{geometric_entry.path}: geometric object slug must be unique and match its file name")
        seen_slugs.add(record.slug)
        if record.family is not None:
            owning_family = by_family.get(record.family)
            if owning_family is None:
                found.append(f"{geometric_entry.path}: geometric family {record.family} is not in the corpus")
            elif record.family_parameter is not None and record.family_parameter < owning_family.minimum:
                found.append(f"{geometric_entry.path}: family parameter is below {owning_family.minimum}")
        for link in record.cohomology_lattices:
            lattice = by_tag.get(link.tag)
            if lattice is None:
                found.append(f"{geometric_entry.path}: cohomology lattice tag {link.tag} is not in the corpus")
            elif lattice.rank != record.betti_number(link.degree):
                found.append(f"{geometric_entry.path}: H^{link.degree} has Betti number {record.betti_number(link.degree)}, but lattice {link.tag} has rank {lattice.rank}")
    loaded = Corpus(
        tuple(entries), families, retired, tuple(morphisms), tuple(geometric), tuple(geometric_families),
        _catalogue(root, "orthogonal-subgroups", OrthogonalSubgroup, found),
        _catalogue(root, "vector-orbits", VectorOrbit, found),
        _catalogue(root, "chambers", Chamber, found),
        _catalogue(root, "genera", LatticeGenus, found),
        _catalogue(root, "lattice-polytopes", LatticePolytope, found),
        _catalogue(root, "toric-varieties", ToricVariety, found),
        _catalogue(root, "geometric-maps", GeometricMap, found),
        _catalogue(root, "integral-local-systems", IntegralLocalSystem, found),
        _catalogue(root, "picard-fuchs-operators", PicardFuchsOperator, found),
        _catalogue(root, "moduli-problems", ModuliProblem, found),
        _catalogue(root, "morphisms/dual", DualIsometry, found),
    )
    found.extend(catalogue_problems(loaded))
    if found:
        raise CorpusInvalid(tuple(found))
    return loaded


def next_tag(corpus: Corpus) -> str:
    """The tag after the greatest corpus, source-card, or retired tag."""
    value = 0
    source_directory = corpus.entries[0].path.parent / "source"
    source_tags = (path.stem for path in source_directory.glob("*.md"))
    for character in max(*(entry.lattice.tag for entry in corpus.entries), *corpus.retired, *source_tags):
        value = value * len(TAG_ALPHABET) + TAG_ALPHABET.index(character)
    value += 1
    digits = []
    for _ in range(4):
        value, digit = divmod(value, len(TAG_ALPHABET))
        digits.append(TAG_ALPHABET[digit])
    assert value == 0, "the four-character tag space is full"
    return "".join(reversed(digits))
