"""Read-only verification of authored and seeded lattice cards."""

from pathlib import Path

from latticedb import corpus
from latticedb.checks import records, relations, sources


def run(root: Path) -> tuple[int, list[str]]:
    """Run independent card, relation, and source checks without changing cards."""
    loaded = corpus.load(root, verify=False)
    problems = [*records.problems(loaded), *relations.problems(loaded), *sources.problems(root, loaded)]
    return len(loaded.entries), problems
