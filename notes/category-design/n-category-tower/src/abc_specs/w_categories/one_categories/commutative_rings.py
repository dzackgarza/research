# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/one_categories/commutative_rings.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Commutative Ring ABCs.

Specialization of Ring ABCs for commutative rings.

Defines:
1. _CommutativeRingsCategory_ABC: The Category of Commutative Rings.
2. _CommutativeRingObject_ABC: A Commutative Ring R.
3. _CommutativeRingElement_ABC: An element r ∈ R.

Per docs/categories_to_implement.md §Rings.
"""

from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs

class Monoid(ABC): ...

class _CommutativeRingsCategory_ABC(CategoryABCs.RingsCategory, ABC):
    """
    The Category of Commutative Rings (CRing).

    - Objects: Commutative rings.
    - Morphisms: Ring homomorphisms.
    - Structure: Complete, Cocomplete.
    """

    # Inherits forgetful functors from RingsCategory
    pass


class _CommutativeRingObject_ABC(CategoryABCs.RingObject, ABC):
    """
    A Commutative Ring R.

    Specializes RingObject with methods specific to commutative rings.
    """

    # === Fraction field (for integral domains) ===

    @final
    @abstractmethod
    def fraction_field(self) -> CategoryABCs.CommutativeRingObject:
        """Frac(R) (requires R to be an integral domain)."""
        ...

    # === Spectrum ===

    @final
    @abstractmethod
    def spectrum(self) -> Any:
        """Spec(R) - the prime spectrum."""
        ...

    @final
    @abstractmethod
    def max_spectrum(self) -> Any:
        """MaxSpec(R) - the maximal spectrum."""
        ...

    @final
    @abstractmethod
    def nilradical(self) -> CategoryABCs.Ideal:
        """nil(R) = √(0) (intersection of all prime ideals)."""
        ...

    @final
    @abstractmethod
    def jacobson_radical(self) -> CategoryABCs.Ideal:
        """J(R) (intersection of all maximal ideals)."""
        ...

    # === Additional predicates for commutative rings ===

    @final
    @abstractmethod
    def is_dedekind_domain(self) -> BoolProof:
        """Check if R is a Dedekind domain."""
        ...

    @final
    @abstractmethod
    def is_regular(self) -> BoolProof:
        """Check if R is a regular ring."""
        ...

    @final
    @abstractmethod
    def is_normal(self) -> BoolProof:
        """Check if R is integrally closed in its field of fractions."""
        ...

    @final
    @abstractmethod
    def is_cohen_macaulay(self) -> BoolProof:
        """Check if R is Cohen-Macaulay."""
        ...

    @final
    @abstractmethod
    def is_gorenstein(self) -> BoolProof:
        """Check if R is Gorenstein."""
        ...

    # === Completions ===

    @final
    @abstractmethod
    def completion_at(
        self, ideal: CategoryABCs.Ideal
    ) -> CategoryABCs.CommutativeRingObject:
        """R̂_I (I-adic completion)."""
        ...

    @final
    @abstractmethod
    def localization_at(
        self, S: Monoid
    ) -> CategoryABCs.CommutativeRingObject:
        """R[S^{-1}], the localization of R at a submonoid S of (R, +)."""
        ...

    # === Integral extensions ===

    @final
    @abstractmethod
    def integral_closure_in(
        self, field: CategoryABCs.CommutativeRingObject
    ) -> CategoryABCs.CommutativeRingObject:
        """Integral closure of R in a field extension."""
        ...


class _CommutativeRingElement_ABC(CategoryABCs.RingElement, ABC):
    """
    An element r ∈ R for commutative R.

    Multiplication is commutative: rs = sr.
    Inherits from CategoryABCs.RingElement which inherits from CategoryABCs.Element.
    """

    @final
    @abstractmethod
    def parent_ring(self) -> CategoryABCs.CommutativeRingObject:
        """Alias for parent_object() - return the commutative ring R containing this element."""
        ...

    @final
    @abstractmethod
    def irreducible_factorization(
        self,
    ) -> list[tuple[CategoryABCs.CommutativeRingElement, int]]:
        """Factor r into irreducibles (if R is a UFD). Returns [(p_i, e_i)]."""
        ...

    @final
    @abstractmethod
    def prime_factorization(
        self,
    ) -> list[tuple[CategoryABCs.CommutativeRingElement, int]]:
        """Factor r into primes (if R is a UFD). Returns [(p_i, e_i)]."""
        ...

    @final
    @abstractmethod
    def gcd(
        self, other: CategoryABCs.CommutativeRingElement
    ) -> CategoryABCs.CommutativeRingElement:
        """gcd(r, s) (if R is a GCD domain)."""
        ...

    @final
    @abstractmethod
    def lcm(
        self, other: CategoryABCs.CommutativeRingElement
    ) -> CategoryABCs.CommutativeRingElement:
        """lcm(r, s) (if R is a GCD domain)."""
        ...

    @final
    @abstractmethod
    def is_irreducible(self) -> BoolProof:
        """Check if r is irreducible."""
        ...

    @final
    @abstractmethod
    def is_prime_element(self) -> BoolProof:
        """Check if r is a prime element."""
        ...

    @final
    @abstractmethod
    def to_principal_ideal(self) -> CategoryABCs.Ideal:
        """The principal ideal generated by r."""
        ...

    @final
    @abstractmethod
    def to_submodule(self) -> CategoryABCs.ModuleObject:
        """The submodule of R generated by r."""
        ...


# Expose for registration
_ = _CommutativeRingsCategory_ABC
_ = _CommutativeRingObject_ABC
_ = _CommutativeRingElement_ABC
