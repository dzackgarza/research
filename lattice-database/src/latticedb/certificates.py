"""The certificates: each computation that the database has carried out, the digest of its inputs, and the program that carried it out.

`certificates.yaml` maps the name of a computation to its certificate. The name of a computation on one
record is `<tag> <computation>`: `<tag> derive` for the fields that `records.derive` computes from the Gram
tensor, and `<tag> <block>.<field>` for a value that SageMath computes. The name of a check of a source
against the corpus is `source <name>`, and that of a computation over every record is `corpus <name>`.

A computation is carried out once. `latticedb enrich` carries out only the computations without a
certificate for their present inputs, and writes the certificate when the computation agrees with the
stored values. A certificate with `seconds` records a computation that did not finish within that many
seconds; it is carried out again only with a larger time limit. To carry out a computation again, remove
its certificate.
"""

import hashlib
import json
from pathlib import Path

import yaml
from pydantic import Field, TypeAdapter

from latticedb.model import Lattice, Record

CERTIFICATES_FILE = "certificates.yaml"


class Certificate(Record):
    inputs: str = Field(description="SHA-256 digest of the inputs of the computation.")
    by: str = Field(description="The program that carried out the computation, with its version.")
    seconds: int | None = Field(default=None, description="The time limit within which the computation did not finish; absent when it finished.")


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


def gram_digest(lattice: Lattice) -> str:
    """The digest of the Gram tensor, the input of every computation on one record."""
    return digest(json.dumps([[str(x) for x in row] for row in lattice.gram_tensor]))


def is_certified(certificates: Certificates, name: str, inputs: str) -> bool:
    certificate = certificates.get(name)
    return certificate is not None and certificate.inputs == inputs and certificate.seconds is None


def is_pending(certificates: Certificates, name: str, inputs: str, seconds: int) -> bool:
    """Whether the computation is to be carried out with the time limit `seconds`: it has no certificate for `inputs`, or did not finish within fewer seconds."""
    certificate = certificates.get(name)
    if certificate is None or certificate.inputs != inputs:
        return True
    return certificate.seconds is not None and certificate.seconds < seconds
