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
import csv
import re
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


def indentation(prefix: str) -> int:
    return len(prefix.expandtabs(8))


def public(name: str) -> bool:
    return not name.startswith("_")


def scan_module(path: Path, root: Path) -> list[Notion]:
    relative = path.relative_to(root.parent).as_posix()
    notions = [Notion(relative, "<module>", "module", 1)]
    class_stack: list[tuple[int, str]] = []
    function_indents: list[int] = []

    for line_number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        match = DEFINITION.match(line)
        if match:
            level = indentation(match.group("indent"))
            while class_stack and level <= class_stack[-1][0]:
                class_stack.pop()
            while function_indents and level <= function_indents[-1]:
                function_indents.pop()

            kind = match.group("kind")
            name = match.group("name")
            if kind == "class":
                if public(name) and not function_indents:
                    prefix = ".".join(item[1] for item in class_stack)
                    qualified = f"{prefix}.{name}" if prefix else name
                    notions.append(Notion(relative, qualified, "class", line_number))
                class_stack.append((level, name))
                continue

            # A function nested inside another function is an implementation
            # detail.  Top-level functions and methods of public classes are
            # part of the archived mathematical surface.
            if public(name) and not function_indents:
                public_classes = [item[1] for item in class_stack if public(item[1])]
                if len(public_classes) == len(class_stack):
                    prefix = ".".join(public_classes)
                    qualified = f"{prefix}.{name}" if prefix else name
                    kind_name = "method" if prefix else "function"
                    if name.startswith("test_"):
                        kind_name = "specimen"
                    notions.append(Notion(relative, qualified, kind_name, line_number))
            function_indents.append(level)
            continue

        # Public module-level named values are part of the source surface too.
        # Sage modules commonly put their build body under an import guard, so
        # indentation alone does not distinguish module scope from function/class
        # scope.  The scope stacks above do.
        if not function_indents and not class_stack:
            assignment = ASSIGNMENT.match(line.lstrip())
            if assignment and public(assignment.group("name")):
                notions.append(
                    Notion(relative, assignment.group("name"), "binding", line_number)
                )

    return notions


def live_name_index(live_root: Path) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    if not live_root.exists():
        return result
    for path in sorted(live_root.rglob("*.py")):
        for line in path.read_text(errors="replace").splitlines():
            match = DEFINITION.match(line)
            if match and public(match.group("name")):
                result.setdefault(match.group("name"), set()).add(
                    path.relative_to(live_root.parent.parent.parent).as_posix()
                )
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
            writer.writerow(
                (
                    notion.module,
                    notion.qualified_name,
                    notion.kind,
                    notion.line,
                    len(candidates),
                    unique_hint,
                    "",
                    "unreviewed",
                )
            )

    public_notion_count = sum(notion.kind != "module" for notion in notions)
    print(
        f"wrote {args.output}: {len(modules)} modules, "
        f"{public_notion_count} public definitions"
    )


if __name__ == "__main__":
    main()
