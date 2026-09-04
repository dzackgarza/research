"""CLI for static complexity and architecture analysis."""

from __future__ import annotations

import argparse
from pathlib import Path

from .report import analyze_tree, render_json, render_markdown


def _default_root() -> Path:
    return Path(__file__).resolve().parents[2] / "preamble"


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze Python source-tree complexity without importing it.")
    parser.add_argument("root", nargs="?", type=Path, default=_default_root())
    parser.add_argument("--package-prefix", default="dzack_research.preamble")
    parser.add_argument(
        "--foundation-prefix",
        action="append",
        default=["categories.abstract_categories"],
        help="Relative package prefix whose outward imports should be inventoried; repeatable.",
    )
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    report = analyze_tree(
        args.root,
        package_prefix=args.package_prefix,
        foundation_prefixes=tuple(args.foundation_prefix),
        top=args.top,
    )
    output = render_json(report) if args.format == "json" else render_markdown(report, top=args.top)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
