"""Three-layer naming observability (identity / standard name / classifier)."""

from sage_category_tree_stubs.naming import (
    CANONICAL_IDENTITIES,
    format_naming_report,
    identity_by_sage_alias,
    naming_report,
    parse_named_presentation,
    presentations_from_graph,
)


def test_named_join_splits_standard_name_and_classifier() -> None:
    p = parse_named_presentation("AbelianGroups = Groups.Commutative")
    assert p is not None
    assert p.standard_name == "AbelianGroups"
    assert p.classifier == "Groups.Commutative"
    assert p.host == "Groups"


def test_presentations_include_groups_ladder() -> None:
    by_name = {p.standard_name: p for p in presentations_from_graph()}
    assert by_name["Semigroups"].classifier == "Magmas.Associative"
    assert by_name["Groups"].classifier == "Magmas.Associative.Unital.Inverse"
    assert by_name["AbelianGroups"].classifier == "Groups.Commutative"


def test_finite_rings_and_fields_are_pullbacks_not_sets_finite() -> None:
    """Finite* are standard names for Rings.Finite / Fields.Finite."""
    by_name = {p.standard_name: p for p in presentations_from_graph()}
    assert by_name["FiniteRings"].classifier == "Rings.Finite"
    assert by_name["FiniteFields"].classifier == "Fields.Finite"
    report = naming_report()
    blocking = [f for f in report.findings if f.kind == "wrong_definition_host"]
    assert not any("FiniteRings" in f.subject or "FiniteFields" in f.subject for f in blocking)
    assert not any(f.kind == "shared_classifier_collision" and f.subject == "Sets.Finite" for f in report.findings)


def test_algebra_classifiers_do_not_collide_with_magma_ladder() -> None:
    by_name = {p.standard_name: p for p in presentations_from_graph()}
    assert by_name["AssociativeAlgebras"].classifier == "Algebras.Associative"
    assert by_name["UnitalAlgebras"].classifier == "Algebras.Associative.Unital"
    assert by_name["Semigroups"].classifier == "Magmas.Associative"
    assert by_name["DGAs"].classifier == "UnitalAlgebras.Differential"
    assert by_name["NonUnitalDGAs"].classifier == "Algebras.Differential"
    report = naming_report()
    collisions = {f.subject for f in report.findings if f.kind == "shared_classifier_collision"}
    assert "Magmas.Associative" not in collisions
    assert "Magmas.Associative.Unital" not in collisions
    assert "Algebras.Differential" not in collisions


def test_sage_alias_is_metadata_not_identity() -> None:
    aliases = identity_by_sage_alias()
    assert aliases["GradedAlgebras"].classifier == "Algebras(R).Graded"
    assert aliases["MagmaticAlgebras"].standard_name == "Algebras(R)"
    assert aliases["CommutativeAdditiveGroups"].standard_name == "AbelianGroups"


def test_abelian_groups_uses_preferred_groups_commutative() -> None:
    report = naming_report()
    expanded = [f for f in report.findings if f.kind == "expanded_classifier" and "AbelianGroups" in f.subject]
    assert not expanded
    by_name = {p.standard_name: p for p in presentations_from_graph()}
    assert by_name["AbelianGroups"].classifier == "Groups.Commutative"


def test_chosen_structure_classifiers_are_flagged_informationally() -> None:
    report = naming_report()
    kinds = {f.kind for f in report.findings}
    assert "chosen_structure_classifier" in kinds
    graded = [f for f in report.findings if f.kind == "chosen_structure_classifier" and "Graded" in (f.subject + str(f.observed))]
    assert graded


def test_naming_report_blocking_cleared_for_known_fixes() -> None:
    report = naming_report()
    assert report.blocking_ok is True
    text = format_naming_report(report)
    assert "wrong_definition_host" not in text or "BLOCKING" not in text


def test_canonical_ledger_nonempty() -> None:
    assert len(CANONICAL_IDENTITIES) >= 10
