r"""Hom, end, and aut categories for lattices.

``Hom_Lattices(L, M)`` is the formed-module Hom object specialized to lattices:
its elements are module morphisms that preserve the specified bilinear form.
Matrix representatives exist only after finite free presentations or chosen
bases.  ``Aut_Lattices(L)`` is the lattice orthogonal group ``O(L)`` as a group
object; generators or presentations belong only to stronger group refinements.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override, TypeAlias

from sage.misc.lazy_import import LazyImport

from ..forms.subcategories.free_bilinear import FreeBilinearModulesCategory
from ..homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalEndElementMethods,
)
from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory

if TYPE_CHECKING:
    from ...cat import Category
    from ..types import Lattice, LatticeOrthogonalGroup, Morphism


class _LatticeHomCategoryObjectMethods(RModuleHomCategory.ParentMethods):
    r"""Lattice hom parent methods; generic hom methods are inherited."""


class _LatticeMorphisms(FreeBilinearModulesCategory.HomCategory.ElementMethods):
    r"""Morphisms of lattices: formed-module morphisms preserving the bilinear form."""

    @abstractmethod
    def restriction_to_sublattice(self, M: Lattice) -> Morphism:
        r"""Return this lattice morphism restricted to the sublattice ``M``."""
        ...

    @abstractmethod
    def induced_map_on_quotient(self, M: Lattice, N: Lattice) -> Morphism:
        r"""Return the induced map ``L/M -> K/N`` when this morphism sends ``M`` into ``N``."""
        ...

    @abstractmethod
    def induced_map_on_discriminant_group(self) -> Morphism:
        r"""Return the induced finite form morphism on discriminant groups."""
        ...

    @abstractmethod
    def kernel_on_discriminant_group(self) -> object:
        r"""Return the kernel of the induced action on the domain discriminant group."""
        ...


class _LatticeEndomorphisms(_LatticeMorphisms, UniversalEndElementMethods):
    r"""Endomorphisms (self-maps) in the lattice category."""


class _LatticeAutomorphisms(_LatticeEndomorphisms, UniversalAutElementMethods):
    r"""Lattice isometries, i.e. automorphisms in the lattice category."""

    @override
    @final
    def is_isometry(self) -> bool:
        return True


class LatticeHomCategory(HomCategoryOf):
    r"""Category of lattice hom objects ``Hom_Lattices(A, B)``.

    Canonical chain: ``Lattices(R).HomCategory()``.
    """

    @final
    def extra_super_categories(self) -> list[Category]:
        from ..modules import Modules

        R = self.base_category().base_ring()
        return [HomCategoryOf(self.base_category()), Modules(R).HomCategory()]

    ParentMethods : TypeAlias = _LatticeHomCategoryObjectMethods
    ElementMethods : TypeAlias = _LatticeMorphisms


    Endset = LazyImport(__name__, "LatticeEndCategory")


class LatticeEndCategory(GenericEndCategory):
    r"""Category of lattice endomorphism objects ``End_Lattices(A)``.

    Canonical chain: ``Lattices(R).EndCategory()``.
    """

    _base_category_class_and_axiom = (LatticeHomCategory, "Endset")
    Autset = LazyImport(__name__, "LatticeAutCategory")

    class ParentMethods(RModuleEndCategory.ParentMethods):
        @abstractmethod
        def base_lattice(self) -> Lattice: ...

    ElementMethods : TypeAlias = _LatticeEndomorphisms



class LatticeAutCategory(GenericAutCategory):
    r"""Category of lattice orthogonal groups ``Aut_Lattices(A)``.

    Canonical chain: ``Lattices(R).AutCategory()``.
    """

    _base_category_class_and_axiom = (LatticeEndCategory, "Autset")

    class ParentMethods(RModuleAutCategory.ParentMethods):
        @abstractmethod
        def discriminant_action(self) -> Morphism:
            r"""Return the action homomorphism ``O(L) -> O(A_L, q_L)``."""
            ...

        @abstractmethod
        def image_in_discriminant_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return the image subgroup of ``O(A_L, q_L)``."""
            ...

        @abstractmethod
        def kernel_of_discriminant_action(self) -> LatticeOrthogonalGroup:
            r"""Return the stable subgroup acting trivially on ``A_L``."""
            ...

        @abstractmethod
        def special_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return the determinant-one subgroup of this lattice orthogonal group."""
            ...

        @abstractmethod
        def stable_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return the subgroup acting trivially on the discriminant form.

            This is the stable orthogonal subgroup
            ``\widetilde O(L) = \ker(O(L) -> O(A_L, q_L))``.
            """
            ...

        @abstractmethod
        def stable_special_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde{SO}(L) = \widetilde O(L) \cap SO(L)``.

            The subgroup is taken inside this lattice orthogonal group.
            """
            ...

        @abstractmethod
        def plus_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``O^+(L)``, the real-spinor-kernel subgroup.

            This is the subgroup of ``O(L)`` whose real spinor norm is trivial.
            Positive-cone preservation is only an equivalent witness under the
            appropriate hyperbolic hypotheses.
            """
            ...

        @abstractmethod
        def special_plus_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO^+(L) = SO(L) \cap O^+(L)``."""
            ...

        @abstractmethod
        def stable_special_plus_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde{SO}^+(L)``.

            This is ``\widetilde O(L) \cap SO(L) \cap O^+(L)``.
            """
            ...

        @final
        def special_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO(L)``.

            This is the determinant-one subgroup of this orthogonal group.
            """
            return self.special_subgroup()

        @final
        def stable_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde O(L)``, the stable subgroup of this group."""
            return self.stable_subgroup()

        @final
        def stable_special_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde{SO}(L) = \widetilde O(L) \cap SO(L)``.

            The notation refers to the underlying lattice ``L``.
            """
            return self.stable_special_subgroup()

        @final
        def plus_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``O^+(L)``, the real-spinor-kernel subgroup."""
            return self.plus_subgroup()

        @final
        def special_plus_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO^+(L) = SO(L) \cap O^+(L)``."""
            return self.special_plus_subgroup()

        @final
        def stable_special_plus_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde{SO}^+(L)``."""
            return self.stable_special_plus_subgroup()

    ElementMethods : TypeAlias = _LatticeAutomorphisms
