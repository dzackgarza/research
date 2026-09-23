"""Internal ring package.

The public aggregated ring surface is :mod:`dzack_research.preamble.rings`.
Keeping this package initializer dependency-light is required because Python
executes it before every import of a defining module in this package.
"""

from dzack_research.preamble.categories.rings.ring_foundation import (
    RingMor,
    RingMorphism,
)

__all__ = ["RingMor", "RingMorphism"]
