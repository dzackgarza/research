r"""The exact complex field.

A complex number is ``z = a + b i`` with ``a, b`` real and ``i^2 = -1``;
sums, products, the conjugate ``a - b i``, the absolute value
``|z| = (a^2 + b^2)^{1/2}`` and the reciprocal ``1/z = conj(z)/|z|^2`` are
computed from the two real parts (Stein--Shakarchi [SS03], Ch. 1, §1.1).  So
``CC = RR[x]/(x^2 + 1)`` is the quadratic extension of the exact real field
``RR`` by the class ``i`` of ``x``, free over ``RR`` on ``1, i``, and a
complex number is stored as its pair of exact real coordinates in that basis.
Equality is the conjunction of the two real equalities, so it is decided
exactly when ``RR`` decides both.

The elementary functions are the principal branches of Gamelin [Gam01],
Ch. I: the argument ``Arg z`` in ``(-pi, pi]`` (§2), the square root
``|z|^{1/2} e^{i Arg z / 2}`` (§4), ``e^{a + b i} = e^a (cos b + i sin b)``
(§5), ``Log z = log|z| + i Arg z`` (§6, (6.1)), the power
``z^w = e^{w Log z}`` (§7) and the trigonometric and hyperbolic functions
through ``exp`` (§8).  Approximation is explicit through ``.n()``.
"""

from __future__ import annotations

from sage.arith.numerical_approx import digits_to_bits
from sage.arith.power import generic_power
from sage.categories.rings import Rings as SageRings
from sage.functions.trig import arctan2
from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex
from sage.rings.integer_ring import ZZ
from sage.rings.qqbar import QQbar as SageQQbar
from sage.rings.ring import Field
from sage.structure.element import FieldElement, parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.rings.ring_foundation import (
    ComplexField,
    OwnedFields,
    OwnedRings,
    _OwnedRingBootstrapParent,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_engine_element,
)
from dzack_research.preamble.categories.sets.cardinals import continuum
from dzack_research.preamble.categories.sets.set_categories import UncountableSets
from dzack_research.preamble.logic import Predicate, conjunction, negation
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.rings.real import RR, ExactRealNumber


def _exact_complex(field: ExactComplexField, real_part, imaginary_part) -> ExactComplexNumber:
    r"""The complex number ``a + b i`` of ``field`` with real coordinates ``a`` and ``b``."""
    return field.element_class(field, RR(real_part), RR(imaginary_part))


class ExactComplexNumber(FieldElement):
    r"""A complex number ``a + b i``, stored as its two exact real coordinates."""

    __hash__ = None

    def __init__(self, parent: ExactComplexField, real_part: ExactRealNumber, imaginary_part: ExactRealNumber) -> None:
        self._real_part = real_part
        self._imaginary_part = imaginary_part
        FieldElement.__init__(self, parent)

    def real_part(self) -> ExactRealNumber:
        r"""The real number ``a`` of ``z = a + b i``."""
        return self._real_part

    def imaginary_part(self) -> ExactRealNumber:
        r"""The real number ``b`` of ``z = a + b i``."""
        return self._imaginary_part

    def _symbolic_(self, symbolic_ring):
        r"""``a + b i`` in ``symbolic_ring``, with ``i`` the algebraic number ``QQbar.gen()``.

        A real coordinate that is algebraic is stored as an ``AA`` number, and
        the symbolic ring's own ``I`` lies in ``QQ(i)``, which has no common
        parent with ``AA`` in Sage's coercion model (TRAPS.md); ``QQbar``
        contains ``AA``.
        """
        return symbolic_ring(self._real_part.expression()) + symbolic_ring(SageQQbar.gen()) * symbolic_ring(
            self._imaginary_part.expression()
        )

    def _repr_(self) -> str:
        return repr(self._symbolic_(SR))

    def _latex_(self) -> str:
        return str(latex(self._symbolic_(SR)))

    def __reduce__(self):
        return (_restore_exact_complex, (self._real_part, self._imaginary_part))

    def _integer_(self, integer_ring):
        r"""The integer this complex number is, when its imaginary part is zero and its real part an integer."""
        match self._imaginary_part.is_zero():
            case True:
                return self._real_part._integer_(integer_ring)
            case _:
                raise TypeError(f"{self} is not known to be an integer: its imaginary part is not known to be zero")

    def n(self, prec: int | None = None, digits: int | None = None, algorithm=None):
        r"""An approximation of ``self`` in the rounded complex field of ``prec`` bits."""
        assert algorithm is None, (
            f"the complex number {self} is approximated from its exact real parts; no algorithm is chosen, "
            f"but algorithm={algorithm!r} was given"
        )
        match (prec, digits):
            case (None, None):
                bits = 53
            case (None, _):
                bits = digits_to_bits(digits)
            case _:
                bits = prec
        approximations = ComplexField(bits)
        return _owned_engine_element(
            approximations,
            _engine_ring(approximations)(self._real_part.expression(), self._imaginary_part.expression()),
        )

    numerical_approx = n

    def _add_(self, other):
        return _exact_complex(
            self.parent(),
            self._real_part + other._real_part,
            self._imaginary_part + other._imaginary_part,
        )

    def _sub_(self, other):
        return _exact_complex(
            self.parent(),
            self._real_part - other._real_part,
            self._imaginary_part - other._imaginary_part,
        )

    def _neg_(self):
        return _exact_complex(self.parent(), -self._real_part, -self._imaginary_part)

    def _mul_(self, other):
        r"""``(a + b i)(c + d i) = (ac - bd) + (ad + bc) i`` [SS03, Ch. 1, §1.1]."""
        a, b = self._real_part, self._imaginary_part
        c, d = other._real_part, other._imaginary_part
        return _exact_complex(self.parent(), a * c - b * d, a * d + b * c)

    def __mul__(self, other):
        r"""Use the exact product, or the action on an owned ``CC``-module.

        The coefficient product cannot call the algebra tensor classifier
        whose own linear evaluation uses these coefficients.
        An element of a ring that ``CC`` coerces into keeps its own ring, so
        that ring's product is taken.
        """
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        field = self.parent()
        source = parent(other)
        match source:
            case _ if source is field:
                return ExactComplexNumber._mul_(self, other)
            case _ if source in Modules(field):
                return source.scalar_multiple(self, other)
            case _ if source in OwnedRings() and source.has_coerce_map_from(field):
                return NotImplemented
            case _ if other in field:
                return ExactComplexNumber._mul_(self, field(other))
            case _:
                return NotImplemented

    def _div_(self, other):
        r"""``z / w = z conj(w) / |w|^2`` [SS03, Ch. 1, §1.1]; the real division decides ``w != 0``."""
        a, b = self._real_part, self._imaginary_part
        c, d = other._real_part, other._imaginary_part
        norm = c * c + d * d
        return _exact_complex(self.parent(), (a * c + b * d) / norm, (b * c - a * d) / norm)

    def __invert__(self):
        return self.parent().one() / self

    def inverse_of_unit(self):
        r"""``z^{-1}``: every nonzero complex number is a unit."""
        assert self.is_zero() is False, f"{self} is not known to be a unit of {self.parent()}: it is not known to be nonzero"
        return ~self

    def __pow__(self, exponent, modulus=None):
        r"""``z^n`` by repeated products for an integer ``n``, else ``z^w = e^{w Log z}`` [Gam01, Ch. I, §7]."""
        assert modulus is None, (
            f"cannot compute {self}^{exponent} mod {modulus}: modular exponentiation is not defined on the complex numbers"
        )
        integers = _own_ring(ZZ)
        field = self.parent()
        match exponent:
            case _ if exponent in integers:
                return generic_power(self, int(integers(exponent)))
            case _:
                return (field(exponent) * self.log()).exp()

    def __rpow__(self, base):
        return self.parent()(base) ** self

    def conjugate(self) -> ExactComplexNumber:
        r"""``conj(a + b i) = a - b i`` [SS03, Ch. 1, §1.1]."""
        return _exact_complex(self.parent(), self._real_part, -self._imaginary_part)

    def __abs__(self) -> ExactRealNumber:
        r"""``|a + b i| = (a^2 + b^2)^{1/2}``, a real number [SS03, Ch. 1, §1.1]."""
        return (self._real_part * self._real_part + self._imaginary_part * self._imaginary_part).sqrt()

    def argument(self) -> ExactRealNumber:
        r"""The principal argument ``Arg z`` in ``(-pi, pi]`` of a nonzero ``z`` [Gam01, Ch. I, §2]."""
        assert self.is_zero() is False, f"the argument of {self} is defined only for a nonzero complex number"
        return RR(arctan2(self._imaginary_part.expression(), self._real_part.expression()))

    def sqrt(self) -> ExactComplexNumber:
        r"""The principal square root ``|z|^{1/2} e^{i Arg z / 2}``, and ``0`` at ``0`` [Gam01, Ch. I, §4]."""
        field = self.parent()
        zero = self.is_zero()
        assert zero is True or zero is False, f"the square root of {self} is undecided: it is not decided whether {self} = 0"
        match zero:
            case True:
                return field.zero()
        radius = abs(self).sqrt()
        half_argument = self.argument() / RR(2)
        return _exact_complex(field, radius * half_argument.cos(), radius * half_argument.sin())

    def exp(self) -> ExactComplexNumber:
        r"""``e^{a + b i} = e^a cos b + i e^a sin b`` [Gam01, Ch. I, §5]."""
        modulus = self._real_part.exp()
        return _exact_complex(
            self.parent(),
            modulus * self._imaginary_part.cos(),
            modulus * self._imaginary_part.sin(),
        )

    def log(self, base=None) -> ExactComplexNumber:
        r"""The principal logarithm ``Log z = log|z| + i Arg z`` of a nonzero ``z`` [Gam01, Ch. I, §6, (6.1)]."""
        field = self.parent()
        angle = self.argument()
        principal = _exact_complex(field, abs(self).log(), angle)
        match base:
            case None:
                return principal
            case _:
                return principal / field(base).log()

    def cos(self) -> ExactComplexNumber:
        r"""``cos z = (e^{iz} + e^{-iz}) / 2`` [Gam01, Ch. I, §8]."""
        i = self.parent().imaginary_unit()
        return ((i * self).exp() + (-(i * self)).exp()) / self.parent()(2)

    def sin(self) -> ExactComplexNumber:
        r"""``sin z = (e^{iz} - e^{-iz}) / 2i`` [Gam01, Ch. I, §8]."""
        i = self.parent().imaginary_unit()
        return ((i * self).exp() - (-(i * self)).exp()) / (self.parent()(2) * i)

    def tan(self) -> ExactComplexNumber:
        r"""``tan z = sin z / cos z`` [Gam01, Ch. I, §8]."""
        return self.sin() / self.cos()

    def cosh(self) -> ExactComplexNumber:
        r"""``cosh z = (e^z + e^{-z}) / 2`` [Gam01, Ch. I, §8]."""
        return (self.exp() + (-self).exp()) / self.parent()(2)

    def sinh(self) -> ExactComplexNumber:
        r"""``sinh z = (e^z - e^{-z}) / 2`` [Gam01, Ch. I, §8]."""
        return (self.exp() - (-self).exp()) / self.parent()(2)

    def tanh(self) -> ExactComplexNumber:
        r"""``tanh z = sinh z / cosh z`` [Gam01, Ch. I, §8]."""
        return self.sinh() / self.cosh()

    def __eq__(self, other) -> bool | Predicate:
        r"""``a + b i = c + d i`` exactly when ``a = c`` and ``b = d``."""
        field = self.parent()
        match other:
            case _ if other in field:
                other = field(other)
                return conjunction(
                    (
                        self._real_part == other._real_part,
                        self._imaginary_part == other._imaginary_part,
                    )
                )
            case _:
                return False

    def __ne__(self, other) -> bool | Predicate:
        return negation(self == other)

    def is_zero(self) -> bool | Predicate:
        return self == self.parent().zero()

    def is_one(self) -> bool | Predicate:
        return self == self.parent().one()

    def __bool__(self) -> bool:
        relation = self != self.parent().zero()
        match relation:
            case True | False:
                return relation
            case _:
                raise TypeError(
                    f"the truth value of {self} is undecided: it is not decided whether {self} != 0; use ask(x != 0)"
                )


class ExactComplexField(UniqueRepresentation, Field):
    r"""The field ``CC = RR[x]/(x^2 + 1)`` of complex numbers ``a + b i`` with exact real parts."""

    Element = ExactComplexNumber
    _preamble_owned_ring_parent = True

    def __init__(self) -> None:
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyGeneratedFreeModules,
        )

        regular_algebra = Algebras(self).Associative().Unital().Commutative()
        Field.__init__(
            self,
            self,
            category=Cat().meet(
                (
                    OwnedFields(),
                    UncountableSets(),
                    regular_algebra,
                    FinitelyGeneratedFreeModules(self),
                )
            ),
        )
        realize_owned_category(self)
        from dzack_research.preamble.categories.algebras.algebras import _algebra_from_native_ring

        _algebra_from_native_ring(
            self,
            lambda left, right: ExactComplexNumber._mul_(left, right),
            ExactComplexField.one(self),
            lambda scalar, element: ExactComplexNumber._mul_(self(scalar), self(element)),
        )

    def is_commutative(self) -> bool:
        r"""A field is commutative; answered by the class so ``Modules(CC)`` can place itself during construction."""
        return True

    def _repr_(self) -> str:
        return "Complex Field"

    def _latex_(self) -> str:
        return r"\mathbb{C}"

    def _element_constructor_(self, value, imaginary_part=None) -> ExactComplexNumber:
        r"""``CC(a, b) = a + b i`` for real ``a, b``, or the complex number ``value`` names."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        source = parent(value)
        match source:
            case _ if imaginary_part is not None:
                return _exact_complex(self, value, imaginary_part)
            case _ if source is self:
                return value
            case _ if source in Modules(self) and source.unformed_module() is self:
                return source._element_of_unformed_module(value)
            case _ if source is SR:
                return _exact_complex(self, value.real_part(), value.imag_part())
            case _ if source is SageQQbar:
                return _exact_complex(self, value.real(), value.imag())
            case _ if source in OwnedRings() and _engine_ring(source) is SageQQbar:
                algebraic = _engine_element(source, value)
                return _exact_complex(self, algebraic.real(), algebraic.imag())
            case _:
                return _exact_complex(self, value, RR.zero())

    def __contains__(self, value) -> bool:
        r"""Whether ``value`` names a complex number: a real number, an algebraic number, or ``a + b i`` with real ``a, b``."""
        source = parent(value)
        match source:
            case _ if source is self:
                return True
            case _ if source is SR:
                return value.real_part() in RR and value.imag_part() in RR
            case _ if source is SageQQbar:
                return True
            case _ if source in OwnedRings() and _engine_ring(source) is SageQQbar:
                return True
            case _:
                return value in RR

    def _coerce_map_from_(self, source):
        r"""``RR`` and every ring that coerces into it, and the algebraic numbers, coerce into ``CC``.

        From an owned ring the map is the element of ``source.Mor(CC)`` sending
        each element to the complex number it names, for the reason stated at
        ``ExactRealField._coerce_map_from_``.  A Sage ring is met only when the
        coercion model passes a Python scalar through its Sage parent.  A
        source that is not a ring, such as Python's ``int``, has no map here.
        """
        match source:
            case _ if source in OwnedRings() and (
                _engine_ring(source) is SageQQbar or RR.has_coerce_map_from(source)
            ):
                return source.Mor(self, category=OwnedRings())(lambda value: self(value))
            case _ if source is SageQQbar:
                return True
            case _ if source in SageRings():
                return RR.has_coerce_map_from(source)
            case _:
                return None

    def zero(self) -> ExactComplexNumber:
        return _exact_complex(self, RR.zero(), RR.zero())

    def one(self) -> ExactComplexNumber:
        return _exact_complex(self, RR.one(), RR.zero())

    def characteristic(self):
        return _own_ring(ZZ).zero()

    def is_exact(self) -> bool:
        return True

    def is_finite(self) -> bool:
        return False

    def cardinality(self):
        return continuum

    def fraction_field(self):
        return self

    def _an_element_(self):
        return self.imaginary_unit()

    @cached_method
    def imaginary_unit(self) -> ExactComplexNumber:
        r"""The class ``i`` of ``x`` in ``RR[x]/(x^2 + 1)``, a square root of ``-1``."""
        return _exact_complex(self, RR.zero(), RR.one())

    @cached_method
    def complex_conjugation(self):
        r"""The ring automorphism ``a + b i -> a - b i`` of ``CC``, fixing ``RR`` [SS03, Ch. 1, §1.1]."""
        return self.Mor(self, category=OwnedRings())(lambda z: self(z).conjugate())

    @cached_method
    def real_field_inclusion(self):
        r"""The ring morphism ``RR -> CC``, ``a -> a + 0 i``, along which ``CC`` is a quadratic extension."""
        return RR.Mor(self, category=OwnedRings())(lambda a: self(a))

    def _module_basis_along(self, ring_map):
        r"""``CC`` over ``RR`` along :meth:`real_field_inclusion`: the basis ``1, i``.

        Implements the protected contract declared at
        ``OwnedRings.ParentMethods._module_basis_along``.  ``CC = RR[x]/(x^2+1)``
        with ``x^2 + 1`` monic of degree 2, so ``1, i`` is an ``RR``-basis and
        the coordinates of ``a + b i`` are ``(a, b)``.  A map out of any other
        ring takes the general contract.
        """
        from dzack_research.preamble.categories.modules.native_modules import _power_module_basis

        match ring_map == self.real_field_inclusion():
            case True:
                return _power_module_basis(
                    RR,
                    2,
                    lambda exponent: self.imaginary_unit() ** exponent,
                    lambda element: (self(element).real_part(), self(element).imaginary_part()),
                )
            case _:
                return OwnedRings.ParentMethods._module_basis_along(self, ring_map)


_OwnedRingBootstrapParent.register(ExactComplexField)


CC = ExactComplexField()


def _restore_exact_complex(real_part: ExactRealNumber, imaginary_part: ExactRealNumber) -> ExactComplexNumber:
    return CC(real_part, imaginary_part)


__all__ = [
    "CC",
    "ExactComplexField",
    "ExactComplexNumber",
]
