r"""Install the interactive Sage session helpers.

EXAMPLES::

    sage: from dzack_research.preamble import install
    sage: install(vendor_paths=False, red_tracebacks=False)
    {}
"""

from __future__ import annotations

from . import ergonomics, fixtures, vendor

__all__ = ["ergonomics", "fixtures", "install", "vendor"]


def install(
    *,
    vendor_paths: bool = True,
    red_tracebacks: bool = True,
    implicit_multiplication: bool = False,
    gap_package_manager: bool = False,
) -> dict[str, object]:
    """Install selected helpers and report each applied helper.

    EXAMPLES::

        sage: from dzack_research.preamble import install
        sage: install(vendor_paths=False, red_tracebacks=False)
        {}
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
