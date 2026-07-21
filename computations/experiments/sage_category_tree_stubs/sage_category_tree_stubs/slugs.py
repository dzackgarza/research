"""Map DOT node ids to valid Python class names."""

from __future__ import annotations

import re

_SLUG_OVERRIDES: dict[str, str] = {
    "CatObject": "CatObject",
    "Cat": "Cat_1",
    "Cat_1": "Cat_1",
    "Cat_2": "Cat_2",
    "(2,1)-Categories": "TwoOneCategories",
    "CatObject.Thin": "CatObject_Thin",
    "TensorProducts = CatObject.Monoidal": "TensorProducts",
    "Arr(−)": "ArrowCategories",
    "(−)^op": "OppositeCategories",
    "G-Objects": "GObjects",
    "G-Objects(G)": "GObjects",
    "Mod(O_X)": "ModOX",
    "Coh(X)": "CohX",
    "QCoh(X)": "QCohX",
    "C∞Algebras": "CInfinityAlgebras",
    "Modules(R)": "Modules",
    "LeftModules(R)": "LeftModules",
    "RightModules(R)": "RightModules",
    "Bimodules(R)": "Bimodules",
    "Algebras(R)": "Algebras",
    "LieAlgebras(R)": "LieAlgebras",
    "Coalgebras(R)": "Coalgebras",
    "Bialgebras(R)": "Bialgebras",
    "HopfAlgebras(R)": "HopfAlgebras",
    "CliffordAlgebras(R)": "CliffordAlgebras",
    "SymmetricAlgebras(R)": "SymmetricAlgebras",
    "ExteriorAlgebras(R)": "ExteriorAlgebras",
    "TensorAlgebras(R)": "TensorAlgebras",
    "C∞Algebras(R)": "CInfinityAlgebras",
    "VectorSpaces(K)": "VectorSpaces",
    "VectorSpaces(K) = Modules.OverField": "VectorSpaces",
    "DivisionRings = Magmas.Inverse": "DivisionRings",
    "Schemes(S)": "Schemes",
    "Varieties(K)": "Varieties",
    "Curves(K)": "Curves",
    "Surfaces(K)": "Surfaces",
    "Hypersurfaces(K)": "Hypersurfaces",
    "CompleteIntersections(K)": "CompleteIntersections",
    "ToricVarieties(K)": "ToricVarieties",
    "ChainComplexes(C)": "ChainComplexes",
    "CochainComplexes(C)": "CochainComplexes",
    "∫Hom_R(−,W)": "HomForms",
    "∫Bil_R(W)": "BilForms",
    "∫Quad_R(W)": "QuadForms",
    "∫Herm_R(W)": "HermForms",
}


def short_name(node: str) -> str:
    """``Groups = Magmas.…`` → ``Groups``; otherwise the node id."""
    if " = " in node:
        return node.split(" = ", 1)[0]
    return node


def class_slug(node: str) -> str:
    base = short_name(node)
    if base in _SLUG_OVERRIDES:
        return _SLUG_OVERRIDES[base]
    if node in _SLUG_OVERRIDES:
        return _SLUG_OVERRIDES[node]
    # sanitize
    out = []
    for ch in base:
        if ch.isalnum() or ch == "_":
            out.append(ch)
        elif ch in "∞":
            out.append("Infinity")
        elif ch in "−-":
            out.append("_")
    slug = "".join(out)
    if slug and slug[0].isdigit():
        slug = "N" + slug
    return slug or "CategoryNode"


def axiom_method_name(label: str) -> str:
    """DOT axiom label → Sage ``CategoryWithAxiom`` attribute name.

    Parameterized axioms ``Foo(arg)`` become ``Foo_arg``; a schematic parameter
    ``Foo(n)`` (or ``Foo(−)``) collapses to the family name ``Foo``.
    """
    if label == "Étale":
        return "Etale"
    match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)", label)
    if match:
        name, arg = match.group(1), match.group(2).strip()
        if arg in {"n", "−", "-", "…", "..."}:
            return name
        safe = re.sub(r"[^A-Za-z0-9_]+", "_", arg)
        return f"{name}_{safe}"
    return label


def is_parameterized_axiom_label(label: str) -> bool:
    """True for ``RelativeDimension(n)``, ``RelativeDimension(1)``, …"""
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*\([^)]+\)", label))


_PARAMETERIZED: frozenset[str] = frozenset(
    {
        "Modules(R)",
        "LeftModules(R)",
        "RightModules(R)",
        "Bimodules(R)",
        "Algebras(R)",
        "LieAlgebras(R)",
        "Coalgebras(R)",
        "Bialgebras(R)",
        "HopfAlgebras(R)",
        "CliffordAlgebras(R)",
        "SymmetricAlgebras(R)",
        "ExteriorAlgebras(R)",
        "TensorAlgebras(R)",
        "C∞Algebras(R)",
        "G-Objects(G)",
        "VectorSpaces(K)",
        "VectorSpaces(K) = Modules.OverField",
        "Schemes(S)",
        "Varieties(K)",
        "Curves(K)",
        "Surfaces(K)",
        "Hypersurfaces(K)",
        "CompleteIntersections(K)",
        "ToricVarieties(K)",
        "∫Hom_R(−,W)",
        "∫Bil_R(W)",
        "∫Quad_R(W)",
        "∫Herm_R(W)",
    }
)


def is_parameterized(node: str) -> bool:
    return short_name(node) in _PARAMETERIZED or node in _PARAMETERIZED
