"""Paths and loaders for the three design static sources.

See ``design/LAYOUT``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_SPIKE_ROOT = Path(__file__).resolve().parent.parent
DESIGN_ROOT = _SPIKE_ROOT / "design"

SAGE_CATEGORY_GRAPH_DIR = DESIGN_ROOT / "sage_category_graph"
NORMALIZED_CATEGORY_GRAPH_DIR = DESIGN_ROOT / "normalized_category_graph"
SAGE_TO_NORMALIZED_MAP_DIR = DESIGN_ROOT / "sage_to_normalized_map"
SEMANTIC_SEED_DIR = NORMALIZED_CATEGORY_GRAPH_DIR / "semantic_seed"
SAGE_OBSERVED_JSON = DESIGN_ROOT / "sage" / "observed.json"
SAGE_MAPPING_YAML = DESIGN_ROOT / "sage" / "mapping.yaml"
SAGE_RUNTIME_PROBE_JSON = DESIGN_ROOT / "sage" / "runtime_probe.json"
SAGE_AUTHORED_DIR = DESIGN_ROOT / "sage" / "authored"
SAGE_AUTHORED_MANIFEST = (
    SAGE_AUTHORED_DIR / "sage_normalized_category_mapping_manifest.json"
)
ROUTES_YAML = DESIGN_ROOT / "routes" / "routes.yaml"
NORMALIZED_MANIFEST_DIR = DESIGN_ROOT / "normalized" / "manifest"

NORMALIZED_DOT = NORMALIZED_CATEGORY_GRAPH_DIR / "category_parent_graph.dot"
SAGE_NODES_JSON = SAGE_CATEGORY_GRAPH_DIR / "nodes.json"
CORRESPONDENCE_JSON = SAGE_TO_NORMALIZED_MAP_DIR / "correspondence.json"
SAGE_INVENTORY_DIR = SAGE_CATEGORY_GRAPH_DIR / "inventory"


def design_paths() -> dict[str, Path]:
    return {
        "design_root": DESIGN_ROOT,
        "sage_category_graph": SAGE_CATEGORY_GRAPH_DIR,
        "normalized_category_graph": NORMALIZED_CATEGORY_GRAPH_DIR,
        "sage_to_normalized_map": SAGE_TO_NORMALIZED_MAP_DIR,
        "semantic_seed": SEMANTIC_SEED_DIR,
        "normalized_manifest": NORMALIZED_MANIFEST_DIR,
        "sage_observed": SAGE_OBSERVED_JSON,
        "sage_mapping": SAGE_MAPPING_YAML,
        "sage_runtime_probe": SAGE_RUNTIME_PROBE_JSON,
        "sage_authored": SAGE_AUTHORED_DIR,
        "sage_authored_manifest": SAGE_AUTHORED_MANIFEST,
        "routes": ROUTES_YAML,
        "normalized_dot": NORMALIZED_DOT,
        "sage_nodes_json": SAGE_NODES_JSON,
        "correspondence_json": CORRESPONDENCE_JSON,
        "sage_inventory": SAGE_INVENTORY_DIR,
        "seed_entities": SEMANTIC_SEED_DIR / "entities.json",
        "seed_classifiers": SEMANTIC_SEED_DIR / "classifiers.json",
        "seed_arrows": SEMANTIC_SEED_DIR / "arrows.json",
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_sage_nodes() -> dict[str, Any]:
    data = load_json(SAGE_NODES_JSON)
    assert isinstance(data, dict)
    return data


def load_correspondence() -> dict[str, Any]:
    data = load_json(CORRESPONDENCE_JSON)
    assert isinstance(data, dict)
    return data


def assert_design_sources_present() -> None:
    # runtime_probe is produced by `just manifests-probe`; optional until first probe.
    optional = {"design_root", "sage_runtime_probe", "sage_authored"}
    missing = [
        name
        for name, path in design_paths().items()
        if name not in optional and not path.exists()
    ]
    if missing:
        raise FileNotFoundError(f"design sources missing: {missing}")
