# Origin: gitclones/integral_lattice/FPModules/finitely_presented_modules_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, section R3). Content below is unmodified.
# This is a DESIGN RECORD; dispositions are in INDEX.md beside this file.

"""
Finitely presented modules over a PID arise as cokernels of morphisms
R^m -> R^n; we track these via their defining presentation matrices.
"""

from functools import reduce

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category_with_axiom import \
    CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.categories.functor import ForgetfulFunctor, Functor
from sage.categories.modules import Modules
from sage.categories.rings import Rings
from sage.categories.sets_cat import Sets
from sage.categories.tensor import TensorProductsCategory
from sage.misc.abstract_method import abstract_method
from sage.sets.set import Set

Sets = Sets()
FiniteSets = Sets().Finite()
FESets = Sets().Finite().Enumerated()

class FinitelyPresentedModules(CategoryWithAxiom_over_base_ring):
    __slots__ = ()

    def super_categories(self):
        return [Modules(self.base_ring()).FinitelyPresented()]

    def example(self, *args, **kwargs):
        return self.FreeFromSet(Set({1, 2, 3}))

    FreeFromFiniteEnumeratedSetFunctor = Functor(
        Sets().Finite().Enumerated(), self.Free()
    )
    FreeFromSetsFunctor = Functor(
        Sets(), Sets().Finite().Enumerated()
    ).compose(
        self.FreeFromSetsFunctor
    )
    
    # Todo: should return the list of free generators AND torsion generators, ordered.
    ForgetToEnumeratedSetFunctor = Functor(
        self.category(), Sets().Finite().Enumerated()
    )

    ForgetToSetFunctor = ForgetToEnumeratedSet.compose(
            Functor(
                Sets().Finite().Enumerated(), Sets()
            )
        )

    def FreeFunctor(self, X):
        if X in Sets().Finite().Enumerated():
            return self.FreeFromFiniteEnumeratedSetFunctor(X)
        else:
            return self.FreeFromSetsFunctor(X) if X in Sets() else self.FreeFromSetsFunctor(Set(X))

    def ForgetfulFunctor(self, X, as_enumerated_set=True):
        C = self.category()
        return self.ForgetToEnumeratedSet(C(X)) if as_enumerated_set else self.ForgetToSet(C(X))

    def BaseChangeFunctor(self, target_ring):
        assert target_ring in Rings()
        C = self.category()
        return Functor(C, FinitelyPresentedModules(target_ring))

    def BaseChange(self, target_ring):
        F = self.BaseChangeFunctor(target_ring)
        return F(self)

    def _call_(self, data = None):
        """
        Construct a finitely presented module from presentation data.
        """
        from sage.matrix.constructor import matrix

        Free = self.FreeFromSet()
        Cyclic = self.Torsion().Cyclic()
        R = self.base_ring()
        assert R in PIDs()

        if isinstance(data, (int, Integer, NN.element_class)):
            # data = 3
            data = NN(data)
            return self.R(n)
        elif data in Ring.Elements():
            # data = QQ[i](I)
            data = self.base_ring(data)
            return Cyclic(data)
        elif isinstance(data, FreeModule):
            # data = ZZ^n
            n = data.rank()
            return self.R(n)
        elif isinstance(data, Matrix):
            # data = matrix(QQ, 2, [0,1,1,0])
            # Interpret as a relations matrix and compute cokernel.
            data = matrix(R, data) 
            return self.from_relations_matrix(data)
        elif data in Sets():
            data = Set(data)
            return Free(data)
        else:
            raise ValueError(f"Unknown input type: {data}, {type(data)}".)

    def from_relations_matrix(self, M: Matrix):
            R = self.base_ring()
            Free = self.FreeFromSet()
            Cyclic = self.Torsion().Cyclic()
            D = M.smith_form()[1].diagonal()
            free_rank = len(
                [entry for entry in D if entry == 0]
            )
            torsion_entries = [
                entry for entry in D if entry != 0
            ]
            components = [Free({1,..,free_rank})] + [
                Cyclic(r) for r in torsion_entries
            ]
            return reduce(lambda A, B: A.direct_sum(B), components)

    def R(self, n = 0):
        assert n in NN
        return self.Free({0}) if n == 0 else self.Free({1,..,n})

    def zero_object(self):
        return self.R(0)

    def unit_object(self):
        return self.R(1)
    
    def canonical_representation(self, A):
        return A.presentation_matrix()

    def tensor(self, A, B):
        Af, Bf = A.free_part(), B.free_part()
        At, Bt = A.torsion_part(), B.torsion_part()
        F = self.Free().tensor( Af, Bf )
        T0 = self.Torsion().tensor(
            A.torsion_part(), B.torsion_part()
        )
        TA = sum(Af.rank() * [At])
        TB = sum(Af.rank() * [Bt])
        T = sum([T0, TA, TB])

        return self.direct_sum(F, T)

    def Hom(self, A, B):
        pass

    class SubcategoryMethods:
        # Hom-based subcategories
        def Homsets(self):
            return FinitelyPresentedModules.Homsets.category_of(self)

        def Endsets(self):
            return self.Homsets()._with_axiom("Endset")

        def Autsets(self):
            return self.Endsets()._with_axiom("Autset")

        # Functorial constructions
        def TensorProducts(self):
            return (
                FinitelyPresentedModules.TensorProducts.category_of(
                    self
                )
            )

        def DirectSums(self):
            return FinitelyPresentedModules.DirectSums.category_of(
                self
            )

        def DualObjects(self):
            return FinitelyPresentedModules.DualObjects.category_of(
                self
            )

        # Axiom-driven refinements
        def Filtered(self):
            return self._with_axiom("Filtered")

        def Graded(self):
            return self._with_axiom("Graded")

        def Super(self):
            return self._with_axiom("Super")

        def Torsion(self):
            return self._with_axiom("Torsion")

        def Finite(self):
            return self._with_axiom("Finite")

        def WithGenerators(self):
            return self._with_axiom("WithGenerators")

        def Free(self):
            return self._with_axiom("Free")

    class ParentMethods:

        @abstract_method
        def _underlying_set(self) -> Set:
            pass

        @abstract_method
        def _invariant_factors(self) -> Tuple[RingElement]:
            pass

        @abstract_method
        def _presentation_matrix(self) -> Matrix:
            pass

        # Submodule/quotient builders
        @abstract_method
        def submodule(self, other):
            pass

        @abstract_method
        def quotient_module(self, submodule):
            pass

        # Structure tests and decompositions
        def is_zero(self):
            return self.is_isomorphic( self.category().zero_object() )

        def is_torsion(self) -> bool:
            return self.torsion_part().is_isomorphic(self)

        def is_free(self) -> bool:
            return self.free_part().is_isomorphic(self)

        def is_torsionfree(self) -> bool:
            return self.torsion_part().is_zero()

        @abstract_method
        def free_part(self):
            pass

        @abstract_method
        def torsion_part(self):
            pass

        def is_isomorphic(self, other):
            return (
                self.free_part().is_isomorphic(other.free_part()) and
                self.torsion_part().is_isomorphic(other.torsion_part()) and
            )

        # Tensor constructions
        def tensor(self, other):
            if other in Rings():
                return self.base_change(other)
            if other in FinitelyPresentedModules():
                F = self.free_part().tensor(other.free_part())
                T = self.torsion_part().tensor(other.torsion_part())
                return RMod( (F, T) )
            
        def direct_sum(self, *modules, **kwargs):
            F = self.free_part().direct_sum(other.free_part())
            T = self.torsion_part().direct_sum(other.torsion_part())
            return RMod( (F, T) )

        def dual(self):
            return self.Hom(self.base_ring())

        def Hom(self, other):
            Hom_F = self.free_part().Hom(other.free_part())
            Hom_F = self.torsion_part().Hom(other.torsion_part())
            return Hom_F.direct_sum(Hom_T)

        def End(self):
            return self.Hom(self, self)

        def Aut(self):
            return self.End().units()

        def base_change(self, new_ring) -> FinitelyPresentedModule:
            return RMod( matrix(new_ring, self._relations_matrix) )

        @abstract_method
        def multiplication_morphism(self, r ) -> End.Element:
            R = self.bsae_ring()
            return self.End()( lambda x: R(r)*x )

        @abstract_method
        def gens(self) -> Tuple[FinitelyPresentedModule.Element]:
            pass

        def _first_ngens(self, n) -> Tuple[FinitelyPresentedModule.Element]:
            return self.gens()[0:n]

        def __add__(self, other) -> FinitelyPresentedModule.DirectSum:
            return self.direct_sum(other)

        def __radd__(self, other) -> FinitelyPresentedModule.DirectSum:
            return self.direct_sum(other)

        def __mul__(self, other) -> FinitelyPresentedModule.TensorProducts
            R = self.base_ring()
            C = self.category()
            if other in Rings().Element() 
                return self.submodule( R(other) )
            if other in FinitelyPresentedModules()
                return self.tensor(other)

        def __rmul__(self, other):
            return self.__mul__(other)

        # Basic algebraic data
        @abstract_method
        def zero(self):
            return self(0)

        @abstract_method
        def invariant_factors(self):
            pass

        @abstract_method
        def an_element(self):
            pass

        @abstract_method
        def random_element(self, *args, **kwargs):
            pass

        @abstract_method
        def elements(self):
            pass

        @abstract_method
        def generators(self):
            pass

        @abstract_method
        def relations(self):
            pass

        def identity_morphism(self):
            return self.End().identity()

        # Power operations
        @abstract_method
        def symmetric_power(self, k):
            pass

        @abstract_method
        def exterior_power(self, k):
            pass

        @abstract_method
        def alternating_power(self, k):
            pass

        def __pow__(self, k):
            if k in Modules.HomSets():
                return Modules.Hom(k, self)
            elif k in ZZ:
                if k == 0:
                    return self.category().unit_object()
                elif k >= 1:
                    return reduce(
                        lambda A,B: RMod.tensor(A, B), k * [self]
                    )
                elif k <= -1:
                    return reduce(
                        lambda A,B: RMod.tensor(A, B), k * [self.dual()]
                    )
            elif k in NN^2:
                a, b = k
                return RMod.tensor( 
                    self.tensor_power(a), self.dual().tensor_power(b) 
                )
            else:
                raise ValueError(f"Unknown exponential: {k}")


        def tensor_power(self, k):
            assert k in NN
            # Todo: handle -k in NN with duals
            return reduce(
                    lambda A, B: RMod.tensor(A, B), k * [self]
            )

        def sum_power(self, k):
            assert k in NN
            # Todo: define when -k in NN.
            return reduce(
                    lambda A, B: RMod.direct_sum(A, B), k * [self]
            )

        # Algebra constructions
        @abstract_method
        def tensor_algebra(self, **kwargs):
            pass

        @abstract_method
        def symmetric_algebra(self, **kwargs):
            pass

        @abstract_method
        def exterior_algebra(self, **kwargs):
            pass

        @abstract_method
        def alternating_algebra(self, **kwargs):
            pass

    class ElementMethods:
        @abstract_method
        def annihilator(self, *args, **kwargs):
            pass

        @abstract_method
        def cyclic_submodule(self, *args, **kwargs):
            pass

    class Homsets(Modules.Homsets):
        class ParentMethods(Modules.Homsets.ParentMethods):
            @abstract_method
            def tensor_hom_adjunction(self, *args, **kwargs):
                A, B = self.domain(), self.codomain()
                assert A in Modules.TensorProducts() and 
                    B in Modules.HomSets()
                fs = A.tensor_factors()
                assert len(fs) >= 2
                A1, A2 = fs[0:-2], fs[-1]
                return Modules.Hom(A1, Modules.Hom(A2, B))

        ElementMethodsBase = getattr(
            Modules.Homsets, "ElementMethods", object
        )

        class ElementMethods(ElementMethodsBase):
            pass

        class Endset(Modules.Homsets.Endset):
            class SubcategoryMethods:
                def Autsets(self):
                    return self._with_axiom("Autset")

                @abstract_method
                def units(self):
                    return 

            class Autset(CategoryWithAxiom_over_base_ring):
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

    class DirectSums(CartesianProductsCategory):
        class ParentMethods:
            pass

        class ElementMethods:
            pass

        class MorphismMethods:
            @abstract_method
            def canonical_projection(self, index):
                pass

            @abstract_method
            def canonical_inclusion(self, index):
                pass

    class TensorProducts(TensorProductsCategory):
        class ParentMethods:
            @abstract_method
            def from_tensor_type(self, tensor_type, *args, **kwargs):
                pass

        class ElementMethods:
            pass

    class DualObjects(DualObjectsCategory):
        def super_categories(self):
            return [self.base_category().Homsets()]

        class ParentMethods:
            pass

        class ElementMethods:
            pass

    class Free(CategoryWithAxiom_over_base_ring):
        @abstract_method
        def __call__(self, set_obj, **kwargs):
            pass

        class Homsets(Modules.Homsets):
            @abstract_method
            def __call__(self, set_morphism, **kwargs):
                pass

        class MorphismMethods:
            @abstract_method
            def to_matrix(self, *args, **kwargs):
                pass

        class ElementMethods(Modules.ElementMethods):
            @abstract_method
            def to_vector(self, **kwargs):
                pass

        class ParentMethods:
            @abstract_method
            def rank(self):
                pass

            @abstract_method
            def standard_generator_e(self, i):
                pass

            def __eq__(self, other):
                if self.category() is not other.category():
                    return False
                forget = self.category().ForgetToSetFunctor()
                return forget(self) == forget(other)

            @abstract_method
            def from_finite_ordered_set(self, ordered_set, **kwargs):
                pass

            def is_isomorphic(self, other):
                if self.category() is not other.category():
                    return False
                forget = self.category().ForgetToSetFunctor()
                return forget(self) == forget(other)

    class Torsion(CategoryWithAxiom_over_base_ring):
        class SubcategoryMethods:
            def Cyclic(self):
                return FinitelyPresentedModules.Torsion.Cyclic.category_of(
                    self
                )

        class Cyclic(CategoryWithAxiom_over_base_ring):
            def super_categories(self):
                return [self.base_category(), Rings(self.base_ring())]

            def __call__(self, element: RingElement) -> object:
                """Return the cyclic quotient module ``R / (element)``."""
                R = self.base_ring()
                r_element = R(element)
                ideal = R.ideal(r_element)
                return R.quotient(ideal)

    class Finite(CategoryWithAxiom_over_base_ring):
        pass

    class WithGenerators(CategoryWithAxiom_over_base_ring):
        pass

    class Filtered(CategoryWithAxiom_over_base_ring):
        pass

    class Graded(CategoryWithAxiom_over_base_ring):
        pass

    class Super(CategoryWithAxiom_over_base_ring):
        pass
