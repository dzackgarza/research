r"""Centralized axiom registration for the category spec redesign.

This file registers each project axiom name exactly once.  Axioms that express
the same mathematical restriction across several categories live in
``SHARED_AXIOMS``; category-specific groups contain only names whose meaning is
specific to that category family.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


# ---------------------------------------------------------------------------
# Shared Axioms
# ---------------------------------------------------------------------------

SHARED_AXIOMS = (
    "Commutative",
    "Finite",
    "FiniteDimensional",
    "Semisimple",
    "Topological",
    "WithBasis",
)


# ---------------------------------------------------------------------------
# Sets Axioms
# ---------------------------------------------------------------------------

SET_AXIOMS = (
    "Countable",
    "Uncountable",
    "Infinite",
    "Facade",
    "TotallyOrdered",
    "Graded",
    "Metric",
)


# ---------------------------------------------------------------------------
# Rings Axioms
# ---------------------------------------------------------------------------

RING_AXIOMS = (
    "Division",
    "WithValuation",
    "Characteristic",
    "Polynomial",
    "PowerSeries",
    "LaurentSeries",
    "PuiseuxSeries",
    "Field",
    "IntegralDomains",
    "Noetherian",
    "Local",
    "KrullDimension",
    "Reduced",
    "Gcd",
    "UniqueFactorization",
    "PrincipalIdeal",
    "Euclidean",
    "IntegrallyClosed",
    "Dedekind",
    "DiscretelyValued",
    "Complete",
    "NumberFields",
    "AlgebraicallyClosed",
    "LocalFields",
    "GlobalFields",
    "Archimedean",
    "NonArchimedean",
    "QuadraticNumberField",
    "Cyclotomic",
)


# ---------------------------------------------------------------------------
# Modules Axioms
# ---------------------------------------------------------------------------

MODULE_AXIOMS = (
    "OverIntegralDomain",
    "OverDedekindDomain",
    "OverPID",
    "OverCommutativeRing",
    "OverField",
    "OverLocalRing",
    "OverCompleteRing",
    "Free",
    "FiniteRank",
    "Torsion",
    "Torsionfree",
    "Projective",
    "WithOrderedBasis",
    "WithOrderedGeneratingSet",
    "FinitelyGenerated",
    "FinitelyPresented",
    "RIdeals",
    "WithForms",
    "Bilinear",
    "Quadratic",
    "Symmetric",
    "Alternating",
    "Nondegenerate",
    "Indefinite",
    "Definite",
    "Integral",
    "Rational",
)


# ---------------------------------------------------------------------------
# Lattice Axioms
# ---------------------------------------------------------------------------

LATTICE_AXIOMS = (
    "Lattice",
    "OverIntegers",
    "Even",
    "Unimodular",
)


# ---------------------------------------------------------------------------
# Sage Hom Axiom Hooks
# ---------------------------------------------------------------------------

HOMSET_AXIOMS = (
    "Endset",
    "Autset",
)


# ---------------------------------------------------------------------------
# Registration Logic
# ---------------------------------------------------------------------------

ALL_AXIOMS = SHARED_AXIOMS + SET_AXIOMS + RING_AXIOMS + MODULE_AXIOMS + LATTICE_AXIOMS + HOMSET_AXIOMS


def register_axioms(axioms: Iterable[str]) -> None:
    r"""Register a collection of custom axioms into Sage's category system."""
    from sage.categories import category_with_axiom as _category_with_axiom

    missing = tuple(axiom for axiom in axioms if axiom not in _category_with_axiom.all_axioms)
    if missing:
        _category_with_axiom.all_axioms += missing


def register_all() -> None:
    r"""Register ALL project-specific custom axioms."""
    register_axioms(ALL_AXIOMS)
