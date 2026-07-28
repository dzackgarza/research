r"""Import third-party code from ``computations/vendor``.

EXAMPLES::

    sage: from dzack_research.preamble.vendor import activate
    sage: all(path.is_dir() for path in activate())
    True
"""

from __future__ import annotations

import sys
from pathlib import Path

#: ``computations/vendor``, resolved from this file rather than hardcoded, so an
#: editable install follows the working tree and a moved repo still works.
VENDOR_DIR = Path(__file__).resolve().parents[3] / "computations" / "vendor"


def _add(path: Path) -> Path | None:
    """Append an existing path to ``sys.path`` once."""
    entry = str(path)
    if not path.is_dir() or entry in sys.path:
        return None
    sys.path.append(entry)
    return path


def activate() -> tuple[Path, ...]:
    """Add recognized vendor layouts to ``sys.path``.

    EXAMPLES::

        sage: from dzack_research.preamble.vendor import activate
        sage: activate()
        (...)
    """
    assert VENDOR_DIR.is_dir(), f"vendor directory is missing: {VENDOR_DIR}"

    candidates = [VENDOR_DIR]
    for clone in sorted(VENDOR_DIR.iterdir()):
        if not clone.is_dir() or clone.name.startswith((".", "__")):
            continue
        candidates.append(clone)
        candidates.append(clone / "src")

    return tuple(added for added in (_add(p) for p in candidates) if added is not None)


def activate_clone(name: str, *subpath: str) -> Path:
    """Add an explicit module directory from one vendored clone to ``sys.path``."""
    target = VENDOR_DIR.joinpath(name, *subpath)
    assert target.is_dir(), (
        f"vendored clone not found: {target}\nclone it into {VENDOR_DIR}/{name} (see that directory's README)"
    )
    _add(target)
    return target
