"""Combined report for source size, dependency shape, and review inventories."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .imports import ImportAnalysis, analyze_imports
from .metrics import TreeMetrics, analyze_metrics
from .patterns import PatternAnalysis, analyze_patterns


@dataclass(frozen=True)
class AnalysisReport:
    metrics: TreeMetrics
    imports: ImportAnalysis
    patterns: PatternAnalysis

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def analyze_tree(
    root: Path,
    *,
    package_prefix: str,
    foundation_prefixes: tuple[str, ...] = (),
    top: int = 20,
) -> AnalysisReport:
    return AnalysisReport(
        metrics=analyze_metrics(root, top=top),
        imports=analyze_imports(
            root,
            package_prefix=package_prefix,
            foundation_prefixes=foundation_prefixes,
            top=top,
        ),
        patterns=analyze_patterns(root, package_prefix=package_prefix),
    )


def _fmt_number(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:.1f}"


def render_markdown(report: AnalysisReport, *, top: int = 20) -> str:
    m = report.metrics
    i = report.imports
    p = report.patterns
    lines = [
        "# Source-tree complexity analysis",
        "",
        f"Analyzed `{m.root}` without importing the target package.",
        "",
        "## Tree summary",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Python files | {m.python_files} |",
        f"| Directories containing Python | {m.directories} |",
        f"| Physical lines | {m.physical_lines:,} |",
        f"| Token-bearing code lines | {m.code_lines:,} |",
        f"| Source bytes | {m.bytes:,} |",
        f"| Functions/methods | {m.functions:,} |",
        f"| Classes | {m.classes:,} |",
        f"| Functions >=100 lines | {m.functions_lines_ge_100} |",
        f"| Function complexity >=10 / >=20 / >=40 | {m.functions_complexity_ge_10} / {m.functions_complexity_ge_20} / {m.functions_complexity_ge_40} |",
        "",
        "Function length percentiles: "
        + ", ".join(f"{key}={_fmt_number(value)}" for key, value in m.function_line_percentiles.items())
        + ".",
        "",
        "Function complexity percentiles: "
        + ", ".join(f"{key}={_fmt_number(value)}" for key, value in m.function_complexity_percentiles.items())
        + ".",
        "",
        "## Dependency shape",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Import records | {i.imports_total:,} |",
        f"| Imports within analyzed package | {i.local_imports:,} |",
        f"| Nested imports | {i.nested_imports:,} |",
        f"| Imports through package aggregators | {i.aggregator_imports:,} |",
        f"| Files using package aggregators | {i.files_with_aggregator_imports:,} |",
        f"| Distinct local import edges | {i.edges:,} |",
        f"| Largest SCC | {i.largest_scc_size} modules |",
        f"| Largest SCC excluding package `__init__` aggregators | {i.largest_scc_without_aggregators} modules |",
        "",
    ]

    if i.top_aggregators:
        lines.extend(["### Most-used package aggregators", "", "| Module | Imports | Files |", "| --- | ---: | ---: |"])
        lines.extend(f"| `{module}` | {count} | {files} |" for module, count, files in i.top_aggregators[:top])
        lines.append("")

    if i.foundation_outward_imports:
        lines.extend(
            [
                "### Imports from configured foundation subtrees to outside theories",
                "",
                "These are review candidates, not automatic violations.",
                "",
            ]
        )
        for record in i.foundation_outward_imports[:top]:
            lines.append(f"- `{record.path}:{record.line}`: `{record.source}` -> `{record.target}`")
        lines.append("")

    lines.extend(
        [
            "## Architectural pattern inventory",
            "",
            "Counts are review inventories; context determines whether a site is valid.",
            "",
            "| Pattern | Count |",
            "| --- | ---: |",
            f"| Public top-level functions | {len(p.public_top_level_functions)} |",
            f"| Session-exported top-level functions | {len(p.session_exported_top_level_functions)} |",
            f"| `assert` statements | {len(p.asserts)} |",
            f"| `tuple(...)` calls | {len(p.tuple_calls)} |",
            f"| `list(...)` calls | {len(p.list_calls)} |",
            f"| `hasattr(...)` calls | {len(p.hasattr_calls)} |",
            f"| `getattr(...)` calls | {len(p.getattr_calls)} |",
            f"| `isinstance(...)` calls | {len(p.isinstance_calls)} |",
            f"| `except AttributeError` probes | {len(p.attribute_error_probes)} |",
            f"| `_preamble_*` attribute mentions | {len(p.preamble_attribute_mentions)} |",
            f"| `_preamble_*` attribute assignments | {len(p.preamble_attribute_assignments)} |",
            f"| Module-global dict caches | {len(p.global_dict_caches)} |",
            f"| Manual method grafts | {len(p.method_grafts)} |",
            f"| Mathematical collection `list`/`tuple` materializations | {len(p.mathematical_collection_materializations)} |",
            f"| Explicit loops exhausting named mathematical collections | {len(p.exhaustive_mathematical_collection_loops)} |",

            f"| Raw matrix/coordinate representation peeks | {len(p.raw_matrix_coordinate_peeks)} |",
            f"| Functions with `*args` | {len(p.variadic_positional_signatures)} |",
            f"| Functions with `**kwargs` | {len(p.variadic_keyword_signatures)} |",
            f"| Functions with a `None` default | {len(p.none_default_signatures)} |",
            f"| `pass` statements | {len(p.pass_statements)} |",
            f"| Exact duplicate function-body groups | {len(p.duplicate_function_bodies)} |",
            "",
            "## Largest files",
            "",
        ]
    )
    for metric in m.largest_files[:top]:
        lines.append(f"- `{metric.path}`: {metric.physical_lines:,} physical lines, {metric.code_lines:,} code lines")

    lines.extend(["", "## Most complex functions", ""])
    for metric in m.most_complex_functions[:top]:
        lines.append(
            f"- `{metric.path}:{metric.line}` `{metric.qualified_name}`: complexity {metric.complexity}, {metric.lines} lines"
        )

    lines.extend(["", "## Largest classes", ""])
    for metric in m.largest_classes[:top]:
        lines.append(f"- `{metric.path}:{metric.line}` `{metric.qualified_name}`: {metric.lines} lines")


    if p.session_exported_top_level_functions:
        lines.extend(["", "## Session-exported standalone functions", ""] )
        for location in p.session_exported_top_level_functions[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`")

    if p.global_dict_caches:
        lines.extend(["", "## Module-global dict caches", ""])
        for location in p.global_dict_caches[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`")

    if p.method_grafts:
        lines.extend(["", "## Manual method grafts", ""])
        for location in p.method_grafts[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`: `{location.detail}`")

    if p.mathematical_collection_materializations:
        lines.extend(["", "## Mathematical collection materializations", "", "Review candidates for finitary overfitting; backend serialization can be legitimate.", ""])
        for location in p.mathematical_collection_materializations[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`: `{location.detail}`")

    if p.exhaustive_mathematical_collection_loops:
        lines.extend(["", "## Explicit loops over named mathematical collections", "", "Review whether the mathematics requires exhaustion or should use a semantic/lazy construction.", ""])
        for location in p.exhaustive_mathematical_collection_loops[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`: `{location.detail}`")

    if p.raw_matrix_coordinate_peeks:
        lines.extend(["", "## Raw matrix/coordinate representation peeks", "", "Review whether rows/columns/bases are private engine serialization or premature semantic lowering.", ""])
        for location in p.raw_matrix_coordinate_peeks[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`: `{location.detail}`")

    if p.variadic_keyword_signatures or p.variadic_positional_signatures or p.none_default_signatures:
        lines.extend(["", "## Public-signature review triggers", "", "Review mathematical APIs for option bags, sentinel polymorphism, and ambiguous input shapes; private protocol adapters can be legitimate.", ""])
        for location in (*p.variadic_positional_signatures, *p.variadic_keyword_signatures, *p.none_default_signatures)[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`: `{location.detail}`")

    if p.pass_statements:
        lines.extend(["", "## `pass` statements", "", "Review mathematical sites for stubs/no-op branches; private engineering no-ops can be legitimate.", ""])
        for location in p.pass_statements[:top]:
            lines.append(f"- `{location.path}:{location.line}` `{location.symbol}`")

    if p.duplicate_function_bodies:
        lines.extend(["", "## Exact duplicate function bodies", ""])
        for group in p.duplicate_function_bodies[:top]:
            rendered = ", ".join(
                f"`{location.path}:{location.line}` `{location.symbol}`" for location in group.occurrences
            )
            lines.append(f"- {group.statement_count} statements: {rendered}")

    return "\n".join(lines) + "\n"


def render_json(report: AnalysisReport) -> str:
    return json.dumps(report.as_dict(), indent=2) + "\n"
