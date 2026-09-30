"""The corpus: every `lattices/<TAG>.md`, read and validated as one database.

A file is YAML front matter, which holds the record of one lattice, and then
prose in Markdown. `load` validates each record by itself and then checks the
statements that concern more than one record.
"""

from dataclasses import dataclass
from pathlib import Path

import frontmatter
from pydantic import ValidationError

from latticedb.arithmetic import GramTensor
from latticedb.model import Lattice

TAG_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@dataclass(frozen=True)
class Entry:
    lattice: Lattice
    prose: str
    path: Path


class CorpusInvalid(Exception):
    """Raised with every problem of the corpus, one line each."""

    def __init__(self, problems: tuple[str, ...]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


def _corpus_problems(entries: list[Entry]) -> list[str]:
    problems = []
    tags = {entry.lattice.tag for entry in entries}
    by_name: dict[str, Path] = {}
    by_components: dict[GramTensor, Path] = {}
    for entry in entries:
        lattice = entry.lattice
        if entry.path.stem != lattice.tag:
            problems.append(f"{entry.path}: the file name must be the tag {lattice.tag}")
        if lattice.name in by_name:
            problems.append(f"{entry.path}: the name '{lattice.name}' is also the name of {by_name[lattice.name]}")
        by_name.setdefault(lattice.name, entry.path)
        if lattice.gram_tensor in by_components:
            problems.append(f"{entry.path}: the Gram tensor has the same components as that of {by_components[lattice.gram_tensor]}")
        by_components.setdefault(lattice.gram_tensor, entry.path)
        for related in lattice.related:
            if related.tag == lattice.tag:
                problems.append(f"{entry.path}: a record cannot be related to itself")
            elif related.tag not in tags:
                problems.append(f"{entry.path}: the related tag {related.tag} is not in the corpus")
    return problems


def load(directory: Path) -> tuple[Entry, ...]:
    """Every entry of the corpus, in tag order. Raises `CorpusInvalid` with all problems when a record or the corpus is not well defined."""
    entries: list[Entry] = []
    problems: list[str] = []
    paths = sorted(directory.glob("*.md"))
    if not paths:
        problems.append(f"{directory}: no records")
    for path in paths:
        document = frontmatter.load(str(path))
        # Pydantic reports the problems of a record only through this exception.
        try:
            entries.append(Entry(Lattice.model_validate(document.metadata), document.content, path))
        except ValidationError as error:
            problems.extend(f"{path}: {'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]" for problem in error.errors())
    problems.extend(_corpus_problems(entries))
    if problems:
        raise CorpusInvalid(tuple(problems))
    return tuple(entries)


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
