"""Static import-graph analysis, including nested imports and SCCs."""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class ImportRecord:
    source: str
    target: str
    path: str
    line: int
    nested: bool
    through_aggregator: bool


@dataclass(frozen=True)
class ImportAnalysis:
    package_prefix: str
    imports_total: int
    local_imports: int
    nested_imports: int
    aggregator_imports: int
    files_with_aggregator_imports: int
    edges: int
    largest_scc_size: int
    largest_scc_without_aggregators: int
    largest_scc: tuple[str, ...]
    largest_scc_no_aggregators: tuple[str, ...]
    top_aggregators: tuple[tuple[str, int, int], ...]
    foundation_outward_imports: tuple[ImportRecord, ...]

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _module_map(root: Path, package_prefix: str) -> tuple[dict[Path, str], set[str]]:
    by_path: dict[Path, str] = {}
    aggregators: set[str] = set()
    for path in sorted(root.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        rel = path.relative_to(root)
        parts = list(rel.parts)
        if parts[-1] == "__init__.py":
            module_parts = parts[:-1]
        else:
            module_parts = [*parts[:-1], path.stem]
        suffix = ".".join(module_parts)
        module = package_prefix if not suffix else f"{package_prefix}.{suffix}"
        by_path[path.resolve()] = module
        if path.name == "__init__.py":
            aggregators.add(module)
    return by_path, aggregators


def _resolve_from(source_package: str, module: str | None, level: int) -> str:
    if level == 0:
        return module or ""
    package_parts = source_package.split(".")
    ascend = level - 1
    base = package_parts[: len(package_parts) - ascend] if ascend else package_parts.copy()
    if module:
        base.extend(module.split("."))
    return ".".join(base)


def _tarjan(nodes: set[str], edges: set[tuple[str, str]]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {node: [] for node in nodes}
    for source, target in edges:
        if source in adjacency and target in adjacency:
            adjacency[source].append(target)

    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    components: list[list[str]] = []

    def strongconnect(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for target in adjacency[node]:
            if target not in indices:
                strongconnect(target)
                lowlinks[node] = min(lowlinks[node], lowlinks[target])
            elif target in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[target])
        if lowlinks[node] == indices[node]:
            component: list[str] = []
            while True:
                target = stack.pop()
                on_stack.remove(target)
                component.append(target)
                if target == node:
                    break
            components.append(component)

    for node in sorted(nodes):
        if node not in indices:
            strongconnect(node)
    return components


def analyze_imports(
    root: Path,
    *,
    package_prefix: str,
    foundation_prefixes: tuple[str, ...] = (),
    top: int = 20,
) -> ImportAnalysis:
    root = root.resolve()
    path_modules, aggregators = _module_map(root, package_prefix)
    modules = set(path_modules.values())
    records: list[ImportRecord] = []

    for path, source_module in path_modules.items():
        source = path.read_text(encoding="utf-8")
        source_package = source_module if path.name == "__init__.py" else source_module.rpartition(".")[0]
        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError:
            continue

        class Visitor(ast.NodeVisitor):
            def __init__(self) -> None:
                self.scope_depth = 0

            def _record(self, target: str, line: int) -> None:
                if not target:
                    return
                local = target == package_prefix or target.startswith(f"{package_prefix}.")
                records.append(
                    ImportRecord(
                        source=source_module,
                        target=target,
                        path=str(path.relative_to(root)),
                        line=line,
                        nested=self.scope_depth > 0,
                        through_aggregator=local and target in aggregators,
                    )
                )

            def visit_Import(self, node: ast.Import) -> None:
                for alias in node.names:
                    self._record(alias.name, node.lineno)

            def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
                self._record(_resolve_from(source_package, node.module, node.level), node.lineno)

            def _scoped(self, node: ast.AST) -> None:
                self.scope_depth += 1
                self.generic_visit(node)
                self.scope_depth -= 1

            def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
                self._scoped(node)

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
                self._scoped(node)

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                self._scoped(node)

        Visitor().visit(tree)

    local_records = [
        record for record in records if record.target == package_prefix or record.target.startswith(f"{package_prefix}.")
    ]
    edges = {(record.source, record.target) for record in local_records if record.target in modules}
    components = _tarjan(modules, edges)
    largest = max(components, key=len, default=[])

    non_aggregator_modules = modules - aggregators
    no_aggregator_edges = {
        (source, target)
        for source, target in edges
        if source in non_aggregator_modules and target in non_aggregator_modules
    }
    no_aggregator_components = _tarjan(non_aggregator_modules, no_aggregator_edges)
    largest_no_aggregators = max(no_aggregator_components, key=len, default=[])

    aggregator_counts: dict[str, tuple[int, set[str]]] = {}
    for record in local_records:
        if not record.through_aggregator:
            continue
        count, files = aggregator_counts.get(record.target, (0, set()))
        files.add(record.path)
        aggregator_counts[record.target] = (count + 1, files)
    top_aggregators = tuple(
        (module, count, len(files))
        for module, (count, files) in sorted(
            aggregator_counts.items(), key=lambda item: item[1][0], reverse=True
        )[:top]
    )

    foundation_outward = tuple(
        record
        for record in local_records
        if any(
            record.source == f"{package_prefix}.{prefix}"
            or record.source.startswith(f"{package_prefix}.{prefix}.")
            for prefix in foundation_prefixes
        )
        and not any(
            record.target == f"{package_prefix}.{prefix}"
            or record.target.startswith(f"{package_prefix}.{prefix}.")
            for prefix in foundation_prefixes
        )
        and record.target != package_prefix
    )

    return ImportAnalysis(
        package_prefix=package_prefix,
        imports_total=len(records),
        local_imports=len(local_records),
        nested_imports=sum(record.nested for record in records),
        aggregator_imports=sum(record.through_aggregator for record in local_records),
        files_with_aggregator_imports=len({record.path for record in local_records if record.through_aggregator}),
        edges=len(edges),
        largest_scc_size=len(largest),
        largest_scc_without_aggregators=len(largest_no_aggregators),
        largest_scc=tuple(sorted(largest)),
        largest_scc_no_aggregators=tuple(sorted(largest_no_aggregators)),
        top_aggregators=top_aggregators,
        foundation_outward_imports=foundation_outward,
    )
