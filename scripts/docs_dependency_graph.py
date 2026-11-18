#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["networkx>=3.4", "panflute>=2.3", "pydot>=3.0", "pyyaml>=6.0"]
# ///
"""Logical dependency graph of the docs book's numbered blocks.

The graph is a `networkx.DiGraph`. Its nodes are the numbered blocks (theorem,
lemma, definition, ... -- the classes `custom-numbered-blocks` lists in
`_quarto.yml`), keyed by their ids. An edge `a -> b` says that `a` uses `b`: the
statement of `a`, or the proof that follows it, cites `b` as `@b`, `[@b]` or
`[-@b]`. The references are the whole dependency record, so a block that uses a
result without citing it is an authoring defect and the graph cannot see it.

A `::: {.proof}` div proves the numbered block that immediately precedes it in
the same enclosing block list. Edge attributes `statement` and `proof` record
which part of `a` cites `b`.

The chapters are parsed by pandoc (through panflute), in `book.chapters` order;
each node's `position` is its index in that reading order.

Findings, each one a defect in the book:
  - a reference to a theorem-family id that no block defines;
  - a forward edge: `a` uses a block that comes after it in reading order;
  - a cycle (each strongly connected component with more than one block);
  - a proof with no numbered block immediately before it;
  - an id that two blocks define;
  - a numbered block with no id (it is a node, keyed `<chapter>#<position>`, but
    nothing can cite it).

Outputs, written to --out: `dependency-graph.graphml`, `dependency-graph.dot`,
`dependency-graph.json` (networkx node-link data, which the book's graph page
reads) and `dependency-findings.json`. With --registry, each node also gets the
`label` the render printed, such as "Theorem 3.2".

The book's post-render step (`writing/.assets/dependency-graph.sh`) runs this into
`_site/dependency-graph/`. `just docs-deps` runs it alone, with `--check`, which
exits nonzero when there are findings.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import panflute as pf
import yaml

# The theorem-family reference prefixes, as the amsthm-refs filter registers them.
AMSTHM_REFS = "_extensions/local/amsthm-refs/amsthm-refs.lua"


@dataclass(frozen=True)
class Finding:
    chapter: str
    message: str

    def __str__(self) -> str:
        return f"{self.chapter}: {self.message}"


def chapter_list(book: dict[str, list[str | dict[str, str | list[str]]]]) -> list[str]:
    out: list[str] = []

    def walk(items: list[str | dict[str, str | list[str]]]) -> None:
        for item in items:
            if isinstance(item, str):
                out.append(item)
                continue
            part = item.get("part")
            if isinstance(part, str) and part.endswith(".md"):
                out.append(part)
            chapters = item.get("chapters")
            if isinstance(chapters, list):
                walk(list(chapters))

    walk(book["chapters"])
    return out


def theorem_prefixes(project: Path) -> set[str]:
    import re

    text = (project / AMSTHM_REFS).read_text()
    table = re.search(r"local ref_prefixes = \{(.*?)\}", text, re.S)
    if table is None:
        sys.exit(f"docs-deps: no ref_prefixes table in {project / AMSTHM_REFS}")
    return set(re.findall(r'(\w+)"?\]?\s*=\s*true', table.group(1)))


def cited_ids(elem: pf.Element, block_classes: set[str]) -> list[str]:
    """Ids cited inside `elem`, not counting nested numbered blocks or proofs."""
    found: list[str] = []

    def walk(e: pf.Element) -> None:
        if isinstance(e, pf.Div) and e is not elem and (
            set(e.classes) & (block_classes | {"proof"})
        ):
            return
        if isinstance(e, pf.Cite):
            found.extend(c.id for c in e.citations)
            return
        for child in children(e):
            walk(child)

    walk(elem)
    return found


def children(e: pf.Element) -> list[pf.Element]:
    out: list[pf.Element] = []
    content = getattr(e, "content", None)
    if content is not None and not isinstance(e, pf.Cite):
        out.extend(content)
    if isinstance(e, pf.Table):
        out.extend([e.head, *e.content, e.foot])
    for attr in ("caption", "term"):
        sub = getattr(e, attr, None)
        if isinstance(sub, pf.Element):
            out.append(sub)
        elif isinstance(sub, pf.ListContainer):
            out.extend(sub)
    if isinstance(e, pf.DefinitionItem):
        out.extend(e.definitions)
    return [c for c in out if isinstance(c, pf.Element)]


def block_lists(e: pf.Element) -> list[list[pf.Element]]:
    """The block sequences directly below `e`: a div's body, each list item, each cell."""
    content = list(getattr(e, "content", []) or [])
    if content and all(isinstance(c, pf.Block) for c in content) and not isinstance(e, pf.Table):
        return [content]
    out: list[list[pf.Element]] = []
    for child in children(e):
        if isinstance(child, (pf.Block, pf.ListItem, pf.TableRow, pf.TableCell, pf.Definition,
                              pf.DefinitionItem, pf.TableHead, pf.TableBody, pf.TableFoot)):
            out.extend(block_lists(child))
    return out


def build(project: Path) -> tuple[nx.DiGraph, list[Finding]]:
    config = yaml.safe_load((project / "_quarto.yml").read_text())
    block_classes = set(config["custom-numbered-blocks"]["classes"])
    prefixes = theorem_prefixes(project)
    graph = nx.DiGraph()
    findings: list[Finding] = []
    # (source id, cited id, part) in reading order; resolved once every block is known
    citations: list[tuple[str, str, str, str]] = []

    position = 0
    for chapter in chapter_list(config["book"]):
        text = (project / chapter).read_text(encoding="utf-8")
        doc = pf.convert_text(text, input_format="markdown", standalone=True)
        assert isinstance(doc, pf.Doc)

        def visit_list(blocks: list[pf.Element]) -> None:
            nonlocal position
            previous: str | None = None
            for block in blocks:
                kinds = set(block.classes) & block_classes if isinstance(block, pf.Div) else set()
                if isinstance(block, pf.Div) and kinds:
                    ident = block.identifier
                    if not ident:
                        # Nothing can cite it, but its own references are still edges.
                        ident = f"{chapter}#{position}"
                        findings.append(Finding(chapter, f"a {sorted(kinds)[0]} block has no id, "
                                                "so nothing can cite it"))
                    if ident in graph:
                        findings.append(Finding(chapter, f"#{ident} is defined twice "
                                                f"(also in {graph.nodes[ident]['chapter']})"))
                    graph.add_node(
                        ident,
                        kind=sorted(kinds)[0],
                        chapter=chapter,
                        position=position,
                        title=block.attributes.get("title", ""),
                        proved=False,
                    )
                    position += 1
                    for cited in cited_ids(block, block_classes):
                        citations.append((chapter, ident, cited, "statement"))
                    previous = ident
                elif isinstance(block, pf.Div) and "proof" in block.classes:
                    if previous is None:
                        findings.append(Finding(chapter, "a proof follows no numbered block"))
                    else:
                        graph.nodes[previous]["proved"] = True
                        for cited in cited_ids(block, block_classes):
                            citations.append((chapter, previous, cited, "proof"))
                    previous = None
                else:
                    previous = None
                for sub in block_lists(block):
                    visit_list(sub)

        visit_list(list(doc.content))

    for chapter, source, cited, part in citations:
        prefix = cited.split(":", 1)[0]
        if cited not in graph:
            if ":" in cited and prefix in prefixes:
                findings.append(Finding(chapter, f"#{source} cites @{cited}, which no block defines"))
            continue
        if cited == source:
            continue
        if graph.has_edge(source, cited):
            graph.edges[source, cited][part] = True
        else:
            graph.add_edge(source, cited, statement=part == "statement", proof=part == "proof")

    for source, target in graph.edges:
        if graph.nodes[target]["position"] > graph.nodes[source]["position"]:
            findings.append(Finding(graph.nodes[source]["chapter"],
                                    f"#{source} uses #{target}, which comes later "
                                    f"(in {graph.nodes[target]['chapter']})"))
    for component in nx.strongly_connected_components(graph):
        if len(component) > 1:
            cycle = [u for u, _ in nx.find_cycle(graph.subgraph(component))]
            findings.append(Finding(graph.nodes[cycle[0]]["chapter"],
                                    "cycle: " + " -> ".join(f"#{n}" for n in [*cycle, cycle[0]])))
    return graph, findings


def add_numbers(graph: nx.DiGraph, registry: Path) -> None:
    """Give each node the label and number the render printed ("Theorem 3.2").

    The registry is the one custom-numbered-blocks writes during a book render; the
    post-render step reads it after the render that wrote it.
    """
    entries = json.loads(registry.read_text())
    for ident, data in graph.nodes(data=True):
        entry = entries.get(ident)
        if isinstance(entry, dict):
            data["label"] = f"{entry.get('reflabel', '')} {entry.get('refnumber', '')}".strip()


def write(graph: nx.DiGraph, findings: list[Finding], out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "dependency-findings.json").write_text(json.dumps(
        [{"chapter": f.chapter, "message": f.message} for f in findings], indent=1))
    nx.write_graphml(graph, out / "dependency-graph.graphml")
    nx.nx_pydot.write_dot(graph, out / "dependency-graph.dot")
    data = nx.node_link_data(graph, edges="edges")
    (out / "dependency-graph.json").write_text(json.dumps(data, indent=1))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", type=Path, default=Path("."),
                        help="Quarto project root (the directory holding _quarto.yml)")
    parser.add_argument("--out", type=Path, required=True, help="directory for the graph files")
    parser.add_argument("--registry", type=Path,
                        help="custom-numbered-blocks registry (._htmlbook_xref.json) "
                             "to take printed block numbers from")
    parser.add_argument("--check", action="store_true", help="exit 1 when there are findings")
    args = parser.parse_args()
    graph, findings = build(args.project)
    if args.registry is not None:
        add_numbers(graph, args.registry)
    write(graph, findings, args.out)
    for finding in findings:
        print(f"docs-deps: {finding}", file=sys.stderr)
    print(f"docs-deps: {graph.number_of_nodes()} blocks, {graph.number_of_edges()} edges, "
          f"{len(findings)} findings -> {args.out}", file=sys.stderr)
    if args.check and findings:
        sys.exit(1)


if __name__ == "__main__":
    main()
