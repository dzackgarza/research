# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/one_categories/mod_R.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
R-Module ABCs.

Defines:
1. _RMod_ABC: The Category of R-Modules for a fixed ring R.
2. _ModuleObject_ABC: An R-module M.
3. _ModuleElement_ABC: An element m ∈ M.

Per docs/categories_to_implement.md §RMod.
"""

from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs


class _RMod_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    The Category of R-Modules (R-Mod) for a fixed ring R.

    - Objects: R-modules.
    - Morphisms: R-module homomorphisms.
    - Structure: Abelian category (kernels, cokernels, exact sequences).
    """

    @final
    @abstractmethod
    def base_ring(self) -> CategoryABCs.RingObject:
        """Return the base ring R."""
        ...

    @final
    @abstractmethod
    def zero_module(self) -> CategoryABCs.ModuleObject:
        """Return the zero module {0} (zero object)."""
        ...

    @final
    @abstractmethod
    def free_module(self, rank: int) -> CategoryABCs.ModuleObject:
        """Return R^n (free module of rank n)."""
        ...

    # === Functors to related categories ===

    @final
    @abstractmethod
    def forgetful_functor_to_sets(self) -> CategoryABCs.Functor:
        """U: R-Mod → Set (forgetful functor)."""
        ...

    @final
    @abstractmethod
    def forgetful_functor_to_abelian_groups(self) -> CategoryABCs.Functor:
        """U: R-Mod → Ab (forget R-action, retain abelian group structure)."""
        ...

    @final
    @abstractmethod
    def base_change_functor(
        self, f: CategoryABCs.OneMorphism_In_A_1_Cat
    ) -> CategoryABCs.Functor:
        """
        Extension of scalars along ring homomorphism f: R → S.
        Returns functor R-Mod → S-Mod.
        """
        ...


class _ModuleObject_ABC(CategoryABCs.GroupObject, ABC):
    """
    An R-module M.

    A 0-cell in R-Mod.
    
    Inherits from GroupObject: (M, +) is an abelian group, so cardinality(),
    is_finite(), identity_element() (=zero), binary_operation() (=add), 
    inverse() (=negation) are inherited.
    """

    # === Forgetful functor views ===

    def as_set(self) -> CategoryABCs.SetObject:
        """View as underlying set (forgetful functor U: R-Mod → Set)."""
        return self

    def as_abelian_group(self) -> CategoryABCs.GroupObject:
        """View (M, +) as an abelian group (forgetful functor U: R-Mod → Ab)."""
        return self

    # === Base ring ===

    @final
    @abstractmethod
    def base_ring(self) -> CategoryABCs.RingObject:
        """Return the base ring R."""
        ...

    # === Module structure ===

    @final
    @abstractmethod
    def zero(self) -> CategoryABCs.ModuleElement:
        """0 ∈ M (additive identity)."""
        ...

    @final
    @abstractmethod
    def add(
        self, x: CategoryABCs.ModuleElement, y: CategoryABCs.ModuleElement
    ) -> CategoryABCs.ModuleElement:
        """x + y."""
        ...

    @final
    @abstractmethod
    def scalar_multiply(
        self, r: CategoryABCs.RingElement, m: CategoryABCs.ModuleElement
    ) -> CategoryABCs.ModuleElement:
        """r · m (scalar multiplication)."""
        ...

    # === Structure theory ===

    @final
    @abstractmethod
    def annihilator(self) -> CategoryABCs.Ideal:
        """Ann(M) = {r ∈ R | rM = 0}."""
        ...

    @final
    @abstractmethod
    def support(self) -> list[CategoryABCs.Ideal]:
        """Supp(M) = {p ∈ Spec(R) | M_p ≠ 0}."""
        ...

    @final
    @abstractmethod
    def associated_primes(self) -> list[CategoryABCs.Ideal]:
        """Ass(M) (associated prime ideals)."""
        ...

    # === Submodules ===

    @final
    @abstractmethod
    def submodule_generated_by(
        self, elements: list[CategoryABCs.ModuleElement]
    ) -> CategoryABCs.ModuleObject:
        """⟨m_1, ..., m_n⟩ ⊆ M."""
        ...

    @final
    @abstractmethod
    def quotient_by_submodule(
        self, submodule: CategoryABCs.ModuleObject
    ) -> CategoryABCs.ModuleObject:
        """M/N (quotient module). Note: quotient_by(N) from GroupObject is for abelian group quotients."""
        ...

    # === Base change ===

    @final
    @abstractmethod
    def base_change(self, f: CategoryABCs.OneMorphism_In_A_1_Cat) -> CategoryABCs.ModuleObject:
        """M ⊗_R S along f: R → S (extension of scalars)."""
        ...

    @final
    @abstractmethod
    def localize(self, s: Any) -> CategoryABCs.ModuleObject:
        """S^{-1}M (localization)."""
        ...

    # === Duality ===

    @final
    @abstractmethod
    def dual(self) -> CategoryABCs.ModuleObject:
        """Hom_R(M, R) (dual module)."""
        ...

    # === Generators and rank ===

    @final
    @abstractmethod
    def generators(self) -> list[CategoryABCs.ModuleElement]:
        """Return a generating set for M."""
        ...

    @final
    @abstractmethod
    def rank(self) -> Any:
        """Rank of M (if free or over a domain)."""
        ...

    # === Predicates ===

    @final
    @abstractmethod
    def is_free(self) -> BoolProof:
        """Check if M is free."""
        ...

    @final
    @abstractmethod
    def is_projective(self) -> BoolProof:
        """Check if M is projective."""
        ...

    @final
    @abstractmethod
    def is_injective(self) -> BoolProof:
        """Check if M is injective."""
        ...

    @final
    @abstractmethod
    def is_flat(self) -> BoolProof:
        """Check if M is flat."""
        ...

    # is_finitely_generated() inherited from GroupObject

    @final
    @abstractmethod
    def is_noetherian(self) -> BoolProof:
        """Check if M is Noetherian."""
        ...

    @final
    @abstractmethod
    def is_artinian(self) -> BoolProof:
        """Check if M is Artinian."""
        ...

    @final
    @abstractmethod
    def is_torsion(self) -> BoolProof:
        """Check if M is a torsion module."""
        ...

    @final
    @abstractmethod
    def is_torsion_free(self) -> BoolProof:
        """Check if M is torsion-free."""
        ...


class _ModuleElement_ABC(CategoryABCs.Element_In_A_1_Cat, ABC):
    """
    An element m ∈ M.

    Inherits from CategoryABCs.Element (the standard element interface).
    """

    @final
    @abstractmethod
    def parent_module(self) -> CategoryABCs.ModuleObject:
        """Alias for parent_object() - return the module M containing this element."""
        ...

    @final
    @abstractmethod
    def __add__(
        self, other: CategoryABCs.ModuleElement
    ) -> CategoryABCs.ModuleElement:
        """m + n."""
        ...

    @final
    @abstractmethod
    def __neg__(self) -> CategoryABCs.ModuleElement:
        """-m (additive inverse)."""
        ...

    @final
    @abstractmethod
    def __sub__(
        self, other: CategoryABCs.ModuleElement
    ) -> CategoryABCs.ModuleElement:
        """m - n."""
        ...

    @final
    @abstractmethod
    def scalar_multiply(
        self, r: CategoryABCs.RingElement
    ) -> CategoryABCs.ModuleElement:
        """r · m."""
        ...

    @final
    @abstractmethod
    def annihilator(self) -> CategoryABCs.Ideal:
        """Ann(m) = {r ∈ R | rm = 0}."""
        ...

    @final
    @abstractmethod
    def is_torsion(self) -> BoolProof:
        """Check if ∃r ≠ 0 with rm = 0."""
        ...

    @final
    @abstractmethod
    def is_zero(self) -> BoolProof:
        """Check if m = 0."""
        ...


class _ModuleHomomorphism_ABC(CategoryABCs.OneMorphism_In_A_1_Cat, ABC):
    """
    An R-module homomorphism φ: M → N.

    Inherits source()/target(), is_injective()/is_surjective()/is_isomorphism(),
    compose(), is_identity(), etc. from Morphism_In_A_1_Cat.
    """
    ...


# Expose for registration
_ = _RMod_ABC
_ = _ModuleObject_ABC
_ = _ModuleElement_ABC
_ = _ModuleHomomorphism_ABC
