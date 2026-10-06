"""Certificates of completed computations.

`certificates.yaml` maps the name of a computation to one hash of the
computation name, the Gram tensor, and the value stored on the card. The card
is the only place that stores the value itself.

A computation that does not finish has no certificate. Authored or seeded
card values have no certification status until the certification phase
computes them and writes a certificate.
"""

import hashlib
import json
from pathlib import Path

import yaml
from pydantic import Field, TypeAdapter

from latticedb.model import Lattice, Record

CERTIFICATES_FILE = "certificates.yaml"


class Certificate(Record):
    hash: str = Field(
        description="SHA-256 digest of the computation name, Gram tensor, and certified card value.",
    )
    by: str = Field(description="The program that carried out the computation, with its version.")


Certificates = dict[str, Certificate]


def load(root: Path) -> Certificates:
    path = root / CERTIFICATES_FILE
    if not path.exists():
        return {}
    return TypeAdapter(Certificates).validate_python(yaml.safe_load(path.read_text()) or {})


def save(root: Path, certificates: Certificates) -> None:
    data = {name: certificate.model_dump(exclude_none=True) for name, certificate in sorted(certificates.items())}
    (root / CERTIFICATES_FILE).write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def certification_hash(name: str, lattice: Lattice, value: object) -> str:
    """Commit to one computation name, Gram tensor, and stored result."""
    return digest(
        json.dumps(
            {
                "computation": name,
                "gram_tensor": [
                    [str(entry) for entry in row] for row in lattice.gram_tensor
                ],
                "result": value,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            default=str,
        )
    )


def is_certified(
    certificates: Certificates,
    name: str,
    cited_hash: str | None,
    expected_hash: str,
) -> bool:
    """Whether the card cites the exact completed certificate for its stored result."""
    certificate = certificates.get(name)
    return (
        cited_hash == expected_hash
        and certificate is not None
        and certificate.hash == cited_hash
    )


def is_pending(
    certificates: Certificates,
    name: str,
    cited_hash: str | None,
    expected_hash: str,
) -> bool:
    """Whether the card lacks a completed certificate for its stored result."""
    return not is_certified(certificates, name, cited_hash, expected_hash)
