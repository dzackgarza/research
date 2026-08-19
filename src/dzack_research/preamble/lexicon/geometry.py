r"""Geometric and combinatorial nouns: polyhedra, diagrams, Coxeter data.

Declaration-only. Where the preamble does not redefine a concept, the
semantic noun is tied directly to the Sage implementation class in play.

``Polyhedron`` here is the CLASS of convex polyhedra — the type a Voronoi
cell, a fundamental chamber, or a polar dual belongs to. Sage spells its
polyhedron *constructor* with the same word; annotating a signature with
that constructor names a function where a type is meant, and this module
exists so owned signatures never do.
"""

from __future__ import annotations

from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.geometry.polyhedron.base import Polyhedron_base as Polyhedron
from sage.graphs.graph import Graph

__all__ = [
    "CoxeterMatrix",
    "Graph",
    "Polyhedron",
]
