"""Typed semantic seed for 𝒢 (authoritative; DOT is presentation)."""

from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .design_sources import NORMALIZED_CATEGORY_GRAPH_DIR, load_json
from .dot_parse import DotGraph, parse_dot
from .slugs import short_name

SEMANTIC_SEED_DIR = NORMALIZED_CATEGORY_GRAPH_DIR / "semantic_seed"

ENTITY_KINDS = frozenset(
    {
        "category_family",
        "classifier_domain",
        "derived_category",
        "category_constructor",
        "alias",
    }
)

ARROW_KINDS = frozenset(
    {
        "forgetful",
        "full_inclusion",
        "classifier_leg",
        "pullback_projection",
        "theorem_inclusion",
        "equivalence",
        "construction",
        "parameter_dependency",
    }
)


@dataclass(frozen=True, slots=True)
class SemanticSeed:
    entities: tuple[dict[str, Any], ...]
    classifiers: tuple[dict[str, Any], ...]
    arrows: tuple[dict[str, Any], ...]

    def entity_by_id(self) -> dict[str, dict[str, Any]]:
        return {e["id"]: e for e in self.entities}

    def entities_with_dot_vertex(self) -> dict[str, dict[str, Any]]:
        return {e["dot_vertex"]: e for e in self.entities if e.get("dot_vertex")}


def load_semantic_seed(path: Path | None = None) -> SemanticSeed:
    root = path or SEMANTIC_SEED_DIR
    entities = load_json(root / "entities.json")["entities"]
    classifiers = load_json(root / "classifiers.json")["classifiers"]
    arrows = load_json(root / "arrows.json")["arrows"]
    return SemanticSeed(
        entities=tuple(entities),
        classifiers=tuple(classifiers),
        arrows=tuple(arrows),
    )


@dataclass(frozen=True, slots=True)
class SeedFinding:
    kind: str
    subject: str
    detail: str


def validate_seed(seed: SemanticSeed | None = None) -> list[SeedFinding]:
    """Internal consistency of the typed seed (no DOT required)."""
    seed = seed or load_semantic_seed()
    findings: list[SeedFinding] = []
    ids = {e["id"] for e in seed.entities}
    for e in seed.entities:
        if e["kind"] not in ENTITY_KINDS:
            findings.append(SeedFinding("bad_entity_kind", e["id"], f"unknown kind {e['kind']!r}"))
        if e["kind"] == "derived_category":
            definition = e.get("definition") or {}
            if definition.get("operation") == "pullback":
                for key in ("left", "right", "over"):
                    if key not in definition:
                        findings.append(
                            SeedFinding(
                                "incomplete_pullback",
                                e["id"],
                                f"pullback missing {key}",
                            )
                        )
            if definition.get("operation") == "incomplete":
                findings.append(
                    SeedFinding(
                        "incomplete_definition",
                        e["id"],
                        definition.get("notes") or "marked incomplete",
                    )
                )
    for c in seed.classifiers:
        if c["host_id"] not in ids:
            findings.append(SeedFinding("dangling_host", c["id"], f"host {c['host_id']} missing"))
        if c.get("transport") and "property" in c:
            findings.append(
                SeedFinding(
                    "declared_character",
                    c["id"],
                    "property/structure/stuff must not be stored on classifiers",
                )
            )
    arrow_ids = {a["id"] for a in seed.arrows}
    for a in seed.arrows:
        if a["kind"] not in ARROW_KINDS:
            findings.append(SeedFinding("bad_arrow_kind", a["id"], f"unknown kind {a['kind']!r}"))
        if a["source"] not in ids:
            findings.append(SeedFinding("dangling_arrow_source", a["id"], a["source"]))
        if a["target"] not in ids:
            findings.append(SeedFinding("dangling_arrow_target", a["id"], a["target"]))
    for c in seed.classifiers:
        leg = c.get("leg_arrow_id")
        if leg and leg not in arrow_ids:
            findings.append(SeedFinding("missing_classifier_leg", c["id"], f"leg {leg} absent"))
    return findings


def _semantic_presentation_graph() -> DotGraph:
    """Seed coverage surface: generated DOT (not the factory hand layout)."""
    from .seed_dot import GENERATED_DOT, write_generated_dot

    if not GENERATED_DOT.is_file():
        write_generated_dot(also_presentation=False)
    return parse_dot(GENERATED_DOT)


def _entity_is_opaque(entity: dict[str, Any]) -> bool:
    definition = entity.get("definition") or {}
    return bool(definition.get("opaque"))


def seed_vs_dot_coverage(seed: SemanticSeed | None = None) -> list[SeedFinding]:
    """Where seed claims a non-opaque DOT vertex, require it in generated DOT."""
    seed = seed or load_semantic_seed()
    graph = _semantic_presentation_graph()
    universe = set(graph.solid_nodes) | set(graph.named_joins) | set(graph.axiom_labels)
    findings: list[SeedFinding] = []
    for e in seed.entities:
        if _entity_is_opaque(e):
            # Authored opaque hosts exist in seed for constructibility; they are
            # omitted from generated/factory DOT until a stub cluster exists.
            continue
        vertex = e.get("dot_vertex")
        if not vertex:
            continue
        if vertex not in universe and short_name(vertex) not in {short_name(n) for n in universe}:
            findings.append(
                SeedFinding(
                    "dot_vertex_missing",
                    e["id"],
                    f"seed cites DOT vertex {vertex!r} absent from generated presentation",
                )
            )
    return findings


def presentation_only_dot_vertices() -> list[str]:
    """Generated DOT solid/named/axiom vertices with no seed ``dot_vertex`` link."""
    seed = load_semantic_seed()
    linked = {e["dot_vertex"] for e in seed.entities if e.get("dot_vertex") and not _entity_is_opaque(e)}
    linked_short = {short_name(v) for v in linked}
    graph = _semantic_presentation_graph()
    universe = set(graph.solid_nodes) | set(graph.named_joins) | set(graph.axiom_labels)
    missing: list[str] = []
    for node in sorted(universe, key=str):
        if node in linked or short_name(node) in linked_short:
            continue
        missing.append(node)
    return missing


def presentation_only_dot_sample(limit: int = 20) -> list[str]:
    return presentation_only_dot_vertices()[:limit]


def solid_edges_missing_seed_arrows() -> list[tuple[str, str]]:
    """Solid generated-DOT edges with no preferred seed arrow between entities."""
    seed = load_semantic_seed()
    by_id = seed.entity_by_id()
    by_dot = {v: e for v, e in seed.entities_with_dot_vertex().items() if not _entity_is_opaque(e)}
    pairs: set[tuple[str, str]] = set()
    for a in seed.arrows:
        if not a.get("preferred", True):
            continue
        src_e = by_id.get(a["source"])
        tgt_e = by_id.get(a["target"])
        if not src_e or not tgt_e:
            continue
        if _entity_is_opaque(src_e) or _entity_is_opaque(tgt_e):
            continue
        src_v = src_e.get("dot_vertex")
        tgt_v = tgt_e.get("dot_vertex")
        if src_v and tgt_v and src_v != tgt_v:
            pairs.add((src_v, tgt_v))
    graph = _semantic_presentation_graph()
    missing: list[tuple[str, str]] = []
    for edge in graph.solid_edges:
        if edge.src == edge.tgt:
            continue
        if edge.src not in by_dot or edge.tgt not in by_dot:
            missing.append((edge.src, edge.tgt))
            continue
        if (edge.src, edge.tgt) not in pairs:
            missing.append((edge.src, edge.tgt))
    return missing


def full_coverage_findings(seed: SemanticSeed | None = None) -> list[SeedFinding]:
    """Require seed ↔ generated DOT coverage on non-opaque vertices/edges."""
    seed = seed or load_semantic_seed()
    findings = list(seed_vs_dot_coverage(seed))
    for node in presentation_only_dot_vertices():
        findings.append(
            SeedFinding(
                "unseeded_dot_vertex",
                node,
                "generated presentation vertex has no seed entity",
            )
        )
    for src, tgt in solid_edges_missing_seed_arrows():
        findings.append(
            SeedFinding(
                "unseeded_solid_edge",
                f"{src} -> {tgt}",
                "solid generated edge has no preferred seed arrow",
            )
        )
    return findings


def format_seed_report(
    seed: SemanticSeed | None = None,
    *,
    findings: Iterable[SeedFinding] | None = None,
) -> str:
    seed = seed or load_semantic_seed()
    findings = list(findings) if findings is not None else (validate_seed(seed) + full_coverage_findings(seed))
    lines = [
        "𝒢 semantic seed report (typed manifest; DOT is presentation)",
        f"  entities:     {len(seed.entities)}",
        f"  classifiers:  {len(seed.classifiers)}",
        f"  arrows:       {len(seed.arrows)}",
        f"  findings:     {len(findings)}",
    ]
    by_kind: dict[str, int] = {}
    for f in findings:
        by_kind[f.kind] = by_kind.get(f.kind, 0) + 1
    if by_kind:
        lines.append("Finding counts:")
        for kind, n in sorted(by_kind.items()):
            lines.append(f"  {kind}: {n}")
    incomplete = [f for f in findings if f.kind == "incomplete_definition"]
    if incomplete:
        lines.append("")
        lines.append("Incomplete definitions (blocking mathematical claims):")
        for f in incomplete:
            lines.append(f"  {f.subject}: {f.detail}")
    param = [a for a in seed.arrows if a["kind"] == "parameter_dependency"]
    if param:
        lines.append("")
        lines.append("Parameter dependencies (not forgetfuls):")
        for a in param:
            lines.append(f"  {a['id']}: {a['source']} → {a['target']}")
    debt = presentation_only_dot_vertices()
    edge_debt = solid_edges_missing_seed_arrows()
    if debt or edge_debt:
        lines.append("")
        lines.append(f"DOT presentation debt: {len(debt)} unseeded vertices, {len(edge_debt)} unseeded solid edges")
        for vertex_name in debt[:12]:
            lines.append(f"  vertex: {vertex_name}")
        for src, tgt in edge_debt[:12]:
            lines.append(f"  edge: {src} -> {tgt}")
    else:
        lines.append("")
        lines.append("DOT coverage: complete (all vertices + solid edges seeded)")
    return "\n".join(lines)


def _cli(argv: Iterable[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help", "help", "report"}:
        print(format_seed_report())
        return 0
    if args[0] == "json":
        seed = load_semantic_seed()
        print(
            json.dumps(
                {
                    "entities": list(seed.entities),
                    "classifiers": list(seed.classifiers),
                    "arrows": list(seed.arrows),
                    "findings": [f.__dict__ for f in validate_seed(seed)],
                },
                indent=2,
            )
        )
        return 0
    print(f"unknown command: {args[0]}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
