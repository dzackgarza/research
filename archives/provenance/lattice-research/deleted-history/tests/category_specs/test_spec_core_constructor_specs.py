"""Tests for constructor-provenance registry behavior.

The tests exercise nontrivial registry behavior in ``category_specs.spec_core``:
lookup by stable identifier, filtering by mathematical owner, and duplicate-id
rejection.
"""

from __future__ import annotations

import importlib

import pytest

importlib.import_module("sage.all")

from category_specs.spec_core import ConstructorRegistry, ConstructorSpec  # noqa: E402

_RING_ZZ = ConstructorSpec(
    id="rings-zz",
    owner_category="Rings()",
    method_name="ZZ",
    sage_entry_point="Rings._Constructors.ZZ",
    sage_source="category_specs.rings.__init__",
    target_category="Rings().IntegralDomain()",
    target_refinement_route=("Rings()",),
    obligation_ids=("rings.has_zero_element", "rings.has_one_element"),
    provider_ids=("rings.provider.base_ring",),
    description=(
        "Refine Sage ZZ into project ring root with integral-domain owner route."
    ),
)


_RING_QQ = ConstructorSpec(
    id="rings-qq",
    owner_category="Rings()",
    method_name="QQ",
    sage_entry_point="Rings._Constructors.QQ",
    sage_source="category_specs.rings.__init__",
    target_category="Rings().Field()",
    target_refinement_route=("Rings()", "Rings().Commutative()"),
    obligation_ids=("rings.is_commutative",),
    witness_ids=("rings.ww-fraction-field",),
    description="Refine Sage QQ with field-level invariants.",
)

_MODULE_FREE = ConstructorSpec(
    id="modules-free-zz-3",
    owner_category="Modules(ZZ).Free()",
    method_name="free_module",
    sage_entry_point="Modules._Constructors.FreeModule",
    sage_source="category_specs.modules.__init__",
    target_category="Modules(ZZ).Free().FinitelyPresented()",
    target_refinement_route=(
        "Modules(ZZ).Free()",
        "Modules(ZZ).FinitelyPresented()",
    ),
    obligation_ids=("modules.free_finite_rank.cartesian_power_carrier",),
    description="Expose the free module construction as finite-presented free modules.",
)

_MODULE_POLY = ConstructorSpec(
    id="modules-free-polynomial-zz",
    owner_category="Modules(ZZ).Free()",
    method_name="free_module_as_polynomial_ring",
    sage_entry_point="Modules._Constructors.polynomial_ring_as_module",
    sage_source="category_specs.modules.__init__",
    target_category="Modules(ZZ).Free().FinitelyPresented()",
    target_refinement_route=("Modules(ZZ).Free()",),
    obligation_ids=("modules.free_finite_rank.cartesian_power_carrier",),
    provider_ids=("modules.provider.vector_space_carrier",),
    description="Refines a polynomial ring object constructor through modules.",
)


def _module_constructor_registry() -> ConstructorRegistry:
    return ConstructorRegistry(
        constructors=(
            _RING_ZZ,
            _RING_QQ,
            _MODULE_FREE,
            _MODULE_POLY,
        )
    )


def test_constructor_registry_lookup_by_id() -> None:
    registry = _module_constructor_registry()

    zz = registry.constructor("rings-zz")
    module_ctor = registry.constructor("modules-free-zz-3")

    assert zz.owner_category == "Rings()"
    assert zz.method_name == "ZZ"
    assert zz.sage_entry_point.endswith("Rings._Constructors.ZZ")
    assert module_ctor.target_category == "Modules(ZZ).Free().FinitelyPresented()"
    assert module_ctor.description
    assert module_ctor.sage_source == "category_specs.modules.__init__"


def test_constructor_registry_filter_by_owner_and_route_query() -> None:
    registry = _module_constructor_registry()

    ring_constructors = registry.by_owner("Rings()")
    module_constructors = registry.by_owner("Modules(ZZ).Free()")

    assert [item.id for item in ring_constructors] == ["rings-zz", "rings-qq"]
    assert [
        item.id for item in module_constructors
    ] == [
        "modules-free-zz-3",
        "modules-free-polynomial-zz",
    ]

    ring_targets = registry.by_route_target("Rings().Field()")
    assert [item.id for item in ring_targets] == ["rings-qq"]
    assert registry.owners() == ("Modules(ZZ).Free()", "Rings()")


def test_constructor_registry_filters_by_obligation() -> None:
    registry = _module_constructor_registry()
    carrier_constructors = registry.with_obligation(
        "modules.free_finite_rank.cartesian_power_carrier"
    )

    assert {constructor.id for constructor in carrier_constructors} == {
        "modules-free-zz-3",
        "modules-free-polynomial-zz",
    }
    assert all(
        "Modules(ZZ).Free()" in constructor.owner_category
        for constructor in carrier_constructors
    )


def test_constructor_spec_rejects_admission_status_metadata() -> None:
    with pytest.raises(ValueError):
        ConstructorSpec(
            id="example-status-tagged-construction",
            owner_category="ExampleCategory()",
            method_name="StatusTaggedConstructor",
            sage_entry_point="ExampleCategory._Constructors.StatusTaggedConstructor",
            sage_source="tests.category_specs",
            target_category="ExampleCategory().Target()",
            status="not-mapped",
        )


def test_constructor_registry_rejects_duplicate_ids() -> None:
    duplicate = ConstructorSpec(
        id="rings-zz",
        owner_category="Rings()",
        method_name="ZeroRing",
        sage_entry_point="Rings._Constructors.ZeroRing",
        sage_source="category_specs.rings.__init__",
        target_category="Rings()",
        description="Different method with colliding constructor id.",
    )

    with pytest.raises(ValueError):
        ConstructorRegistry(constructors=(_RING_ZZ, duplicate))
