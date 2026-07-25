r"""The interactive preamble: what a fresh Sage session gets, and how to toggle it.

``sage-init.sage`` at the repo root is a thin caller; the decisions live here so
they can be changed, tested and reviewed without touching machine state. Import
this package from a notebook to get the same session a REPL gets.

Every stanza of :func:`install` is a keyword you can turn off, because the old
init.sage's failure mode was that it was all-or-nothing: one broken import at the
top cost you the whole namespace.

Monkeypatches are NOT installed by default and are not part of this package's
import side effects -- see :mod:`dzack_research.preamble.patches`.
"""

from __future__ import annotations

from . import ergonomics, vendor

__all__ = ["ergonomics", "install", "vendor"]


def install(
    *,
    vendor_paths: bool = True,
    red_tracebacks: bool = True,
    implicit_multiplication: bool = False,
    gap_package_manager: bool = False,
) -> dict[str, object]:
    """Apply the session preamble; return a report of what was actually done.

    The report is the point: a preamble that silently half-applies is the thing
    the old init.sage got wrong, so every stanza states its outcome and a caller
    can assert on it.

    ``implicit_multiplication`` defaults off -- it rewrites how source is parsed,
    which is not something to inherit by surprise.
    """
    report: dict[str, object] = {}

    if vendor_paths:
        report["vendor_paths"] = [str(p) for p in vendor.activate()]

    if red_tracebacks:
        ergonomics.enable_red_traceback_highlight()
        report["red_tracebacks"] = True

    if implicit_multiplication:
        ergonomics.enable_implicit_multiplication()
        report["implicit_multiplication"] = True

    if gap_package_manager:
        ergonomics.load_gap_package_manager()
        report["gap_package_manager"] = True

    return report
