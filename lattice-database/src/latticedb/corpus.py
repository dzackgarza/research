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

from dataclasses import dataclass
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb.arithmetic import GramTensor
from latticedb.model import Family, Lattice, Morphisms, Tag

TAG_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
class Corpus:
    entries: tuple[Entry, ...]
    families: Families
    retired: Retired
    morphisms: tuple[MorphismEntry, ...]


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


def morphism_problems(morphisms: list[MorphismEntry], entries: list[Entry], retired: Retired) -> list[str]:
    """The problems of the morphism files.

    A file name that is not `<source>-<target>`, a tag that is not in the corpus or is retired, and two files for one pair.
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
    if found:
        raise CorpusInvalid(tuple(found))
    return Corpus(tuple(entries), families, retired, tuple(morphisms))


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
