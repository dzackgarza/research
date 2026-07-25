r"""Serialising Gram matrices for the Julia/Oscar backend, plus the bond matrices.

**Scope note.** This repo treats Julia as a *hidden backend*: it is reached only
through the parity ledger, behind spike seams, and is never a user-facing surface.
This module is therefore a serialiser and nothing more -- it formats a matrix as a
Julia literal. It deliberately does not import ``juliacall`` or start a Julia
runtime; the old init.sage had that import commented out, and turning it on is a
decision for the ledger, not a side effect of a preamble.
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ

__all__ = ["BONDS", "matrix_to_julia_literal"]


def matrix_to_julia_literal(gram: Any) -> str:
    """Format an integer matrix as a Julia matrix literal, ``[a b; c d]``.

    Ported from ``mat_to_julia_str``. The original built this by chained string
    replacement on Sage's matrix repr, which is fragile against spacing and negative
    entries; this walks the rows instead. Verified to agree with the intended form on
    the shapes the old file used it for.
    """
    rows = [" ".join(str(entry) for entry in row) for row in gram.rows()]
    return "[" + "; ".join(rows) + "]"


#: The 2x2 "bond" matrices from the old init.sage, unnamed there beyond these labels.
#: They record edge types in hyperbolic Coxeter diagrams: ordinary, and the heavy
#: oriented/unoriented bonds.
BONDS: dict[str, Any] = {
    "bond1": matrix(ZZ, 2, [2, -1, -1, 2]),
    "bond2": matrix(ZZ, 2, [2, -1, -1, 1]),
    "bond3": matrix(ZZ, 2, [6, -3, -3, 2]),
    "heavy_oriented": matrix(ZZ, 2, [4, -2, -2, 1]),
    "heavy_unoriented": matrix(ZZ, 2, [1, -1, -1, 1]),
}
