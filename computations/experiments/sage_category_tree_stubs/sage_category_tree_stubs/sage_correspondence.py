r"""Versioned Sage ↔ 𝒢 correspondence (the adapter seam).

This module is the **Sage-version correspondence** in the pipeline::

    DSL → 𝒢 → *this layer* → Sage implementations

It does **not** make Sage’s taxonomy authoritative. Canonical meaning lives in
``𝒢`` (``semantic_seed``; DOT is presentation). This layer only:

- maps genuine Sage categories onto unique seed entity ids (resolved to DOT
  vertices for embed tooling);
- records aliases / transitional names / known incorrect parents as ledger rows;
- exposes reverse lookup for routing graph operations to Sage methods later.

When Sage N → N+1 changes parents or names, update this correspondence (and
``exceptions``) — leave mathematical definitions in the seed unless the math
itself changed.

Current Sage surface is whatever this process’s Sage provides; there is not yet
a multi-version registry — ``SAGE_CORRESPONDENCE_VERSION`` is the label for that
future split.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from .design_sources import load_correspondence
from .exceptions import EMBED_EXCEPTIONS, SageEmbedException, alias_map
from .native_research_only import RESEARCH_ONLY_VERTICES
from .sage_to_stub import (
    SAGE_AXIOM_TO_STUB,
    SAGE_TO_ENTITY,
    SAGE_TO_STUB,
    STUB_TO_SAGE,
)

# Label for the correspondence table; bump when maintaining parallel Sage versions.
SAGE_CORRESPONDENCE_VERSION: str = str(
    load_correspondence().get("version_label", "sage-dev-local")
)


@dataclass(frozen=True, slots=True)
class SageCorrespondence:
    """Frozen view of one Sage-version map into ``𝒢``."""

    version: str
    sage_to_entity: Mapping[str, str]
    sage_to_graph: Mapping[str, str]
    graph_to_sage: Mapping[str, str]
    axiom_sage_to_graph: Mapping[str, str]
    aliases: Mapping[str, str]
    research_only: frozenset[str]
    exceptions: tuple[SageEmbedException, ...]

    def entity_id(self, sage_name: str) -> str | None:
        """Semantic seed entity id for a Sage short name, or None if unmapped."""
        if sage_name in self.aliases:
            sage_name = self.aliases[sage_name]
        return self.sage_to_entity.get(sage_name)

    def graph_vertex(self, sage_name: str) -> str | None:
        """Presentation DOT vertex for a Sage short name, or None if unmapped."""
        if sage_name in self.aliases:
            sage_name = self.aliases[sage_name]
        return self.sage_to_graph.get(sage_name)

    def sage_name(self, graph_vertex: str) -> str | None:
        """Preferred Sage short name for a presentation vertex, if any."""
        return self.graph_to_sage.get(graph_vertex)


def current_sage_correspondence() -> SageCorrespondence:
    """Correspondence for the Sage this process is running."""
    return SageCorrespondence(
        version=SAGE_CORRESPONDENCE_VERSION,
        sage_to_entity=SAGE_TO_ENTITY,
        sage_to_graph=SAGE_TO_STUB,
        graph_to_sage=STUB_TO_SAGE,
        axiom_sage_to_graph=SAGE_AXIOM_TO_STUB,
        aliases=alias_map(),
        research_only=RESEARCH_ONLY_VERTICES,
        exceptions=EMBED_EXCEPTIONS,
    )


def route_summary(sage_name: str) -> str:
    """Human-readable one-liner: Sage name → 𝒢 vertex (or unmapped)."""
    corr = current_sage_correspondence()
    if sage_name in corr.aliases:
        primary = corr.aliases[sage_name]
        target = corr.graph_vertex(primary)
        return f"{sage_name} (alias of {primary}) ↦ {target}"
    target = corr.graph_vertex(sage_name)
    if target is None:
        return f"{sage_name} ↦ ∅ (unmapped)"
    return f"{sage_name} ↦ {target}"
