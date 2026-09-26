"""The owned operation spine below groups."""

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
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
            return NotImplemented
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


class Magmas(OwnedCategory):
    _MorCategory = MagmaMorCategoryConstruction

    def an_object(self):
        r"""The owned integers under multiplication."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

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


class MonoidMorCategoryConstruction(MorCategoryConstruction):
    r"""The fixed-endpoint Mor categories of owned monoids."""

    def fixed_category_class(self):
        return MonoidMor


class Semigroups(OwnedCategory):
    _MorCategory = MagmaMorCategoryConstruction

    def an_object(self):
        return Magmas().an_object()

    def super_categories(self):
        return [Magmas()]


class Monoids(OwnedCategory):
    def an_object(self):
        return Magmas().an_object()

    def super_categories(self):
        return [Semigroups()]

    class ElementMethods:
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



class AdditiveMagmas(OwnedCategory):
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

    class SubcategoryMethods:
        def AdditiveCommutative(self):
            r"""Return this category with the axiom ``x + y = y + x``."""
            return self._with_axiom("AdditiveCommutative")


class AdditiveSemigroups(OwnedCategory):
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


class AdditiveMonoids(OwnedCategory):
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
        def monoidal_unit(self):
            return self.zero()


class AdditiveGroups(OwnedCategory):
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
