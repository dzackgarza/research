r"""Additive Mor groups and their composition endomorphism rings.

The enrichment is pointwise addition.  An elementwise map is supplied with
additivity as a hypothesis; construction does not decide arbitrary function
identities.  This is the additive specialization of the existing owned Mor
packet, using Sage's ``Mor``, ``Morphism`` and integer multiplication action.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.coerce_actions import IntegerMulAction
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
)


class _ScalarIdentityEvaluation:
    r"""Native evaluation of the scalar endomorphism r.id, from its actual r.

    This callable is the defining computation, not an annotation on another
    map. The parent supplies its already constructed pointwise scalar action.
    Arithmetic of two such maps is arithmetic of the supplied scalars, even
    when arbitrary endomorphism equality cannot be decided.
    """

    def __init__(self, parent, scalar):
        assert parent.domain() is parent.codomain(), (
            f"cannot form the scalar multiple {scalar}·id in {parent}: a multiple of the "
            f"identity is an endomorphism, but {parent.domain()} and {parent.codomain()} "
            f"are different groups"
        )
        self._parent = parent
        self.scalar = parent.base_ring()(scalar)

    def __call__(self, element):
        return self._parent._apply_pointwise_scalar(self.scalar, element)


def _scalar_identity_coefficient(morphism):
    r"""Read only the actual scalar-evaluation realization of an owned map.

    Private shared additive/linear map adapter. Its callers are native map
    arithmetic and endomorphism centrality. It inspects the selected callable
    at those two declared engines, never infers a scalar by sampling a map.
    """
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

    match morphism:
        case AdditiveMorphism():
            evaluation = morphism._function
        case ModuleMorphism():
            evaluation = morphism._element_function
        case _:
            return None
    return evaluation.scalar if isinstance(evaluation, _ScalarIdentityEvaluation) else None


class AdditiveMorGroups(OwnedCategory):
    r"""Additively enriched Mor groups with pointwise operations."""

    def super_categories(self):
        return [AdditiveGroups().AdditiveCommutative()]

    class ParentMethods:
        def zero(self):
            if self.domain() is self.codomain():
                return self._scalar_identity(self.base_ring().zero())
            return self.elementwise(lambda element: self.codomain().zero())

    class ElementMethods:
        def _add_(self, other):
            r"""Pointwise sum; Sage's arithmetic calls this with two elements of one Mor."""
            left, right = _scalar_identity_coefficient(self), _scalar_identity_coefficient(other)
            if left is not None and right is not None:
                return self.parent()._scalar_identity(left + right)
            return self.parent().elementwise(lambda element: self(element) + other(element))

        def __neg__(self):
            scalar = _scalar_identity_coefficient(self)
            if scalar is not None:
                return self.parent()._scalar_identity(-scalar)
            return self.parent().elementwise(lambda element: -self(element))

        def __sub__(self, other):
            return self + (-other)

        def _composition(self, right):
            r"""``self ∘ right`` in the additive Mor family.

            Sage's ``Map.__mul__`` has checked that ``right`` is a map into
            this morphism's domain; a map outside the additive Mor theory is
            not composed here.
            """
            if not right.parent().mor_category().is_subcategory(self.parent().mor_category()):
                return NotImplemented
            if right.parent() is self.parent() and self.domain() is self.codomain():
                return self.parent()._compose_endomorphisms(self, right)
            mor = self.parent().mor_family().Of(right.domain(), self.codomain())
            return mor.elementwise(lambda element: self(right(element)))

        def __rmul__(self, scalar):
            return self.parent()._owned_scalar_multiple(scalar, self)


class AdditiveEndomorphismRings(OwnedCategoryOverBaseRing):
    r"""Endomorphism algebras over their selected commutative scalar ring."""

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        assert self.base_ring() in OwnedRings().Commutative(), (
            f"endomorphisms of abelian groups form an algebra over {self.base_ring()} only "
            f"when that ring is commutative, but {self.base_ring()} is only known to be in "
            f"{self.base_ring().category()}"
        )
        return [AdditiveMorGroups(), Algebras(self.base_ring()).Associative().Unital()]

    class ParentMethods:
        def unformed_module(self):
            r"""The endomorphism algebra is built on this already-constructed Mor module."""
            return self

        @cached_method
        def multiplication(self):
            r"""Classify composition as the bilinear multiplication of the endomorphism algebra."""
            from dzack_research.preamble.categories.modules.native_modules import (
                _RingModulePresentation,
            )

            presentation = _RingModulePresentation(
                self,
                self.base_ring(),
                self._compose_endomorphisms,
                self.identity(),
                lambda scalar, arrow: self._owned_scalar_multiple(scalar, arrow),
            )
            return presentation.multiplication()

        def multiplication_morphism(self):
            r"""Return the retained tensor classifier of composition."""
            return self.multiplication()

        def associativity_decision(self):
            r"""Composition of endomorphisms is associative by construction."""
            return True

        def unit_laws_decision(self):
            r"""The identity endomorphism is a two-sided unit for composition."""
            return True

        def _compose_endomorphisms(self, left, right):
            left_scalar, right_scalar = _scalar_identity_coefficient(left), _scalar_identity_coefficient(right)
            if left_scalar is not None and right_scalar is not None:
                return self._scalar_identity(left_scalar * right_scalar)
            return self.elementwise(lambda element: left(right(element)))

        def is_central(self, morphism):
            r"""Scalar endomorphisms commute with all linear endomorphisms.

            h(rx)=r h(x) proves the assertion without enumerating h. For
            additive endomorphisms the scalars are integers and the same
            equation follows by repeated addition. Other cases are undecided.
            See Mathlib Algebra/Module/LinearMap/End, Module.toModuleEnd.
            """
            morphism = self(morphism)
            if _scalar_identity_coefficient(morphism) is not None:
                return True
            return Unknown

        def scalar_multiple(self, scalar, morphism):
            return self._owned_scalar_multiple(scalar, morphism)

        def _owned_scalar_multiple(self, scalar, morphism):
            r"""Apply the selected scalar enrichment pointwise.

            The Mor constructor supplies its scalar ring.  Integer scalars
            act on every additive group through Sage's repeated addition;
            a commutative scalar ring acts through the target module.
            """
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            scalar = self.base_ring()(scalar)
            coefficient = _scalar_identity_coefficient(morphism)
            if coefficient is not None:
                return self._scalar_identity(scalar * coefficient)
            if self.base_ring() is _own_ring(SageZZ):
                action = IntegerMulAction(SageZZ, self.codomain(), m=self.codomain().zero())
                return self.elementwise(lambda element: action(int(scalar), morphism(element)))
            return self.elementwise(
                lambda element: self.codomain().scalar_multiple(scalar, morphism(element))
            )

        @cached_method
        def identity(self):
            return self._scalar_identity(self.base_ring().one())

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

    def _add_(self, other):
        return AdditiveMorGroups.ElementMethods._add_(self, other)

    def _neg_(self):
        return AdditiveMorGroups.ElementMethods.__neg__(self)

    def __neg__(self):
        return AdditiveMorGroups.ElementMethods.__neg__(self)

    def __rmul__(self, scalar):
        return self.parent()._owned_scalar_multiple(scalar, self)

    def _lmul_(self, scalar):
        return self.parent()._owned_scalar_multiple(scalar, self)

    def _rmul_(self, scalar):
        return self.parent()._owned_scalar_multiple(scalar, self)

    def _acted_upon_(self, actor, self_on_left):
        r"""Scalar action of the Mor's scalar ring; any other actor is not an action here."""
        scalars = self.parent().base_ring()
        if actor not in scalars:
            return None
        return self.parent()._owned_scalar_multiple(scalars(actor), self)

    def _composition(self, right):
        if right.codomain() is not self.domain():
            return NotImplemented
        return AdditiveMorGroups.ElementMethods._composition(self, right)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if self is other:
            return op == op_EQ
        from sage.structure.element import parent as element_parent
        from dzack_research.preamble.categories.sets.set_categories import EnumeratedSets

        if element_parent(other) is not self.parent():
            return op == op_NE
        left, right = _scalar_identity_coefficient(self), _scalar_identity_coefficient(other)
        if left is not None and right is not None and (left == right) is True:
            return op == op_EQ
        domain = self.domain()
        if domain.is_finite() is not True or domain not in EnumeratedSets():
            return Unknown
        decisions = tuple(self(element) == other(element) for element in domain)
        match (all(value is True for value in decisions), any(value is False for value in decisions)):
            case (True, _):
                equal = True
            case (_, True):
                equal = False
            case _:
                equal = Unknown
        return equal if op == op_EQ or equal is Unknown else not equal


class AdditiveMor(CategoricalMor):
    r"""The Sage Mor parent realizing the additive Mor enrichment."""

    Element = AdditiveMorphism

    def __init__(self, family, domain, codomain) -> None:
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        self._base_ring = _own_ring(SageZZ)
        self._integer_action = IntegerMulAction(SageZZ, codomain, m=codomain.zero())
        category = AdditiveEndomorphismRings(self._base_ring) if domain is codomain else AdditiveMorGroups()
        super().__init__(family, domain, codomain, category=category, base=self._base_ring)

    def _element_constructor_(self, datum):
        if isinstance(datum, Morphism):
            assert datum.domain() is self.domain() and datum.codomain() is self.codomain(), (
                f"{datum} is a morphism {datum.domain()} -> {datum.codomain()}, not a "
                f"morphism {self.domain()} -> {self.codomain()}"
            )
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if callable(datum):
            return self.elementwise(datum)
        assert self.domain() is self.codomain(), (
            f"cannot read the scalar {datum} as a morphism {self.domain()} -> "
            f"{self.codomain()}: a scalar is a multiple of the identity, which exists only "
            f"when the domain and codomain are the same group"
        )
        return self._owned_scalar_multiple(self._base_ring(datum), self.identity())

    def elementwise(self, function):
        r"""Construct the additive map declared by ``function``."""
        assert callable(function), (
            f"cannot build a morphism {self.domain()} -> {self.codomain()} from {function}: "
            f"an additive morphism is given by a map on elements, and {function} is not a map"
        )
        return self.element_class(self, function)

    def _apply_pointwise_scalar(self, scalar, element):
        return self._integer_action(int(self._base_ring(scalar)), element)

    def _scalar_identity(self, scalar):
        return self.elementwise(_ScalarIdentityEvaluation(self, scalar))

    def _owned_scalar_multiple(self, scalar, morphism):
        r"""Realize the canonical integer action through Sage's additive action."""
        coefficient = _scalar_identity_coefficient(morphism)
        if coefficient is not None:
            return self._scalar_identity(self._base_ring(scalar) * coefficient)
        integer = int(self._base_ring(scalar))
        return self.elementwise(lambda element: self._integer_action(integer, morphism(element)))
