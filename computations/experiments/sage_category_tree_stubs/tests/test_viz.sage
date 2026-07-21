"""Viewer artifact stays synchronized with the DOT source."""

from sage_category_tree_stubs.dot_parse import parse_dot
from sage_category_tree_stubs.viz import rebuild_viewer, viewer_paths


def test_viewer_svg_reflects_current_dot() -> None:
    """Regenerate (idempotent) and require key DOT vertices in the SVG."""
    rebuild_viewer()
    paths = viewer_paths()
    svg = paths["svg"].read_text(encoding="utf-8")
    graph = parse_dot()
    for needle in (
        "Cat_1",
        "Cat_2",
        "CatObject",
        "CatObject.Limits",
        "HomCategories",
        "TensorProducts = CatObject.Monoidal",
        "Monoidal",
        "Manifolds",
        "Algebras(R)",
        "Modules.FiniteRank",
    ):
        assert needle in svg, f"{needle!r} missing from {paths['svg']}"
    assert "Cat_1" in graph.solid_nodes
    assert "Cat" not in graph.solid_nodes
    assert "Products" not in graph.solid_nodes  # plain Products node removed
    assert "CatObject.Products" in graph.axiom_labels
    assert "CatObject.Limits" in graph.axiom_labels
    assert "DifferentiableManifolds" not in graph.solid_nodes
    html = paths["html"].read_text(encoding="utf-8")
    assert "category_parent_graph.svg?v=" in html
