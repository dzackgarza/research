"""The corpus: every `lattices/<TAG>.md` and the families of `families.yaml`, read and validated as one database.

A file is YAML front matter, which holds the record of one lattice, and then
prose in Markdown. `load` validates each record by itself and then checks the
statements that concern more than one record, or a record and the families,
and that no two definite records are the same lattice in different bases.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb import arithmetic
from latticedb.arithmetic import GramTensor
from latticedb.model import AdeType, Definiteness, Family, Lattice

TAG_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Families = dict[Family, str]
"""Each family that a record may name, with one line of its meaning."""

FAMILIES_FILE = "families.yaml"


@dataclass(frozen=True)
class Entry:
    lattice: Lattice
    prose: str
    path: Path


@dataclass(frozen=True)
class Corpus:
    entries: tuple[Entry, ...]
    families: Families


class CorpusInvalid(Exception):
    """Raised with every problem of the corpus, one line each."""

    def __init__(self, problems: tuple[str, ...]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


IsometryInvariants = tuple[int, Definiteness, Fraction, Fraction, int, tuple[AdeType, ...] | None, tuple[int, ...] | None, tuple[int, ...] | None]
"""Rank, definiteness, determinant, minimum, kissing number, root system, theta series and discriminant group: invariants of the isometry class that a record states, and that the build has checked."""


def _isometry_invariants(lattice: Lattice) -> IsometryInvariants:
    definite = lattice.definite
    assert definite is not None, "only a definite record is compared by isometry class"
    integral = lattice.integral
    discriminant_group = None if integral is None else integral.discriminant_group
    return (lattice.rank, lattice.definiteness, lattice.determinant, definite.minimum, definite.kissing_number, definite.root_system, definite.theta_series, discriminant_group)


def _isometric_pairs(entries: list[Entry]) -> list[tuple[Entry, Entry]]:
    """Each pair of definite records that are isometric, decided by `qfisom` on the pairs whose stated invariants agree.

    Whether two indefinite lattices are isometric is not decided here: `qfisom`
    decides it for definite forms only, and the corpus states no invariant that
    would decide it for the others.
    """
    by_invariants: dict[IsometryInvariants, list[Entry]] = {}
    for entry in entries:
        if entry.lattice.definite is not None:
            by_invariants.setdefault(_isometry_invariants(entry.lattice), []).append(entry)
    return [
        (first, second)
        for group in by_invariants.values()
        for first, second in combinations(group, 2)
        # A pair with the same components is reported as such.
        if first.lattice.gram_tensor != second.lattice.gram_tensor and arithmetic.is_isometric(first.lattice.gram_tensor, second.lattice.gram_tensor)
    ]


def problems(entries: list[Entry], families: Families) -> list[str]:
    """The problems that concern more than one record or the families: a file name that is not its tag, a repeated name or Gram tensor, two definite records that are isometric, a family that `families.yaml` does not list, a related or summand tag that is not in the corpus, and an embedding whose Gram tensor is not that of its summands."""
    found = []
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    by_name: dict[str, Path] = {}
    by_components: dict[GramTensor, Path] = {}
    for entry in entries:
        lattice = entry.lattice
        if entry.path.stem != lattice.tag:
            found.append(f"{entry.path}: the file name must be the tag {lattice.tag}")
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
        if span is not None and span.summands is not None and span.embedding is not None:
            missing = [tag for tag in span.summands if tag not in by_tag]
            found.extend(f"{entry.path}: the summand tag {tag} is not in the corpus" for tag in missing)
            summands = tuple(by_tag[tag].gram_tensor for tag in span.summands if tag in by_tag)
            if not missing and arithmetic.restriction(lattice.gram_tensor, span.embedding) != arithmetic.orthogonal_sum(summands):
                found.append(f"{entry.path}: the rows of root_span.embedding do not have the Gram tensor of the orthogonal sum of the summands")
    found.extend(f"{second.path}: the lattice is isometric to {first.path} ({first.lattice.name}), in another basis" for first, second in _isometric_pairs(entries))
    return found


def _record_problems(path: Path, error: ValidationError) -> list[str]:
    return [f"{path}: {'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]" for problem in error.errors()]


def load(root: Path) -> Corpus:
    """The families of `root/families.yaml` and every entry of `root/lattices`, in tag order. Raises `CorpusInvalid` with all problems when a record or the corpus is not well defined."""
    entries: list[Entry] = []
    found: list[str] = []
    families: Families = {}
    families_path = root / FAMILIES_FILE
    # Pydantic reports the problems of a value only through this exception.
    try:
        families = TypeAdapter(Families).validate_python(yaml.safe_load(families_path.read_text()))
    except ValidationError as error:
        found.extend(_record_problems(families_path, error))
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
    found.extend(problems(entries, families))
    if found:
        raise CorpusInvalid(tuple(found))
    return Corpus(tuple(entries), families)


def next_tag(entries: tuple[Entry, ...]) -> str:
    """The tag after the greatest tag of the corpus, in the order 0-9 then A-Z."""
    value = 0
    for character in max(entry.lattice.tag for entry in entries):
        value = value * len(TAG_ALPHABET) + TAG_ALPHABET.index(character)
    value += 1
    digits = []
    for _ in range(4):
        value, digit = divmod(value, len(TAG_ALPHABET))
        digits.append(TAG_ALPHABET[digit])
    assert value == 0, "the four-character tag space is full"
    return "".join(reversed(digits))
