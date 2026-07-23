"""Three-manifest architecture: observed Sage + normalized + correspondence."""

import pytest
from pathlib import Path

from sage_category_tree_stubs.design_sources import design_paths
from sage_category_tree_stubs.manifests import (
    format_manifests_report,
    load_mapping,
    load_observed,
    validate_three_manifests,
)
from sage_category_tree_stubs.mapping_build import build_mapping
from sage_category_tree_stubs.observed_build import build_observed_from_inventory
from sage_category_tree_stubs.observed_diff import diff_observed


def test_manifest_files_present() -> None:
    paths = design_paths()
    assert paths["sage_observed"].is_file()
    assert paths["sage_mapping"].is_file()
    assert paths["normalized_manifest"].is_dir()
    assert paths["routes"].is_file()


def test_observed_is_empirical_snapshot() -> None:
    obs = load_observed()
    assert obs["manifest"]["schema_version"] == 1
    assert obs["manifest"]["sage_version"]
    assert len(obs["categories"]) >= 200
    assert len(obs["axioms"]) >= 40
    assert len(obs["constructions"]) >= 10
    for ax in obs["axioms"]:
        assert "property" not in ax
        assert "structure" not in ax
        assert "stuff" not in ax
    assert sum(len(cat["defined_constructions"]) for cat in obs["categories"]) > 0


def test_composed_parents_resolve_to_ids() -> None:
    obs = load_observed()
    unresolved = []
    for cat in obs["categories"]:
        for edge in cat.get("immediate_supercategories") or []:
            if not edge.get("target"):
                unresolved.append((cat.get("qualname"), edge.get("sage_name")))
    assert unresolved == [], unresolved[:10]


def test_additive_commutative_is_constructible_tower() -> None:
    from sage_category_tree_stubs.composed_identity import normalized_reading
    from sage_category_tree_stubs.constructibility import (
        ClassifierRequest,
        build_sketch,
        check_constructibility,
        check_requests,
    )

    assert normalized_reading("AdditiveMagmas.AdditiveCommutative") == "Magmas.Additive.Commutative"
    # Principled form: Magmas + {Additive, Commutative} — no named Magmas.Additive.Commutative node
    sketch = build_sketch()
    flat = check_requests(
        "cat.magmas",
        [
            ClassifierRequest("clf.magmas.additive", occurrence_id="add"),
            ClassifierRequest("clf.magmas.commutative", occurrence_id="comm"),
        ],
        sketch=sketch,
    )
    assert flat.ok, flat.detail
    assert set(flat.certificate) == {"add", "comm"}

    result = check_constructibility("AdditiveMagmas.AdditiveCommutative")
    assert result.ok, result.detail
    assert result.base_id == "cat.magmas"
    assert "clf.magmas.additive" in result.classifier_ids
    assert "clf.magmas.commutative" in result.classifier_ids
    assert not any(cid.startswith("clf.additive_magmas.") for cid in result.classifier_ids)

    mapping = load_mapping()
    row = next(r for r in mapping["category_mappings"] if r.get("source_sage_name") == "AdditiveMagmas.AdditiveCommutative")
    assert row["relation"] == "constructible"
    assert row["normalized_reading"] == "Magmas.Additive.Commutative"
    assert row["construction"]["ok"] is True
    assert "clf.magmas.commutative" in row["construction"]["classifiers"]
    assert not any(c.startswith("clf.additive_magmas.") for c in row["construction"]["classifiers"])


def test_finite_available_via_path_to_sets() -> None:
    from sage_category_tree_stubs.constructibility import ClassifierRequest, check_requests

    # Rings.Finite via Rings → Sets
    r = check_requests(
        "cat.rings",
        [ClassifierRequest("clf.sets.finite", occurrence_id="fin")],
    )
    assert r.ok, r.detail


def test_rings_commutative_requires_multiplicative_route() -> None:
    """Rings has multiple Magmas ports; Commutative needs along=."""
    from sage_category_tree_stubs.constructibility import (
        ClassifierRequest,
        build_sketch,
        check_requests,
    )

    sketch = build_sketch()
    ambiguous = check_requests(
        "cat.rings",
        [ClassifierRequest("clf.magmas.commutative", occurrence_id="c")],
        sketch=sketch,
    )
    assert ambiguous.status == "AMBIGUOUS", ambiguous

    ok = check_requests(
        "cat.rings",
        [
            ClassifierRequest(
                "clf.magmas.commutative",
                along="multiplicative_operation",
                occurrence_id="c",
            )
        ],
        sketch=sketch,
    )
    assert ok.ok, ok.detail


def test_mapping_targets_normalized_ids_only() -> None:
    mapping = load_mapping()
    assert mapping["manifest"]["schema_version"] == 1
    for row in mapping["category_mappings"]:
        assert row["relation"] in {
            "exact",
            "presentation_alias",
            "canonical_equivalence",
            "corrected_embedding",
            "constructible",
            "unsupported",
            "removed",
        }
        tgt = row["target"]
        if tgt is None:
            assert row["relation"] == "unsupported"
            continue
        assert tgt.startswith("cat.") or tgt.startswith("clf.") or tgt.startswith("val.")


def test_mapping_does_not_restate_pullbacks() -> None:
    text = Path(design_paths()["sage_mapping"]).read_text(encoding="utf-8")
    assert "operation: pullback" not in text
    assert "left: fun." not in text


def test_axiom_and_construction_census_mapped() -> None:
    obs = load_observed()
    mapping = load_mapping()
    ax_sources = {r["source"] for r in mapping["axiom_mappings"]}
    for ax in obs["axioms"]:
        assert ax["id"] in ax_sources
    cons_sources = {r["source"] for r in mapping["construction_mappings"]}
    for cons in obs["constructions"]:
        assert cons["id"] in cons_sources


def test_validate_three_manifests_hygiene_clean() -> None:
    findings = validate_three_manifests(require_full_parity=False)
    assert findings == [], findings


def test_parity_mode_reports_unsupported() -> None:
    findings = validate_three_manifests(require_full_parity=True)
    kinds = {f.kind for f in findings}
    assert "unsupported_mapping" in kinds


def test_format_manifests_report() -> None:
    text = format_manifests_report()
    assert "observed categories" in text
    assert "category mappings" in text
    assert "Category mapping relations" in text


def test_build_observed_deterministic_counts() -> None:
    a = build_observed_from_inventory()
    b = build_observed_from_inventory()
    assert len(a["categories"]) == len(b["categories"])
    assert len(a["axioms"]) == len(b["axioms"])


def test_build_mapping_includes_finite_axiom_from_authored() -> None:
    mapping = build_mapping()
    finite = [r for r in mapping["axiom_mappings"] if r.get("source_sage_name") == "Finite"]
    assert finite
    assert finite[0]["target"] == "clf.sets.finite"
    assert finite[0]["least_normalized_host"] == "cat.sets"


def test_axiom_classifier_resolution_respects_the_authored_least_host() -> None:
    mapping = build_mapping()
    by_name = {row["source_sage_name"]: row for row in mapping["axiom_mappings"]}
    assert by_name["FinitelyGeneratedAsMagma"]["target"] == "clf.magmas.finitelygenerated"
    assert by_name["FinitelyGeneratedAsLambdaBracketAlgebra"]["target"] == "clf.finitelygenerated_lambdabracket"


def test_authored_public_ledger_fully_covered_and_constructible() -> None:
    """Every public authored Sage category is exact/constructible (no seed gaps)."""
    from sage_category_tree_stubs.authored_mapping import load_authored_manifest

    authored = load_authored_manifest()
    auth_names = {r["source"]["name"] for r in authored["category_mappings"]}
    mapping = load_mapping()
    by_name = {r["source_sage_name"]: r for r in mapping["category_mappings"] if r.get("source_sage_name") in auth_names}
    assert set(by_name) == auth_names
    allowed_rel = {
        "exact",
        "constructible",
        "presentation_alias",
        "removed",
        "corrected_embedding",
    }
    for name, row in by_name.items():
        assert row["relation"] in allowed_rel, (name, row["relation"])
        assert row["relation"] != "unsupported", name
        construction = row.get("construction") or {}
        assert "could not parse" not in str(construction), name
        assert "MISSING_SEED" not in str(construction), name


def test_authored_specimens_constructible() -> None:
    mapping = load_mapping()
    by_name = {r["source_sage_name"]: r for r in mapping["category_mappings"]}

    additive = by_name["AdditiveMagmas"]
    assert additive["relation"] == "constructible"
    assert additive["construction"]["ok"] is True
    assert "clf.magmas.additive" in additive["construction"]["classifiers"]

    crings = by_name["CommutativeRings"]
    assert crings["relation"] == "constructible"
    assert crings["construction"]["ok"] is True
    assert "clf.magmas.commutative" in crings["construction"]["classifiers"]
    routes = crings["construction"].get("authored_routes") or []
    assert any((r.get("support_route") or "").endswith("multiplicative") or r.get("along") == "multiplicative_operation" for r in routes)

    finite_groups = by_name["FiniteGroups"]
    assert finite_groups["relation"] == "constructible"
    assert finite_groups["construction"]["ok"] is True


def test_authored_nonpublic_dispositions_present() -> None:
    mapping = load_mapping()
    nonpub = mapping.get("nonpublic_dispositions") or []
    assert len(nonpub) >= 40
    assert any(r.get("sage_class") for r in nonpub)


def test_observed_diff_identity_empty() -> None:
    obs = load_observed()
    diff = diff_observed(obs, obs)
    assert diff["categories_added"] == []
    assert diff["categories_removed"] == []
    assert diff["immediate_supercategory_changes"] == []


def test_join_view_dots_exist() -> None:
    sage = design_paths()["sage_observed"].parent
    for name in (
        "correspondence.dot",
        "observed_parents.dot",
            ):
        assert (sage / name).is_file(), name


def test_requirement_manifest_matches_the_live_ledger() -> None:
    """The committed demand must be the ledger's demand.

    A stale manifest is worse than none: lean-lattices would validate a release
    against requirements this ledger no longer states.
    """
    from sage_category_tree_stubs.requirement_manifest import check_requirement_manifest

    assert check_requirement_manifest() == []


def test_requirement_extraction_rejects_an_incomplete_ledger() -> None:
    """A row that lost its classifier host must fail extraction, not drop silently."""
    import copy

    from sage_category_tree_stubs.requirement_manifest import (
        StaleExtractionError,
        _category_mapping_requirements,
        build_requirement_manifest,
    )

    ledger = build_requirement_manifest()
    assert ledger["coverage"]["public_rows"] == 179
    assert ledger["coverage"]["requirements"] > 0

    row = {
        "source": {"name": "Fixture"},
        "normalized": {
            "base_id": "cat.sets",
            "classifier_applications": [{"order": 1, "classifier_id": "clf.sets.finite"}],
            "target_expression": "Sets.Finite",
            "target_id": "cat_expr.sets_finite",
        },
    }
    try:
        _category_mapping_requirements(copy.deepcopy(row))
    except StaleExtractionError as exc:
        assert "least host" in str(exc)
    else:
        raise AssertionError("a classifier application with no least host was accepted")


def test_axiom_dispositions_separate_rulings_from_gaps() -> None:
    """A decided exclusion is a ruling, not a missing capability.

    The crosswalk records, per axiom, whether a normalized classifier is owed:
    doctest-only tokens, engineering-only mechanisms, construction-owned axioms
    and deliberately un-globalized tokens are settled. Counting them as pending
    inflates the parity gap with work nobody intends to do.
    """
    from sage_category_tree_stubs.manifests import AXIOM_DISPOSITIONS

    mapping = build_mapping()
    rows = {r["source_sage_name"]: r for r in mapping["axiom_mappings"]}

    for row in mapping["axiom_mappings"]:
        assert row["disposition"] in AXIOM_DISPOSITIONS, row

    assert rows["Facade"]["disposition"] == "excluded_engineering"
    assert rows["Blue"]["disposition"] == "excluded_test_only"
    assert rows["Flying"]["disposition"] == "excluded_test_only"
    assert rows["Endset"]["disposition"] == "construction_owned"
    assert rows["Connected"]["disposition"] == "split_by_host"


def test_axiom_classifiers_are_not_duplicated_across_ids() -> None:
    """Minting a host-qualified id for a classifier the seed already hosts would
    split one piece of mathematics across two stable ids."""
    from sage_category_tree_stubs.design_sources import DESIGN_ROOT
    from sage_category_tree_stubs.design_sources import load_json

    classifiers = load_json(
        DESIGN_ROOT / "normalized_category_graph" / "semantic_seed" / "classifiers.json"
    )["classifiers"]
    seen: dict[tuple[str, str], list[str]] = {}
    for c in classifiers:
        key = (str(c["name"]).lower(), str(c.get("host_id")))
        seen.setdefault(key, []).append(c["id"])

    mapping = build_mapping()
    targets = {r["target"] for r in mapping["axiom_mappings"] if r.get("target")}
    for key, ids in seen.items():
        if len(ids) > 1 and len(targets.intersection(ids)) > 1:
            raise AssertionError(f"axiom surface resolves {key} to several ids: {ids}")


def test_committed_artifacts_match_a_fresh_build() -> None:
    """Regenerating must not change the committed artifacts.

    A generated artifact that always differs from its generator cannot be trusted:
    a stale one looks exactly like a fresh one, so a checked-in mapping can claim
    coverage the current code no longer produces.
    """
    import json

    from sage_category_tree_stubs.design_sources import DESIGN_ROOT, load_json
    from sage_category_tree_stubs.observed_build import build_observed_from_inventory

    committed = load_json(DESIGN_ROOT / "sage" / "observed.json")
    fresh = build_observed_from_inventory()
    assert committed["manifest"]["generated_at"] == fresh["manifest"]["generated_at"], (
        "observed.json is not reproducible: its timestamp moves on every rebuild"
    )
    assert json.dumps(committed, sort_keys=True) == json.dumps(fresh, sort_keys=True), (
        "committed observed.json differs from a fresh build of the pinned inventory"
    )

    live = build_mapping()
    committed_mapping = load_mapping()
    assert committed_mapping["category_mappings"] == live["category_mappings"], (
        "committed mapping.yaml category mappings differ from a fresh build"
    )
    assert committed_mapping["axiom_mappings"] == live["axiom_mappings"], (
        "committed mapping.yaml axiom dispositions differ from a fresh build"
    )


def test_no_sage_category_is_excluded_as_non_mathematical() -> None:
    """Every named Sage category has a destination.

    Each entry once parked here turned out to have a formalization that was simply
    not looked for: a facade parent declares monomorphisms in Sets and lands in
    `Subobjects(Sets)`; `Objects()` is the coslice under the terminal category, since
    an object of C is a point `* -> C`; `LieGroups` and the reflection/Coxeter join are
    ordinary mathematics behind awkward Sage names. An exclusion bucket that can be
    filled silently is where unfound mathematics accumulates, so it stays empty and
    adding to it requires stating why no destination exists.
    """
    from sage_category_tree_stubs.capability import excluded_as_non_mathematical, sigma

    assert excluded_as_non_mathematical() == {}
    s = sigma()
    for name in ("FacadeSets", "Objects", "LieGroups", "ComplexReflectionOrGeneralizedCoxeterGroups"):
        assert s.get(name), f"{name} has no destination"
    assert s["FacadeSets"].expression == "Subobjects(Sets)"
    assert s["Objects"].expression == "Coslices(Cat_1)"


def test_a_refinement_never_grants_algorithms_to_its_base() -> None:
    """The direction invariant: algorithms flow along forgetting only.

    A plain module must not receive grading algorithms. Making one graded is an
    explicit lift -- a named section of the grading fiber -- not something method
    inheritance supplies.
    """
    from sage_category_tree_stubs.capability import providers_for, sigma

    s = sigma()
    graded, plain = s.get("GradedModules"), s.get("Modules")
    assert graded and plain, "GradedModules or Modules has no destination"
    assert graded != plain, f"GradedModules and Modules share destination {graded}"

    for names in providers_for(plain).values():
        assert "GradedModules" not in names, "a plain module was offered graded-module algorithms"


def test_a_refinement_reaches_its_base() -> None:
    """A graded module is a module, so it may use module algorithms.

    This holds only because parameters are compared by canonical entity id: the two
    rows spell the parameter category `R : CommutativeRings` and
    `R : CommutativeRings (intended Sage semantics)`, and resolve through the alias
    `cat.commutativerings` to `cat.commutative_rings`.
    """
    from sage_category_tree_stubs.capability import providers_for, sigma

    graded = sigma()["GradedModules"]
    assert any("Modules" in names for names in providers_for(graded).values())


def test_parameter_constraints_are_compared_by_identifier() -> None:
    """Destinations must not be split or merged on the spelling of a constraint."""
    from sage_category_tree_stubs.capability import sigma

    s = sigma()
    assert s["Modules"].parameters == s["GradedModules"].parameters
    assert s["LeftModules"].parameters != s["Modules"].parameters
    assert s["RingIdeals"].parameters != s["CommutativeRingIdeals"].parameters
