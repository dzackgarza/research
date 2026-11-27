r"""Hom, end, and aut categories for singular lattice objects."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.misc.lazy_import import LazyImport

from category_specs.homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalEndElementMethods,
)
from category_specs.lattices import Lattices
from category_specs.lattices.homsets import (
    LatticeHomCategory as SpecLatticeHomCategory,
)
from category_specs.modules import Modules
from category_specs.modules.homsets import (
    RModuleAutCategory,
    RModuleEndCategory,
    RModuleHomCategory,
)

if TYPE_CHECKING:
    from category_specs.cat import Category
    from category_specs.types import (
        Lattice,
        LatticeOrthogonalGroup,
        Matrix,
        Morphism,
        RModuleElement,
    )


class LatticeHomParentMethods(
    RModuleHomCategory.ParentMethods,
    metaclass=ABCMeta,
):
    r"""Parent methods for Hom objects between singular lattice objects."""

    @abstractmethod
    def domain(self) -> Lattice:
        r"""Return the source lattice."""
        ...

    @abstractmethod
    def codomain(self) -> Lattice:
        r"""Return the target lattice."""
        ...

    @abstractmethod
    def from_matrix(self, matrix: Matrix) -> LatticeMorphismMethods:
        r"""Construct a lattice morphism from a matrix in chosen generators."""
        ...

    @abstractmethod
    def from_images(
        self, images: tuple[RModuleElement, ...]
    ) -> LatticeMorphismMethods:
        r"""Construct a lattice morphism from generator images."""
        ...

    @abstractmethod
    def identity(self) -> LatticeMorphismMethods:
        r"""Return the identity morphism when domain and codomain agree."""
        ...

    @override
    @final
    def zero(self) -> LatticeMorphismMethods:
        r"""Return the zero lattice morphism."""
        return super().zero()


class LatticeMorphismMethods(
    SpecLatticeHomCategory.ElementMethods,
    metaclass=ABCMeta,
):
    r"""Element methods for lattice morphisms.

    Elements of a lattice Hom object are module morphisms preserving the
    bilinear form. Isometries are precisely the bijective such morphisms.
    """

    @abstractmethod
    def domain(self) -> Lattice:
        r"""Return the source lattice."""
        ...

    @abstractmethod
    def codomain(self) -> Lattice:
        r"""Return the target lattice."""
        ...

    @abstractmethod
    def __call__(self, vector: RModuleElement) -> RModuleElement:
        r"""Evaluate this morphism on a lattice element."""
        ...

    @abstractmethod
    def to_matrix(self) -> Matrix:
        r"""Return the matrix in the chosen generators of domain and codomain."""
        ...

    @final
    def is_form_preserving(self) -> bool:
        r"""Return ``True`` because this is the Hom category membership witness."""
        return True

    @final
    def is_isometry(self) -> bool:
        r"""Return whether this form-preserving morphism is bijective."""
        return bool(self.is_bijective())


class LatticeEndomorphismMethods(
    LatticeMorphismMethods,
    UniversalEndElementMethods,
):
    r"""Element methods for lattice endomorphisms."""


class LatticeAutomorphismMethods(
    LatticeEndomorphismMethods,
    UniversalAutElementMethods,
):
    r"""Element methods for lattice automorphisms."""

    @override
    @final
    def is_isometry(self) -> bool:
        r"""Return ``True`` because lattice automorphisms are isometries."""
        return True


class LatticeHomCategory(HomCategoryOf):
    r"""Category of Hom objects between singular lattice objects."""

    @final
    def extra_super_categories(self) -> list[Category]:
        R = self.base_category().base_ring()
        return [
            HomCategoryOf(self.base_category()),
            SpecLatticeHomCategory(Lattices(R)),
            Modules(R).HomCategory(),
        ]

    ParentMethods = LatticeHomParentMethods
    ElementMethods = LatticeMorphismMethods

    Endset = LazyImport(__name__, "LatticeEndCategory")


class LatticeEndCategory(GenericEndCategory):
    r"""Category of endomorphism objects of singular lattice objects."""

    _base_category_class_and_axiom = (LatticeHomCategory, "Endset")
    Autset = LazyImport(__name__, "LatticeAutCategory")

    class ParentMethods(RModuleEndCategory.ParentMethods, metaclass=ABCMeta):
        @abstractmethod
        def base_lattice(self) -> Lattice:
            r"""Return the lattice on which this endomorphism object acts."""
            ...

    ElementMethods = LatticeEndomorphismMethods


class LatticeAutCategory(GenericAutCategory):
    r"""Category of automorphism objects of singular lattice objects."""

    _base_category_class_and_axiom = (LatticeEndCategory, "Autset")

    class ParentMethods(RModuleAutCategory.ParentMethods, metaclass=ABCMeta):
        @abstractmethod
        def base_lattice(self) -> Lattice:
            r"""Return the lattice on which this automorphism object acts."""
            ...

        @abstractmethod
        def discriminant_action(self) -> Morphism:
            r"""Return the action homomorphism ``O(L) -> O(A_L, q_L)``."""
            ...

        @abstractmethod
        def image_in_discriminant_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return the image subgroup in ``O(A_L, q_L)``."""
            ...

        @abstractmethod
        def kernel_of_discriminant_action(self) -> LatticeOrthogonalGroup:
            r"""Return the subgroup acting trivially on the discriminant group."""
            ...

        @abstractmethod
        def special_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return the determinant-one subgroup of this orthogonal group."""
            ...

        @abstractmethod
        def stable_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde O(L)``, the stable orthogonal subgroup."""
            ...

    ElementMethods = LatticeAutomorphismMethods
