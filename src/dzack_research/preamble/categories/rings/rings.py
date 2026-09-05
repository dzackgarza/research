"""Compatibility import surface for the owned scalar foundation.

Standard ring constructions are methods of the foundational owned ring
categories themselves.  Importing this module therefore performs no category
refinement or structure installation.
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
