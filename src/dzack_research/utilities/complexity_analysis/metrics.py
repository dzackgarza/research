"""AST and source-size metrics for a Python source tree."""

from __future__ import annotations

import ast
import io
import tokenize
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class ScopeMetric:
    path: str
    qualified_name: str
    kind: str
    line: int
    end_line: int
    lines: int
    complexity: int


@dataclass(frozen=True)
class FileMetric:
    path: str
    physical_lines: int
    code_lines: int
    bytes: int
    functions: int
    classes: int


@dataclass(frozen=True)
class TreeMetrics:
    root: str
    python_files: int
    directories: int
    physical_lines: int
    code_lines: int
    bytes: int
    functions: int
    classes: int
    function_line_percentiles: dict[str, float]
    class_line_percentiles: dict[str, float]
    function_complexity_percentiles: dict[str, float]
    functions_complexity_ge_10: int
    functions_complexity_ge_20: int
    functions_complexity_ge_40: int
    functions_lines_ge_100: int
    largest_files: tuple[FileMetric, ...]
    largest_functions: tuple[ScopeMetric, ...]
    largest_classes: tuple[ScopeMetric, ...]
    most_complex_functions: tuple[ScopeMetric, ...]

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _python_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.py") if "__pycache__" not in path.parts)


def _code_line_count(source: str) -> int:
    lines: set[int] = set()
    ignored = {
        tokenize.ENCODING,
        tokenize.ENDMARKER,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.NEWLINE,
        tokenize.NL,
        tokenize.COMMENT,
    }
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for token in tokens:
            if token.type not in ignored and token.string.strip():
                lines.add(token.start[0])
    except (IndentationError, tokenize.TokenError):
        return sum(1 for line in source.splitlines() if line.strip() and not line.lstrip().startswith("#"))
    return len(lines)


def _complexity(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    """Return a small McCabe-style branch-count proxy for one function."""

    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.score = 1

        def visit_If(self, child: ast.If) -> None:
            self.score += 1
            self.generic_visit(child)

        def visit_For(self, child: ast.For) -> None:
            self.score += 1
            self.generic_visit(child)

        def visit_AsyncFor(self, child: ast.AsyncFor) -> None:
            self.score += 1
            self.generic_visit(child)

        def visit_While(self, child: ast.While) -> None:
            self.score += 1
            self.generic_visit(child)

        def visit_IfExp(self, child: ast.IfExp) -> None:
            self.score += 1
            self.generic_visit(child)

        def visit_BoolOp(self, child: ast.BoolOp) -> None:
            self.score += max(0, len(child.values) - 1)
            self.generic_visit(child)

        def visit_Try(self, child: ast.Try) -> None:
            self.score += len(child.handlers)
            self.generic_visit(child)

        def visit_Match(self, child: ast.Match) -> None:
            self.score += len(child.cases)
            self.generic_visit(child)

        def visit_comprehension(self, child: ast.comprehension) -> None:
            self.score += len(child.ifs)
            self.generic_visit(child)

        def visit_FunctionDef(self, child: ast.FunctionDef) -> None:
            if child is node:
                self.generic_visit(child)

        def visit_AsyncFunctionDef(self, child: ast.AsyncFunctionDef) -> None:
            if child is node:
                self.generic_visit(child)

        def visit_ClassDef(self, child: ast.ClassDef) -> None:
            return

    visitor = Visitor()
    visitor.visit(node)
    return visitor.score


def _percentiles(values: list[int]) -> dict[str, float]:
    if not values:
        return {key: 0.0 for key in ("p50", "p90", "p95", "p99", "max")}
    ordered = sorted(values)

    def q(p: float) -> float:
        if len(ordered) == 1:
            return float(ordered[0])
        position = p * (len(ordered) - 1)
        lower = int(position)
        upper = min(lower + 1, len(ordered) - 1)
        fraction = position - lower
        return ordered[lower] * (1 - fraction) + ordered[upper] * fraction

    return {
        "p50": q(0.50),
        "p90": q(0.90),
        "p95": q(0.95),
        "p99": q(0.99),
        "max": float(max(ordered)),
    }


def _scope_metrics(tree: ast.AST, relative_path: str) -> tuple[list[ScopeMetric], list[ScopeMetric]]:
    functions: list[ScopeMetric] = []
    classes: list[ScopeMetric] = []

    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.stack: list[str] = []

        def _record(self, node: ast.AST, name: str, kind: str) -> None:
            line = getattr(node, "lineno", 0)
            end_line = getattr(node, "end_lineno", line)
            metric = ScopeMetric(
                path=relative_path,
                qualified_name=".".join([*self.stack, name]),
                kind=kind,
                line=line,
                end_line=end_line,
                lines=max(0, end_line - line + 1),
                complexity=_complexity(node) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) else 0,
            )
            (functions if kind == "function" else classes).append(metric)

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            self._record(node, node.name, "class")
            self.stack.append(node.name)
            self.generic_visit(node)
            self.stack.pop()

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            self._record(node, node.name, "function")
            self.stack.append(node.name)
            self.generic_visit(node)
            self.stack.pop()

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            self._record(node, node.name, "function")
            self.stack.append(node.name)
            self.generic_visit(node)
            self.stack.pop()

    Visitor().visit(tree)
    return functions, classes


def analyze_metrics(root: Path, *, top: int = 20) -> TreeMetrics:
    root = root.resolve()
    file_metrics: list[FileMetric] = []
    function_metrics: list[ScopeMetric] = []
    class_metrics: list[ScopeMetric] = []

    for path in _python_files(root):
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(root))
        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError:
            tree = ast.Module(body=[], type_ignores=[])
        functions, classes = _scope_metrics(tree, rel)
        function_metrics.extend(functions)
        class_metrics.extend(classes)
        file_metrics.append(
            FileMetric(
                path=rel,
                physical_lines=len(source.splitlines()),
                code_lines=_code_line_count(source),
                bytes=len(source.encode("utf-8")),
                functions=len(functions),
                classes=len(classes),
            )
        )

    function_lines = [metric.lines for metric in function_metrics]
    class_lines = [metric.lines for metric in class_metrics]
    complexities = [metric.complexity for metric in function_metrics]
    dirs = {path.parent for path in _python_files(root)}

    return TreeMetrics(
        root=str(root),
        python_files=len(file_metrics),
        directories=len(dirs),
        physical_lines=sum(metric.physical_lines for metric in file_metrics),
        code_lines=sum(metric.code_lines for metric in file_metrics),
        bytes=sum(metric.bytes for metric in file_metrics),
        functions=len(function_metrics),
        classes=len(class_metrics),
        function_line_percentiles=_percentiles(function_lines),
        class_line_percentiles=_percentiles(class_lines),
        function_complexity_percentiles=_percentiles(complexities),
        functions_complexity_ge_10=sum(value >= 10 for value in complexities),
        functions_complexity_ge_20=sum(value >= 20 for value in complexities),
        functions_complexity_ge_40=sum(value >= 40 for value in complexities),
        functions_lines_ge_100=sum(value >= 100 for value in function_lines),
        largest_files=tuple(sorted(file_metrics, key=lambda item: item.physical_lines, reverse=True)[:top]),
        largest_functions=tuple(sorted(function_metrics, key=lambda item: item.lines, reverse=True)[:top]),
        largest_classes=tuple(sorted(class_metrics, key=lambda item: item.lines, reverse=True)[:top]),
        most_complex_functions=tuple(sorted(function_metrics, key=lambda item: item.complexity, reverse=True)[:top]),
    )
