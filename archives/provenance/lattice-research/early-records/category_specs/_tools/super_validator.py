#!/usr/bin/env python3
"""Parse super_categories() declarations, build the DAG, report transitive violations."""

import ast
import pathlib
import sys
from collections import defaultdict


def extract_call_name(node: ast.expr) -> str | None:
    """Recover a string like '_Fields()' or 'Rings().Commutative()' from a Call AST node."""
    if isinstance(node, ast.Call):
        inner = _expr_name(node.func)
        if inner:
            return f"{inner}()"
    return None


def _expr_name(node: ast.expr) -> str | None:
    """Recover a readable name from an expression AST node."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _expr_name(node.value)
        if base:
            return f"{base}.{node.attr}"
    if isinstance(node, ast.Call):
        inner = _expr_name(node.func)
        if inner:
            return f"{inner}()"
    return None


def extract_class_name(node: ast.ClassDef) -> str:
    return node.name


def find_enclosing_class(parents: list[ast.AST], node_idx: int) -> ast.ClassDef | None:
    """Walk up the parent chain to find the enclosing class."""
    for p in reversed(parents[:node_idx]):
        if isinstance(p, ast.ClassDef):
            return p
    return None


class ClassExtractor(ast.NodeVisitor):
    """Extract super_categories() return lists and _base_category_class_and_axiom assignments."""

    def __init__(self):
        self.entries: dict[
            str, dict
        ] = {}  # full_name -> {parents: [...], axiom_base: str|None, dynamic: bool, zero: bool}
        self._current_class: ast.ClassDef | None = None
        self._class_stack: list[ast.ClassDef] = []

    def visit_ClassDef(self, node: ast.ClassDef):
        self._class_stack.append(node)
        self.generic_visit(node)
        self._class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if node.name == "super_categories" and self._class_stack:
            cls = self._class_stack[-1]
            parents, dynamic = self._extract_return_list(node)
            key = cls.name
            existing = self.entries.get(key, {})
            existing["parents"] = parents
            existing["dynamic"] = dynamic
            existing.setdefault("axiom_base", None)
            self.entries[key] = existing

    def visit_Assign(self, node: ast.Assign):
        if self._class_stack:
            cls = self._class_stack[-1]
            for target in node.targets:
                target_name = _expr_name(target)
                if target_name and (
                    target_name == "_base_category_class_and_axiom"
                    or target_name.endswith("._base_category_class_and_axiom")
                ):
                    # Extract the tuple value: (_SomeClass, "SomeAxiom") or (SomeClass, "SomeAxiom")
                    if isinstance(node.value, ast.Tuple):
                        elts = node.value.elts
                        if len(elts) >= 1:
                            base_name = _expr_name(elts[0])
                            key = cls.name
                            existing = self.entries.get(key, {})
                            existing["axiom_base"] = base_name
                            existing.setdefault("parents", [])
                            existing.setdefault("dynamic", False)
                            self.entries[key] = existing

    def _extract_return_list(self, func: ast.FunctionDef) -> tuple[list[str], bool]:
        """Extract parent names from a return statement containing a list literal."""
        for stmt in func.body:
            if isinstance(stmt, ast.Return):
                return self._extract_list_value(stmt.value)
        return [], False

    def _extract_list_value(self, node: ast.expr) -> tuple[list[str], bool]:
        if isinstance(node, ast.List):
            parents = []
            for elt in node.elts:
                name = extract_call_name(elt)
                if name:
                    parents.append(name)
                elif isinstance(elt, ast.Attribute):
                    name = _expr_name(elt)
                    if name:
                        parents.append(name)
                elif isinstance(elt, ast.Call):
                    # nested call, try full expression
                    name = _expr_name(elt)
                    if name:
                        parents.append(name)
            return parents, False
        # Dynamic return (e.g. cast(list, super().super_categories()))
        return [], True


def resolve_name(name: str, entries: dict[str, dict]) -> str | None:
    """Resolve a name like '_Fields()' to the canonical entry key.
    Handles LazyImport aliases: _Fields -> _Fields (the LazyImport is called as _Fields())"""
    # Strip trailing () if present
    bare = name.rstrip("()")
    # Try exact match first
    if bare in entries:
        return bare
    return None


def build_graph(entries: dict[str, dict]) -> dict[str, set[str]]:
    """Build adjacency dict: category_name -> set of parent names.
    Includes implicit axiom_base edges."""
    adj: dict[str, set[str]] = defaultdict(set)
    for cls_name, data in entries.items():
        # Explicit parents
        for p in data.get("parents", []):
            resolved = resolve_name(p, entries)
            if resolved:
                adj[cls_name].add(resolved)
        # Implicit axiom base
        base = data.get("axiom_base")
        if base:
            resolved = resolve_name(base, entries)
            if resolved:
                adj[cls_name].add(resolved)
    return dict(adj)


def transitive_closure(adj: dict[str, set[str]]) -> dict[str, set[str]]:
    """Compute transitive closure of each node (reachable supercategories) using Floyd-Warshall style."""
    nodes = list(adj.keys())
    # reachable[k][v] = True if there is a path from k to v
    reachable: dict[str, set[str]] = {n: set(adj.get(n, set())) for n in nodes}

    changed = True
    while changed:
        changed = False
        for n in nodes:
            new_reached = set(reachable[n])
            for u in list(reachable[n]):
                new_reached |= reachable.get(u, set())
            if new_reached != reachable[n]:
                reachable[n] = new_reached
                changed = True

    return reachable


def find_transitive_violations(
    entries: dict[str, dict], adj: dict[str, set[str]], closure: dict[str, set[str]]
) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Return (explicit_violations, axiom_violations).
    Explicit: a declared explicit parent is reachable through another explicit parent.
    Axiom: the axiom_base is reachable through an explicit parent (chain disagrees)."""
    explicit = []
    axiom = []
    for cls_name, data in entries.items():
        if data.get("dynamic"):
            continue
        explicit_parents = set()
        for p in data.get("parents", []):
            resolved = resolve_name(p, entries)
            if resolved:
                explicit_parents.add(resolved)

        base = data.get("axiom_base")
        base_resolved = resolve_name(base, entries) if base else None

        # Check explicit parents against each other
        explicit_list = list(explicit_parents)
        for i, p in enumerate(explicit_list):
            for j, q in enumerate(explicit_list):
                if i == j:
                    continue
                if p in closure.get(q, set()):
                    explicit.append((cls_name, p, q))

        # Check axiom_base against explicit parents
        if base_resolved and explicit_parents:
            for q in explicit_parents:
                if base_resolved in closure.get(q, set()):
                    axiom.append((cls_name, base_resolved, q))

    return explicit, axiom


def report(
    entries: dict[str, dict],
    explicit_violations: list[tuple[str, str, str]],
    axiom_violations: list[tuple[str, str, str]],
):
    """Print report."""
    print("=== SUMMARY ===")
    total = len(entries)
    dynamic = sum(1 for v in entries.values() if v.get("dynamic"))
    zero = sum(
        1
        for v in entries.values()
        if not v.get("dynamic") and not v.get("parents") and not v.get("axiom_base")
    )
    print(f"Total categories: {total}")
    print(f"Dynamic (skip): {dynamic}")
    print(f"Zero-parent: {zero}")
    print(f"Explicit transitive violations: {len(explicit_violations)}")
    print(f"Axiom-base transitives (rewire needed): {len(axiom_violations)}")
    print()

    if explicit_violations:
        print("=== EXPLICIT TRANSITIVE VIOLATIONS (must fix) ===")
        for cls, trans, via in sorted(explicit_violations):
            print(f"  {cls}: {trans} is reachable through {via}")

    if axiom_violations:
        print()
        print("=== AXIOM-BASE TRANSITIVES (rewire _base_category_class_and_axiom?) ===")
        for cls, base, via in sorted(axiom_violations):
            print(f"  {cls}: axiom base {base} is reachable through explicit {via}")

    # Also report 1-parent categories (for verification)
    single = [
        k
        for k, v in entries.items()
        if not v.get("dynamic")
        and (len(v.get("parents", [])) + (1 if v.get("axiom_base") else 0)) == 1
    ]
    print()
    print(f"=== SINGLE-PARENT ({len(single)}) === (verification needed)")
    for k in sorted(single):
        print(f"  {k}")

    # Zero parent
    zeros = [
        k
        for k, v in entries.items()
        if not v.get("dynamic") and not v.get("parents") and not v.get("axiom_base")
    ]
    if zeros:
        print()
        print("=== ZERO-PARENT (needs fix) ===")
        for k in sorted(zeros):
            print(f"  {k}")

    # Dynamic
    dynamics = [k for k, v in entries.items() if v.get("dynamic")]
    if dynamics:
        print()
        print("=== DYNAMIC (manual review) ===")
        for k in sorted(dynamics):
            print(f"  {k}")


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    extractor = ClassExtractor()

    for pyfile in sorted(root.rglob("*.py")):
        if "__pycache__" in str(pyfile):
            continue
        try:
            tree = ast.parse(pyfile.read_text())
        except SyntaxError:
            continue

        # Use standard NodeVisitor — the class stack in ClassExtractor
        # tracks nesting correctly for both function defs and assign targets.
        extractor.visit(tree)

    entries = extractor.entries
    adj = build_graph(entries)
    closure = transitive_closure(adj)
    explicit, axiom = find_transitive_violations(entries, adj, closure)

    report(entries, explicit, axiom)

    if explicit:
        sys.exit(1)


if __name__ == "__main__":
    main()
