r"""Architectural layers for the category-graph spike.

Purpose: **decoupling**, not a wholesale Sage rewrite.

Pipeline::

    DSL mathematics
        → normalized category graph 𝒢
        → Sage-version correspondence
        → existing Sage implementations

Three manifests (see ``design/LAYOUT``): observed Sage @ *v*, normalized ``𝒢``,
and reviewed correspondence. Graphviz is generated from their join. Sage is an
execution backend; its category graph is a *marked compatibility image* inside
``𝒢``, not the foundation the DSL inherits.

Module map
----------
- **𝒢 (stable mathematics):** ``design/normalized/manifest/`` → semantic_seed,
  ``design/normalized_category_graph/category_parent_graph.dot``,
  ``dot_parse``, ``factory``, ``clusters``, ``axioms``, ``naming``, ``seed_dot``
- **Observed Sage:** ``design/sage/observed.json`` (from ``sage_category_graph/``
  inventory via ``observed_build``)
- **Correspondence:** ``design/sage/mapping.yaml`` (``mapping_build``,
  ``manifests``; reviewed rows load into ``sage_to_stub``); legacy
  ``sage_to_normalized_map/correspondence.json`` for reverse lookup / bootstrap
- **Runtime probe:** ``design/sage/runtime_probe.json`` via ``runtime_probe``
- **Routes (optional):** ``design/routes/routes.yaml``
- **Observability:** ``sage_embed``, ``native_semantics``, ``graph_compare``,
  ``audit``, ``join_views``
- **Presentation:** ``viz``

Sage *v*→*v+1*: regenerate observed, diff, patch mapping only, regen DOT.
Change ``𝒢`` only when the mathematics changes.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Layer:
    """One stage of the DSL → 𝒢 → backend pipeline."""

    name: str
    role: str
    spike_modules: tuple[str, ...]


LAYERS: tuple[Layer, ...] = (
    Layer(
        "dsl",
        "Expressions targeting canonical categories / classifiers / constructions",
        (),  # not in this spike yet
    ),
    Layer(
        "graph",
        "Authoritative normalized category graph 𝒢",
        (
            "design/normalized/manifest/",
            "design/normalized_category_graph/semantic_seed/",
            "design/normalized_category_graph/category_parent_graph.dot",
            "dot_parse",
            "seed_dot",
            "factory",
            "clusters",
            "axioms",
            "naming",
            "semantic_seed",
        ),
    ),
    Layer(
        "sage_correspondence",
        "Observed Sage + reviewed mapping (categories/edges/axioms) ↔ 𝒢",
        (
            "design/sage/observed.json",
            "design/sage/mapping.yaml",
            "design/sage_to_normalized_map/correspondence.json",
            "design/sage_category_graph/",
            "observed_build",
            "mapping_build",
            "manifests",
            "join_views",
            "sage_correspondence",
            "sage_to_stub",
            "native_map",
            "native_research_only",
            "exceptions",
        ),
    ),
    Layer(
        "sage_backend",
        "Existing Sage Category / Parent implementations and algorithms",
        (),  # external
    ),
)


def pipeline_summary() -> str:
    lines = ["DSL → 𝒢 → Sage correspondence → Sage backend"]
    for layer in LAYERS:
        mods = ", ".join(layer.spike_modules) if layer.spike_modules else "(external / future)"
        lines.append(f"  [{layer.name}] {layer.role}")
        lines.append(f"           modules: {mods}")
    return "\n".join(lines)
