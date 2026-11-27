"""Focused tests for free finite-rank module construction witness reports."""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from category_specs.spec_core import SpecReport

importlib.import_module("sage.all")
witnesses = importlib.import_module("category_specs.modules.free_module_witnesses")


def _computed_values(report: SpecReport) -> dict[str, str]:
    return {value.name: value.value for value in report.computed_values}


def _computed_sources(report: SpecReport) -> dict[str, str]:
    return {value.name: value.source for value in report.computed_values}


def test_gf5_rank3_report_uses_cartesian_power_cardinality_provider() -> None:
    report = witnesses.gf5_rank3_report()
    values = _computed_values(report)

    assert report.subject == "GF(5)^3"
    assert report.declared_category == "Modules(GF(5)).Free().FiniteRank()"
    assert values["carrier"] == "CartesianPower(GF(5), 3)"
    assert values["cardinality"] == "125"
    assert [result.obligation.id for result in report.satisfied_by_witness] == [
        "modules.free_finite_rank.cartesian_power_carrier"
    ]
    assert (
        report.satisfied_by_witness[0].witness.construction
        == "CartesianPower(GF(5), 3)"
    )
    assert [result.obligation.id for result in report.satisfied_by_provider] == [
        "sets.cartesian_product.cardinality"
    ]
    assert all(
        not result.provider.category.startswith("Modules")
        for result in report.satisfied_by_provider
    )
    assert report.missing_obligations == ()


def test_zz_rank2_report_records_countability_and_missing_enumeration_provider(  # noqa: E501
) -> None:
    report = witnesses.zz_rank2_report()
    values = _computed_values(report)
    sources = _computed_sources(report)

    assert report.subject == "ZZ^2"
    assert report.declared_category == "Modules(ZZ).Free().FiniteRank()"
    assert values["carrier"] == "CartesianPower(ZZ, 2)"
    assert values["cardinality"] == "+Infinity"
    assert values["countability"] == "countably infinite"
    assert [result.obligation.id for result in report.satisfied_by_provider] == [
        "sets.cartesian_product.cardinality",
        "sets.cartesian_product.countability",
    ]
    assert [result.obligation.id for result in report.satisfied_by_witness] == [
        "modules.free_finite_rank.cartesian_power_carrier"
    ]
    assert [result.obligation.id for result in report.missing_obligations] == [
        "sets.cartesian_product.deterministic_enumeration"
    ]

    missing = report.missing_obligations[0].obligation
    assert "Owner: Sets().CartesianProducts()" in missing.description
    assert "not satisfied by module-local iteration" in missing.description
    assert sources["countability"].endswith("sage.modules.free_module")


def test_uncountable_infinite_base_does_not_claim_countability_provider() -> None:
    sage_all = importlib.import_module("sage.all")
    report = witnesses.free_finite_rank_module_report(
        sage_all.RR, 1, base_label="RR"
    )
    values = _computed_values(report)

    assert values["cardinality"] == "+Infinity"
    assert "countability" not in values
    assert [result.obligation.id for result in report.satisfied_by_provider] == [
        "sets.cartesian_product.cardinality"
    ]
    assert report.missing_obligations == ()


def test_report_sources_use_stable_sage_module_identifiers() -> None:
    report = witnesses.zz_rank2_report()
    sources = _computed_sources(report)

    assert sources["cardinality"].startswith("sage.categories.sets_cat")
    assert [result.provider.source for result in report.satisfied_by_provider] == [
        "category_specs/sets/subcategories/cartesian_product.py",
        "sage.categories.enumerated_sets",
    ]
    assert all(not source.startswith("/") for source in sources.values())


def test_negative_rank_is_rejected_with_deterministic_api_error() -> None:
    sage_all = importlib.import_module("sage.all")

    with pytest.raises(ValueError):
        witnesses.free_finite_rank_module_report(sage_all.ZZ, -1, base_label="ZZ")
