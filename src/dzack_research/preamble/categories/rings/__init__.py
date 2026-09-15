"""Internal ring package.

The public aggregated ring surface is :mod:`dzack_research.preamble.rings`.
Keeping this package initializer dependency-light is required because Python
executes it before every import of a defining module in this package.
"""

from dzack_research.preamble.categories.rings.ring_foundation import (
    RingHomset,
    RingMorphism,
)

__all__ = ["RingHomset", "RingMorphism"]
