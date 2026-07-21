"""Parse ``category_parent_graph.dot`` into solid edges and axiom attachments."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .design_sources import NORMALIZED_DOT

_DOT_PATH = NORMALIZED_DOT

# Node token: quoted string, or bare identifier (letters, digits, unicode ops)
_NODE = r'(?:"([^"]+)"|([A-Za-z_][A-Za-z0-9_()∞^,.Éé−-]*)|"([^"]+)")'


@dataclass(frozen=True)
class Edge:
    src: str
    tgt: str
    dotted: bool
    # True only when the DOT edge attributes include ``style=dotted``.
    # ``dotted`` also marks edges whose *source* is an axiom node (legacy
    # classification used by solid/axiom multidigraph splits).
    style_dotted: bool = False


@dataclass(frozen=True)
class DotGraph:
    edges: tuple[Edge, ...]
    axiom_labels: dict[str, str]  # node id -> short axiom label
    named_joins: dict[str, tuple[str, tuple[str, ...]]]  # display -> (host, axioms)

    @property
    def solid_edges(self) -> tuple[Edge, ...]:
        return tuple(e for e in self.edges if not e.dotted)

    @property
    def axiom_edges(self) -> tuple[Edge, ...]:
        return tuple(e for e in self.edges if e.dotted)

    @property
    def declared_axiom_edges(self) -> tuple[Edge, ...]:
        """Axiom *definition* attachments: explicit ``style=dotted`` only."""
        return tuple(e for e in self.edges if e.style_dotted)

    @property
    def solid_nodes(self) -> frozenset[str]:
        nodes: set[str] = set()
        for edge in self.solid_edges:
            nodes.add(edge.src)
            nodes.add(edge.tgt)
        for edge in self.axiom_edges:
            nodes.add(edge.tgt)
        for join in self.named_joins:
            nodes.add(join)
        return frozenset(nodes)


def _strip_comments(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        if "//" in line:
            line = line[: line.index("//")]
        out.append(line)
    return "\n".join(out)


def _parse_named_join(
    node: str,
    *,
    known_hosts: frozenset[str] | None = None,
) -> tuple[str, tuple[str, ...]] | None:
    if " = " not in node:
        return None
    _name, path = node.split(" = ", 1)
    parts = path.split(".")
    if len(parts) < 2:
        return None
    # Prefer the longest dotted prefix that is an existing host vertex
    # (so Magmas.Additive.Associative → host Magmas.Additive, not Magmas).
    if known_hosts:
        for i in range(len(parts) - 1, 0, -1):
            cand = ".".join(parts[:i])
            if cand in known_hosts:
                return cand, tuple(parts[i:])
    return parts[0], tuple(parts[1:])


def _node_from_match(groups: tuple[str | None, ...]) -> str:
    for g in groups:
        if g:
            return g
    raise ValueError(groups)


def parse_dot(path: Path | None = None) -> DotGraph:
    text = _strip_comments((path or _DOT_PATH).read_text(encoding="utf-8"))

    axiom_labels: dict[str, str] = {}
    for match in re.finditer(r'"([^"]+)"\s*\[([^\]]*)\]', text):
        node_id, attrs = match.group(1), match.group(2)
        if "dotted" not in attrs:
            continue
        # Edge lines attach ``[style=dotted]`` to the target, not a node declaration.
        prefix = text[max(0, match.start() - 12) : match.start()]
        if "->" in prefix:
            continue
        label_match = re.search(r'label="([^"]+)"', attrs)
        axiom_labels[node_id] = label_match.group(1) if label_match else node_id.rsplit(".", 1)[-1]

    # Also collect bare axiom ids declared with dotted style in multi-line blocks:
    # after `node [style=...dotted...]` until the next `node [` reset.
    in_dotted = False
    for line in text.splitlines():
        if re.search(r"node\s*\[", line):
            in_dotted = "dotted" in line
            continue
        if not in_dotted:
            continue
        for match in re.finditer(r'"([^"]+)"\s*(?:\[|;)', line):
            node_id = match.group(1)
            if node_id not in axiom_labels:
                label_m = re.search(r'label="([^"]+)"', line)
                axiom_labels[node_id] = label_m.group(1) if label_m else node_id.rsplit(".", 1)[-1]
        # label on same declaration: "id" [label="Foo"];
        for match in re.finditer(r'"([^"]+)"\s*\[\s*label="([^"]+)"\s*\]', line):
            axiom_labels[match.group(1)] = match.group(2)

    edge_re = re.compile(
        r'("([^"]+)"|([A-Za-z_][A-Za-z0-9_()∞^.Éé−-]*))'
        r"\s*->\s*"
        r'("([^"]+)"|([A-Za-z_][A-Za-z0-9_()∞^.Éé−-]*))'
        r"\s*(\[[^\]]*\])?"
    )
    edges: list[Edge] = []
    seen: set[tuple[str, str, bool]] = set()
    for match in edge_re.finditer(text):
        src = match.group(2) or match.group(3)
        tgt = match.group(5) or match.group(6)
        attrs = match.group(7) or ""
        style_dotted = "style=dotted" in attrs.replace(" ", "")
        dotted = style_dotted or src in axiom_labels
        key = (src, tgt, dotted)
        if key in seen:
            continue
        seen.add(key)
        edges.append(Edge(src=src, tgt=tgt, dotted=dotted, style_dotted=style_dotted))

    # Named joins: longest dotted host prefix among known vertices
    # (Magmas.Additive.Associative → host Magmas.Additive, not Magmas).
    candidate_hosts: set[str] = set(axiom_labels)
    for edge in edges:
        candidate_hosts.add(edge.src)
        candidate_hosts.add(edge.tgt)
    for match in re.finditer(r'"([^"=]+ = [^"]+)"', text):
        candidate_hosts.add(match.group(1).split(" = ", 1)[0])
    candidate_hosts.update(
        {
            "Magmas.Additive",
            "Magmas.Multiplicative",
            "∫Bil_R(R)",
            "∫Bil_R(W)",
            "∫Quad_R(W)",
            "∫Herm_R(W)",
            "UnitalAlgebras",
            "VectorSpaces(K)",
        }
    )
    known_hosts = frozenset(candidate_hosts)

    named_joins: dict[str, tuple[str, tuple[str, ...]]] = {}
    for edge in edges:
        for node in (edge.src, edge.tgt):
            parsed = _parse_named_join(node, known_hosts=known_hosts)
            if parsed is not None:
                named_joins[node] = parsed
    for match in re.finditer(r'"([^"=]+ = [^"]+)"', text):
        node = match.group(1)
        parsed = _parse_named_join(node, known_hosts=known_hosts)
        if parsed is not None:
            named_joins[node] = parsed

    return DotGraph(
        edges=tuple(edges),
        axiom_labels=axiom_labels,
        named_joins=named_joins,
    )
