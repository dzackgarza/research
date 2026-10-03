"""The corpus: every `lattices/<TAG>.md` and the families of `families.yaml`, read as one database.

A file is YAML front matter, which holds the record of one lattice, and then
prose in Markdown. `load` reads the stored values and checks only that each
file has the shape of its schema. The references between records, families,
retired tags, catalogues and file names are checked by the read-only
verification in `latticedb.checks`, never while reading.

A tag is permanent. `retired-tags.yaml` lists each tag whose record the corpus
no longer admits, with the lattice that was there and why it is not a record;
no record takes a retired tag, and `next_tag` counts them.

`morphisms/<S>-<T>.md` holds morphisms from the lattice with tag `S` to the
lattice with tag `T`: YAML front matter, a `Morphisms` record, and notes in
Markdown.
"""

from dataclasses import dataclass
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

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
from latticedb.geometric import GeometricFamily, GeometricObject
from latticedb.graphs import WeightedGraph
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
class GraphEntry:
    graph: WeightedGraph
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
    graphs: tuple[GraphEntry, ...]
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
    return {
        (entry.morphisms.source, entry.morphisms.target): tuple(
            (morphism.matrix, morphism.scale) for morphism in entry.morphisms.morphisms
        )
        for entry in corpus.morphisms
    }


class CorpusInvalid(Exception):
    """Raised with every problem of the corpus, one line each."""

    def __init__(self, problems: tuple[str, ...]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


def _record_problems(path: Path, error: ValidationError) -> list[str]:
    return [
        f"{path}: {'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]"
        for problem in error.errors()
    ]


def _catalogue[Value: CatalogueRecord](
    root: Path, directory: str, schema: type[Value], found: list[str]
) -> tuple[CatalogueEntry[Value], ...]:
    """Every record of `root/directory` that has the shape of `schema`."""
    entries: list[CatalogueEntry[Value]] = []
    for path in sorted((root / directory).glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            value = schema.model_validate(document.metadata)
        except ValidationError as error:
            found.extend(_record_problems(path, error))
            continue
        entries.append(CatalogueEntry(value, document.content, path))
    return tuple(entries)


def load(root: Path) -> Corpus:
    """The families, the retired tags, every entry of `root/lattices` in tag order, and every file of `root/morphisms`.

    Raises `CorpusInvalid` with all problems when a file does not have the shape of its schema.
    """
    entries: list[Entry] = []
    found: list[str] = []
    families: Families = {}
    retired: Retired = {}
    families_path = root / FAMILIES_FILE
    retired_path = root / RETIRED_FILE
    # Pydantic reports the problems of a value only through this exception.
    try:
        families = TypeAdapter(Families).validate_python(
            yaml.safe_load(families_path.read_text())
        )
    except ValidationError as error:
        found.extend(_record_problems(families_path, error))
    try:
        retired = TypeAdapter(Retired).validate_python(
            yaml.safe_load(retired_path.read_text()) or {}
        )
    except ValidationError as error:
        found.extend(_record_problems(retired_path, error))
    directory = root / "lattices"
    paths = sorted(directory.glob("*.md"))
    if not paths:
        found.append(f"{directory}: no records")
    for path in paths:
        document = frontmatter.load(str(path))
        try:
            lattice = Lattice.model_validate(document.metadata)
            entries.append(Entry(lattice, document.content, path))
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    morphisms: list[MorphismEntry] = []
    for path in sorted((root / "morphisms").glob("*.md")):
        document = frontmatter.load(str(path))
        # Pydantic reports the problems of a morphism file only through this exception.
        try:
            morphisms.append(
                MorphismEntry(
                    Morphisms.model_validate(document.metadata), document.content, path
                )
            )
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    geometric: list[GeometricEntry] = []
    geometric_adapter = TypeAdapter(GeometricObject)
    for path in sorted((root / "geometric-objects").glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            geometric.append(
                GeometricEntry(
                    geometric_adapter.validate_python(document.metadata),
                    document.content,
                    path,
                )
            )
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    geometric_families: list[GeometricFamilyEntry] = []
    for path in sorted((root / "geometric-families").glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            geometric_families.append(
                GeometricFamilyEntry(
                    GeometricFamily.model_validate(document.metadata),
                    document.content,
                    path,
                )
            )
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    graphs: list[GraphEntry] = []
    for path in sorted((root / "graphs").glob("*.md")):
        document = frontmatter.load(str(path))
        try:
            graphs.append(
                GraphEntry(
                    WeightedGraph.model_validate(document.metadata),
                    document.content,
                    path,
                )
            )
        except ValidationError as error:
            found.extend(_record_problems(path, error))
    loaded = Corpus(
        tuple(entries),
        families,
        retired,
        tuple(morphisms),
        tuple(geometric),
        tuple(geometric_families),
        tuple(graphs),
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
    if found:
        raise CorpusInvalid(tuple(found))
    return loaded


def next_tag(root: Path) -> str:
    """The tag after the greatest card filename or retired tag."""
    value = 0
    tags = [path.stem for path in (root / "lattices").glob("*.md")]
    retired = yaml.safe_load((root / RETIRED_FILE).read_text()) or {}
    for character in max([*tags, *retired], default="0000"):
        value = value * len(TAG_ALPHABET) + TAG_ALPHABET.index(character)
    value += 1
    digits = []
    for _ in range(4):
        value, digit = divmod(value, len(TAG_ALPHABET))
        digits.append(TAG_ALPHABET[digit])
    assert value == 0, "the four-character tag space is full"
    return "".join(reversed(digits))
