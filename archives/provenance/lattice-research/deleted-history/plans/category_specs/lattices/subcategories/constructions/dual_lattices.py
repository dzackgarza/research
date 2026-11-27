r"""Compatibility route for the old dual-lattice construction name."""

from __future__ import annotations

from .dual_objects import LatticeDualObjectsCategory


DualLatticesCategory = LatticeDualObjectsCategory
DualLatticesObject = LatticeDualObjectsCategory.ParentMethods
DualLatticesElement = LatticeDualObjectsCategory.ElementMethods
DualLatticesMorphism = LatticeDualObjectsCategory.MorphismMethods
