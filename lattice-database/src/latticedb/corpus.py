"""The corpus: every `lattices/<TAG>.md` and the families of `families.yaml`, read as one database.

A file is YAML front matter, which holds the record of one lattice, and then
prose in Markdown. `load` reads the stored values and checks only that each
file has the shape of its schema. The references between records, families,
retired tags, catalogues and file names are checked by the read-only
verification in `latticedb.checks`, never while reading.

A tag is permanent. `retired-tags.yaml` lists each tag whose record the corpus
no longer admits, with the lattice that was there and why it is not a record;
no record takes a retired tag, and `next_tag` counts them.

Each lattice card owns the stored morphisms whose domain is that lattice. Each
morphism names its codomain lattice by tag; incoming morphisms are derived by indexing
the cards.
"""

from dataclasses import dataclass
import json
import re
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb.catalogues import (
    ArithmeticGroup,
    CatalogueRecord,
    GeometricMap,
    IntegralLocalSystem,
    LatticeFamily,
    LatticeGenus,
    LatticePolytope,
    LieGroup,
    ModuliProblem,
    PicardFuchsOperator,
    ToricVariety,
)
from latticedb.model import GramTensor
from latticedb.geometric import GeometricFamily, GeometricObject
from latticedb.graphs import WeightedGraph
from latticedb.model import Family, Lattice, Tag, Yaml

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
    geometric: tuple[GeometricEntry, ...]
    geometric_families: tuple[GeometricFamilyEntry, ...]
    graphs: tuple[GraphEntry, ...]
    genera: tuple[CatalogueEntry[LatticeGenus], ...]
    polytopes: tuple[CatalogueEntry[LatticePolytope], ...]
    toric_varieties: tuple[CatalogueEntry[ToricVariety], ...]
    geometric_maps: tuple[CatalogueEntry[GeometricMap], ...]
    local_systems: tuple[CatalogueEntry[IntegralLocalSystem], ...]
    operators: tuple[CatalogueEntry[PicardFuchsOperator], ...]
    moduli_problems: tuple[CatalogueEntry[ModuliProblem], ...]
    lattice_families: tuple[CatalogueEntry[LatticeFamily], ...]
    lie_groups: tuple[CatalogueEntry[LieGroup], ...]
    arithmetic_groups: tuple[CatalogueEntry[ArithmeticGroup], ...]


Matrix = tuple[tuple[int, ...], ...]
Held = dict[tuple[Tag, Tag], tuple[tuple[Matrix, int], ...]]
"""For each source/target pair, the matrix and scale of each stored morphism."""


def held(corpus: Corpus) -> Held:
    """The matrices and scales of the lattice-card morphisms of `corpus`."""
    grouped: dict[tuple[Tag, Tag], list[tuple[Matrix, int]]] = {}
    for entry in corpus.entries:
        for morphism in entry.lattice.morphisms:
            grouped.setdefault((entry.lattice.tag, morphism.target), []).append(
                (morphism.matrix, morphism.scale)
            )
    return {pair: tuple(values) for pair, values in grouped.items()}


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
        tuple(geometric),
        tuple(geometric_families),
        tuple(graphs),
        _catalogue(root, "genera", LatticeGenus, found),
        _catalogue(root, "lattice-polytopes", LatticePolytope, found),
        _catalogue(root, "toric-varieties", ToricVariety, found),
        _catalogue(root, "geometric-maps", GeometricMap, found),
        _catalogue(root, "integral-local-systems", IntegralLocalSystem, found),
        _catalogue(root, "picard-fuchs-operators", PicardFuchsOperator, found),
        _catalogue(root, "moduli-problems", ModuliProblem, found),
        _catalogue(root, "lattice-families", LatticeFamily, found),
        _catalogue(root, "lie-groups", LieGroup, found),
        _catalogue(root, "arithmetic-groups", ArithmeticGroup, found),
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


def duplicate_grams(entries: tuple[Entry, ...]) -> dict[GramTensor, list[str]]:
    """Each Gram tensor held by more than one record, with its tags in corpus order.

    The tensor is already canonical — every component a `Fraction` — so
    dictionary equality is Gram equality. Records without a Gram tensor
    (sparse cards) are skipped.
    """
    tags: dict[GramTensor, list[str]] = {}
    for entry in entries:
        gram = entry.lattice.gram_tensor
        if gram is not None:
            tags.setdefault(gram, []).append(entry.lattice.tag)
    return {gram: found for gram, found in tags.items() if len(found) > 1}


_GRAM_HEAD = re.compile(r"^gram_tensor:\s*$")
_GRAM_ROW = re.compile(r"^\s*-\s*\[(.*)\]\s*$")
_GRAM_TOKEN = re.compile(r"\"([^\"]+)\"|(-?\d+(?:/\d+)?)")


def _stated_gram(path: Path) -> GramTensor | None:
    """The Gram tensor stated by a card, read as text; `None` when absent.

    Only the `gram_tensor` block is read — the file is never parsed as YAML,
    so shells of minimal vectors and other large fields cost nothing. Each row
    is one `- [...]` line of integers or `p/q` strings, as `record_text`
    writes them; anything else falls back to the record reader.
    """
    from latticedb import records

    rows: list[list[int | str]] = []
    started = False
    with path.open() as handle:
        for line in handle:
            if not started:
                if _GRAM_HEAD.match(line):
                    started = True
                continue
            match = _GRAM_ROW.match(line)
            if match is None:
                break
            tokens = _GRAM_TOKEN.findall(match.group(1))
            covered = "".join(first or second for first, second in tokens)
            if covered != re.sub(r"[\s,]", "", match.group(1)) or not tokens:
                return records.gram_tensor(
                    frontmatter.load(str(path)).metadata.get("gram_tensor")
                )
            rows.append(
                [
                    int(token) if "/" not in token else token
                    for token in (first or second for first, second in tokens)
                ]
            )
    if not started or not rows or any(len(row) != len(rows) for row in rows):
        return None
    return records.gram_tensor(rows)


GRAM_INDEX_FILE = "gram-index.json"
"""Each Gram tensor stated by a card, keyed canonically, with the tags stating it."""


def gram_key(gram: GramTensor) -> str:
    """The canonical string of a Gram tensor: each component as `n` or `p/q`."""
    return ";".join(",".join(str(value) for value in row) for row in gram)


def _read_index(root: Path) -> dict[str, list[str]] | None:
    """The stored index, or `None` when it is missing or malformed.

    The file holds two maps: `grams`, Gram key -> tags stating it, and
    `without`, the tags of cards stating no Gram tensor (sparse cards).
    """
    path = root / GRAM_INDEX_FILE
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except ValueError:
        return None
    if (
        not isinstance(data, dict)
        or not isinstance(data.get("grams"), dict)
        or not isinstance(data.get("without"), list)
        or any(
            not isinstance(key, str)
            or not isinstance(tags, list)
            or any(not isinstance(tag, str) for tag in tags)
            for key, tags in data["grams"].items()
        )
        or any(not isinstance(tag, str) for tag in data["without"])
    ):
        return None
    return data


def save_index(root: Path, index: dict[str, list[str]]) -> None:
    """Write the index file."""
    (root / GRAM_INDEX_FILE).write_text(json.dumps(index, separators=(",", ":")))


def append_index(root: Path, tag: str, gram: GramTensor) -> None:
    """Record a newly written card in the index file."""
    data = _read_index(root)
    if data is None:
        gram_index(root)
        data = _read_index(root)
        assert data is not None
    data["grams"].setdefault(gram_key(gram), []).append(tag)
    save_index(root, data)


def gram_index(root: Path) -> dict[str, list[str]]:
    """Gram key -> tags stating it, from the durable index file.

    The file is built once by scanning the cards. A load re-reads only the
    gram-less cards (tens of files); a card that gained a Gram tensor since
    promotes into the map. Any other change of the card set rebuilds it.
    Each lookup and each append is O(1) in the corpus.
    """
    paths = {path.stem: path for path in (root / "lattices").glob("*.md")}
    data = _read_index(root)
    if data is not None and (
        {tag for tags in data["grams"].values() for tag in tags}
        | set(data["without"])
    ) == set(paths):
        changed = False
        for tag in list(data["without"]):
            gram = _stated_gram(paths[tag])
            if gram is not None:
                data["grams"].setdefault(gram_key(gram), []).append(tag)
                data["without"].remove(tag)
                changed = True
        if changed:
            save_index(root, data)
        return data["grams"]
    grams: dict[str, list[str]] = {}
    without: list[str] = []
    for stem in sorted(paths):
        gram = _stated_gram(paths[stem])
        if gram is None:
            without.append(stem)
        else:
            grams.setdefault(gram_key(gram), []).append(stem)
    data = {"grams": grams, "without": without}
    save_index(root, data)
    return grams
