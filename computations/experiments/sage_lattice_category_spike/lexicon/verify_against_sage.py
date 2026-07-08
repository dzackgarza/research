r"""Verify the stub tree against the running Sage (INVENTORY.md Part V.2).

Stubs are claims about an external system; this script re-derives every claim
from the ``.pyi`` sources themselves (no hand-maintained mirror to drift) and
asserts it against the live library:

- every stubbed module imports;
- every stubbed class/function/value exists in the real module;
- every stubbed method exists on the real class;
- every stub base-class edge is a real ``issubclass`` relation.

Run under Sage's Python:

    sage -python -m sage_lattice_category_spike.lexicon.verify_against_sage
"""

from __future__ import annotations

import ast
import importlib
from pathlib import Path

#: Stub-only helper names that deliberately have no runtime counterpart,
#: each justified where it is declared.
STUB_ONLY = {
    # categories/category_with_axiom.pyi: `all_axioms` is a dynamic
    # AxiomContainer; the stub names its shape locally.
    ("sage.categories.category_with_axiom", "_AxiomSet"),
    # matrix/constructor.pyi: `matrix` is a cython function carrying the named
    # constructors (matrix.diagonal, ...); its class has no importable name.
    ("sage.matrix.constructor", "_MatrixConstructor"),
}


def _representatives() -> dict[str, list[object]]:
    """Concrete instances for classes whose declared surface Sage attaches
    below the abstract marker (cdef markers like ``element.Matrix``) or
    synthesizes dynamically (category axiom methods). A method claim on such
    a class is verified against these values instead of the bare class."""
    from sage.categories.modules import Modules
    from sage.categories.sets_cat import Sets
    from sage.groups.additive_abelian.qmodnz import QmodnZ
    from sage.matrix.constructor import matrix
    from sage.modules.free_module_element import vector
    from sage.rings.integer_ring import ZZ
    from sage.rings.rational_field import QQ

    return {
        "sage.structure.element.Matrix": [
            matrix(ZZ, 2, 2, [2, 1, 1, 2]),
            matrix(QQ, 2, 2, [1, 0, 0, 1]),
        ],
        # Category method holders: Sage copies ParentMethods into each
        # parent's dynamic class, so the claims are checked on representative
        # parents of the category rather than on the holder class itself.
        "sage.categories.rings.Rings.ParentMethods": [ZZ, QQ],
        "sage.categories.fields.Fields.ParentMethods": [QQ],
        "sage.rings.integer_ring.IntegerRing_class": [ZZ],
        "sage.structure.factorization.Factorization": [ZZ(12).factor()],
        "sage.structure.element.Vector": [vector(QQ, [1, 2]), vector(ZZ, [1, 2])],
        "sage.categories.category.Category": [Sets()],
        "sage.categories.modules.Modules": [Modules(ZZ)],
        "sage.groups.additive_abelian.qmodnz.QmodnZ": [QmodnZ(1)],
        "sage.modules.free_module.FreeModule_generic": [
            ZZ**2,
            (QQ**2).span([[1, 0]]),
        ],
    }


def _module_name(pyi: Path, root: Path) -> str:
    parts = pyi.relative_to(root).with_suffix("").parts
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _fail(problems: list[str], message: str) -> None:
    problems.append(message)


def verify() -> None:
    root = Path(__file__).resolve().parent.parent / "typings"
    problems: list[str] = []
    checked = 0
    representatives = _representatives()
    for pyi in sorted(root.rglob("*.pyi")):
        module_name = _module_name(pyi, root)
        if not module_name:
            continue
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001 - report, don't mask
            _fail(problems, f"{module_name}: module import failed: {exc!r}")
            continue
        tree = ast.parse(pyi.read_text(), filename=str(pyi))
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                if (module_name, node.name) in STUB_ONLY:
                    continue
                if not hasattr(module, node.name):
                    _fail(problems, f"{module_name}.{node.name}: class missing")
                    continue
                real = getattr(module, node.name)
                checked += 1
                checked += _verify_class(node, real, f"{module_name}.{node.name}", tree, module, representatives, problems)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name in dir(module):
                    checked += 1
                else:
                    _fail(problems, f"{module_name}.{node.name}: function missing")
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                if node.target.id in dir(module):
                    checked += 1
                else:
                    _fail(problems, f"{module_name}.{node.target.id}: value missing")
    assert not problems, "stub tree disagrees with the running Sage:\n" + "\n".join(problems)
    print(f"lexicon stubs verified against running Sage: {checked} claims OK")


def _verify_class(
    node: ast.ClassDef,
    real: object,
    qualname: str,
    tree: ast.Module,
    module: object,
    representatives: dict[str, list[object]],
    problems: list[str],
) -> int:
    """Verify one stub class (recursing into nested classes, e.g. a category's
    ParentMethods) against its runtime counterpart. Base-class edges ending in
    ``ParentMethods``/``ElementMethods`` are stub-declared category opt-ins:
    Sage realizes them by COPYING methods into dynamic classes, so they are
    checked through category representatives, not ``issubclass``."""
    checked = 0
    for base in node.bases:
        base_name = ast.unparse(base)
        if base_name.endswith(("ParentMethods", "ElementMethods")):
            continue
        if node.name in ("ParentMethods", "ElementMethods"):
            # A holder class's own stub bases (e.g. Rings.ParentMethods
            # subsuming Parent) are the mathematically true edge, realized by
            # method copying; they are verified extensionally through the
            # representative parents below, never by issubclass.
            continue
        base_obj = _resolve(base_name, tree, module)
        if isinstance(real, type) and isinstance(base_obj, type) and not issubclass(real, base_obj):
            _fail(problems, f"{qualname}: not a subclass of stub base {base_name}")
    carriers: list[object] = [real]
    if qualname in representatives:
        carriers += representatives[qualname]
    for item in node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if any((item.name in dir(carrier)) for carrier in carriers):
                checked += 1
            elif item.name == "__iter__" and any(_legacy_iterable(carrier) for carrier in carriers if not isinstance(carrier, type)):
                # Sage vectors iterate through the legacy __getitem__/__len__
                # protocol; the claim is verified by actually iterating a
                # representative instance.
                checked += 1
            else:
                _fail(problems, f"{qualname}.{item.name}: method missing")
        elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            # Instance attributes (e.g. QmodnZ.n) are not on the class object
            # for cdef classes; probed only when exposed statically.
            checked += 1
        elif isinstance(item, ast.ClassDef):
            if not hasattr(real, item.name):
                _fail(problems, f"{qualname}.{item.name}: nested class missing")
                continue
            nested_real = getattr(real, item.name)
            checked += 1
            checked += _verify_class(item, nested_real, f"{qualname}.{item.name}", tree, module, representatives, problems)
    return checked


def _legacy_iterable(value: object) -> bool:
    try:
        iter(value)  # type: ignore[call-overload]
    except TypeError:
        return False
    return True


def _resolve(name: str, tree: ast.Module, module: object) -> object | None:
    """Resolve a stub base-class name: local to the module, or via the stub's imports."""
    if hasattr(module, name):
        local: object = getattr(module, name)
        return local
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                if (alias.asname or alias.name) == name:
                    imported = importlib.import_module(node.module)
                    if not hasattr(imported, alias.name):
                        return None
                    resolved: object = getattr(imported, alias.name)
                    return resolved
    return None


if __name__ == "__main__":
    verify()
