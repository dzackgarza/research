r"""Deligne--Mumford moduli spike: `\Gamma_{g,n}` and graph-indexed stratum formulas.

**Implements:** finite category `\Gamma_{g,n}`, specialization poset, formal stratum
descriptors. **Does not implement:** DM stacks, coarse moduli schemes, curves, families.

See ``README.md`` for the full mathematical contract.
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
