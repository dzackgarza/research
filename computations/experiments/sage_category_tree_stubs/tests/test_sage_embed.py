"""Observability for Sage ↪ 𝒢 embedding (bijection frame)."""

from sage_category_tree_stubs.exceptions import (
    EMBED_EXCEPTIONS,
    alias_map,
    incorrect_parent_stub_edges,
)
from sage_category_tree_stubs.sage_embed import (
    embedding_report,
    format_embedding_report,
    full_embedding_report,
    semantic_sage_names,
    vertex_in_graph,
)
from sage_category_tree_stubs.sage_to_stub import SAGE_TO_STUB


def test_alias_map_excludes_aliases_from_semantic_names() -> None:
    aliases = alias_map()
    assert "CommutativeAdditiveSemigroups" in aliases
    semantic = semantic_sage_names()
    assert "CommutativeAdditiveSemigroups" not in semantic
    assert "AdditiveSemigroups" in semantic
    assert "MagmaticAlgebras" in semantic
    assert "Algebras" in semantic


def test_ledger_has_incorrect_parent_for_modules_bimodules() -> None:
    edges = incorrect_parent_stub_edges()
    assert ("Modules(R)", "Bimodules(R)") in edges
    assert any(e.kind == "incorrect_parent" and e.sage_name == "Modules" for e in EMBED_EXCEPTIONS)


def test_graded_algebras_target_is_in_graph() -> None:
    """GradedAlgebras ↦ Algebras(R).Graded pullback is present in 𝒢."""
    report = embedding_report()
    missing = dict(report.missing_targets)
    assert "GradedAlgebras" not in missing
    assert vertex_in_graph("Algebras(R).Graded")
    assert SAGE_TO_STUB["GradedAlgebras"] == "Algebras(R).Graded"


def test_embedding_report_no_magmatic_algebras_collapse_onto_graded() -> None:
    """MagmaticAlgebras and GradedAlgebras must not share a target (injectivity)."""
    report = embedding_report()
    by_sage = {s: t for s, t in SAGE_TO_STUB.items() if s in semantic_sage_names()}
    assert by_sage["MagmaticAlgebras"] != by_sage["GradedAlgebras"]
    for collapse in report.collapses:
        assert "MagmaticAlgebras" not in collapse.sage_names or "GradedAlgebras" not in (collapse.sage_names)


def test_magmatic_and_unital_algebras_are_distinct_targets() -> None:
    assert SAGE_TO_STUB["MagmaticAlgebras"] == "Algebras(R)"
    assert SAGE_TO_STUB["Algebras"] == "UnitalAlgebras = Algebras.Associative.Unital"
    report = embedding_report()
    assert ("MagmaticAlgebras", "Algebras(R)") not in [(s, t) for s, t in report.missing_targets if s == "MagmaticAlgebras"]
    assert vertex_in_graph("Algebras(R)")
    assert vertex_in_graph("UnitalAlgebras = Algebras.Associative.Unital")


def test_format_embedding_report_runs() -> None:
    text = format_embedding_report(embedding_report())
    assert "Sage" in text
    assert "bijection_ok" in text


def test_full_report_runs() -> None:
    report = full_embedding_report()
    assert report.semantic_sage_count >= 20
    assert "alias" in report.exception_counts
    assert "incorrect_parent" in report.exception_counts
    assert "composite_edge" in report.exception_counts
    d = report.to_dict()
    assert d["bijection_ok"] is True
    assert not report.missing_targets
    assert not report.collapses


def test_axiom_host_solidifications_are_ledger_explained_not_unexplained() -> None:
    """Native Host.Axiom → Host edges live in the ledger, not as silent remaps."""
    from sage_category_tree_stubs.exceptions import composite_stub_edges

    edges = composite_stub_edges()
    assert ("Sets.Finite", "Sets") in edges
    assert ("Magmas.Additive", "Sets") in edges
    report = full_embedding_report()
    unexplained = set(report.unexplained_native_edges)
    assert ("Sets.Finite", "Sets") not in unexplained
    assert ("Magmas.Additive", "Sets") not in unexplained
    explained = set(report.explained_incorrect_parents)
    assert ("Sets.Finite", "Sets") in explained or ("Sets.Finite", "Sets") in edges
