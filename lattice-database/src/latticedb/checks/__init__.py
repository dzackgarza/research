"""Read-only verification of stored lattice-db claims.

`corpus.load` reads each file and checks that it has the shape of its schema.
Every question that needs two records, or a record and the family, the retired
tags or the catalogues is asked here only when it is a storage/reference question.
Mathematical validity is queried through the corresponding preamble object; no
mathematical algorithm is implemented here.
Archived intake sources are provenance for how cards were seeded. Nothing here writes.
"""

from pathlib import Path

from latticedb import certificates, corpus
from latticedb.checks import catalogues, records, relations


def run(root: Path) -> tuple[int, list[str]]:
    """Run stored-card verification without changing cards."""
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
