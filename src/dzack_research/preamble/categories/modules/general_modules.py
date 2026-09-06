r"""Modules given as an abelian group together with a ring morphism into its endomorphisms.

An ``R``-module is an abelian group ``A`` and a ring morphism
``rho : R -> End(A)``.  This module states that definition directly: the
underlying set, its addition, zero and negation are the abelian group, and
``rho`` is the scalar action.  Nothing here is a second kind of module.  The
object is built through the owned module chain like every other module, so
every operation the module graph owns -- Hom-sets, scalar change,
localization, the annihilator as the kernel of ``rho`` -- answers on it
without being restated at this level.
"""

import logging

from sage.structure.element import ModuleElement
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import Set
from dzack_research.preamble.owned_category import object_of


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

        def _acted_upon_(self, actor, self_on_left):
            try:
                scalar = self.parent().base_ring()(actor)
            except (TypeError, ValueError):
                return None
            return self.parent().scalar_multiple(scalar, self)

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
        return GeneralModule(
            self.base_ring(),
            Set([0]),
            addition=lambda left, right: 0,
            zero=0,
            negation=lambda value: 0,
            scalar_action=lambda scalar, value: 0,
        )

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            base_ring,
            underlying_set,
            addition,
            zero,
            negation,
            scalar_action=None,
            rho=None,
            verify=True,
            **rest,
        ) -> None:
            ring = _owned_ring(base_ring)
            assert (scalar_action is None) != (rho is None), (
                "a module is given either by a binary scalar action or by rho: R -> End(A), not both"
            )
            assert callable(addition) and callable(negation), (
                "the additive structure of the underlying group is given by its operations"
            )
            self._preamble_underlying_set = Set(underlying_set)
            self._preamble_addition = addition
            self._preamble_negation = negation
            self._preamble_input_rho = rho
            if rho is None:
                self._preamble_raw_scalar_action = scalar_action
            else:
                assert _engine_ring(rho.domain()) is _engine_ring(ring), (
                    "the scalar action must be a ring morphism out of the module's base ring"
                )
                self._preamble_raw_scalar_action = lambda scalar, value: rho(scalar)(value)

            super().__init__(base_ring=ring, **rest)

            self._preamble_zero_value = self._normalize_underlying_value(zero)
            self._preamble_scalar_action_morphism = self._build_scalar_action_morphism()
            if verify:
                self._verify_module_laws_when_decidable()

        def underlying_set(self):
            r"""Return the set this module is built on."""
            return self._preamble_underlying_set

        def cardinality(self):
            r"""Return the cardinality of the set this module is built on.

            The module adds structure to that set and no elements, so the count
            is the set's and is not computed a second time here.
            """
            return cardinal(self.underlying_set().cardinality())

        def is_finite(self):
            return self.cardinality().is_finite()

        def _normalize_underlying_value(self, value):
            r"""Read foreign data as a value of the underlying set.

            Reached only from ``_element_constructor_``, the one boundary that
            admits data this parent did not build.
            """
            if isinstance(value, self.category().ElementType):
                value = value.underlying_element()
            assert value in self.underlying_set(), (
                f"{value!r} is not in the set this module is built on"
            )
            return value

        def _element_constructor_(self, value):
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return value
            return self.element_class(self, self._normalize_underlying_value(value))

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
            return self(self._preamble_zero_value)

        def _add_elements(self, left, right):
            return self(
                self._preamble_addition(
                    self(left).underlying_element(),
                    self(right).underlying_element(),
                )
            )

        def _negate_element(self, element):
            return self(self._preamble_negation(self(element).underlying_element()))

        def _raw_scalar_multiple(self, scalar, element):
            return self(
                self._preamble_raw_scalar_action(
                    self.base_ring()(scalar),
                    self(element).underlying_element(),
                )
            )

        def _build_scalar_action_morphism(self):
            r"""Return ``rho : R -> End(M)``, the module structure itself.

            Each ``rho(r)`` is linear because ``rho`` is a ring morphism into
            the endomorphisms: that is the hypothesis this construction is
            given, so it is asserted here rather than re-derived on elements.
            """
            endomorphisms = Modules(self.base_ring()).End(self)
            return ring_morphism(
                self.base_ring(),
                endomorphisms,
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._raw_scalar_multiple(scalar, element),
                    verify_linearity=False,
                ),
            )

        def scalar_action_input(self):
            r"""Return the supplied ``rho`` when the module was given one."""
            assert self._preamble_input_rho is not None, (
                "this module was given by a binary scalar action, not by a morphism"
            )
            return self._preamble_input_rho

        def _represented_annihilator_ideal(self):
            r"""Represent the scalar-action kernel by exhaustive finite enumeration.

            This is a private backend for ``scalar_action().kernel()``.  Outside
            an enumerable finite regime a stronger algebra backend is required.
            """
            assert self.is_finite() is True, (
                "the annihilator of this general module needs a finite underlying set "
                "or a stronger algebra backend"
            )
            scalars = _enumerated_scalars(self.base_ring())
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

        def _verify_module_laws_when_decidable(self) -> None:
            r"""Check the supplied structure exactly where the check is decidable.

            The addition, zero, negation and action are supplied callables, so
            the module laws are hypotheses on them rather than theorems.  A
            finite underlying set decides the additive laws exactly, and a
            finite scalar ring decides the module laws exactly.  Outside those
            regimes the structure is declared and a DEBUG diagnostic records
            that no exhaustive check was available.
            """
            if self.is_finite() is not True:
                _LOGGER.debug(
                    "General module over %s accepted without exhaustive module-law verification",
                    self.base_ring(),
                )
                return
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

            scalars = _enumerated_scalars(self.base_ring())
            if scalars is None:
                _LOGGER.debug(
                    "Additive group laws for the finite set %s were exhaustively checked, but "
                    "scalar-module laws over non-enumerated %s were not",
                    self.underlying_set(),
                    self.base_ring(),
                )
                return

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

        def _repr_(self):
            return f"Module over {self.base_ring()} on {self.underlying_set()}"


def _enumerated_scalars(ring):
    r"""Return the elements of a finite enumerable ring, or ``None``."""
    engine = _engine_ring(ring)
    try:
        if not bool(engine.is_finite()):
            return None
        return tuple(ring._from_engine_element(engine(scalar)) for scalar in engine)
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return None


def GeneralModule(
    ring,
    underlying_set,
    *,
    addition,
    zero,
    negation,
    scalar_action=None,
    rho=None,
    verify=True,
):
    r"""Return the ``R``-module on ``underlying_set`` with the given structure.

    Either a binary ``scalar_action(r, x)`` or the ring morphism
    ``rho : R -> End(A)`` fixes the module structure; they are the same datum
    written two ways.
    """
    return object_of(
        GeneralModules(_owned_ring(ring)),
        base_ring=ring,
        underlying_set=underlying_set,
        addition=addition,
        zero=zero,
        negation=negation,
        scalar_action=scalar_action,
        rho=rho,
        verify=verify,
    )


module_from_action = GeneralModule


__all__ = [
    "GeneralModule",
    "GeneralModules",
    "module_from_action",
]
