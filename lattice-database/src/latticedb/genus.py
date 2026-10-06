"""CI serialization of lattice invariants computed by the research preamble.

`certify` sends each uncertified applicable computation to `sage_genus.py` under SageMath.
That module is a thin process/serialization boundary: every mathematical operation it
calls is owned by `dzack_research.preamble`.
A completed computation is authoritative for the part of the card that computation owns:
an authored value that disagrees is replaced by the computed value, and the resulting
card value is certified. A computation that does not finish remains uncertified.
"""

import json
import os
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import TypedDict

import frontmatter
from pydantic import BaseModel

from latticedb import certificates, corpus, records
from latticedb.certificates import Certificate, Certificates
from latticedb.model import DefiniteData, IntegralData, Lattice, Yaml

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "overlattice_count": ("integral", IntegralData),
    "spinor_genus_count": ("integral", IntegralData),
    "spinor_genera": ("integral", IntegralData),
    "hyperbolic_index": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
    "automorphism_group_generator_morphisms": ("definite", DefiniteData),
}
"""Each preamble-computed field, with the card block that stores it."""


def certified_value(field: str, value: Yaml, lattice: Lattice | None = None) -> Yaml:
    """The stored value committed to by one completed preamble computation."""
    if field == "automorphism_group_generator_morphisms":
        if lattice is None or not isinstance(value, list):
            return value
        by_name = {
            morphism.name: morphism
            for morphism in lattice.morphisms
            if morphism.target == lattice.tag and morphism.scale == 1
        }
        if any(name not in by_name for name in value):
            return value
        matrices = [
            [list(row) for row in by_name[name].matrix]
            for name in value
        ]
        return sorted(
            matrices,
            key=lambda rows: tuple(entry for row in rows for entry in row),
        )
    return value


def applies(field: str, lattice: Lattice, planes: int) -> bool:
    """Whether the preamble exposes `field` on this stored lattice."""
    del planes
    if lattice.integral is None:
        return False
    match field:
        case "automorphism_group_order" | "automorphism_group_generator_morphisms":
            return lattice.definite is not None
        case "spinor_genus_count" | "spinor_genera":
            return lattice.rank >= 3
        case _:
            return True


SAGE_MODULE = Path(__file__).with_name("sage_genus.py")


class Request(TypedDict):
    """One integral lattice and the preamble-owned fields CI asks it to compute."""

    tag: str
    gram: list[list[int]]
    fields: list[str]


def name(tag: str, field: str) -> str:
    """The name of the certificate of `field` of the record `tag`."""
    return f"{tag} {BLOCKS[field][0]}.{field}"


def requests(
    loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...], seconds: int
) -> list[Request]:
    """For each nondegenerate integral record, the uncertified preamble computations."""
    chosen: list[Request] = []
    for entry in loaded.entries:
        lattice = entry.lattice
        if (
            lattice.integral is None
            or lattice.determinant == 0
            or (tags and lattice.tag not in tags)
        ):
            continue
        applicable = [
            field
            for field in BLOCKS
            if applies(field, lattice, 0)
        ]
        metadata = corpus.front_matter(frontmatter.load(str(entry.path)))
        card_certifications = metadata.get("certifications")
        cited = card_certifications if isinstance(card_certifications, dict) else {}
        fields = []
        for field in applicable:
            block_name = BLOCKS[field][0]
            block = metadata.get(block_name)
            stored_value = block.get(field) if isinstance(block, dict) else None
            computation = name(lattice.tag, field)
            expected_hash = certificates.certification_hash(
                computation, lattice, certified_value(field, stored_value, lattice)
            )
            if stored_value is None or certificates.is_pending(
                held, computation, cited.get(f"{block_name}.{field}"), expected_hash
            ):
                fields.append(field)
        if fields:
            gram = [[int(value) for value in row] for row in lattice.gram_tensor]
            chosen.append(
                {
                    "tag": lattice.tag,
                    "gram": gram,
                    "fields": fields,
                }
            )
    return chosen


def computed(chosen: list[Request], seconds: int) -> Iterator[dict[str, Yaml]]:
    """The values that SageMath computes for `chosen`, one record at a time."""
    task = json.dumps({"seconds": seconds, "lattices": chosen})
    # Keep the host SageMath environment separate from the project environment.
    environment = {
        variable: value
        for variable, value in os.environ.items()
        if variable != "VIRTUAL_ENV"
    }
    own = str(Path(sys.prefix) / "bin")
    environment["PATH"] = os.pathsep.join(
        entry for entry in environment["PATH"].split(os.pathsep) if entry != own
    )
    command = [
        environment["SAGE_BIN"],
        "-c",
        f"import runpy; runpy.run_path({str(SAGE_MODULE)!r}, run_name='__main__')",
    ]
    with subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        env=environment,
    ) as process:
        assert process.stdin is not None and process.stdout is not None
        process.stdin.write(task)
        process.stdin.close()
        # SageMath writes a carriage return to standard output for some lattices (for E8, record 0094), which reads as an empty line.
        yield from (json.loads(line) for line in process.stdout if line.strip())
    assert process.returncode == 0, (
        f"{SAGE_MODULE} exited with status {process.returncode}"
    )


def _generator_morphisms(
    tag: str, morphisms: list[dict[str, Yaml]], matrices: list[Yaml]
) -> tuple[list[str], list[dict[str, Yaml]]]:
    """Place computed generators of O(L) on the lattice card and return their names."""
    names: list[str] = []
    used_self_names = {
        morphism["name"]
        for morphism in morphisms
        if morphism.get("target") == tag
        and morphism.get("scale", 1) == 1
        and isinstance(morphism.get("name"), str)
    }
    for index, matrix in enumerate(matrices, start=1):
        assert isinstance(matrix, list)
        existing = next(
            (
                morphism
                for morphism in morphisms
                if morphism.get("target") == tag
                and morphism["matrix"] == matrix
                and morphism.get("scale", 1) == 1
            ),
            None,
        )
        if existing is None:
            base = f"O(L) generator {index}"
            name = base
            suffix = 2
            while name in used_self_names:
                name = f"{base} #{suffix}"
                suffix += 1
            morphisms.append({"target": tag, "name": name, "matrix": matrix})
            used_self_names.add(name)
        else:
            assert isinstance(existing["name"], str)
            name = existing["name"]
        names.append(name)
    return names, morphisms


def store(path: Path, values: dict[str, Yaml]) -> None:
    """Replace each computed scope on the card by the completed computation."""
    document = frontmatter.load(str(path))
    metadata = corpus.front_matter(document)
    morphisms = list(metadata.get("morphisms", []))
    for field, (block_name, model) in BLOCKS.items():
        value = values.get(field)
        if value is None:
            continue
        if field == "automorphism_group_generator_morphisms":
            assert isinstance(value, list)
            value, morphisms = _generator_morphisms(path.stem, morphisms, value)
        match metadata.get(block_name):
            case dict() as block:
                block[field] = value
                metadata[block_name] = {
                    key: block[key] for key in model.model_fields if key in block
                }
    metadata["morphisms"] = morphisms
    text = records.record_text(metadata, document.content)
    if text != path.read_text():
        path.write_text(text)


def certify(
    root: Path,
    loaded: corpus.Corpus,
    held: Certificates,
    tags: tuple[str, ...],
    seconds: int,
) -> None:
    """Compute every uncertified value, replace its card scope, and certify the result."""
    by_tag = {entry.lattice.tag: entry for entry in loaded.entries}
    for values in computed(requests(loaded, held, tags, seconds), seconds):
        entry = by_tag[str(values["tag"])]
        store(entry.path, values)
        stored = corpus.front_matter(frontmatter.load(str(entry.path)))
        stored_lattice = Lattice.model_validate(stored)
        card_certifications = dict(stored.get("certifications") or {})
        for field in BLOCKS:
            if field not in values or values[field] is None:
                continue
            block_name = BLOCKS[field][0]
            block = stored.get(block_name)
            assert isinstance(block, dict)
            computation = name(entry.lattice.tag, field)
            certificate_hash = certificates.certification_hash(
                computation, stored_lattice, certified_value(field, block.get(field), stored_lattice)
            )
            card_certifications[f"{block_name}.{field}"] = certificate_hash
            held[computation] = Certificate(hash=certificate_hash, by=str(values["by"]))
        stored["certifications"] = card_certifications
        document = frontmatter.load(str(entry.path))
        entry.path.write_text(records.record_text(stored, document.content))
        certificates.save(root, held)
        print(
            entry.lattice.tag,
            {field: values[field] for field in BLOCKS if field in values},
            flush=True,
        )
