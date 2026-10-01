"""The genus symbol, the class number of the genus and the order of O(L), computed by SageMath and stored in the records.

`certify` sends the Gram tensor of each integral record with a nonzero determinant, with the values that
have no certificate for that Gram tensor, to `sage_genus.py` under `sage -python`, and stores each value as
soon as SageMath returns it: a value that the record does not hold is written into it, and a stored value
that differs from the computed one is a problem. A value that agrees with the record is certified; a value
that SageMath does not compute within the time limit is certified as not finished within it.
"""

import json
import os
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import frontmatter
from pydantic import BaseModel

from latticedb import certificates, corpus, records
from latticedb.certificates import Certificate, Certificates
from latticedb.model import DefiniteData, IntegralData, Lattice, Yaml

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
}
"""Each computed field, with the block of the record that holds it and the model of that block."""

SAGE_MODULE = Path(__file__).with_name("sage_genus.py")


def name(tag: str, field: str) -> str:
    """The name of the certificate of `field` of the record `tag`."""
    return f"{tag} {BLOCKS[field][0]}.{field}"


def _sign(lattice: Lattice) -> int:
    match lattice.definiteness:
        case "positive_definite":
            return 1
        case "negative_definite":
            return -1
        case _:
            return 0


def requests(loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...], seconds: int) -> list[dict[str, Yaml]]:
    """For each integral record with a nonzero determinant, among `tags` when it is not empty, the fields that are pending with the time limit `seconds`."""
    chosen: list[dict[str, Yaml]] = []
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.integral is None or lattice.determinant == 0 or (tags and lattice.tag not in tags):
            continue
        inputs = certificates.gram_digest(lattice)
        applicable = [field for field in BLOCKS if field != "automorphism_group_order" or lattice.definite is not None]
        fields: list[Yaml] = [field for field in applicable if certificates.is_pending(held, name(lattice.tag, field), inputs, seconds)]
        if fields:
            gram: list[Yaml] = [[int(x) for x in row] for row in lattice.gram_tensor]
            chosen.append({"tag": lattice.tag, "gram": gram, "sign": _sign(lattice), "fields": fields})
    return chosen


def computed(chosen: list[dict[str, Yaml]], seconds: int) -> Iterator[dict[str, int | str | None]]:
    """The values that SageMath computes for `chosen`, one record at a time."""
    task = json.dumps({"seconds": seconds, "lattices": chosen})
    # `sage -python` runs the first `python` on PATH, and `uv run` puts the environment of latticedb first.
    environment = {variable: value for variable, value in os.environ.items() if variable != "VIRTUAL_ENV"}
    own = str(Path(sys.prefix) / "bin")
    environment["PATH"] = os.pathsep.join(entry for entry in environment["PATH"].split(os.pathsep) if entry != own)
    command = [environment["SAGE_BIN"], "-python", str(SAGE_MODULE)]
    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, env=environment) as process:
        assert process.stdin is not None and process.stdout is not None
        process.stdin.write(task)
        process.stdin.close()
        # SageMath writes a carriage return to standard output for some lattices (for E8, record 0094), which reads as an empty line.
        yield from (json.loads(line) for line in process.stdout if line.strip())
    assert process.returncode == 0, f"{SAGE_MODULE} exited with status {process.returncode}"


def store(path: Path, values: dict[str, int | str | None]) -> dict[str, str]:
    """Write into the record at `path` each computed value that it does not hold; for each field whose stored value differs from the computed one, the problem."""
    document = frontmatter.load(str(path))
    metadata: dict[str, Yaml] = dict(document.metadata)
    found: dict[str, str] = {}
    for field, (block_name, model) in BLOCKS.items():
        value = values.get(field)
        match metadata.get(block_name):
            case dict() as block if value is not None:
                stored = block.get(field)
                if stored is None:
                    block[field] = value
                    metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
                elif stored != value:
                    found[field] = f"{path}: {block_name}.{field} is {stored}, and SageMath computes {value}"
    text = records.record_text(metadata, document.content)
    if text != path.read_text():
        path.write_text(text)
    return found


def certify(root: Path, loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...], seconds: int) -> Iterator[str]:
    """Compute the pending values, store them, and write their certificates after each record; yield each problem."""
    by_tag = {entry.lattice.tag: entry for entry in loaded.entries}
    for values in computed(requests(loaded, held, tags, seconds), seconds):
        entry = by_tag[str(values["tag"])]
        inputs = certificates.gram_digest(entry.lattice)
        found = store(entry.path, values)
        for field in BLOCKS:
            if field not in values or field in found:
                continue
            finished = values[field] is not None
            held[name(entry.lattice.tag, field)] = Certificate(inputs=inputs, by=str(values["by"]), seconds=None if finished else seconds)
        certificates.save(root, held)
        print(entry.lattice.tag, {field: values[field] for field in BLOCKS if field in values}, flush=True)
        yield from found.values()
