# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/one_categories/ideals.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Ideal ABCs.

Defines:
1. _IdealsCategory_ABC: The Category of Ideals of a fixed ring R.
2. _Ideal_ABC: An ideal I ⊆ R (a submodule of R as an R-module).

Ideals are special R-submodules of R itself. The category of ideals
is equipped with functors to related categories.

Per docs/categories_to_implement.md §Rings.
"""

from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs


class _IdealsCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    The Category of Ideals of a fixed ring R.

    - Objects: Ideals I ⊆ R.
    - Morphisms: Inclusion maps (I ⊆ J).
    - Structure: Lattice structure (meet = ∩, join = +).
    """

    @final
    @abstractmethod
    def base_ring(self) -> CategoryABCs.RingObject:
        """Return the ambient ring R."""
        ...

    @final
    @abstractmethod
    def zero_ideal(self) -> CategoryABCs.Ideal:
        """Return (0) ⊆ R (initial object in this category)."""
        ...

    @final
    @abstractmethod
    def unit_ideal(self) -> CategoryABCs.Ideal:
        """Return R = (1) ⊆ R (terminal object in this category)."""
        ...

    @final
    @abstractmethod
    def principal_ideal(self, a: CategoryABCs.RingElement) -> CategoryABCs.Ideal:
        """Return (a) = Ra ⊆ R."""
        ...

    @final
    @abstractmethod
    def ideal_generated_by(
        self, generators: list[CategoryABCs.RingElement]
    ) -> CategoryABCs.Ideal:
        """Return (a_1, ..., a_n) = Ra_1 + ... + Ra_n ⊆ R."""
        ...

    # === Functors to related categories ===

    @final
    @abstractmethod
    def forgetful_functor_to_sets(self) -> CategoryABCs.Functor:
        """U: Ideals(R) → Set (forgetful functor)."""
        ...

    @final
    @abstractmethod
    def functor_to_mod_R(self) -> CategoryABCs.Functor:
        """Inclusion functor: Ideals(R) → R-Mod (ideals as R-submodules of R)."""
        ...

    @final
    @abstractmethod
    def functor_to_quotient_rings(self) -> CategoryABCs.Functor:
        """Quotient functor: I ↦ R/I (contravariant: I ⊆ J ⟹ R/J → R/I)."""
        ...


class _Ideal_ABC(CategoryABCs.Object_In_A_1_Cat, ABC):
    """
    An ideal I ⊆ R.

    An ideal is a submodule of R viewed as an R-module over itself.
    This is a 0-cell in the category of ideals.
    """

    # === Ideal-specific accessors ===

    @final
    @abstractmethod
    def base_ring(self) -> CategoryABCs.RingObject:
        """Return the ambient ring R."""
        ...

    @final
    @abstractmethod
    def generators(self) -> Sequence[CategoryABCs.RingElement]:
        """Return generators of I."""
        ...

    # === Conversion to related structures ===

    @final
    @abstractmethod
    def to_module(self) -> CategoryABCs.ModuleObject:
        """View I as an R-module (submodule of R)."""
        ...

    @final
    @abstractmethod
    def quotient_ring(self) -> CategoryABCs.RingObject:
        """R/I (quotient ring)."""
        ...

    # === Ideal operations (element-level, NOT categorical products) ===

    @final
    @abstractmethod
    def ideal_intersection(self, other: CategoryABCs.Ideal) -> CategoryABCs.Ideal:
        """I ∩ J (set-theoretic intersection)."""
        ...

    @final
    @abstractmethod
    def ideal_sum(self, other: CategoryABCs.Ideal) -> CategoryABCs.Ideal:
        """I + J = {a + b | a ∈ I, b ∈ J}."""
        ...

    @final
    @abstractmethod
    def ideal_product(self, other: CategoryABCs.Ideal) -> CategoryABCs.Ideal:
        """IJ = {Σ aᵢbᵢ | aᵢ ∈ I, bᵢ ∈ J}."""
        ...

    @final
    @abstractmethod
    def ideal_quotient(self, other: CategoryABCs.Ideal) -> CategoryABCs.Ideal:
        """(I : J) = {r ∈ R | rJ ⊆ I} (colon ideal)."""
        ...

    @final
    @abstractmethod
    def radical(self) -> CategoryABCs.Ideal:
        """√I = {r ∈ R | r^n ∈ I for some n > 0}."""
        ...

    @final
    @abstractmethod
    def saturation(self, other: CategoryABCs.Ideal) -> CategoryABCs.Ideal:
        """I : J^∞ = ⋃_{n≥1} (I : J^n)."""
        ...

    @final
    @abstractmethod
    def ideal_power(self, n: int) -> CategoryABCs.Ideal:
        """I^n (n-fold product of I with itself)."""
        ...

    # === Computational algebra ===

    @final
    @abstractmethod
    def groebner_basis(self, reduced: bool) -> Sequence[CategoryABCs.RingElement]:
        """Compute a Gröbner basis for I (if R is a polynomial ring)."""
        ...

    @final
    @abstractmethod
    def normal_form(
        self, element: CategoryABCs.RingElement
    ) -> CategoryABCs.RingElement:
        """Compute the normal form of element modulo I."""
        ...

    # === Predicates ===

    @final
    @abstractmethod
    def is_principal(self) -> BoolProof:
        """Check if I = (a) for some a ∈ R."""
        ...

    @final
    @abstractmethod
    def is_prime(self) -> BoolProof:
        """Check if I is a prime ideal (ab ∈ I ⟹ a ∈ I or b ∈ I)."""
        ...

    @final
    @abstractmethod
    def is_maximal(self) -> BoolProof:
        """Check if I is a maximal ideal (R/I is a field)."""
        ...

    @final
    @abstractmethod
    def is_radical(self) -> BoolProof:
        """Check if I = √I."""
        ...

    @final
    @abstractmethod
    def is_primary(self) -> BoolProof:
        """Check if I is primary (ab ∈ I, a ∉ I ⟹ b^n ∈ I for some n)."""
        ...

    @final
    @abstractmethod
    def contains(self, element: CategoryABCs.RingElement) -> BoolProof:
        """Check if element ∈ I."""
        ...

    @final
    @abstractmethod
    def is_subset_of(self, other: CategoryABCs.Ideal) -> BoolProof:
        """Check if I ⊆ J."""
        ...

    @final
    @abstractmethod
    def is_proper_subset_of(self, other: CategoryABCs.Ideal) -> BoolProof:
        """Check if I ⊂ J (proper subset)."""
        ...


class _IdealInclusion_ABC(CategoryABCs.OneMorphism_In_A_1_Cat, ABC):
    """
    An ideal inclusion I ⊆ J.

    Inherits source()/target() from Morphism_In_A_1_Cat.
    Uses smaller()/larger() as semantic aliases.
    """

    @final
    @abstractmethod
    def smaller(self) -> CategoryABCs.Ideal:
        """Return the smaller ideal I (alias for source())."""
        ...

    @final
    @abstractmethod
    def larger(self) -> CategoryABCs.Ideal:
        """Return the larger ideal J (alias for target())."""
        ...

    @final
    @abstractmethod
    def is_proper(self) -> BoolProof:
        """Check if I ⊂ J (proper inclusion)."""
        ...


# Expose for registration
_ = _IdealsCategory_ABC
_ = _Ideal_ABC
_ = _IdealInclusion_ABC
