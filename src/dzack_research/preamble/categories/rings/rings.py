"""Selected higher constructions on the owned scalar foundation.

Internal mathematical theories should import scalar categories, engine
crossings, and owned-ring adoption from :mod:`ring_foundation`.  This module
is intentionally above the module/algebra implementations: it owns only the
standard ring syntax whose values are constructions in those theories.
"""

from dzack_research.preamble.categories.rings.ring_foundation import *  # noqa: F401,F403
from dzack_research.preamble.categories.rings.ring_foundation import (
    _OwnedRingElement,
    _OwnedRingParent,
    _constructor_over_ring,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_engine_ring,
    _owned_ring,
    _owned_ring_category,
    _owning_constructor,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    RingAdjunctionConstructions as RingConstructions,
)
from dzack_research.preamble.refine import refine


def refine_ring_constructions(ring):
    r"""Attach the selected standard construction syntax to an owned ring."""
    if ring not in OwnedRings():
        raise TypeError("ring constructions require an owned ring")
    return refine(ring, RingConstructions())
