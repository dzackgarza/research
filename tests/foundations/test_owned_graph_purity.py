"""Regression tests for the owned mathematical category graph."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.group.groups import OwnedGroups, TopologicalGroups
from dzack_research.preamble.categories.group.magmas import Magmas
from dzack_research.preamble.categories.group.profinite.profinite_groups import ProfiniteGroups
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormedModules
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings, _own_ring
from dzack_research.preamble.categories.sets.set_categories import Sets


def _semantic_supercategory_closure(*roots):
    pending = list(roots)
    seen = set()
    while pending:
        category = pending.pop()
        marker = id(category)
        if marker in seen:
            continue
        seen.add(marker)
        yield category
        pending.extend(category.super_categories())


def test_foundational_owned_graph_has_no_sage_mathematical_supercategory() -> None:
    integers = _own_ring(SageZZ)
    roots = (
        Objects(),
        Sets(),
        Magmas(),
        OwnedGroups(),
        TopologicalGroups(),
        ProfiniteGroups(),
        OwnedRings(),
        Modules(integers),
        Algebras(integers),
        FormedModules(integers),
    )

    for category in _semantic_supercategory_closure(*roots):
        assert not type(category).__module__.startswith("sage.categories."), category
