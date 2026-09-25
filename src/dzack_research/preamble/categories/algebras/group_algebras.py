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

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    UnitalMultiplicativeAlgebraMorphism,
    _algebra_on_module,
    _center_algebra,
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
    OwnedRings,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


class GroupAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras of the form \(R[G]\), interned on their group.

    A data subcategory of \(R\)-algebras: an object is \(R[G]\) together with
    the group \(G\) framing it.  It is the algebra on the free module
    \(F_R(G)\) whose multiplication \(F_R(G)\otimes_R F_R(G)\to F_R(G)\)
    extends the group law, and the augmentation is determined by \(G\), so it
    is an augmented algebra.
    """

    def an_object(self):
        r"""\(R[C_2]\), the smallest group algebra with a nontrivial group."""
        return self.base_ring()[OwnedGroups.C(2)]

    @classmethod
    def _repr_object_names(cls):
        return "group algebras"

    def super_categories(self):
        return [AugmentedAlgebras(self.base_ring())]

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
            r"""The centre \(Z(R[G])\), the algebra on the span of the conjugacy-class sums.

            An element \(\sum a_g g\) is central exactly when \(a\) is a class
            function, so the class sums \(\sum_{h\in C} h\) over the conjugacy
            classes \(C\) of \(G\) form an \(R\)-basis of \(Z(R[G])\) (Isaacs,
            *Character Theory of Finite Groups*, Theorem 2.4).  Each class is
            the conjugation orbit of its representative.  That basis replaces
            the equalizers the general centre intersects; the algebra on it is
            built the same way.
            """
            group = self.group()
            assert group in FiniteGroups(), (
                f"the centre of {self} is computed from conjugacy-class sums, which needs a finite group, but "
                f"{group} is not known to be finite"
            )
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
            return _center_algebra(self, self.subobject_on(class_sums))

        @cached_method
        def group_inclusion(self):
            r"""The monoid morphism \(G\to R[G]\), \(g\mapsto g\).

            Every image is a unit, with inverse the image of \(g^{-1}\).
            """
            return Monoids().Mor(self.group(), self)(self.module_generator)

        @cached_method
        def regular_representation(self):
            r"""``R[G]`` as a module over itself by left multiplication.

            The group acts on the algebra, an ``R``-module, by left
            multiplication through the group inclusion; ``Modules(R[G])``
            equips that action with the group-algebra scalar action.
            """
            inclusion = self.group_inclusion()

            def left_action(group_element, element):
                return inclusion(group_element) * self(element)

            return Modules(self)(self, left_action)

        def is_semisimple(self) -> bool:
            r"""Maschke's theorem in its ring form (Lam, FC, Theorem 6.1).

            \(R[G]\) is semisimple if and only if \(R\) is semisimple and
            \(|G|\) is a unit of \(R\).  A commutative semisimple ring is a
            finite product of fields, so an integral domain is semisimple
            exactly when it is a field.
            """
            ring = self.base_ring()
            order = self.group().cardinality()
            assert order.is_finite(), (
                f"Maschke's theorem concerns a finite group, but {self.group()} has order {order}"
            )
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
    multiplication = BilinearMap(
        module,
        module,
        module,
        lambda left, right: module.module_generator(left * right),
    )
    scalars = Algebras(ring).underlying_module()(ring)
    selected_augmentation = module.module_category().Mor(module, scalars)(
        lambda _label: scalars(ring.one())
    )
    # The group law decides the placement (Lam, A First Course in
    # Noncommutative Rings, §1): the multiplication extending an associative
    # law with identity e is associative with unit e, and R[G] is commutative
    # when R and G are.  Those theorems are the placement; the group answers
    # whether it is abelian, so no enumeration of R[G] decides it.
    commutative = (
        (Algebras(ring).Commutative(),)
        if ring in OwnedRings().Commutative() and group.is_abelian() is True
        else ()
    )
    law_decisions = {"associativity": True, "unit": True}
    match commutative:
        case (_commutative_category,):
            law_decisions["commutativity"] = True
        case ():
            pass
    return _algebra_on_module(
        module,
        multiplication,
        placement=(GroupAlgebras(ring), *commutative),
        unit=module.module_generator(group.one()),
        construction_data={
            "group": group,
            "selected_augmentation": selected_augmentation,
        },
        law_decisions=law_decisions,
    )


class GroupAlgebraMorphism(UnitalMultiplicativeAlgebraMorphism):
    r"""The algebra map ``R[H] -> R[G]`` induced by a represented group map.

    The multiplication law is not re-decided by equality of two linear maps on
    the (possibly infinite) basis ``H``.  A group morphism already satisfies
    ``f(hk)=f(h)f(k)`` and ``f(1)=1``; extending its basis map ``R``-linearly is
    therefore the unique unital algebra morphism of group algebras.
    """

    def __init__(self, parent, group_morphism) -> None:
        source = self.domain()
        target = self.codomain()
        if group_morphism.domain() is not source.group():
            raise ValueError(
                f"the group algebra morphism {self.domain()} -> {self.codomain()} needs a group map starting "
                f"at {source.group()}, but {group_morphism} starts at {group_morphism.domain()}"
            )
        if group_morphism.codomain() is not target.group():
            raise ValueError(
                f"the group algebra morphism {self.domain()} -> {self.codomain()} needs a group map ending at "
                f"{target.group()}, but {group_morphism} ends at {group_morphism.codomain()}"
            )

        linear = source.module_category().Mor(source, target)(
            lambda label: target.module_generator(group_morphism(label))
        )
        super().__init__(parent, linear)

    def _multiplicativity_derivation(self):
        return True

    def _unit_preservation_derivation(self):
        return True


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
