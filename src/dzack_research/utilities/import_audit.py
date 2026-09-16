"""Intra-package imports of the preamble, checked against source alone.

Every ``from dzack_research... import name`` must name something its target
module binds.  Read with :mod:`ast`, so it answers on a tree that does not
import, which is when a dangling import is invisible to everything else.

A module that re-exports by star import is skipped, since its bound names are
not decidable from its own source.  A package whose ``__init__`` resolves
names lazily through an ``_EXPORTS`` table binds the keys of that table.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


def bound_names(path: Path) -> set[str] | None:
    """The names ``path`` binds at module level, or None if it star-imports."""
    module = ast.parse(path.read_text(encoding="utf-8"))
    if any(
        isinstance(s, ast.ImportFrom) and any(a.name == "*" for a in s.names)
        for s in module.body
    ):
        return None
    names: set[str] = set()

    def visit(body: list[ast.stmt]) -> None:
        for statement in body:
            if isinstance(statement, (ast.ClassDef, ast.FunctionDef)):
                names.add(statement.name)
            elif isinstance(statement, ast.Assign):
                targets = [t.id for t in statement.targets if isinstance(t, ast.Name)]
                names.update(targets)
                if "_EXPORTS" in targets and isinstance(statement.value, ast.Dict):
                    names.update(
                        key.value
                        for key in statement.value.keys
                        if isinstance(key, ast.Constant) and isinstance(key.value, str)
                    )
            elif isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
                names.add(statement.target.id)
            elif isinstance(statement, (ast.ImportFrom, ast.Import)):
                names.update(a.asname or a.name.split(".")[0] for a in statement.names)
            elif isinstance(statement, (ast.If, ast.Try)):
                visit(statement.body)
                visit(statement.orelse)

    visit(module.body)
    return names


def unresolved_imports(root: Path, package: str) -> list[tuple[Path, int, str, str]]:
    """Every ``(file, line, module, name)`` whose import names nothing bound."""
    cache: dict[Path, set[str] | None] = {}
    missing: list[tuple[Path, int, str, str]] = []
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ImportFrom) or not node.module:
                continue
            if not node.module.startswith(package):
                continue
            as_path = node.module.replace(".", "/")
            target = root / (as_path[len(package) :].lstrip("/") + ".py")
            directory = root / as_path[len(package) :].lstrip("/")
            if not target.exists():
                target = directory / "__init__.py"
            if not target.exists():
                missing.append((path, node.lineno, node.module, "<module missing>"))
                continue
            if target not in cache:
                cache[target] = bound_names(target)
            bound = cache[target]
            if bound is None:
                continue
            for alias in node.names:
                if alias.name == "*" or alias.name in bound:
                    continue
                if (directory / (alias.name + ".py")).exists() or (directory / alias.name).is_dir():
                    continue
                missing.append((path, node.lineno, node.module, alias.name))
    return missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List intra-package imports that name nothing their module binds."
    )
    parser.add_argument("root", nargs="?", type=Path, default=Path("src/dzack_research"))
    parser.add_argument("--package", default="dzack_research")
    arguments = parser.parse_args()
    missing = unresolved_imports(arguments.root, arguments.package)
    for path, line, module, name in missing:
        print(f"{path}:{line}: {name} not bound in {module}")
    print(f"{len(missing)} unresolved imports")
    raise SystemExit(1 if missing else 0)


if __name__ == "__main__":
    main()
