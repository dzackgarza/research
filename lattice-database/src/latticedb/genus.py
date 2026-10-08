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
from latticedb.model import DefiniteData, HyperbolicData, IntegralData, Lattice, Yaml
from latticedb.relations import hyperbolic_index_bounds

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "overlattice_count": ("integral", IntegralData),
    "spinor_genus_count": ("integral", IntegralData),
    "spinor_genera": ("integral", IntegralData),
    "hyperbolic_index": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
    "automorphism_group_generator_morphisms": ("definite", DefiniteData),
    "discriminant_sequence": ("integral", IntegralData),
    "primitive_orbits": ("integral", IntegralData),
    "discriminant_orbits": ("integral", IntegralData),
    "reflective": ("hyperbolic", HyperbolicData),
}
"""Each preamble-computed field, with the card block that stores it."""

ORBIT_CERTIFIED_BOUND = 4
"""The z/w degree through which the bounded preamble orbit computation certifies a series."""


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
        matrices = [[list(row) for row in by_name[name].matrix] for name in value]
        return sorted(
            matrices,
            key=lambda rows: tuple(entry for row in rows for entry in row),
        )
    if field in {"primitive_orbits", "discriminant_orbits"}:
        if not isinstance(value, dict):
            return value
        projected: dict[str, Yaml] = {}
        for group, series in value.items():
            if not isinstance(series, dict):
                projected[group] = series
                continue
            z = series.get("z")
            w = series.get("w")
            projected[group] = {
                "constant": series.get("constant"),
                "z": z[:ORBIT_CERTIFIED_BOUND] if isinstance(z, list) else z,
                "w": w[:ORBIT_CERTIFIED_BOUND] if isinstance(w, list) else w,
            }
        return projected
    return value


def applies(field: str, lattice: Lattice, planes: int) -> bool:
    """Whether the preamble exposes `field` on this stored lattice."""
    match field:
        case "automorphism_group_order" | "automorphism_group_generator_morphisms":
            return lattice.definite is not None
        case _ if lattice.integral is None:
            return False
        case "reflective":
            # Signature (1, 1) has a half-line as its domain, where no polyhedron criterion applies.
            return lattice.rank >= 3 and 1 in (lattice.signature or ())
        case "discriminant_sequence":
            return lattice.definite is not None and lattice.integral.parity == "even"
        case "spinor_genus_count" | "spinor_genera":
            return lattice.rank >= 3
        case "primitive_orbits":
            return lattice.definite is not None
        case "discriminant_orbits":
            index = max(planes, lattice.integral.hyperbolic_index or 0)
            return (
                lattice.definite is None
                and lattice.integral.parity == "even"
                and index >= 2
            )
        case _:
            return True


SAGE_MODULE = Path(__file__).with_name("sage_genus.py")


class Request(TypedDict):
    """One lattice and the preamble-owned fields CI asks it to compute."""

    tag: str
    gram: list[list[int | str]]
    integral: bool
    fields: list[str]


def name(tag: str, field: str) -> str:
    """The name of the certificate of `field` of the record `tag`."""
    return f"{tag} {BLOCKS[field][0]}.{field}"


def requests(
    loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...]
) -> list[Request]:
    """For each nondegenerate record, the uncertified applicable preamble computations."""
    chosen: list[Request] = []
    bounds = hyperbolic_index_bounds(loaded.entries)
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.determinant == 0 or (tags and lattice.tag not in tags):
            continue
        applicable = [
            field
            for field in BLOCKS
            if applies(field, lattice, bounds.get(lattice.tag, 0))
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
            gram = [
                [int(value) if value.denominator == 1 else str(value) for value in row]
                for row in lattice.gram_tensor
            ]
            chosen.append(
                {
                    "tag": lattice.tag,
                    "gram": gram,
                    "integral": lattice.integral is not None,
                    "fields": fields,
                }
            )
    return chosen


def computed(chosen: list[Request]) -> Iterator[dict[str, Yaml]]:
    """The values that SageMath computes for `chosen`, one record at a time."""
    task = json.dumps({"lattices": chosen})
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
        # The hyperbolic block holds only computed fields, so the first computed value creates it.
        match metadata.setdefault(block_name, {}):
            case dict() as block:
                if field in {"primitive_orbits", "discriminant_orbits"} and isinstance(
                    value, dict
                ):
                    present = block.get(field)
                    replacement = dict(present) if isinstance(present, dict) else {}
                    for group, computed_series in value.items():
                        if not isinstance(computed_series, dict):
                            replacement[group] = computed_series
                            continue
                        old_series = replacement.get(group)
                        updated_series = (
                            dict(old_series) if isinstance(old_series, dict) else {}
                        )
                        for key, computed_part in computed_series.items():
                            if key in {"z", "w"} and isinstance(computed_part, list):
                                old_part = updated_series.get(key)
                                tail = (
                                    old_part[len(computed_part) :]
                                    if isinstance(old_part, list)
                                    else []
                                )
                                updated_series[key] = [*computed_part, *tail]
                            else:
                                updated_series[key] = computed_part
                        replacement[group] = updated_series
                    block[field] = replacement
                else:
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
) -> None:
    """Compute every uncertified value, replace its card scope, and certify the result."""
    by_tag = {entry.lattice.tag: entry for entry in loaded.entries}
    for values in computed(requests(loaded, held, tags)):
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
                computation,
                stored_lattice,
                certified_value(field, block.get(field), stored_lattice),
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
