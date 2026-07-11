r"""Deligne-Mumford compactification spike.

A stack-aware *combinatorial* model of :math:`\overline{\mathcal M}_{g,n}`.  It
models strata, dimensions, automorphisms, clutching presentations and closure
incidence exactly, while making no claim to implement the algebraic stack as a
functor of points.

The public object model:

- :class:`DMCompactificationModel` -- the typed ambient :math:`\overline{\mathcal M}_{g,n}`.
- :class:`StableCurveTypes` / :class:`StableCurveType` -- the Sage parent/element
  of stable dual-graph types (an index for a stratum).
- :class:`StableGraphContraction` -- a contraction morphism of curve types.
- :class:`DMStratum` -- a geometric stratum (distinct from its indexing graph).
- :class:`DMStratification` -- the finite / rank-truncated stratification.
- :class:`StratificationPoset` -- a typed poset carrying its order convention.
- :class:`StableGraphRecord` -- the immutable half-edge source of truth.
- :class:`QuotientStackPresentation`, :class:`ClutchingMorphism`,
  :class:`ModuliFactor` -- symbolic stack-geometric presentations.

"Weighted stable curve" here means a stable dual graph whose vertex weights are
component genera -- named :class:`StableCurveType` to avoid confusion with
Hassett-weighted marked curves.
"""

from __future__ import annotations

# Eager Sage core initialisation: importing ``sage.categories.*`` before
# ``sage.structure.element`` is fully initialised triggers a circular-import
# failure under a bare ``sage -python`` process ("cannot import name Category").
# Importing ``sage.all`` first forces the correct initialisation order, exactly
# as the sibling lattice spike does through its eager ``sage_patches`` import.
import sage.all  # noqa: F401  (eager load; see comment above)

from .objects.contractions import StableGraphContraction
from .objects.curve_types import StableCurveType, StableCurveTypes
from .objects.model import DMCompactificationModel
from .objects.records import StableGraphRecord
from .objects.strata import (
    ClutchingMorphism,
    DMStratum,
    ModuliFactor,
    QuotientStackPresentation,
)
from .objects.stratification import DMStratification, StratificationPoset

__all__ = [
    "ClutchingMorphism",
    "DMCompactificationModel",
    "DMStratification",
    "DMStratum",
    "ModuliFactor",
    "QuotientStackPresentation",
    "StableCurveType",
    "StableCurveTypes",
    "StableGraphContraction",
    "StableGraphRecord",
    "StratificationPoset",
]
