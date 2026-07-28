r"""Expose Coxeter diagrams, their category, and their morphisms.

EXAMPLES::

    sage: from dzack_research.preamble.coxeter import CoxeterDiagrams
    sage: from dzack_research import lattice
    sage: diagram = lattice.Lattice("A4").coxeter_diagram()
    sage: diagram.category().is_subcategory(CoxeterDiagrams())
    True
    sage: diagram.subdiagram(diagram.vertices()[:3]).coxeter_matrix()
    [1 3 2]
    [3 1 3]
    [2 3 1]
"""

from sage_lattice_category_spike import (
    CoxeterDiagramHomset,
    CoxeterDiagramMorphism,
    CoxeterDiagrams,
    FiniteCoxeterDiagram,
)

from .fixtures import (
    CROSS_CHECK_RECIPES,
    DIAGRAM_CONVENTION,
    STERK_POSITIONS,
    STERK_ROOT_COUNTS,
)

__all__ = [
    "CROSS_CHECK_RECIPES",
    "DIAGRAM_CONVENTION",
    "STERK_POSITIONS",
    "STERK_ROOT_COUNTS",
    "CoxeterDiagramHomset",
    "CoxeterDiagramMorphism",
    "CoxeterDiagrams",
    "FiniteCoxeterDiagram",
]
