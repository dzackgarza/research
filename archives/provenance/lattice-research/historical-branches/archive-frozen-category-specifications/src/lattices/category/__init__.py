r"""Consolidated lattice adapters over Sage reference implementations."""

from __future__ import annotations

from .category import (
    ConsolidatedLattice,
)
from .category import (
    DiscriminantGroupAdapter as DiscriminantGroupAdapter,
)
from .category import (
    DiscriminantGroups as DiscriminantGroups,
)
from .category import (
    DiscriminantGroupsCategory as DiscriminantGroupsCategory,
)
from .category import (
    Lattice as Lattice,
)
from .category import (
    LatticeHomset as LatticeHomset,
)
from .category import (
    LatticeMorphismAdapter as LatticeMorphismAdapter,
)
from .category import (
    LatticeQuotientAdapter as LatticeQuotientAdapter,
)
from .category import (
    RationalLattices as RationalLattices,
)
from .category import (
    RationalLatticesCategory as RationalLatticesCategory,
)
from .category import (
    from_sage as from_sage,
)

type LatticeObject = ConsolidatedLattice
