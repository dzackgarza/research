"""The genus symbol, the class number, the spinor genera, the hyperbolic index, the order of O(L), and the two series of orbits, from SageMath.

`certify` sends each uncertified applicable computation to `sage_genus.py` under SageMath.
A completed computation is authoritative for the part of the card that computation owns:
an authored value that disagrees is replaced by the computed value, and the resulting
card value is certified. A computation that does not finish remains uncertified.

Two series are computed. `integral.primitive_orbits` is the series $F_{L,\\Gamma}$ of $\\Gamma$-orbits on the
primitive vectors of $L$, written for a definite lattice by enumerating its vectors. `integral.discriminant_orbits`
is the series $F_{A_L,\\Gamma}$ of $\\Gamma$-orbits on the discriminant group $A_L$, written for an even lattice
containing $U^2$; the two agree on that class (Eichler), and only there.
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
from latticedb.relations import hyperbolic_index_bounds

BLOCKS: dict[str, tuple[str, type[BaseModel]]] = {
    "genus_symbol": ("integral", IntegralData),
    "genus_class_count": ("integral", IntegralData),
    "overlattice_count": ("integral", IntegralData),
    "spinor_genus_count": ("integral", IntegralData),
    "spinor_genera": ("integral", IntegralData),
    "hyperbolic_index": ("integral", IntegralData),
    "automorphism_group_order": ("definite", DefiniteData),
    "discriminant_sequence": ("integral", IntegralData),
    "primitive_orbits": ("integral", IntegralData),
    "discriminant_orbits": ("integral", IntegralData),
}
"""Each computed field, with the block of the record that holds it and the model of that block."""

ORBIT_CERTIFIED_BOUND = 4
"""The z/w degree through which the Sage orbit computation certifies a stored series."""


def certified_value(field: str, value: Yaml) -> Yaml:
    """The part of a stored field determined by one completed computation.

    The orbit computations determine only the coefficients through degree 4.
    A card may hold additional source-stated coefficients and a reference; those
    remain on the card but are not included in this computation's certificate.
    Every other field in BLOCKS is determined in full by its computation.
    """
    if field not in {"primitive_orbits", "discriminant_orbits"}:
        return value
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


def applies(field: str, lattice: Lattice, planes: int) -> bool:
    """Whether SageMath computes `field` for `lattice`, of which `planes` is a lower bound of the hyperbolic index.

    Spinor genera are computed for a lattice of rank at least 3, the dimension for which SPLAG, Chapter 15, Theorem 15(b) defines them.
    The order of O(L) is computed for a definite lattice, whose vectors of bounded norm are finite in number.
    The series $F_{L,\\Gamma}$ of orbits of primitive vectors is computed for a definite lattice, by enumerating its vectors.
    The series $F_{A_L,\\Gamma}$ of orbits on the discriminant group is computed for an even lattice that contains $U^2$ (theory/orbits.md).
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


def requests(
    loaded: corpus.Corpus, held: Certificates, tags: tuple[str, ...], seconds: int
) -> list[Request]:
    """For each integral record with a nonzero determinant, the uncertified applicable fields."""
    chosen: list[Request] = []
    bounds = hyperbolic_index_bounds(loaded.entries)
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
                computation, lattice, certified_value(field, stored_value)
            )
            if stored_value is None or certificates.is_pending(
                held, computation, cited.get(f"{block_name}.{field}"), expected_hash
            ):
                fields.append(field)
        if fields:
            gram = [[int(x) for x in row] for row in lattice.gram_tensor]
            chosen.append(
                {
                    "tag": lattice.tag,
                    "gram": gram,
                    "sign": _sign(lattice),
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


def _sequence_morphisms(
    tag: str, morphisms: list[dict[str, Yaml]], value: dict[str, Yaml]
) -> tuple[dict[str, Yaml], list[dict[str, Yaml]]]:
    """Place full lattice isometry generators on the lattice card and refer to them by name."""
    names: list[str] = []
    matrices = value["lattice_generators"]
    assert isinstance(matrices, list)
    for index, matrix in enumerate(matrices, start=1):
        existing = next(
            (
                morphism
                for morphism in morphisms
                if morphism["matrix"] == matrix and morphism.get("scale", 1) == 1
            ),
            None,
        )
        if existing is None:
            name = f"O(L) generator {index} from PARI qfauto"
            morphisms.append({"target": tag, "name": name, "matrix": matrix})
        else:
            assert isinstance(existing["name"], str)
            name = existing["name"]
        names.append(name)
    stored = {key: item for key, item in value.items() if key != "lattice_generators"}
    stored["lattice_generator_morphisms"] = names
    return stored, morphisms


def store(path: Path, values: dict[str, Yaml]) -> None:
    """Replace each computed scope on the card by the completed computation."""
    document = frontmatter.load(str(path))
    metadata = corpus.front_matter(document)
    morphisms = list(metadata.get("morphisms", []))
    for field, (block_name, model) in BLOCKS.items():
        value = values.get(field)
        if value is None:
            continue
        if field == "discriminant_sequence" and isinstance(value, dict):
            value, morphisms = _sequence_morphisms(path.stem, morphisms, value)
        match metadata.get(block_name):
            case dict() as block:
                if field in {"primitive_orbits", "discriminant_orbits"} and isinstance(value, dict):
                    present = block.get(field)
                    replacement = dict(present) if isinstance(present, dict) else {}
                    for group, computed_series in value.items():
                        if not isinstance(computed_series, dict):
                            replacement[group] = computed_series
                            continue
                        old_series = replacement.get(group)
                        updated_series = dict(old_series) if isinstance(old_series, dict) else {}
                        for key, computed_part in computed_series.items():
                            if key in {"z", "w"} and isinstance(computed_part, list):
                                old_part = updated_series.get(key)
                                tail = old_part[len(computed_part):] if isinstance(old_part, list) else []
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
    seconds: int,
) -> None:
    """Compute every uncertified value, replace its card scope, and certify the result."""
    by_tag = {entry.lattice.tag: entry for entry in loaded.entries}
    for values in computed(requests(loaded, held, tags, seconds), seconds):
        entry = by_tag[str(values["tag"])]
        store(entry.path, values)
        stored = corpus.front_matter(frontmatter.load(str(entry.path)))
        card_certifications = dict(stored.get("certifications") or {})
        for field in BLOCKS:
            if field not in values or values[field] is None:
                continue
            block_name = BLOCKS[field][0]
            block = stored.get(block_name)
            assert isinstance(block, dict)
            computation = name(entry.lattice.tag, field)
            certificate_hash = certificates.certification_hash(
                computation, entry.lattice, certified_value(field, block.get(field))
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
