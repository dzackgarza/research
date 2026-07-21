"""Register every axiom name introduced by the category parent graph."""

from __future__ import annotations

from sage.categories.category_with_axiom import all_axioms

from .dot_parse import parse_dot

# Sage already owns many of these; add only those missing.
_GRAPH_AXIOMS: frozenset[str] = frozenset(
    {
        # Sets
        "Countable",
        "Uncountable",
        "Graded",
        # Magmas (Additive/Multiplicative are stub-owned; Associative/… are Sage's)
        "Additive",
        "Multiplicative",
        "FinitelyGenerated",
        # Algebras
        "Differential",
        # Modules
        "Free",
        "Projective",
        "WithBasis",
        "WithGenerators",
        "FiniteRank",
        "FinitelyPresented",
        "Torsion",
        "TorsionFree",
        "OverField",
        # Rings / domains
        "Domain",
        "IntegralDomain",
        "GCDDomain",
        "UFD",
        "PID",
        "Euclidean",
        "Noetherian",
        # Forms (∫Hom)
        "Nondegenerate",
        "Even",
        "Odd",
        "Unimodular",
        "Symmetric",
        "SkewSymmetric",
        "Alternating",
        # Lattices
        "Definite",
        "PositiveDefinite",
        "NegativeDefinite",
        "Indefinite",
        "Hyperbolic",
        # CatObject (nested-cat + (co)limit axioms)
        "LocallySmall",
        "Thin",
        "Monoidal",
        "Limits",
        "Colimits",
        "Products",
        "Coproducts",
        # Spaces / manifolds
        "PL",
        # Graphs
        "Directed",
        # Schemes
        "Affine",
        "Separated",
        "Proper",
        "Smooth",
        "Unramified",
        "Etale",
        "Flat",
        "Projective",
        "LocallyFinitePresentation",
        "Integral",
        "FiniteType",
        # Parameterized: RelativeDimension(n); instances RelativeDimension_1, …
        "RelativeDimension",
    }
)


def _axiom_name_from_dot_label(label: str) -> str:
    from .slugs import axiom_method_name

    return axiom_method_name(label)


def register_graph_axioms() -> frozenset[str]:
    """Idempotently add graph axioms to Sage's global registry."""
    from .slugs import axiom_method_name

    graph = parse_dot()
    names = set(_GRAPH_AXIOMS)
    for _node_id, label in graph.axiom_labels.items():
        names.add(_axiom_name_from_dot_label(label))
    for _join, (_host, path) in graph.named_joins.items():
        for axiom in path:
            names.add(axiom_method_name(axiom))
    for name in sorted(names):
        if name not in all_axioms:
            all_axioms.add(name)
    return frozenset(names)


register_graph_axioms()
