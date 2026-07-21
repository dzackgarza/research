"""Generate presentation DOT from the authoritative semantic seed.

Writes ``category_parent_graph.generated.dot`` (pure semantic view).
The hand-layout ``category_parent_graph.dot`` remains the factory/viz
presentation until clusters are driven from the seed directly.
"""

from __future__ import annotations

import shutil
from collections import defaultdict
from pathlib import Path

from .design_sources import NORMALIZED_CATEGORY_GRAPH_DIR, NORMALIZED_DOT
from .semantic_seed import load_semantic_seed

HAND_DOT = NORMALIZED_CATEGORY_GRAPH_DIR / "category_parent_graph.hand.dot"
GENERATED_DOT = NORMALIZED_CATEGORY_GRAPH_DIR / "category_parent_graph.generated.dot"

_KIND_FILL = {
    "category_family": "#f7f7f7",
    "derived_category": "#e8f5e9",
    "classifier_domain": "#fffef5",
    "category_constructor": "#e3f2fd",
    "alias": "#fce4ec",
}

_KIND_COLOR = {
    "category_family": "#333333",
    "derived_category": "#1b5e20",
    "classifier_domain": "#888888",
    "category_constructor": "#1565c0",
    "alias": "#880e4f",
}

_ARROW_STYLE = {
    "forgetful": "",
    "full_inclusion": "",
    "classifier_leg": "style=dotted",
    "pullback_projection": "",
    "theorem_inclusion": "style=dashed",
    "equivalence": "dir=both",
    "construction": 'color="#6a1b9a"',
    "parameter_dependency": 'style=dashed,color="#e65100"',
}


def re_needs_quote(s: str) -> bool:
    if not s:
        return True
    if any(c in s for c in " =()−∞∫^,.\"'\\"):
        return True
    if not (s[0].isalpha() or s[0] == "_"):
        return True
    return False


def _dot_quote(s: str) -> str:
    if re_needs_quote(s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def generate_dot_text(*, include_opaque: bool = False) -> str:
    """Serialize preferred seed arrows + entities as a Graphviz digraph.

    Opaque authored-ledger hosts are omitted from the factory presentation by
    default (no stub cluster yet); set ``include_opaque=True`` for a full
    semantic dump.
    """
    seed = load_semantic_seed()
    by_id = seed.entity_by_id()
    skip_ids = set()
    if not include_opaque:
        for e in seed.entities:
            definition = e.get("definition") or {}
            if definition.get("opaque"):
                skip_ids.add(e["id"])
    lines: list[str] = [
        "// GENERATED from semantic_seed/ — semantic presentation view.",
        "// Authoritative: design/normalized_category_graph/semantic_seed/",
        "// Factory/viz layout: category_parent_graph.dot (hand; see .hand.dot)",
        "",
        "digraph CategoryParents {",
        "  graph [",
        "    rankdir=BT",
        "    labelloc=t",
        '    label="Category parents (generated from semantic seed)"',
        "    fontsize=15",
        '    fontname="Helvetica"',
        "    nodesep=0.28",
        "    ranksep=0.45",
        "    splines=true",
        "  ];",
        "  node [",
        "    shape=box",
        '    style="rounded,filled"',
        '    fontname="Helvetica"',
        "    fontsize=9",
        '    fillcolor="#f7f7f7"',
        '    color="#333333"',
        "  ];",
        '  edge [color="#444444", arrowsize=0.65];',
        "",
    ]

    by_kind: dict[str, list] = defaultdict(list)
    for e in seed.entities:
        if e["id"] in skip_ids:
            continue
        if not e.get("dot_vertex"):
            continue
        by_kind[e["kind"]].append(e)

    for kind in (
        "category_family",
        "derived_category",
        "category_constructor",
        "classifier_domain",
        "alias",
    ):
        group = by_kind.get(kind) or []
        if not group:
            continue
        lines.append(f"  // --- {kind} ---")
        for e in sorted(group, key=lambda x: x["dot_vertex"]):
            vertex = e["dot_vertex"]
            fill = _KIND_FILL.get(kind, "#f7f7f7")
            color = _KIND_COLOR.get(kind, "#333333")
            style = "rounded,filled,dotted" if kind == "classifier_domain" else "rounded,filled"
            attrs = [
                f'style="{style}"',
                f'fillcolor="{fill}"',
                f'color="{color}"',
                f'id="{e["id"]}"',
                f'kind="{kind}"',
            ]
            if kind == "classifier_domain":
                label = e.get("canonical_name", "").rsplit(".", 1)[-1]
                if label and label != vertex:
                    attrs.append(f'label="{label}"')
            lines.append(f"  {_dot_quote(vertex)} [{', '.join(attrs)}];")
        lines.append("")

    lines.append("  // --- preferred arrows ---")
    seen: set[tuple[str, str, str]] = set()
    for a in seed.arrows:
        if not a.get("preferred", True):
            continue
        if a["source"] in skip_ids or a["target"] in skip_ids:
            continue
        src_e = by_id.get(a["source"])
        tgt_e = by_id.get(a["target"])
        if not src_e or not tgt_e:
            continue
        src = src_e.get("dot_vertex")
        tgt = tgt_e.get("dot_vertex")
        if not src or not tgt or src == tgt:
            continue
        key = (src, tgt, a["kind"])
        if key in seen:
            continue
        seen.add(key)
        style = _ARROW_STYLE.get(a["kind"], "")
        attr_parts = [f'kind="{a["kind"]}"', f'id="{a["id"]}"']
        if style:
            attr_parts.insert(0, style)
        lines.append(f"  {_dot_quote(src)} -> {_dot_quote(tgt)} [{', '.join(attr_parts)}];")

    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def write_generated_dot(path: Path | None = None, *, also_presentation: bool = False) -> Path:
    """Write semantic DOT without opaque hosts.

    Factory/viz keep ``category_parent_graph.dot`` (hand layout). Generated is
    the seed↔DOT coverage surface. Pass ``also_presentation=True`` only when
    deliberately replacing the factory graph (unsafe for opaque/extra edges).
    """
    text = generate_dot_text(include_opaque=False)
    dest = path or GENERATED_DOT
    if NORMALIZED_DOT.is_file() and not HAND_DOT.is_file():
        prior = NORMALIZED_DOT.read_text(encoding="utf-8")
        if "GENERATED from semantic_seed" not in prior:
            shutil.copy2(NORMALIZED_DOT, HAND_DOT)
    dest.write_text(text, encoding="utf-8")
    if also_presentation and dest.resolve() != NORMALIZED_DOT.resolve():
        NORMALIZED_DOT.write_text(text, encoding="utf-8")
        from .factory import reset_factory

        reset_factory()
    return dest


def main() -> int:
    path = write_generated_dot(also_presentation=False)
    print(f"wrote {path}")
    print(f"factory presentation: {NORMALIZED_DOT}")
    if HAND_DOT.is_file():
        print(f"hand archive: {HAND_DOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
