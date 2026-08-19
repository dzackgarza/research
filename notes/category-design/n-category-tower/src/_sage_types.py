# Origin: gitclones/integral_lattice/cat/src/_sage_types.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations
from src.local_typing import *


@dataclass
class InfinitePowerset:
    """
    Wrapper for the powerset of an infinite set.

    Sage's Subsets doesn't handle infinite sets properly (e.g., Subsets(NN).cardinality()
    tries to compute 1 << Infinity which fails). This wrapper provides correct cardinality
    for infinite powersets: |P(S)| = 2^|S|, which is uncountably infinite when |S| = ℵ₀.
    """

    base_set: Any

    def cardinality(self) -> "SageType.PlusInfinity":
        """The powerset of any infinite set is uncountably infinite."""
        return SageType.Infinity

    def is_finite(self) -> bool:
        return False

    def __contains__(self, x: Any) -> bool:
        """Checks if a set x is a subset of the base_set."""
        # For an infinite powerset, x is contained if all its elements are in the base_set
        if hasattr(x, "is_subset"):
            return x.is_subset(self.base_set)
        return all(elem in self.base_set for elem in x)

    def __iter__(self) -> Iterator[Any]:
        """Iterates over the elements of the infinite powerset. This will be an infinite iterator."""
        yield from SageType.powerset(self.base_set)

    def an_element(self) -> Any:
        """Returns an arbitrary element from the infinite powerset (the empty set)."""
        return self.base_set.empty_set()

    def first(self) -> Any:
        """Returns the first element of the infinite powerset (the empty set)."""
        return self.base_set.empty_set()

    def last(self) -> Any:
        """Returns the last element of the infinite powerset (the base set itself)."""
        return self.base_set


class SageType:
    """
    Namespace for Sage type aliases.
    """

    # Internal imports - exception to "no internal imports" rule
    from sage.all import NN, MatrixSpace as MatrixRing, NumberFields, NumberField, PolynomialRing, Permutation, Rings, Sets, AA, CC, QQ, RR, ZZ, Primes as SagePrimes, QQbar, CyclotomicField, GF, Qp, Zp, Subsets as SageSubsets, powerset, Rngs, Semirings, Semigroups
    from sage.groups.matrix_gps.linear import GL


    Primes = SagePrimes(modulus=1, classes=[1], exceptions={})
    from sage.structure.richcmp import op_EQ, op_GE, op_GT, op_LE, op_LT, op_NE
    from sage.combinat.subset import Subsets_s
    from sage.rings.infinity import PlusInfinity
    from sage.rings.number_field.number_field_base import (  
        NumberField as NumberField_class,  
    )
    from sage.rings.padics.padic_base_generic import pAdicBaseGeneric as pAdicRing
    # from sage.rings.polynomial.multi_polynomial_ring import (
    #     MPolynomialRing_base as MPolynomialRing,  
    # )
    from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing
    from sage.rings.polynomial.polynomial_ring import (
        PolynomialRing_general as PolynomialRing_class,
    )
    from sage.rings.power_series_ring import PowerSeriesRing_generic as PowerSeriesRing
    from sage.rings.ring import Ring  
    from sage.structure.element import Matrix  
    from sage.structure.parent import Set_generic as Set 
    from sage.symbolic.expression import Expression as SymbolicExpression 

    from sage.libs.gap.element import GapElement

    # Type aliases


    Powerset = Subsets_s | InfinitePowerset
    NaturalNumber = NonNegativeInt
    NN_U_infty = NaturalNumber | PlusInfinity

    SetsCat = Sets()
    RingsCat = Rings() # type: ignore
    # Sage does some complex runtime magic to make Rings() a category with axioms

    # Constants
    Infinity: PlusInfinity = PlusInfinity()

    from sage.graphs.digraph import DiGraph

    from sage.monoids.monoid import Monoid_class as Monoid
    from sage.groups.group import Group
    from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic as MatrixGroup


    @staticmethod
    def Mat(R: Ring, n: NaturalNumber, m: NaturalNumber) -> MatrixRing:
        return SageType.MatrixRing(R, n, m, sparse=False, implementation=None)


    @staticmethod
    def Subsets(s: Any) -> SageType.Subsets_s | InfinitePowerset: 
        """
        Wrapper around sage's Subsets that handles infinite sets correctly.

        For finite sets, defers to sage's Subsets.
        For infinite sets, returns an InfinitePowerset with correct cardinality.
        """
        if hasattr(s, "cardinality") and s.cardinality() >= SageType.Infinity:
            return InfinitePowerset(base_set=s)
        result: SageType.Subsets_s = SageType.SageSubsets(s)
        return result

# =============================================================================
# Type Guards — Organized by namespace
# =============================================================================

class SageTypeChecks:
    """Type guards for Sage types."""

    @runtime_checkable
    class HasCardinality(Protocol):
        """Protocol for objects with a cardinality method."""

        def cardinality(self) -> int: ...


    @runtime_checkable
    class HasDegree(Protocol):
        """Protocol for objects with a degree method (e.g., number fields)."""

        def degree(self) -> int: ...


    @runtime_checkable
    class HasBaseRing(Protocol):
        """Protocol for rings with a base_ring method."""

        def base_ring(self) -> object: ...
    
    @runtime_checkable
    class HasOrder(Protocol):
        """Protocol for objects with an order method (e.g., groups, graphs)."""
        
        def order(self) -> int: ...

    @staticmethod
    def is_natural_number(r: Any) -> TypeIs[SageType.NaturalNumber]:
        """Check if r is a natural number (non-negative integer)."""
        return r in SageType.NN

    @staticmethod
    def has_cardinality(r: Any) -> TypeIs[HasCardinality]:
        """Check if object has a cardinality method."""
        return hasattr(r, "cardinality")

    @staticmethod
    def has_degree(r: Any) -> TypeIs[HasDegree]:
        """Check if object has a degree method."""
        return hasattr(r, "degree")

    @staticmethod
    def has_base_ring(r: Any) -> TypeIs[HasBaseRing]:
        """Check if object has a base_ring method."""
        return hasattr(r, "base_ring")

    @staticmethod
    def has_order(r: Any) -> TypeIs[HasOrder]:
        """Check if object has an order method."""
        return hasattr(r, "order")

    @staticmethod
    def is_natural_number_or_infinity(r: Any) -> TypeIs[SageType.NN_U_infty]:
        """Check if r is a natural number or infinity."""
        return SageTypeChecks.is_natural_number(r) or r == SageType.Infinity

    @staticmethod
    def is_set(r: Any) -> TypeIs[SageType.Set]:
        """Check if r is a Sage Set."""
        return r in SageType.SetsCat

    @staticmethod
    def is_power_set(r: Any) -> TypeIs[SageType.Powerset]:
        """Check if r is a powerset."""
        return isinstance(r, (SageType.Subsets_s, InfinitePowerset))

    @staticmethod
    def is_ring(r: Any) -> TypeIs[SageType.Ring]:
        """Check if r is a Sage Ring."""
        return r in SageType.RingsCat

    @staticmethod
    def is_padic_ring(r: Any) -> TypeIs[SageType.pAdicRing]:
        """Check if r is a p-adic ring."""
        return isinstance(r, SageType.pAdicRing)

    @staticmethod
    def is_number_field(r: Any) -> TypeIs[SageType.NumberField_class]:
        """Check if r is a number field."""
        return r in SageType.NumberFields()

    @staticmethod
    def is_polynomial_ring(r: Any) -> TypeIs[SageType.PolynomialRing_class]:
        """Check if r is a univariate polynomial ring."""
        return isinstance(r, SageType.PolynomialRing_class)

    @staticmethod
    def is_multivariate_polynomial_ring(r: Any) -> TypeIs[SageType.MPolynomialRing]:  
        """Check if r is a multivariate polynomial ring."""
        return isinstance(r, SageType.MPolynomialRing)

    @staticmethod
    def is_power_series_ring(r: Any) -> TypeIs[SageType.PowerSeriesRing]:
        """Check if r is a power series ring."""
        return isinstance(r, SageType.PowerSeriesRing)

    @staticmethod
    def is_matrix_ring(r: Any) -> TypeIs[SageType.MatrixRing]:
        """Check if r is a matrix ring (MatrixSpace)."""
        return isinstance(r, SageType.MatrixRing)

    @staticmethod
    def is_matrix(r: Any) -> TypeIs[SageType.Matrix]:
        """Check if r is a Sage matrix."""
        return isinstance(r, SageType.Matrix)
    
    @staticmethod
    def is_matrix_group(r: Any) -> TypeIs[SageType.MatrixGroup]:
        """Check if r is a Sage Matrix Group."""
        return isinstance(r, SageType.MatrixGroup)

    @staticmethod
    def is_symbolic_expression(x: Any) -> TypeIs[SageType.SymbolicExpression]:
        """Check if x is a Sage symbolic expression."""
        return isinstance(x, SageType.SymbolicExpression)

    @staticmethod
    def is_iterable(x: Any) -> TypeIs[Iterable[Any]]:
        """Check if x is iterable."""
        return isinstance(x, Iterable)