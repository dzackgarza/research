#!/usr/bin/env python3
"""Build a source-level inventory of SageMath 10.9 categories.

The inventory is intentionally static and reproducible.  It enumerates named
category classes and category-valued wrapper constructors in src/sage/categories,
including the category class in sage.categories.examples, then records
source-declared axiom and functorial-construction entry points, implementations,
and bindings.
"""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import zipfile
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

SOURCE_ROOT = Path("/mnt/data/sage109/src/sage/categories")
DIST_ROOT = Path("/mnt/data/sage109")
OUT = Path("/mnt/data")
VERSION = (DIST_ROOT / "VERSION.txt").read_text(encoding="utf-8").strip()
COMMIT = "686dc1a8d420c2e0aabadd4f602d9a0aa4690c50"
SDIST = Path("/mnt/data/sagemath-10.9.tar.gz")
SDIST_SHA256 = hashlib.sha256(SDIST.read_bytes()).hexdigest()
GITHUB_BASE = f"https://github.com/sagemath/sage/blob/{COMMIT}/src/sage/categories"

MIXIN_CONTAINERS = {
    "ParentMethods",
    "ElementMethods",
    "MorphismMethods",
    "SubcategoryMethods",
    "AdditionalStructure",
}

# These are implementation/framework category classes rather than the named
# mathematical category constructors normally presented in the reference manual.
TECHNICAL_CATEGORY_IDS = {
    "category.Category",
    "category.CategoryWithParameters",
    "category.JoinCategory",
    "category_types.Elements",
    "category_types.Category_over_base",
    "category_types.AbelianCategory",
    "category_types.Category_over_base_ring",
    "category_types.Category_in_ambient",
    "category_types.Category_module",
    "category_types.Category_ideal",
    "category_with_axiom.CategoryWithAxiom",
    "category_with_axiom.CategoryWithAxiom_over_base_ring",
    "category_with_axiom.CategoryWithAxiom_singleton",
    "covariant_functorial_construction.FunctorialConstructionCategory",
    "covariant_functorial_construction.CovariantConstructionCategory",
    "covariant_functorial_construction.RegressiveCovariantConstructionCategory",
    "algebra_functor.AlgebrasCategory",
    "cartesian_product.CartesianProductsCategory",
    "dual.DualObjectsCategory",
    "filtered_modules.FilteredModulesCategory",
    "graded_modules.GradedModulesCategory",
    "graded_lie_conformal_algebras.GradedLieConformalAlgebrasCategory",
    "homsets.HomsetsCategory",
    "homsets.HomsetsOf",
    "isomorphic_objects.IsomorphicObjectsCategory",
    "metric_spaces.MetricSpacesCategory",
    "quotients.QuotientsCategory",
    "realizations.RealizationsCategory",
    "realizations.Category_realization_of_parent",
    "signed_tensor.SignedTensorProductsCategory",
    "subobjects.SubobjectsCategory",
    "subquotients.SubquotientsCategory",
    "super_modules.SuperModulesCategory",
    "tensor.TensorProductsCategory",
    "topological_spaces.TopologicalSpacesCategory",
    "with_realizations.WithRealizationsCategory",
    "schemes.Schemes_over_base",
}

TEST_CATEGORY_IDS = {
    "category_with_axiom.Blahs",
    "category_with_axiom.Bars",
    "category_with_axiom.TestObjects",
    "category_with_axiom.DummyObjectsOverBaseRing",
}

# Cython-defined category framework class.
CYTHON_TECHNICAL_CATEGORY = {
    "category_id": "category_singleton.Category_singleton",
    "constructor": "Category_singleton",
    "module": "category_singleton",
    "source_line": 83,
    "source": "src/sage/categories/category_singleton.pyx:83",
    "source_url": f"{GITHUB_BASE}/category_singleton.pyx#L83",
    "bases": "Category",
    "role": "framework/helper category class",
    "implementation_kind": "Cython class",
    "defining_relation": "",
    "direct_defining_axiom": "",
    "syntactic_defining_axiom_chain": "",
    "defining_functorial_construction": "",
    "bound_as": "",
    "local_axiom_paths": "",
    "local_functorial_construction_paths": "",
    "other_local_category_paths": "",
    "notes": "Technical singleton-category base class defined in category_singleton.pyx.",
}

# The sole category class in sage.categories.examples.  It is deliberately
# separated from the production API and from test fixtures.
CYTHON_EXAMPLE_CATEGORY = {
    "category_id": "examples.semigroups_cython.IdempotentSemigroups",
    "constructor": "IdempotentSemigroups",
    "module": "examples/semigroups_cython",
    "source_line": 13,
    "source": "src/sage/categories/examples/semigroups_cython.pyx:13",
    "source_url": f"{GITHUB_BASE}/examples/semigroups_cython.pyx#L13",
    "bases": "Category",
    "role": "example-only category class",
    "implementation_kind": "Cython class",
    "defining_relation": "supercategory Semigroups()",
    "direct_defining_axiom": "",
    "syntactic_defining_axiom_chain": "",
    "defining_functorial_construction": "",
    "bound_as": "",
    "local_axiom_paths": "",
    "local_functorial_construction_paths": "",
    "other_local_category_paths": "",
    "notes": "Demonstration category used by the Cython semigroup example.",
}

PUBLIC_WRAPPER_NAMES = {
    "FiniteDimensionalBialgebrasWithBasis",
    "FiniteDimensionalCoalgebrasWithBasis",
    "GradedBialgebras",
    "GradedBialgebrasWithBasis",
    "GradedHopfAlgebras",
    "MonoidAlgebras",
}

ALIASES: list[dict[str, Any]] = [
    {
        "alias": "PartiallyOrderedSets",
        "canonical": "Posets",
        "module": "basic",
        "source_line": 17,
        "status": "backward compatibility",
    },
    {
        "alias": "OrderedSets",
        "canonical": "Posets",
        "module": "basic",
        "source_line": 18,
        "status": "backward compatibility",
    },
    {
        "alias": "OrderedMonoids",
        "canonical": "PartiallyOrderedMonoids",
        "module": "basic",
        "source_line": 34,
        "status": "backward compatibility",
    },
    {
        "alias": "RingModules",
        "canonical": "Modules",
        "module": "all",
        "source_line": 107,
        "status": "alias",
    },
    {
        "alias": "Ideals",
        "canonical": "RingIdeals",
        "module": "all",
        "source_line": 125,
        "status": "alias",
    },
    {
        "alias": "FreeModules",
        "canonical": "ModulesWithBasis",
        "module": "all",
        "source_line": 137,
        "status": "alias",
    },
]

# Explicit special case used by Sage's own name-based axiom heuristic.
SPECIAL_DEFINITIONS = {
    "facade_sets.FacadeSets": ("Sets", "Facade"),
}


def unparse(node: ast.AST | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def simple_base_name(expr: str) -> str:
    """Get the leading class name from a base expression."""
    head = re.split(r"[\[.(]", expr, maxsplit=1)[0]
    return head.split(".")[-1]


def parse_lazy_import(call: ast.AST) -> tuple[str, str] | None:
    if not isinstance(call, ast.Call):
        return None
    if unparse(call.func).split(".")[-1] not in {"LazyImport", "lazy_import"}:
        return None
    if len(call.args) < 2:
        return None
    if not isinstance(call.args[0], ast.Constant) or not isinstance(call.args[1], ast.Constant):
        return None
    module = call.args[0].value
    target = call.args[1].value
    if not isinstance(module, str) or not isinstance(target, str):
        return None
    return module, target


def source_url(module: str, line: int, suffix: str = "py") -> str:
    return f"{GITHUB_BASE}/{module}.{suffix}#L{line}"


@dataclass
class ClassRecord:
    module: str
    path: str
    name: str
    line: int
    bases: list[str]
    node: ast.ClassDef
    parent_path: str | None

    @property
    def top_name(self) -> str:
        return self.path.split(".")[0]

    @property
    def category_id(self) -> str:
        return f"{self.module}.{self.top_name}"


@dataclass
class FeatureDeclaration:
    category_id: str
    owner_path: str
    relative_path: str
    feature_name: str
    feature_type: str
    declaration_kind: str
    target_or_expansion: str
    module: str
    source_line: int
    notes: str = ""

    @property
    def source(self) -> str:
        return f"src/sage/categories/{self.module}.py:{self.source_line}"

    @property
    def source_url(self) -> str:
        return source_url(self.module, self.source_line)


# ---------------------------------------------------------------------------
# Parse Python sources and class trees
# ---------------------------------------------------------------------------

trees: dict[str, ast.Module] = {}
top_classes: dict[str, ClassRecord] = {}
all_class_records: list[ClassRecord] = []


def scan_class(module: str, node: ast.ClassDef, path: list[str], parent_path: str | None) -> ClassRecord:
    rec = ClassRecord(
        module=module,
        path=".".join(path),
        name=node.name,
        line=node.lineno,
        bases=[unparse(b) for b in node.bases],
        node=node,
        parent_path=parent_path,
    )
    all_class_records.append(rec)
    for child in node.body:
        if isinstance(child, ast.ClassDef):
            scan_class(module, child, path + [child.name], rec.path)
    return rec


for pyfile in sorted(SOURCE_ROOT.glob("*.py")):
    module = pyfile.stem
    tree = ast.parse(pyfile.read_text(encoding="utf-8"), filename=str(pyfile))
    trees[module] = tree
    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef):
            rec = scan_class(module, stmt, [stmt.name], None)
            top_classes[f"{module}.{stmt.name}"] = rec

# Detect top-level category classes by transitive inheritance, including the
# Cython Category_singleton base as a seed.
category_class_names = {"Category", "Category_singleton"}
changed = True
while changed:
    changed = False
    for rec in top_classes.values():
        if rec.name in category_class_names:
            continue
        if any(simple_base_name(base) in category_class_names for base in rec.bases):
            category_class_names.add(rec.name)
            changed = True

category_class_ids = {
    cid for cid, rec in top_classes.items() if rec.name in category_class_names
}


def top_class_is_descendant(category_id: str, targets: set[str], seen: set[str] | None = None) -> bool:
    if seen is None:
        seen = set()
    if category_id in seen:
        return False
    seen.add(category_id)
    rec = top_classes[category_id]
    for base in rec.bases:
        name = simple_base_name(base)
        if name in targets:
            return True
        for other_id, other in top_classes.items():
            if other.name == name and other_id in category_class_ids:
                if top_class_is_descendant(other_id, targets, seen):
                    return True
    return False


# ---------------------------------------------------------------------------
# Axiom registry
# ---------------------------------------------------------------------------

axiom_registry: list[dict[str, Any]] = []
for module in ("category_with_axiom", "semigroups"):
    tree = trees[module]
    for stmt in tree.body:
        if (
            isinstance(stmt, ast.AugAssign)
            and isinstance(stmt.target, ast.Name)
            and stmt.target.id == "all_axioms"
            and isinstance(stmt.op, ast.Add)
            and isinstance(stmt.value, (ast.Tuple, ast.List))
        ):
            for elt in stmt.value.elts:
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                    axiom_registry.append(
                        {
                            "axiom": elt.value,
                            "registry_module": module,
                            "registry_line": stmt.lineno,
                            "status": "test-only placeholder" if elt.value in {"Flying", "Blue"} else "production",
                        }
                    )

AXIOMS = [r["axiom"] for r in axiom_registry]
AXIOM_SET = set(AXIOMS)

# ---------------------------------------------------------------------------
# Functorial construction registry from _functor_category
# ---------------------------------------------------------------------------

functor_helpers: dict[str, list[dict[str, Any]]] = defaultdict(list)
for cid, rec in top_classes.items():
    for stmt in rec.node.body:
        if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
            targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
            for target in targets:
                if isinstance(target, ast.Name) and target.id == "_functor_category":
                    value = stmt.value
                    if isinstance(value, ast.Constant) and isinstance(value.value, str):
                        functor_helpers[value.value].append(
                            {
                                "class_id": cid,
                                "class_name": rec.name,
                                "module": rec.module,
                                "line": stmt.lineno,
                                "bases": rec.bases,
                                "is_category_class": cid in category_class_ids,
                            }
                        )

FUNCTORS = sorted(functor_helpers)
FUNCTOR_SET = set(FUNCTORS)
HELPER_TO_FUNCTOR: dict[str, str] = {}
for functor, helpers in functor_helpers.items():
    for helper in helpers:
        if helper["is_category_class"]:
            HELPER_TO_FUNCTOR[helper["class_name"]] = functor

# ---------------------------------------------------------------------------
# Lazy-import bindings and hardcoded category-with-axiom definitions
# ---------------------------------------------------------------------------

incoming_bindings: dict[str, list[dict[str, Any]]] = defaultdict(list)
hardcoded_definitions: dict[str, tuple[str, str, int]] = {}

for rec in all_class_records:
    for stmt in rec.node.body:
        if not isinstance(stmt, (ast.Assign, ast.AnnAssign)):
            continue
        targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
        for target in targets:
            if not isinstance(target, ast.Name):
                continue
            if target.id == "_base_category_class_and_axiom":
                value = stmt.value
                if isinstance(value, (ast.Tuple, ast.List)) and len(value.elts) == 2:
                    axiom_node = value.elts[1]
                    axiom = axiom_node.value if isinstance(axiom_node, ast.Constant) else unparse(axiom_node)
                    hardcoded_definitions[rec.category_id] = (unparse(value.elts[0]), str(axiom), stmt.lineno)
            value = stmt.value
            if value is None:
                continue
            lazy = parse_lazy_import(value)
            if lazy:
                target_module, target_name = lazy
                if target_module.startswith("sage.categories."):
                    target_id = f"{target_module.rsplit('.', 1)[-1]}.{target_name}"
                    incoming_bindings[target_id].append(
                        {
                            "source_category_id": rec.category_id,
                            "source_path": rec.path,
                            "attribute": target.id,
                            "module": rec.module,
                            "line": stmt.lineno,
                        }
                    )

# ---------------------------------------------------------------------------
# Feature declarations attached to each category class tree
# ---------------------------------------------------------------------------

features: list[FeatureDeclaration] = []


def relative_feature_path(top_name: str, owner_path: str, feature_name: str) -> str:
    parts = owner_path.split(".")
    rel_parts = parts[1:] if parts and parts[0] == top_name else parts
    return ".".join(rel_parts + [feature_name])


def extract_with_axiom_calls(node: ast.AST) -> list[str]:
    result: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) and sub.func.attr == "_with_axiom":
            if sub.args and isinstance(sub.args[0], ast.Constant) and isinstance(sub.args[0].value, str):
                result.append(sub.args[0].value)
    return result


def extract_category_of_calls(node: ast.AST) -> list[str]:
    result: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) and sub.func.attr == "category_of":
            result.append(unparse(sub.func.value))
    return result


def extract_with_axioms_calls(node: ast.AST) -> list[str]:
    """Return expressions on which ``_with_axioms`` is invoked."""
    result: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) and sub.func.attr == "_with_axioms":
            result.append(unparse(sub.func.value))
    return result


def extract_recognized_category_calls(node: ast.AST) -> list[str]:
    """Return calls to registered axiom/functor methods or public shorthands."""
    recognized = AXIOM_SET | FUNCTOR_SET | {"Endsets"} | category_class_names | PUBLIC_WRAPPER_NAMES
    result: list[str] = []
    for sub in ast.walk(node):
        if not isinstance(sub, ast.Call):
            continue
        if isinstance(sub.func, ast.Attribute):
            name = sub.func.attr
        elif isinstance(sub.func, ast.Name):
            name = sub.func.id
        else:
            continue
        if name in recognized:
            result.append(name)
    return result


def classify_nested_class(child: ast.ClassDef) -> tuple[str, str] | None:
    if child.name in AXIOM_SET:
        return "axiom", child.name
    if child.name in FUNCTOR_SET:
        return "functorial construction", child.name
    bases = [unparse(b) for b in child.bases]
    if any("CategoryWithAxiom" in base for base in bases):
        return "axiom", child.name
    for base in bases:
        helper = simple_base_name(base)
        if helper in HELPER_TO_FUNCTOR:
            return "functorial construction", HELPER_TO_FUNCTOR[helper]
    if any("Category" in base or simple_base_name(base) in category_class_names for base in bases):
        return "other category", child.name
    return None


def scan_category_method(
    category_id: str,
    top_name: str,
    owner_path: str,
    stmt: ast.FunctionDef | ast.AsyncFunctionDef,
    module: str,
    declaration_kind: str,
) -> None:
    """Record a source-visible category-valued method declaration.

    Registered axiom and functor names are authoritative.  Other uppercase
    methods are retained only when their bodies visibly construct/refine a
    category; this catches public shorthands such as ``FinitelyGenerated``,
    ``Complex``, and ``Endsets`` without misclassifying methods such as
    ``R_matrix`` or ``A_field``.
    """
    name = stmt.name
    if not name[:1].isupper() or name.endswith("_extra_super_categories"):
        return

    axiom_calls = extract_with_axiom_calls(stmt)
    category_of_calls = extract_category_of_calls(stmt)
    with_axioms_calls = extract_with_axioms_calls(stmt)
    recognized_calls = [call for call in extract_recognized_category_calls(stmt) if call != name]

    if name in AXIOM_SET:
        feature_type = "axiom"
    elif name in FUNCTOR_SET:
        feature_type = "functorial construction"
    elif axiom_calls or category_of_calls or with_axioms_calls or recognized_calls:
        feature_type = "derived category shorthand"
    else:
        return

    expansion_parts: list[str] = []
    if axiom_calls:
        expansion_parts.append(" then ".join(f"_with_axiom({a})" for a in axiom_calls))
    if category_of_calls:
        expansion_parts.append(", ".join(f"{c}.category_of(...)" for c in category_of_calls))
    if with_axioms_calls:
        expansion_parts.append(", ".join(f"{c}._with_axioms(...)" for c in with_axioms_calls))
    if recognized_calls:
        seen_calls: set[str] = set()
        stable_calls: list[str] = []
        for c in recognized_calls:
            if c not in seen_calls:
                seen_calls.add(c)
                stable_calls.append(c)
        expansion_parts.append("calls " + ", ".join(f"{c}()" for c in stable_calls))
    expansion = "; ".join(expansion_parts)

    notes = ""
    if name in AXIOM_SET and axiom_calls and axiom_calls != [name]:
        notes = "Named shorthand expands to different primitive axiom steps."

    features.append(
        FeatureDeclaration(
            category_id=category_id,
            owner_path=owner_path,
            relative_path=relative_feature_path(top_name, owner_path, name),
            feature_name=name,
            feature_type=feature_type,
            declaration_kind=declaration_kind,
            target_or_expansion=expansion,
            module=module,
            source_line=stmt.lineno,
            notes=notes,
        )
    )


def scan_subcategory_methods(
    category_id: str,
    top_name: str,
    owner_path: str,
    container: ast.ClassDef,
    module: str,
) -> None:
    for stmt in container.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
            scan_category_method(
                category_id,
                top_name,
                owner_path,
                stmt,
                module,
                "subcategory interface method",
            )
            continue

        if not isinstance(stmt, (ast.Assign, ast.AnnAssign)):
            continue
        targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
        for target in targets:
            if not isinstance(target, ast.Name) or target.id.startswith("_"):
                continue

            # The test framework uses ``A = axiom("A")`` as a compact
            # way to create an axiom-defining SubcategoryMethods method.
            value = stmt.value
            if (
                isinstance(value, ast.Call)
                and unparse(value.func).split(".")[-1] == "axiom"
                and value.args
                and isinstance(value.args[0], ast.Constant)
                and isinstance(value.args[0].value, str)
            ):
                axiom_name = value.args[0].value
                features.append(
                    FeatureDeclaration(
                        category_id=category_id,
                        owner_path=owner_path,
                        relative_path=relative_feature_path(top_name, owner_path, target.id),
                        feature_name=axiom_name,
                        feature_type="axiom",
                        declaration_kind="subcategory interface method",
                        target_or_expansion=f"_with_axiom({axiom_name})",
                        module=module,
                        source_line=stmt.lineno,
                        notes=(
                            "The public method name differs from the registered axiom name."
                            if target.id != axiom_name
                            else ""
                        ),
                    )
                )
                continue

            # Record source aliases such as ``Modules.SubcategoryMethods.dual
            # = DualObjects`` while normalizing the feature to the registered
            # axiom/functor name.
            if isinstance(value, (ast.Name, ast.Attribute)):
                rhs = unparse(value).split(".")[-1]
                if target.id in AXIOM_SET or rhs in AXIOM_SET:
                    feature_type = "axiom"
                    normalized_name = target.id if target.id in AXIOM_SET else rhs
                elif target.id in FUNCTOR_SET or rhs in FUNCTOR_SET:
                    feature_type = "functorial construction"
                    normalized_name = target.id if target.id in FUNCTOR_SET else rhs
                else:
                    continue
                features.append(
                    FeatureDeclaration(
                        category_id=category_id,
                        owner_path=owner_path,
                        relative_path=relative_feature_path(top_name, owner_path, target.id),
                        feature_name=normalized_name,
                        feature_type=feature_type,
                        declaration_kind="subcategory API alias",
                        target_or_expansion=unparse(value),
                        module=module,
                        source_line=stmt.lineno,
                    )
                )


def scan_category_class_body(
    category_id: str,
    top_name: str,
    node: ast.ClassDef,
    owner_path: str,
    module: str,
) -> None:
    # Category-valued methods declared directly on this category class.
    for stmt in node.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
            scan_category_method(
                category_id,
                top_name,
                owner_path,
                stmt,
                module,
                "category method",
            )

    # Bindings declared in this category class.
    for stmt in node.body:
        if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
            targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
            for target in targets:
                if not isinstance(target, ast.Name) or target.id.startswith("_"):
                    continue
                value = stmt.value
                if value is None:
                    continue
                lazy = parse_lazy_import(value)
                if lazy:
                    target_module, target_name = lazy
                    feature_name = target.id
                    if feature_name in AXIOM_SET:
                        feature_type = "axiom"
                    elif feature_name in FUNCTOR_SET:
                        feature_type = "functorial construction"
                    else:
                        feature_type = "other category"
                    features.append(
                        FeatureDeclaration(
                            category_id=category_id,
                            owner_path=owner_path,
                            relative_path=relative_feature_path(top_name, owner_path, feature_name),
                            feature_name=feature_name,
                            feature_type=feature_type,
                            declaration_kind="lazy-import binding",
                            target_or_expansion=f"{target_module}.{target_name}",
                            module=module,
                            source_line=stmt.lineno,
                        )
                    )
                elif isinstance(stmt.value, (ast.Name, ast.Attribute)):
                    # Record API aliases only when either side names a recognized feature.
                    rhs = unparse(stmt.value).split(".")[-1]
                    if target.id in AXIOM_SET or rhs in AXIOM_SET:
                        ftype = "axiom"
                    elif target.id in FUNCTOR_SET or rhs in FUNCTOR_SET:
                        ftype = "functorial construction"
                    else:
                        continue
                    normalized_name = target.id if target.id in (AXIOM_SET | FUNCTOR_SET) else rhs
                    features.append(
                        FeatureDeclaration(
                            category_id=category_id,
                            owner_path=owner_path,
                            relative_path=relative_feature_path(top_name, owner_path, target.id),
                            feature_name=normalized_name,
                            feature_type=ftype,
                            declaration_kind="API alias",
                            target_or_expansion=unparse(stmt.value),
                            module=module,
                            source_line=stmt.lineno,
                        )
                    )

    # Nested category implementations and SubcategoryMethods interfaces.
    for stmt in node.body:
        if not isinstance(stmt, ast.ClassDef):
            continue
        if stmt.name == "SubcategoryMethods":
            scan_subcategory_methods(category_id, top_name, owner_path, stmt, module)
            continue
        if stmt.name in MIXIN_CONTAINERS:
            continue
        classification = classify_nested_class(stmt)
        if classification:
            feature_type, normalized_name = classification
            rel = relative_feature_path(top_name, owner_path, stmt.name)
            features.append(
                FeatureDeclaration(
                    category_id=category_id,
                    owner_path=owner_path,
                    relative_path=rel,
                    feature_name=normalized_name,
                    feature_type=feature_type,
                    declaration_kind="nested category class",
                    target_or_expansion=", ".join(unparse(b) for b in stmt.bases),
                    module=module,
                    source_line=stmt.lineno,
                )
            )
            scan_category_class_body(
                category_id,
                top_name,
                stmt,
                owner_path + "." + stmt.name,
                module,
            )


for category_id in sorted(category_class_ids):
    rec = top_classes[category_id]
    scan_category_class_body(category_id, rec.name, rec.node, rec.name, rec.module)

# Module-level bindings of category paths, notably the optimized implementation
# of LatticePosets().Distributive(), and global Category methods.
for module, tree in trees.items():
    for stmt in tree.body:
        if not isinstance(stmt, ast.Assign):
            continue
        for target in stmt.targets:
            if not isinstance(target, ast.Attribute):
                continue
            target_text = unparse(target)
            value_text = unparse(stmt.value)
            parts = target_text.split(".")
            if len(parts) < 2:
                continue
            root_name, feature_name = parts[0], parts[-1]
            matching_ids = [cid for cid, rec in top_classes.items() if rec.name == root_name and cid in category_class_ids]
            if not matching_ids:
                continue
            category_id = matching_ids[0]
            if feature_name in AXIOM_SET:
                feature_type = "axiom"
            elif feature_name in FUNCTOR_SET:
                feature_type = "functorial construction"
            else:
                feature_type = "other category"
            features.append(
                FeatureDeclaration(
                    category_id=category_id,
                    owner_path=".".join(parts[:-1]),
                    relative_path=".".join(parts[1:]),
                    feature_name=feature_name,
                    feature_type=feature_type,
                    declaration_kind="module-level binding",
                    target_or_expansion=value_text,
                    module=module,
                    source_line=stmt.lineno,
                )
            )

# ---------------------------------------------------------------------------
# Wrapper functions and their exact returned category expressions
# ---------------------------------------------------------------------------

wrappers: list[dict[str, Any]] = []
for module, tree in trees.items():
    for stmt in tree.body:
        if not isinstance(stmt, ast.FunctionDef) or stmt.name not in PUBLIC_WRAPPER_NAMES:
            continue
        returns = [sub for sub in ast.walk(stmt) if isinstance(sub, ast.Return)]
        return_expr = unparse(returns[-1].value) if returns else ""
        args = [a.arg for a in stmt.args.args]
        terminal = ""
        defining_axiom = ""
        defining_functor = ""
        # Terminal category operation in expressions such as C(...).FiniteDimensional().
        m = re.search(r"\.([A-Za-z][A-Za-z0-9_]*)\(\)$", return_expr)
        if m:
            terminal = m.group(1)
            if terminal in AXIOM_SET:
                defining_axiom = terminal
            if terminal in FUNCTOR_SET:
                defining_functor = terminal
        wrappers.append(
            {
                "category_id": f"{module}.{stmt.name}",
                "constructor": stmt.name,
                "signature": f"{stmt.name}({', '.join(args)})",
                "module": module,
                "source_line": stmt.lineno,
                "return_expression": return_expr,
                "direct_defining_axiom": defining_axiom,
                "defining_functorial_construction": defining_functor,
            }
        )

# ---------------------------------------------------------------------------
# Category definitions and syntactic axiom chains
# ---------------------------------------------------------------------------

# Simple class-name lookup is sufficient for the source's standard naming scheme.
class_name_to_ids: dict[str, list[str]] = defaultdict(list)
for cid in category_class_ids:
    class_name_to_ids[top_classes[cid].name].append(cid)


def direct_definition(category_id: str) -> dict[str, Any]:
    if category_id in hardcoded_definitions:
        base, axiom, line = hardcoded_definitions[category_id]
        return {
            "base": base,
            "axiom": axiom,
            "construction": "",
            "kind": "hardcoded category-with-axiom relation",
            "line": line,
        }
    if category_id in SPECIAL_DEFINITIONS:
        base, axiom = SPECIAL_DEFINITIONS[category_id]
        return {
            "base": base,
            "axiom": axiom,
            "construction": "",
            "kind": "Sage name-heuristic category-with-axiom relation",
            "line": top_classes[category_id].line,
        }
    bindings = incoming_bindings.get(category_id, [])
    for binding in bindings:
        attr = binding["attribute"]
        if attr in AXIOM_SET:
            return {
                "base": binding["source_path"],
                "axiom": attr,
                "construction": "",
                "kind": "lazy-bound category-with-axiom relation",
                "line": binding["line"],
            }
    for binding in bindings:
        attr = binding["attribute"]
        if attr in FUNCTOR_SET:
            return {
                "base": binding["source_path"],
                "axiom": "",
                "construction": attr,
                "kind": "lazy-bound functorial construction relation",
                "line": binding["line"],
            }
    # Infer the construction from a construction-category helper base even when
    # the generic binding is implemented by an inherited method rather than a local LazyImport.
    rec = top_classes[category_id]
    for base_expr in rec.bases:
        helper_name = simple_base_name(base_expr)
        if helper_name in HELPER_TO_FUNCTOR:
            return {
                "base": "",
                "axiom": "",
                "construction": HELPER_TO_FUNCTOR[helper_name],
                "kind": "functorial construction category subclass",
                "line": rec.line,
            }
    if bindings:
        binding = bindings[0]
        return {
            "base": binding["source_path"],
            "axiom": "",
            "construction": "",
            "kind": "named category binding",
            "line": binding["line"],
        }
    return {"base": "", "axiom": "", "construction": "", "kind": "", "line": top_classes[category_id].line}


def resolve_root_category_id(base_expression: str) -> str | None:
    if not base_expression:
        return None
    root = base_expression.split(".")[0]
    ids = class_name_to_ids.get(root, [])
    # Prefer nontechnical named classes when a name were ever ambiguous.
    if not ids:
        return None
    ids = sorted(ids, key=lambda cid: (cid in TECHNICAL_CATEGORY_IDS, cid))
    return ids[0]


def path_axioms(base_expression: str) -> list[str]:
    if not base_expression:
        return []
    parts = base_expression.split(".")[1:]
    return [part for part in parts if part in AXIOM_SET]


def syntactic_axiom_chain(category_id: str, stack: set[str] | None = None) -> list[str]:
    if stack is None:
        stack = set()
    if category_id in stack:
        return []
    stack = set(stack)
    stack.add(category_id)
    definition = direct_definition(category_id)
    if not definition["axiom"]:
        return []
    base_expr = definition["base"]
    chain: list[str] = []
    base_id = resolve_root_category_id(base_expr)
    if base_id:
        chain.extend(syntactic_axiom_chain(base_id, stack))
    chain.extend(path_axioms(base_expr))
    chain.append(definition["axiom"])
    # Stable unique sequence.
    seen: set[str] = set()
    unique: list[str] = []
    for x in chain:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    return unique

# ---------------------------------------------------------------------------
# Aggregate local features and build category rows
# ---------------------------------------------------------------------------

features_by_category: dict[str, list[FeatureDeclaration]] = defaultdict(list)
for feature in features:
    features_by_category[feature.category_id].append(feature)


def aggregate_feature_paths(category_id: str, feature_type: str) -> str:
    vals = sorted(
        {
            f.relative_path
            for f in features_by_category.get(category_id, [])
            if f.feature_type == feature_type
        },
        key=lambda s: (s.count("."), s.lower(), s),
    )
    return "; ".join(vals)


def aggregate_other_paths(category_id: str) -> str:
    vals = sorted(
        {
            f.relative_path
            for f in features_by_category.get(category_id, [])
            if f.feature_type in {"other category", "derived category shorthand"}
        },
        key=lambda s: (s.count("."), s.lower(), s),
    )
    return "; ".join(vals)


def role_for(category_id: str) -> str:
    if category_id in TEST_CATEGORY_IDS:
        return "test-only category class"
    if category_id in TECHNICAL_CATEGORY_IDS:
        return "framework/helper category class"
    return "public named category class"


category_rows: list[dict[str, Any]] = []
for category_id in sorted(category_class_ids, key=lambda cid: (top_classes[cid].name.lower(), cid)):
    rec = top_classes[category_id]
    definition = direct_definition(category_id)
    bindings = incoming_bindings.get(category_id, [])
    bound_as = "; ".join(
        sorted({f"{b['source_path']}.{b['attribute']}" for b in bindings})
    )
    relation = ""
    if definition["axiom"]:
        relation = f"{definition['base']} + axiom {definition['axiom']}"
    elif definition["construction"]:
        base_text = definition["base"] or "generic base category"
        relation = f"{base_text}.{definition['construction']}()"
    elif definition["base"]:
        relation = f"bound from {definition['base']}"
    notes: list[str] = []
    if category_id == "lattice_posets.DistributiveLattices":
        notes.append(
            "The public shorthand LatticePosets().Distributive() expands to Trim then ChainGraded; "
            "the implementation class is bound at LatticePosets.Trim.ChainGraded."
        )
    if category_id == "facade_sets.FacadeSets":
        notes.append("The base/axiom relation is inferred by Sage's documented category-name heuristic.")
    if category_id == "facade_sets.FacadeSets":
        notes.append("Listed under Technical Categories in Sage's reference index, but callable as Sets().Facade().")
    category_rows.append(
        {
            "category_id": category_id,
            "constructor": rec.name,
            "module": rec.module,
            "source_line": rec.line,
            "source": f"src/sage/categories/{rec.module}.py:{rec.line}",
            "source_url": source_url(rec.module, rec.line),
            "bases": ", ".join(rec.bases),
            "role": role_for(category_id),
            "implementation_kind": "Python class",
            "defining_relation": relation,
            "direct_defining_axiom": definition["axiom"],
            "syntactic_defining_axiom_chain": "; ".join(syntactic_axiom_chain(category_id)),
            "defining_functorial_construction": definition["construction"],
            "bound_as": bound_as,
            "local_axiom_paths": aggregate_feature_paths(category_id, "axiom"),
            "local_functorial_construction_paths": aggregate_feature_paths(category_id, "functorial construction"),
            "other_local_category_paths": aggregate_other_paths(category_id),
            "notes": " ".join(notes),
        }
    )

category_rows.append(CYTHON_TECHNICAL_CATEGORY.copy())
category_rows.append(CYTHON_EXAMPLE_CATEGORY.copy())

for wrapper in wrappers:
    relation = wrapper["return_expression"]
    category_rows.append(
        {
            "category_id": wrapper["category_id"],
            "constructor": wrapper["signature"],
            "module": wrapper["module"],
            "source_line": wrapper["source_line"],
            "source": f"src/sage/categories/{wrapper['module']}.py:{wrapper['source_line']}",
            "source_url": source_url(wrapper["module"], wrapper["source_line"]),
            "bases": "",
            "role": "public category-valued wrapper constructor",
            "implementation_kind": "Python function",
            "defining_relation": relation,
            "direct_defining_axiom": wrapper["direct_defining_axiom"],
            "syntactic_defining_axiom_chain": wrapper["direct_defining_axiom"],
            "defining_functorial_construction": wrapper["defining_functorial_construction"],
            "bound_as": "",
            "local_axiom_paths": "",
            "local_functorial_construction_paths": "",
            "other_local_category_paths": "",
            "notes": "Returns a dynamically constructed category rather than an instance of a dedicated class.",
        }
    )

category_rows.sort(key=lambda r: (r["role"], re.sub(r"\(.*", "", r["constructor"]).lower(), r["category_id"]))

# ---------------------------------------------------------------------------
# Axiom rows
# ---------------------------------------------------------------------------

# Add top-level defining relations to the axiom implementation index.
defining_axiom_categories: dict[str, list[str]] = defaultdict(list)
for row in category_rows:
    if row["direct_defining_axiom"]:
        defining_axiom_categories[row["direct_defining_axiom"]].append(row["category_id"])

axiom_rows: list[dict[str, Any]] = []
for registry in axiom_registry:
    name = registry["axiom"]
    decls = [f for f in features if f.feature_type == "axiom" and f.feature_name == name]
    interface_sites = sorted(
        {f"{f.category_id}:{f.relative_path}" for f in decls if f.declaration_kind in {"subcategory interface method", "subcategory API alias"}}
    )
    implementation_sites = sorted(
        {
            f"{f.category_id}:{f.relative_path} [{f.declaration_kind}]"
            for f in decls
            if f.declaration_kind not in {"subcategory interface method", "subcategory API alias"}
        }
    )
    expansions = sorted(
        {
            f"{f.category_id}:{f.relative_path} -> {f.target_or_expansion}"
            for f in decls
            if f.target_or_expansion and f.declaration_kind == "subcategory interface method"
        }
    )
    axiom_rows.append(
        {
            "axiom": name,
            "status": registry["status"],
            "registry_source": f"src/sage/categories/{registry['registry_module']}.py:{registry['registry_line']}",
            "registry_source_url": source_url(registry["registry_module"], registry["registry_line"]),
            "defining_named_categories": "; ".join(sorted(defining_axiom_categories.get(name, []))),
            "interface_declarations": "; ".join(interface_sites),
            "implementation_or_binding_declarations": "; ".join(implementation_sites),
            "method_expansions": "; ".join(expansions),
        }
    )

# ---------------------------------------------------------------------------
# Functorial construction rows
# ---------------------------------------------------------------------------


def construction_flavor(helper: dict[str, Any]) -> str:
    bases = helper["bases"]
    if any("RegressiveCovariantConstructionCategory" in b for b in bases):
        return "regressive covariant"
    if any("CovariantConstructionCategory" in b for b in bases):
        return "covariant"
    if any("FunctorialConstructionCategory" in b for b in bases):
        return "general/specialized functorial"
    return "functor implementation"


def is_functor_interface_declaration(feature: FeatureDeclaration) -> bool:
    return feature.declaration_kind in {"subcategory interface method", "subcategory API alias"} or (
        feature.category_id == "category.Category" and feature.declaration_kind == "module-level binding"
    )


functor_rows: list[dict[str, Any]] = []
for name in FUNCTORS:
    helpers = functor_helpers[name]
    category_helpers = [h for h in helpers if h["is_category_class"]]
    selected = category_helpers[0] if category_helpers else helpers[0]
    decls = [f for f in features if f.feature_type == "functorial construction" and f.feature_name == name]
    interface_sites = sorted(
        {f"{f.category_id}:{f.relative_path}" for f in decls if is_functor_interface_declaration(f)}
    )
    implementation_sites = sorted(
        {
            f"{f.category_id}:{f.relative_path} [{f.declaration_kind}]"
            for f in decls
            if not is_functor_interface_declaration(f)
        }
    )
    result_categories = sorted(
        {
            row["category_id"]
            for row in category_rows
            if row["defining_functorial_construction"] == name
        }
    )
    functor_rows.append(
        {
            "construction": name,
            "flavor": construction_flavor(selected),
            "category_implementation_class": selected["class_id"],
            "implementation_source": f"src/sage/categories/{selected['module']}.py:{selected['line']}",
            "implementation_source_url": source_url(selected["module"], selected["line"]),
            "implementation_module": selected["module"],
            "implementation_line": selected["line"],
            "other_classes_with_same_functor_tag": "; ".join(
                sorted(h["class_id"] for h in helpers if h["class_id"] != selected["class_id"])
            ),
            "interface_declarations": "; ".join(interface_sites),
            "specialized_implementation_declarations": "; ".join(implementation_sites),
            "named_result_categories": "; ".join(result_categories),
        }
    )

# ---------------------------------------------------------------------------
# Feature declaration rows
# ---------------------------------------------------------------------------

feature_rows = []
for f in sorted(
    features,
    key=lambda x: (x.category_id, x.relative_path, x.feature_type, x.declaration_kind, x.source_line),
):
    feature_rows.append(
        {
            "category_id": f.category_id,
            "owner_path": f.owner_path,
            "relative_path": f.relative_path,
            "feature_name": f.feature_name,
            "feature_type": f.feature_type,
            "declaration_kind": f.declaration_kind,
            "target_or_expansion": f.target_or_expansion,
            "source": f.source,
            "source_url": f.source_url,
            "notes": f.notes,
        }
    )

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

public_class_count = sum(r["role"] == "public named category class" for r in category_rows)
public_wrapper_count = sum(r["role"] == "public category-valued wrapper constructor" for r in category_rows)
technical_count = sum(r["role"] == "framework/helper category class" for r in category_rows)
test_count = sum(r["role"] == "test-only category class" for r in category_rows)
example_count = sum(r["role"] == "example-only category class" for r in category_rows)

assert VERSION == "10.9"
assert SDIST_SHA256 == "5855626668197958372403dc6fa1878750b90ac7f113f49a5bc43ddaafd60591"
assert len(AXIOMS) == 51 and len(set(AXIOMS)) == 51
assert len(FUNCTORS) == 17 and len(set(FUNCTORS)) == 17
assert public_class_count == 173
assert public_wrapper_count == 6
assert technical_count == 38
assert test_count == 4
assert example_count == 1
assert len(category_class_ids) == 214  # Root Python classes; Cython classes are added separately.
assert len(category_rows) == 222
assert len(feature_rows) == 444
assert len(ALIASES) == 6
assert all(name in {r["axiom"] for r in axiom_rows} for name in AXIOMS)
assert all(name in {r["construction"] for r in functor_rows} for name in FUNCTORS)
assert any(r["category_id"] == "algebras.Algebras" and r["feature_name"] == "Semisimple" for r in feature_rows)
assert any(r["category_id"] == "drinfeld_modules.DrinfeldModules" and r["feature_name"] == "Homsets" for r in feature_rows)
assert any(r["category_id"] == "drinfeld_modules.DrinfeldModules" and r["feature_name"] == "Endsets" for r in feature_rows)
assert any(r["category_id"] == "manifolds.Manifolds" and r["feature_name"] == "Complex" for r in feature_rows)
assert any(r["category_id"] == "modules.Modules" and r["relative_path"] == "dual" and r["feature_name"] == "DualObjects" for r in feature_rows)
assert any(r["category_id"] == "category_with_axiom.Blahs" and r["feature_name"] == "Flying" for r in feature_rows)

# ---------------------------------------------------------------------------
# Write CSV / JSON / Markdown
# ---------------------------------------------------------------------------


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


categories_csv = OUT / f"sagemath-{VERSION}-categories.csv"
features_csv = OUT / f"sagemath-{VERSION}-category-feature-declarations.csv"
axioms_csv = OUT / f"sagemath-{VERSION}-axioms.csv"
functors_csv = OUT / f"sagemath-{VERSION}-functorial-constructions.csv"
aliases_csv = OUT / f"sagemath-{VERSION}-category-aliases.csv"
json_path = OUT / f"sagemath-{VERSION}-category-inventory.json"
markdown_path = OUT / f"sagemath-{VERSION}-category-inventory.md"
zip_path = OUT / f"sagemath-{VERSION}-category-inventory.zip"

write_csv(categories_csv, category_rows)
write_csv(features_csv, feature_rows)
write_csv(axioms_csv, axiom_rows)
write_csv(functors_csv, functor_rows)

alias_rows = []
for alias in ALIASES:
    alias_rows.append(
        {
            **alias,
            "source": f"src/sage/categories/{alias['module']}.py:{alias['source_line']}",
            "source_url": source_url(str(alias["module"]), int(alias["source_line"])),
        }
    )
write_csv(aliases_csv, alias_rows)

payload = {
    "metadata": {
        "sage_version": VERSION,
        "sage_commit": COMMIT,
        "sdist_sha256": SDIST_SHA256,
        "scope": "Named category classes and category-valued wrapper constructors in src/sage/categories, including sage.categories.examples, plus source-declared axioms and functorial constructions.",
        "counts": {
            "public_named_category_classes": public_class_count,
            "public_category_wrapper_constructors": public_wrapper_count,
            "framework_helper_category_classes": technical_count,
            "test_only_category_classes": test_count,
            "example_only_category_classes": example_count,
            "registered_axioms": len(AXIOMS),
            "functorial_constructions": len(FUNCTORS),
            "feature_declarations": len(feature_rows),
            "aliases": len(alias_rows),
        },
    },
    "categories": category_rows,
    "feature_declarations": feature_rows,
    "axioms": axiom_rows,
    "functorial_constructions": functor_rows,
    "aliases": alias_rows,
}
json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def md_escape(value: Any) -> str:
    text = str(value or "")
    return text.replace("|", "\\|").replace("\n", "<br>")


def md_table(headers: list[str], rows: Iterable[Iterable[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(md_escape(x) for x in row) + " |")
    return "\n".join(out)


def source_link(module: str, line: int, suffix: str = "py") -> str:
    return f"[`{module}.{suffix}:{line}`]({source_url(module, line, suffix)})"


md: list[str] = []
md.append(f"# SageMath {VERSION}: complete source inventory of categories, axioms, and functorial constructions")
md.append("")
md.append(
    f"**Revision.** SageMath `{VERSION}`, commit [`{COMMIT}`](https://github.com/sagemath/sage/commit/{COMMIT}). "
    f"The audited source distribution has SHA-256 `{SDIST_SHA256}`."
)
md.append("")
md.append("## Scope and interpretation")
md.append("")
md.append(
    "Sage can construct infinitely many category *instances*: categories may be parameterized by base rings or other objects, "
    "joined by intersection, refined by combinations of axioms, and transformed by functorial constructions. Therefore a finite "
    "literal list of all runtime instances does not exist. This inventory gives the finite, reproducible source-level list of "
    "named category classes and public category-valued wrapper constructors implemented in `src/sage/categories` at the revision above, "
    "including the sole category class in `sage.categories.examples`."
)
md.append("")
md.append(
    "For each named category, the inventory distinguishes: (i) the source relation defining a category-with-axiom or named "
    "functorial-construction result; (ii) the **syntactic defining axiom chain** obtained from those source relations; "
    "(iii) locally declared axiom implementations/entry points; and (iv) locally declared functorial constructions. "
    "The local columns do not claim to be the complete runtime method set of every instance: Sage dynamically inherits and "
    "combines declarations through supercategories, joins, and generated category classes. The declaration-level CSV records "
    "all declarations matched by the audit's explicit source patterns: nested category classes, direct category-valued "
    "methods, `SubcategoryMethods` methods, lazy bindings, recognized API aliases, and module-level category bindings."
)
md.append("")
md.append("### Counts")
md.append("")
md.append(
    md_table(
        ["Item", "Count"],
        [
            ("Public named category classes", public_class_count),
            ("Public category-valued wrapper constructors", public_wrapper_count),
            ("Framework/helper category classes", technical_count),
            ("Test-only category classes", test_count),
            ("Example-only category classes", example_count),
            ("Registered axioms", len(AXIOMS)),
            ("Functorial constructions", len(FUNCTORS)),
            ("Source-level feature declarations", len(feature_rows)),
            ("Documented compatibility aliases", len(alias_rows)),
        ],
    )
)
md.append("")
md.append("## Registered axioms")
md.append("")
md.append(
    "`Flying` and `Blue` are intentionally retained below because they occur in the executable global registry; their only "
    "implementations are test fixtures. The five semigroup-specific axioms are appended to the registry in `semigroups.py`."
)
md.append("")
md.append(
    md_table(
        ["Axiom", "Status", "Defining named category classes", "Interface sites", "Implementation/binding sites", "Registry"],
        (
            (
                r["axiom"],
                r["status"],
                r["defining_named_categories"],
                r["interface_declarations"],
                r["implementation_or_binding_declarations"],
                f"[`{r['registry_source']}`]({r['registry_source_url']})",
            )
            for r in axiom_rows
        ),
    )
)
md.append("")
md.append("## Functorial constructions")
md.append("")
md.append(
    md_table(
        ["Construction", "Flavor", "Implementation class", "Interface sites", "Specialized implementation sites", "Named result categories", "Source"],
        (
            (
                r["construction"],
                r["flavor"],
                r["category_implementation_class"],
                r["interface_declarations"],
                r["specialized_implementation_declarations"],
                r["named_result_categories"],
                f"[`{r['implementation_source']}`]({r['implementation_source_url']})",
            )
            for r in functor_rows
        ),
    )
)
md.append("")
md.append("## Public named category classes")
md.append("")
public_rows = [r for r in category_rows if r["role"] == "public named category class"]
md.append(
    md_table(
        ["Category class", "Module", "Defining relation", "Syntactic defining axioms", "Local axiom paths", "Local functorial-construction paths", "Other local category paths", "Source"],
        (
            (
                r["constructor"],
                r["module"],
                r["defining_relation"],
                r["syntactic_defining_axiom_chain"],
                r["local_axiom_paths"],
                r["local_functorial_construction_paths"],
                r["other_local_category_paths"],
                source_link(r["module"], r["source_line"]),
            )
            for r in sorted(public_rows, key=lambda x: (x["constructor"].lower(), x["category_id"]))
        ),
    )
)
md.append("")
md.append("## Public category-valued wrapper constructors")
md.append("")
wrapper_rows = [r for r in category_rows if r["role"] == "public category-valued wrapper constructor"]
md.append(
    md_table(
        ["Constructor", "Exact returned category expression", "Axiom", "Functorial construction", "Source"],
        (
            (
                r["constructor"],
                r["defining_relation"],
                r["direct_defining_axiom"],
                r["defining_functorial_construction"],
                source_link(r["module"], r["source_line"]),
            )
            for r in sorted(wrapper_rows, key=lambda x: x["constructor"].lower())
        ),
    )
)
md.append("")
md.append("## Framework/helper, test-only, and example-only category classes")
md.append("")
aux_rows = [
    r for r in category_rows
    if r["role"] in {"framework/helper category class", "test-only category class", "example-only category class"}
]
md.append(
    md_table(
        ["Category class", "Role", "Module", "Bases", "Local axiom paths", "Local functorial paths", "Source"],
        (
            (
                r["constructor"],
                r["role"],
                r["module"],
                r["bases"],
                r["local_axiom_paths"],
                r["local_functorial_construction_paths"],
                source_link(r["module"], r["source_line"], "pyx" if r["implementation_kind"] == "Cython class" else "py"),
            )
            for r in sorted(aux_rows, key=lambda x: (x["role"], x["constructor"].lower()))
        ),
    )
)
md.append("")
md.append("## Compatibility aliases")
md.append("")
md.append(
    md_table(
        ["Alias", "Canonical constructor", "Status", "Source"],
        (
            (
                r["alias"],
                r["canonical"],
                r["status"],
                source_link(str(r["module"]), int(r["source_line"])),
            )
            for r in alias_rows
        ),
    )
)
md.append("")
md.append("## Machine-readable companion files")
md.append("")
md.append(
    "- `sagemath-10.9-categories.csv`: one row per class or public wrapper constructor.\n"
    "- `sagemath-10.9-category-feature-declarations.csv`: one row per source declaration, including nested paths and declaration modes.\n"
    "- `sagemath-10.9-axioms.csv`: one row per registered axiom.\n"
    "- `sagemath-10.9-functorial-constructions.csv`: one row per `_functor_category` name.\n"
    "- `sagemath-10.9-category-aliases.csv`: compatibility aliases.\n"
    "- `sagemath-10.9-category-inventory.json`: the complete combined dataset.\n"
    "- `build_sage_category_inventory.py`: the deterministic AST-based generator used for the audit."
)
md.append("")
md.append("## Audit checks")
md.append("")
md.append(
    f"The generator asserts the expected source counts, uniqueness of all {len(AXIOMS)} axiom names and {len(FUNCTORS)} "
    f"functorial-construction names, the {len(feature_rows)} source-level feature declarations, the source-distribution hash, "
    f"and complete representation of all detected category classes."
)

markdown_path.write_text("\n".join(md) + "\n", encoding="utf-8")

# Put the report and machine-readable files into one deterministic convenience archive.
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in [
        markdown_path,
        categories_csv,
        features_csv,
        axioms_csv,
        functors_csv,
        aliases_csv,
        json_path,
        Path(__file__).resolve(),
    ]:
        zf.write(path, arcname=path.name)

summary = {
    "version": VERSION,
    "commit": COMMIT,
    "sdist_sha256": SDIST_SHA256,
    "counts": cast(dict[str, Any], payload["metadata"])["counts"],
    "files": [
        str(markdown_path),
        str(categories_csv),
        str(features_csv),
        str(axioms_csv),
        str(functors_csv),
        str(aliases_csv),
        str(json_path),
        str(Path(__file__).resolve()),
        str(zip_path),
    ],
}
print(json.dumps(summary, indent=2))
