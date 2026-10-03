"""Seed permanent Markdown cards from the published source-row index."""

import gzip
import json
from collections.abc import Iterator
from pathlib import Path

import frontmatter
import yaml

from latticedb.corpus import TAG_ALPHABET
from latticedb.model import Yaml

SOURCES = ("nipp", "brandt_intrau", "watson", "nebe_sloane")


def rows(root: Path) -> Iterator[dict[str, Yaml]]:
    """Read source rows in a fixed order from the stored index."""
    for source in SOURCES:
        with gzip.open(root / "sources" / "normalized" / f"{source}.jsonl.gz", "rt") as stream:
            for line in stream:
                row = json.loads(line)
                assert isinstance(row, dict) and row.get("source") == source and isinstance(row.get("id"), str)
                yield row


def _number(tag: str) -> int:
    value = 0
    for character in tag:
        value = value * len(TAG_ALPHABET) + TAG_ALPHABET.index(character)
    return value


def _tag(value: int) -> str:
    digits = []
    for _ in range(4):
        value, digit = divmod(value, len(TAG_ALPHABET))
        digits.append(TAG_ALPHABET[digit])
    assert value == 0, "the four-character tag space is full"
    return "".join(reversed(digits))


def _existing(directory: Path) -> dict[tuple[str, str], str]:
    cards: dict[tuple[str, str], str] = {}
    for path in sorted(directory.glob("*.md")):
        document = frontmatter.load(str(path))
        key = (document["source"], document["id"])
        assert key not in cards, f"repeated source item {key}"
        assert document["tag"] == path.stem, f"tag and path differ: {path}"
        cards[key] = path.stem
    return cards


def seed(root: Path) -> int:
    """Give each source item one stable tag and a Markdown home."""
    directory = root / "lattices" / "source"
    directory.mkdir(parents=True, exist_ok=True)
    existing = _existing(directory)
    occupied = {_number(path.stem) for path in (root / "lattices").glob("*.md")}
    occupied.update(_number(tag) for tag in existing.values())
    retired = yaml.safe_load((root / "retired-tags.yaml").read_text()) or {}
    occupied.update(_number(tag) for tag in retired)
    next_number = max(occupied) + 1
    seen: set[tuple[str, str]] = set()
    written = 0
    for row in rows(root):
        source, source_id = row["source"], row["id"]
        assert isinstance(source, str) and isinstance(source_id, str)
        key = (source, source_id)
        assert key not in seen, f"repeated source item {key}"
        seen.add(key)
        if key in existing:
            continue
        tag = _tag(next_number)
        next_number += 1
        card = {"tag": tag, "kind": "source", "name": row.get("name", f"{source} {source_id}"), **row}
        (directory / f"{tag}.md").write_text("---\n" + yaml.safe_dump(card, sort_keys=False, allow_unicode=True, width=100000) + "---\n\n")
        written += 1
    assert set(existing) <= seen, "a stored source card is absent from the source index"
    return written
