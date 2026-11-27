"""Research-language obligation tests for the category-spec phase."""

from __future__ import annotations

import importlib

importlib.import_module("sage.all")


def test_research_language_obligations_name_required_foundational_vocabulary() -> None:
    language = importlib.import_module("category_specs.spec_core.research_language")

    registry = language.research_language_registry()
    required_ids = registry.required_ids()

    assert required_ids == (
        "sets",
        "rings",
        "modules",
        "hom_end_aut",
        "groups_and_group_refinements",
        "modules_with_forms",
        "lattices",
        "discriminant_forms",
        "orthogonal_complements",
        "embeddings",
        "group_actions_stabilizers_centralizers",
        "schemes_varieties_curves_surfaces",
        "divisors_and_picard_groups",
    )
    assert registry.obligation("groups_and_group_refinements").disposition == "missing_spec"
    assert registry.obligation("schemes_varieties_curves_surfaces").disposition == "deferred"
    assert registry.obligation("divisors_and_picard_groups").disposition == "deferred"


def test_research_language_obligations_all_have_sources_and_next_claims() -> None:
    language = importlib.import_module("category_specs.spec_core.research_language")

    registry = language.research_language_registry()

    assert registry.undisposed_ids() == ()
    assert registry.unanchored_ids() == ()
    assert registry.obligation("modules_with_forms").next_mathematical_claim == (
        "Define modules equipped with bilinear or quadratic forms and their "
        "form-preserving Hom, End, and Aut objects."
    )
