"""DSL → 𝒢 → Sage correspondence architecture (decoupling, not rewrite)."""

from sage_category_tree_stubs.architecture import LAYERS, pipeline_summary
from sage_category_tree_stubs.sage_correspondence import (
    current_sage_correspondence,
    route_summary,
)
from sage_category_tree_stubs.sage_embed import embedding_report


def test_pipeline_layers_name_graph_before_sage_backend() -> None:
    names = [layer.name for layer in LAYERS]
    assert names == ["dsl", "graph", "sage_correspondence", "sage_backend"]
    assert "design/normalized_category_graph/semantic_seed/" in LAYERS[1].spike_modules
    assert "design/sage/mapping.yaml" in LAYERS[2].spike_modules
    assert "design/sage/observed.json" in LAYERS[2].spike_modules


def test_correspondence_routes_magmatic_and_unital_distinctly() -> None:
    corr = current_sage_correspondence()
    assert corr.graph_vertex("MagmaticAlgebras") == "Algebras(R)"
    assert corr.graph_vertex("Algebras") == "UnitalAlgebras = Algebras.Associative.Unital"
    assert corr.graph_vertex("GradedAlgebras") == "Algebras(R).Graded"
    assert corr.graph_vertex("CommutativeAdditiveSemigroups") == (
        "AdditiveSemigroups = Magmas.Additive.Associative"
    )


def test_route_summary_mentions_alias() -> None:
    text = route_summary("CommutativeAdditiveGroups")
    assert "alias" in text
    assert "AdditiveAbelianGroups" in text or "AdditiveGroups" in text


def test_embedding_bijection_holds_under_correspondence() -> None:
    """Backend coverage: every mapped semantic Sage name has a 𝒢 target."""
    report = embedding_report()
    assert report.bijection_ok
    corr = current_sage_correspondence()
    assert corr.version
    assert "𝒢" in pipeline_summary() or "graph" in pipeline_summary()
