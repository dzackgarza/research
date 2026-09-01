r"""Programmatic megadoc extractor and renderer for preamble constructions.

This module walks the AST of ``dzack_research.preamble`` to extract all public
classes, constructors, public methods, categories, super-categories,
ParentMethods, ElementMethods, functors, adjunctions, universal constructions,
morphisms, objects, and catalogue definitions without importing SageMath or
incurring runtime overhead.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Final, Literal

SymbolKind = Literal[
    "CATEGORY",
    "SUBCATEGORY",
    "FUNCTOR",
    "ADJUNCTION",
    "CONSTRUCTION",
    "MORPHISM",
    "HOMSET",
    "OBJECT",
    "ELEMENT",
    "CATALOGUE",
    "REGISTRY",
    "FUNCTION",
]

SUBSYSTEM_ORDER: Final[list[tuple[str, str, str]]] = [
    (
        "abstract_categories",
        "Abstract Category Theory & Universal Constructions",
        "Category of categories (Cat), Arrow and Slice categories, Limits, Colimits, Biproducts, Subobjects, and Diagram categories.",
    ),
    (
        "functors",
        "Functors & Adjunctions",
        "Functorial constructions, Adjunctions, Base change, Free/Forgetful, Cohomology, De Rham, Group actions, and Induction.",
    ),
    (
        "lattices",
        "Lattices, Quadratic Forms & Invariants",
        "Free modules with quadratic forms, Genus, Definite/Root/Rational lattices, Isometries, Embeddings, Orbits, and Diagrams.",
    ),
    (
        "modules",
        "Modules, Complexes & Homological Algebra",
        "Framed free modules, Finitely presented modules, Formed modules, Group modules, Cochain complexes, Connections, and DG modules.",
    ),
    (
        "algebras",
        "Algebras & Differential Graded Algebras",
        "Associative/Commutative algebras, DGAs, Cohomology algebras, De Rham algebras, Derivations, and Graded algebras.",
    ),
    (
        "group",
        "Groups, Profinite Groups & Galois Theory",
        "Groups, Finitely presented groups, G-Sets, Actions, Profinite groups, Absolute Galois groups, Characters, and Inertia.",
    ),
    (
        "rings",
        "Rings, Fields & Commutative Algebra",
        "Owned rings, Fields, Number fields, Prime spectrum, Completions, Localizations, Exact real field, and Predicate subrings.",
    ),
    (
        "schemes",
        "Schemes & Algebraic Geometry",
        "Schemes, Affine/Projective schemes, Subschemes, Varieties, Curves, Surfaces, Polytopes, and Structure sheaves.",
    ),
    (
        "divisors",
        "Divisors & Picard Theory",
        "Divisor groups, Cartier divisors, Weil divisors, Picard groups, Class groups, and Formal divisors.",
    ),
    (
        "forms",
        "Bilinear Forms, Quadratic Forms & Pairings",
        "Bilinear/Quadratic forms, Pairings, Gram matrices, and Form spaces.",
    ),
    (
        "functions",
        "Function Spaces & Analysis",
        "Lebesgue modules, Lp, ell, C(X), Graded Lebesgue algebras, and Convolution algebras.",
    ),
    (
        "sets",
        "Sets, Cardinals & Ordinals",
        "Sets, Cardinalities, Ordinals, Enumerated sets, Fourier characters, Hermite polynomials, and Power sets.",
    ),
    (
        "catalogue",
        "Named Catalogue & Classification Tables",
        "Named integral lattices (U, E8, LK3, Mukai, etc.), 2-elementary tables, Nikulin involutions, and Primitive embeddings.",
    ),
    (
        "tensors",
        "Tensor Calculus",
        "Multilinear tensors, Tensor modules, Tensor shapes, and Tensor products.",
    ),
    (
        "logic",
        "Logic & Predicates",
        "Three-valued logic predicates, queries, and certainty propagation.",
    ),
    (
        "geometry_specialized",
        "Specialized Geometries (Coble & Sterk)",
        "Coble surfaces, Sterk invariant theory, and Automorphic forms.",
    ),
    (
        "lexicon",
        "Mathematical Lexicon & Vocabulary",
        "Canonical vocabulary across algebra, foundations, geometry, and interop layers.",
    ),
    (
        "preamble_root",
        "Preamble Entrypoints & Utilities",
        "Top-level session loaders, environment initializers, and refinement helpers.",
    ),
]


@dataclass
class MethodDoc:
    name: str
    args: str
    return_type: str
    doc: str
    decorators: list[str] = field(default_factory=list)


@dataclass
class InnerClassDoc:
    name: str
    doc: str
    methods: list[MethodDoc] = field(default_factory=list)


@dataclass
class SymbolDoc:
    name: str
    kind: SymbolKind
    subsystem: str
    file_path: str
    line_number: int
    doc: str
    bases: list[str] = field(default_factory=list)
    super_categories: list[str] = field(default_factory=list)
    category_constructors: list[MethodDoc] = field(default_factory=list)
    object_constructors: list[MethodDoc] = field(default_factory=list)
    constructors: list[MethodDoc] = field(default_factory=list)
    methods: list[MethodDoc] = field(default_factory=list)
    parent_methods: list[MethodDoc] = field(default_factory=list)
    element_methods: list[MethodDoc] = field(default_factory=list)
    subcategory_methods: list[MethodDoc] = field(default_factory=list)
    inner_classes: list[InnerClassDoc] = field(default_factory=list)
    class_vars: list[tuple[str, str]] = field(default_factory=list)
    is_exported_in_all: bool = False
    export_module: str = ""


class PreambleExtractor:
    r"""Extract mathematical constructions from ASTs of preamble python source files."""

    def __init__(self, preamble_root: Path | None = None) -> None:
        if preamble_root is None:
            preamble_root = Path(__file__).resolve().parent
        self.preamble_root: Path = preamble_root
        self.exported_symbols: dict[str, str] = self._load_all_exports()

    def _load_all_exports(self) -> dict[str, str]:
        all_py = self.preamble_root / "all.py"
        exported: dict[str, str] = {}
        if not all_py.exists():
            return exported
        try:
            with open(all_py, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(all_py))
            for node in tree.body:
                if isinstance(node, ast.ImportFrom) and node.module:
                    if "dzack_research.preamble" in node.module:
                        for alias in node.names:
                            exported[alias.name] = node.module
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and not target.id.startswith("_"):
                            exported[target.id] = "dzack_research.preamble.all"
                elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                    exported[node.name] = "dzack_research.preamble.all"
        except Exception:
            pass
        return exported

    def _determine_subsystem(self, rel_path: str, name: str) -> str:
        parts = Path(rel_path).parts
        if not parts:
            return "preamble_root"
        if parts[0] == "categories":
            if len(parts) > 2:
                # categories/<subsystem_dir>/...
                return parts[1]
            if len(parts) == 2:
                cat_sub = parts[1]
                if cat_sub.endswith(".py"):
                    stem = Path(cat_sub).stem
                    if stem in (
                        "lattices",
                        "_lattice",
                        "definite_lattices",
                        "rational_lattices",
                        "root_lattices",
                        "lattice_morphisms",
                        "lattice_properties",
                        "lattice_engines",
                        "isotropic_orbits",
                        "vector_orbits",
                        "orthogonal_quotients",
                        "coxeter_diagrams",
                    ):
                        return "lattices"
                    if stem in ("free_modules",):
                        return "modules"
                    return stem
                return cat_sub
        if len(parts) > 1:
            # <top_dir>/...
            return parts[0]
        # Top-level file
        top = parts[0]
        if top == "catalogue.py":
            return "catalogue"
        if top == "logic.py":
            return "logic"
        if top in ("coble.py", "sterk.py"):
            return "geometry_specialized"
        if top in ("all.py", "utilities.py", "refine.py", "__init__.py"):
            return "preamble_root"
        return Path(top).stem

    def _classify_class(self, name: str, bases: list[str], body: list[ast.stmt], rel_path: str) -> SymbolKind:
        bases_str = " ".join(bases)
        has_parent_m = any(isinstance(n, ast.ClassDef) and n.name == "ParentMethods" for n in body)
        has_elem_m = any(isinstance(n, ast.ClassDef) and n.name == "ElementMethods" for n in body)

        if "catalogue" in rel_path or name in ("NamedLattices", "Involutions", "Embeddings") or "Table" in name:
            return "CATALOGUE"
        if "Adjunction" in name or any("Adjunction" in b for b in bases):
            return "ADJUNCTION"
        if "Functor" in name or any("Functor" in b for b in bases) or name in ("NaturalTransformation", "NaturalIsomorphism"):
            return "FUNCTOR"
        if (
            any(
                b in ("Category", "OwnedCategoryOverBaseRing", "Category_over_base_ring", "Category_singleton", "HomCategoryConstruction")
                for b in bases
            )
            or has_parent_m
            or has_elem_m
        ):
            if any(
                p in name
                for p in (
                    "Definite",
                    "Even",
                    "Unimodular",
                    "Finite",
                    "Countable",
                    "Infinite",
                    "Uncountable",
                    "Commutative",
                    "Smooth",
                    "Integral",
                    "Separated",
                    "Projective",
                    "Affine",
                    "Nondegenerate",
                )
            ):
                return "SUBCATEGORY"
            return "CATEGORY"
        if any(k in bases_str for k in ("Morphism", "ArrowObject", "CommutativeSquare", "Homomorphism", "Embedding", "Isometry", "Inclusion", "Map")):
            return "MORPHISM"
        if any(k in bases_str for k in ("Homset", "HomCategory")):
            return "HOMSET"
        if any(k in bases_str for k in ("Element", "ModuleElement")) or name.endswith("Element"):
            return "ELEMENT"
        if any(k in bases_str for k in ("Parent", "UniqueRepresentation", "SageObject", "Tensor", "GradedDirectSumModule")) or name in (
            "Lattice",
            "Genus",
            "Tensor",
            "Coble",
            "Sterk",
            "Predicate",
        ):
            return "OBJECT"
        if (
            "Category" in name
            or name.endswith("Categories")
            or name.endswith("Groups")
            or name.endswith("Modules")
            or name.endswith("Algebras")
            or name.endswith("Schemes")
            or name.endswith("Sets")
            or name.endswith("Rings")
            or name.endswith("Spaces")
        ):
            return "CATEGORY"
        return "OBJECT"

    def _classify_function(self, name: str, rel_path: str) -> SymbolKind:
        if name in (
            "TensorProduct",
            "TensorSquare",
            "Biproduct",
            "Product",
            "Coproduct",
            "Kernel",
            "Cokernel",
            "Subobjects",
            "Superobjects",
            "SliceOver",
            "CosliceUnder",
            "DirectSumObjects",
            "DirectSumDecomposition",
            "common_category",
            "ambient_category_of",
            "scheme_product",
            "cartesian_product_of",
        ):
            return "CONSTRUCTION"
        if "adjunction" in name or "Adjunction" in name:
            return "ADJUNCTION"
        if "functor" in name or "Functor" in name:
            return "FUNCTOR"
        if name.startswith("register_"):
            return "REGISTRY"
        return "FUNCTION"

    def extract_all(self) -> list[SymbolDoc]:
        symbols: list[SymbolDoc] = []
        for path in sorted(self.preamble_root.rglob("*.py")):
            if path.name.startswith("."):
                continue
            rel_path = str(path.relative_to(self.preamble_root))
            try:
                with open(path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=str(path))
            except Exception:
                continue

            for node in tree.body:
                if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                    symbol = self._extract_class(node, rel_path, str(path))
                    symbols.append(symbol)
                elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                    symbol = self._extract_function(node, rel_path, str(path))
                    symbols.append(symbol)

        return symbols

    def _extract_method(self, node: ast.FunctionDef) -> MethodDoc:
        args = ast.unparse(node.args)
        ret = f" -> {ast.unparse(node.returns)}" if node.returns else ""
        doc = ast.get_docstring(node) or ""
        decorators = [ast.unparse(d) for d in node.decorator_list]
        return MethodDoc(
            name=node.name,
            args=args,
            return_type=ret,
            doc=doc.strip(),
            decorators=decorators,
        )

    def _extract_class(self, node: ast.ClassDef, rel_path: str, full_path: str) -> SymbolDoc:
        name = node.name
        doc = (ast.get_docstring(node) or "").strip()
        bases = [ast.unparse(b) for b in node.bases]
        subsystem = self._determine_subsystem(rel_path, name)
        kind = self._classify_class(name, bases, node.body, rel_path)

        category_constructors: list[MethodDoc] = []
        object_constructors: list[MethodDoc] = []
        constructors: list[MethodDoc] = []
        methods: list[MethodDoc] = []
        parent_methods: list[MethodDoc] = []
        element_methods: list[MethodDoc] = []
        subcategory_methods: list[MethodDoc] = []
        inner_classes: list[InnerClassDoc] = []
        class_vars: list[tuple[str, str]] = []
        super_categories: list[str] = []

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                if item.name in ("__classcall_private__", "__init__") and kind in ("CATEGORY", "SUBCATEGORY"):
                    category_constructors.append(self._extract_method(item))
                elif item.name in ("_call_", "__call__", "_element_constructor_") and kind in ("CATEGORY", "SUBCATEGORY"):
                    object_constructors.append(self._extract_method(item))
                elif item.name in ("__init__", "_call_", "__call__", "__classcall_private__", "_element_constructor_"):
                    constructors.append(self._extract_method(item))
                elif not item.name.startswith("_"):
                    methods.append(self._extract_method(item))
                if item.name == "super_categories":
                    for stmt in item.body:
                        if isinstance(stmt, ast.Return) and stmt.value:
                            super_categories.append(ast.unparse(stmt.value))
            elif isinstance(item, ast.ClassDef) and not item.name.startswith("_"):
                inner_m = [
                    self._extract_method(m) for m in item.body if isinstance(m, ast.FunctionDef) and not m.name.startswith("_")
                ]
                inner_doc = (ast.get_docstring(item) or "").strip()
                if item.name == "ParentMethods":
                    parent_methods.extend(inner_m)
                elif item.name == "ElementMethods":
                    element_methods.extend(inner_m)
                elif item.name == "SubcategoryMethods":
                    subcategory_methods.extend(inner_m)
                else:
                    inner_classes.append(InnerClassDoc(name=item.name, doc=inner_doc, methods=inner_m))
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and not target.id.startswith("_"):
                        try:
                            val_str = ast.unparse(item.value)
                            if len(val_str) > 80:
                                val_str = val_str[:77] + "..."
                            class_vars.append((target.id, val_str))
                        except Exception:
                            pass

        is_exported = name in self.exported_symbols
        export_mod = self.exported_symbols.get(name, "")

        return SymbolDoc(
            name=name,
            kind=kind,
            subsystem=subsystem,
            file_path=rel_path,
            line_number=node.lineno,
            doc=doc,
            bases=bases,
            super_categories=super_categories,
            category_constructors=category_constructors,
            object_constructors=object_constructors,
            constructors=constructors,
            methods=methods,
            parent_methods=parent_methods,
            element_methods=element_methods,
            subcategory_methods=subcategory_methods,
            inner_classes=inner_classes,
            class_vars=class_vars,
            is_exported_in_all=is_exported,
            export_module=export_mod,
        )

    def _extract_function(self, node: ast.FunctionDef, rel_path: str, full_path: str) -> SymbolDoc:
        name = node.name
        doc = (ast.get_docstring(node) or "").strip()
        subsystem = self._determine_subsystem(rel_path, name)
        kind = self._classify_function(name, rel_path)
        method = self._extract_method(node)

        is_exported = name in self.exported_symbols
        export_mod = self.exported_symbols.get(name, "")

        return SymbolDoc(
            name=name,
            kind=kind,
            subsystem=subsystem,
            file_path=rel_path,
            line_number=node.lineno,
            doc=doc,
            constructors=[method],
            is_exported_in_all=is_exported,
            export_module=export_mod,
        )


class PreambleRenderer:
    r"""Render extracted preamble mathematical constructions to Markdown, Text, or JSON."""

    @staticmethod
    def _first_sentence(doc: str) -> str:
        if not doc:
            return ""
        lines = [line.strip() for line in doc.splitlines() if line.strip()]
        if not lines:
            return ""
        first = lines[0]
        match = re.search(r"(.*?\.\s)", first)
        if match:
            return match.group(1).strip()
        return first

    @classmethod
    def _get_subsystem_sequence(cls, symbols: list[SymbolDoc]) -> list[tuple[str, str, str]]:
        known_map = {key: (title, desc) for key, title, desc in SUBSYSTEM_ORDER}
        found_keys = {s.subsystem for s in symbols}
        result: list[tuple[str, str, str]] = []
        for key, title, desc in SUBSYSTEM_ORDER:
            if key in found_keys:
                result.append((key, title, desc))
        for key in sorted(found_keys):
            if key not in known_map:
                title = key.replace("_", " ").title()
                desc = f"Constructions defined in subsystem {key}."
                result.append((key, title, desc))
        return result

    @classmethod
    def render_markdown(
        cls,
        symbols: list[SymbolDoc],
        subsystem_filter: str | None = None,
        kind_filter: str | None = None,
        search_query: str | None = None,
        session_only: bool = False,
        summary_only: bool = False,
    ) -> str:
        filtered = cls._filter_symbols(symbols, subsystem_filter, kind_filter, search_query, session_only)
        subsystems = cls._get_subsystem_sequence(filtered)
        lines: list[str] = []

        lines.append("# Preamble Mathematical Constructions Megadoc\n")
        lines.append(
            "Programmatic catalogue of all reusable mathematical categories, subcategories, "
            "functors, adjunctions, universal constructions, morphisms, objects, and classification tables "
            "owned by `dzack_research.preamble`.\n"
        )

        total_symbols = len(filtered)
        categories_count = sum(1 for s in filtered if s.kind in ("CATEGORY", "SUBCATEGORY"))
        functors_count = sum(1 for s in filtered if s.kind in ("FUNCTOR", "ADJUNCTION"))
        constructions_count = sum(1 for s in filtered if s.kind == "CONSTRUCTION")
        morphisms_count = sum(1 for s in filtered if s.kind in ("MORPHISM", "HOMSET"))
        objects_count = sum(1 for s in filtered if s.kind in ("OBJECT", "ELEMENT"))
        catalogue_count = sum(1 for s in filtered if s.kind in ("CATALOGUE", "REGISTRY"))
        functions_count = sum(1 for s in filtered if s.kind == "FUNCTION")

        lines.append("## Executive Summary\n")
        lines.append(f"- **Total Constructions**: {total_symbols}")
        lines.append(f"- **Categories & Subcategories**: {categories_count}")
        lines.append(f"- **Functors & Adjunctions**: {functors_count}")
        lines.append(f"- **Universal Categorical Constructions**: {constructions_count}")
        lines.append(f"- **Morphisms & Hom-Sets**: {morphisms_count}")
        lines.append(f"- **Mathematical Objects & Elements**: {objects_count}")
        lines.append(f"- **Named Catalogues & Registries**: {catalogue_count}")
        lines.append(f"- **Factory Functions & Constructors**: {functions_count}\n")

        lines.append("## Table of Subsystems\n")
        lines.append("| Subsystem | Key Domains | Items |")
        lines.append("| :--- | :--- | :--- |")
        for key, title, desc in subsystems:
            sub_count = sum(1 for s in filtered if s.subsystem == key)
            if sub_count > 0:
                slug = key.replace("_", "-")
                lines.append(f"| [{title}](#subsystem-{slug}) | {desc} | **{sub_count}** |")
        lines.append("\n---\n")

        if summary_only:
            lines.append("## Complete Index of Public Constructions\n")
            lines.append("| Symbol | Kind | Subsystem | File Location | Summary |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            for s in sorted(filtered, key=lambda x: (x.subsystem, x.kind, x.name)):
                first = cls._first_sentence(s.doc)
                export_badge = "★" if s.is_exported_in_all else ""
                lines.append(f"| `{s.name}` {export_badge} | `{s.kind}` | `{s.subsystem}` | `{s.file_path}:{s.line_number}` | {first} |")
            return "\n".join(lines)

        for key, title, desc in subsystems:
            sub_symbols = [s for s in filtered if s.subsystem == key]
            if not sub_symbols:
                continue

            slug = key.replace("_", "-")
            lines.append(f"<a id=\"subsystem-{slug}\"></a>")
            lines.append(f"## {title}\n")
            lines.append(f"> {desc}\n")

            cats = [s for s in sub_symbols if s.kind in ("CATEGORY", "SUBCATEGORY")]
            if cats:
                lines.append("### 🏛 Categories & Subcategories\n")
                for s in sorted(cats, key=lambda x: x.name):
                    lines.extend(cls._render_category_symbol(s))

            functors = [s for s in sub_symbols if s.kind in ("FUNCTOR", "ADJUNCTION")]
            if functors:
                lines.append("### 🔄 Functors & Adjunctions\n")
                for s in sorted(functors, key=lambda x: x.name):
                    lines.extend(cls._render_functor_symbol(s))

            constructions = [s for s in sub_symbols if s.kind == "CONSTRUCTION"]
            if constructions:
                lines.append("### ⚙ Universal Categorical Constructions\n")
                for s in sorted(constructions, key=lambda x: x.name):
                    lines.extend(cls._render_construction_symbol(s))

            morphisms = [s for s in sub_symbols if s.kind in ("MORPHISM", "HOMSET")]
            if morphisms:
                lines.append("### ↗ Morphisms & Hom-Sets\n")
                for s in sorted(morphisms, key=lambda x: x.name):
                    lines.extend(cls._render_morphism_symbol(s))

            objects = [s for s in sub_symbols if s.kind in ("OBJECT", "ELEMENT")]
            if objects:
                lines.append("### 📦 Mathematical Objects & Parents\n")
                for s in sorted(objects, key=lambda x: x.name):
                    lines.extend(cls._render_object_symbol(s))

            catalogue = [s for s in sub_symbols if s.kind in ("CATALOGUE", "REGISTRY")]
            if catalogue:
                lines.append("### 📚 Catalogues & Named Tables\n")
                for s in sorted(catalogue, key=lambda x: x.name):
                    lines.extend(cls._render_catalogue_symbol(s))

            functions = [s for s in sub_symbols if s.kind == "FUNCTION"]
            if functions:
                lines.append("### 🛠 Helper Functions & Constructors\n")
                for s in sorted(functions, key=lambda x: x.name):
                    lines.extend(cls._render_function_symbol(s))

            lines.append("\n---\n")

        return "\n".join(lines)

    @classmethod
    def _render_category_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        kind_badge = f"`[{s.kind}]`"
        out.append(f"#### `{s.name}` {kind_badge} {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.bases:
            out.append(f"- **Bases**: `{'`, `'.join(s.bases)}`")
        if s.super_categories:
            out.append(f"- **Super Categories**: `{'`, `'.join(s.super_categories)}`")

        if s.doc:
            out.append(f"\n{s.doc}\n")

        if s.category_constructors:
            out.append("**Category Constructor:**")
            for c in s.category_constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- {dec}`{s.name}({c.args}){c.return_type}`")
                if c.doc:
                    out.append(f"  > {cls._first_sentence(c.doc)}")

        if s.object_constructors:
            out.append("\n**Object Constructor (Calling Category on Data):**")
            for c in s.object_constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- {dec}`{s.name}(...)({c.args}){c.return_type}`")
                if c.doc:
                    out.append(f"  > {cls._first_sentence(c.doc)}")

        if s.parent_methods:
            out.append("\n**ParentMethods (Methods on Category Objects):**")
            for m in sorted(s.parent_methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")

        if s.element_methods:
            out.append("\n**ElementMethods (Methods on Category Elements):**")
            for m in sorted(s.element_methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")

        if s.subcategory_methods:
            out.append("\n**SubcategoryMethods (Subcategory Refinements):**")
            for m in sorted(s.subcategory_methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")

        if s.methods:
            out.append("\n**Category Instance Methods:**")
            for m in sorted(s.methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")

        out.append("")
        return out

    @classmethod
    def _render_functor_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        kind_badge = f"`[{s.kind}]`"
        out.append(f"#### `{s.name}` {kind_badge} {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.bases:
            out.append(f"- **Bases**: `{'`, `'.join(s.bases)}`")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        if s.constructors:
            out.append("**Constructors / Factory Signatures:**")
            for c in s.constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- {dec}`def {c.name}({c.args}){c.return_type}`")
                if c.doc:
                    out.append(f"  > {cls._first_sentence(c.doc)}")
        if s.methods:
            out.append("\n**Functor / Adjunction Methods:**")
            for m in sorted(s.methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")
        out.append("")
        return out

    @classmethod
    def _render_construction_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        out.append(f"#### `{s.name}` `[CONSTRUCTION]` {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        if s.constructors:
            for c in s.constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- **Signature**: {dec}`def {c.name}({c.args}){c.return_type}`")
        out.append("")
        return out

    @classmethod
    def _render_morphism_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        out.append(f"#### `{s.name}` `[{s.kind}]` {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.bases:
            out.append(f"- **Bases**: `{'`, `'.join(s.bases)}`")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        if s.constructors:
            for c in s.constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- **Constructor**: {dec}`def {c.name}({c.args}){c.return_type}`")
        if s.methods:
            out.append("\n**Public Methods:**")
            for m in sorted(s.methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")
        out.append("")
        return out

    @classmethod
    def _render_object_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        out.append(f"#### `{s.name}` `[{s.kind}]` {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.bases:
            out.append(f"- **Bases**: `{'`, `'.join(s.bases)}`")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        if s.constructors:
            for c in s.constructors:
                dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
                out.append(f"- **Constructor**: {dec}`def {c.name}({c.args}){c.return_type}`")
        if s.methods:
            out.append("\n**Public Methods:**")
            for m in sorted(s.methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")
        out.append("")
        return out

    @classmethod
    def _render_catalogue_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        out.append(f"#### `{s.name}` `[{s.kind}]` {export_badge}\n")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        if s.class_vars:
            out.append("**Catalogue Entries / Constants:**")
            for var_name, var_val in s.class_vars:
                out.append(f"- `{var_name}`: `{var_val}`")
        if s.methods:
            out.append("\n**Methods / Registry Functions:**")
            for m in sorted(s.methods, key=lambda x: x.name):
                dec = f"`@{', @'.join(m.decorators)}` " if m.decorators else ""
                out.append(f"- {dec}`{m.name}({m.args}){m.return_type}`")
                if m.doc:
                    out.append(f"  > {cls._first_sentence(m.doc)}")
        out.append("")
        return out

    @classmethod
    def _render_function_symbol(cls, s: SymbolDoc) -> list[str]:
        out: list[str] = []
        export_badge = "`[Exported Session]`" if s.is_exported_in_all else "`[Internal]`"
        c = s.constructors[0] if s.constructors else MethodDoc(name=s.name, args="", return_type="", doc="")
        dec = f"`@{', @'.join(c.decorators)}` " if c.decorators else ""
        out.append(f"#### `{s.name}` `[FUNCTION]` {export_badge}\n")
        out.append(f"- **Signature**: {dec}`def {s.name}({c.args}){c.return_type}`")
        out.append(f"- **Source**: [`src/dzack_research/preamble/{s.file_path}#L{s.line_number}`](file:///home/dzack/research/src/dzack_research/preamble/{s.file_path}#L{s.line_number})")
        if s.doc:
            out.append(f"\n{s.doc}\n")
        out.append("")
        return out

    @classmethod
    def render_text(
        cls,
        symbols: list[SymbolDoc],
        subsystem_filter: str | None = None,
        kind_filter: str | None = None,
        search_query: str | None = None,
        session_only: bool = False,
    ) -> str:
        filtered = cls._filter_symbols(symbols, subsystem_filter, kind_filter, search_query, session_only)
        subsystems = cls._get_subsystem_sequence(filtered)
        lines: list[str] = []
        lines.append("=" * 80)
        lines.append(f"PREAMBLE MATHEMATICAL CONSTRUCTIONS ({len(filtered)} items)")
        lines.append("=" * 80)

        for key, title, _ in subsystems:
            sub_symbols = [s for s in filtered if s.subsystem == key]
            if not sub_symbols:
                continue
            lines.append(f"\n[{title.upper()}] ({len(sub_symbols)} items)")
            lines.append("-" * 80)
            for s in sorted(sub_symbols, key=lambda x: (x.kind, x.name)):
                exp = "*" if s.is_exported_in_all else " "
                first = cls._first_sentence(s.doc)
                lines.append(f"{exp} [{s.kind:12}] {s.name:<32} {s.file_path}:{s.line_number}")
                if first:
                    lines.append(f"     {first}")
                if s.parent_methods:
                    pm_names = ", ".join(m.name for m in s.parent_methods[:6])
                    if len(s.parent_methods) > 6:
                        pm_names += f", ... (+{len(s.parent_methods)-6} more)"
                    lines.append(f"     ParentMethods: {pm_names}")
                if s.element_methods:
                    em_names = ", ".join(m.name for m in s.element_methods[:6])
                    if len(s.element_methods) > 6:
                        em_names += f", ... (+{len(s.element_methods)-6} more)"
                    lines.append(f"     ElementMethods: {em_names}")
        return "\n".join(lines)

    @classmethod
    def render_json(
        cls,
        symbols: list[SymbolDoc],
        subsystem_filter: str | None = None,
        kind_filter: str | None = None,
        search_query: str | None = None,
        session_only: bool = False,
    ) -> str:
        filtered = cls._filter_symbols(symbols, subsystem_filter, kind_filter, search_query, session_only)
        raw_list = [asdict(s) for s in filtered]
        return json.dumps(raw_list, indent=2)

    @staticmethod
    def _filter_symbols(
        symbols: list[SymbolDoc],
        subsystem_filter: str | None = None,
        kind_filter: str | None = None,
        search_query: str | None = None,
        session_only: bool = False,
    ) -> list[SymbolDoc]:
        res = symbols
        if subsystem_filter:
            sub = subsystem_filter.lower().strip()
            # If subsystem_filter matches a known subsystem key prefix or name exactly
            matched_subsystems = [k for k, _, _ in SUBSYSTEM_ORDER if sub == k or sub in k]
            if matched_subsystems:
                res = [s for s in res if s.subsystem in matched_subsystems]
            else:
                res = [s for s in res if sub in s.subsystem.lower() or sub in s.file_path.lower()]
        if kind_filter:
            kd = kind_filter.upper().strip()
            res = [s for s in res if kd in s.kind]
        if search_query:
            sq = search_query.lower().strip()
            res = [
                s
                for s in res
                if sq in s.name.lower()
                or sq in s.doc.lower()
                or any(sq in m.name.lower() or sq in m.doc.lower() for m in s.methods)
                or any(sq in m.name.lower() or sq in m.doc.lower() for m in s.parent_methods)
                or any(sq in m.name.lower() or sq in m.doc.lower() for m in s.element_methods)
            ]
        if session_only:
            res = [s for s in res if s.is_exported_in_all]
        return res


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Surface a programmatic megadoc of all reusable constructions in the preamble."
    )
    parser.add_argument(
        "subsystem",
        nargs="?",
        default=None,
        help="Subsystem filter (e.g. lattices, functors, algebras, modules, categories, group, schemes, catalogue).",
    )
    parser.add_argument(
        "-k",
        "--kind",
        default=None,
        help="Filter by kind (category, subcategory, functor, adjunction, construction, morphism, homset, object, element, catalogue, function).",
    )
    parser.add_argument(
        "-s",
        "--search",
        default=None,
        help="Search query matching symbol names, docstrings, or method names.",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=["markdown", "text", "json", "md", "txt"],
        default="markdown",
        help="Output format (markdown, text, json). Default: markdown.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Write output to specified file path instead of stdout.",
    )
    parser.add_argument(
        "--toc",
        "--summary",
        action="store_true",
        dest="summary",
        help="Display only the executive summary and index table.",
    )
    parser.add_argument(
        "--session-only",
        action="store_true",
        help="Include only symbols exported into the session via preamble.all.",
    )

    args = parser.parse_args()

    extractor = PreambleExtractor()
    symbols = extractor.extract_all()

    fmt = args.format
    if fmt == "md":
        fmt = "markdown"
    elif fmt == "txt":
        fmt = "text"

    if fmt == "markdown":
        output = PreambleRenderer.render_markdown(
            symbols,
            subsystem_filter=args.subsystem,
            kind_filter=args.kind,
            search_query=args.search,
            session_only=args.session_only,
            summary_only=args.summary,
        )
    elif fmt == "text":
        output = PreambleRenderer.render_text(
            symbols,
            subsystem_filter=args.subsystem,
            kind_filter=args.kind,
            search_query=args.search,
            session_only=args.session_only,
        )
    elif fmt == "json":
        output = PreambleRenderer.render_json(
            symbols,
            subsystem_filter=args.subsystem,
            kind_filter=args.kind,
            search_query=args.search,
            session_only=args.session_only,
        )
    else:
        output = ""

    try:
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Preamble megadoc written to {out_path} ({len(output)} bytes)")
        else:
            sys.stdout.write(output)
            sys.stdout.flush()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
