r"""Geometric and combinatorial nouns.

Declaration-only (INVENTORY.md II.4). ``Polyhedron`` is the CLASS of convex
polyhedra (Voronoi cells, fundamental chambers), not Sage's constructor
function of the same spelling — annotating with the constructor is the defect
this module fixes.
"""

from __future__ import annotations

from sage.geometry.polyhedron.base import Polyhedron_base as Polyhedron
from sage.graphs.graph import Graph

__all__ = [
    "Graph",
    "Polygon",
    "Polyhedron",
]

Polygon = Polyhedron
"""A 2-dimensional polytope; the dimension is the constructor's contract."""
