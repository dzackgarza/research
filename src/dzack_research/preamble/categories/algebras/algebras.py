"""Associative unital algebras over an owned base ring."""

from sage.categories.commutative_algebras import (
    CommutativeAlgebras as SageCommutativeAlgebras,
)
from sage.categories.morphism import SetMorphism
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedCommutativeRings,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import _OwnedRingElement, _OwnedRingParent
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    _category_homset,
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
from dzack_research.preamble.categories.abstract_categories.products import _finite_factor_family
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BilinearMap,
    FramedModules,
    MatrixEndomorphismSpaces,
    Modules,
    TensorProductModules,
)
from dzack_research.preamble.categories.modules.tensor_products import tensor_product_morphism
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism
from dzack_research.preamble.categories.sets.cardinals import aleph0
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)


class AssociativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative \(R\)-algebras, not necessarily unital.

    An associative algebra is an \(R\)-module with an associative bilinear
    product. A unit is extra structure: the owned unital category is
    :class:`Algebras`. Convolution \(L^1(\mathbb R)\) is the standard
    non-unital example.
    """

    def an_object(self):
        r"""The base ring itself, associative over itself."""
        return self.base_ring()

    @classmethod
    def _repr_object_names(cls):
        return "associative algebras"

    def super_categories(self):

        return [Modules(self.base_ring())]

    def _call_(self, multiplication):
        return algebra_from_multiplication(
            multiplication, self.base_ring(), unital=False
        )


class AssociativeAlgebrasWithChosenMultiplication(OwnedCategoryOverBaseRing):
    r"""Associative algebras interned on a chosen morphism \(A\otimes_R A\to A\)."""

    def an_object(self):
        r"""``R`` itself, presented by a chosen multiplication.

        The rank-one free module on one label, with the multiplication
        \(e\otimes e\mapsto e\): the smallest object whose algebra structure is
        a chosen morphism rather than one inherited from a construction.
        """
        from dzack_research.preamble.categories.abstract_categories.constructions import TensorSquare
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        line = BasedFreeModule(self.base_ring(), finite_ordinal_set(1))
        label = next(iter(line.module_generating_set()))
        multiplication = module_homset(TensorSquare(line), line)(
            {(label, label): line.module_generator(label)}
        )
        return algebra_from_multiplication(multiplication)

    @classmethod
    def _repr_object_names(cls):
        return "associative algebras with chosen multiplication"

    def super_categories(self):
        return [AssociativeAlgebras(self.base_ring())]

    class ParentMethods:
        def multiplication_morphism(self):
            return self._preamble_multiplication_morphism

    class ElementMethods:
        def _mul_(self, other):
            multiplication = self.parent().multiplication_morphism()
            return multiplication(multiplication.domain().pure_tensor(self, other))


class AlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of associative unital ``R``-algebras."""

    def Of(self, domain, codomain):
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("algebra Hom endpoints must lie in the base algebra category")
        cached = self._cached_between(domain, codomain)
        if cached is not None:
            return cached

        result = domain.algebra_homset(self, codomain)
        return self._remember_between(domain, codomain, result)


class Algebras(OwnedCategoryOverBaseRing):
    r"""Associative unital algebras over ``R``.

    The structure morphism is \(\eta\colon R\to Z(A)\).  The forgetful
    functor \(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\) is
    :func:`~dzack_research.preamble.categories.functors.algebra_modules.algebra_underlying_module_functor`.
    Multiplication is the \(R\)-module morphism
    \(m\colon A\otimes_R A\to A\).
    """

    def an_object(self):
        r"""The base ring itself, an algebra over itself."""
        return self.base_ring()

    @classmethod
    def _repr_object_names(cls):
        return "algebras"

    def super_categories(self):

        return [
            OwnedRings(),
            AssociativeAlgebras(self.base_ring()),
            Modules(self.base_ring()),
        ]

    def Mor(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_{R-Alg}(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-algebra Hom requires two R-algebras")
        return self.HomCategory().Of(domain, codomain)

    _HomCategory = AlgebraHomCategoryConstruction

    class ParentMethods:
        def algebra_homset(self, hom_family, codomain):
            r"""Return the fixed-endpoint Hom carrier selected by this algebra category."""
            return AlgebraHomset(hom_family, self, codomain)

        def base_ring(self):
            return self.algebra_base_ring()

        def is_algebra(self) -> bool:
            return True

        def algebra_base_ring(self):
            base = self.__dict__.get("_preamble_algebra_base_ring")
            if base is not None:
                return base
            return _owned_ring(_engine_ring(self).base_ring())

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):
            base = self.algebra_base_ring()
            center = self.ring_center()

            return ring_morphism(
                base,
                center,
                lambda scalar: center(self(scalar)),
            )

        def _owned_scalar_multiple(self, scalar, element):
            r"""Apply the ``R``-algebra scalar action ``r*a = eta(r)a``."""
            scalar = self.base_ring()(scalar)
            element = self(element)
            scalar_image = self(self.algebra_structure_morphism()(scalar))
            return scalar_image * element

        @cached_method
        def algebra_structure_morphism(self):
            r"""The structure morphism \(\eta\colon R\to Z(A)\) of this \(R\)-algebra."""
            eta = self._ring_morphism_defining_algebra_structure()
            center = self.ring_center()
            if eta.codomain() is center:
                return eta

            return ring_morphism(eta.domain(), center, eta)

        @cached_method
        def multiplication_morphism(self):
            r"""The multiplication \(m\colon A\otimes_R A\to A\) as an \(R\)-module morphism.

            Centrality of the image of \(R\) is exactly \(R\)-bilinearity of
            the product, so \(m\) is the unique factorization of
            \((a,b)\mapsto ab\) through the tensor product.
            """
            selected = self.__dict__.get("_preamble_multiplication_morphism")
            if selected is not None:
                return selected

            ring = self.algebra_base_ring()
            module = self
            try:
                tensor = TensorProduct(module, module)
            except NotImplementedError as error:
                raise TypeError(
                    f"the multiplication morphism of {self} has no represented "
                    f"tensor-product realization by finitely presented {ring}-modules"
                ) from error
            return tensor.from_bilinear(
                BilinearMap(
                    module,
                    module,
                    module,
                    {
                        (left, right): (
                            module.module_generator(left)
                            * module.module_generator(right)
                        )
                        for left in module.module_generating_set()
                        for right in module.module_generating_set()
                    },
                )
            )

        def Mor(self, codomain, category=None):
            algebras = Algebras(self.base_ring())
            if category is None or category.is_subcategory(algebras):
                return algebras.Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(
                Algebras(self.base_ring())
            ):
                raise TypeError("this is not an algebra homset category")
            return algebra_homset(self, codomain)

    def _call_(self, multiplication):
        return algebra_from_multiplication(
            multiplication, self.base_ring(), unital=True
        )


class AlgebrasWithChosenMultiplication(OwnedCategoryOverBaseRing):
    r"""Unital algebras interned on a chosen morphism \(A\otimes_R A\to A\)."""

    def an_object(self):
        r"""``R`` itself, presented by a chosen multiplication.

        The rank-one free module on one label, with the multiplication
        \(e\otimes e\mapsto e\): the smallest object whose algebra structure is
        a chosen morphism rather than one inherited from a construction.
        """
        from dzack_research.preamble.categories.abstract_categories.constructions import TensorSquare
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        line = BasedFreeModule(self.base_ring(), finite_ordinal_set(1))
        label = next(iter(line.module_generating_set()))
        multiplication = module_homset(TensorSquare(line), line)(
            {(label, label): line.module_generator(label)}
        )
        return algebra_from_multiplication(multiplication)

    @classmethod
    def _repr_object_names(cls):
        return "algebras with chosen multiplication"

    def super_categories(self):
        return [
            AssociativeAlgebrasWithChosenMultiplication(self.base_ring()),
            Algebras(self.base_ring()),
        ]

    class ParentMethods:
        def one(self):
            return self._preamble_algebra_unit

        def multiplication_morphism(self):
            return self._preamble_multiplication_morphism

        def _owned_scalar_multiple(self, scalar, element):
            r"""Use the selected underlying module action on an interned algebra."""
            scalar = self.base_ring()(scalar)
            element = self(element)
            return element._lmul_(scalar)

        def _ring_morphism_defining_algebra_structure(self):
            base = self.algebra_base_ring()
            center = self.ring_center()
            unit = self.one()

            return ring_morphism(
                base,
                center,
                lambda scalar: center(unit._lmul_(base(scalar))),
            )


class CommutativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Commutative associative unital algebras over ``R``."""

    class SubcategoryMethods:
        r"""Constructions this category owns, reachable from any subcategory."""

        def product(self, factors):
            r"""Return the product of a finite family of objects of this category."""
            return self._fold_construction(
                self._categorical_product, factors, name="Product factors"
            )

        def _categorical_product(self, left, right):
            raise NotImplementedError(
                "the represented categorical product of commutative algebras is not yet implemented"
            )

        def coproduct(self, factors):
            r"""Return the coproduct of a finite family of objects of this category."""
            return self._fold_construction(
                self._categorical_coproduct, factors, name="Coproduct factors"
            )

        def _categorical_coproduct(self, left, right):
            operation = getattr(left, "_commutative_algebra_coproduct", None)
            if operation is None:
                operation = getattr(right, "_commutative_algebra_coproduct", None)
            if operation is None:
                raise NotImplementedError(
                    "neither factor carries a represented commutative-algebra coproduct backend"
                )
            return operation(left, right)

        def _categorical_coproduct_morphism(self, left_morphism, right_morphism, source, target):
            return source.from_cocone(
                target.left_coproduct_map() * left_morphism,
                target.right_coproduct_map() * right_morphism,
            )

        def _categorical_pushout(self, left_morphism, right_morphism):
            left = left_morphism.codomain()
            right = right_morphism.codomain()
            operation = getattr(left, "_commutative_algebra_pushout", None)
            if operation is None:
                operation = getattr(right, "_commutative_algebra_pushout", None)
            if operation is None:
                raise NotImplementedError(
                    "neither factor carries a represented commutative-algebra pushout backend"
                )
            return operation(left_morphism, right_morphism)

    _HomCategory = AlgebraHomCategoryConstruction

    def an_object(self):
        r"""The polynomial algebra on one generator."""
        from dzack_research.preamble.categories.functors.free_algebras import SymmetricAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return SymmetricAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "commutative algebras"

    def super_categories(self):

        return [Algebras(self.base_ring()), OwnedCommutativeRings()]







    class ParentMethods:
        def is_commutative(self) -> bool:
            return True


class FramedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras carrying a chosen algebra generating set."""

    def an_object(self):
        r"""The polynomial algebra on one generator, framed by it."""
        from dzack_research.preamble.categories.functors.free_algebras import SymmetricAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return SymmetricAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "framed algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def cardinality(self):
            base_cardinality = self.base_ring().cardinality()
            generator_cardinality = self.algebra_generating_set().cardinality()
            if generator_cardinality.is_countable():
                if base_cardinality.is_finite() or base_cardinality.is_countable():
                    return aleph0
                return base_cardinality
            return super().cardinality()

        def algebra_generating_set(self):
            return self._preamble_algebra_generating_set

        @cached_method
        def algebra_generators(self):

            return indexed_family(
                self.algebra_generating_set(),
                self.algebra_generator,
                name=f"Algebra generators of {self}",
            )


        def algebra_generator(self, label):
            labels = self.algebra_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not an algebra-generator label")
            return self._preamble_algebra_generator_values[label]

        def number_of_algebra_generators(self):
            return self.algebra_generating_set().cardinality()

        def product_on_algebra_generators(self, left, right):
            return self.algebra_generator(left) * self.algebra_generator(right)

        def is_central(self, element):
            r"""Decide centrality from the selected algebra generating family."""
            if element not in self:
                return False
            return all(
                element * self.algebra_generator(label)
                == self.algebra_generator(label) * element
                for label in self.algebra_generating_set()
            )


class MatrixAlgebras(OwnedCategoryOverBaseRing):
    r"""Finite matrix endomorphism Hom objects with their canonical algebra structure."""

    def an_object(self):
        r"""``End_R(Free_R([2]))``, the two-by-two matrix algebra."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        ring = self.base_ring()
        plane = FreeModuleFunctor(ring)(finite_ordinal_set(2))
        return Modules(ring).Mor(plane, plane)

    @classmethod
    def _repr_object_names(cls):
        return "matrix algebras"

    def super_categories(self):

        if self.base_ring() not in OwnedCommutativeRings():
            raise TypeError("the canonical R-algebra structure on End_R(F) needs commutative R")
        return [
            MatrixEndomorphismSpaces(self.base_ring()),
            Algebras(self.base_ring()),
            FramedAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def algebra_base_ring(self):
            return self._preamble_base_ring

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):

            ring = self.base_ring()
            center = self.ring_center()
            identity = self.identity()
            return ring_morphism(
                ring,
                center,
                lambda scalar: center(self.scalar_multiple(scalar, identity)),
            )

        def algebra_generating_set(self):
            return self._preamble_algebra_generating_set

        def algebra_generator(self, label):
            label = self.algebra_generating_set()(label)
            return self.matrix_unit(label[0], label[1])


def refine_matrix_algebra(homset):
    r"""Attach the canonical ``R``-algebra structure to a square matrix Hom object."""

    ring = homset.base_ring()
    if homset not in MatrixEndomorphismSpaces(ring):
        return homset
    if ring not in OwnedCommutativeRings():
        return homset
    homset._preamble_base_ring = ring
    homset._preamble_algebra_generating_set = homset.module_generating_set()
    return refine(homset, MatrixAlgebras(ring))


class FinitelyPresentedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras that admit a finite algebra presentation."""

    def an_object(self):
        r"""``R[x]/(x^2)``, the dual numbers: one generator and one relation."""
        from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
            FinitelyPresentedAlgebraOn,
        )

        return FinitelyPresentedAlgebraOn(self.base_ring(), ("x",), ("x^2",))

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True


class AlgebrasWithChosenFinitePresentation(OwnedCategoryOverBaseRing):
    r"""Finitely presented algebras carrying one selected finite presentation."""

    def an_object(self):
        r"""``R[x]/(x^2)``, the dual numbers: one generator and one relation."""
        from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
            FinitelyPresentedAlgebraOn,
        )

        return FinitelyPresentedAlgebraOn(self.base_ring(), ("x",), ("x^2",))

    @classmethod
    def _repr_object_names(cls):
        return "algebras with a chosen finite presentation"

    def super_categories(self):
        return [
            FinitelyPresentedAlgebras(self.base_ring()),
            FramedAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def algebra_homset(self, hom_family, codomain):
            return PresentedAlgebraHomset(hom_family, self, codomain)

        def presentation_ring(self):
            return self._preamble_presentation_ring

        def _has_selected_exact_coefficient_presentation(self) -> bool:
            return True

        def _exact_coefficient_presentation_ring(self):
            return self.presentation_ring()

        def _exact_coefficient_presentation_relations(self):
            return self.relations()

        def _lift_coefficient_to_presentation(self, value):
            return self.lift_to_presentation(self(value))

        def _descend_coefficient_from_presentation(self, value):
            return self(value)

        def relations(self):
            return self._preamble_presentation_relations

        def presentation_ideal(self):
            return self._preamble_presentation_ideal

        def presentation(self):
            return self.presentation_ring(), self.relations()

        def algebra_presentation_morphism(self):
            return self._preamble_algebra_presentation_morphism

        def lift_to_presentation(self, element):
            return self._preamble_lift_to_presentation(element)

        def base_change(self, ring_map):
            operation = self.__dict__.get("_preamble_base_change_selected_presentation")
            if operation is None:
                raise NotImplementedError(
                    "this selected algebra presentation has no represented base-change backend"
                )
            return operation(ring_map)

        def _commutative_algebra_coproduct(self, left, right):
            operation = getattr(
                self,
                "_preamble_commutative_algebra_coproduct_backend",
                None,
            )
            if operation is None:
                raise NotImplementedError(
                    "this selected presentation has no represented coproduct backend"
                )
            return operation(left, right)

        def _quotient_by_algebra_elements(self, elements):
            operation = getattr(
                self,
                "_preamble_quotient_by_algebra_elements_backend",
                None,
            )
            if operation is None:
                raise NotImplementedError(
                    "this selected presentation has no represented quotient backend"
                )
            return operation(elements)

        def _commutative_algebra_pushout(self, left_map, right_map):
            operation = getattr(
                self,
                "_preamble_commutative_algebra_pushout_backend",
                None,
            )
            if operation is None:
                raise NotImplementedError(
                    "this selected presentation has no represented pushout backend"
                )
            return operation(left_map, right_map)


class CommutativeAlgebraCoproducts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected binary coproducts."""

    def an_object(self):
        r"""``R[x] \otimes_R R[y]``, the coproduct of two polynomial algebras."""
        from dzack_research.preamble.categories.abstract_categories.constructions import Coproduct
        from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebraOn

        ring = self.base_ring()
        return Coproduct(SymmetricAlgebraOn(ring, ("x",)), SymmetricAlgebraOn(ring, ("y",)))

    def super_categories(self):
        return [CommutativeAlgebras(self.base_ring())]

    class ParentMethods:
        def coproduct_factors(self):
            r"""Return the family of factors, indexed by the product's own index set."""

            return _finite_factor_family(self._preamble_coproduct_factors, name="Coproduct factors")

        tensor_factors = coproduct_factors

        def coproduct_injection(self, index):
            return self._preamble_coproduct_injections[index]

        def coproduct_injections(self):
            return tuple(self.coproduct_injection(index) for index in range(2))

        def left_coproduct_map(self):
            return self.coproduct_injection(0)

        def right_coproduct_map(self):
            return self.coproduct_injection(1)

        def from_cocone(self, left_map, right_map):
            left, right = self.coproduct_factors()
            if left_map.domain() is not left or right_map.domain() is not right:
                raise ValueError("the cocone maps have the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the cocone maps must have one common codomain")
            target = left_map.codomain()
            images = {
                **{
                    ("left", label): left_map(left.algebra_generator(label))
                    for label in left.algebra_generating_set()
                },
                **{
                    ("right", label): right_map(right.algebra_generator(label))
                    for label in right.algebra_generating_set()
                },
            }
            return self.Mor(target)(images)

        tensor_map = from_cocone


class CommutativeAlgebraPushouts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected pushouts of one span."""

    def an_object(self):
        r"""``R[x] \otimes_{R[t]} R[y]`` for ``t`` sent to ``x`` and to ``y``.

        The pushout of the span whose legs are the two isomorphisms
        \(R[t]\to R[x]\) and \(R[t]\to R[y]\).
        """
        from dzack_research.preamble.categories.abstract_categories.constructions import Pushout
        from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebraOn

        ring = self.base_ring()
        common = SymmetricAlgebraOn(ring, ("t",))
        left = SymmetricAlgebraOn(ring, ("x",))
        right = SymmetricAlgebraOn(ring, ("y",))
        return Pushout(
            common.Mor(left)({"t": left.algebra_generator("x")}),
            common.Mor(right)({"t": right.algebra_generator("y")}),
        )

    def super_categories(self):
        return [CommutativeAlgebras(self.base_ring())]

    class ParentMethods:
        def pushout_span(self):
            return self._preamble_pushout_span

        def pushout_maps(self):
            return self._preamble_pushout_maps

        def left_pushout_map(self):
            return self.pushout_maps()[0]

        def right_pushout_map(self):
            return self.pushout_maps()[1]

        def from_pushout_cocone(self, left_map, right_map):
            source_map, target_map = self.pushout_span()
            left_factor = source_map.codomain()
            right_factor = target_map.codomain()
            if left_map.domain() is not left_factor or right_map.domain() is not right_factor:
                raise ValueError("the pushout cocone has the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the pushout cocone maps require one common codomain")
            common_source = source_map.domain()
            for label in common_source.algebra_generating_set():
                element = common_source.algebra_generator(label)
                if left_map(source_map(element)) != right_map(target_map(element)):
                    raise ValueError("the cocone does not agree on the common algebra")
            target = left_map.codomain()
            images = {
                **{
                    ("left", label): left_map(left_factor.algebra_generator(label))
                    for label in left_factor.algebra_generating_set()
                },
                **{
                    ("right", label): right_map(right_factor.algebra_generator(label))
                    for label in right_factor.algebra_generating_set()
                },
            }
            return self.Mor(target)(images)



class AlgebraMorphism(Morphism):
    r"""An ``R``-algebra morphism specified by the images of algebra generators."""

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        codomain = self.codomain()
        engine_domain = _engine_ring(domain)
        engine_codomain = _engine_ring(codomain)
        framed_domain = domain in FramedAlgebras(domain.base_ring())
        self._engine_morphism = None
        self._element_function = None

        if isinstance(images, ModuleMorphism):
            if images.domain() is not domain or images.codomain() is not codomain:
                raise ValueError(
                    "an adopted module morphism must have the owned algebra homset's "
                    "exact domain and codomain"
                )

            labels = domain.module_generating_set()
            size = labels.cardinality()
            try:
                finite = size.is_finite()
            except NotImplementedError:
                finite = False
            if not finite:
                raise NotImplementedError(
                    "verification that a module morphism is multiplicative currently "
                    "requires a finite module generating set"
                )
            if images(domain.one()) != codomain.one():
                raise ValueError("an algebra morphism must preserve the unit")
            for left_label in labels:
                left = domain.module_generator(left_label)
                for right_label in labels:
                    right = domain.module_generator(right_label)
                    if images(left * right) != images(left) * images(right):
                        raise ValueError(
                            "the adopted module morphism is not multiplicative on "
                            "the selected module generators"
                        )
            self._element_function = images
            if framed_domain:
                algebra_labels = domain.algebra_generating_set()
                self._generator_images = indexed_family(
                    algebra_labels,
                    lambda label: codomain(images(domain.algebra_generator(label))),
                    name="Algebra-morphism generator-image family",
                )
            else:
                self._generator_images = None
            return
        if isinstance(images, Map):
            if images.domain() is domain and images.codomain() is codomain:
                self._element_function = images
                if framed_domain:
                    labels = domain.algebra_generating_set()
                    self._generator_images = indexed_family(
                        labels,
                        lambda label: codomain(images(domain.algebra_generator(label))),
                        name="Algebra-morphism generator-image family",
                    )
                else:
                    self._generator_images = None
                return
            if (
                images.domain() is not engine_domain
                or images.codomain() is not engine_codomain
            ):
                raise ValueError(
                    "an algebra morphism datum must have either the owned endpoints "
                    "or their private engine endpoints"
                )
            self._engine_morphism = images
            if framed_domain:
                labels = domain.algebra_generating_set()
                self._generator_images = indexed_family(
                    labels,
                    lambda label: codomain(
                        images(engine_domain(domain.algebra_generator(label)))
                    ),
                    name="Algebra-morphism generator-image family",
                )
            else:
                self._generator_images = None
            return
        if not framed_domain:
            raise NotImplementedError(
                "an algebra morphism from an unframed domain must be supplied "
                "as an exact engine ring morphism"
            )
        labels = domain.algebra_generating_set()
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images[source_indices(label)]),
                name="Algebra-morphism generator-image family",
            )
        elif isinstance(images, dict):
            if not labels.cardinality().is_finite():
                raise TypeError(
                    "dictionary algebra-generator syntax requires a finite framing; "
                    "use a callable or indexed family for an infinite framing"
                )
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images[label]),
                name="Algebra-morphism generator-image family",
            )
        elif isinstance(images, (tuple, list)):
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError(
                    "sequence algebra-generator syntax requires a finite framing; "
                    "use a callable or indexed family for an infinite framing"
                )
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError(
                    "the number of algebra-generator images must equal the framing size"
                )
            try:
                labels.rank(labels.unrank(0)) if values else None
            except AttributeError as error:
                raise TypeError(
                    "sequence algebra-generator syntax requires a ranked framing"
                ) from error
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(values[int(labels.rank(label))]),
                name="Algebra-morphism generator-image family",
            )
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images(label)),
                name="Algebra-morphism generator-image family",
            )
        else:
            raise TypeError(
                "an algebra morphism is specified on the algebra generating set"
            )

        if engine_domain not in SageRings() or engine_codomain not in SageRings():
            raise NotImplementedError(
                "generator-defined maps with no Sage ring target are constructed "
                "through the free or chosen-presentation algebra Hom categories"
            )
        self._engine_morphism = _engine_algebra_morphism_from_generator_images(
            domain,
            codomain,
            self._generator_images,
        )

    def __call__(self, element):
        r"""Apply this owned algebra morphism to an engine-backed facade element."""
        return self._call_(element)

    def _call_(self, element):
        r"""Apply the algebra map in its represented realization."""
        if self._element_function is not None:
            return self.codomain()(self._element_function(self.domain()(element)))
        engine_morphism = self._engine_morphism_crossing()
        source = _engine_ring(self.domain())
        return self.codomain()(engine_morphism(source(element)))

    def _engine_morphism_crossing(self):
        r"""Return the private engine morphism when this map has one.

        Protected contract for bridge consumers that must construct a native
        Sage object.  An algebra morphism represented entirely in the owned
        universe deliberately has no such engine morphism.
        """
        if self._engine_morphism is not None:
            return self._engine_morphism
        return _engine_algebra_morphism(self)

    def algebra_generator_morphism(self):
        if self._generator_images is None:
            raise NotImplementedError(
                "an unframed algebra domain has no selected generator morphism"
            )
        return SetMorphism(
            Sets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def algebra_generator_images(self):
        if self._generator_images is None:
            raise NotImplementedError(
                "an unframed algebra domain has no selected generator-image family"
            )
        return self._generator_images

    def _richcmp_(self, other, op):
        r"""Decide equality from the source's chosen algebra generating set.

        Two algebra morphisms agree exactly when they agree on generators, so
        this is decidable when the source is framed and not otherwise.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, AlgebraMorphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        domain = self.domain()
        if domain not in FramedAlgebras(domain.base_ring()):
            raise NotImplementedError(
                "algebra-morphism equality requires a chosen algebra generating set"
            )
        equal = self.algebra_generator_images() == other.algebra_generator_images()
        if equal is Unknown:
            return Unknown
        return equal if op == op_EQ else not equal

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if not isinstance(other, AlgebraMorphism):
            compose = getattr(other, "_postcompose_algebra_morphism", None)
            return NotImplemented if compose is None else compose(self)
        if self._engine_morphism is not None and other._engine_morphism is not None:
            composed_engine = self._engine_morphism * other._engine_morphism
            return algebra_homset(other.domain(), self.codomain())(composed_engine)
        if other.domain() in FramedAlgebras(other.domain().base_ring()):
            return algebra_homset(other.domain(), self.codomain())(
                lambda label: self(other(other.domain().algebra_generator(label)))
            )

        if other.domain() in FramedModules(other.domain().base_ring()):
            module_map = module_homset(other.domain(), self.codomain())(
                lambda label: self(other(other.domain().module_generator(label)))
            )
            return algebra_homset(other.domain(), self.codomain())(module_map)
        return algebra_homset(other.domain(), self.codomain())(
            SetMorphism(
                Sets().Mor(other.domain(), self.codomain()),
                lambda element: self(other(element)),
            )
        )


class PresentedAlgebraMorphism(Morphism):
    r"""A map from an algebra with a chosen finite presentation.

    The map is defined on the presentation algebra, its selected relations are
    checked once, and evaluation descends by the chosen quotient projection.
    No Sage target-ring protocol is involved.
    """

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        labels = domain.algebra_generating_set()
        size = labels.cardinality()
        if not size.is_finite():
            raise ValueError("a chosen finite algebra presentation must have a finite framing")
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images[source_indices(label)]),
                name="Presented-algebra morphism generator-image family",
            )
        elif isinstance(images, dict):
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Presented-algebra morphism generator-image family",
            )
        elif isinstance(images, (tuple, list)):
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError(
                    "the number of algebra-generator images must equal the framing size"
                )
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(values[int(labels.rank(label))]),
                name="Presented-algebra morphism generator-image family",
            )
        elif callable(images):
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Presented-algebra morphism generator-image family",
            )
        else:
            raise TypeError(
                "a presented-algebra morphism is specified on its algebra generators"
            )
        self._generator_images = selected
        self._presentation_map = algebra_homset(
            domain.presentation_ring(), self.codomain()
        )(selected)
        zero = self.codomain().zero()
        for relation in domain.relations():
            if self._presentation_map(relation) != zero:
                raise ValueError(
                    "relations do not all map to zero under the stated algebra-generator images"
                )

    def algebra_generator_morphism(self):
        return SetMorphism(
            Sets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def algebra_generator_images(self):
        return self._generator_images

    def _call_(self, element):
        return self._presentation_map(self.domain().lift_to_presentation(element))

    def __call__(self, element):
        return self._call_(element)

    def _richcmp_(self, other, op):
        r"""Decide equality on the chosen algebra generators of the source.

        A morphism out of a presented algebra is determined by the images of
        those generators: its map from the presentation algebra is determined
        there, and the quotient projection is surjective.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if (
            not isinstance(other, PresentedAlgebraMorphism)
            or other.parent() is not self.parent()
        ):
            return op == op_NE
        if self is other:
            return op == op_EQ
        equal = self._generator_images == other._generator_images
        return equal if op == op_EQ else not equal

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if other.domain() not in FramedAlgebras(other.domain().base_ring()):
            return NotImplemented
        return algebra_homset(other.domain(), self.codomain())(
            lambda label: self(other(other.domain().algebra_generator(label)))
        )


class _AlgebraHomsetCommonMethods:
    r"""Shared equality protocol for represented algebra Hom parents."""

    def _from_degree_preserving_generator_map(self, images):
        r"""Construct from a structurally degree-preserving generator map."""
        return self(images)


class PresentedAlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = PresentedAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    @cached_method
    def identity(self):
        r"""Return the identity of this endomorphism Hom.

        The identity of an object needs no framing: an unframed algebra such as
        the integers regarded over themselves has no algebra generating set,
        and its identity is still the identity.  A Hom object has one identity,
        so this is cached.
        """
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        domain = self.domain()
        if domain in FramedAlgebras(domain.base_ring()):
            return self(lambda label: domain.algebra_generator(label))
        engine = _engine_ring(domain)
        return self(engine.hom(engine))


class AlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = AlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("algebra morphisms require one common base ring")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)


    def _repr_(self):
        return f"Mor_Alg({self.domain()}, {self.codomain()})"


def algebra_homset(domain, codomain) -> AlgebraHomset:
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("algebra morphisms require one common base ring")
    return Algebras(ring).Mor(domain, codomain)


@cached_function
def commutative_algebra_coproduct(left, right):
    r"""Return ``left tensor_R right``, the coproduct in commutative algebras."""
    base = left.base_ring()
    if right.base_ring() is not base:
        raise ValueError("commutative-algebra coproducts require one scalar base")
    return CommutativeAlgebras(base)._categorical_coproduct(left, right)


@cached_function
def commutative_algebra_pushout(left_map, right_map):
    r"""Return the pushout of two commutative-algebra maps with common domain."""
    return CommutativeAlgebras(left_map.domain().base_ring())._categorical_pushout(
        left_map,
        right_map,
    )


class OwnedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras carrying their chosen structure map ``R -> Z(A)``."""

    def an_object(self):
        r"""The polynomial algebra on one generator."""
        from dzack_research.preamble.categories.functors.free_algebras import SymmetricAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return SymmetricAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "owned algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def _ring_morphism_defining_algebra_structure(self):
            return self._preamble_structure_map


class _OwnedAlgebraElement(_OwnedRingElement):
    r"""Engine-backed owned algebra element with ring multiplication syntax."""

    def __mul__(self, other):
        return _OwnedRingElement.__mul__(self, other)

    def __rmul__(self, other):
        return _OwnedRingElement.__rmul__(self, other)


class _OwnedAlgebraParent(_OwnedRingParent):
    r"""One ring read as an algebra through one specified scalar map."""

    Element = _OwnedAlgebraElement

    def __init__(
        self,
        engine,
        base_ring,
        labels,
        structure_map,
        generator_values=None,
    ) -> None:
        self._preamble_algebra_base_ring = _owned_ring(base_ring)
        self._preamble_algebra_generating_set = (
            None if labels is None else finite_ordered_set(labels)
        )
        self._preamble_structure_map = structure_map
        _OwnedRingParent.__init__(self, engine)
        if labels is None:
            if generator_values is not None:
                raise ValueError(
                    "an unframed algebra cannot carry framed generator values"
                )
            self._preamble_algebra_generator_values = None
            return


        selected_labels = self._preamble_algebra_generating_set
        label_size = selected_labels.cardinality()
        if not label_size.is_finite():
            raise TypeError(
                "an engine-backed framed algebra requires a finite backend generator set"
            )

        if generator_values is None:
            def value(label):
                position = int(selected_labels.rank(label))
                return self._from_engine_element(engine.gen(position))
        else:
            if hasattr(generator_values, "index_set") and callable(
                getattr(generator_values, "value", None)
            ):
                if generator_values.cardinality() != label_size:
                    raise ValueError(
                        "the number of algebra-generator values must equal the framing size"
                    )
                value = lambda label: self(
                    generator_values.value(selected_labels.rank(label))
                )
            elif callable(generator_values):
                def value(label):
                    raw = generator_values(label)
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            elif isinstance(generator_values, (tuple, list)):
                if len(generator_values) != int(label_size.finite_value()):
                    raise ValueError(
                        "the number of algebra-generator values must equal the framing size"
                    )
                # Explicit finite ingress is parsed by position; the Python
                # sequence is not retained as the mathematical family.
                by_position = {
                    position: generator_values[position]
                    for position in range(len(generator_values))
                }

                def value(label):
                    raw = by_position[int(selected_labels.rank(label))]
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            else:
                raise TypeError(
                    "algebra-generator values are a callable/indexed family or explicit finite ingress"
                )

        self._preamble_algebra_generator_values = indexed_family(
            selected_labels,
            value,
            name=f"Algebra generator values of {self}",
        )


def _default_structure_map(base, algebra):
    center = algebra.ring_center()

    return ring_morphism(
        base,
        center,
        lambda scalar: algebra(scalar),
    )


@cached_function
def _owned_algebra_view(engine, base_ring, labels=None):
    base = _owned_ring(base_ring)
    # Construct the parent first with a temporary engine-level map argument;
    # the public map is replaced immediately below once the parent exists.
    engine_map = engine.coerce_map_from(_engine_ring(base))
    view = _OwnedAlgebraParent(engine, base, labels, engine_map)
    view._preamble_structure_map = _default_structure_map(base, view)
    return view


def refine_algebra(algebra, base_ring, labels=None, *categories):
    r"""Place a native algebra in its owned algebra categories."""
    base = _owned_ring(base_ring)
    algebra = _owned_algebra_view(_engine_ring(algebra), base, labels)
    placement = [Algebras(base), OwnedAlgebras(base)]
    if _engine_ring(algebra) in SageCommutativeAlgebras(_engine_ring(base)):
        placement.append(CommutativeAlgebras(base))
    if labels is not None:
        placement.append(FramedAlgebras(base))
    placement.extend(categories)
    return refine(algebra, placement)


def _require_endomorphism_multiplication(multiplication, ring):
    from sage.categories.map import Map

    if not isinstance(multiplication, Map):
        raise TypeError(
            "an algebra is presented by an R-module morphism A tensor_R A -> A"
        )
    module = multiplication.codomain()
    if _owned_ring(module.base_ring()) is not ring:
        raise TypeError(f"the multiplication morphism is not a map of {ring}-modules")
    domain = multiplication.domain()
    try:
        left, right = domain.tensor_factors()
    except AttributeError as error:
        raise TypeError(
            "the domain of a multiplication morphism is the tensor square of the module"
        ) from error
    if left is not module or right is not module:
        raise TypeError("the multiplication morphism must be a map A tensor_R A -> A")
    return module


def _module_presented_by_multiplication(module):
    from sage.rings.infinity import Infinity

    ring = _owned_ring(module.base_ring())
    labels = module.module_generating_set()
    if labels.cardinality() == Infinity:
        raise TypeError(
            "the multiplication internment requires a finite module generating set"
        )
    constructor = getattr(module, "_same_presentation_module", None)
    if constructor is None:
        raise TypeError(
            "the multiplication internment requires a represented finite module presentation"
        )
    return constructor(labels)


def _unit_from_multiplication(multiplication):
    from sage.matrix.constructor import matrix as sage_matrix
    from sage.modules.free_module_element import vector as sage_vector

    module = multiplication.codomain()
    tensor_square = multiplication.domain()
    labels = module.module_generating_set()
    size = labels.cardinality()
    if not size.is_finite():
        raise TypeError("a unit is recovered from a finite module generating set")
    ring = module.base_ring()
    engine = _engine_ring(ring)
    rank = int(size.finite_value())

    # Private finite linear-system serialization.  The mathematical basis stays
    # the owned ordered framing ``labels``; only this backend array is concrete.
    system_entries = [
        [engine.zero() for _ in range(rank)] for _ in range(rank * rank)
    ]
    target_entries = [engine.zero() for _ in range(rank * rank)]
    for right_index in range(rank):
        right_label = labels.unrank(right_index)
        target_entries[right_index * rank + right_index] = engine.one()
        for left_index in range(rank):
            left_label = labels.unrank(left_index)
            product = multiplication(
                tensor_square.pure_tensor(
                    module.module_generator(left_label),
                    module.module_generator(right_label),
                )
            )
            coefficients = module_coefficients(product, module)
            for out_index in range(rank):
                out_label = labels.unrank(out_index)
                system_entries[right_index * rank + out_index][left_index] = _engine_element(
                    ring, coefficients.get(out_label, ring.zero())
                )
    system = sage_matrix(engine, rank * rank, rank, system_entries)
    target = sage_vector(engine, target_entries)
    try:
        coefficients = system.solve_right(target)
    except (ValueError, ArithmeticError) as error:
        raise TypeError("the multiplication morphism has no left unit") from error
    unit = module.linear_combination(
        {
            labels.unrank(index): ring._from_engine_element(engine(coefficients[index]))
            for index in range(rank)
            if coefficients[index]
        }
    )
    for label in labels:
        generator = module.module_generator(label)
        if multiplication(tensor_square.pure_tensor(generator, unit)) != generator:
            raise TypeError("the multiplication morphism has no two-sided unit")
    return unit


def _multiplication_is_commutative(multiplication) -> bool:
    module = multiplication.codomain()
    tensor = multiplication.domain()
    labels = module.module_generating_set()
    for left in labels:
        for right in labels:
            left_element = module.module_generator(left)
            right_element = module.module_generator(right)
            if multiplication(
                tensor.pure_tensor(left_element, right_element)
            ) != multiplication(tensor.pure_tensor(right_element, left_element)):
                return False
    return True


def algebra_from_multiplication(multiplication, base_ring=None, unital=True):
    r"""Return the algebra presented by an \(R\)-module morphism \(A\otimes_R A\to A\)."""
    from sage.categories.map import Map

    module = multiplication.codomain()
    ring = _owned_ring(module.base_ring() if base_ring is None else base_ring)
    if not isinstance(multiplication, Map):
        specialized = getattr(module, "algebra_from_multiplication", None)
        if specialized is None:
            raise TypeError(
                "a non-module-morphism multiplication requires its module to own the algebra construction"
            )
        return specialized(multiplication, unital=unital)


    module = _require_endomorphism_multiplication(multiplication, ring)
    if multiplication.domain() not in TensorProductModules(ring):
        specialized = getattr(module, "algebra_from_multiplication", None)
        if specialized is None:
            raise TypeError(
                "a multiplication outside the represented tensor-product category requires its module to own the algebra construction"
            )
        return specialized(multiplication, unital=unital)
    algebra = _module_presented_by_multiplication(module)
    labels = module.module_generating_set()
    forget = module_homset(algebra, module)(
        {label: module.module_generator(label) for label in labels}
    )
    equip = module_homset(module, algebra)(
        {label: algebra.module_generator(label) for label in labels}
    )
    source_tensor = TensorProduct(algebra, algebra)
    transported = tensor_product_morphism(
        forget,
        forget,
        source=source_tensor,
        target=multiplication.domain(),
    )
    algebra._preamble_multiplication_morphism = equip * multiplication * transported
    algebra._preamble_algebra_base_ring = ring
    placement = [AssociativeAlgebrasWithChosenMultiplication(ring)]
    if unital:
        if module in Algebras(ring):
            unit_source = module.one()
        else:
            unit_source = _unit_from_multiplication(multiplication)
        algebra._preamble_algebra_unit = equip(unit_source)
        placement.extend(
            [
                Algebras(ring),
                AlgebrasWithChosenMultiplication(ring),
            ]
        )
        if _multiplication_is_commutative(multiplication):
            placement.append(CommutativeAlgebras(ring))
    return refine(algebra, placement)


@cached_function
def own_algebra(structure_map):
    r"""Return the algebra object presented by the supplied ring map."""
    if not isinstance(structure_map, Map):
        raise TypeError("an algebra is presented by a ring map")
    base = _owned_ring(structure_map.domain())
    engine = _engine_ring(structure_map.codomain())
    algebra = _OwnedAlgebraParent(engine, base, None, structure_map)
    return refine(algebra, [Algebras(base), OwnedAlgebras(base)])


def _engine_algebra_morphism_from_generator_images(
    domain, codomain, generator_images
):
    r"""Realize a framed owned algebra map in Sage when both engines exist.

    This is a private bridge boundary.  The mathematical datum is the owned
    generator map; Sage receives only engine endpoints and engine elements.
    """
    engine_domain = _engine_ring(domain)
    engine_codomain = _engine_ring(codomain)
    if engine_domain not in SageRings() or engine_codomain not in SageRings():
        raise NotImplementedError(
            "this algebra morphism has no native Sage ring realization"
        )
    labels = domain.algebra_generating_set()
    if not labels.cardinality().is_finite():
        raise NotImplementedError(
            "the private Sage algebra-morphism realization requires a finite generator framing"
        )

    base = domain.base_ring()
    engine_base = _engine_ring(base)
    target_structure = codomain._ring_morphism_defining_algebra_structure()

    def engine_base_image(scalar):
        owned_scalar = base._from_engine_element(engine_base(scalar))
        return _engine_element(codomain, target_structure(owned_scalar))

    base_map = SetMorphism(
        engine_base.Hom(engine_codomain),
        engine_base_image,
    )
    engine_generator_images = {
        label: _engine_element(codomain, codomain(image))
        for label, image in generator_images.items()
    }

    scalar_labels_method = getattr(domain, "restricted_scalar_generator_labels", None)
    algebra_labels_method = getattr(domain, "restricted_algebra_generator_labels", None)
    if scalar_labels_method is not None and algebra_labels_method is not None:
        scalar_labels = tuple(domain.restricted_scalar_generator_labels())
        algebra_labels = tuple(domain.restricted_algebra_generator_labels())
        extension_engine = _engine_ring(domain.extension_ring())
        extension_map = _engine_morphism_from_generator_images(
            extension_engine,
            engine_codomain,
            [engine_generator_images[("scalar", label)] for label in scalar_labels],
            base_map,
        )
        return _engine_morphism_from_generator_images(
            engine_domain,
            engine_codomain,
            [engine_generator_images[("algebra", label)] for label in algebra_labels],
            extension_map,
        )

    return _engine_morphism_from_generator_images(
        engine_domain,
        engine_codomain,
        [engine_generator_images[label] for label in labels],
        base_map,
    )


def _engine_algebra_morphism(morphism):
    r"""Return a private Sage realization of an owned algebra morphism.

    Bridge consumers such as affine ``Spec`` use this function.  It is not a
    public method on the mathematical morphism.
    """
    if isinstance(morphism, AlgebraMorphism) and morphism._engine_morphism is not None:
        return morphism._engine_morphism
    domain = morphism.domain()
    if domain not in FramedAlgebras(domain.base_ring()):
        raise NotImplementedError(
            "a Sage realization of this unframed algebra morphism is not represented"
        )
    images = {
        label: morphism(domain.algebra_generator(label))
        for label in domain.algebra_generating_set()
    }
    return _engine_algebra_morphism_from_generator_images(
        domain, morphism.codomain(), images
    )


def _engine_morphism_from_generator_images(engine_domain, engine_codomain, images, base_map):
    r"""Construct a native Sage ring morphism at the engine boundary."""
    if engine_domain not in SageRings() or engine_codomain not in SageRings():
        raise NotImplementedError(
            "a native engine ring morphism requires native Sage ring endpoints"
        )
    return engine_domain.hom(
        [engine_codomain(image) for image in images],
        engine_codomain,
        base_map=base_map,
    )


def finite_algebra_generators(algebra):
    r"""Return the chosen finite algebra generating family, when represented."""
    if algebra not in FramedAlgebras(algebra.algebra_base_ring()):
        raise NotImplementedError(
            f"{algebra} carries no chosen finite algebra generating set"
        )
    if not algebra.algebra_generating_set().cardinality().is_finite():
        raise NotImplementedError(
            f"{algebra} has an infinite chosen algebra generating set"
        )
    return tuple(algebra.algebra_generators())


__all__ = [
    "AlgebraHomset",
    "AlgebraMorphism",
    "Algebras",
    "AlgebrasWithChosenFinitePresentation",
    "AlgebrasWithChosenMultiplication",
    "AssociativeAlgebras",
    "AssociativeAlgebrasWithChosenMultiplication",
    "CommutativeAlgebraCoproducts",
    "CommutativeAlgebraPushouts",
    "CommutativeAlgebras",
    "FinitelyPresentedAlgebras",
    "FramedAlgebras",
    "OwnedAlgebras",
    "algebra_from_multiplication",
    "algebra_homset",
    "commutative_algebra_coproduct",
    "commutative_algebra_pushout",
    "finite_algebra_generators",
    "own_algebra",
    "refine_algebra",
]
