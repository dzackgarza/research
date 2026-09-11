#!/usr/bin/env python3
"""Generate the archive-reconciliation denominator from source definitions.

This is intentionally source-only: terminal-T owns execution of the archived Sage
modules.  The inventory enumerates every archived ``.sage``/``.py`` module and
its public definition surface, then records exact-name candidates in the live
preamble.  A name match is evidence for inspection, not a reconciliation
disposition, so every newly discovered notion remains ``unreviewed`` until its
mathematics is compared at the live owner.
"""

from __future__ import annotations

import argparse
import ast
import csv
import io
import re
import tokenize
from dataclasses import dataclass
from pathlib import Path

DEFINITION = re.compile(r"^(?P<indent>[ \t]*)(?P<kind>class|def)\s+(?P<name>[A-Za-z_]\w*)\b")
ASSIGNMENT = re.compile(
    r"^(?P<name>[A-Za-z][A-Za-z0-9_]*)\s*(?::[^=]+)?=(?!=)"
)


@dataclass(frozen=True)
class Notion:
    module: str
    qualified_name: str
    kind: str
    line: int


def semantic_scopes(text: str) -> dict[int, tuple[tuple[str, str], ...]]:
    """Return enclosing class/function scopes at each token-bearing source line.

    Python's tokenizer is lexical rather than grammatical, so it handles Sage
    syntax such as ``R.<x> = ...`` while still supplying exact INDENT/DEDENT
    tokens.  Control-flow indentation is deliberately not a semantic scope:
    only class/function suites affect whether a name is module-public.
    """
    scopes: list[tuple[int, str, str]] = []
    pending: tuple[str, str] | None = None
    pending_kind: str | None = None
    depth = 0
    result: dict[int, tuple[tuple[str, str], ...]] = {}
    tokens = tokenize.generate_tokens(io.StringIO(text).readline)
    try:
        for token in tokens:
            token_type, value, start, _end, _line = token
            if token_type == tokenize.DEDENT:
                depth -= 1
                while scopes and scopes[-1][0] > depth:
                    scopes.pop()
                continue
            if token_type == tokenize.INDENT:
                depth += 1
                if pending is not None:
                    kind, name = pending
                    scopes.append((depth, kind, name))
                    pending = None
                continue
            if token_type in {
                tokenize.ENCODING,
                tokenize.NL,
                tokenize.NEWLINE,
                tokenize.COMMENT,
                tokenize.ENDMARKER,
            }:
                continue
            result.setdefault(start[0], tuple((kind, name) for _d, kind, name in scopes))
            if token_type == tokenize.NAME and value in {"class", "def"}:
                pending_kind = value
                continue
            if pending_kind is not None and token_type == tokenize.NAME:
                pending = (pending_kind, value)
                pending_kind = None
    except (IndentationError, tokenize.TokenError):
        # The inventory must still name the module even if an archived source is
        # lexically incomplete.  Definitions before the lexical failure remain
        # available in ``result``.
        pass
    return result


def declared_exports(text: str) -> tuple[str, ...] | None:
    r"""Return a static ``__all__`` list when the archived module declares one."""
    match = re.search(r"(?ms)^[ \t]*__all__\s*=\s*\[(.*?)^[ \t]*\]", text)
    if match is None:
        return None
    return tuple(
        name
        for _quote, name in re.findall(
            r"([\"'])([A-Za-z_][A-Za-z0-9_]*)\1", match.group(1)
        )
    )


def public(name: str) -> bool:
    return not name.startswith("_")


def scan_module(path: Path, root: Path) -> list[Notion]:
    relative = path.relative_to(root.parent).as_posix()
    notions = [Notion(relative, "<module>", "module", 1)]
    text = path.read_text(errors="replace")
    scopes_by_line = semantic_scopes(text)

    for line_number, line in enumerate(text.splitlines(), 1):
        scopes = scopes_by_line.get(line_number, ())
        functions = tuple(name for kind, name in scopes if kind == "def")
        classes = tuple(name for kind, name in scopes if kind == "class")
        match = DEFINITION.match(line)
        if match:
            kind = match.group("kind")
            name = match.group("name")
            if public(name) and not functions and all(public(item) for item in classes):
                prefix = ".".join(classes)
                qualified = f"{prefix}.{name}" if prefix else name
                if kind == "class":
                    kind_name = "class"
                elif name.startswith("test_"):
                    kind_name = "specimen"
                else:
                    kind_name = "method" if prefix else "function"
                notions.append(Notion(relative, qualified, kind_name, line_number))
            continue

        # Module-level control-flow guards do not hide mathematical bindings;
        # class and function scopes do.
        if not scopes:
            assignment = ASSIGNMENT.match(line.lstrip())
            if assignment and public(assignment.group("name")):
                notions.append(
                    Notion(relative, assignment.group("name"), "binding", line_number)
                )

    exports = declared_exports(text)
    if exports is None:
        return notions

    exported = set(exports)
    filtered = [notions[0]]
    represented = set()
    for notion in notions[1:]:
        root_name = notion.qualified_name.split(".", 1)[0]
        if root_name in exported:
            filtered.append(notion)
            represented.add(root_name)
    for name in exports:
        if name not in represented:
            filtered.append(Notion(relative, name, "reexport", 1))
    return filtered


def live_name_index(live_root: Path) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    if not live_root.exists():
        return result
    for path in sorted(live_root.rglob("*.py")):
        for notion in scan_module(path, live_root):
            if notion.kind == "module" or "." in notion.qualified_name:
                continue
            result.setdefault(notion.qualified_name, set()).add(path.as_posix())
    return result


def reconciliation_metadata(test_root: Path) -> dict[str, dict[str, object]]:
    r"""Read archive dispositions from source-backed reconciliation specimens."""
    result: dict[str, dict[str, object]] = {}
    if not test_root.exists():
        return result
    for path in sorted(test_root.rglob("test_*archive_reconciliation.py")):
        source = path.read_text()
        if "ARCHIVE_RECONCILIATION" not in source:
            continue
        tree = ast.parse(source, filename=str(path))
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if not any(isinstance(target, ast.Name) and target.id == "ARCHIVE_RECONCILIATION" for target in targets):
                continue
            value = ast.literal_eval(node.value)
            module = value["archive_module"]
            if module in result and result[module] != value:
                raise ValueError(f"conflicting archive reconciliation metadata for {module}")
            result[module] = value
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive-root", type=Path, default=Path("archives/preamble"))
    parser.add_argument(
        "--live-root",
        type=Path,
        default=Path("src/dzack_research/preamble"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("computations/reports/archive_reconciliation_inventory.tsv"),
    )
    parser.add_argument("--test-root", type=Path, default=Path("tests"))
    args = parser.parse_args()

    modules = sorted(
        path
        for path in args.archive_root.rglob("*")
        if path.is_file() and path.suffix in {".py", ".sage"}
    )
    notions = [
        notion
        for module in modules
        for notion in scan_module(module, args.archive_root)
    ]
    live = live_name_index(args.live_root)
    reconciled = reconciliation_metadata(args.test_root)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            (
                "archive_module",
                "qualified_name",
                "kind",
                "archive_line",
                "name_match_count",
                "unique_name_match_hint",
                "live_owner",
                "disposition",
            )
        )
        for notion in notions:
            short_name = notion.qualified_name.rsplit(".", 1)[-1]
            candidates = () if short_name == "<module>" else tuple(sorted(live.get(short_name, ())))
            unique_hint = candidates[0] if len(candidates) == 1 else ""
            metadata = reconciled.get(notion.module)
            if metadata is None:
                live_owner, disposition = "", "unreviewed"
            else:
                overrides = metadata.get("owner_overrides", {})
                live_owner = overrides.get(
                    notion.qualified_name, metadata["live_owner"]
                )
                disposition = metadata["disposition"]
            writer.writerow(
                (
                    notion.module,
                    notion.qualified_name,
                    notion.kind,
                    notion.line,
                    len(candidates),
                    unique_hint,
                    live_owner,
                    disposition,
                )
            )

    public_notion_count = sum(notion.kind != "module" for notion in notions)
    print(
        f"wrote {args.output}: {len(modules)} modules, "
        f"{public_notion_count} public definitions"
    )


if __name__ == "__main__":
    main()
