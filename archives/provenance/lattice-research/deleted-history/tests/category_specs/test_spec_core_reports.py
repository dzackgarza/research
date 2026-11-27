"""Focused tests for the standalone spec-core report kernel."""

from __future__ import annotations

import importlib

import pytest

importlib.import_module("sage.all")
spec_core = importlib.import_module("category_specs.spec_core")
ComputedValue = spec_core.ComputedValue
ConstructionWitness = spec_core.ConstructionWitness
SpecCheckResult = spec_core.SpecCheckResult
SpecObligation = spec_core.SpecObligation
SpecProvider = spec_core.SpecProvider
SpecRegistry = spec_core.SpecRegistry


def test_registry_report_partitions_provider_witness_and_missing_obligations() -> None:
    finite_cardinality = SpecObligation(
        id="finite-cardinality",
        title="Finite objects expose their cardinality",
        source="category_specs/sets/subcategories/finite.py",
    )
    enumerability = SpecObligation(
        id="enumerability",
        title="Enumerated objects expose an iterator contract",
        source="category_specs/sets/subcategories/finite_enumerated_set.py",
    )
    free_rank = SpecObligation(
        id="free-rank",
        title="Free finite-rank modules expose rank",
        source="category_specs/modules/subcategories/free.py",
    )

    registry = SpecRegistry(
        obligations=(finite_cardinality, enumerability, free_rank),
        providers=(
            SpecProvider(
                id="finite-set-cardinality-methods",
                category="Sets().Finite()",
                provides=("finite-cardinality",),
                source="category_specs/sets/subcategories/finite.py",
            ),
        ),
        witnesses=(
            ConstructionWitness(
                id="cartesian-power-free-module-witness",
                construction="cartesian_power",
                source_category="Modules(GF(5)).Free()",
                target_category="Modules(GF(5)).Free().FinitelyPresented()",
                provides=("free-rank",),
                source=(
                    ".agents/plans/features/"
                    "FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/"
                    "PLAN-SPEC-CORE-VERTICAL-SLICE/"
                    "PHASE-SPEC-CORE-VERTICAL-SLICE"
                ),
            ),
        ),
    )

    report = registry.report(
        subject="GF(5)^3",
        declared_category="Modules(GF(5)).Free().FinitelyPresented()",
        inherited_obligation_ids=(
            "finite-cardinality",
            "free-rank",
            "enumerability",
        ),
        computed_values=(
            ComputedValue(
                name="cardinality",
                value="125",
                source="Sage GF(5)^3 cardinality",
            ),
        ),
    )

    assert report.declared_category == "Modules(GF(5)).Free().FinitelyPresented()"
    assert report.computed_value("cardinality") == ComputedValue(
        name="cardinality",
        value="125",
        source="Sage GF(5)^3 cardinality",
    )
    assert report.obligation_result_by_id("finite-cardinality").provider.id == (
        "finite-set-cardinality-methods"
    )
    assert report.obligation_result_by_id("free-rank").witness.id == (
        "cartesian-power-free-module-witness"
    )
    assert report.obligation_result_by_id("enumerability").status == "missing"
    assert report.missing_obligation_ids() == ("enumerability",)
    assert report.provider_ids() == ("finite-set-cardinality-methods",)
    assert report.witness_ids() == ("cartesian-power-free-module-witness",)
    assert tuple(type(item).__name__ for item in report.completion_evidence()) == (
        "SpecProvider",
        "ConstructionWitness",
        "ComputedValue",
    )
    assert registry.obligation("finite-cardinality").title == (
        "Finite objects expose their cardinality"
    )
    assert registry.provider("finite-cardinality").id == (
        "finite-set-cardinality-methods"
    )
    assert registry.witness("free-rank").id == "cartesian-power-free-module-witness"
    assert registry.missing_obligation_ids(
        ("finite-cardinality", "free-rank", "enumerability")
    ) == ("enumerability",)
    assert registry.provider_ids == ("finite-set-cardinality-methods",)
    assert registry.witness_ids == ("cartesian-power-free-module-witness",)
    assert [result.obligation.id for result in report.satisfied_by_provider] == [
        "finite-cardinality"
    ]
    assert (
        report.satisfied_by_provider[0].provider.id
        == "finite-set-cardinality-methods"
    )
    assert [result.obligation.id for result in report.satisfied_by_witness] == [
        "free-rank"
    ]
    assert (
        report.satisfied_by_witness[0].witness.id
        == "cartesian-power-free-module-witness"
    )
    assert [(value.name, value.value) for value in report.computed_values] == [
        ("cardinality", "125")
    ]
    assert [result.obligation.id for result in report.missing_obligations] == [
        "enumerability"
    ]
    assert not report.is_complete()
    assert [result.status for result in report.all_results()] == [
        "satisfied_by_provider",
        "satisfied_by_witness",
        "missing",
    ]


def test_report_query_helpers_raise_for_unknown_keys() -> None:
    finite_cardinality = SpecObligation(
        id="finite-cardinality",
        title="Finite objects expose their cardinality",
        source="category_specs/sets/subcategories/finite.py",
    )
    registry = SpecRegistry(
        obligations=(finite_cardinality,),
    )
    report = registry.report(
        subject="GF(5)^3",
        declared_category="Modules(GF(5)).Free().FinitelyPresented()",
        inherited_obligation_ids=("finite-cardinality",),
    )

    with pytest.raises(KeyError):
        report.obligation_result_by_id("not-an-obligation")
    with pytest.raises(KeyError):
        report.computed_value("cardinality")
    with pytest.raises(KeyError):
        registry.obligation("not-an-obligation")


def test_registry_rejects_unregistered_inherited_obligation() -> None:
    registry = SpecRegistry(
        obligations=(
            SpecObligation(
                id="finite-cardinality",
                title="Finite objects expose their cardinality",
                source="category_specs/sets/subcategories/finite.py",
            ),
        ),
    )

    with pytest.raises(ValueError):
        registry.report(
            subject="GF(5)^3",
            declared_category="Modules(GF(5)).Free().FinitelyPresented()",
            inherited_obligation_ids=("finite-cardinality", "enumerability"),
        )


def test_registry_rejects_duplicate_obligation_providers_and_witnesses() -> None:
    finite_cardinality = SpecObligation(
        id="finite-cardinality",
        title="Finite objects expose their cardinality",
        source="category_specs/sets/subcategories/finite.py",
    )
    first_provider = SpecProvider(
        id="finite-cardinality-methods",
        category="Sets().Finite()",
        provides=("finite-cardinality",),
        source="category_specs/sets/subcategories/finite.py",
    )
    second_provider = SpecProvider(
        id="cartesian-product-cardinality-methods",
        category="Sets().CartesianProducts()",
        provides=("finite-cardinality",),
        source="category_specs/sets/subcategories/constructions/cartesian_product.py",
    )
    first_witness = ConstructionWitness(
        id="finite-product-witness",
        construction="cartesian_power",
        source_category="Sets().Finite()",
        target_category="Sets().Finite()",
        provides=("finite-cardinality",),
        source="category_specs/sets/subcategories/constructions/cartesian_product.py",
    )
    second_witness = ConstructionWitness(
        id="module-carrier-witness",
        construction="free_module_carrier",
        source_category="Modules(GF(5)).Free()",
        target_category="Sets().Finite()",
        provides=("finite-cardinality",),
        source=(
            ".agents/plans/features/"
            "FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/"
            "PLAN-SPEC-CORE-VERTICAL-SLICE"
        ),
    )

    provider_registry = SpecRegistry(
        obligations=(finite_cardinality,),
        providers=(first_provider, second_provider),
    )
    witness_registry = SpecRegistry(
        obligations=(finite_cardinality,),
        witnesses=(first_witness, second_witness),
    )

    with pytest.raises(ValueError):
        provider_registry.report(
            subject="GF(5)^3",
            declared_category="Modules(GF(5)).Free().FinitelyPresented()",
            inherited_obligation_ids=("finite-cardinality",),
        )
    with pytest.raises(ValueError):
        witness_registry.report(
            subject="GF(5)^3",
            declared_category="Modules(GF(5)).Free().FinitelyPresented()",
            inherited_obligation_ids=("finite-cardinality",),
        )


def test_check_result_requires_status_evidence_to_match() -> None:
    obligation = SpecObligation(
        id="finite-cardinality",
        title="Finite objects expose their cardinality",
        source="category_specs/sets/subcategories/finite.py",
    )
    provider = SpecProvider(
        id="finite-cardinality-methods",
        category="Sets().Finite()",
        provides=("finite-cardinality",),
        source="category_specs/sets/subcategories/finite.py",
    )
    witness = ConstructionWitness(
        id="finite-product-witness",
        construction="cartesian_power",
        source_category="Sets().Finite()",
        target_category="Sets().Finite()",
        provides=("finite-cardinality",),
        source="category_specs/sets/subcategories/constructions/cartesian_product.py",
    )

    provider_result = SpecCheckResult(
        status="satisfied_by_provider",
        obligation=obligation,
        provider=provider,
    )
    witness_result = SpecCheckResult(
        status="satisfied_by_witness",
        obligation=obligation,
        witness=witness,
    )
    missing_result = SpecCheckResult(status="missing", obligation=obligation)

    assert provider_result.provider.id == "finite-cardinality-methods"
    assert provider_result.witness is None
    assert witness_result.witness.id == "finite-product-witness"
    assert witness_result.provider is None
    assert missing_result.status == "missing"
    assert missing_result.provider is None
    assert missing_result.witness is None

    with pytest.raises(ValueError):
        SpecCheckResult(status="satisfied_by_provider", obligation=obligation)
    with pytest.raises(ValueError):
        SpecCheckResult(
            status="satisfied_by_witness",
            obligation=obligation,
            provider=provider,
        )
    with pytest.raises(ValueError):
        SpecCheckResult(
            status="missing",
            obligation=obligation,
            witness=witness,
        )
