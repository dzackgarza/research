"""Explicit exception ledger for Sage ↪ 𝒢 embedding (not silent remaps).

Static source: ``design/sage_to_normalized_map/correspondence.json`` (``exceptions`` key).

Kinds (comparison-frame §8):

- ``alias`` — Python/Sage name that is not a distinct semantic entity
- ``incorrect_parent`` — Sage records a parent that 𝒢 rejects; edge maps to a
  composite or is waived with evidence
- ``transitional_name`` — Sage name that will be replaced (e.g. MagmaticAlgebras)
- ``version_artifact`` — version-/export-dependent surface
- ``composite_edge`` — Sage immediate edge realizes a non-trivial path in 𝒢
- ``parameterization`` — base-ring / family specialization mismatch in harnesses

Nothing here is discarded silently: every entry is inspectable and counted in
``sage_embed`` reports.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .design_sources import load_correspondence

ExceptionKind = Literal[
    "alias",
    "incorrect_parent",
    "transitional_name",
    "version_artifact",
    "composite_edge",
    "parameterization",
]


@dataclass(frozen=True, slots=True)
class SageEmbedException:
    """One classified departure from a naive name-preserving subgraph embedding."""

    kind: ExceptionKind
    sage_name: str
    detail: str
    # When kind is alias: the primary Sage semantic name this collapses to.
    alias_of: str | None = None
    # Stub/DOT vertex when the exception names a target or edge endpoint.
    stub_vertex: str | None = None
    # For incorrect_parent / composite_edge: Sage parent short name.
    sage_parent: str | None = None


def _load_embed_exceptions() -> tuple[SageEmbedException, ...]:
    rows = load_correspondence()["exceptions"]
    return tuple(
        SageEmbedException(
            kind=row["kind"],
            sage_name=row["sage_name"],
            detail=row["detail"],
            alias_of=row.get("alias_of"),
            stub_vertex=row.get("stub_vertex"),
            sage_parent=row.get("sage_parent"),
        )
        for row in rows
    )


EMBED_EXCEPTIONS: tuple[SageEmbedException, ...] = _load_embed_exceptions()


def exceptions_by_kind() -> dict[ExceptionKind, tuple[SageEmbedException, ...]]:
    out: dict[ExceptionKind, list[SageEmbedException]] = {}
    for row in EMBED_EXCEPTIONS:
        out.setdefault(row.kind, []).append(row)
    return {k: tuple(v) for k, v in out.items()}


def alias_map() -> dict[str, str]:
    """Sage alias name → primary Sage semantic name."""
    return {row.sage_name: row.alias_of for row in EMBED_EXCEPTIONS if row.kind == "alias" and row.alias_of is not None}


def incorrect_parent_stub_edges() -> frozenset[tuple[str, str]]:
    """Stub-vertex pairs corresponding to ledger incorrect_parent rows."""
    from .sage_to_stub import SAGE_TO_STUB

    out: set[tuple[str, str]] = set()
    for row in EMBED_EXCEPTIONS:
        if row.kind != "incorrect_parent" or row.sage_parent is None:
            continue
        child = SAGE_TO_STUB.get(row.sage_name)
        parent = SAGE_TO_STUB.get(row.sage_parent)
        if child and parent:
            out.add((child, parent))
        if child and row.sage_parent == "VectorSpaces":
            vs = SAGE_TO_STUB.get("VectorSpaces")
            if vs:
                out.add((child, vs))
        if row.sage_name == "Modules" and row.sage_parent == "Bimodules":
            out.add(("Modules(R)", "Bimodules(R)"))
        # FreeModules / ModulesWithBasis are stub named joins, not SAGE_TO_STUB keys
        if row.stub_vertex and row.sage_parent == "VectorSpaces":
            vs = SAGE_TO_STUB.get("VectorSpaces")
            if vs:
                out.add((row.stub_vertex, vs))
    return frozenset(out)


def composite_stub_edges() -> frozenset[tuple[str, str]]:
    """Stub-vertex pairs for ledger ``composite_edge`` rows (axiom→host solidifications)."""
    from .sage_to_stub import SAGE_TO_STUB

    out: set[tuple[str, str]] = set()
    for row in EMBED_EXCEPTIONS:
        if row.kind != "composite_edge" or row.sage_parent is None:
            continue
        child = row.stub_vertex or SAGE_TO_STUB.get(row.sage_name)
        parent = SAGE_TO_STUB.get(row.sage_parent, row.sage_parent)
        if child and parent:
            out.add((child, parent))
    return frozenset(out)


def waived_native_stub_edges() -> frozenset[tuple[str, str]]:
    """All ledger-explained native solid edges that need not have a stub path."""
    return incorrect_parent_stub_edges() | composite_stub_edges()
