"""Convert stored source rows into permanent lattice Markdown cards."""

from pathlib import Path

import frontmatter

from latticedb import corpus, nebe_sloane, records
from latticedb.model import Yaml

_IDENTITY = ("tag", "name", "latex", "aliases", "certifications")
_GATHERED = ("families", "related", "references")


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
    if source == "nebe_sloane":
        return {
            "citation": f"G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry {source_id}.",
            "url": nebe_sloane.ARCHIVE,
        }
    raise ValueError(f"source {source} has no lattice citation")


def _archive_card(row: dict[str, Yaml], source_id: str) -> tuple[dict[str, Yaml], str]:
    sections = row["sections"]
    if not isinstance(sections, dict):
        raise ValueError(f"{source_id} has no archive sections")
    title = str(row["name"])
    name = f"{title} ({source_id})"
    fields: dict[str, Yaml] = {
        "tag": row["tag"],
        "name": name,
        "latex": title,
        "aliases": [title],
        "families": [],
        "related": [],
        "references": [_reference("nebe_sloane", source_id, row)],
    }
    dimension = sections.get("DIMENSION") or sections.get("DIM")
    if isinstance(dimension, list) and dimension and isinstance(dimension[0], str) and dimension[0].isdecimal():
        fields["rank"] = int(dimension[0])
    stated_determinant = sections.get("DET") or sections.get("DETERMINANT")
    if isinstance(stated_determinant, list) and stated_determinant and isinstance(stated_determinant[0], str):
        try:
            fields["determinant"] = nebe_sloane.determinant(stated_determinant[0])
        except ArithmeticError, AssertionError, ValueError:
            pass
    gram = sections.get("GRAM_MATRIX") or sections.get("GRAM")
    if isinstance(gram, list) and gram:
        try:
            matrix = nebe_sloane.maple_components(gram, int(fields["rank"])) if "GRAM_MATRIX" in sections else nebe_sloane.components(gram)
            fields["gram_tensor"] = [list(line) for line in matrix]
        except ArithmeticError, AssertionError, KeyError, ValueError, IndexError, SyntaxError:
            pass
    prose = f"Catalogue of Lattices archive entry `{source_id}` names `{title}`."
    notes = sections.get("NOTES")
    if isinstance(notes, list) and notes:
        prose += "\n\n" + " ".join(str(line) for line in notes)
    return fields, prose


def card(row: dict[str, Yaml]) -> tuple[dict[str, Yaml], str]:
    """Use only fields explicitly carried by the normalized source row."""
    source = row["source"]
    source_id = row["id"]
    if not isinstance(source, str) or not isinstance(source_id, str):
        raise ValueError("a source row needs a source and identifier")
    if source == "nebe_sloane":
        return _archive_card(row, source_id)
    gram = row.get("gram_tensor")
    rank = row.get("rank")
    if not isinstance(gram, list) or not isinstance(rank, int):
        raise ValueError(f"{source}:{source_id} has no indexed Gram tensor and rank")
    name = f"{source} {source_id}"
    fields: dict[str, Yaml] = {
        "tag": row["tag"],
        "name": name,
        "latex": name,
        "aliases": [],
        "rank": rank,
        "gram_tensor": gram,
        "families": [],
        "related": [],
        "references": [_reference(source, source_id, row)],
    }
    if isinstance(row.get("determinant"), int):
        fields["determinant"] = row["determinant"]
    prose = f"Source entry `{source}:{source_id}` gives this Gram tensor."
    return fields, prose


def attach(path: Path, fields: dict[str, Yaml], prose: str) -> None:
    """Add a second statement of the lattice of the card at `path` to that card.

    The statement's references, families, related lattices and prose join the
    card. Every other field it states must agree with the card's value, which a
    field the card lacks takes. Its name, TeX name and aliases stay out of the
    card: a source's name for an entry is not always a name of the lattice the
    entry's Gram tensor states, and the prose records it.
    """
    document = frontmatter.load(str(path))
    held = corpus.front_matter(document)
    for key, value in fields.items():
        if key in _IDENTITY:
            continue
        if key in _GATHERED:
            assert isinstance(value, list)
            present = held.get(key)
            gathered = list(present) if isinstance(present, list) else []
            gathered.extend(item for item in value if item not in gathered)
            held[key] = gathered
            continue
        if isinstance(value, dict):
            block = held.get(key)
            merged = dict(block) if isinstance(block, dict) else {}
            for field, field_value in value.items():
                assert merged.get(field) in (None, field_value), f"{path}: {key}.{field} is {merged[field]}, the second statement {field_value}"
                merged[field] = field_value
            held[key] = merged
            continue
        assert held.get(key) in (None, value), f"{path}: {key} is {held[key]}, the second statement {value}"
        held[key] = value
    text = document.content.strip()
    path.write_text(records.record_text(held, text if prose in text else f"{text}\n\n{prose}".strip()))


def run(root: Path, limit: int | None = None) -> tuple[int, int, tuple[str, ...]]:
    """Move source entries into their permanent `lattices/<TAG>.md` cards.

    An entry whose Gram tensor a card already states joins that card; it
    writes no second card.
    """
    source_directory = root / "lattices" / "source"
    paths = sorted(source_directory.glob("*.md"))
    if limit is not None:
        paths = paths[:limit]
    index = corpus.gram_index(root)
    seeded = 0
    attached = 0
    missing: list[str] = []
    for path in paths:
        document = frontmatter.load(str(path))
        row = dict(document.metadata)
        fields, prose = card(row)
        if "gram_tensor" not in fields:
            missing.append(f"{row.get('source')}:{row.get('id')}")
        else:
            gram = records.gram_tensor(fields["gram_tensor"])
            held = index.get(corpus.gram_key(gram))
            if held:
                attach(root / "lattices" / f"{held[0]}.md", fields, prose)
                path.unlink()
                attached += 1
                continue
        destination = root / "lattices" / f"{path.stem}.md"
        if path != destination:
            if destination.exists():
                raise FileExistsError(destination)
            path.rename(destination)
        destination.write_text(records.record_text(fields, prose))
        if "gram_tensor" in fields:
            corpus.append_index(root, path.stem, records.gram_tensor(fields["gram_tensor"]))
            index[corpus.gram_key(records.gram_tensor(fields["gram_tensor"]))] = [path.stem]
        seeded += 1
    return seeded, attached, tuple(missing)
