"""The owned operation spine below groups."""

from sage.misc.abstract_method import abstract_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import (
    CategoryPacketMethods,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


class MagmaMorphism:
    r"""A map preserving the selected binary operation."""

    def __init__(self, parent, function) -> None:
        if not callable(function):
            raise TypeError(
                f"cannot build a morphism in {parent} from {function}: an operation-preserving "
                "morphism is given by a map on elements"
            )
        self._function = function
        super().__init__(parent, function)

    def _composition(self, right):
        if right.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().mor_family().base_category()
        if (
            right.domain() not in category
            or not right.parent().mor_family().base_category().is_subcategory(category)
        ):
            return super()._composition(right)
        return self.parent().mor_family().Of(
            right.domain(), self.codomain()
        )(lambda element: self(right(element)))


class MagmaMor(CategoricalMor):
    r"""The fixed Mor category of operation-preserving magma maps."""

    ElementMethods = MagmaMorphism

    def _element_constructor_(self, function):
        if isinstance(function, MagmaMorphism):
            if function.domain() is not self.domain() or function.codomain() is not self.codomain():
                raise ValueError(
                    f"{function} is a morphism {function.domain()} -> {function.codomain()}, "
                    f"not a morphism {self.domain()} -> {self.codomain()}"
                )
            if function.parent() is self:
                return function
            function = function.__call__
        if not callable(function):
            raise TypeError(
                f"a morphism {self.domain()} -> {self.codomain()} needs a map on elements, "
                f"but got {function!r}"
            )
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"there is no identity morphism {self.domain()} -> {self.codomain()}: the endpoints differ"
            )
        return self(lambda element: element)


class MagmaMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return MagmaMor


class Magmas(CategoryPacketMethods, OwnedCategory):
    _MorCategory = MagmaMorCategoryConstruction

    def an_object(self):
        r"""The owned integers under multiplication."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

    class ElementMethods:
        @abstract_method
        def _mul_(self, other):
            r"""Return the value of the selected magma law on ``(self, other)``.

            ``other`` has the parent of ``self``.  ``x * y`` reaches this
            through Sage's ``Element.__mul__``, which coerces both operands
            into one parent first; an element supplies the law here, never by
            overriding the operator.
            """

    class ParentMethods:
        def _commutativity_decision(self):
            r"""Protected decision procedure for the magma commutativity predicate."""
            return NotImplemented

        def is_commutative(self):
            r"""Return whether the magma law satisfies ``xy = yx`` for all elements."""
            match self in Magmas().Commutative():
                case True:
                    return True
                case False:
                    decision = self._commutativity_decision()
                    assert decision is not NotImplemented, (
                        f"commutativity is defined for every magma, but no decision procedure is available for {self}"
                    )
                    return decision

    class SubcategoryMethods:
        def Subobjects(self, base_object):
            r"""Return represented structured subobjects of ``base_object``.

            A submagma remains a magma equipped with its chosen monomorphism
            into the fixed object.  It therefore uses the generic structured
            subobject category rather than the set-specific slice realization
            inherited from ``Sets``.
            """
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                SubobjectCategory,
            )

            return SubobjectCategory(self, base_object)

        def Commutative(self):
            r"""Return this category with the axiom ``xy = yx``.

            Commutativity is a property of the operation, so it is stated once
            here, at the level that introduces the operation, and every
            subcategory reaches it.
            """
            return self._with_axiom("Commutative")

        def Unital(self):
            r"""Return this category with a two-sided unit for its multiplication.

            ``lean-categories``: ``LeanCategories.Algebra.unital``, the
            classifier ``UnitalMagma -> MagmaCat`` on magmas
            (``Algebra/Concrete/Magmas.lean``).
            """
            return self._with_axiom("Unital")

    class Commutative(CategoryWithAxiom):
        r"""Magmas whose law satisfies ``xy = yx``.

        The axiom is implemented here, at the level that introduces the law.
        ``Category._with_axiom_as_tuple`` (``sage/categories/category.py``)
        returns the category itself for an axiom no class on its path
        implements, so without this class ``Magmas().Commutative()`` would be
        ``Magmas()`` and every magma would be a commutative magma.  Sage then
        joins this class into the supercategories of every category with the
        ``Commutative`` axiom whose path reaches ``Magmas()``: commutative
        rings, commutative algebras and abelian groups are commutative magmas
        through it.
        """

        def an_object(self):
            r"""The owned integers under multiplication."""
            return Magmas().an_object()

        @classmethod
        def _repr_object_names(cls):
            return "commutative magmas"

    class Unital(CategoryWithAxiom):
        r"""Unital magmas: a magma ``(M, *)`` with an element ``1`` with ``1 * x = x = x * 1``.

        ``lean-categories``: ``UnitalMagma`` (``Algebra/Concrete/Magmas.lean``).
        The unit is introduced at this level, so its contract is stated here:
        monoids and unital algebras are unital magmas and supply it.
        """

        @classmethod
        def _repr_object_names(cls):
            return "unital magmas"

        class ParentMethods:
            @abstract_method
            def one(self):
                r"""Return the two-sided unit of this magma."""


class MonoidMorCategoryConstruction(MorCategoryConstruction):
    r"""The fixed-endpoint Mor categories of owned monoids."""

    def fixed_category_class(self):
        return MonoidMor


class Semigroups(CategoryPacketMethods, OwnedCategory):
    _MorCategory = MagmaMorCategoryConstruction

    def an_object(self):
        return Magmas().an_object()

    def super_categories(self):
        return [Magmas()]


class Monoids(CategoryPacketMethods, OwnedCategory):
    def an_object(self):
        return Magmas().an_object()

    def super_categories(self):
        r"""A monoid is a semigroup whose magma is unital (Mathlib ``Monoid.toMulOneClass``)."""
        return [Semigroups(), Magmas().Unital()]

    class ElementMethods:
        def _unit_decision(self):
            r"""Protected decision procedure for invertibility in the ambient monoid."""
            return NotImplemented

        def is_unit(self):
            r"""Return whether this element has a two-sided inverse in its monoid."""
            decision = self._unit_decision()
            assert decision is not NotImplemented, (
                f"invertibility is defined for every monoid element, but no decision procedure is available for {self}"
            )
            return decision

        def _pow_int(self, exponent):
            r"""Integer powers by repeated squaring, from the monoid law."""
            from sage.arith.power import generic_power

            return generic_power(self, exponent)

    class ParentMethods:
        def generated_submonoid(
            self, generators, *, description=None, structure_data=None
        ):
            r"""Return the represented submonoid generated by ``generators``."""
            from dzack_research.preamble.categories.group.submonoids import (
                _generated_submonoid,
            )

            return _generated_submonoid(
                self,
                generators,
                description=description,
                structure_data=structure_data,
            )

        def predicate_submonoid(
            self, predicate, description, *, placements=(), structure_data=None
        ):
            r"""Return the represented submonoid cut out by ``predicate``.

            A specialized construction may supply theorem-backed stronger
            ``placements``; they are part of the object's category at
            construction rather than a later refinement.
            """
            from dzack_research.preamble.categories.group.submonoids import (
                _predicate_submonoid,
            )

            return _predicate_submonoid(
                self,
                predicate,
                description,
                placements=placements,
                structure_data=structure_data,
            )

    _MorCategory = MonoidMorCategoryConstruction

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError(
                f"cannot form Mor({domain}, {codomain}) in {self}: the domain and the "
                f"codomain must both be monoids"
            )
        return self.MorCategory().Of(domain, codomain)



class AdditiveMagmas(CategoryPacketMethods, OwnedCategory):
    class _MorCategory(MorCategoryConstruction):
        def fixed_category_class(self):
            from dzack_research.preamble.categories.group.additive_mors import (
                AdditiveMagmaMor,
            )

            return AdditiveMagmaMor

    def an_object(self):
        r"""The owned integers under addition."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

    class ElementMethods:
        @abstract_method
        def __add__(self, other):
            r"""Return the value of the selected additive magma law on ``(self, other)``."""

    class SubcategoryMethods:
        def AdditiveCommutative(self):
            r"""Return this category with the axiom ``x + y = y + x``."""
            return self._with_axiom("AdditiveCommutative")

    class AdditiveCommutative(CategoryWithAxiom):
        r"""Additive magmas whose law satisfies ``x + y = y + x``.

        The axiom is implemented here, at the level that introduces the
        additive law.  ``Category._with_axiom_as_tuple``
        (``sage/categories/category.py``) returns the category itself for an
        axiom no class on its path implements, so without this class
        ``AdditiveMagmas().AdditiveCommutative()`` would be
        ``AdditiveMagmas()`` and every additive magma, semigroup and monoid
        would be additively commutative.  Sage joins this class into the
        supercategories of every category with the ``AdditiveCommutative``
        axiom whose path reaches ``AdditiveMagmas()``.
        """

        def an_object(self):
            r"""The owned integers under addition."""
            return AdditiveMagmas().an_object()

        @classmethod
        def _repr_object_names(cls):
            return "additive commutative magmas"


class AdditiveSemigroups(CategoryPacketMethods, OwnedCategory):
    class _MorCategory(MorCategoryConstruction):
        def fixed_category_class(self):
            from dzack_research.preamble.categories.group.additive_mors import (
                AdditiveMagmaMor,
            )

            return AdditiveMagmaMor

    def an_object(self):
        return AdditiveMagmas().an_object()

    def super_categories(self):
        return [AdditiveMagmas()]


class AdditiveMonoids(CategoryPacketMethods, OwnedCategory):
    class _MorCategory(MorCategoryConstruction):
        def fixed_category_class(self):
            from dzack_research.preamble.categories.group.additive_mors import (
                AdditiveMonoidMor,
            )

            return AdditiveMonoidMor

    def an_object(self):
        return AdditiveMagmas().an_object()

    def super_categories(self):
        return [AdditiveSemigroups()]

    class ParentMethods:
        @abstract_method
        def zero(self):
            r"""Return the identity element for the additive monoid law."""

        def monoidal_unit(self):
            return self.zero()


class AdditiveGroups(CategoryPacketMethods, OwnedCategory):
    class _MorCategory(MorCategoryConstruction):
        def fixed_category_class(self):
            from dzack_research.preamble.categories.group.additive_mors import (
                AdditiveMonoidMor,
            )

            return AdditiveMonoidMor

    def an_object(self):
        r"""The additive group of the owned integers."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        return [AdditiveMonoids()]

    class AdditiveCommutative(CategoryWithAxiom):
        """Additive groups whose addition is commutative."""

        class _MorCategory(MorCategoryConstruction):
            def fixed_category_class(self):
                from dzack_research.preamble.categories.group.additive_mors import (
                    AdditiveMor,
                )

                return AdditiveMor

        @classmethod
        def _repr_object_names(cls):
            return "commutative additive groups"


class MonoidMorphism:
    """A morphism in the owned category of monoids."""

    def __init__(self, parent, function) -> None:
        super().__init__(parent, function)


class MonoidMor(CategoricalMor):
    r"""The owned fixed Mor category ``Mor_Mon(A,B)``."""

    ElementMethods = MonoidMorphism

    def __init__(self, family, domain, codomain) -> None:
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, function):
        if isinstance(function, MonoidMorphism):
            if function.domain() is not self.domain() or function.codomain() is not self.codomain():
                raise ValueError(
                    f"{function} is a monoid morphism {function.domain()} -> "
                    f"{function.codomain()}, not a morphism {self.domain()} -> {self.codomain()}"
                )
            if function.parent() is self:
                return function
            function = function.__call__
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"there is no identity morphism {self.domain()} -> {self.codomain()}: an "
                f"identity exists only when the domain and codomain are the same monoid"
            )
        return self(lambda element: element)
