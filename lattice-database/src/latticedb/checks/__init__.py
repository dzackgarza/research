"""Read-only mathematical verification of authored and seeded lattice cards.

`corpus.load` reads each file and checks that it has the shape of its schema.
Every question that needs two records, or a record and the family, the retired
tags or the catalogues is asked here and reported as a line of text. Archived
intake sources are provenance for how cards were seeded; they are not
mathematical oracles for verification. Nothing in this package writes.
"""

from pathlib import Path

from latticedb import certificates, corpus
from latticedb.checks import catalogues, records, relations


def run(root: Path) -> tuple[int, list[str]]:
    """Run mathematical card, relation and catalogue checks without changing cards."""
    loaded = corpus.load(root)
    held = certificates.load(root)
    problems = [
        *records.problems(loaded, held),
        *relations.problems(loaded, root),
        *catalogues.problems(loaded),
    ]
    return len(loaded.entries), problems


def report(root: Path) -> tuple[str, ...]:
    """Every problem of the corpus under `root`, one line each."""
    return tuple(run(root)[1])
