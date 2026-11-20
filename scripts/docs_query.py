#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["networkx>=3.4", "panflute>=2.3", "pydot>=3.0", "pyyaml>=6.0", "torch>=2.9", "txtai>=9.0"]
# [tool.uv.sources]
# torch = { index = "pytorch-cpu" }
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
# ///
"""Structural queries over the docs book: its numbered blocks, headings, citations and uses.

The index has three parts:
  - the dependency graph that `docs_dependency_graph.build` reads from the pandoc AST
    (blocks, their kinds, titles, defined terms, and the `uses`/`mentions` edges);
  - the source span of every fenced div with an id, and of the proof after it, read
    from the chapter files line by line, so that each block has a `file:line`;
  - the headings of each chapter, with their levels, lines and anchors.

Building the graph runs pandoc on every chapter. With --cache, the index is stored
there and reused while no chapter, `_quarto.yml` or script has changed.

Subcommands (each takes --json for machine output where it prints records):
  list      the blocks, filtered by kind, chapter, title or proof status
  show      the source of blocks, with their proofs
  tree      the heading structure of the book, with the blocks under each heading
  search    hybrid (BM25 and sentence-embedding) search over block text, via txtai
  term      the same search, restricted to definitions, constructions, notations, conventions
  where     every occurrence of a citation key or block id, with its enclosing block
  deps      the blocks a block uses, transitively, as a tree (--reverse: its users)
  path      a shortest chain of uses from one block to another
  graph     the dot source of a block's neighbourhood in the graph
  stats     block counts by kind and part
  findings  the defects that `just docs-deps` reports
"""

from __future__ import annotations

import argparse
import difflib
import fnmatch
import hashlib
import json
import os
import pickle
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from collections.abc import Callable
from typing import TYPE_CHECKING

import networkx as nx
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs_dependency_graph as ddg  # noqa: E402

if TYPE_CHECKING:
    from txtai import Embeddings

INDEX_VERSION = 5
# The sentence-embedding model of the semantic half of `search` and `term`.
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
# Block kinds that assert something a proof establishes.
# One printed record: a block, a cited result, an occurrence or a count row.
Row = dict[str, str | bool | int]
PROVABLE = frozenset({"theorem", "lemma", "corollary", "proposition", "observation", "claim"})
_OPEN = re.compile(r"^\s*(:{3,})\s*(\{.*\}|[\w-]+)\s*$")
# A bold phrase with no mathematics in it.
_CLOSE = re.compile(r"^\s*:{3,}\s*$")
_CODE_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(?:\{([^}]*)\})?\s*$")
_ATTR_ID = re.compile(r"(?<![\w-])#([^\s}]+)")
_ATTR_CLASS = re.compile(r"(?<![\w-])\.([\w-]+)")


@dataclass
class Span:
    """Lines (1-based, inclusive) of one fenced div with an id, and of its proof."""

    file: str
    start: int
    end: int
    classes: list[str]
    proof_start: int | None = None
    proof_end: int | None = None


@dataclass
class Heading:
    file: str
    line: int
    level: int
    text: str
    anchor: str


@dataclass
class Index:
    graph: nx.DiGraph
    findings: list[ddg.Finding]
    chapters: list[str]
    # chapter (as `_quarto.yml` names it) -> source path relative to the working directory
    files: dict[str, str]
    spans: dict[str, Span] = field(default_factory=dict)
    headings: list[Heading] = field(default_factory=list)
    # source path -> its lines
    lines: dict[str, list[str]] = field(default_factory=dict)
    # the fingerprint of the sources the index was built from
    key: str = ""


def display_path(path: Path) -> str:
    return os.path.relpath(path.resolve(), Path.cwd())


def scan(file: str, lines: list[str], spans: dict[str, Span], headings: list[Heading]) -> None:
    """Record the fenced divs with ids and the headings of one chapter's lines.

    A fence of three or more colons with attributes opens a div; a bare fence closes the
    innermost open one, as in pandoc's fenced_divs. Lines inside code fences are skipped.
    A `.proof` div opened right after a block with an id closes (blank lines between
    are allowed) proves that block, as `docs_dependency_graph` reads it.
    """
    # (opening line, id, classes, the block a proof proves)
    stack: list[tuple[int, str | None, list[str], str | None]] = []
    code: str | None = None
    last_closed: str | None = None
    for number, line in enumerate(lines, 1):
        fence = _CODE_FENCE.match(line)
        if code is not None:
            if fence and fence.group(1)[0] == code[0] and len(fence.group(1)) >= len(code):
                code = None
            continue
        if fence:
            code = fence.group(1)
            last_closed = None
            continue
        if not stack and line.startswith("#"):
            heading = _HEADING.match(line)
            if heading:
                attrs = heading.group(3) or ""
                anchor = _ATTR_ID.search(attrs)
                headings.append(Heading(file, number, len(heading.group(1)), heading.group(2),
                                        anchor.group(1) if anchor else ""))
        opened = _OPEN.match(line)
        if opened:
            # A quoted value, such as a title holding $D_{16}$, is no class or id.
            attrs = re.sub(r'"[^"]*"', '""', opened.group(2))
            classes = _ATTR_CLASS.findall(attrs) if attrs.startswith("{") else [attrs]
            ident = _ATTR_ID.search(attrs) if attrs.startswith("{") else None
            proves = last_closed if "proof" in classes else None
            stack.append((number, ident.group(1) if ident else None, classes, proves))
            last_closed = None
            continue
        if _CLOSE.match(line) and stack:
            start, ident, classes, proves = stack.pop()
            if proves is not None and proves in spans:
                proved = spans[proves]
                if proved.proof_start is None and proved.file == file:
                    proved.proof_start, proved.proof_end = start, number
            if ident is not None:
                spans.setdefault(ident, Span(file, start, number, classes))
            last_closed = ident
            continue
        if line.strip():
            last_closed = None


def fingerprint(project: Path, chapters: list[str]) -> str:
    digest = hashlib.sha256(str(INDEX_VERSION).encode())
    paths = [project / "_quarto.yml", Path(__file__), Path(ddg.__file__),
             *(project / c for c in chapters)]
    for path in paths:
        stat = path.stat()
        digest.update(f"{path.resolve()}:{stat.st_mtime_ns}:{stat.st_size}".encode())
    return digest.hexdigest()


def load(project: Path, cache: Path | None) -> Index:
    config = yaml.safe_load((project / "_quarto.yml").read_text())
    chapters = ddg.chapter_list(config["book"])
    key = fingerprint(project, chapters)
    if cache is not None and cache.exists():
        stored_key, index = pickle.loads(cache.read_bytes())
        if stored_key == key:
            return index
    graph, findings = ddg.build(project)
    files = {c: display_path(project / c) for c in chapters}
    index = Index(graph, findings, chapters, files, key=key)
    for chapter in chapters:
        file = files[chapter]
        lines = (project / chapter).read_text().splitlines()
        index.lines[file] = lines
        scan(file, lines, index.spans, index.headings)
    if cache is not None:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(pickle.dumps((key, index)))
    return index


# --- records -------------------------------------------------------------------------


def is_block(data: dict[str, str | bool | int]) -> bool:
    return data.get("kind") != ddg.REFERENCE


def location(index: Index, ident: str) -> str:
    span = index.spans.get(ident)
    if span is not None:
        return f"{span.file}:{span.start}"
    chapter = index.graph.nodes[ident].get("chapter", "")
    return index.files.get(chapter, chapter)


def record(index: Index, ident: str) -> Row:
    data = index.graph.nodes[ident]
    out: Row = {"id": ident, "kind": data["kind"],
                                        "title": data.get("title", ""),
                                        "location": location(index, ident)}
    if is_block(data):
        out["proved"] = bool(data.get("proved"))
        if data.get("label"):
            out["label"] = data["label"]
        if data.get("defines"):
            out["defines"] = data["defines"]
    else:
        out["work"] = data.get("work", "")
    return out


def emit(rows: list[Row], as_json: bool, columns: tuple[str, ...]) -> None:
    if as_json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return
    if not rows:
        return
    header = {c: c for c in columns}
    widths = {c: min(48, max(len(str(r.get(c, ""))) for r in [header, *rows]))
              for c in columns[:-1]}
    for row in [header, *rows]:
        cells = [str(row.get(c, "")).ljust(widths[c]) for c in columns[:-1]]
        print("  ".join([*cells, str(row.get(columns[-1], ""))]).rstrip())


def require(index: Index, ident: str) -> str:
    if ident in index.graph:
        return ident
    hint = ", ".join(difflib.get_close_matches(ident, list(index.graph.nodes), n=5, cutoff=0.4))
    sys.exit(f"docs-query: no block or cited result '{ident}'; closest: {hint}")


def section_of(index: Index, file: str, line: int) -> Heading | None:
    best: Heading | None = None
    for heading in index.headings:
        if heading.file == file and heading.line <= line:
            best = heading
    return best


def enclosing_block(index: Index, file: str, line: int) -> str | None:
    """The innermost block (or its proof) whose span holds the line."""
    best: tuple[int, str] | None = None
    for ident, span in index.spans.items():
        if span.file != file:
            continue
        ranges = [(span.start, span.end)]
        if span.proof_start is not None and span.proof_end is not None:
            ranges.append((span.proof_start, span.proof_end))
        for start, end in ranges:
            if start <= line <= end and (best is None or start > best[0]):
                best = (start, ident)
    return best[1] if best else None


# --- subcommands ---------------------------------------------------------------------


def cmd_list(index: Index, args: argparse.Namespace) -> None:
    rows = []
    for ident, data in sorted(index.graph.nodes(data=True), key=lambda n: n[1]["position"]):
        if not is_block(data):
            continue
        if args.kind and data["kind"] not in args.kind:
            continue
        if args.chapter and not fnmatch.fnmatch(location(index, ident), f"*{args.chapter}*"):
            continue
        if args.title and args.title.lower() not in data.get("title", "").lower():
            continue
        if args.unproved and (data.get("proved") or data["kind"] not in PROVABLE):
            continue
        if args.unused and (data["kind"] not in ddg.LOGICAL or any(
                index.graph.edges[u, ident]["relation"] == "uses"
                for u in index.graph.predecessors(ident))):
            continue
        rows.append(record(index, ident))
    if args.ids:
        print("\n".join(str(r["id"]) for r in rows))
        return
    emit(rows, args.json, ("kind", "id", "location", "title"))


def cmd_show(index: Index, args: argparse.Namespace) -> None:
    for raw in args.ids:
        ident = require(index, raw)
        span = index.spans.get(ident)
        if span is None:
            print(f"== {ident} ({index.graph.nodes[ident]['kind']}): no source span")
            continue
        lines = index.lines[span.file]
        end = span.end
        if span.proof_end is not None and not args.no_proof:
            end = span.proof_end
        print(f"== {span.file}:{span.start}")
        print("\n".join(lines[span.start - 1:end]))
        print()


def cmd_tree(index: Index, args: argparse.Namespace) -> None:
    """Chapters, then headings indented by level, then the blocks under each heading."""
    depth = args.depth
    for chapter in index.chapters:
        file = index.files[chapter]
        if args.chapter and args.chapter not in file:
            continue
        items: list[tuple[int, str]] = []
        for heading in index.headings:
            if heading.file == file and heading.level <= depth:
                anchor = f"  {{#{heading.anchor}}}" if heading.anchor else ""
                items.append((heading.line, "  " * heading.level
                              + f"{'#' * heading.level} {heading.text}{anchor}"))
        if args.blocks:
            for ident, span in index.spans.items():
                if span.file != file or ident not in index.graph:
                    continue
                heading = section_of(index, file, span.start)
                level = heading.level if heading else 0
                data = index.graph.nodes[ident]
                if args.kind and data["kind"] not in args.kind:
                    continue
                title = f'  "{data["title"]}"' if data.get("title") else ""
                items.append((span.start, "  " * (level + 1) + f"{data['kind']} {ident}{title}"))
        print(file)
        for _, text in sorted(items):
            print(text)


def document(index: Index, ident: str) -> str:
    """The text a block is searched by: its title, defined terms, statement and proof."""
    data = index.graph.nodes[ident]
    parts = [data.get("title", ""), data.get("defines", "")]
    span = index.spans.get(ident)
    if span is not None:
        end = span.proof_end if span.proof_end is not None else span.end
        parts.extend(index.lines[span.file][span.start - 1:end])
    return "\n".join(parts)


def search_engine(index: Index, cache: Path | None) -> Embeddings:
    """A txtai hybrid index (BM25 and sentence embeddings) of every block's document.

    It is saved beside the --cache pickle and rebuilt when the book changes.
    """
    from txtai import Embeddings  # torch loads for search only, not for the other queries

    engine = Embeddings(path=EMBEDDING_MODEL, hybrid=True, content=False)
    store = cache.parent / "txtai" if cache is not None else None
    stamp = store / "book-key" if store is not None else None
    if stamp is not None and stamp.exists() and stamp.read_text() == index.key:
        engine.load(str(store))
        return engine
    engine.index((ident, document(index, ident), None)
                 for ident, data in index.graph.nodes(data=True) if is_block(data))
    if store is not None and stamp is not None:
        engine.save(str(store))
        stamp.write_text(index.key)
    return engine


def search_rows(index: Index, args: argparse.Namespace, kinds: list[str] | None) -> list[Row]:
    engine = search_engine(index, args.cache)
    rows: list[Row] = []
    for ident, score in engine.search(" ".join(args.query), limit=args.limit * 10):
        if kinds and index.graph.nodes[ident]["kind"] not in kinds:
            continue
        rows.append({**record(index, ident), "score": f"{score:.2f}"})
        if len(rows) == args.limit:
            break
    return rows


def cmd_search(index: Index, args: argparse.Namespace) -> None:
    emit(search_rows(index, args, args.kind), args.json,
         ("score", "kind", "id", "location", "title"))


def cmd_term(index: Index, args: argparse.Namespace) -> None:
    emit(search_rows(index, args, sorted(ddg.DEFINING)), args.json,
         ("score", "kind", "id", "location", "defines"))


def cmd_where(index: Index, args: argparse.Namespace) -> None:
    """Every `@key` in the chapters: its locator, the enclosing block and the heading."""
    key = re.escape(args.key)
    pattern = re.compile(r"(?<![\w@])-?@" + key + r"(?![\w:.-]*[\w])(?:,\s*([^;\]]*))?")
    rows = []
    for chapter in index.chapters:
        file = index.files[chapter]
        for number, line in enumerate(index.lines[file], 1):
            for match in pattern.finditer(line):
                block = enclosing_block(index, file, number)
                heading = section_of(index, file, number)
                part = ""
                if block is not None:
                    span = index.spans[block]
                    part = "proof" if span.proof_start and number >= span.proof_start else "statement"
                rows.append({"location": f"{file}:{number}",
                             "locator": (match.group(1) or "").strip(),
                             "block": block or "", "part": part,
                             "section": heading.text if heading else ""})
    if args.json:
        emit(rows, True, ())
    else:
        emit(rows, False, ("location", "block", "part", "locator", "section"))
    results = sorted((n for n, d in index.graph.nodes(data=True)
                      if d.get("work") == args.key), key=str)
    if results and not args.json:
        print(f"\ncited results of {args.key}:")
        for result in results:
            users = sorted(index.graph.predecessors(result))
            print(f"  {result}  <- {', '.join(users)}")


def neighbours(graph: nx.DiGraph, node: str, reverse: bool, logical: bool) -> list[str]:
    edges = graph.in_edges(node, data=True) if reverse else graph.out_edges(node, data=True)
    out = []
    for u, v, data in edges:
        if logical and data["relation"] != "uses":
            continue
        out.append(u if reverse else v)
    return sorted(out, key=lambda n: (graph.nodes[n]["position"] < 0, graph.nodes[n]["position"], n))


def cmd_deps(index: Index, args: argparse.Namespace) -> None:
    graph = index.graph
    root = require(index, args.id)
    seen: set[str] = set()
    rows: list[Row] = []

    def visit(node: str, depth: int) -> None:
        data = graph.nodes[node]
        repeat = node in seen
        if not args.json:
            label = f"{data['kind']} {node}"
            if data.get("title") and data["title"] != node:
                label += f'  "{data["title"]}"'
            print("  " * depth + label + ("  (above)" if repeat else ""))
        else:
            rows.append({**record(index, node), "depth": depth})
        if repeat:
            return
        seen.add(node)
        if args.depth is not None and depth >= args.depth:
            return
        for child in neighbours(graph, node, args.reverse, not args.all):
            visit(child, depth + 1)

    visit(root, 0)
    if args.json:
        emit(rows, True, ())


def cmd_path(index: Index, args: argparse.Namespace) -> None:
    graph = index.graph
    source, target = require(index, args.source), require(index, args.target)
    view = graph if args.all else graph.edge_subgraph(
        (u, v) for u, v, r in graph.edges(data="relation") if r == "uses")
    try:
        chain = nx.shortest_path(view, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        sys.exit(f"docs-query: no chain of uses from {source} to {target}")
    emit([record(index, n) for n in chain], args.json, ("kind", "id", "location", "title"))


def cmd_graph(index: Index, args: argparse.Namespace) -> None:
    graph = index.graph
    root = require(index, args.id)
    keep = {root}
    frontier = {root}
    for _ in range(args.depth):
        step: set[str] = set()
        for node in frontier:
            step.update(neighbours(graph, node, False, not args.all))
            if args.both:
                step.update(neighbours(graph, node, True, not args.all))
        frontier = step - keep
        keep |= step
    sub = graph.subgraph(keep)
    print(f"digraph {json.dumps(root)} {{\n  rankdir=BT; node [shape=box, fontsize=10];")
    for node, data in sub.nodes(data=True):
        label = f"{data['kind']}\\n{node}"
        style = ", style=dashed" if data["kind"] == ddg.REFERENCE else ""
        style += ", penwidth=2" if node == root else ""
        print(f"  {json.dumps(node)} [label={json.dumps(label)}{style}];")
    for u, v, data in sub.edges(data=True):
        if not args.all and data["relation"] != "uses":
            continue
        style = " [style=dotted]" if data["relation"] == "mentions" else ""
        print(f"  {json.dumps(u)} -> {json.dumps(v)}{style};")
    print("}")


def cmd_stats(index: Index, args: argparse.Namespace) -> None:
    counts: dict[str, dict[str, int]] = {}
    for _, data in index.graph.nodes(data=True):
        if not is_block(data):
            continue
        part = data["chapter"].split("/", 1)[0] if "/" in data["chapter"] else "(top level)"
        counts.setdefault(data["kind"], {}).setdefault(part, 0)
        counts[data["kind"]][part] += 1
    parts = sorted({p for row in counts.values() for p in row})
    rows = [{"kind": kind, **{p: row.get(p, 0) for p in parts}, "total": sum(row.values())}
            for kind, row in sorted(counts.items(), key=lambda kv: -sum(kv[1].values()))]
    rows.append({"kind": "total", **{p: sum(r[p] for r in rows) for p in parts},
                 "total": sum(r["total"] for r in rows)})
    emit(rows, args.json, ("kind", *parts, "total"))


def cmd_findings(index: Index, args: argparse.Namespace) -> None:
    if args.json:
        print(json.dumps([asdict(f) for f in index.findings], indent=1))
        return
    for finding in index.findings:
        print(finding)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", type=Path, default=Path("writing/.book"),
                        help="Quarto project root (the directory holding _quarto.yml)")
    parser.add_argument("--cache", type=Path, help="pickle file to keep the index in")
    sub = parser.add_subparsers(dest="command", required=True)

    def command(name: str, func: Callable[[Index, argparse.Namespace], None], help_text: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name, help=help_text, description=help_text)
        p.set_defaults(func=func)
        p.add_argument("--json", action="store_true", help="print JSON records")
        return p

    kinds = {"nargs": "*", "metavar": "KIND", "help": "block kinds (theorem, definition, ...)"}
    p = command("list", cmd_list, "List the numbered blocks in reading order.")
    p.add_argument("--kind", **kinds)
    p.add_argument("--chapter", help="substring of the source path")
    p.add_argument("--title", help="substring of the title")
    p.add_argument("--unproved", action="store_true",
                   help="only theorem-like blocks with no proof after them")
    p.add_argument("--unused", action="store_true",
                   help="only logical blocks that no logical block uses")
    p.add_argument("--ids", action="store_true", help="print only the ids")
    p = command("show", cmd_show, "Print the source of blocks, with their proofs.")
    p.add_argument("ids", nargs="+")
    p.add_argument("--no-proof", action="store_true")
    p = command("tree", cmd_tree, "Print the heading tree, with the blocks under each heading.")
    p.add_argument("chapter", nargs="?", help="substring of the source path")
    p.add_argument("--depth", type=int, default=6, help="deepest heading level")
    p.add_argument("--blocks", action="store_true", help="also list the blocks")
    p.add_argument("--kind", **kinds)
    p = command("search", cmd_search, "Search block titles, terms, statements and proofs by meaning and words.")
    p.add_argument("query", nargs="+")
    p.add_argument("--kind", **kinds)
    p.add_argument("--limit", type=int, default=15)
    p = command("term", cmd_term, "Search the defining blocks (definitions, constructions, ...) by meaning and words.")
    p.add_argument("query", nargs="+")
    p.add_argument("--limit", type=int, default=10)
    p = command("where", cmd_where, "Locate every @key: bibliography key or block id.")
    p.add_argument("key")
    p = command("deps", cmd_deps, "Print the uses of a block as a tree (--reverse: its users).")
    p.add_argument("id")
    p.add_argument("--reverse", action="store_true", help="the blocks that use it instead")
    p.add_argument("--depth", type=int, help="stop at this depth")
    p.add_argument("--all", action="store_true", help="follow `mentions` edges too")
    p = command("path", cmd_path, "Print a shortest chain of uses from SOURCE to TARGET.")
    p.add_argument("source")
    p.add_argument("target")
    p.add_argument("--all", action="store_true", help="follow `mentions` edges too")
    p = command("graph", cmd_graph, "Print the dot source of a block's neighbourhood.")
    p.add_argument("id")
    p.add_argument("--depth", type=int, default=2)
    p.add_argument("--both", action="store_true", help="also follow edges into the block")
    p.add_argument("--all", action="store_true", help="draw `mentions` edges too")
    command("stats", cmd_stats, "Count the blocks by kind and part of the book.")
    command("findings", cmd_findings, "Print the dependency-graph findings.")
    args = parser.parse_args()
    index = load(args.project, args.cache)
    args.func(index, args)


if __name__ == "__main__":
    main()
