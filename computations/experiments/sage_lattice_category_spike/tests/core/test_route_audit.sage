r"""The introspective category-route audit (issue #197, CP3 closure).

Every maintained parent is audited from the LIVE graph: route termination
at the owned ``Sets()`` (by placement or by the underlying-set functor),
per-operation method provenance against the frozen ownership table,
forgetful-functor honesty with morphism action and functor laws, route
coherence, and the executable consequences of the refinement
classification. The inventory lives in ``route_audit`` — a new maintained
parent is audited by adding one row there, with no test edits.

The anti-bypass property is what distinguishes this audit from
output-comparison testing: a leaf override with a numerically CORRECT
answer must still turn the provenance check red.
"""

from __future__ import annotations

import pytest

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.route_audit import (
    audit_parent,
    maintained_parent_inventory,
    provenance_failures,
    report,
)

_INVENTORY = maintained_parent_inventory()


@pytest.mark.parametrize("spec", _INVENTORY, ids=[spec.label for spec in _INVENTORY])
def test_the_maintained_parent_survives_the_route_audit(spec):
    failures = audit_parent(spec)
    assert not failures, "; ".join(failures)


def test_a_numerically_correct_leaf_override_turns_the_provenance_check_red():
    r"""Check 8: introduce a leaf override whose ANSWER is exactly right —
    the provenance comparator must red on it anyway, because provenance is
    a fact of the resolution order, not of the output."""
    a2 = Lattice("A2")
    spec = next(row for row in _INVENTORY if row.label == "lattice A2 (definite)")

    # positive control: the real parent's provenance is green
    assert not provenance_failures(type(a2), spec.owners)

    correct_answer = a2.cardinality()
    bypassed = type("LeafBypassedLattice", (type(a2),), {"cardinality": lambda self: correct_answer})
    failures = provenance_failures(bypassed, spec.owners)
    assert failures
    assert any("cardinality" in failure for failure in failures)
    assert all("cardinality" in failure for failure in failures), "only the bypassed operation may red"


def test_the_route_report_derives_from_the_live_graph_and_is_green():
    r"""Deliverable 2: the report runs from the same introspection surface
    (no stored inputs, so report/test disagreement is impossible) and shows
    every inventory row green on the completed foundation."""
    text = report()
    assert "RED" not in text
    for spec in _INVENTORY:
        assert spec.label in text
