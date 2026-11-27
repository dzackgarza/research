"""Spec inspection facade tests for real module reports."""

from __future__ import annotations

import importlib

import pytest

importlib.import_module("sage.all")

free_module_witnesses = importlib.import_module(
    "category_specs.modules.free_module_witnesses"
)
Spec = importlib.import_module("category_specs.spec_core").Spec


def test_gf5_rank3_facade_reports_cardinality_and_discoverable_evidence() -> None:
    spec = Spec.of(free_module_witnesses.gf5_rank3_report())

    assert spec.subject == "GF(5)^3"
    assert spec.declared_category == "Modules(GF(5)).Free().FiniteRank()"
    assert spec.value("cardinality").value == "125"
    assert tuple(obligation.id for obligation in spec.obligations) == (
        "sets.cartesian_product.cardinality",
        "modules.free_finite_rank.cartesian_power_carrier",
    )
    assert tuple(provider.id for provider in spec.providers) == (
        "sets.cartesian_product.cardinality",
    )
    assert tuple(witness.id for witness in spec.construction_witnesses) == (
        "modules.free_finite_rank.cartesian_power.GF(5).3",
    )
    assert spec.obligation("sets.cartesian_product.cardinality").id == (
        "sets.cartesian_product.cardinality"
    )
    assert spec.is_complete


def test_zz_rank2_facade_records_missing_deterministic_enumeration() -> None:
    spec = Spec.of(free_module_witnesses.zz_rank2_report())

    assert spec.subject == "ZZ^2"
    assert spec.value("countability").value == "countably infinite"
    assert [
        result.obligation.id for result in spec.missing_obligations
    ] == ["sets.cartesian_product.deterministic_enumeration"]
    result = spec.obligation_result(
        "sets.cartesian_product.deterministic_enumeration"
    )
    assert result.status == "missing"
    assert tuple(obligation.id for obligation in spec.obligations) == (
        "sets.cartesian_product.cardinality",
        "modules.free_finite_rank.cartesian_power_carrier",
        "sets.cartesian_product.countability",
        "sets.cartesian_product.deterministic_enumeration",
    )
    assert tuple(w.id for w in spec.witnesses) == (
        "modules.free_finite_rank.cartesian_power.ZZ.2",
    )
    assert not spec.is_complete


def test_spec_lookup_raises_key_error_by_type_only() -> None:
    spec = Spec.of(free_module_witnesses.gf5_rank3_report())

    with pytest.raises(KeyError):
        spec.obligation("not-an-obligation")
    with pytest.raises(KeyError):
        spec.value("not-a-value")
