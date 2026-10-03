"""Reproducible source-row index for the published bulk lattice tables."""

import gzip
import io
import json
from collections.abc import Iterable
from pathlib import Path

from flint import fmpz_mat

from latticedb import brandt_intrau, nipp, watson
from latticedb.model import Yaml


def _determinant(gram: tuple[tuple[int, ...], ...]) -> int:
    return int(fmpz_mat(gram).det())


def _write(path: Path, rows: Iterable[dict[str, Yaml]]) -> int:
    output = io.BytesIO()
    count = 0
    with gzip.GzipFile(fileobj=output, mode="wb", filename="", mtime=0) as compressed:
        for row in rows:
            compressed.write((json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode())
            count += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(output.getvalue())
    return count


def _nipp_rows(directory: Path) -> Iterable[dict[str, Yaml]]:
    for entry in nipp.stored(directory):
        yield {
            "source": "nipp",
            "id": f"{entry.source_file}:{entry.source_line}",
            "source_file": entry.source_file,
            "source_line": entry.source_line,
            "rank": entry.rank,
            "gram_tensor": [list(row) for row in entry.gram_tensor],
            "determinant": _determinant(entry.gram_tensor),
            "discriminant": entry.discriminant,
            "genus": entry.genus,
            "hasse_symbols": list(entry.hasse_symbols),
            "level": entry.level,
            "automorphism_group_order": entry.automorphism_group_order,
            "mass": str(entry.mass),
        }


def _brandt_intrau_rows(directory: Path) -> Iterable[dict[str, Yaml]]:
    for entry in brandt_intrau.stored(directory):
        yield {
            "source": "brandt_intrau",
            "id": f"{entry.source_file}:{entry.source_number}",
            "source_file": entry.source_file,
            "source_line": entry.source_line,
            "source_number": entry.source_number,
            "rank": 3,
            "gram_tensor": [list(row) for row in entry.gram_tensor],
            "determinant": _determinant(entry.gram_tensor),
            "discriminant": entry.discriminant,
            "coefficients": list(entry.coefficients),
            "odd_form": entry.odd_form,
        }


def _watson_rows(path: Path) -> Iterable[dict[str, Yaml]]:
    for entry in watson.stored(path):
        yield {
            "source": "watson",
            "id": f"{entry.dimension}:{entry.ordinal}",
            "source_line": entry.source_line,
            "rank": entry.dimension,
            "gram_tensor": [list(row) for row in entry.gram_tensor],
            "determinant": _determinant(entry.gram_tensor),
            "genus_class_count": 1,
        }


def write(root: Path) -> dict[str, int]:
    """Store every parsed source form and its exact Gram determinant."""
    sources = root / "sources"
    target = sources / "normalized"
    return {
        "nipp": _write(target / "nipp.jsonl.gz", _nipp_rows(sources / "nipp")),
        "brandt_intrau": _write(target / "brandt_intrau.jsonl.gz", _brandt_intrau_rows(sources / "brandt_intrau")),
        "watson": _write(target / "watson.jsonl.gz", _watson_rows(sources / "watson" / "watson.txt")),
    }
