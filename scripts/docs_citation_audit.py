#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["networkx>=3.4", "panflute>=2.3", "pydot>=3.0", "pyyaml>=6.0"]
# ///
"""Every citation in the docs book that names no result, with its context.

A citation of a whole work (`[@Vin75]`), or of a chapter, section or page of one
(`[@Hum90, Ch. 5]`), names no result, so the dependency graph draws no arrow for it
(`docs_dependency_graph.cited_results` decides what names a result). Such a
citation is either attribution or summary, which is correct prose, or a use of one
result of the work cited loosely, which should name that result. Only a reader can
tell which, so this audit lists each one with the paragraph around it, the block that
holds it (kind, id, and statement or proof) and the chapter line, grouped by work
with the most-cited work first. Reading one source then settles every loose citation
of it.

The dependency graph reports only the loose citations in proofs of logical blocks;
this audit lists all of them, in statements, commentary and running prose too.

Output: a Markdown report at --out, and one summary line on stdout.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml

_spec = importlib.util.spec_from_file_location(
    "docs_dependency_graph", Path(__file__).with_name("docs_dependency_graph.py"))
assert _spec and _spec.loader
graph = importlib.util.module_from_spec(_spec)
sys.modules["docs_dependency_graph"] = graph
_spec.loader.exec_module(graph)

FENCE_OPEN = re.compile(r"^(:{3,})\s*\{\.([\w-]+)([^}]*)\}")
FENCE_CLOSE = re.compile(r"^:{3,}\s*$")
BRACKET = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
CITE_ITEM = re.compile(r"^\s*-?@([\w+:.-]*[\w+])\s*,?\s*(.*?)\s*$", re.S)
NARRATIVE = re.compile(r"(?<![\w\[@-])@([A-Za-z][\w+:.-]*[\w+])")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z$\[(])")
CONTEXT = 600


def sentence(paragraph: str, key: str) -> str:
    """The sentences of `paragraph` around the first citation of `key`: the one that
    holds it and the one before, which usually says what the citation is for."""
    at = paragraph.find("@" + key)
    sentences = SENTENCE_END.split(paragraph)
    offset = 0
    for index, text in enumerate(sentences):
        offset += len(text) + 1
        if offset > at:
            context = " ".join(sentences[max(0, index - 1):index + 1])
            return context if len(context) <= CONTEXT else context[:CONTEXT] + " …"
    return paragraph[:CONTEXT]


@dataclass(frozen=True)
class Loose:
    key: str
    locator: str
    outside: str  # a result named after the brackets, as "Definition 3.6"; "" if none
    chapter: str
    line: int
    block: str  # "theorem thm:x (proof)", or "" for running prose
    paragraph: str


def is_bibliography_key(key: str) -> bool:
    if key.startswith(graph.QUARTO_CROSSREF_PREFIXES):
        return False
    return ":" not in key or key.startswith(graph.RESULT_KEY_PREFIXES)


# Text right after a citation that may name its result outside the brackets:
# "([@AEGS25], Definition 3.6)", "of [@AEGS25], Lemma 3.9", "@Nik80, Thm. 1.14.4".
OUTSIDE = re.compile(r"^\)?\s*,\s*([^;()\[\]]{1,80})")
# Where the text after a citation stops being its locator: a dash, a clause, a sentence.
LOCATOR_END = re.compile(r"\s+---|\s+--\s|:\s|\.\s+(?=[A-Z$])|\.$|,\s+(?![A-Z§(]|pp?\.|and\s|\d)")


def outside_locator(key: str, after: str) -> str:
    """The result named just after a citation with no locator of its own, or ""."""
    match = OUTSIDE.match(after)
    if not match:
        return ""
    text = LOCATOR_END.split(match.group(1), maxsplit=1)[0].strip(" ,")
    return text if graph.cited_results(key, text) else ""


def citations(paragraph: str) -> list[tuple[str, str, str]]:
    """(key, locator in the brackets, result named after the brackets) per citation."""
    found: list[tuple[str, str, str]] = []
    for bracket in BRACKET.finditer(paragraph):
        items = [CITE_ITEM.match(item) for item in bracket.group(1).split(";")]
        for match in filter(None, items):
            after = paragraph[bracket.end():] if len(items) == 1 and not match.group(2) else ""
            found.append((match.group(1), match.group(2), outside_locator(match.group(1), after)))
    rest = BRACKET.sub(" ", paragraph)
    for match in NARRATIVE.finditer(rest):
        found.append((match.group(1), "", outside_locator(match.group(1), rest[match.end():])))
    return found


def audit_chapter(path: Path, chapter: str) -> list[Loose]:
    out: list[Loose] = []
    stack: list[tuple[str, str]] = []  # (kind, id) of open divs
    last_closed = ""  # the block a following proof proves
    paragraph: list[str] = []
    start = 0

    def where() -> str:
        for kind, ident in reversed(stack):
            if kind == "proof":
                return f"proof of {last_closed}" if last_closed else "proof"
            if ident:
                return f"{kind} {ident} (statement)"
        return ""

    def flush() -> None:
        text = " ".join(paragraph).strip()
        for key, locator, outside in citations(text):
            if is_bibliography_key(key) and not graph.cited_results(key, locator):
                out.append(Loose(key, locator, outside, chapter, start, where(),
                                 sentence(text, key)))
        paragraph.clear()

    for number, line in enumerate(path.read_text().splitlines(), 1):
        opened = FENCE_OPEN.match(line)
        if (opened or FENCE_CLOSE.match(line) or not line.strip()
                or LIST_ITEM.match(line)):
            flush()
        if opened:
            ident = re.search(r"#([\w:.-]+)", opened.group(3))
            stack.append((opened.group(2), ident.group(1) if ident else ""))
            continue
        if FENCE_CLOSE.match(line):
            if stack:
                kind, ident = stack.pop()
                if kind != "proof" and ident:
                    last_closed = f"{kind} {ident}"
            continue
        if line.strip():
            if not paragraph:
                start = number
            paragraph.append(line.strip())
    flush()
    return out


def report(loose: list[Loose]) -> str:
    outside = [item for item in loose if item.outside]
    by_key: dict[str, list[Loose]] = defaultdict(list)
    for item in loose:
        if not item.outside:
            by_key[item.key].append(item)
    lines = ["# Citations that name no result", "",
             f"{len(loose)} citations. {len(outside)} name their result after the brackets; "
             "moving it inside makes it a node of the dependency graph. The other "
             f"{len(loose) - len(outside)}, of {len(by_key)} works, need a reading: "
             "attribution or summary (keep it), or a use of one result (name it).", "",
             "## Result named outside the brackets", ""]
    for item in sorted(outside, key=lambda i: (i.chapter, i.line)):
        lines.append(f"- `{item.chapter}:{item.line}` {item.block or 'prose'}: "
                     f"`[@{item.key}]` then \"{item.outside}\" → `[@{item.key}, {item.outside}]`")
    lines.append("")
    for key, items in sorted(by_key.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines += [f"## @{key} ({len(items)})", ""]
        # Proofs first: a loose citation there is most likely a use of one result.
        for item in sorted(items, key=lambda i: (not i.block.startswith("proof"),
                                                 not i.block, i.chapter, i.line)):
            cite = f"@{key}" + (f", {item.locator}" if item.locator else "")
            lines += [f"- `{item.chapter}:{item.line}` {item.block or 'prose'}: `[{cite}]`",
                      "", f"  > {item.paragraph}", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", type=Path, default=Path("."),
                        help="the Quarto project directory (holds _quarto.yml)")
    parser.add_argument("--out", type=Path, required=True, help="the Markdown report to write")
    args = parser.parse_args()
    config = yaml.safe_load((args.project / "_quarto.yml").read_text())
    loose = [item for chapter in graph.chapter_list(config["book"])
             for item in audit_chapter(args.project / chapter, chapter)]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report(loose))
    parts = defaultdict(int)
    for item in loose:
        parts["proof" if item.block.startswith("proof") else
              "statement" if item.block else "prose"] += 1
    print(f"docs-citation-audit: {len(loose)} citations name no result "
          f"({', '.join(f'{n} in {p}' for p, n in sorted(parts.items()))}) -> {args.out}")


if __name__ == "__main__":
    main()
