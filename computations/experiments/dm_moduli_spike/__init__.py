r"""Deligne--Mumford moduli spike: the finite category `\Gamma_{g,n}`.

Mathematical contract
=====================

**Implements**

1. The finite category `\Gamma_{g,n}` of stable `n`-marked weighted dual graphs of
   genus `g`, with finite Hom-sets, identity morphisms, and composition
   (Chan--Galatius--Payne).
2. The specialization poset of graph strata — the thinification of `\Gamma_{g,n}`
   after passing to isomorphism classes — as a Sage ``FinitePoset``.
3. Formal graph-indexed stratum formulas (clutching sources, codimension,
   automorphism actions) attached to stable graphs.

**Does not implement**

* The Deligne--Mumford stacks `\mathcal M_{g,n}`, `\overline{\mathcal M}_{g,n}`
  (no universal family, no stack structure).
* Coarse moduli schemes `M_{g,n}`, `\overline M_{g,n}`.
* Stable pointed curves, families `\pi:\mathcal C\to S`, or geometric specializations.

**Notation**

* `\mathcal M_{g,n}`, `\overline{\mathcal M}_{g,n}` — fine moduli stacks (not implemented).
* `M_{g,n}`, `\overline M_{g,n}` — coarse moduli schemes (not implemented).
* `\mathcal M_G` — stratum of curves with dual graph `G` (formal index only).
* `\Gamma_{g,n}` — this package's finite graph category.

Vertex weights are geometric genera of normalization components; total graph genus
is arithmetic genus `b_1(\Gamma)+\sum_v w(v)`.

See ``README.md`` for the full contract and evidence hierarchy.
"""

from __future__ import annotations

import sage.all  # noqa: F401

from .objects.gamma import Gamma_gn, StableGraphCategory, StableGraphHomset, StableGraphMorphism
from .objects.graph_types import StableGraphType, StableGraphTypes
from .objects.records import StableGraph

# Scheme functor (for private landscape stubs).
from .categories.base import AffineScheme, complex_numbers_ring, spec, spec_complex

# Legacy combinatorial API (importable; not in __all__).
from .objects.model import DMCompactificationModel  # noqa: F401
from .objects.strata import DMStratum, ModuliFactor  # noqa: F401
from .stratification.indexing import DualGraphType  # noqa: F401

__all__ = [
    "AffineScheme",
    "Gamma_gn",
    "StableGraph",
    "StableGraphCategory",
    "StableGraphHomset",
    "StableGraphMorphism",
    "StableGraphType",
    "StableGraphTypes",
    "complex_numbers_ring",
    "spec",
    "spec_complex",
]

# Private landscape stubs: dm_moduli_spike.moduli, dm_moduli_spike.geometry, ...
