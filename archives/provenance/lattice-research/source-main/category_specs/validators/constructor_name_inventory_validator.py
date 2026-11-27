#!/usr/bin/env python3
"""Validate constructor collector names against Sage constructor provenance."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_ROOT = (
    REPO_ROOT
    / ".agents"
    / "plans"
    / "features"
    / "FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES"
    / "specs"
)
NON_CONSTRUCTOR_METHOD_NAMES = frozenset({"provenance", "category", "base_ring"})
CONSTRUCTOR_SOURCE_GLOB_ROOTS = (
    SPEC_ROOT,
    REPO_ROOT / ".agents" / "plans" / "visuals",
)
CONSTRUCTOR_SOURCE_BANNED_PATTERNS = (
    re.compile(r"\bdeferred constructors?\b", re.IGNORECASE),
    re.compile(r"\bdeferred constructor records?\b", re.IGNORECASE),
    re.compile(r"\bexisting deferred constructors?\b", re.IGNORECASE),
    re.compile(r"\bnot[- ]admitted as (?:a )?project constructors?\b", re.IGNORECASE),
    re.compile(r"\bblocked constructor surface\b", re.IGNORECASE),
    re.compile(r"\bconstructor gap frontier\b", re.IGNORECASE),
)


@dataclass(frozen=True)
class ConstructorMethod:
    owner: str
    name: str
    path: Path
    line_number: int

    @property
    def location(self) -> str:
        return f"{self.path}:{self.line_number}"


@dataclass(frozen=True)
class ConstructorNameFailure:
    method: ConstructorMethod
    reason: str


@dataclass(frozen=True)
class ConstructorSourceFailure:
    path: Path
    line_number: int
    line: str
    reason: str

    @property
    def location(self) -> str:
        return f"{self.path}:{self.line_number}"


@dataclass(frozen=True)
class ConstructorNameInventory:
    owner: str
    sage_names: frozenset[str]
    project_owned_names: frozenset[str]
    source_path: Path


class ConstructorCollectorVisitor(ast.NodeVisitor):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.class_stack: list[str] = []
        self.methods: list[ConstructorMethod] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.class_stack.append(node.name)
        if node.name in {"_Constructors", "Constructors"}:
            owner = self._owner_name()
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and self._is_public(child.name):
                    self.methods.append(
                        ConstructorMethod(owner, child.name, self.path, child.lineno)
                    )
        self.generic_visit(node)
        self.class_stack.pop()

    def _owner_name(self) -> str:
        module_parts = self.path.with_suffix("").parts
        if module_parts[-1] == "__init__":
            module_parts = module_parts[:-1]
        module = ".".join(module_parts)
        return ".".join((module, *self.class_stack))

    @staticmethod
    def _is_public(name: str) -> bool:
        return not name.startswith("_") and name not in NON_CONSTRUCTOR_METHOD_NAMES


def tracked_python_paths() -> list[Path]:
    return [
        path
        for path in sorted((REPO_ROOT / "category_specs").rglob("*.py"))
        if "__pycache__" not in path.parts
        and path.relative_to(REPO_ROOT).parts[1] != "validators"
    ]


def constructor_methods() -> list[ConstructorMethod]:
    methods: list[ConstructorMethod] = []
    for absolute_path in tracked_python_paths():
        relative_path = absolute_path.relative_to(REPO_ROOT)
        tree = ast.parse(absolute_path.read_text(), filename=str(relative_path))
        visitor = ConstructorCollectorVisitor(relative_path)
        visitor.visit(tree)
        methods.extend(visitor.methods)
    return methods


def spec_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    _, frontmatter, _ = text.split("---\n", 2)
    data = yaml.safe_load(frontmatter)
    assert isinstance(data, dict), f"{path} frontmatter must be a mapping"
    return data


def constructor_name_inventories() -> dict[str, ConstructorNameInventory]:
    inventories: dict[str, ConstructorNameInventory] = {}
    for path in sorted(SPEC_ROOT.glob("SPEC-MAPPING-*.md")):
        data = spec_frontmatter(path)
        raw_inventories = data.get("constructorNameInventories", [])
        assert isinstance(raw_inventories, list), (
            f"{path} constructorNameInventories must be a list"
        )
        for raw_inventory in raw_inventories:
            assert isinstance(raw_inventory, dict), (
                f"{path} constructorNameInventories entries must be mappings"
            )
            owner = raw_inventory.get("owner")
            sage_names = raw_inventory.get("sageConstructorNames", [])
            project_owned_names = raw_inventory.get("projectOwnedConstructionNames", [])
            assert isinstance(owner, str), f"{path} constructor inventory owner missing"
            assert isinstance(sage_names, list), (
                f"{path} sageConstructorNames for {owner} must be a list"
            )
            assert isinstance(project_owned_names, list), (
                f"{path} projectOwnedConstructionNames for {owner} must be a list"
            )
            assert owner not in inventories, (
                f"{owner} constructor-name inventory is declared more than once"
            )
            inventories[owner] = ConstructorNameInventory(
                owner=owner,
                sage_names=frozenset(str(name) for name in sage_names),
                project_owned_names=frozenset(str(name) for name in project_owned_names),
                source_path=path.relative_to(REPO_ROOT),
            )
    return inventories


def constructor_source_paths() -> list[Path]:
    paths: list[Path] = []
    for root in CONSTRUCTOR_SOURCE_GLOB_ROOTS:
        paths.extend(path for path in sorted(root.rglob("*.md")) if path.is_file())
    return paths


def constructor_source_failures() -> list[ConstructorSourceFailure]:
    failures: list[ConstructorSourceFailure] = []
    for absolute_path in constructor_source_paths():
        relative_path = absolute_path.relative_to(REPO_ROOT)
        for line_number, line in enumerate(
            absolute_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for pattern in CONSTRUCTOR_SOURCE_BANNED_PATTERNS:
                if not pattern.search(line):
                    continue
                failures.append(
                    ConstructorSourceFailure(
                        path=relative_path,
                        line_number=line_number,
                        line=line,
                        reason=(
                            "constructor source artifacts must not preserve "
                            "deferred/not-admitted constructor ideas; return to "
                            "Sage source and mapping reconstruction instead"
                        ),
                    )
                )
    return failures


def validate_method(method: ConstructorMethod) -> ConstructorNameFailure | None:
    inventories = constructor_name_inventories()
    if method.owner not in inventories:
        return ConstructorNameFailure(
            method,
            "constructor collector has no constructor-name inventory entry in "
            "tracked mapping specs",
        )

    inventory = inventories[method.owner]
    if method.name in inventory.sage_names or method.name in inventory.project_owned_names:
        return None

    return ConstructorNameFailure(
        method,
        "name is neither an inventoried Sage constructor name nor an explicit "
        "project-owned construction",
    )


def main() -> int:
    inventories = constructor_name_inventories()
    failures = [
        failure
        for method in constructor_methods()
        if (failure := validate_method(method)) is not None
    ]
    source_failures = constructor_source_failures()

    if not failures and not source_failures:
        print("Constructor name inventory validation passed.")
        return 0

    print("Constructor name inventory validation failed.")
    print(
        "Every category-exposed constructor name must either exactly match an "
        "inventoried Sage constructor name, or be explicitly classified as a "
        "project-owned construction in the tracked mapping specs."
    )
    print("Inventory sources:")
    for inventory in sorted(inventories.values(), key=lambda item: item.owner):
        print(f"- {inventory.owner}: {inventory.source_path}")
    for failure in failures:
        method = failure.method
        print(f"- {method.location} {method.owner}.{method.name}: {failure.reason}")
    if source_failures:
        print()
        print("Constructor source artifact validation failed.")
        print(
            "Constructor mapping docs are the admission boundary. If a constructor "
            "shape is not source-grounded and mapped, it must be absent rather than "
            "preserved as deferred, not-admitted, blocked, or gap evidence."
        )
        for failure in source_failures:
            print(f"- {failure.location}: {failure.reason}")
            print(f"  Code: {failure.line.strip()}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
