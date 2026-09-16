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

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenMultiplication,
    UnitalMultiplicativeAlgebraMorphism,
    _algebra_element_in_module,
    _unit_morphism_from_element,
)
from dzack_research.preamble.categories.algebras.augmented_algebras import (
    AugmentedAlgebras,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.groups import (
    FiniteGroups,
    OwnedGroups,
    _owned_group,
)
from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap, Modules

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedIntegralDomains,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.refine import refine


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
        return self.base_ring()[OwnedGroups.C(2)]

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
            assert group in FiniteGroups(), (
                "the represented conjugacy-class-sum basis of a group-algebra center "
                "requires a finite group"
            )
            module = self.underlying_module()
            class_sums = finite_ordered_set(
                [
                    sum(
                        module.module_generator(element)
                        for element in {
                            g * representative * g.inverse() for g in group
                        }
                    )
                    for representative in group.conjugacy_classes_representatives()
                ]
            )
            return module.subobject_on(class_sums)

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
            target_module = Algebras(ring).underlying_module()(ring)
            source_module = self.underlying_module()
            counit = source_module.module_category().Mor(source_module, target_module)(
                {
                    label: target_module(ring.one())
                    for label in self.module_generating_set()
                }
            )
            return Algebras(self.base_ring()).Associative().Unital().Mor(self, ring)(counit)

        @cached_method
        def regular_representation(self):
            r"""``R[G]`` as a module over itself by left multiplication.

            The algebra object and its coefficient-module carrier are distinct
            objects: ``Alg_R -> Mod_R`` is the represented forgetful functor,
            not a category-inclusion edge.  Linearize left multiplication on
            that exact carrier, then let ``Modules(R[G])`` equip the resulting
            group action with the group-algebra scalar action.
            """
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            carrier = self.underlying_module()
            inclusion = self.group_inclusion()

            def left_action(group_element, element):
                product = inclusion(group_element) * self(element)
                return _algebra_element_in_module(self, carrier, product)

            return Modules(self)(carrier, left_action)

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
def _group_algebra(base_ring, group):
    r"""The group algebra \(R[G]\): the free \(R\)-module on \(G\), multiplied by the group law."""
    ring = _owned_ring(base_ring)
    group = _owned_group(group)
    module = ring.free_module(group)
    tensor_square = Modules(ring).tensor_product((module, module))
    multiplication = tensor_square.from_bilinear(
        BilinearMap(
            module,
            module,
            module,
            lambda left, right: module.module_generator(left * right),
        )
    )
    unit_element = module.module_generator(group.one())
    unit = _unit_morphism_from_element(module, unit_element, ring)

    # The group law already decides the multiplication before the object is
    # refined into the ring category: R[G] is commutative exactly when R and
    # G are commutative.  Retain that defining datum before the unital
    # refinement reaches OwnedRings; its construction hook legitimately asks
    # the algebra for commutativity.  No finite enumeration of G is involved.
    algebra = Algebras(ring)(module, multiplication)
    algebra._preamble_multiplication_morphism = multiplication
    algebra._preamble_algebra_is_commutative = bool(
        ring.is_commutative() and group.is_abelian()
    )
    algebra = Algebras(ring).Associative().Unital()(algebra, unit)
    algebra._preamble_group = group
    refine(algebra, GroupAlgebras(ring))
    if algebra.is_commutative():
        refine(algebra, Algebras(ring).Associative().Unital().Commutative())
    return algebra


class GroupAlgebraMorphism(UnitalMultiplicativeAlgebraMorphism):
    r"""The algebra map ``R[H] -> R[G]`` induced by a represented group map.

    The multiplication law is not re-decided by equality of two linear maps on
    the (possibly infinite) basis ``H``.  A group morphism already satisfies
    ``f(hk)=f(h)f(k)`` and ``f(1)=1``; extending its basis map ``R``-linearly is
    therefore the unique unital algebra morphism of group algebras.
    """

    def __init__(self, parent, group_morphism) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        target = self.codomain()
        if group_morphism.domain() is not source.group():
            raise ValueError("the group map has the wrong source group algebra")
        if group_morphism.codomain() is not target.group():
            raise ValueError("the group map has the wrong target group algebra")

        source_module = source.underlying_module()
        target_module = target.underlying_module()
        linear = source_module.module_category().Mor(source_module, target_module)(
            lambda label: target_module.module_generator(group_morphism(label))
        )
        source_multiplication = source.multiplication_morphism()
        target_multiplication = target.multiplication_morphism()
        self._underlying_morphism = linear
        self._tensor_square_morphism = linear.tensor_product_map(
            linear,
            source=source_multiplication.domain(),
            target=target_multiplication.domain(),
        )

        source_identity = source_module.module_generator(source.group().one())
        target_identity = target_module.module_generator(target.group().one())
        if linear(source_identity) != target_identity:
            raise ValueError("the induced group-algebra map does not preserve the unit")


class _GroupAlgebraFunctor(Functor):
    r"""\(R[-]\colon \mathbf{Grp}\to \mathbf{Alg}_R\).

    On a group morphism \(f\colon H\to G\) it is the algebra morphism
    \(R[H]\to R[G]\) extending \(f\) \(R\)-linearly; for a subgroup
    inclusion this is the ring morphism \(R[H]\to R[G]\).
    """

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        super().__init__(OwnedGroups(), Algebras(ring).Associative().Unital())

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, group):
        return self._base_ring[group]

    def _apply_morphism(self, group_morphism):
        source = self(group_morphism.domain())
        target = self(group_morphism.codomain())
        return GroupAlgebraMorphism(
            Algebras(source.base_ring()).Associative().Unital().Mor(source, target),
            group_morphism,
        )

    def _repr_(self):
        return f"Group-algebra functor over {self._base_ring}"


class GroupAlgebraUnderlyingModuleFunctor(Functor):
    r"""The composite ``Grp -> Alg_R -> Mod_R``, ``G |-> R[G]`` as a module.

    This is the archived ``FreeModuleOnGroupFunctor`` construction stated at
    its actual owner: first form the group algebra, then forget only its
    multiplication.  Object and morphism actions therefore reuse the live
    group-algebra and algebra-underlying-module functors rather than rebuilding
    the free module or its induced map.
    """

    def __init__(self, base_ring) -> None:
        ring = _owned_ring(base_ring)
        self._base_ring = ring
        self._group_algebra_functor = _GroupAlgebraFunctor(ring)
        self._underlying_module_functor = (
            self._group_algebra_functor.codomain().underlying_module()
        )
        super().__init__(OwnedGroups(), self._underlying_module_functor.codomain())

    def base_ring(self):
        return self._base_ring

    def group_algebra_functor(self):
        return self._group_algebra_functor

    def underlying_module_functor(self):
        return self._underlying_module_functor

    def _apply_object(self, group):
        return self.underlying_module_functor()(self.group_algebra_functor()(group))

    def _apply_morphism(self, group_morphism):
        return self.underlying_module_functor()(
            self.group_algebra_functor()(group_morphism)
        )

    def _repr_(self):
        return f"Underlying-module-of-group-algebra functor over {self.base_ring()}"


FreeModuleOnGroupFunctor = GroupAlgebraUnderlyingModuleFunctor
