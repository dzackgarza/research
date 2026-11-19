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

A cited result of another work is a node too, of kind `reference`: a block that cites
`[@AEGS25, Lem. 3.9]` has an edge to the node `AEGS25 Lem. 3.9`, whose `work` is
`AEGS25`. Spellings of one result are one node ("Theorem 2" and "Thm. 2"); see
`cited_results`. A citation of a whole work, or of a chapter, section or page of one,
names no result: it says where something comes from or summarizes the work, so it makes
no node and no edge. Results of other works have no outgoing edges, so every chain of
uses ends at a definition, an uncited block or the literature.

A `::: {.proof}` div proves the numbered block that immediately precedes it in
the same enclosing block list. Edge attributes `statement` and `proof` record
which part of `a` cites `b`. `relation` is `uses` when both blocks belong to the
logical development (LOGICAL below) and `mentions` when either is commentary.

The chapters are parsed by pandoc (through panflute), in `book.chapters` order;
each node's `position` is its index in that order, and an edge's `forward` says
the cited block comes later. The site is not read in order, so a forward edge is
information, not a defect.

Findings, each one a defect in the book:
  - a reference to a theorem-family id that no block defines;
  - a cycle of `uses` edges (circular definitions or proofs);
  - a proof with no numbered block immediately before it;
  - an id that two blocks define;
  - a numbered block with no id (it is a node, keyed `<chapter>#<position>`, but
    nothing can cite it);
  - a pandoc warning while reading a chapter, such as an unclosed div;
  - a use with no citation: a logical block whose prose contains a term of two or
    more words that a definition, construction, notation or convention sets in bold,
    when no block that it reaches through citations defines that term. One-word terms
    are not checked, because the same word has different senses in different parts;
  - an unlocated citation: the proof of a logical block cites a whole work, or a chapter,
    section or page of one. If the proof rests on one result of that work, the citation
    must name it; if the proof only says where the argument comes from, the citation is
    attribution and belongs in the statement or in the prose around the block.

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
import dataclasses
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import networkx as nx
import panflute as pf
import yaml

# The theorem-family reference prefixes, as the amsthm-refs filter registers them.
AMSTHM_REFS = "_extensions/local/amsthm-refs/amsthm-refs.lua"

# Block kinds whose statement or proof is part of the logical development: a later
# proof can take the block as a premise. A citation between two of them is a `uses`
# edge. An observation is a stated fact with its proof, so it is logical; a conjecture
# is logical because a result can be proved conditionally on it.
LOGICAL = frozenset({
    "theorem", "lemma", "corollary", "proposition", "observation", "claim", "conjecture",
    "definition", "construction", "notation", "convention", "assumption",
})

# Block kinds that comment on the development and establish nothing in it. A citation
# to or from one of them is a `mentions` edge. An example illustrates and a remark or
# note points; an exercise, problem or question asks for work that the text does not
# do, so none of them can be a premise.
COMMENTARY = frozenset({
    "example", "remark", "note", "warning", "exercise", "problem", "question",
})

# The kind of a node that is one result of a cited work, keyed "<bibliography key>
# <locator>", as "AEGS25 Lem. 3.9". A result taken from a paper is a premise, so a citation
# of it by a logical block is a `uses` edge. A citation of a whole work, or of a chapter,
# section or page of one, names no result: it says where something comes from or
# summarizes the work, so it makes no node and no edge.
REFERENCE = "reference"
# Keys that name one result by themselves: a Stacks Project tag, an nLab page.
RESULT_KEY_PREFIXES = ("stacks-", "nlab:")
# The spellings of each kind of result, mapped to one abbreviation, so that "Theorem 2"
# and "Thm. 2" are one node. A numbered section counts as a result when it has a
# subsection number (§4.2); a chapter, a whole section (§2) or a page does not.
RESULT_LABELS = {
    "Thm.": ("theorems", "theorem", "thms", "thm", "th"),
    "Prop.": ("propositions", "proposition", "props", "prop"),
    "Lem.": ("lemmas", "lemmata", "lemma", "lems", "lem"),
    "Cor.": ("corollaries", "corollary", "cors", "cor"),
    "Def.": ("definitions", "definition", "defs", "defn", "def"),
    "Rem.": ("remarks", "remark", "rems", "rem", "rmk"),
    "Ex.": ("examples", "example", "exercises", "exercise", "exs", "exa", "ex"),
    "Constr.": ("constructions", "construction", "constr"),
    "Alg.": ("algorithms", "algorithm", "alg"),
    "Conj.": ("conjectures", "conjecture", "conj"),
    "Table": ("tables", "table", "tab"),
    "Fig.": ("figures", "figure", "fig"),
    "Obs.": ("observations", "observation", "obs"),
    "Fact": ("facts", "fact"),
    "Claim": ("claims", "claim"),
    "Not.": ("notations", "notation", "not"),
    "eq.": ("equations", "equation", "eqs", "eq"),
    "§": ("sections", "section", "secs", "sec", "§§", "§", "subsection"),
}
_LABEL = {alias: label for label, aliases in RESULT_LABELS.items() for alias in aliases}
_NUMBER = (r"\(?(?:[IVXLC]+\.)?[A-Z]?\d+(?:\.\d+)*[A-Za-z]?\)?(?:\([ivxlc\d]+\))?"
           r"|(?-i:[A-Z])(?![a-z])")
_RESULT = re.compile(
    r"(?<![\w.])(" + "|".join(sorted(map(re.escape, _LABEL), key=len, reverse=True))
    + r")\.?\s*((?:" + _NUMBER + r")(?:\s*(?:,|and|&)\s*(?:" + _NUMBER + r"))*)",
    re.IGNORECASE)
# A Stacks Project tag in a locator: "Tag 0109", "Tags 01DQ and 02F5".
_TAGS = re.compile(r"\bTags?\s+([0-9A-Z]{4}(?:\s*(?:,|and)\s*[0-9A-Z]{4})*)")
# A Bourbaki numbered paragraph: "Ch. V §3 no. 1".
_BOURBAKI = re.compile(r"(?:(?:Ch\.|Chapter)\s*([IVXLC\d]+),?\s*)?§\s*(\d+)\s*no\.\s*(\d+)")
# A bare item or equation number with a dot: "4.6", "V.3.3", "(2.1.10)".
_BARE_NUMBER = re.compile(r"(?<![\w.§])\(?(?:[IVXLC]+\.\d+(?:\.\d+)*|\d+(?:\.\d+)+)\)?(?![\w.])")


def cited_results(key: str, locator: str) -> list[str]:
    """The node ids of the results that `[@key, locator]` names; empty for a whole work."""
    if key.startswith(RESULT_KEY_PREFIXES):
        return [key]
    out: list[str] = []

    def add(node: str) -> None:
        if node not in out:
            out.append(node)

    rest = locator
    for match in _TAGS.finditer(rest):
        for tag in re.split(r"\s*(?:,|and)\s*", match.group(1)):
            add(f"{key} Tag {tag}")
    rest = _TAGS.sub(" ", rest)
    # O'Meara's item numbers, "42:16", read before a section label can take the "42".
    for match in re.finditer(r"(?<![\w.:])\d+:\d+(?![\w:])", rest):
        add(f"{key} {match.group(0)}")
    rest = re.sub(r"(?<![\w.:])\d+:\d+(?![\w:])", " ", rest)
    for match in _BOURBAKI.finditer(rest):
        chapter = f"Ch. {match.group(1)} " if match.group(1) else ""
        add(f"{key} {chapter}§{match.group(2)} no. {match.group(3)}")
    rest = _BOURBAKI.sub(" ", rest)
    for match in _RESULT.finditer(rest):
        label = _LABEL[match.group(1).lower()]
        for number in re.split(r"\s*(?:,|and|&)\s*", match.group(2)):
            # A section is a result only at subsection depth: §4.2, §III.2, §3D.
            # A parenthesized number after another label is an equation: "§III.2 and (2.9)".
            if number.startswith("(") and label != "eq.":
                add(f"{key} {number}")
                continue
            if not number or (label == "§" and "." not in number and not number[-1].isalpha()):
                continue
            add(f"{key} {label}{'' if label == '§' else ' '}{number}")
    # A page reference is never a result; drop it before reading bare numbers.
    rest = re.sub(r"\bpp?\.\s*\S+", " ", _RESULT.sub(" ", rest))
    for match in _BARE_NUMBER.finditer(rest):
        add(f"{key} {match.group(0)}")
    return out
# Quarto's own cross-reference keys (sections, figures, tables, equations), which are
# neither blocks nor works.
QUARTO_CROSSREF_PREFIXES = ("sec-", "fig-", "tbl-", "eq-")

# Block kinds whose bold phrases are defined terms.
DEFINING = frozenset({"definition", "construction", "notation", "convention"})
# A span of this class holds words that read as a defined term but are meant in another
# sense, as "right adjoints" of a functor beside the right adjoints of a pairing. The
# uncited-use check skips them; the page renders them as plain text.
OTHER_SENSE = "other-sense"


class Kind(StrEnum):
    DANGLING = "dangling"
    CYCLE = "cycle"
    ORPHAN_PROOF = "orphan-proof"
    DUPLICATE_ID = "duplicate-id"
    MISSING_ID = "missing-id"
    UNCITED_TERM = "uncited-term"
    PARSE_WARNING = "parse-warning"
    UNLOCATED_CITATION = "unlocated-citation"


@dataclass(frozen=True)
class Finding:
    """One defect: its kind, the chapter it is in, the block ids it concerns, a detail.

    kind is one of "dangling" (blocks = [citing block, missing id]), "cycle" (the
    blocks of the cycle, in order), "orphan-proof" (no blocks), "duplicate-id"
    ([id]), "missing-id" ([the node key `<chapter>#<position>`]), "uncited-term"
    ([using block, defining blocks ...]; detail = the term), "parse-warning" (no
    blocks; detail = pandoc's warning, such as an unclosed div, after which the
    chapter's blocks are nested wrongly) and "unlocated-citation" ([citing block];
    detail = the citation, as "@Nik80" or "@Hum90, Ch. 5").
    """

    kind: Kind
    chapter: str
    blocks: tuple[str, ...] = ()
    detail: str = ""

    def __str__(self) -> str:
        detail = f' "{self.detail}"' if self.detail else ""
        return f"{self.chapter}: {self.kind}{detail} {' '.join(self.blocks)}".rstrip()


def parse(path: Path) -> tuple[pf.Doc, list[str]]:
    """The chapter's pandoc AST, and the warnings pandoc gave while reading it."""
    done = subprocess.run(["pandoc", "-f", "markdown", "-t", "json", str(path)],
                          capture_output=True, text=True, check=True)
    doc = pf.load(io.StringIO(done.stdout))
    warnings = [" ".join(line.split()) for line in done.stderr.splitlines() if line.strip()]
    return doc, warnings


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


@dataclass
class Contents:
    """What one statement or proof holds, not counting nested numbered blocks or proofs."""

    # (citation key, locator): `[@AEGS25, Lem. 3.9]` is ("AEGS25", "Lem. 3.9").
    cited: list[tuple[str, str]] = dataclasses.field(default_factory=list)
    # The prose words, lowercased; mathematics and citations are left out.
    text: str = ""
    # The bold phrases (`**term**`) that contain no mathematics, lowercased.
    terms: set[str] = dataclasses.field(default_factory=set)


def contents(elem: pf.Element, block_classes: set[str]) -> Contents:
    found = Contents()
    words: list[str] = []

    def walk(e: pf.Element) -> None:
        if isinstance(e, pf.Div) and e is not elem and (
            set(e.classes) & (block_classes | {"proof"})
        ):
            return
        if isinstance(e, pf.Cite):
            found.cited.extend((c.id, pf.stringify(pf.Span(*c.suffix)).strip(" ,"))
                               for c in e.citations)
            return
        if isinstance(e, pf.Span) and OTHER_SENSE in e.classes:
            words.append(" ")
            return
        if isinstance(e, pf.Str):
            words.append(e.text)
        elif isinstance(e, pf.Math):
            # A formula stays a token, so "marked $K3$ surface" does not read as
            # "marked surface".
            words.append(" \u00a4 ")
        elif isinstance(e, (pf.Space, pf.SoftBreak, pf.LineBreak)):
            words.append(" ")
        elif isinstance(e, pf.Strong) and not any(
                isinstance(m, pf.Math) for m in _descendants(e)):
            term = " ".join(pf.stringify(e).lower().split()).strip(" .,;:")
            if re.search(r"[a-z]{3}", term) and " " in term:
                found.terms.add(term)
        for child in children(e):
            walk(child)

    walk(elem)
    found.text = " ".join("".join(words).lower().split())
    return found


def _descendants(e: pf.Element) -> list[pf.Element]:
    out: list[pf.Element] = []
    for child in children(e):
        out.append(child)
        out.extend(_descendants(child))
    return out


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
    unclassified = block_classes - LOGICAL - COMMENTARY
    if unclassified:
        sys.exit(f"docs-deps: block kinds {sorted(unclassified)} are neither LOGICAL nor "
                 "COMMENTARY; classify them in scripts/docs_dependency_graph.py")
    prefixes = theorem_prefixes(project)
    graph = nx.DiGraph()
    findings: list[Finding] = []
    # (source id, cited id, part) in reading order; resolved once every block is known
    citations: list[tuple[str, str, str, str]] = []
    # Each block's prose (statement and proof), and each bold term's defining blocks.
    prose: dict[str, str] = {}
    definers: dict[str, set[str]] = {}

    position = 0
    for chapter in chapter_list(config["book"]):
        doc, warnings = parse(project / chapter)
        for warning in warnings:
            findings.append(Finding(Kind.PARSE_WARNING, chapter, (), warning))

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
                        findings.append(Finding(Kind.MISSING_ID, chapter, (ident,)))
                    if ident in graph:
                        findings.append(Finding(Kind.DUPLICATE_ID, chapter, (ident,)))
                    graph.add_node(
                        ident,
                        kind=sorted(kinds)[0],
                        chapter=chapter,
                        position=position,
                        title=block.attributes.get("title", ""),
                        proved=False,
                    )
                    position += 1
                    found = contents(block, block_classes)
                    for cited, locator in found.cited:
                        citations.append((chapter, ident, cited, locator, "statement"))
                    prose[ident] = found.text
                    if graph.nodes[ident]["kind"] in DEFINING:
                        for term in found.terms:
                            definers.setdefault(term, set()).add(ident)
                    previous = ident
                elif isinstance(block, pf.Div) and "proof" in block.classes:
                    if previous is None:
                        findings.append(Finding(Kind.ORPHAN_PROOF, chapter))
                    else:
                        graph.nodes[previous]["proved"] = True
                        found = contents(block, block_classes)
                        for cited, locator in found.cited:
                            citations.append((chapter, previous, cited, locator, "proof"))
                        prose[previous] += " " + found.text
                    previous = None
                else:
                    previous = None
                for sub in block_lists(block):
                    visit_list(sub)

        visit_list(list(doc.content))

    def add_edge(source: str, target: str, part: str) -> None:
        if target == source:
            return
        if not graph.has_edge(source, target):
            graph.add_edge(source, target, statement=False, proof=False)
        graph.edges[source, target][part] = True

    for chapter, source, cited, locator, part in citations:
        if cited in graph:
            add_edge(source, cited, part)
            continue
        if ":" in cited and cited.split(":", 1)[0] in prefixes:
            findings.append(Finding(Kind.DANGLING, chapter, (source, cited)))
            continue
        if cited.startswith(QUARTO_CROSSREF_PREFIXES):
            continue
        # A bibliography key. Each result it names is a node; its page is the citing
        # chapter, whose bibliography holds the work as `#ref-<key>`.
        results = cited_results(cited, locator)
        for result in results:
            if result not in graph:
                graph.add_node(result, kind=REFERENCE, work=cited, chapter=chapter,
                               position=-1, title=result, proved=False)
            add_edge(source, result, part)
        if not results and part == "proof" and graph.nodes[source]["kind"] in LOGICAL:
            findings.append(Finding(Kind.UNLOCATED_CITATION, chapter, (source,),
                                    f"@{cited}" + (f", {locator}" if locator else "")))

    for source, target, data in graph.edges(data=True):
        data["forward"] = graph.nodes[target]["position"] > graph.nodes[source]["position"]
        data["relation"] = ("uses" if graph.nodes[source]["kind"] in LOGICAL
                            and graph.nodes[target]["kind"] in LOGICAL | {REFERENCE}
                            else "mentions")
    uses = graph.edge_subgraph(
        (u, v) for u, v, r in graph.edges(data="relation") if r == "uses")
    for component in nx.strongly_connected_components(uses):
        if len(component) > 1:
            cycle = [u for u, _ in nx.find_cycle(uses.subgraph(component))]
            findings.append(Finding(Kind.CYCLE, graph.nodes[cycle[0]]["chapter"], tuple(cycle)))
    findings.extend(uncited_terms(graph, prose, definers))
    return graph, findings


def uncited_terms(graph: nx.DiGraph, prose: dict[str, str],
                  definers: dict[str, set[str]]) -> list[Finding]:
    """Uses of a defined term by a block that cites none of the blocks defining it.

    A defining block names its term in bold. A block of the logical development whose
    prose contains that term (or its plural), that defines it nowhere itself and that
    cites none of its defining blocks, uses the definition without a citation, which the
    citation edges cannot show.
    """
    if not definers:
        return []
    # "long roots" and "long root" are one term: a plural folds into its singular.
    for term in sorted(definers):
        for suffix in ("es", "s"):
            if term.endswith(suffix) and term[:-len(suffix)] in definers:
                definers[term[:-len(suffix)]] |= definers.pop(term)
                break
    terms = sorted(definers, key=len, reverse=True)
    pattern = re.compile(r"(?<![\w-])(" + "|".join(map(re.escape, terms)) + r")(?:s|es)?(?![\w-])")
    out: list[Finding] = []
    for ident, text in prose.items():
        data = graph.nodes[ident]
        if data["kind"] not in LOGICAL:
            continue
        cited = nx.descendants(graph, ident)
        for term in sorted({m.group(1) for m in pattern.finditer(text)}):
            owners = definers[term]
            if ident in owners or cited & owners:
                continue
            out.append(Finding(Kind.UNCITED_TERM, data["chapter"],
                               (ident, *sorted(owners)), term))
    return out


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
        [dataclasses.asdict(f) for f in findings], indent=1))
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
    works = sum(1 for _, kind in graph.nodes(data="kind") if kind == REFERENCE)
    print(f"docs-deps: {graph.number_of_nodes() - works} blocks, {works} cited results, "
          f"{graph.number_of_edges()} edges, "
          f"{len(findings)} findings -> {args.out}", file=sys.stderr)
    if args.check and findings:
        sys.exit(1)


if __name__ == "__main__":
    main()
