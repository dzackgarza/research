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


def test_the_inventory_covers_the_production_parent_surface():
    r"""Independent completeness: the production-parent surface is
    enumerated from the modules themselves and compared against the
    authored inventory — a new production Parent class must either be
    covered by an inventory instance's family or carry an explicit,
    reasoned exemption here."""
    import inspect

    from sage.structure.parent import Parent as SageParent

    from sage_lattice_category_spike.forms import discriminant, discriminant_forms
    from sage_lattice_category_spike.morphisms import homsets, isometry_groups
    from sage_lattice_category_spike.objects import (
        fundamental_sets,
        functors,
        parents,
        set_constructions,
        underlying_sets,
    )

    exempt = {
        # the route's own codomain: audited as every row's underlying set
        "UnderlyingSet",
        # kernel-contract parents with no set-refinement claim (proven by
        # the functor-kernel suite)
        "FunctorSpace",
        # regime-gated engine contracts with no total refinement
        # classification; their proofs live with their engines
        # (test_method_placement, the embedding suites)
        "LatticeHomset", "EmbeddingHomset",
    }

    inventory_types = tuple(type(spec.construct()) for spec in _INVENTORY)
    covered_bases = tuple({base for parent_type in inventory_types for base in parent_type.__mro__})

    missing = []
    for module in (parents, fundamental_sets, set_constructions, underlying_sets, functors, discriminant, discriminant_forms, homsets, isometry_groups):
        for name, cls in sorted(vars(module).items()):
            if not (inspect.isclass(cls) and issubclass(cls, SageParent) and cls.__module__ == module.__name__):
                continue
            if name in exempt:
                continue
            if any(issubclass(cls, base) and base is not SageParent for base in covered_bases if base in cls.__mro__ and getattr(base, "__module__", "").startswith("sage_lattice_category_spike")):
                continue
            missing.append(f"{module.__name__}.{name}")
    assert not missing, f"production parents with no inventory family and no reasoned exemption: {missing}"


def test_an_identity_returning_forgetful_functor_turns_the_honesty_check_red():
    r"""Red demonstration for check 3, kept as a permanent test: a functor
    that hands back the structured object unchanged must fail honesty."""
    from sage.structure.parent import Parent as SageParent

    from sage_lattice_category_spike.objects.sets import Sets
    from sage_lattice_category_spike.route_audit import MaintainedParent, forgetful_functor_failures

    class DishonestlyForgetting(SageParent):
        def __init__(self):
            SageParent.__init__(self, category=Sets().Finite())

        def underlying_set(self):
            return self

        def an_element(self):
            return 0

    parent = DishonestlyForgetting()
    spec = MaintainedParent(
        label="dishonest forgetting",
        construct=DishonestlyForgetting,
        classification="finite",
        owners={"underlying_set": "test::DishonestlyForgetting.underlying_set"},
    )
    failures = forgetful_functor_failures(spec, parent)
    assert failures
    assert any("not an UnderlyingSet" in failure for failure in failures)

    # positive control: the real A2 row passes the same check
    a2_spec = next(row for row in _INVENTORY if row.label == "lattice A2 (definite)")
    assert not forgetful_functor_failures(a2_spec, a2_spec.construct())


def test_a_broken_enumeration_turns_the_refinement_check_red():
    r"""Red demonstration for check 7, kept as a permanent test: a
    countable parent whose enumeration repeats itself must fail the
    duplicate-free prefix law even though every other answer is right."""
    from sage.structure.parent import Parent as SageParent

    from sage_lattice_category_spike.objects.cardinals import Cardinal, aleph0
    from sage_lattice_category_spike.objects.sets import Sets
    from sage_lattice_category_spike.route_audit import MaintainedParent, refinement_failures

    class ConstantEnumeration(SageParent):
        def __init__(self):
            SageParent.__init__(self, category=Sets().Countable().Infinite())

        def cardinality(self):
            return aleph0

        def __iter__(self):
            while True:
                yield 1

        def __getitem__(self, n):
            return 1

        def index(self, element):
            return 0

    parent = ConstantEnumeration()
    spec = MaintainedParent(
        label="constant enumeration",
        construct=ConstantEnumeration,
        classification="countably_infinite",
        owners={"cardinality": "test::ConstantEnumeration.cardinality", "__iter__": "test::ConstantEnumeration.__iter__"},
    )
    failures = refinement_failures(spec, parent)
    assert failures
    assert any("duplicate-free" in failure for failure in failures)
