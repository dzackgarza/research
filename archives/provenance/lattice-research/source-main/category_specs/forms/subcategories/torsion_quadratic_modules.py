r"""Finite torsion modules with quadratic forms."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Self, final

from sage.categories.category import Category

from ...cat import Category_over_base_ring
from ...modules import Modules
from .quadratic import QuadraticModulesMorphism

if TYPE_CHECKING:
    from ...types import Group, Matrix, Morphism, RingElement, RModule, RModuleElement, SetFamily


class TorsionQuadraticModulesCategory(Category_over_base_ring):
    r"""Finite ``ZZ``-modules equipped with a torsion quadratic form.

    Canonical chain:
    ``FinitelyPresentedModulesOverPID(ZZ).Torsion().WithForms().Quadratic()``.

    The invariant-factor surface belongs to
    ``Modules(R).FinitelyPresented().OverPID()`` and is inherited here.
    """

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Modules(R)
            .FinitelyPresented()
            .OverPID()
            .Torsion()
            .WithForms()
            .Quadratic(),
        ]

    class ParentMethods:
        @final
        def is_torsion_quadratic_module(self) -> bool:
            return True

        @abstractmethod
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstractmethod
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstractmethod
        def brown_invariant(self) -> RingElement: ...

        @abstractmethod
        def b(self, x: RModuleElement, y: RModuleElement) -> RingElement:
            r"""Evaluate the torsion bilinear pairing."""
            ...

        @abstractmethod
        def q(self, x: RModuleElement) -> RingElement:
            r"""Evaluate the torsion quadratic refinement."""
            ...

        @abstractmethod
        def orthogonal_group(self) -> Group:
            r"""Return the automorphism group preserving the torsion quadratic form."""
            ...

        @abstractmethod
        def isotropic_elements(self) -> tuple[RModuleElement, ...]:
            r"""Return the finite tuple of elements ``x`` with ``q(x) = 0``."""
            ...

        @abstractmethod
        def normal_form(
            self, *, partial: bool = False, return_isometry: bool = False
        ) -> object:
            r"""Return a canonical torsion quadratic module normal form, optionally with an isometry."""
            ...

        @abstractmethod
        def primary_part(self, m: RingElement) -> Self:
            r"""Return the ``m``-primary formed submodule."""
            ...

        @abstractmethod
        def value_module(self) -> RModule:
            r"""Return the quotient module containing bilinear-form values."""
            ...

        @abstractmethod
        def value_module_qf(self) -> RModule:
            r"""Return the quotient module containing quadratic-form values."""
            ...

        @abstractmethod
        def as_additive_abelian_group(self) -> Group:
            """Return the underlying finite additive abelian group view."""
            ...

        @final
        def underlying_abelian_group(self) -> Group:
            """Alias for the underlying finite additive abelian group view."""
            return self.as_additive_abelian_group()

        @abstractmethod
        def zero(self) -> RModuleElement:
            """Return the additive identity element."""
            ...

        @final
        def identity(self) -> RModuleElement:
            """Return the additive identity element."""
            return self.zero()

        @abstractmethod
        def generator_orders(self) -> tuple[RingElement, ...]:
            """Return the orders of the distinguished additive generators."""
            ...

        @abstractmethod
        def rank_p(self, p: RingElement) -> int:
            """Return the p-rank of the underlying finite abelian group."""
            ...

        @abstractmethod
        def length_p(self, p: RingElement) -> int:
            """Return the p-length of the underlying finite abelian group."""
            ...

        @abstractmethod
        def discrete_log(self, x: RModuleElement, gens: Sequence[RModuleElement] | None = None) -> object:
            """Express ``x`` in the requested finite generating set."""
            ...

        @abstractmethod
        def discrete_exp(self, v: Sequence[RingElement], gens: Sequence[RModuleElement] | None = None) -> RModuleElement:
            """Build an element from coordinates in the requested finite generating set."""
            ...

        @abstractmethod
        def coordinates(self, x: RModuleElement, gens: Sequence[RModuleElement] | None = None, *, reduce: bool = True) -> object:
            """Return additive coordinates of ``x`` in the requested generators."""
            ...

        @abstractmethod
        def relations_among(self, gens: Sequence[RModuleElement]) -> RModule:
            """Return the relation module among the supplied finite-order generators."""
            ...

        @abstractmethod
        def basis_from_generators(self, gens: Sequence[RModuleElement]) -> object:
            """Return a presentation basis produced by the supplied generators."""
            ...

        @abstractmethod
        def from_generators(self, gens: Sequence[RModuleElement]) -> object:
            """Return the subgroup generated by finite-order elements, preserving form data when possible."""
            ...

        @final
        def subgroup_generated_by(self, gens: Sequence[RModuleElement]) -> object:
            """Return the subgroup generated by ``gens``."""
            return self.from_generators(gens)

        @final
        def subgroup(self, gens: Sequence[RModuleElement]) -> object:
            """Group-language alias for the subgroup generated by ``gens``."""
            return self.subgroup_generated_by(gens)

        @abstractmethod
        def subgroups(self) -> SetFamily:
            """Return the finite subgroups in group-facing vocabulary."""
            ...

        @final
        def all_subgroups(self) -> SetFamily:
            """Alias for the full subgroup family."""
            return self.subgroups()

        @abstractmethod
        def contains_subgroup(self, H: object) -> bool:
            """Return whether ``H`` is a subgroup of this finite module."""
            ...

        @abstractmethod
        def quotient_group(self, H: object) -> Group:
            """Return the ordinary finite abelian quotient by ``H``."""
            ...

        @abstractmethod
        def quotient(self, H: object) -> object:
            """Return the quotient object, using form-aware semantics only when the form descends."""
            ...

        @abstractmethod
        def quotient_map(self, H: object) -> Morphism:
            """Return the quotient map to the quotient by ``H``."""
            ...

        @abstractmethod
        def cosets(self, H: object) -> SetFamily:
            """Return the cosets of ``H`` in the underlying finite group."""
            ...

        @abstractmethod
        def p_torsion(self, p: RingElement, *, k: int = 1) -> object:
            """Return the subgroup killed by p^k."""
            ...

        @abstractmethod
        def p_primary_part(self, p: RingElement) -> object:
            """Return the p-primary part of the finite additive group."""
            ...

        @abstractmethod
        def primary_decomposition(self) -> tuple[object, ...]:
            """Return the primary decomposition of the finite additive group."""
            ...

        @final
        def primary_parts(self) -> tuple[object, ...]:
            """Alias for the primary decomposition."""
            return self.primary_decomposition()

        @abstractmethod
        def torsion_subgroup(self) -> object:
            """Return the torsion subgroup; for this category it is the whole object."""
            ...

        @abstractmethod
        def automorphism_group(self) -> Group:
            """Return the underlying finite abelian group automorphism group."""
            ...

        @abstractmethod
        def is_isotropic_element(self, x: RModuleElement) -> bool:
            """Return whether the quadratic form vanishes on ``x`` in Q/Z."""
            ...

        @abstractmethod
        def is_isotropic_subgroup(self, H: object) -> bool:
            """Return whether every element of ``H`` is isotropic."""
            ...

        @final
        def is_totally_isotropic(self, H: object) -> bool:
            """Alias for isotropic subgroup testing."""
            return self.is_isotropic_subgroup(H)

        @abstractmethod
        def is_lagrangian(self, H: object) -> bool:
            """Return whether ``H`` is maximal isotropic and equals its orthogonal complement quotient-theoretically."""
            ...

        @abstractmethod
        def is_metabolic(self) -> bool:
            """Return whether this torsion quadratic module admits a lagrangian subgroup."""
            ...

        @abstractmethod
        def is_anisotropic(self) -> bool:
            """Return whether the only isotropic element is zero."""
            ...

        @abstractmethod
        def is_maximal_isotropic(self, H: object) -> bool:
            """Return whether ``H`` is maximal among isotropic subgroups."""
            ...

        @abstractmethod
        def isotropic_subgroups(self) -> SetFamily:
            """Return the isotropic subgroups."""
            ...

        @abstractmethod
        def maximal_isotropic_subgroups(self) -> SetFamily:
            """Return maximal isotropic subgroups."""
            ...

        @abstractmethod
        def lagrangian_subgroups(self) -> SetFamily:
            """Return lagrangian subgroups."""
            ...

        @final
        def metabolizers(self) -> SetFamily:
            """Alias for lagrangian subgroups in gluing terminology."""
            return self.lagrangian_subgroups()

        @abstractmethod
        def orthogonal(self, H: object) -> object:
            """Return the orthogonal subgroup to ``H`` for the bilinear pairing."""
            ...

        @final
        def orthogonal_complement(self, H: object) -> object:
            """Alias for the orthogonal subgroup to ``H``."""
            return self.orthogonal(H)

        @abstractmethod
        def orthogonal_quotient(self, H: object) -> object:
            """Return H^perp/H with the induced finite quadratic or bilinear form."""
            ...

        @abstractmethod
        def restricted_form(self, H: object) -> object:
            """Return the restriction of the finite form to ``H``."""
            ...

        @abstractmethod
        def pushforward_form(self, phi: Morphism) -> object:
            """Return the pushed-forward finite form along ``phi`` when defined."""
            ...

        @abstractmethod
        def pullback_form(self, phi: Morphism) -> object:
            """Return the pulled-back finite form along ``phi``."""
            ...

        @abstractmethod
        def subquotient_form(self, H: object, K: object) -> object:
            """Return the induced form on K/H for H contained in K contained in H^perp."""
            ...

        @abstractmethod
        def bilinear_orthogonal_group(self) -> Group:
            """Return the automorphism group preserving only the bilinear pairing."""
            ...

        @abstractmethod
        def quadratic_orthogonal_group(self) -> Group:
            """Return the automorphism group preserving the quadratic refinement."""
            ...

        @final
        def isometry_group(self) -> Group:
            """Return the quadratic isometry group."""
            return self.quadratic_orthogonal_group()

        @abstractmethod
        def isometry_to(self, other: object, *, kind: str = "quadratic") -> Morphism:
            """Return an isometry to ``other`` for the requested group, bilinear form, or quadratic form structure."""
            ...

        @abstractmethod
        def is_isomorphic_to(self, other: object, *, kind: str = "quadratic") -> bool:
            """Return whether this object is isomorphic to ``other`` in the requested category."""
            ...

        @abstractmethod
        def character_group(self) -> Group:
            """Return the additive character group Hom(A, Q/Z)."""
            ...

        @final
        def pontryagin_dual(self) -> Group:
            """Alias for the character group."""
            return self.character_group()

        @abstractmethod
        def pairing_character(self, x: RModuleElement) -> object:
            """Return the character y |-> b(x, y)."""
            ...

        @abstractmethod
        def pairing_isomorphism_to_dual(self) -> Morphism:
            """Return the pairing map from this module to its Pontryagin dual when nondegenerate."""
            ...

        @abstractmethod
        def annihilator_subgroup(self, H: object) -> object:
            """Return the annihilator of ``H`` under the finite pairing."""
            ...

        @abstractmethod
        def left_kernel(self) -> object:
            """Return the left kernel of the bilinear pairing."""
            ...

        @abstractmethod
        def right_kernel(self) -> object:
            """Return the right kernel of the bilinear pairing."""
            ...

        @abstractmethod
        def is_nondegenerate(self) -> bool:
            """Return whether the finite bilinear pairing is nondegenerate."""
            ...
    class ElementMethods: ...


TorsionQuadraticModulesObject = TorsionQuadraticModulesCategory.ParentMethods
TorsionQuadraticModulesElement = TorsionQuadraticModulesCategory.ElementMethods
TorsionQuadraticModulesMorphism = QuadraticModulesMorphism
