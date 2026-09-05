r"""Group algebras: the free \(R\)-module on a group, multiplied by the group law.

For a ring \(R\) and a group \(G\), the group algebra \(R[G]\) is the free
\(R\)-module on the underlying set of \(G\) with the \(R\)-bilinear
multiplication extending the group law; its unit is the identity of \(G\).
The three structure maps everything downstream consumes are the group
inclusion \(G\to R[G]^{\times}\), the augmentation \(R[G]\to R\) sending
every group element to \(1\), and, for a group morphism \(H\to G\), the
induced algebra morphism \(R[H]\to R[G]\).  Reference: Lam, *A First Course
in Noncommutative Rings*, §1 and Theorem 6.1 (Maschke).
"""

from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.abstract_categories.constructions import TensorSquare
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenMultiplication,
    algebra_from_multiplication,
    algebra_homset,
)
from dzack_research.preamble.categories.algebras.augmented_algebras import AugmentedAlgebras
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.groups import (
    FiniteGroups,
    OwnedGroups,
    _owned_group,
)
from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedIntegralDomains,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


class GroupAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras of the form \(R[G]\), interned on their group.

    A data subcategory of \(R\)-algebras: an object is \(R[G]\) together with
    the group \(G\) framing it.  The multiplication is the chosen morphism
    \(R[G]\otimes_R R[G]\to R[G]\) extending the group law, and the augmentation
    is determined by the datum, so this refines both chosen-multiplication
    algebras and augmented algebras.
    """

    def an_object(self):
        r"""\(R[C_2]\), the smallest group algebra with a nontrivial group."""
        return GroupAlgebra(self.base_ring(), OwnedGroups.C(2))

    @classmethod
    def _repr_object_names(cls):
        return "group algebras"

    def super_categories(self):
        ring = self.base_ring()
        return [AlgebrasWithChosenMultiplication(ring), AugmentedAlgebras(ring)]

    class ParentMethods:
        def __init__(self, group, **rest) -> None:
            self._preamble_group = group
            super().__init__(**rest)

        def group(self):
            r"""The group \(G\) this algebra is \(R[G]\) of."""
            return self._preamble_group

        def _repr_(self):
            return f"Group algebra of {self.group()} over {self.base_ring()}"

        @cached_method
        def center(self):
            r"""The centre \(Z(R[G])\), free on the conjugacy-class sums.

            An element \(\sum a_g g\) is central exactly when \(a\) is a class
            function, so the class sums \(\sum_{h\in C} h\) over the conjugacy
            classes \(C\) of \(G\) form an \(R\)-basis of \(Z(R[G])\) (Isaacs,
            *Character Theory of Finite Groups*, Theorem 2.4).  Each class is
            the conjugation orbit of its representative.
            """
            group = self.group()
            class_sums = finite_ordered_set(
                [
                    sum(
                        self.module_generator(element)
                        for element in {
                            g * representative * g.inverse() for g in group
                        }
                    )
                    for representative in group.conjugacy_classes_representatives()
                ]
            )
            return self.subobject_on(class_sums)

        @cached_method
        def group_inclusion(self):
            r"""The monoid morphism \(G\to R[G]\), \(g\mapsto g\).

            Every image is a unit, with inverse the image of \(g^{-1}\).
            """
            return Monoids().Mor(self.group(), self)(self.module_generator)

        @cached_method
        def augmentation(self):
            r"""The algebra morphism \(\varepsilon\colon R[G]\to R\), \(g\mapsto 1\)."""
            ring = self.base_ring()
            counit = module_homset(self, ring)(
                {label: ring.one() for label in self.module_generating_set()}
            )
            return algebra_homset(self, ring)(counit)

        @cached_method
        def regular_representation(self):
            r"""``R[G]`` as a module over itself by left multiplication."""
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            return Modules(self)(self, lambda g, element: self(g) * element)

        def is_semisimple(self) -> bool:
            r"""Maschke's theorem in its ring form (Lam, FC, Theorem 6.1).

            \(R[G]\) is semisimple if and only if \(R\) is semisimple and
            \(|G|\) is a unit of \(R\).  A commutative semisimple ring is a
            finite product of fields, so an integral domain is semisimple
            exactly when it is a field.
            """
            ring = self.base_ring()
            order = self.group().cardinality()
            assert order.is_finite(), "Maschke's theorem concerns a finite group"
            match ring:
                case _ if ring in OwnedFields():
                    return bool(ring(int(order.finite_value())).is_unit())
                case _ if ring in OwnedIntegralDomains():
                    return False
                case _:
                    raise AssertionError(
                        f"semisimplicity of {ring} is decided here only for integral domains"
                    )


@cached_function
def GroupAlgebra(base_ring, group):
    r"""The group algebra \(R[G]\): the free \(R\)-module on \(G\), multiplied by the group law."""
    ring = _owned_ring(base_ring)
    group = _owned_group(group)
    assert group in FiniteGroups(), (
        "the free module on an infinite group needs a lazy framing, which this route lacks"
    )
    elements = finite_ordered_set(group)
    module = BasedFreeModule(ring, elements)
    multiplication = module_homset(TensorSquare(module), module)(
        {
            (left, right): module.module_generator(left * right)
            for left in elements
            for right in elements
        }
    )
    return algebra_from_multiplication(
        multiplication,
        ring,
        extra_categories=(GroupAlgebras(ring),),
        extra_construction_data={"group": group},
        unit=module.module_generator(group.one()),
        commutative=group.is_abelian(),
    )


class GroupAlgebraFunctor(Functor):
    r"""\(R[-]\colon \mathbf{Grp}\to \mathbf{Alg}_R\).

    On a group morphism \(f\colon H\to G\) it is the algebra morphism
    \(R[H]\to R[G]\) extending \(f\) \(R\)-linearly; for a subgroup
    inclusion this is the ring morphism \(R[H]\to R[G]\).
    """

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(OwnedGroups(), Algebras(ring))

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, group):
        return GroupAlgebra(self._base_ring, group)

    def _apply_morphism(self, group_morphism):
        source = self(group_morphism.domain())
        target = self(group_morphism.codomain())
        linear = module_homset(source, target)(
            {
                label: target.module_generator(group_morphism(label))
                for label in source.module_generating_set()
            }
        )
        return algebra_homset(source, target)(linear)

    def _repr_(self):
        return f"Group-algebra functor over {self._base_ring}"
