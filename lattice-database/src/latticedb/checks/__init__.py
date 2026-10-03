"""Read-only verification of authored and seeded lattice cards.

`corpus.load` reads each file and checks that it has the shape of its schema.
Every question that needs two records, or a record and the family, the retired
tags, the catalogues or an archived source that it names, is asked here and
reported as a line of text. Nothing in this package writes.
"""

from pathlib import Path

from latticedb import corpus
from latticedb.checks import catalogues, records, relations, sources


def run(root: Path) -> tuple[int, list[str]]:
    """Run independent card, relation, catalogue and source checks without changing cards."""
    loaded = corpus.load(root)
    problems = [
        *records.problems(loaded),
        *relations.problems(loaded, root),
        *catalogues.problems(loaded),
        *sources.problems(root, loaded),
    ]
    return len(loaded.entries), problems


def report(root: Path) -> tuple[str, ...]:
    """Every problem of the corpus under `root`, one line each."""
    return tuple(run(root)[1])
