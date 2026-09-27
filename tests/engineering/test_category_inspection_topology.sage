"""The topology report distinguishes the selected mathematical complexes."""

from dzack_research.utilities.category_graph import render_topology


def test_triangle_boundary_and_filled_triangle_have_different_homology():
    vertices = {"A", "B", "C"}
    relation = {("A", "B"), ("B", "C"), ("A", "C")}
    graph_report = render_topology(vertices, relation, "graph", 3, False)
    flag_report = render_topology(vertices, relation, "flag", 3, False)
    order_report = render_topology(vertices, relation, "order", 3, False)
    assert "1: Z" in graph_report
    assert "1: 0" in flag_report
    assert "1: 0" in order_report


def test_isolated_category_contributes_a_connected_component():
    report = render_topology({"A", "B", "C"}, {("A", "B")}, "graph", 3, False)
    assert "0: Z x Z" in report
