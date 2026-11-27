r"""Discriminant-group construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, TypeAlias

from ....cat import Category_module
from ....forms.subcategories.quadratic import QuadraticModulesMorphism
from ....modules import (
    Modules,
    ModulesAut,
    ModulesAutCategory,
    ModulesAutomorphism,
    ModulesEnd,
    ModulesEndCategory,
    ModulesEndomorphism,
    ModulesHom,
    ModulesHomCategory,
)

if TYPE_CHECKING:
    from ....cat import Category
    from ....types import (
        BilinearForm,
        DiscriminantGroupElement,
        FormedModuleMorphism,
        Group,
        Lattice,
        LatticeMorphism,
        Matrix,
        Morphism,
        QuadraticForm,
        RingElement,
        RModuleElement,
        SetFamily,
    )


class LatticeDiscriminantGroupsCategory(Category_module):
    r"""Finite torsion modules with the discriminant form of a lattice.

    Canonical chain: ``Lattices(R).DiscriminantGroups()``.

    Invariant factors are inherited from the finitely presented PID-module
    surface.  They are not discriminant-group-specific data.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"discriminant groups over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Modules(R)
            .FinitelyPresented()
            .OverPID()
            .Torsion()
            .WithForms()
            .Bilinear()
            .Quadratic(),
        ]

    class ParentMethods:
        @abstractmethod
        def source_lattice(self) -> Lattice:
            r"""Return the lattice ``L`` whose dual inclusion defines this object."""
            ...

        @abstractmethod
        def metric_dual(self) -> Lattice:
            r"""Return the metric dual ``L^\#`` in the cokernel diagram."""
            ...

        @abstractmethod
        def inclusion_morphism(self) -> LatticeMorphism:
            r"""Return the metric inclusion ``L -> L^\#``."""
            ...

        @abstractmethod
        def projection(self) -> FormedModuleMorphism:
            r"""Return the quotient projection ``L^\# -> L^\#/L``."""
            ...

        @abstractmethod
        def bilinear_form(self) -> BilinearForm:
            r"""Return the descended bilinear form with codomain ``K/R``."""
            ...

        @abstractmethod
        def quadratic_form(self) -> QuadraticForm:
            r"""Return the descended quadratic form with codomain ``K/2R``."""
            ...

        @abstractmethod
        def b(self, x: RModuleElement, y: RModuleElement) -> RingElement:
            r"""Evaluate the induced discriminant bilinear form."""
            ...

        @abstractmethod
        def q(self, x: RModuleElement) -> RingElement:
            r"""Evaluate the induced discriminant quadratic form."""
            ...

        @abstractmethod
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstractmethod
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstractmethod
        def brown_invariant(self) -> RingElement: ...

        @abstractmethod
        def is_trivial(self) -> bool: ...

        @abstractmethod
        def primary_part(
            self, p: RingElement
        ) -> LatticeDiscriminantGroupsCategory.ParentMethods: ...

        @abstractmethod
        def p_primary_part(
            self, p: RingElement
        ) -> LatticeDiscriminantGroupsCategory.ParentMethods: ...

        @abstractmethod
        def all_submodules(self) -> SetFamily: ...

        @final
        def dual_lattice(self) -> Lattice:
            """Return the covering metric dual lattice L^vee."""
            return self.metric_dual()

        @final
        def cover_lattice(self) -> Lattice:
            """Return the covering lattice in the quotient L^vee/L."""
            return self.metric_dual()

        @final
        def relation_lattice(self) -> Lattice:
            """Return the relation lattice L in the quotient L^vee/L."""
            return self.source_lattice()

        @abstractmethod
        def lift_to_dual(self, x: DiscriminantGroupElement) -> RModuleElement:
            """Lift a discriminant-group element to a representative in L^vee."""
            ...

        @abstractmethod
        def project_from_dual(self, v: RModuleElement) -> DiscriminantGroupElement:
            """Project a vector in L^vee to its class in L^vee/L."""
            ...

        @abstractmethod
        def coset_representative(self, x: DiscriminantGroupElement) -> RModuleElement:
            """Return a preferred representative of the discriminant-group class ``x``."""
            ...

        @abstractmethod
        def preimage_lattice(self, H: object) -> Lattice:
            """Return the lattice preimage of a subgroup H of L^vee/L."""
            ...

        @abstractmethod
        def overlattice_from_isotropic_subgroup(self, H: object) -> Lattice:
            """Return the overlattice corresponding to an isotropic subgroup by Nikulin gluing."""
            ...

        @abstractmethod
        def discriminant_form_of_overlattice(self, H: object) -> object:
            """Return the discriminant form H^perp/H of the overlattice associated to H."""
            ...

        @abstractmethod
        def action_of_lattice_isometry(self, g: LatticeMorphism) -> Morphism:
            """Return the induced action of a lattice isometry on this discriminant group."""
            ...

        @abstractmethod
        def action_of_lattice_group(self, G: Group) -> Group:
            """Return the induced finite group action of a supplied lattice isometry group."""
            ...

        @abstractmethod
        def image_of_lattice_group(self, G: Group) -> Group:
            """Return the image of the supplied lattice group in the discriminant-form automorphism group."""
            ...

        @abstractmethod
        def kernel_of_lattice_group_action(self, G: Group) -> Group:
            """Return the kernel of the supplied lattice group action on the discriminant group."""
            ...

        @abstractmethod
        def orbit(self, x: object, G: Group | None = None) -> SetFamily:
            """Return the orbit of an element or subgroup under a supplied action, defaulting to the form isometry group."""
            ...

        @abstractmethod
        def orbits(self, G: Group | None = None) -> SetFamily:
            """Return element orbits under a supplied action, defaulting to the form isometry group."""
            ...

        @abstractmethod
        def orbits_on_subgroups(self, G: Group | None = None) -> SetFamily:
            """Return subgroup orbits under a supplied action."""
            ...

        @abstractmethod
        def orbits_on_isotropic_subgroups(self, G: Group | None = None) -> SetFamily:
            """Return isotropic-subgroup orbits under a supplied action."""
            ...
    class ElementMethods:
        @abstractmethod
        def additive_order(self) -> RingElement: ...

        @abstractmethod
        def lift(self) -> RModuleElement: ...

        @final
        def lift_to_dual(self) -> RModuleElement:
            """Lift this discriminant-group element to the covering metric dual lattice."""
            return self.parent().lift_to_dual(self)

        @final
        def coset_representative(self) -> RModuleElement:
            """Return a preferred representative of this discriminant class."""
            return self.parent().coset_representative(self)

LatticeDiscriminantGroupsObject : TypeAlias = LatticeDiscriminantGroupsCategory.ParentMethods
LatticeDiscriminantGroupsElement : TypeAlias = LatticeDiscriminantGroupsCategory.ElementMethods
LatticeDiscriminantGroupsMorphism : TypeAlias = QuadraticModulesMorphism
LatticeDiscriminantGroupsHomCategory : TypeAlias = ModulesHomCategory
LatticeDiscriminantGroupsEndCategory : TypeAlias = ModulesEndCategory
LatticeDiscriminantGroupsAutCategory : TypeAlias = ModulesAutCategory
LatticeDiscriminantGroupsHom : TypeAlias = ModulesHom
LatticeDiscriminantGroupsEnd : TypeAlias = ModulesEnd
LatticeDiscriminantGroupsAut : TypeAlias = ModulesAut
LatticeDiscriminantGroupsEndomorphism : TypeAlias = ModulesEndomorphism
LatticeDiscriminantGroupsAutomorphism : TypeAlias = ModulesAutomorphism
