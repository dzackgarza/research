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
                    f"cannot construct an {ring}-module from {rho}: a ring morphism rho: {ring} -> End(A) "
                    "already determines the additive group A, so no set, addition, zero, negation or "
                    "scalar multiplication may be given alongside it"
                )
                assert rho.parent().mor_category().is_subcategory(OwnedRings()) and rho.domain() is ring, (
                    f"cannot construct an {ring}-module from {rho}: the scalar action must be a ring "
                    f"morphism out of {ring}, but {rho} lies in {rho.parent()}"
                )
                underlying_set = rho.codomain().domain()
                assert rho.codomain() is AdditiveGroups().AdditiveCommutative().End(underlying_set), (
                    f"cannot construct an {ring}-module from {rho}: the scalar action must take values in "
                    f"the endomorphism ring End(A) of an abelian group A, but its codomain is {rho.codomain()}"
                )
                addition = operator.add
                zero = underlying_set.zero()
                negation = operator.neg
            else:
                assert callable(scalar_action), (
                    f"cannot construct an {ring}-module on {underlying_set}: a scalar multiplication "
                    f"{ring} x A -> A is required, but {scalar_action!r} is not a function"
                )
            assert callable(addition) and callable(negation), (
                f"cannot construct an {ring}-module on {underlying_set}: an addition and a negation are "
                f"required, but got addition {addition!r} and negation {negation!r}"
            )
            self._underlying_set = Set(underlying_set)
            self._addition = addition
            self._negation = negation
            assert zero in self._underlying_set, (
                f"cannot construct an {ring}-module on {underlying_set}: the zero {zero!r} is not an "
                f"element of {underlying_set}"
            )
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
                f"{value!r} is not an element of {self}: it is not in the underlying set {underlying}"
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
                f"{self} has no ring morphism {self.base_ring()} -> End(A): it was constructed from a "
                f"scalar multiplication {self.base_ring()} x A -> A instead"
            )
            return self._rho

        def _represented_annihilator_ideal(self):
            r"""Represent the scalar-action kernel by exhaustive finite enumeration.

            This is a private backend for ``scalar_action().kernel()``.  Outside
            an enumerable finite regime a stronger algebra backend is required.
            """
            assert self.is_finite() is True, (
                f"cannot compute the annihilator of {self}: this algorithm needs a finite underlying set, "
                f"and {self.underlying_set()} is not known to be finite"
            )
            scalars = _enumerated_ring_elements(self.base_ring())
            assert scalars is not None, (
                f"cannot compute the annihilator of {self}: this algorithm needs a finite scalar ring "
                f"whose elements can be listed, and {self.base_ring()} is not one"
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
                    f"{self} is not a module: the given zero {zero} is not an additive identity, "
                    f"since {element} + {zero} != {element}"
                )
                assert element + (-element) == zero, (
                    f"{self} is not a module: the given negation does not give additive inverses, "
                    f"since {element} + ({-element}) != {zero}"
                )
            for left in elements:
                for right in elements:
                    assert left + right == right + left, (
                        f"{self} is not a module: its addition is not commutative, "
                        f"since {left} + {right} != {right} + {left}"
                    )
                    for third in elements:
                        assert (left + right) + third == left + (right + third), (
                            f"{self} is not a module: its addition is not associative on "
                            f"{left}, {right}, {third}"
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
                    f"{self} is not a module: 1 in {self.base_ring()} does not act as the identity, "
                    f"since 1 * {element} != {element}"
                )
                assert self.scalar_multiple(zero_scalar, element) == zero, (
                    f"{self} is not a module: 0 in {self.base_ring()} does not act as zero, "
                    f"since 0 * {element} != {zero}"
                )
                for scalar in scalars:
                    for other in elements:
                        assert self.scalar_multiple(scalar, element + other) == (
                            self.scalar_multiple(scalar, element)
                            + self.scalar_multiple(scalar, other)
                        ), (
                            f"{self} is not a module: scalar multiplication by {scalar} is not additive, "
                            f"since {scalar} * ({element} + {other}) != {scalar} * {element} + {scalar} * {other}"
                        )
                    for second_scalar in scalars:
                        assert self.scalar_multiple(scalar + second_scalar, element) == (
                            self.scalar_multiple(scalar, element)
                            + self.scalar_multiple(second_scalar, element)
                        ), (
                            f"{self} is not a module: ({scalar} + {second_scalar}) * {element} != "
                            f"{scalar} * {element} + {second_scalar} * {element}"
                        )
                        assert self.scalar_multiple(
                            scalar * second_scalar, element
                        ) == self.scalar_multiple(
                            scalar, self.scalar_multiple(second_scalar, element)
                        ), (
                            f"{self} is not a module: ({scalar} * {second_scalar}) * {element} != "
                            f"{scalar} * ({second_scalar} * {element})"
                        )
            return True

        def _repr_(self):
            return f"Module over {self.base_ring()} on {self.underlying_set()}"


__all__ = [
    "GeneralModules",
]
