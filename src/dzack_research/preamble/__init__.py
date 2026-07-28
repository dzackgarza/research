r"""Install the interactive Sage session helpers.

EXAMPLES::

    sage: from dzack_research.preamble import install
    sage: install(vendor_paths=False)
    {'categories': True}
"""

from __future__ import annotations

# Import order: categories registers post-init hooks before catalogue builds lattices.
# Importing ergonomics applies interactive defaults (implicit multiplication, red
# tracebacks, GAP PackageManager).
from . import categories, ergonomics, fixtures, refine, vendor

__all__ = ["categories", "ergonomics", "fixtures", "install", "refine", "vendor"]


def install(*, vendor_paths: bool = True) -> dict[str, object]:
    r"""Register category hooks and optionally activate vendor paths.

    Interactive defaults live in :mod:`ergonomics` and take effect on import.

    EXAMPLES::

        sage: from dzack_research.preamble import install
        sage: install(vendor_paths=False)
        {'categories': True}
    """
    report: dict[str, object] = {}

    categories.install()
    report["categories"] = True

    if vendor_paths:
        report["vendor_paths"] = [str(p) for p in vendor.activate()]

    return report
