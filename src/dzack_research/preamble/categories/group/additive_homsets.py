r"""Additive Hom groups and their composition endomorphism rings.

The enrichment is pointwise addition.  An elementwise map is supplied with
additivity as a hypothesis; construction does not decide arbitrary function
identities.  This is the additive specialization of the existing owned Hom
packet, using Sage's ``Homset``, ``Morphism`` and integer multiplication action.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.coerce_actions import IntegerMulAction
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.magmas import AdditiveGroups


class AdditiveHomGroups(OwnedCategory):
    r"""Additively enriched Hom groups with pointwise operations."""

    def super_categories(self):
        return [AdditiveGroups().AdditiveCommutative()]

    class ParentMethods:
        def zero(self):
            return self.elementwise(lambda element: self.codomain().zero())

    class ElementMethods:
        # Sage's Morphism binary-operator protocol returns NotImplemented for
        # a foreign operand; the Hom parent then states its mathematical type.
        def __add__(self, other):
            if not isinstance(other, Morphism) or other.parent() is not self.parent():
                return NotImplemented
            return self.parent().elementwise(lambda element: self(element) + other(element))

        def __neg__(self):
            return self.parent().elementwise(lambda element: -self(element))

        def __sub__(self, other):
            return self + (-other)

        def __mul__(self, other):
            if not isinstance(other, Morphism) or other.codomain() is not self.domain():
                return NotImplemented
            if not other.parent().homset_category().is_subcategory(self.parent().homset_category()):
                return NotImplemented
            hom = self.parent().hom_family().Of(other.domain(), self.codomain())
            return hom.elementwise(lambda element: self(other(element)))

        def __rmul__(self, scalar):
            return self.parent()._owned_scalar_multiple(scalar, self)


class AdditiveEndomorphismRings(OwnedCategory):
    r"""Rings of additive endomorphisms, with multiplication by composition."""

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return [AdditiveHomGroups(), Algebras(_own_ring(SageZZ))]

    class ParentMethods:
        def scalar_multiple(self, scalar, morphism):
            return self._owned_scalar_multiple(scalar, morphism)

        def _owned_scalar_multiple(self, scalar, morphism):
            r"""Apply the selected scalar enrichment pointwise.

            The Hom constructor supplies its scalar ring.  Integer scalars
            act on every additive group through Sage's repeated addition;
            a commutative scalar ring acts through the target module.
            """
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            scalar = self.base_ring()(scalar)
            if self.base_ring() is _own_ring(SageZZ):
                action = IntegerMulAction(SageZZ, self.codomain(), m=self.codomain().zero())
                return self.elementwise(lambda element: action(int(scalar), morphism(element)))
            return self.elementwise(
                lambda element: self.codomain().scalar_multiple(scalar, morphism(element))
            )

        @cached_method
        def identity(self):
            return self.elementwise(lambda element: element)

        def one(self):
            return self.identity()

        def is_commutative(self):
            r"""Return the undetermined value for a general endomorphism ring.

            Represented matrix endomorphism rings supply their rank-dependent
            decision in their more specific category.
            """
            return Unknown


class AdditiveMorphism(Morphism):
    r"""An additive map with a supplied elementwise realization."""

    def __init__(self, parent, function) -> None:
        self._function = function
        Morphism.__init__(self, parent)

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, Morphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        assert self.domain().is_finite() is True, (
            "equality of elementwise additive maps requires a finite enumerable source"
        )
        equal = all(self(element) == other(element) for element in self.domain())
        return equal if op == op_EQ else not equal


class AdditiveHomset(CategoricalHomset):
    r"""The Sage Hom parent realizing the additive Hom enrichment."""

    Element = AdditiveMorphism

    def __init__(self, family, domain, codomain) -> None:
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        self._preamble_base_ring = _own_ring(SageZZ)
        self._preamble_algebra_base_ring = self._preamble_base_ring
        self._integer_action = IntegerMulAction(SageZZ, codomain, m=codomain.zero())
        category = AdditiveEndomorphismRings() if domain is codomain else AdditiveHomGroups()
        super().__init__(family, domain, codomain, category=category)

    def _element_constructor_(self, datum):
        if isinstance(datum, Morphism):
            assert datum.domain() is self.domain() and datum.codomain() is self.codomain(), (
                "an additive morphism must have the selected Hom endpoints"
            )
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if callable(datum):
            return self.elementwise(datum)
        assert self.domain() is self.codomain(), "integer scalars embed in an endomorphism ring"
        return self._owned_scalar_multiple(self._preamble_base_ring(datum), self.identity())

    def elementwise(self, function):
        r"""Construct the additive map declared by ``function``."""
        assert callable(function), "an additive morphism requires its element map"
        return self.element_class(self, function)

    def _owned_scalar_multiple(self, scalar, morphism):
        r"""Realize the canonical integer action through Sage's additive action."""
        integer = int(self._preamble_base_ring(scalar))
        return self.elementwise(lambda element: self._integer_action(integer, morphism(element)))
