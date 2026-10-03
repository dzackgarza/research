"""Convert stored source rows into permanent lattice Markdown cards."""

from pathlib import Path

import frontmatter

from latticedb import records
from latticedb.model import Yaml


def _reference(source: str, source_id: str, row: dict[str, Yaml]) -> dict[str, Yaml]:
    if source == "nipp":
        file = row["source_file"]
        return {
            "citation": f"G. Nipp, Tables of Quaternary and Quinary Quadratic Forms, {source_id}.",
            "url": f"https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/{file}",
        }
    if source == "brandt_intrau":
        file = row["source_file"]
        return {
            "citation": f"Brandt–Intrau–Schiemann ternary form table, {source_id}.",
            "url": f"https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/{file}",
        }
    if source == "watson":
        return {
            "citation": f"Watson, primitive lattices of class number one, {source_id}.",
            "url": "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson",
        }
    raise ValueError(f"source {source} has no lattice citation")


def card(row: dict[str, Yaml]) -> tuple[dict[str, Yaml], str]:
    """Use a source's defining Gram tensor and identity without deriving invariants."""
    source = row["source"]
    source_id = row["id"]
    if not isinstance(source, str) or not isinstance(source_id, str):
        raise ValueError("a source row needs a source and identifier")
    gram = row.get("gram_tensor")
    rank = row.get("rank")
    determinant = row.get("determinant")
    if not isinstance(gram, list) or not isinstance(rank, int) or not isinstance(determinant, int):
        raise ValueError(f"{source}:{source_id} has no indexed Gram tensor, rank, and determinant")
    name = f"{source} {source_id}"
    fields: dict[str, Yaml] = {
        "tag": row["tag"],
        "name": name,
        "latex": name,
        "aliases": [],
        "rank": rank,
        "gram_tensor": gram,
        "signature": [rank, 0],
        "determinant": determinant,
        "definiteness": "positive_definite",
        "families": [],
        "related": [],
        "references": [_reference(source, source_id, row)],
    }
    prose = f"Source entry `{source}:{source_id}` gives this Gram tensor."
    return fields, prose


def run(root: Path, limit: int | None = None) -> tuple[int, tuple[str, ...]]:
    """Move every source form with an indexed Gram tensor into `lattices/<TAG>.md`."""
    source_directory = root / "lattices" / "source"
    paths = sorted(source_directory.glob("*.md"))
    if limit is not None:
        paths = paths[:limit]
    seeded = 0
    missing: list[str] = []
    for path in paths:
        document = frontmatter.load(str(path))
        row = dict(document.metadata)
        try:
            fields, prose = card(row)
        except ValueError:
            missing.append(f"{row.get('source')}:{row.get('id')}")
            continue
        destination = root / "lattices" / f"{path.stem}.md"
        if path != destination:
            if destination.exists():
                raise FileExistsError(destination)
            path.rename(destination)
        destination.write_text(records.record_text(fields, prose))
        seeded += 1
    return seeded, tuple(missing)
