"""Generate Graphviz views from the join of the three manifests."""

from __future__ import annotations

from pathlib import Path

from .design_sources import DESIGN_ROOT
from .manifests import load_mapping, load_observed
from .seed_dot import generate_dot_text, write_generated_dot

CORRESPONDENCE_DOT = DESIGN_ROOT / "sage" / "correspondence.dot"
SAGE_RAW_DOT = DESIGN_ROOT / "sage" / "observed_parents.dot"
EDGE_OVERLAY_DOT = DESIGN_ROOT / "sage" / "edge_dispositions.dot"


def generate_correspondence_dot() -> str:
    """Bipartite Sage → normalized view (mapping dashed edges)."""
    observed = load_observed()
    mapping = load_mapping()
    obs_by_id = {c["id"]: c for c in observed.get("categories", [])}
    lines = [
        "// GENERATED from observed + mapping + normalized ids",
        "digraph SageToNormalized {",
        "  graph [rankdir=LR, labelloc=t, label=\"Sage → normalized correspondence\"];",
        "  node [shape=box, style=\"rounded,filled\", fontname=\"Helvetica\", fontsize=9];",
        '  edge [arrowsize=0.65];',
        "",
        "  subgraph cluster_sage {",
        '    label="observed Sage";',
        '    style=filled; fillcolor="#fff3e0";',
    ]
    used_sage: set[str] = set()
    used_norm: set[str] = set()
    for row in mapping.get("category_mappings", []):
        if row.get("relation") == "unsupported":
            continue
        used_sage.add(row["source"])
        if row.get("target"):
            used_norm.add(row["target"])

    for sid in sorted(used_sage):
        cat = obs_by_id.get(sid)
        label = (cat or {}).get("qualname") or sid
        lines.append(
            f'    "{sid}" [label="Sage: {label}", kind="sage_category", '
            f'fillcolor="#ffe0b2"];'
        )
    lines.append("  }")
    lines.append("")
    lines.append("  subgraph cluster_norm {")
    lines.append('    label="normalized";')
    lines.append('    style=filled; fillcolor="#e8f5e9";')
    for tid in sorted(used_norm):
        lines.append(
            f'    "{tid}" [label="{tid}", kind="normalized", fillcolor="#c8e6c9"];'
        )
    lines.append("  }")
    lines.append("")
    for row in mapping.get("category_mappings", []):
        src = row["source"]
        tgt = row.get("target")
        if not tgt:
            continue
        rel = row.get("relation", "exact")
        lines.append(
            f'  "{src}" -> "{tgt}" '
            f'[kind="normalizes_to", mapping="{rel}", style=dashed];'
        )
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def generate_observed_parents_dot() -> str:
    """Raw observed immediate-supercategory graph."""
    observed = load_observed()
    lines = [
        "// GENERATED from design/sage/observed.json immediate_supercategories",
        "digraph ObservedSageParents {",
        '  graph [rankdir=BT, labelloc=t, label="Observed Sage immediate supercategories"];',
        '  node [shape=box, style="rounded,filled", fillcolor="#fff8e1", fontname="Helvetica", fontsize=9];',
        '  edge [arrowsize=0.6];',
    ]
    used: set[str] = set()
    edges: list[tuple[str, str]] = []
    for cat in observed.get("categories", []):
        frm = cat["id"]
        for edge in cat.get("immediate_supercategories") or []:
            to = edge.get("target")
            if not to:
                continue
            used.add(frm)
            used.add(to)
            edges.append((frm, to))
    by_id = {c["id"]: c for c in observed.get("categories", [])}
    for sid in sorted(used):
        label = (by_id.get(sid) or {}).get("qualname") or sid
        lines.append(f'  "{sid}" [label="{label}"];')
    for frm, to in sorted(set(edges)):
        lines.append(f'  "{frm}" -> "{to}" [kind="super_categories"];')
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


_DISP_STYLE = {
    "preserved": 'color="#2e7d32", style=solid',
    "subdivided": 'color="#1565c0", style=dashed',
    "corrected": 'color="#c62828", style=bold',
    "alias_artifact": 'color="#6a1b9a", style=dotted',
    "unsupported": 'color="#9e9e9e", style=dashed',
}


def generate_edge_dispositions_dot() -> str:
    """Observed Sage edges colored by correspondence disposition."""
    mapping = load_mapping()
    observed = load_observed()
    by_id = {c["id"]: c for c in observed.get("categories", [])}
    lines = [
        "// GENERATED from mapping edge_mappings dispositions",
        "digraph SageEdgeDispositions {",
        '  graph [rankdir=BT, labelloc=t, label="Sage edges by disposition"];',
        '  node [shape=box, style="rounded,filled", fillcolor="#eceff1", fontname="Helvetica", fontsize=9];',
        '  edge [arrowsize=0.6];',
    ]
    used: set[str] = set()
    for row in mapping.get("edge_mappings", []):
        se = row.get("source_edge") or {}
        frm, to = se.get("from"), se.get("to")
        if frm and to:
            used.add(frm)
            used.add(to)
    for sid in sorted(used):
        label = (by_id.get(sid) or {}).get("qualname") or sid
        lines.append(f'  "{sid}" [label="{label}"];')
    for row in mapping.get("edge_mappings", []):
        se = row.get("source_edge") or {}
        frm, to = se.get("from"), se.get("to")
        if not frm or not to:
            continue
        disp = row.get("disposition") or "unsupported"
        style = _DISP_STYLE.get(disp, _DISP_STYLE["unsupported"])
        lines.append(
            f'  "{frm}" -> "{to}" [disposition="{disp}", {style}];'
        )
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def write_correspondence_dot(path: Path | None = None) -> Path:
    dest = path or CORRESPONDENCE_DOT
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(generate_correspondence_dot(), encoding="utf-8")
    return dest


def write_observed_parents_dot(path: Path | None = None) -> Path:
    dest = path or SAGE_RAW_DOT
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(generate_observed_parents_dot(), encoding="utf-8")
    return dest


def write_edge_dispositions_dot(path: Path | None = None) -> Path:
    dest = path or EDGE_OVERLAY_DOT
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(generate_edge_dispositions_dot(), encoding="utf-8")
    return dest


def write_all_views() -> dict[str, Path]:
    """Regenerate normalized + correspondence + observed parent DOTs."""
    return {
        "normalized": write_generated_dot(also_presentation=False),
        "correspondence": write_correspondence_dot(),
        "observed_parents": write_observed_parents_dot(),
        "edge_dispositions": write_edge_dispositions_dot(),
    }


def main() -> int:
    paths = write_all_views()
    for name, path in paths.items():
        print(f"{name}: {path}")
    _ = generate_dot_text
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
