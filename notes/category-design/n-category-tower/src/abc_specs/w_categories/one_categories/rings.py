# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/one_categories/rings.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Ring ABCs.

Defines:
1. _RingsCategory_ABC: The Category of Rings (Objects=Rings, Morphisms=Ring Homomorphisms).
2. _RingObject_ABC: An Object in the Category of Rings (A Ring R).
3. _RingElement_ABC: An element r ∈ R (a (-1)-cell).
4. _Ideal_ABC: An ideal I ⊆ R.

Per docs/categories_to_implement.md §Rings.
"""

from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs


class _RingsCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    The Category of Rings (Ring).

    - Objects: Rings (instances of CategoryABCs.RingObject).
    - Morphisms: Ring homomorphisms.
    - Structure: Complete, Cocomplete.
    """

    @final
    @abstractmethod
    def forgetful_functor_to_abelian_groups(self) -> CategoryABCs.Functor:
        """U: Ring → Ab (forgetful to additive group)."""
        ...

    @final
    @abstractmethod
    def forgetful_functor_to_sets(self) -> CategoryABCs.Functor:
        """U: Ring → Set."""
        ...

    @final
    @abstractmethod
    def zero_ring(self) -> CategoryABCs.RingObject:
        """Return the zero ring {0} (terminal object)."""
        ...

    @final
    @abstractmethod
    def integers(self) -> CategoryABCs.RingObject:
        """Return ℤ (initial object in Ring)."""
        ...


class _RingObject_ABC(CategoryABCs.GroupObject, ABC):
    """
    An Object in the Category of Rings (A Ring R).

    By default, rings are assumed associative and unital.
    
    Inherits from GroupObject: (R, +) is an abelian group, so cardinality(),
    is_finite(), identity_element() (=zero), binary_operation() (=add), 
    inverse() (=negation) are inherited.
    """

    # === Forgetful functor views ===

    def as_set(self) -> CategoryABCs.SetObject:
        """View as underlying set (forgetful functor U: Ring → Set)."""
        return self

    def as_additive_group(self) -> CategoryABCs.GroupObject:
        """View (R, +) as an abelian group (forgetful functor U: Ring → Ab)."""
        return self

    @abstractmethod
    def as_multiplicative_monoid(self) -> CategoryABCs.Object:
        """
        View (R, ×) as a monoid (forgetful functor U: Ring → Mon).
        
        Abstract since this may require constructing a separate object
        representing the multiplicative structure.
        """
        ...

    # === Ring structure ===

    @final
    @abstractmethod
    def zero(self) -> CategoryABCs.RingElement:
        """0 ∈ R (additive identity)."""
        ...

    @final
    @abstractmethod
    def one(self) -> CategoryABCs.RingElement:
        """1 ∈ R (multiplicative identity)."""
        ...

    @final
    @abstractmethod
    def characteristic(self) -> int:
        """char(R) = min{n > 0 | n · 1 = 0}, or 0 if none exists."""
        ...

    # === Unit group ===

    @final
    @abstractmethod
    def unit_group(self) -> CategoryABCs.GroupObject:
        """R^× (group of units)."""
        ...

    # === Ideals ===

    @final
    @abstractmethod
    def ideal_generated_by(
        self, xs: list[CategoryABCs.RingElement]
    ) -> CategoryABCs.Ideal:
        """⟨x_1, ..., x_n⟩ ⊆ R."""
        ...

    @final
    @abstractmethod
    def zero_ideal(self) -> CategoryABCs.Ideal:
        """(0) ⊆ R."""
        ...

    @final
    @abstractmethod
    def unit_ideal(self) -> CategoryABCs.Ideal:
        """R = (1) ⊆ R."""
        ...

    @final
    @abstractmethod
    def quotient_by_ideal(self, ideal: CategoryABCs.Ideal) -> CategoryABCs.RingObject:
        """R/I (quotient ring by ideal). Note: quotient_by(N) from GroupObject is for subgroup quotients."""
        ...

    # === Localization ===

    @final
    @abstractmethod
    def localize(self, s: Any) -> CategoryABCs.RingObject:
        """S^{-1}R (localization at multiplicative set S)."""
        ...

    @final
    @abstractmethod
    def localize_at_prime(self, p: CategoryABCs.Ideal) -> CategoryABCs.RingObject:
        """R_p (localization at prime ideal p)."""
        ...

    # === Polynomial extensions ===

    @final
    @abstractmethod
    def polynomial_ring(self, var_names: list[str]) -> CategoryABCs.RingObject:
        """R[x_1, ..., x_n]."""
        ...

    @final
    @abstractmethod
    def power_series_ring(self, var_names: list[str]) -> CategoryABCs.RingObject:
        """R[[x_1, ..., x_n]]."""
        ...

    # === Dimension theory ===

    @final
    @abstractmethod
    def krull_dimension(self) -> Any:
        """dim(R) (Krull dimension)."""
        ...

    # === Predicates ===

    @final
    @abstractmethod
    def is_unital(self) -> BoolProof:
        """Check if R has a multiplicative identity."""
        ...

    @final
    @abstractmethod
    def is_commutative(self) -> BoolProof:
        """Check if R is commutative."""
        ...

    @final
    @abstractmethod
    def is_field(self) -> BoolProof:
        """Check if R is a field."""
        ...

    @final
    @abstractmethod
    def is_integral_domain(self) -> BoolProof:
        """Check if R is an integral domain."""
        ...

    @final
    @abstractmethod
    def is_pid(self) -> BoolProof:
        """Check if R is a principal ideal domain."""
        ...

    @final
    @abstractmethod
    def is_ufd(self) -> BoolProof:
        """Check if R is a unique factorization domain."""
        ...

    @final
    @abstractmethod
    def is_noetherian(self) -> BoolProof:
        """Check if R is Noetherian."""
        ...

    @final
    @abstractmethod
    def is_artinian(self) -> BoolProof:
        """Check if R is Artinian."""
        ...

    @final
    @abstractmethod
    def is_local(self) -> BoolProof:
        """Check if R is local (unique maximal ideal)."""
        ...

    @final
    @abstractmethod
    def is_reduced(self) -> BoolProof:
        """Check if R has no nonzero nilpotent elements."""
        ...


class _RingElement_ABC(CategoryABCs.Element, ABC):
    """
    An element r ∈ R.

    Inherits from CategoryABCs.Element (the standard element interface).
    """

    @abstractmethod
    def parent_ring(self) -> CategoryABCs.RingObject:
        """Alias for parent_object() - return the ring R containing this element."""
        ...

    @final
    @abstractmethod
    def __add__(self, other: CategoryABCs.RingElement) -> CategoryABCs.RingElement:
        """r + s."""
        ...

    @final
    @abstractmethod
    def __neg__(self) -> CategoryABCs.RingElement:
        """-r (additive inverse)."""
        ...

    @final
    @abstractmethod
    def __sub__(self, other: CategoryABCs.RingElement) -> CategoryABCs.RingElement:
        """r - s."""
        ...

    @final
    @abstractmethod
    def __mul__(self, other: CategoryABCs.RingElement) -> CategoryABCs.RingElement:
        """r · s."""
        ...

    @final
    @abstractmethod
    def __pow__(self, n: int) -> CategoryABCs.RingElement:
        """r^n."""
        ...

    @final
    @abstractmethod
    def is_unit(self) -> BoolProof:
        """Check if r ∈ R^×."""
        ...

    @final
    @abstractmethod
    def is_zero_divisor(self) -> BoolProof:
        """Check if ∃s ≠ 0 with rs = 0."""
        ...

    @final
    @abstractmethod
    def is_nilpotent(self) -> BoolProof:
        """Check if ∃n with r^n = 0."""
        ...


class _RingHomomorphism_ABC(CategoryABCs.OneMorphism_In_A_1_Cat, ABC):
    """
    A ring homomorphism φ: R → S.

    Inherits source()/target(), is_injective()/is_surjective()/is_isomorphism(),
    compose(), is_identity(), etc. from Morphism_In_A_1_Cat.
    """
    ...


# Expose for registration
_ = _RingsCategory_ABC
_ = _RingObject_ABC
_ = _RingElement_ABC
_ = _RingHomomorphism_ABC

