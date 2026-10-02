"""The genus symbol, the class number, the spinor genera, the hyperbolic index, the order of O(L) and the series of orbits of primitive vectors, from SageMath.

`certify` sends the Gram tensor of each integral record with a nonzero determinant, with the values that
have no certificate for that Gram tensor, to `sage_genus.py` under SageMath, and stores each value as
soon as SageMath returns it: a value that the record does not hold is written into it, and a stored value
that differs from the computed one is a problem. A series of orbits merges with the stored one: each coefficient
that the record does not state is written, and the stated ones must agree. A value that agrees with the record is certified; a value
that SageMath does not compute within the time limit is certified as not finished within it.
"""

import json
import os
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import TypedDict

import frontmatter
from pydantic import BaseModel, TypeAdapter

from latticedb import certificates, corpus, records
from latticedb.certificates import Certificate, Certificates
from latticedb.model import DefiniteData, IntegralData, Lattice, Yaml

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "spinor_genus_count": ("integral", IntegralData),
    "spinor_genera": ("integral", IntegralData),
    "hyperbolic_index": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
    "discriminant_sequence": ("integral", IntegralData),
    "primitive_orbits": ("integral", IntegralData),
}
"""Each computed field, with the block of the record that holds it and the model of that block."""


def applies(field: str, lattice: Lattice, planes: int) -> bool:
    """Whether SageMath computes `field` for `lattice`, of which `planes` is a lower bound of the hyperbolic index.

    Spinor genera are computed for a lattice of rank at least 3, the dimension for which SPLAG, Chapter 15, Theorem 15(b) defines them.
    The order of O(L) is computed for a definite lattice, whose vectors of bounded norm are finite in number. The series of
    orbits of primitive vectors is computed for a definite lattice, and for an even lattice that contains U^2 (theory/orbits.md).
    """
    assert lattice.integral is not None
    match field:
        case "automorphism_group_order":
            return lattice.definite is not None
        case "discriminant_sequence":
            return lattice.definite is not None and lattice.integral.parity == "even"
        case "spinor_genus_count" | "spinor_genera":
            return lattice.rank >= 3
        case "primitive_orbits":
            index = max(planes, lattice.integral.hyperbolic_index or 0)
            return lattice.definite is not None or (lattice.integral.parity == "even" and index >= 2)
        case _:
            return True


SAGE_MODULE = Path(__file__).with_name("sage_genus.py")


class Request(TypedDict):
    """One lattice of the task that `SAGE_MODULE` reads as its `Request`: the tag, the Gram matrix, the sign of `_sign` and the pending fields."""

    tag: str
    gram: list[list[int]]
    sign: int
    fields: list[str]


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


def requests(loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...], seconds: int) -> list[Request]:
    """For each integral record with a nonzero determinant, among `tags` when it is not empty, the fields that are pending with the time limit `seconds`."""
    chosen: list[Request] = []
    bounds = corpus.hyperbolic_index_bounds(loaded.morphisms, loaded.entries)
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.integral is None or lattice.determinant == 0 or (tags and lattice.tag not in tags):
            continue
        inputs = certificates.gram_digest(lattice)
        applicable = [field for field in BLOCKS if applies(field, lattice, bounds.get(lattice.tag, 0))]
        fields = [field for field in applicable if certificates.is_pending(held, name(lattice.tag, field), inputs, seconds)]
        if fields:
            gram = [[int(x) for x in row] for row in lattice.gram_tensor]
            chosen.append({"tag": lattice.tag, "gram": gram, "sign": _sign(lattice), "fields": fields})
    return chosen


def computed(chosen: list[Request], seconds: int) -> Iterator[dict[str, Yaml]]:
    """The values that SageMath computes for `chosen`, one record at a time."""
    task = json.dumps({"seconds": seconds, "lattices": chosen})
    # Keep the host SageMath environment separate from the project environment.
    environment = {variable: value for variable, value in os.environ.items() if variable != "VIRTUAL_ENV"}
    own = str(Path(sys.prefix) / "bin")
    environment["PATH"] = os.pathsep.join(entry for entry in environment["PATH"].split(os.pathsep) if entry != own)
    command = [environment["SAGE_BIN"], "-c", f"import runpy; runpy.run_path({str(SAGE_MODULE)!r}, run_name='__main__')"]
    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, env=environment) as process:
        assert process.stdin is not None and process.stdout is not None
        process.stdin.write(task)
        process.stdin.close()
        # SageMath writes a carriage return to standard output for some lattices (for E8, record 0094), which reads as an empty line.
        yield from (json.loads(line) for line in process.stdout if line.strip())
    assert process.returncode == 0, f"{SAGE_MODULE} exited with status {process.returncode}"


def merged(stored: Yaml, value: Yaml, location: str) -> tuple[Yaml, list[str]]:
    """The union of a stored and a computed value, with a problem at each place where both state a different scalar.

    Dictionaries merge key by key, lists entry by entry with null for an entry that is not stated, and a null value is not stated.
    """
    match stored, value:
        case None, _:
            return value, []
        case _, None:
            return stored, []
        case dict(), dict():
            union: dict[str, Yaml] = {}
            found: list[str] = []
            for key in [*stored, *(key for key in value if key not in stored)]:
                union[key], problems = merged(stored.get(key), value.get(key), f"{location}.{key}")
                found.extend(problems)
            return union, found
        case list(), list():
            entries: list[Yaml] = []
            found = []
            for index in range(max(len(stored), len(value))):
                left = stored[index] if index < len(stored) else None
                right = value[index] if index < len(value) else None
                entry, problems = merged(left, right, f"{location}[{index}]")
                entries.append(entry)
                found.extend(problems)
            return entries, found
        case _ if stored == value:
            return stored, []
        case _:
            return stored, [f"{location} is {stored}, and SageMath computes {value}"]


def _sequence_morphisms(path: Path, value: dict[str, Yaml]) -> tuple[dict[str, Yaml], Path, list[dict[str, Yaml]], str]:
    """Place full lattice isometry generators in the self-morphism file and refer to them by name."""
    tag = path.stem
    morphism_path = path.parent.parent / "morphisms" / f"{tag}-{tag}.md"
    if morphism_path.exists():
        document = frontmatter.load(str(morphism_path))
        morphisms = TypeAdapter(list[dict[str, Yaml]]).validate_python(document.metadata["morphisms"])
        prose = document.content
    else:
        morphisms = []
        prose = "Generators of the integral orthogonal group in the basis of the lattice record."
    names: list[str] = []
    matrices = value["lattice_generators"]
    assert isinstance(matrices, list)
    for index, matrix in enumerate(matrices, start=1):
        existing = next((morphism for morphism in morphisms if morphism["matrix"] == matrix and morphism.get("scale", 1) == 1), None)
        if existing is None:
            name = f"O(L) generator {index} from PARI qfauto"
            morphisms.append({"name": name, "matrix": matrix})
        else:
            assert isinstance(existing["name"], str)
            name = existing["name"]
        names.append(name)
    stored = {key: item for key, item in value.items() if key != "lattice_generators"}
    stored["lattice_generator_morphisms"] = names
    return stored, morphism_path, morphisms, prose


def store(path: Path, values: dict[str, Yaml]) -> dict[str, str]:
    """Write into the record at `path` each computed value that it does not hold; for each field whose stored value differs from the computed one, the problem."""
    document = frontmatter.load(str(path))
    metadata = corpus.front_matter(document)
    found: dict[str, str] = {}
    sequence_morphisms: tuple[Path, list[dict[str, Yaml]], str] | None = None
    for field, (block_name, model) in BLOCKS.items():
        value = values.get(field)
        if field == "discriminant_sequence" and isinstance(value, dict):
            value, morphism_path, morphisms, prose = _sequence_morphisms(path, value)
            sequence_morphisms = morphism_path, morphisms, prose
        match metadata.get(block_name):
            case dict() as block if value is not None:
                union, problems = merged(block.get(field), value, f"{path}: {block_name}.{field}")
                if problems:
                    found[field] = "; ".join(problems)
                    continue
                block[field] = union
                metadata[block_name] = {key: block[key] for key in model.model_fields if key in block}
                if field == "discriminant_sequence" and sequence_morphisms is not None:
                    morphism_path, morphisms, prose = sequence_morphisms
                    morphism_text = records.morphisms_text(path.stem, path.stem, morphisms, prose)
                    if not morphism_path.exists() or morphism_path.read_text() != morphism_text:
                        morphism_path.write_text(morphism_text)
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
