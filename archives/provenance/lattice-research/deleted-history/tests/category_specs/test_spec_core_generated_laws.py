"""Generated-law style tests for SpecReport outputs in the spec-core slice."""

from __future__ import annotations

import importlib
from collections.abc import Callable
from math import prod
from typing import TYPE_CHECKING, cast

import pytest

importlib.import_module("sage.all")
spec_core = importlib.import_module("category_specs.spec_core")
witnesses = importlib.import_module("category_specs.modules.free_module_witnesses")

if TYPE_CHECKING:
    from category_specs.spec_core import Spec, SpecCheckResult, SpecReport
else:
    SpecReport = spec_core.SpecReport
    SpecCheckResult = spec_core.SpecCheckResult
    Spec = spec_core.Spec


_PRODUCT_CARDINALITY_OBLIGATION_ID: str = "sets.cartesian_product.cardinality"
_PRODUCT_COUNTABILITY_OBLIGATION_ID: str = (
    "sets.cartesian_product.countability"
)
_PRODUCT_ENUMERATION_OBLIGATION_ID: str = (
    "sets.cartesian_product.deterministic_enumeration"
)
_MODULE_CATEGORY_PREFIX: str = "Modules("


def _source_truth_set_provider_category_is_not_module(result: SpecCheckResult) -> None:
    assert result.provider is not None
    assert not result.provider.category.startswith(_MODULE_CATEGORY_PREFIX)


def _result_for_obligation(
    report: SpecReport, obligation_id: str
) -> SpecCheckResult:
    return report.obligation_result_by_id(obligation_id)


def _assert_obligation_status(
    report: SpecReport,
    obligation_id: str,
    expected_status: str,
) -> None:
    result = _result_for_obligation(report, obligation_id)
    assert result.status == expected_status


def _law_finite_product_cardinality_factors(report: SpecReport) -> None:
    assert report.computed_value("cardinality").value == str(prod((5,) * 3))
    spec = Spec.of(report)
    assert spec.subject == "GF(5)^3"
    assert spec.declared_category == "Modules(GF(5)).Free().FiniteRank()"
    assert spec.obligation("sets.cartesian_product.cardinality").id == (
        _PRODUCT_CARDINALITY_OBLIGATION_ID
    )
    cardinality_result = spec.obligation_result(_PRODUCT_CARDINALITY_OBLIGATION_ID)
    _source_truth_set_provider_category_is_not_module(cardinality_result)
    assert tuple(provider.id for provider in spec.providers) == (
        "sets.cartesian_product.cardinality",
    )
    _assert_obligation_status(
        report,
        _PRODUCT_CARDINALITY_OBLIGATION_ID,
        "satisfied_by_provider",
    )
    assert tuple(witness.id for witness in spec.witnesses) == (
        "modules.free_finite_rank.cartesian_power.GF(5).3",
    )
    assert report.computed_value("carrier").value == "CartesianPower(GF(5), 3)"


def _law_countable_product_enumeration_is_missing(report: SpecReport) -> None:
    assert report.computed_value("countability").value == "countably infinite"
    assert report.computed_value("cardinality").value == "+Infinity"
    spec = Spec.of(report)
    countability_result = spec.obligation_result(_PRODUCT_COUNTABILITY_OBLIGATION_ID)
    _assert_obligation_status(
        report, _PRODUCT_COUNTABILITY_OBLIGATION_ID, "satisfied_by_provider"
    )
    assert countability_result.provider is not None
    assert countability_result.provider.category == "Sets().CartesianProducts()"
    assert countability_result.provider.id.startswith("sets.cartesian_product.")
    _assert_obligation_status(
        report, _PRODUCT_ENUMERATION_OBLIGATION_ID, "missing"
    )
    enumeration_result = spec.obligation_result(_PRODUCT_ENUMERATION_OBLIGATION_ID)
    assert enumeration_result.provider is None
    assert enumeration_result.witness is None
    assert "module-local iteration" in enumeration_result.obligation.description
    assert tuple(missing.obligation.id for missing in spec.missing_obligations) == (
        _PRODUCT_ENUMERATION_OBLIGATION_ID,
    )
    countability_provider = countability_result.provider
    assert countability_provider is not None
    _source_truth_set_provider_category_is_not_module(countability_result)


_GENERATED_LAWS: tuple[
    tuple[str, Callable[[], SpecReport], tuple[Callable[[SpecReport], None], ...]],
    ...
] = (
    (
        "gf5_rank3_cardinality_matches_factor_product",
        cast(Callable[[], SpecReport], witnesses.gf5_rank3_report),
        (_law_finite_product_cardinality_factors,),
    ),
    (
        "zz2_missing_countable_product_enumeration",
        cast(Callable[[], SpecReport], witnesses.zz_rank2_report),
        (_law_countable_product_enumeration_is_missing,),
    ),
)


@pytest.mark.parametrize(
    "name,report_builder,laws",
    _GENERATED_LAWS,
    ids=[name for name, _, _ in _GENERATED_LAWS],
)
def test_generated_laws_for_spec_report(
    name: str,
    report_builder: Callable[[], SpecReport],
    laws: tuple[Callable[[SpecReport], None], ...],
) -> None:
    del name
    report = report_builder()
    for law in laws:
        law(report)
