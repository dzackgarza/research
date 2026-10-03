"""Compare archived source claims with their cited lattice cards."""

from pathlib import Path

from latticedb import hashimoto, hoehn_mason, nebe_sloane
from latticedb.corpus import Corpus


def problems(root: Path, loaded: Corpus) -> list[str]:
    found: list[str] = []
    for source, check in (
        ("hashimoto", hashimoto.stored_problems),
        ("hoehn_mason", hoehn_mason.stored_problems),
        ("nebe_sloane_archive", nebe_sloane.stored_problems),
    ):
        found.extend(f"{source}: {problem}" for problem in check(root, loaded))
    return found
