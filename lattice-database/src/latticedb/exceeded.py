"""Computations that a certification job ended before they finished.

`exceeded.yaml` maps the name of a computation to the hash of that name and the
Gram tensor, with the seconds the computation had run when its job ended.

Certification writes the entry when a computation starts, with the seconds left
until the job's timeout, and deletes it when the computation finishes. So an
entry that remains after a job records a computation the timeout ended, and the
time it ran. A computation that ran for at least `WINDOW_SECONDS` does not fit in
one job: certification never requests it again. A computation that ran for less
was ended only because it started late, and the next job computes it first.

The log is permanent. A changed Gram tensor changes the hash, so the entry no
longer applies. After a faster implementation, delete the entry by hand.
"""

from pathlib import Path

import yaml
from pydantic import Field, TypeAdapter

from latticedb import certificates
from latticedb.model import Lattice, Record

EXCEEDED_FILE = "exceeded.yaml"

WINDOW_SECONDS = 5 * 60 * 60
"""The least running time that shows a computation does not fit in one job.

The certification workflow gives a job 330 minutes, so a computation that starts
first in its job runs for more than this before the timeout ends it.
"""


class Interruption(Record):
    hash: str = Field(
        description="SHA-256 digest of the computation name and Gram tensor."
    )
    seconds: int = Field(
        description="Seconds the computation had run when its job ended."
    )


Interruptions = dict[str, Interruption]


def load(root: Path) -> Interruptions:
    path = root / EXCEEDED_FILE
    if not path.exists():
        return {}
    return TypeAdapter(Interruptions).validate_python(
        yaml.safe_load(path.read_text()) or {}
    )


def save(root: Path, log: Interruptions) -> None:
    data = {name: entry.model_dump() for name, entry in sorted(log.items())}
    (root / EXCEEDED_FILE).write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    )


def input_hash(name: str, lattice: Lattice) -> str:
    """Commit to one computation name and Gram tensor."""
    return certificates.certification_hash(name, lattice, None)


def seconds_run(log: Interruptions, name: str, lattice: Lattice) -> int | None:
    """The seconds this computation ran before a job ended it, if one did."""
    entry = log.get(name)
    if entry is None or entry.hash != input_hash(name, lattice):
        return None
    return entry.seconds


def is_exceeded(log: Interruptions, name: str, lattice: Lattice) -> bool:
    """Whether this computation ran for a whole job without finishing."""
    seconds = seconds_run(log, name, lattice)
    return seconds is not None and seconds >= WINDOW_SECONDS
