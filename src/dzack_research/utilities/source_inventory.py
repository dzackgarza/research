"""Content identity for source-only inspections and live survey provenance."""

from __future__ import annotations

import hashlib
from pathlib import Path


def source_fingerprint(root: Path) -> str:
    """Hash the sorted relative paths and bytes of the inspected Python tree."""
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*.py")):
        digest.update(path.relative_to(root).as_posix().encode() + b"\0")
        digest.update(path.read_bytes() + b"\0")
    return digest.hexdigest()
