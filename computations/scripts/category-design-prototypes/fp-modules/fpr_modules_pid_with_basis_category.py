# Origin: gitclones/integral_lattice/FPModulesPID/fpr_modules_pid_with_basis_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, section R3). Content below is unmodified.
# This is a DESIGN RECORD; dispositions are in INDEX.md beside this file.

r"""
Category of finitely presented R-modules with a distinguished basis.
"""

from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring, all_axioms)
from sage.categories.fields import Fields
from sage.categories.functor import Functor
from sage.categories.groups import Groups
from sage.categories.homset import Hom
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.rings.localization import Localization

from .rmod_parent_methods import RModParentMethods

__all__ = ["FPRModulesPIDWithBasis"]


all_axioms += (
    "Autset",
    "Free",
    "Torsion",
    "Cyclic"
)

BaseMod = lambda R: Modules(R).FinitelyPresented().WithBasis()
PIDS = PrincipalIdealDomains()
natural_numbers = NN.element_class


class RMod(Modules):

    def __classcall_private__(cls, R, dispatch=True):
        if (
            R in Fields()
            or R in PIDS
            or (isinstance(R, Localization) and R.base_ring() in PIDS)
        ):
            return super().__classcall_private__(cls, R, dispatch)
        else:
            raise ValueError(
                f"Unable to recognize this ring as a PID: {R}"
            )

    extra_super_categories = lambda self: [BaseMod(self.base_ring())]

    # Subcategories
    DirectProducts = lambda self: self.CartesianProducts()
    DirectSums = DirectProducts

    # Functors
    DirectSum = lambda self: Functor(
        self.CartesianProducts(), self.DirectProducts()
    )
    DirectProduct = DirectSum

    # Functors
    Hom = lambda self: Functor(self.DirectSums(), self)
    End = lambda self: Functor(self, self.Homsets().Endsets())
    Aut = lambda self: Functor(self, self.Homsets().Autsets())
    Dual = lambda self: Functor(self, self.DualObjects())
    Tensor = lambda self: Functor(
        self.DirectSums(), self.TensorProducts()
    )
    
    def FreeFromSet(self, X):
        X = FiniteEnumeratedSet( Set(X) )
        F = Functor(FiniteEnumeratedSets(), self.Free())
        return F(X)
    zero = lambda self: self.FreeFromSet({})
    unit = lambda self: self.FreeFromSet({1})
    def R(self, n=0):
        return self.zero() if n==0 else self.FreeFromSet({1,..,n})

    CyclicFromRingElement = lambda self, r: self.Cyclic()(
        self.base_ring()(r)
    )

    ParentMethods = RModParentMethods

    class ElementMethods(ElementMethodsBase):
        @abstract_method
        def annihilator(self, *args, **kwargs):
            pass

        @abstract_method
        def cyclic_submodule(self, *args, **kwargs):
            pass

    class MorphismMethods:
        @abstract_method
        def kernel(self):
            pass

        @abstract_method
        def cokernel(self):
            pass

        @abstract_method
        def image(self):
            pass

        @abstract_method
        def coimage(self):
            pass

        @abstract_method
        def is_injective(self):
            pass

        @abstract_method
        def is_surjective(self):
            pass

        @abstract_method
        def is_isomorphism(self):
            pass

        @abstract_method
        def compose(self, other):
            pass

        @abstract_method
        def inverse(self):
            pass

        @abstract_method
        def lift(self, target):
            pass

    class Homsets(Modules.Homsets):
        extra_super_categories = lambda self: [
            BaseMod(self.base_ring()).Homsets(),
            RMod(self.base_ring()),
        ]

        class SubcategoryMethods:
            Endsets = lambda self: self._with_axiom("Endset")
            Autsets = lambda self: self._with_axiom("Autset")

        class Endset(CategoryWithAxiom_over_base_ring):
            extra_super_categories = lambda self: [
                RMod(self.base_ring()).Homsets()
            ]

            class ParentMethods:
                aut = lambda self: RMod(self.base_ring()).Aut(self)

        class Autset(CategoryWithAxiom_over_base_ring):
            extra_super_categories = lambda self: [
                RMod(self.base_ring()).Homsets(),
                Groups(),
            ]

            class ParentMethods:
                end = lambda self: RMod(self.base_ring()).End(self)

        class ElementMethods(ElementMethodsBase):

    class DualObjects:
        extra_super_categories = lambda self: [
            BaseMod(self.base_ring()).Homsets(),
            RMod(self.base_ring()),
        ]

    class Free:
        extra_super_categories = lambda self: [
            RMod(self.base_ring()),
        ]
        
        def __call__(self, data=None):
            if data is None:
                return self.base_category()
            X = Set(data)
            X = FiniteEnumeratedSet(data)

    class Torsion:
        extra_super_categories = lambda self: [
            RMod(self.base_ring()),
        ]

        class Cyclic:
            extra_super_categories = lambda self: [
                RMod(self.base_ring()).Torsion(),
            ]


FPRModulesPIDWithBasis = RMod
