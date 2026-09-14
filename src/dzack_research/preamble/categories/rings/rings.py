"""Compatibility import surface for the owned scalar foundation.

Standard ring constructions are methods of the foundational owned ring
categories themselves.  Importing this module therefore performs no category
refinement or structure installation.
"""

from dzack_research.preamble.categories.rings.ring_foundation import *  # noqa: F401,F403
from dzack_research.preamble.categories.rings.ring_foundation import (
    _constructor_over_ring as _constructor_over_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element as _engine_element,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring as _engine_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _own_ring as _own_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_engine_ring as _owned_engine_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring as _owned_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring_category as _owned_ring_category,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _OwnedRingElement as _OwnedRingElement,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _OwnedRingParent as _OwnedRingParent,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owning_constructor as _owning_constructor,
)
