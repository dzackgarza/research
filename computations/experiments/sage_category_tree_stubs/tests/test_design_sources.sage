"""Three static design sources under design/."""

from sage_category_tree_stubs.design_sources import (
    CORRESPONDENCE_JSON,
    NORMALIZED_DOT,
    SAGE_NODES_JSON,
    assert_design_sources_present,
    design_paths,
    load_correspondence,
    load_sage_nodes,
)
from sage_category_tree_stubs.dot_parse import parse_dot
from sage_category_tree_stubs.sage_to_stub import SAGE_TO_STUB


def test_design_sources_present() -> None:
    assert_design_sources_present()
    paths = design_paths()
    assert paths["normalized_dot"].is_file()
    assert paths["correspondence_json"].is_file()
    assert paths["sage_nodes_json"].is_file()
    assert paths["sage_inventory"].is_dir()


def test_normalized_dot_is_design_file() -> None:
    assert NORMALIZED_DOT.name == "category_parent_graph.dot"
    assert "normalized_category_graph" in str(NORMALIZED_DOT)
    graph = parse_dot()
    assert "Sets" in graph.solid_nodes or any("Sets" in n for n in graph.solid_nodes)


def test_correspondence_json_is_loaded_into_sage_to_stub() -> None:
    data = load_correspondence()
    assert data["kind"] == "sage_to_normalized_map"
    assert data["sage_to_graph"]["MagmaticAlgebras"] == "cat.algebras_r"
    assert data.get("target_kind") == "semantic_seed_entity_id"
    assert SAGE_TO_STUB["MagmaticAlgebras"] == "Algebras(R)"
    assert CORRESPONDENCE_JSON.is_file()
    paths = design_paths()
    assert paths["sage_mapping"].is_file()
    assert paths["sage_observed"].is_file()


def test_sage_nodes_cover_inventory_extract() -> None:
    sage = load_sage_nodes()
    assert sage["kind"] == "sage_category_graph"
    assert sage["node_count"] >= 200
    assert len(sage["nodes"]) == sage["node_count"]
    constructors = {n["constructor"] for n in sage["nodes"]}
    assert "Magmas" in constructors or "Sets" in constructors
    assert SAGE_NODES_JSON.is_file()
