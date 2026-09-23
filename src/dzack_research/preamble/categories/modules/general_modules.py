r"""Modules given as an abelian group together with a ring morphism into its endomorphisms.

An ``R``-module is an abelian group ``A`` and a ring morphism
``rho : R -> End(A)``.  This module states that definition directly: the
underlying set, its addition, zero and negation are the abelian group, and
``rho`` is the scalar action.  Nothing here is a second kind of module.  The
object is built through the owned module chain like every other module, so
every operation the module graph owns -- Mor objects, scalar change,
localization, the annihilator as the kernel of ``rho`` -- answers on it
without being restated at this level.
"""

import logging
import operator

from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement, parent as element_parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _owned_ring,
    _enumerated_ring_elements,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Set,
)
from dzack_research.preamble.owned_category import _object_of

_LOGGER = logging.getLogger(__name__)


class GeneralModules(OwnedCategoryOverBaseRing):
    r"""Modules presented by an abelian group and a ring morphism ``rho : R -> End(A)``."""

    class ElementMethods(ModuleElement):
        r"""One element of the module, which is one element of the underlying set."""

        def __init__(self, parent, value) -> None:
            ModuleElement.__init__(self, parent)
            self._value = value

        def underlying_element(self):
            r"""Return this element read in the underlying set."""
            return self._value

        value = underlying_element

        def _add_(self, other):
            return self.parent()._add_elements(self, other)

        def _sub_(self, other):
            return self.parent()._add_elements(self, -other)

        def _neg_(self):
            return self.parent()._negate_element(self)

        def _lmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _rmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def __rmul__(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _acted_upon_(self, actor, self_on_left):
            _ = self_on_left
            parent = self.parent()
            match actor:
                case _ if actor in parent.base_ring():
                    return parent.scalar_multiple(actor, self)
                case _:
                    return None

        def _richcmp_(self, other, op):
            if other.parent() is not self.parent():
                return NotImplemented
            if op == op_EQ:
                return self.underlying_element() == other.underlying_element()
            if op == op_NE:
                return self.underlying_element() != other.underlying_element()
            return NotImplemented

        def _repr_(self):
            return repr(self.underlying_element())

    @classmethod
    def _repr_object_names(cls):
        return "general modules"

    def an_object(self):
        r"""The zero module, the one-point set with its only additive structure."""
        return self.from_operations(
            Set([0]),
            addition=lambda left, right: 0,
            zero=0,
            negation=lambda value: 0,
            scalar_action=lambda scalar, value: 0,
        )

    def from_operations(
        self,
        underlying_set,
        *,
        addition,
        zero,
        negation,
        scalar_action,
    ):
        r"""Return the module on ``underlying_set`` with the stated operations."""
        return _object_of(
            self,
            base_ring=self.base_ring(),
            underlying_set=underlying_set,
            addition=addition,
            zero=zero,
            negation=negation,
            scalar_action=scalar_action,
        )

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            base_ring,
            rho=None,
            *,
            underlying_set=None,
            addition=None,
            zero=None,
            negation=None,
            scalar_action=None,
            **rest,
        ) -> None:
            ring = _owned_ring(base_ring)
            if rho is not None:
                assert all(datum is None for datum in (underlying_set, addition, zero, negation, scalar_action)), (
                    "the action morphism determines the underlying additive group"
                )
                assert rho.parent().mor_category().is_subcategory(OwnedRings()) and rho.domain() is ring, (
                    "the scalar action must be a ring morphism out of the module's base ring"
                )
                underlying_set = rho.codomain().domain()
                assert rho.codomain() is AdditiveGroups().AdditiveCommutative().End(underlying_set), (
                    "the action takes values in the endomorphism ring of an additive group"
                )
                addition = operator.add
                zero = underlying_set.zero()
                negation = operator.neg
            else:
                assert callable(scalar_action), "an elementwise module presentation includes scalar multiplication"
            assert callable(addition) and callable(negation), (
                "the additive structure of the underlying group is given by its operations"
            )
            self._underlying_set = Set(underlying_set)
            self._addition = addition
            self._negation = negation
            assert zero in self._underlying_set, "the additive zero belongs to the underlying set"
            self._zero_value = zero
            self._rho = rho
            self._elementwise_scalar_action = scalar_action
            super().__init__(base_ring=ring, **rest)
            self._module_laws_decision = self._verify_module_laws_when_decidable()

        def module_laws_decision(self):
            r"""Return the admission decision for the stated module laws.

            ``True`` means the laws were either supplied by the defining ring
            morphism ``rho : R -> End(A)`` or exhaustively decided on the
            represented finite data.  ``Unknown`` means an elementwise
            operation presentation retains the module laws as its defining
            hypothesis because the represented data do not supply an exact
            decision procedure.
            """
            return self._module_laws_decision

        def underlying_set(self):
            r"""Return the set this module is built on."""
            return self._underlying_set

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return the stated ``rho : R -> End(A)``, or the one the elementwise action defines."""
            match self._rho:
                case None:
                    return super()._ring_morphism_defining_module_action()
                case rho:
                    return rho

        def underlying_additive_group(self):
            match self._rho:
                case None:
                    return self
                case rho:
                    return rho.codomain().domain()

        def _underlying_additive_element(self, element):
            if self.underlying_additive_group() is self:
                return self(element)
            return self(element).underlying_element()

        def cardinality(self):
            r"""Return the cardinality of the set this module is built on.

            The module adds structure to that set and no elements, so the count
            is the set's and is not computed a second time here.
            """
            return cardinal(self.underlying_set().cardinality())

        def is_finite(self):
            r"""Whether the underlying set is placed as finite: ``True``, ``False`` or ``Unknown``.

            Read from placement rather than from ``cardinality``, which asserts
            where no cardinality of the underlying set is represented.
            """
            from sage.misc.unknown import Unknown

            from dzack_research.preamble.categories.sets.set_categories import Sets

            underlying = self.underlying_set()
            match underlying:
                case _ if underlying in Sets().Finite():
                    return True
                case _ if underlying in Sets().Infinite():
                    return False
                case _:
                    return Unknown

        def _element_constructor_(self, value):
            r"""Read foreign data as an element of the underlying set.

            A value of the underlying set is taken as it is; any other value is
            converted by the underlying set, which rejects what it does not
            contain.
            """
            source = element_parent(value)
            if source is self:
                return value
            if source in Modules(self.base_ring()) and source.unformed_module() is self:
                return source._element_of_unformed_module(value)
            if isinstance(value, self.category().ElementType):
                if value.parent() is self:
                    return value
                value = value.underlying_element()
            underlying = self.underlying_set()
            normalized = value if value in underlying else underlying(value)
            assert normalized in underlying, (
                f"{normalized!r} is not in the set this module is built on"
            )
            return self.element_class(self, normalized)

        def __call__(self, value):
            r"""Construct an element without Sage coercion discovery.

            The underlying set is an owned set that Sage's coercion graph has
            never heard of, so asking it for a conversion map fails before this
            parent's own constructor is reached.
            """
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            if isinstance(value, self.category().ElementType):
                return value.parent() is self
            return value in self.underlying_set()

        def __iter__(self):
            return (self(value) for value in self.underlying_set())

        def zero(self):
            return self(self._zero_value)

        def _add_elements(self, left, right):
            return self(
                self._addition(
                    self(left).underlying_element(),
                    self(right).underlying_element(),
                )
            )

        def _negate_element(self, element):
            return self(self._negation(self(element).underlying_element()))

        def _owned_scalar_multiple(self, scalar, element):
            scalar = self.base_ring()(scalar)
            value = self(element).underlying_element()
            match self._rho:
                case None:
                    return self(self._elementwise_scalar_action(scalar, value))
                case rho:
                    return self(rho(scalar)(value))

        def scalar_action_input(self):
            r"""Return the supplied ``rho`` when the module was given one."""
            assert self._rho is not None, (
                "this module was given by a binary scalar action, not by a morphism"
            )
            return self._rho

        def _represented_annihilator_ideal(self):
            r"""Represent the scalar-action kernel by exhaustive finite enumeration.

            This is a private backend for ``scalar_action().kernel()``.  Outside
            an enumerable finite regime a stronger algebra backend is required.
            """
            assert self.is_finite() is True, (
                "the annihilator of this general module needs a finite underlying set "
                "or a stronger algebra backend"
            )
            scalars = _enumerated_ring_elements(self.base_ring())
            assert scalars is not None, (
                "the annihilator of this general module needs an enumerable finite scalar ring"
            )
            zero = self.zero()
            annihilating = tuple(
                scalar
                for scalar in scalars
                if all(self.scalar_multiple(scalar, element) == zero for element in self)
            )
            return self.base_ring().ideal(*(annihilating or (self.base_ring().zero(),)))

        def _verify_module_laws_when_decidable(self):
            r"""Check the supplied structure exactly where the check is decidable.

            A supplied ``rho : R -> End(A)`` is the defining module datum, so
            its module laws follow from the ring-morphism and additive-group
            laws already carried by that datum.  For raw operations, a finite
            underlying set decides the additive laws exactly and an enumerable
            finite scalar ring decides the remaining module laws exactly.
            Outside those regimes the object explicitly retains ``Unknown`` as
            the module-law hypothesis rather than silently promoting it to a
            theorem.
            """
            if self._rho is not None:
                return True
            if self.underlying_set() not in FiniteSets():
                _LOGGER.debug(
                    "General module over %s retains an Unknown module-law hypothesis",
                    self.base_ring(),
                )
                return Unknown
            if self.underlying_set() not in EnumeratedSets():
                _LOGGER.debug(
                    "Finite general module over %s retains an Unknown module-law hypothesis; its underlying set has no selected enumeration",
                    self.base_ring(),
                )
                return Unknown
            elements = tuple(self)

            zero = self.zero()
            for element in elements:
                assert element + zero == element and zero + element == element, (
                    "the selected zero is not an additive identity"
                )
                assert element + (-element) == zero, (
                    "the selected negation does not give additive inverses"
                )
            for left in elements:
                for right in elements:
                    assert left + right == right + left, (
                        "the selected addition is not commutative"
                    )
                    for third in elements:
                        assert (left + right) + third == left + (right + third), (
                            "the selected addition is not associative"
                        )

            scalars = _enumerated_ring_elements(self.base_ring())
            if scalars is None:
                _LOGGER.debug(
                    "Additive group laws for the finite set %s were exhaustively checked, but "
                    "scalar-module laws over non-enumerated %s remain an Unknown hypothesis",
                    self.underlying_set(),
                    self.base_ring(),
                )
                return Unknown

            one = self.base_ring().one()
            zero_scalar = self.base_ring().zero()
            for element in elements:
                assert self.scalar_multiple(one, element) == element, (
                    "1 does not act as the identity on the module"
                )
                assert self.scalar_multiple(zero_scalar, element) == zero, (
                    "0 does not act as zero on the module"
                )
                for scalar in scalars:
                    for other in elements:
                        assert self.scalar_multiple(scalar, element + other) == (
                            self.scalar_multiple(scalar, element)
                            + self.scalar_multiple(scalar, other)
                        ), "scalar multiplication is not additive in the module variable"
                    for second_scalar in scalars:
                        assert self.scalar_multiple(scalar + second_scalar, element) == (
                            self.scalar_multiple(scalar, element)
                            + self.scalar_multiple(second_scalar, element)
                        ), "scalar multiplication is not additive in the scalar"
                        assert self.scalar_multiple(
                            scalar * second_scalar, element
                        ) == self.scalar_multiple(
                            scalar, self.scalar_multiple(second_scalar, element)
                        ), "scalar multiplication is not associative"
            return True

        def _repr_(self):
            return f"Module over {self.base_ring()} on {self.underlying_set()}"


__all__ = [
    "GeneralModules",
]
