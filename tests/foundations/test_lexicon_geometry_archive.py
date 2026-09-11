r"""Archive reconciliation for geometric/combinatorial vocabulary.

The archive module was declaration-only.  The live lexicon retains the exact
implementation classes for Coxeter matrices, graphs and convex polyhedra.
"""

from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix as SageCoxeterMatrix
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.graphs.graph import Graph as SageGraph

from dzack_research.preamble.lexicon import CoxeterMatrix, Graph, Polyhedron

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/lexicon/geometry.py",
    "live_owner": "src/dzack_research/preamble/lexicon/__init__.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_geometry_nouns_are_the_live_semantic_classes() -> None:
    assert CoxeterMatrix is SageCoxeterMatrix
    assert Graph is SageGraph
    assert Polyhedron is Polyhedron_base
