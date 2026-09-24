"""Lazy public aggregation for mathematical nouns used by the preamble.

The lexicon's defining modules must remain independently importable. Python
executes a package ``__init__`` before any submodule, so eager re-exports here
pull category-owning modules into dependency-light type imports and create
artificial import cycles. Public names are resolved lazily instead.
"""

from importlib import import_module as _import_module


_EXPORTS = {
    "AlgebraHomomorphism": ("dzack_research.preamble.lexicon.algebra", "AlgebraHomomorphism"),
    "BaseRing": ("dzack_research.preamble.lexicon.algebra", "BaseRing"),
    "Element": ("dzack_research.preamble.lexicon.algebra", "Element"),
    "Matrix": ("dzack_research.preamble.lexicon.algebra", "Matrix"),
    "ModuleElement": ("dzack_research.preamble.lexicon.algebra", "ModuleElement"),
    "MonoidObject": ("dzack_research.preamble.lexicon.algebra", "MonoidObject"),
    "RingElement": ("dzack_research.preamble.lexicon.algebra", "RingElement"),
    "ElementOfCategoryObject": (
        "dzack_research.preamble.lexicon.category_theory",
        "ElementOfCategoryObject",
    ),
    "ObjectOfCategory": ("dzack_research.preamble.lexicon.category_theory", "ObjectOfCategory"),
    "CartanType": ("dzack_research.preamble.lexicon.foundations", "CartanType"),
    "GramMatrix": ("dzack_research.preamble.lexicon.foundations", "GramMatrix"),
    "Integer": ("dzack_research.preamble.lexicon.foundations", "Integer"),
    "LatticeName": ("dzack_research.preamble.lexicon.foundations", "LatticeName"),
    "MatrixData": ("dzack_research.preamble.lexicon.foundations", "MatrixData"),
    "OrderedSet": ("dzack_research.preamble.lexicon.foundations", "OrderedSet"),
    "Rational": ("dzack_research.preamble.lexicon.foundations", "Rational"),
    "RealApproximation": ("dzack_research.preamble.lexicon.foundations", "RealApproximation"),
    "RealNumber": ("dzack_research.preamble.lexicon.foundations", "RealNumber"),
    "SignaturePair": ("dzack_research.preamble.lexicon.foundations", "SignaturePair"),
    "SymbolicExpression": ("dzack_research.preamble.lexicon.foundations", "SymbolicExpression"),
    "CoxeterMatrix": ("dzack_research.preamble.lexicon.geometry", "CoxeterMatrix"),
    "Graph": ("dzack_research.preamble.lexicon.geometry", "Graph"),
    "Polyhedron": ("dzack_research.preamble.lexicon.geometry", "Polyhedron"),
    "SageCategory": ("dzack_research.preamble.lexicon.interop", "SageCategory"),
    "SageElement": ("dzack_research.preamble.lexicon.interop", "SageElement"),
    "SageMorphism": ("dzack_research.preamble.lexicon.interop", "SageMorphism"),
    "SageParent": ("dzack_research.preamble.lexicon.interop", "SageParent"),
    "SageUniqueRepresentation": (
        "dzack_research.preamble.lexicon.interop",
        "SageUniqueRepresentation",
    ),
    "SetObject": ("dzack_research.preamble.lexicon.set_theory", "SetObject"),
}

__all__ = [
    "AlgebraHomomorphism",
    "BaseRing",
    "CartanType",
    "CoxeterMatrix",
    "Element",
    "ElementOfCategoryObject",
    "GramMatrix",
    "Graph",
    "Integer",
    "LatticeName",
    "Matrix",
    "MatrixData",
    "ModuleElement",
    "MonoidObject",
    "OrderedSet",
    "ObjectOfCategory",
    "Polyhedron",
    "Rational",
    "RealApproximation",
    "RealNumber",
    "RingElement",
    "SageCategory",
    "SageElement",
    "SageMorphism",
    "SageParent",
    "SageUniqueRepresentation",
    "SetObject",
    "SignaturePair",
    "SymbolicExpression",
]


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(name)
    module_name, attribute = _EXPORTS[name]
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value


def __dir__():
    return sorted((*globals(), *__all__))
