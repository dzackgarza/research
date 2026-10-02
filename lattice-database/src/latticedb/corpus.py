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
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb.arithmetic import GramTensor
from latticedb.geometric import GeometricObject
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
class Corpus:
    entries: tuple[Entry, ...]
    families: Families
    retired: Retired
    morphisms: tuple[MorphismEntry, ...]
    geometric: tuple[GeometricEntry, ...]


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
    if not paths:
        found.append(f"{directory}: no records")
    for path in paths:
        document = frontmatter.load(str(path))
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
    seen_slugs: set[str] = set()
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    for entry in geometric:
        record = entry.geometric
        if entry.path.stem != record.slug or record.slug in seen_slugs:
            found.append(f"{entry.path}: geometric object slug must be unique and match its file name")
        seen_slugs.add(record.slug)
        for link in record.cohomology_lattices:
            lattice = by_tag.get(link.tag)
            if lattice is None:
                found.append(f"{entry.path}: cohomology lattice tag {link.tag} is not in the corpus")
            elif lattice.rank != record.betti_number(link.degree):
                found.append(f"{entry.path}: H^{link.degree} has Betti number {record.betti_number(link.degree)}, but lattice {link.tag} has rank {lattice.rank}")
    if found:
        raise CorpusInvalid(tuple(found))
    return Corpus(tuple(entries), families, retired, tuple(morphisms), tuple(geometric))


def next_tag(corpus: Corpus) -> str:
    """The tag after the greatest tag of the corpus, retired tags counted, in the order 0-9 then A-Z."""
    value = 0
    for character in max(*(entry.lattice.tag for entry in corpus.entries), *corpus.retired):
        value = value * len(TAG_ALPHABET) + TAG_ALPHABET.index(character)
    value += 1
    digits = []
    for _ in range(4):
        value, digit = divmod(value, len(TAG_ALPHABET))
        digits.append(TAG_ALPHABET[digit])
    assert value == 0, "the four-character tag space is full"
    return "".join(reversed(digits))
