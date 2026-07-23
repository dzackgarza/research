"""Typed semantic seed is authoritative; DOT is presentation."""

from sage_category_tree_stubs.design_sources import design_paths
from sage_category_tree_stubs.sage_to_stub import SAGE_TO_ENTITY, SAGE_TO_STUB
from sage_category_tree_stubs.semantic_seed import (
    ARROW_KINDS,
    ENTITY_KINDS,
    format_seed_report,
    load_semantic_seed,
    seed_vs_dot_coverage,
)


def test_seed_files_present() -> None:
    paths = design_paths()
    assert paths["semantic_seed"].is_dir()
    assert paths["seed_entities"].is_file()
    assert paths["seed_classifiers"].is_file()
    assert paths["seed_arrows"].is_file()


def test_entity_and_arrow_kinds_are_closed() -> None:
    seed = load_semantic_seed()
    for e in seed.entities:
        assert e["kind"] in ENTITY_KINDS
    for a in seed.arrows:
        assert a["kind"] in ARROW_KINDS


def test_commutative_rings_is_structured_pullback() -> None:
    seed = load_semantic_seed()
    by_id = seed.entity_by_id()
    rings = by_id["cat.commutative_rings"]
    assert rings["kind"] == "derived_category"
    assert rings["definition"]["operation"] == "pullback"
    assert rings["definition"]["over"] == "cat.magmas"
    assert rings["definition"]["right"] == "clf.magmas.commutative"
    assert "CommRings" in rings["aliases"]


def test_algebras_to_rings_is_parameter_dependency_not_forgetful() -> None:
    seed = load_semantic_seed()
    param = [a for a in seed.arrows if a["id"] == "arr.param.algebras_r_base_ring"]
    assert param and param[0]["kind"] == "parameter_dependency"
    rejected = [a for a in seed.arrows if a["id"] == "arr.warn.dot_algebras_to_rings_as_forgetful"]
    assert rejected and rejected[0]["preferred"] is False


def test_division_rings_are_rings_division() -> None:
    seed = load_semantic_seed()
    div = seed.entity_by_id()["cat.division_rings"]
    assert div["definition"]["operation"] == "classifier_application"
    assert div["definition"]["host"] == "cat.rings"
    assert div["definition"]["classifier"] == "clf.division"
    assert div["dot_vertex"] == "DivisionRings = Rings.Division"
    assert div["definition"].get("classifier") != "clf.magmas.inverse"


def test_finite_classifier_has_leg_and_graded_is_distinct_record() -> None:
    seed = load_semantic_seed()
    by_clf = {c["id"]: c for c in seed.classifiers}
    assert by_clf["clf.sets.finite"]["leg_arrow_id"] == "arr.clf.sets.finite"
    assert by_clf["clf.sets.graded"]["host_id"] == "cat.sets"
    assert "property" not in by_clf["clf.sets.finite"]
    assert by_clf["clf.algebras_r.graded"]["transport"]["from_classifier_id"] == ("clf.sets.graded")


def test_seed_dot_links_resolve() -> None:
    assert not seed_vs_dot_coverage()


def test_orthogonal_groups_not_category_family() -> None:
    seed = load_semantic_seed()
    og = seed.entity_by_id()["val.orthogonal_groups"]
    assert og["kind"] == "alias"
    assert og["definition"]["operation"] == "construction_value"


def test_format_seed_report_mentions_param_and_coverage() -> None:
    text = format_seed_report()
    assert "parameter" in text.lower()
    assert "DOT coverage: complete" in text


def test_full_dot_vertex_and_solid_edge_coverage() -> None:
    from sage_category_tree_stubs.semantic_seed import (
        full_coverage_findings,
        presentation_only_dot_vertices,
        solid_edges_missing_seed_arrows,
    )

    assert presentation_only_dot_vertices() == []
    assert solid_edges_missing_seed_arrows() == []
    assert not [f for f in full_coverage_findings() if f.kind in {"unseeded_dot_vertex", "unseeded_solid_edge", "dot_vertex_missing"}]


def test_generated_dot_carries_semantic_attrs() -> None:
    from sage_category_tree_stubs.design_sources import NORMALIZED_DOT
    from sage_category_tree_stubs.seed_dot import GENERATED_DOT, write_generated_dot

    path = write_generated_dot(also_presentation=False)
    assert path == GENERATED_DOT
    text = GENERATED_DOT.read_text(encoding="utf-8")
    assert "GENERATED from semantic_seed" in text
    assert 'kind="category_family"' in text
    assert 'id="cat.sets"' in text
    # Factory presentation stays the hand layout, not the generated dump.
    hand = NORMALIZED_DOT.read_text(encoding="utf-8")
    assert "GENERATED from semantic_seed" not in hand


def test_no_named_join_import_leftovers() -> None:
    seed = load_semantic_seed()
    leftovers = [e["id"] for e in seed.entities if isinstance(e.get("definition"), dict) and "Imported from DOT" in str(e["definition"].get("notes", ""))]
    assert leftovers == []


def test_correspondence_targets_are_seed_entity_ids() -> None:
    seed = load_semantic_seed()
    ids = set(seed.entity_by_id())
    for sage, entity_id in SAGE_TO_ENTITY.items():
        assert entity_id in ids, (sage, entity_id)
        entity = seed.entity_by_id()[entity_id]
        definition = entity.get("definition") or {}
        if definition.get("operation") == "construction_value":
            # A destination may be a constructible category with no name, hence no
            # vertex in the curated presentation: `FacadeSets` lands in
            # `Subobjects(Sets)`. Requiring a drawn vertex would force every discovered
            # construction to be named before it could be a target.
            assert entity.get("dot_vertex") is None, (sage, entity_id)
            continue
        assert entity.get("dot_vertex")
        assert SAGE_TO_STUB[sage] == entity["dot_vertex"]


def test_right_modules_are_opposite_ring_substitution() -> None:
    seed = load_semantic_seed()
    right = seed.entity_by_id()["cat.right_modules_r"]
    assert right["definition"]["operation"] == "parameter_substitution"
    assert right["definition"]["substitute"]["R"] == "R^op"


def test_additive_magmas_is_magmas_additive_one_tower() -> None:
    """AdditiveMagmas = Magmas.Additive ⊂ Magmas (not a Sets sibling root)."""
    seed = load_semantic_seed()
    add = seed.entity_by_id()["cat.additive_magmas"]
    assert add["kind"] == "derived_category"
    assert add["definition"]["operation"] == "classifier_application"
    assert add["definition"]["host"] == "cat.magmas"
    assert add["definition"]["classifier"] == "clf.magmas.additive"
    preferred = [a for a in seed.arrows if a["source"] == "cat.additive_magmas" and a.get("preferred", True)]
    assert any(a["target"] == "cat.magmas" for a in preferred)
    assert not any(a["target"] == "cat.sets" and a.get("preferred", True) for a in preferred)

    assert not any(c["id"].startswith("clf.additive_magmas.") for c in seed.classifiers)

    # Additive tower reuses Magmas law classifiers with along=additive_operation.
    for eid, clf in (
        ("cat.additive_semigroups", "clf.magmas.associative"),
        ("cat.additive_monoids", "clf.magmas.associative"),
        ("cat.additive_groups", "clf.magmas.associative"),
    ):
        d = seed.entity_by_id()[eid]["definition"]
        assert d.get("along") == "additive_operation"
        clfs = d.get("classifiers") or [d.get("classifier")]
        assert clf in clfs

    ab = seed.entity_by_id()["cat.additive_abelian_groups"]["definition"]
    assert ab["right"] == "clf.magmas.commutative"
    assert ab["over"] == "cat.magmas"
    assert ab.get("along") == "additive_operation"


def _lean_seed_manifest() -> dict:
    import json
    from pathlib import Path

    from sage_category_tree_stubs.design_sources import DESIGN_ROOT

    path = (
        DESIGN_ROOT.parent.parent
        / "lean_category_dsl_spike"
        / "NormalizedCategoryGraph"
        / "Spec"
        / "seed_manifest.json"
    )
    assert path.is_file(), path
    return json.loads(path.read_text(encoding="utf-8"))


def test_lean_seed_has_no_functor_or_classifier_in_category_position() -> None:
    """``CategoryExpr.reference`` holds a ``CategoryId``.

    Emitting a ``fun.*`` or ``clf.*`` id there makes a typed importer search for a
    category that does not exist instead of reading a pullback or a construction.
    """
    manifest = _lean_seed_manifest()
    found: list[str] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if node.get("tag") == "reference" and str(node.get("id", "")).startswith(("fun.", "clf.")):
                found.append(str(node["id"]))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(manifest)
    assert not found, f"non-category ids in category-reference position: {sorted(set(found))}"


def test_lean_seed_structural_ports_have_present_endpoints() -> None:
    """A port whose endpoint is not a manifest category is a dangling structural map."""
    manifest = _lean_seed_manifest()
    present = {c["id"] for c in manifest["categories"]} | {o["id"] for o in manifest["opaqueCategories"]}
    ports = manifest["structuralPorts"]
    assert ports, "no structural ports exported"
    dangling = [p["id"] for p in ports if p["source"] not in present or p["target"] not in present]
    assert not dangling, f"structural ports with absent endpoints: {dangling[:5]}"
