"""Phase 3 constructor redefinition entry point.

This module is intentionally inert during Phase 1.  Constructor redefinitions
are specified after the static category hierarchy and concrete category
interceptors are in place.
"""

from __future__ import annotations


def install() -> None:
    """Phase 1 no-op."""
