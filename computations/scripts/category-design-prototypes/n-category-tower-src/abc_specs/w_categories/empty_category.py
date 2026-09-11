# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/empty_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Empty Category: the empty category as an object in wCat.

The empty category 𝟘 has:
- No 0-cells (no objects)
- No 1-cells (no morphisms)
- No 2-cells (no natural transformations)

As an object in wCat, the empty category inherits from _wCat_0Cell_ABC.
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


@dataclass
class _EmptyCategory_ABC(CategoryABCs.Category, ABC):
    """
    The empty category 𝟘 as a 0-cell in wCat.

    Has no objects and no morphisms.
    """

    pass


_ = _EmptyCategory_ABC
