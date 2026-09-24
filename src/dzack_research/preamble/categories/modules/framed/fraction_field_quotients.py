r"""Fraction-field quotients ``K / a`` as modules over the base ring.

The owned quotient is a parent built through the owned module chain; Sage's
``QmodnZ`` is its private engine and its elements are engine elements, the
shape of the owned ring views.
"""

from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation

from sage.arith.functions import lcm
from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
    _torsion_module_presented_by_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import aleph0
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class FractionFieldQuotients(OwnedCategoryOverBaseRing):
    r"""Modules ``Frac(R) / a`` for a fractional ideal ``a`` of ``R``.

    The active computation engine specializes this construction to
    ``R = ZZ``, where Sage's :class:`QmodnZ` computes ``QQ / n ZZ``.
    """

    class ElementMethods(ModuleElement):
        r"""What a class in \(\operatorname{Frac}(R)/R\) is.

        A class in \(K/R\) is an element of a module over \(R\), so it
        subtracts and is scaled like one.  ``Element`` leaves ``x - y``
        raising, and the polarization \(q(x+y)-q(x)-q(y)\) of a discriminant
        quadratic form is one of the places that reaches it.
        """

        def __init__(self, parent, backend_element) -> None:
            ModuleElement.__init__(self, parent)
            self._backend_element = backend_element

        def _backend(self):
            return self._backend_element

        def _add_(self, other):
            return _owned_engine_element(self.parent(), self._backend() + other._backend())

        def _neg_(self):
            return _owned_engine_element(self.parent(), -self._backend())

        def _lmul_(self, scalar):
            return _owned_engine_element(self.parent(),
                _engine_element(self.parent().base_ring(), scalar) * self._backend()
            )

        _rmul_ = _lmul_

        def __rmul__(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _richcmp_(self, other, op):
            if other.parent() is not self.parent() or other.parent() is not self.parent():
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
            return _owned_engine_element(fraction_field,
                _engine_ring(fraction_field)(self._backend().lift())
            )

        def additive_order(self):
            order = SageZZ(self._backend().additive_order())
            return _owned_engine_element(self.parent().base_ring(), order)

        def _repr_(self):
            return f"[{self.lift()}] in {self.parent()}"

        def _latex_(self):
            return rf"[{self.lift()}]\in {self.parent()}"

    def an_object(self):
        r"""``Frac(R)/R``."""
        return self()

    def _call_(self, modulus=1):
        r"""Return ``Frac(R) / modulus*R`` when the selected engine supports it."""
        base_ring = self.base_ring()
        assert _engine_ring(base_ring) is SageZZ, (
            f"cannot form Frac(R)/nR for R = {base_ring}: this quotient is computed only "
            "for R = ZZ, i.e. QQ/nZZ"
        )
        return _from_qmodnz_backend(
            QmodnZ(_engine_element(base_ring, base_ring(modulus)))
        )

    @classmethod
    def _repr_object_names(cls):
        return "fraction-field quotients"

    def super_categories(self):

        return [FramedModules(self.base_ring())]

    class ParentMethods:
        _derived_construction_parameters = frozenset({"base_ring"})

        def __init__(self, engine: QmodnZ, **rest) -> None:
            self._engine = engine
            base_ring = _own_ring(SageZZ)
            field = base_ring.fraction_field()
            self._fraction_field_modulus = _owned_engine_element(field, SageQQ(engine.n))
            super().__init__(
                base_ring=base_ring,
                module_generating_set=Sets.Δ[aleph0],
                module_generator_function=self._divisibility_chain_generator,
                **rest,
            )

        def _selected_module_coefficients(self, element):
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
                        f"cannot convert {value!r} into {self}: it is an element of {parent}, "
                        "which is not a ring of this session"
                    )
            if isinstance(value, SageObject):
                raise TypeError(
                    f"cannot convert {value!r} into {self}: it is not a number or an element "
                    "of a ring of this session"
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
            return f"{self.fraction_field()} / ({self.modulus()}){self.base_ring()}"

        def _latex_(self):
            return rf"{self.fraction_field()} / ({self.modulus()}){self.base_ring()}"
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
            return _owned_engine_element(self.fraction_field(), representative)

        def divisibility_chain(self, index):
            r"""Return the chosen cofinal divisibility chain element ``d_index``."""
            assert _engine_ring(self.base_ring()) is SageZZ, (
                f"no cofinal divisibility chain for {self}: the chain d_k = (k+1)! is "
                f"defined only over ZZ, and the base ring is {self.base_ring()}"
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

        def subobject_on(self, module_generators):
            r"""Return the cyclic submodule generated by finitely many classes.

            For ``QQ / n ZZ`` with ``n != 0``, let ``x_1,...,x_r`` be the
            selected lifts.  The subgroup of ``QQ`` generated by these lifts
            and ``n`` is ``g ZZ`` for one positive rational ``g``.  Hence the
            generated submodule is

            ``g ZZ / n ZZ ~= ZZ / (n/g) ZZ``.

            The source is returned as an actual module subobject carrying its
            inclusion into this quotient.  This PID classification is the
            reason the operation is exact despite the ambient module's
            countable framing.
            """
            classes = tuple(self(element) for element in module_generators)
            assert not self.modulus().is_zero(), (
                f"cannot classify the submodule of {self} generated by {classes}: the "
                "classification gZZ/nZZ ~= ZZ/(n/g)ZZ needs a nonzero modulus n, and here n = 0 "
                "(a finitely generated submodule of QQ itself is free)"
            )

            field = self.fraction_field()
            values = tuple(self.lift(element) for element in classes) + (
                self.modulus(),
            )
            denominator = lcm(tuple(int(value.denominator()) for value in values))
            numerators = tuple(
                SageZZ(_engine_element(field, value) * denominator)
                for value in values
            )
            generator_numerator = abs(gcd(numerators))
            generator = _owned_engine_element(field,
                SageQQ(generator_numerator) / SageQQ(denominator)
            )
            # ``g`` divides every lift and the modulus, so ``n/g`` is integral.
            order_in_field = self.modulus() / generator
            assert int(order_in_field.denominator()) == 1, (
                f"the submodule of {self} generated by {classes} is gZZ/nZZ with g = {generator}, "
                f"but g does not divide the modulus n = {self.modulus()}: n/g = {order_in_field} "
                "is not an integer"
            )
            order = self.base_ring()(order_in_field)
            cyclic = _torsion_module_presented_by_matrix(
                ((order,),),
                base_ring=self.base_ring(),
            )
            label = cyclic.module_generating_set()[0]
            image = self(generator)

            def lift_from_ambient(subobject, element):
                # ``[x]`` lies in ``gZ/nZ`` exactly when the lift ``x`` lies in
                # ``gZ + nZ = gZ``, that is when ``x/g`` is integral.
                element = self(element)
                quotient = self.lift(element) / generator
                if int(quotient.denominator()) != 1:
                    return None
                return subobject.scalar_multiple(
                    self.base_ring()(quotient),
                    subobject.module_generator(label),
                )

            subobject = ModulesWithChosenFinitePresentation(self.base_ring())(
                cyclic.presentation(),
                category=Category.join((
                    ModuleSubobjects(self.base_ring()),
                    Modules(self.base_ring()).FinitelyPresented().Torsion(),
                )),
                subobject_ambient=self,
                subobject_generator_images=lambda _label: image,
                subobject_lift=lift_from_ambient,
            )
            return subobject






@cached_function
def _owned_fraction_field_quotient(engine: QmodnZ) -> Parent:
    base_ring = _own_ring(SageZZ)
    placement = [FractionFieldQuotients(base_ring)]
    if not engine.n.is_zero():
        placement.append(Modules(base_ring).Torsion())
    return _object_of(Category.join(placement), engine=engine)


def _from_qmodnz_backend(quotient):
    r"""Return the owned ``QQ / n ZZ`` over the Sage parent ``quotient``."""
    if quotient in FractionFieldQuotients(_own_ring(SageZZ)):
        return quotient
    if not isinstance(quotient, QmodnZ):
        raise TypeError(f"{quotient!r} is not a quotient QQ/nZZ")
    return _owned_fraction_field_quotient(quotient)


__all__ = [
    "FractionFieldQuotients",
]
