"""Compare archived source claims with their cited lattice cards."""

from pathlib import Path

from latticedb import hashimoto, hoehn_mason, nebe_sloane
from latticedb.corpus import Corpus


def problems(root: Path, loaded: Corpus) -> list[str]:
    found: list[str] = []
    for source, directory, check in (
        ("hashimoto", root / "sources" / "hashimoto", hashimoto.stored_problems),
        (
            "hoehn_mason",
            root / "sources" / "hoehn_mason",
            hoehn_mason.stored_problems,
        ),
        (
            "nebe_sloane_archive",
            root / "sources" / "nebe_sloane",
            nebe_sloane.stored_problems,
        ),
    ):
        if not directory.exists():
            continue
        try:
            found.extend(f"{source}: {problem}" for problem in check(root, loaded))
        except FileNotFoundError as error:
            found.append(f"{source}: missing stored source file {error.filename}")
    return found
