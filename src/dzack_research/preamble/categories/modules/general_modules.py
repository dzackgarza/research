"""General represented modules from a carrier and explicit structure maps."""

import logging

from sage.categories.map import Map
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Set
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    register_module_scalar_action,
)
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism


_LOGGER = logging.getLogger(__name__)


class GeneralModuleElement(ModuleElement):
    r"""One element of a module presented on an arbitrary set carrier."""

    def __init__(self, parent, value) -> None:
        self._value = value
        ModuleElement.__init__(self, parent)

    def underlying_element(self):
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
        if not isinstance(other, GeneralModuleElement) or other.parent() is not self.parent():
            return NotImplemented
        if op == op_EQ:
            return self.underlying_element() == other.underlying_element()
        if op == op_NE:
            return self.underlying_element() != other.underlying_element()
        return NotImplemented

    def _repr_(self):
        return repr(self.underlying_element())


class GeneralModuleParent(Parent):
    r"""A general ``R``-module carried by a represented set.

    The defining data are additive operations on the carrier and a scalar
    action.  After construction the action is stored as the actual morphism
    ``rho : R -> End_R(M)``; it is not merely a callback attached to the
    parent.
    """

    Element = GeneralModuleElement

    def __init__(
        self,
        ring,
        carrier,
        *,
        addition,
        zero,
        negation,
        scalar_action=None,
        rho=None,
        verify=True,
    ) -> None:
        if scalar_action is None and rho is None:
            raise TypeError("a module requires either scalar_action(r,x) or rho(r)(x)")
        if scalar_action is not None and rho is not None:
            raise TypeError("supply scalar_action or rho, not both")
        if not callable(addition) or not callable(negation):
            raise TypeError("addition and negation must be callable")

        self._preamble_base_ring = _owned_ring(ring)
        self._preamble_carrier = Set(carrier)
        self._preamble_addition = addition
        self._preamble_zero_value = self._normalize_carrier_value(zero)
        self._preamble_negation = negation
        self._preamble_input_rho = rho
        self._preamble_scalar_callback = scalar_action
        if rho is not None:
            if isinstance(rho, Map):
                if _engine_ring(rho.domain()) is not _engine_ring(self._preamble_base_ring):
                    raise ValueError("the supplied scalar-action morphism has the wrong domain ring")
                self._preamble_raw_scalar_action = (
                    lambda scalar, value: rho(_engine_ring(self._preamble_base_ring)(scalar))(value)
                )
            elif callable(rho):
                self._preamble_raw_scalar_action = lambda scalar, value: rho(scalar)(value)
            else:
                raise TypeError("rho must be a represented morphism or callable ring action")
        else:
            self._preamble_raw_scalar_action = scalar_action


        Parent.__init__(self, category=Modules(self._preamble_base_ring))
        self._preamble_scalar_action_morphism = self._build_scalar_action_morphism()

        register_module_scalar_action(self)
        if verify:
            self._verify_module_laws_when_decidable()

    def base_ring(self):
        return self._preamble_base_ring

    def base(self):
        return self.base_ring()

    def carrier(self):
        return self._preamble_carrier

    underlying_set = carrier

    def _normalize_carrier_value(self, value):
        if isinstance(value, GeneralModuleElement):
            value = value.underlying_element()
        if value not in self._preamble_carrier:
            raise ValueError(f"{value!r} is not in the selected module carrier")
        return value

    def _element_constructor_(self, value):
        if isinstance(value, GeneralModuleElement) and value.parent() is self:
            return value
        return self.element_class(self, self._normalize_carrier_value(value))

    def __call__(self, value):
        return self._element_constructor_(value)

    def __contains__(self, value) -> bool:
        if isinstance(value, GeneralModuleElement):
            return value.parent() is self
        return value in self.carrier()

    def __iter__(self):
        return (self(value) for value in self.carrier())

    def cardinality(self):
        return cardinal(self.carrier().cardinality())

    def is_finite(self):
        try:
            return bool(self.carrier().is_finite())
        except (AttributeError, NotImplementedError):
            try:
                return bool(self.cardinality().is_finite())
            except (AttributeError, NotImplementedError):
                return Unknown

    def _represented_annihilator_ideal(self):
        r"""Represent the scalar-action kernel by exhaustive finite enumeration.

        This is a private backend for ``scalar_action().kernel()``.  Outside an
        enumerable finite regime a stronger algebra backend is required.
        """
        if self.is_finite() is not True:
            raise NotImplementedError(
                "annihilator of this general module requires a represented finite carrier or a stronger algebra backend"
            )
        engine = _engine_ring(self.base_ring())
        try:
            if not bool(engine.is_finite()):
                raise NotImplementedError
            scalars = tuple(
                self.base_ring()._from_engine_element(engine(scalar))
                for scalar in engine
            )
        except (AttributeError, NotImplementedError, TypeError, ValueError) as error:
            raise NotImplementedError(
                "annihilator of this general module requires an enumerable finite scalar ring"
            ) from error
        zero = self.zero()
        annihilating = tuple(
            scalar
            for scalar in scalars
            if all(self.scalar_multiple(scalar, element) == zero for element in self)
        )
        return self.base_ring().ideal(*(annihilating or (self.base_ring().zero(),)))

    def zero(self):
        return self(self._preamble_zero_value)

    def _add_elements(self, left, right):
        value = self._preamble_addition(
            self(left).underlying_element(),
            self(right).underlying_element(),
        )
        return self(value)

    def _negate_element(self, element):
        return self(self._preamble_negation(self(element).underlying_element()))

    def _raw_scalar_multiple(self, scalar, element):
        value = self._preamble_raw_scalar_action(
            _engine_element(self.base_ring(), self.base_ring()(scalar)),
            self(element).underlying_element(),
        )
        return self(value)

    def _build_scalar_action_morphism(self):

        endomorphisms = Modules(self.base_ring()).End(self)
        return ring_morphism(
            self.base_ring(),
            endomorphisms,
            lambda scalar: endomorphisms.elementwise(
                lambda element: self._raw_scalar_multiple(scalar, element),
                verify_linearity=False,
            ),
        )

    def _ring_morphism_defining_module_action(self):
        return self._preamble_scalar_action_morphism

    def scalar_action_input(self):
        r"""Return the supplied ``rho`` when one was given explicitly."""
        if self._preamble_input_rho is None:
            raise ValueError("this module was supplied by a binary scalar action")
        return self._preamble_input_rho

    def _verify_module_laws_when_decidable(self) -> None:
        try:
            finite = self.is_finite()
            elements = tuple(self) if finite else None
        except (NotImplementedError, TypeError, ValueError):
            finite = False
            elements = None
        if not finite or elements is None:
            _LOGGER.debug(
                "General module over %s accepted without exhaustive carrier-law verification",
                self.base_ring(),
            )
            return

        zero = self.zero()
        for element in elements:
            if element + zero != element or zero + element != element:
                raise ValueError("the selected zero is not an additive identity")
            if element + (-element) != zero:
                raise ValueError("the selected negation does not give additive inverses")
        for left in elements:
            for right in elements:
                if left + right != right + left:
                    raise ValueError("the selected addition is not commutative")
                for third in elements:
                    if (left + right) + third != left + (right + third):
                        raise ValueError("the selected addition is not associative")

        engine = _engine_ring(self.base_ring())
        try:
            if not bool(engine.is_finite()):
                raise NotImplementedError
            scalars = tuple(
                self.base_ring()._from_engine_element(engine(scalar))
                for scalar in engine
            )
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            _LOGGER.debug(
                "Additive group laws for finite carrier %s were exhaustively checked, but "
                "scalar-module laws over non-enumerated/infinite %s were not exhaustive",
                self.carrier(),
                self.base_ring(),
            )
            return

        one = self.base_ring().one()
        zero_scalar = self.base_ring().zero()
        for element in elements:
            if self.scalar_multiple(one, element) != element:
                raise ValueError("1 does not act as the identity on the module")
            if self.scalar_multiple(zero_scalar, element) != zero:
                raise ValueError("0 does not act as zero on the module")
            for scalar in scalars:
                for other in elements:
                    if self.scalar_multiple(scalar, element + other) != (
                        self.scalar_multiple(scalar, element)
                        + self.scalar_multiple(scalar, other)
                    ):
                        raise ValueError("scalar multiplication is not additive in the module variable")
                for second_scalar in scalars:
                    if self.scalar_multiple(scalar + second_scalar, element) != (
                        self.scalar_multiple(scalar, element)
                        + self.scalar_multiple(second_scalar, element)
                    ):
                        raise ValueError("scalar multiplication is not additive in the scalar")
                    if self.scalar_multiple(scalar * second_scalar, element) != self.scalar_multiple(
                        scalar,
                        self.scalar_multiple(second_scalar, element),
                    ):
                        raise ValueError("scalar multiplication is not associative")

    def _repr_(self):
        return f"Module over {self.base_ring()} on carrier {self.carrier()}"


def GeneralModule(
    ring,
    carrier,
    *,
    addition,
    zero,
    negation,
    scalar_action=None,
    rho=None,
    verify=True,
):
    r"""Construct a general represented ``R``-module from its structure data."""
    return GeneralModuleParent(
        ring,
        carrier,
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
    "GeneralModuleElement",
    "GeneralModuleParent",
    "module_from_action",
]
