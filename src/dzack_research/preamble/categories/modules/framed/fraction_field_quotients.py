r"""Fraction-field quotients ``K / a`` as modules over the base ring.

The owned quotient is a parent built through the owned module chain; Sage's
``QmodnZ`` is its private engine and its elements are engine elements, the
shape of the owned ring views.
"""

from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from sage.structure.element import Element
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.refine import realize_owned_category, refine
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.modules.pure.torsion_modules import TorsionModules
from dzack_research.preamble.categories.sets.cardinals import aleph0
from dzack_research.preamble.categories.sets.set_categories import Sets


class FractionFieldQuotients(OwnedCategoryOverBaseRing):
    r"""Modules ``Frac(R) / a`` for a fractional ideal ``a`` of ``R``.

    The active computation engine specializes this construction to
    ``R = ZZ``, where Sage's :class:`QmodnZ` computes ``QQ / n ZZ``.
    """

    class ElementMethods(Element):
        r"""What a class in \(\operatorname{Frac}(R)/R\) is."""

        def __init__(self, parent, backend_element) -> None:
            ModuleElement.__init__(self, parent)
            self._backend_element = backend_element

        def _backend(self):
            return self._backend_element

        def _add_(self, other):
            return self.parent()._from_engine_element(self._backend() + other._backend())

        def _neg_(self):
            return self.parent()._from_engine_element(-self._backend())

        def _lmul_(self, scalar):
            return self.parent()._from_engine_element(
                _engine_element(self.parent().base_ring(), scalar) * self._backend()
            )

        _rmul_ = _lmul_

        def _richcmp_(self, other, op):
            if not other.parent() is self.parent() or other.parent() is not self.parent():
                return NotImplemented
            return richcmp(self._backend(), other._backend(), op)

        def __eq__(self, other):
            return (
                other.parent() is self.parent()
                and other.parent() is self.parent()
                and self._backend() == other._backend()
            )

        def __ne__(self, other):
            return not self == other

        def __hash__(self):
            return hash((id(self.parent()), self._backend()))

        def lift(self):
            r"""Return this class's representative in \(K\) under the chosen section.

            A coset of \(K/R\) has no canonical element.  The section this quotient
            selects is the representative in \([0,n)\), and every caller that lifts
            a discriminant value uses that one.
            """
            fraction_field = self.parent().base_ring().fraction_field()
            return fraction_field._from_engine_element(
                _engine_ring(fraction_field)(self._backend().lift())
            )

        def additive_order(self):
            order = SageZZ(self._backend().additive_order())
            return self.parent().base_ring()._from_engine_element(order)

        def _repr_(self):
            return repr(self._backend())

        def _latex_(self):
            return str(latex(self._backend()))

    def an_object(self):
        r"""``Frac(R)/R``."""
        return FractionFieldQuotient(self.base_ring())

    @classmethod
    def _repr_object_names(cls):
        return "fraction-field quotients"

    def super_categories(self):

        return [FramedModules(self.base_ring())]

    class ParentMethods:

        def __init__(self, engine: QmodnZ, **rest) -> None:
            self._engine = engine
            base_ring = _own_ring(SageZZ)
            field = base_ring.fraction_field()
            self._fraction_field_modulus = field._from_engine_element(SageQQ(engine.n))
            super().__init__(
                base_ring=base_ring,
                module_generating_set=Sets.Δ[aleph0],
                module_generator_function=self._divisibility_chain_generator,
                **rest,
            )
            self._preamble_module_coefficient_function = self._framing_coefficients

        def _framing_coefficients(self, element):
            r"""Return finite support in the chosen factorial divisibility framing."""
            element = self(element)
            if element == self.zero():
                return {}
            field = self.fraction_field()
            representative = self.lift(element)
            denominator = int(representative.denominator())
            factorial = 1
            index = 0
            while factorial % denominator:
                index += 1
                factorial *= index + 1
            coefficient = self.base_ring()(representative * field(factorial))
            label = self.module_generating_set()(index)
            return {} if coefficient == self.base_ring().zero() else {label: coefficient}

        def _from_engine_element(self, value):
            return self.element_class(self, self._engine(value))

        def _engine_element(self, value):
            value = self(value)
            return value._backend()

        def _element_constructor_(self, value):
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return value
            parent = getattr(value, "parent", lambda: None)()
            if parent is not None:
                if parent in OwnedRings():
                    return self._from_engine_element(_engine_element(parent, value))
                if isinstance(value, SageObject):
                    raise TypeError(
                        "raw backend elements are not accepted by the public fraction-field quotient"
                    )
            if isinstance(value, SageObject):
                raise TypeError(
                    "raw backend objects are not accepted by the public fraction-field quotient"
                )
            return self._from_engine_element(value)

        def __call__(self, value):
            r"""Construct a class in ``K/R`` without Sage coercion discovery.

            A session's rational is an element of the owned fraction field, which
            Sage's coercion graph has never heard of, so asking it for a conversion
            map fails before this parent's own constructor is reached.
            """
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            return isinstance(value, self.category().ElementType) and value.parent() is self

        def zero(self):
            return self._from_engine_element(self._engine.zero())

        def an_element(self):
            return self.module_generator(self.module_generating_set()(1))

        def _repr_(self):
            return repr(self._engine)

        def _latex_(self):
            return str(latex(self._engine))
        def base_ring(self):
            return self.base()

        def fraction_field(self):
            return self.base_ring().fraction_field()

        def modulus(self):
            r"""Return a generator of the fractional ideal being quotiented out."""
            return self._fraction_field_modulus

        def lift(self, element):
            r"""Return the selected representative of ``element`` in the fraction field."""
            element = self(element)
            representative = element._backend().lift()
            return self.fraction_field()._from_engine_element(representative)

        def divisibility_chain(self, index):
            r"""Return the chosen cofinal divisibility chain element ``d_index``."""
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "the active divisibility chain is the factorial chain over ZZ"
                )
            return self.base_ring()(int(index) + 1).factorial()

        def _divisibility_chain_generator(self, label):
            r"""Return the class of the reciprocal of the chain element at ``label``."""
            denominator = self.divisibility_chain(label)
            field = self.fraction_field()
            return self(field.one() / field(denominator))

        def projection_from_fraction_field(self):
            r"""Return the quotient map ``Frac(R) -> Frac(R) / a`` as an owned set map.

            The fraction field currently has no canonical ``R``-module structure
            for arbitrary ``R`` at this layer, so the underlying map is stated
            in the owned category of sets rather than returning Sage's coercion
            map.  Module-valued consumers should use the scalar-restricted
            fraction-field module construction.
            """

            return SetMorphism(
                Sets().Mor(self.fraction_field(), self),
                lambda element: self(element),
            )






@cached_function
def _owned_fraction_field_quotient(engine: QmodnZ) -> Parent:
    base_ring = _own_ring(SageZZ)
    placement = [FractionFieldQuotients(base_ring)]
    if not engine.n.is_zero():
        placement.append(TorsionModules(base_ring))
    return object_of(Category.join(placement), engine=engine)


def _from_qmodnz_backend(quotient):
    r"""Return the owned ``QQ / n ZZ`` over the Sage parent ``quotient``."""
    if quotient in FractionFieldQuotients(_own_ring(SageZZ)):
        return quotient
    if not isinstance(quotient, QmodnZ):
        raise TypeError("the active fraction-field quotient engine is Sage's QmodnZ")
    return _owned_fraction_field_quotient(quotient)


def FractionFieldQuotient(base_ring, modulus=1):
    r"""Return ``Frac(base_ring) / modulus*base_ring`` when natively supported."""
    if base_ring not in OwnedRings() or _engine_ring(base_ring) is not SageZZ:
        raise NotImplementedError(
            "the active native fraction-field quotient engine currently implements QQ / n ZZ"
        )
    return _from_qmodnz_backend(QmodnZ(_engine_element(base_ring, base_ring(modulus))))


__all__ = [
    "FractionFieldQuotient",
    "FractionFieldQuotients",
]
