"""Auditable Sage ``sage.categories`` → 𝒢 map (correspondence table).

Reviewed surface: ``design/sage/mapping.yaml`` (category_mappings with a
normalized target). Legacy ``design/sage_to_normalized_map/correspondence.json``
remains the bootstrap / reverse-lookup source and must stay consistent with
the reviewed rows.

Targets are **semantic_seed entity ids**; this module resolves them to DOT
presentation vertices for embed / native tooling.

Prefer :mod:`sage_correspondence` for the typed seam.
"""

from __future__ import annotations

import yaml

from .design_sources import DESIGN_ROOT, load_correspondence
from .semantic_seed import load_semantic_seed

_MAPPING_YAML = DESIGN_ROOT / "sage" / "mapping.yaml"
_data = load_correspondence()
_seed = load_semantic_seed()
_entity_by_id = _seed.entity_by_id()


def _resolve_to_dot_vertex(target: str) -> str:
    """Map a seed entity id (or legacy DOT string) to a presentation vertex."""
    seen: set[str] = set()
    cur = target
    while cur not in seen:
        seen.add(cur)
        entity = _entity_by_id.get(cur)
        if entity is None:
            return cur
        vertex = entity.get("dot_vertex")
        if vertex:
            return str(vertex)
        definition = entity.get("definition") or {}
        if definition.get("operation") == "same_as" and definition.get("of"):
            cur = str(definition["of"])
            continue
        return cur
    return target


def _reviewed_sage_to_entity() -> dict[str, str]:
    """Sage short name → seed entity id from reviewed *named* mapping rows.

    ``constructible`` towers are ephemeral and must not enter the named
    Sage↦entity bijection (many towers share one base).
    """
    legacy = dict(_data["sage_to_graph"])
    if not _MAPPING_YAML.is_file():
        return legacy
    mapping = yaml.safe_load(_MAPPING_YAML.read_text(encoding="utf-8")) or {}
    reviewed: dict[str, str] = {}
    # presentation_alias / removed / constructible must not overwrite the
    # named Sage↦entity bijection (aliases share a target by definition).
    named_relations = {
        "exact",
        "canonical_equivalence",
        "corrected_embedding",
    }
    for row in mapping.get("category_mappings", []):
        if row.get("relation") not in named_relations:
            continue
        name = row.get("source_sage_name")
        target = row.get("target")
        if not (name and target and "." not in name):
            continue
        # Opaque authored hosts are constructibility interfaces, not factory
        # presentation vertices — keep them out of SAGE_TO_STUB bijection.
        entity = _entity_by_id.get(target)
        if entity is not None:
            definition = entity.get("definition") or {}
            if definition.get("opaque"):
                continue
        reviewed[name] = target
    return {**legacy, **reviewed}


def _reviewed_axiom_map() -> dict[str, str]:
    """Keep the flat Magmas Additive* → stub axiom map from correspondence."""
    return dict(_data["axiom_sage_to_graph"])


# Sage short name → semantic_seed entity id.
SAGE_TO_ENTITY: dict[str, str] = _reviewed_sage_to_entity()

# Sage short name → stub DOT vertex (presentation; used by embed / native).
SAGE_TO_STUB: dict[str, str] = {sage: _resolve_to_dot_vertex(entity_id) for sage, entity_id in SAGE_TO_ENTITY.items()}

# Sage Additive* axiom name → stub Magmas axiom name (flat registry).
SAGE_AXIOM_TO_STUB: dict[str, str] = _reviewed_axiom_map()

# Stub DOT vertex → preferred Sage short name (for native_instance).
STUB_TO_SAGE: dict[str, str] = {_resolve_to_dot_vertex(entity_id): sage for entity_id, sage in dict(_data["graph_to_sage"]).items()}
