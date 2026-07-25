r"""Import paths for third-party code under ``computations/vendor/``.

This is the repo-owned replacement for a hand-placed ``.pth`` file in Sage's
venv. A ``.pth`` works, but it is untracked, unreviewable, and silently
destroyed by any Sage rebuild -- the same objection that moved ``sage-init.sage``
into the repo. This module is pip-installed with the package, so it is versioned
and reachable from kernels, the REPL, tests, and plain ``sage -python`` alike.

Two entry points, because clone layouts differ and only the caller knows which:

- :func:`activate` handles the layouts a glob can recognise -- a loose script or
  a package at the clone root, and the ``src/`` layout.
- :func:`activate_clone` takes an explicit subpath, for a clone whose importable
  module sits deeper than that. ``vinal`` is the live example: its module is at
  ``vinal/src/sage/vinal.py``, so no general glob finds it, and adding
  ``vinal/src`` would put a ``sage/`` directory on ``sys.path``.
"""

from __future__ import annotations

import sys
from pathlib import Path

#: ``computations/vendor``, resolved from this file rather than hardcoded, so an
#: editable install follows the working tree and a moved repo still works.
VENDOR_DIR = Path(__file__).resolve().parents[3] / "computations" / "vendor"


def _add(path: Path) -> Path | None:
    """Prepend nothing, append once: never shadow an installed module."""
    entry = str(path)
    if not path.is_dir() or entry in sys.path:
        return None
    sys.path.append(entry)
    return path


def activate() -> tuple[Path, ...]:
    """Put the recognisable vendor layouts on ``sys.path``; return what was added.

    Skips dotted and dunder directories, so ``__pycache__`` and ``.git`` never
    become import roots. Idempotent.
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
    """Put one clone's explicit module directory on ``sys.path``.

    For a clone whose importable module is deeper than :func:`activate` can find.
    Fails loudly when the path is absent: a missing vendored dependency is a
    setup error to fix, never something to proceed past.
    """
    target = VENDOR_DIR.joinpath(name, *subpath)
    assert target.is_dir(), f"vendored clone not found: {target}\nclone it into {VENDOR_DIR}/{name} (see that directory's README)"
    _add(target)
    return target
