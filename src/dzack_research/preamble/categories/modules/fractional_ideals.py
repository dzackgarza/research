r"""Ideals and fractional ideals as modules represented by their inclusions."""

from functools import reduce

from sage.categories.category import Category
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.rings import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    OwnedOrders,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
)
from dzack_research.preamble.refine import refine


class FractionalIdeals(OwnedCategoryOverBaseRing):
    r"""Fractional ideals of an integral domain, as modules in its fraction field."""

    @classmethod
    def _repr_object_names(cls):
        return "fractional ideals"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.modules.subobjects import ModuleSubobjects

        return [Modules(self.base_ring()), ModuleSubobjects(self.base_ring())]

    class ParentMethods:
        def fraction_field(self):
            return self._preamble_fraction_field

        def module_generating_set(self):
            return self._preamble_module_generating_set

        def module_generator(self, label):
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a module-generator label")
            return self.element_class(
                self,
                self._preamble_module_generator_values[labels.position(label)],
            )

        def module_generators(self):
            return finite_ordered_set(
                self.module_generator(label) for label in self.module_generating_set()
            )

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules import FreeModuleOn
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            source = FreeModuleOn(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def scalar_multiple(self, scalar, element):
            if element.parent() is not self:
                element = self(element)
            value = (
                engine_ring(self.base_ring())(scalar)
                * element._inclusion_value()
            )
            return self.element_class(self, value)

        def is_principal(self) -> bool:
            if engine_ring(self.base_ring()) is SageZZ:
                return True
            return _principal_generator_from_integer_module(self) is not None

        def principal_generator(self):
            r"""Return ``a`` with ``I=aR`` when this ideal is principal."""
            if not self.is_principal():
                raise ValueError(f"{self} is not principal")
            if engine_ring(self.base_ring()) is SageZZ:
                return self.fraction_field()(
                    _zz_fractional_generator(self._preamble_module_generator_values)
                )
            generator = _principal_generator_from_integer_module(self)
            if generator is None:
                raise ValueError(f"{self} is not principal")
            return generator

        def inverse(self):
            r"""Return ``I^{-1}={x in K : xI subseteq R}`` for an invertible ideal."""
            if engine_ring(self.base_ring()) is SageZZ:
                value = self.principal_generator()
                if value == 0:
                    raise ZeroDivisionError("the zero fractional ideal is not invertible")
                return FractionalIdeal(self.base_ring(), (value**-1,))
            if not self._preamble_module_generator_values or all(
                value == 0 for value in self._preamble_module_generator_values
            ):
                raise ZeroDivisionError("the zero fractional ideal is not invertible")
            return _inverse_order_fractional_ideal(self)

        def __invert__(self):
            r"""Return the inverse fractional ideal ``I^{-1}``."""
            return self.inverse()

        def sum(self, other):
            r"""Return ``I+J`` inside the common fraction field."""
            if self.base_ring() is not other.base_ring():
                raise ValueError("fractional-ideal sum requires the same base ring")
            integral = (
                self in Ideals(self.base_ring())
                and other in Ideals(self.base_ring())
            )
            if engine_ring(self.base_ring()) is SageZZ:
                values = (
                    tuple(self._preamble_module_generator_values)
                    + tuple(other._preamble_module_generator_values)
                )
                return (
                    Ideal(self.base_ring(), values)
                    if integral
                    else FractionalIdeal(self.base_ring(), values)
                )
            values = (
                tuple(self._preamble_module_generator_values)
                + tuple(other._preamble_module_generator_values)
            )
            return (
                Ideal(self.base_ring(), values)
                if integral
                else FractionalIdeal(self.base_ring(), values)
            )

        def __add__(self, other):
            r"""Return the sum fractional ideal ``I+J``."""
            if other not in FractionalIdeals(self.base_ring()):
                return NotImplemented
            return self.sum(other)

        def intersection(self, other):
            r"""Return ``I intersect J`` inside the common fraction field."""
            if self.base_ring() is not other.base_ring():
                raise ValueError("fractional-ideal intersection requires the same base ring")
            integral = (
                self in Ideals(self.base_ring())
                and other in Ideals(self.base_ring())
            )
            if engine_ring(self.base_ring()) is SageZZ:
                left = self.principal_generator()
                right = other.principal_generator()
                if left == 0 or right == 0:
                    values = (SageQQ.zero(),)
                    return (
                        Ideal(self.base_ring(), values)
                        if integral
                        else FractionalIdeal(self.base_ring(), values)
                    )
                ratio = SageQQ(left / right)
                numerator = abs(ratio.numerator())
                denominator = ratio.denominator()
                values = (left * denominator, right * numerator)
                return (
                    Ideal(self.base_ring(), values)
                    if integral
                    else FractionalIdeal(self.base_ring(), values)
                )
            integer_submodule = _integer_coordinate_submodule(self).intersection(
                _integer_coordinate_submodule(other)
            )
            values = _order_integer_submodule_values(
                self.base_ring(), integer_submodule
            )
            return _fractional_ideal_from_order_values(
                self.base_ring(), values, integral=integral
            )

        def __mul__(self, other):
            r"""Return the product fractional ideal ``IJ``."""
            if other not in FractionalIdeals(self.base_ring()):
                return NotImplemented
            integral = (
                self in Ideals(self.base_ring())
                and other in Ideals(self.base_ring())
            )
            if engine_ring(self.base_ring()) is SageZZ:
                values = (
                    self.principal_generator() * other.principal_generator(),
                )
                return (
                    Ideal(self.base_ring(), values)
                    if integral
                    else FractionalIdeal(self.base_ring(), values)
                )
            values = tuple(
                left * right
                for left in self._preamble_module_generator_values
                for right in other._preamble_module_generator_values
            )
            return _fractional_ideal_from_order_values(
                self.base_ring(),
                values,
                integral=integral,
            )

        def _repr_(self):
            listed = ", ".join(str(value) for value in self._preamble_module_generator_values)
            return f"Fractional ideal ({listed}) of {self.base_ring()}"


class Ideals(OwnedCategoryOverBaseRing):
    r"""Integral ideals ``I <= R``."""

    @classmethod
    def _repr_object_names(cls):
        return "ideals"

    def super_categories(self):
        from dzack_research.preamble.categories.rings.commutative_ideals import (
            CommutativeIdeals,
        )

        return [
            FractionalIdeals(self.base_ring()),
            CommutativeIdeals(self.base_ring()),
        ]

    class ParentMethods:
        def ring(self):
            return self.base_ring()

        def ideal_generators(self):
            return tuple(
                self.base_ring()(value)
                for value in self._preamble_module_generator_values
            )

        gens = ideal_generators

        def _engine_ideal(self):
            engine = engine_ring(self.base_ring())
            return engine.ideal(
                tuple(engine(value) for value in self._preamble_module_generator_values)
            )

        def _repr_(self):
            listed = ", ".join(str(value) for value in self._preamble_module_generator_values)
            return f"Ideal ({listed}) of {self.base_ring()}"


class FractionalIdealElement(ModuleElement):
    r"""An element of a fractional ideal, distinct from its image in the fraction field."""

    def __init__(self, parent, value) -> None:
        ModuleElement.__init__(self, parent)
        self._value = engine_ring(parent.fraction_field())(value)

    def _inclusion_value(self):
        r"""Protected representation contract used only by ``FractionalIdealInclusion``."""
        return self._value

    def _add_(self, other):
        return self.parent()(self._value + other._value)

    def _neg_(self):
        return self.parent()(-self._value)

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        return richcmp(self._value, other._value, op)

    def _repr_(self):
        return repr(self._value)


class FractionalIdealModule(Parent):
    Element = FractionalIdealElement

    _preamble_fraction_field = None
    _preamble_module_generating_set = None
    _preamble_module_generator_values = None
    _preamble_inclusion = None

    def __init__(
        self,
        base_ring,
        fraction_field,
        module_generator_values,
        *,
        integral,
    ) -> None:
        ring = owned_ring_view(base_ring)
        self._preamble_fraction_field = owned_ring_view(fraction_field)
        self._preamble_module_generator_values = tuple(module_generator_values)
        self._preamble_module_generating_set = finite_ordered_set(
            range(len(self._preamble_module_generator_values))
        )
        if engine_ring(ring) is SageZZ:
            values = self._preamble_module_generator_values
            if not values:
                self._preamble_module_coordinate_function = lambda element: ()
            else:
                (principal,) = values

                def principal_coordinates(element):
                    value = (
                        element._inclusion_value()
                        if isinstance(element, FractionalIdealElement)
                        else engine_ring(self._preamble_fraction_field)(element)
                    )
                    if principal == 0:
                        if value != 0:
                            raise ValueError("a nonzero element has no coordinates in the zero ideal")
                        return ()
                    coefficient = SageQQ(value / principal)
                    if coefficient.denominator() != 1:
                        raise ValueError("the element is not in this integral ideal")
                    return (SageZZ(coefficient),)

                self._preamble_module_coordinate_function = principal_coordinates
        categories = [FractionalIdeals(ring)]
        if integral:
            categories.append(Ideals(ring))
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import (
            FinitelyGeneratedModules,
        )

        categories.extend([FramedModules(ring), FinitelyGeneratedModules(ring)])
        Parent.__init__(self, base=ring, category=Category.join(tuple(categories)))
        refine(self, categories)

    def _element_constructor_(self, value):
        if isinstance(value, self.element_class) and value.parent() is self:
            return value
        candidate = engine_ring(self._preamble_fraction_field)(value)
        if candidate not in self:
            raise ValueError(f"{candidate} is not in {self}")
        return self.element_class(self, candidate)

    def __contains__(self, value) -> bool:
        if isinstance(value, self.element_class) and value.parent() is self:
            return True
        try:
            candidate = engine_ring(self._preamble_fraction_field)(value)
        except (TypeError, ValueError):
            return False
        if engine_ring(self.base_ring()) is SageZZ:
            principal = _zz_fractional_generator(self._preamble_module_generator_values)
            if principal == 0:
                return candidate == 0
            return SageQQ(candidate / principal).denominator() == 1
        return bool(
            _order_coordinate_vector(self.base_ring(), candidate)
            in _integer_coordinate_submodule(self)
        )

    def zero(self):
        return self(self._preamble_fraction_field.zero())

    def an_element(self):
        if self._preamble_module_generator_values:
            return self(self._preamble_module_generator_values[0])
        return self.zero()


class FractionalIdealInclusion(ModuleEmbedding):
    r"""The selected monomorphism from an ideal into ``R`` or ``Frac(R)``."""

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        value = element._inclusion_value()
        target = self.codomain()
        from dzack_research.preamble.categories.modules.restricted_scalars import (
            RestrictedScalarsModules,
        )

        if target in RestrictedScalarsModules(self.domain().base_ring()):
            extension_module = target.module_over_extension()
            labels = tuple(extension_module.module_generating_set())
            if len(labels) != 1:
                raise ArithmeticError("the fraction field is not represented as a rank-one module over itself")
            return target(
                extension_module.scalar_multiple(
                    value,
                    extension_module.module_generator(labels[0]),
                )
            )
        return target(self.domain().base_ring()(value))

    def lift(self, element):
        r"""Return the ideal element mapping to ``element`` when it belongs to the ideal."""
        target = self.codomain()
        from dzack_research.preamble.categories.modules.restricted_scalars import (
            RestrictedScalarsModules,
        )

        if target in RestrictedScalarsModules(self.domain().base_ring()):
            if element.parent() is not target:
                element = target(element)
            extension_module = target.module_over_extension()
            labels = tuple(extension_module.module_generating_set())
            if len(labels) != 1:
                raise ArithmeticError("the fraction field is not represented as a rank-one module over itself")
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            coefficients = module_coefficients(
                element.underlying_element(),
                extension_module,
            )
            value = coefficients.get(labels[0], extension_module.base_ring().zero())
        else:
            if element.parent() is not target:
                element = target(element)
            value = element
        return self.domain()(value)

    def is_in_image(self, element) -> bool:
        try:
            self.lift(element)
        except (TypeError, ValueError):
            return False
        return True

    def is_primitive(self) -> bool:
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        if self.codomain() not in FramedModules(self.domain().base_ring()):
            raise NotImplementedError(
                "primitivity of a fractional ideal inside its fraction field is not a finite-presentation question"
            )
        return super().is_primitive()

    def index(self):
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        if self.codomain() not in FramedModules(self.domain().base_ring()):
            raise NotImplementedError(
                "the quotient of the fraction field by a fractional ideal is not generally finite"
            )
        return super().index()


@cached_function
def _fraction_field_as_module(base_ring):
    r"""Return ``Frac(R)`` restricted to an ``R``-module along ``R -> Frac(R)``."""
    from dzack_research.preamble.categories.modules import restrict_scalars, ring_as_module

    ring = owned_ring_view(base_ring)
    field = ring.fraction_field()
    scalar_map = SetMorphism(
        Hom(ring, field, _OwnedRings()),
        lambda scalar: field(scalar),
    )
    return restrict_scalars(ring_as_module(field), scalar_map)


def _fractional_ideal_inclusion(ideal, integral):
    from dzack_research.preamble.categories.modules import ring_as_module
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    target = ring_as_module(ideal.base_ring()) if integral else _fraction_field_as_module(ideal.base_ring())
    images = {}
    for label in ideal.module_generating_set():
        value = ideal.module_generator(label)._inclusion_value()
        if integral:
            value = ideal.base_ring()(value)
            images[label] = value if target is ideal.base_ring() else target((value,))
        else:
            extension_module = target.module_over_extension()
            labels = tuple(extension_module.module_generating_set())
            if len(labels) != 1:
                raise ArithmeticError("the fraction field is not represented as a rank-one module over itself")
            images[label] = target(
                extension_module.scalar_multiple(
                    value,
                    extension_module.module_generator(labels[0]),
                )
            )
    return FractionalIdealInclusion(module_homset(ideal, target), images)


def _zz_fractional_generator(module_generator_values):
    values = tuple(SageQQ(value) for value in module_generator_values)
    if not values or all(value == 0 for value in values):
        return SageQQ.zero()
    denominator = reduce(
        lambda current, value: current.lcm(value.denominator()),
        values,
        SageZZ.one(),
    )
    integral_ideal = SageZZ.ideal(
        tuple(SageZZ(denominator * value) for value in values)
    )
    return SageQQ(integral_ideal.gen()) / denominator


def _order_coordinate_vector(base_ring, value):
    from dzack_research.preamble.tensors import tensor

    ring = owned_ring_view(base_ring)
    field = engine_ring(ring.fraction_field())
    return tensor.vector(SageQQ, tuple(field(value).vector()))


def _integer_to_order_map(order):
    r"""Return the structural ring morphism ``ZZ -> order``."""
    structure_map = order._ring_morphism_defining_algebra_structure()
    assert engine_ring(structure_map.domain()) is SageZZ
    assert structure_map.codomain() is order
    return structure_map


def _underlying_integer_module(ideal):
    r"""Return ``Res_ZZ^O(I)`` for an ``O``-fractional ideal ``I``."""
    order = ideal.base_ring()
    assert order in OwnedOrders()
    return ideal.restrict_scalars(_integer_to_order_map(order))


def _integer_coordinate_submodule(ideal):
    r"""Materialize ``Res_ZZ^O(I)`` inside ``K``'s rational coordinate space."""
    from sage.modules.free_module import span
    from dzack_research.preamble.tensors import tensor

    ring = ideal.base_ring()
    order = engine_ring(ring)
    underlying = _underlying_integer_module(ideal)
    rows = [
        _order_coordinate_vector(
            ring,
            generator.underlying_element()._inclusion_value(),
        )
        for generator in underlying.module_generators()
    ]
    if not rows:
        rows = [tensor.vector(SageQQ, [SageQQ.zero()] * int(order.rank()))]
    return span(rows, SageZZ)


def _order_integer_submodule_values(base_ring, integer_submodule):
    ring = owned_ring_view(base_ring)
    field = engine_ring(ring.fraction_field())
    return tuple(
        field(row) for row in integer_submodule.basis_matrix().rows()
    )


def _fractional_ideal_from_order_values(
    base_ring,
    module_generator_values,
    *,
    integral=False,
):
    ring = owned_ring_view(base_ring)
    order = engine_ring(ring)
    field = engine_ring(ring.fraction_field())
    values = tuple(field(value) for value in module_generator_values)

    ideal = FractionalIdealModule(
        ring,
        ring.fraction_field(),
        values,
        integral=integral,
    )
    ideal._preamble_inclusion = _fractional_ideal_inclusion(ideal, integral)
    if bool(order.is_maximal()) or ideal.is_principal():
        from dzack_research.preamble.categories.modules.pure.projective_modules import (
            ProjectiveModules,
        )

        refine(ideal, ProjectiveModules(ring))
    return ideal


def _principal_generator_from_integer_module(ideal):
    r"""Return a generator of an order fractional ideal, or ``None`` if nonprincipal."""
    from dzack_research.preamble.tensors import tensor

    ring = ideal.base_ring()
    order = engine_ring(ring)
    field = engine_ring(ideal.fraction_field())
    basis_values = _order_integer_submodule_values(
        ring, _integer_coordinate_submodule(ideal)
    )
    if not basis_values:
        return field.zero()

    order_basis_rows = tensor.matrix(
        SageQQ,
        [tuple(field(basis_element).vector()) for basis_element in order.basis()],
    )
    basis_map = order_basis_rows.dual_tensor()
    inverse_basis_map = basis_map.inverse_tensor()
    denominator = SageZZ.one()
    for value in basis_values:
        coordinates = inverse_basis_map * _order_coordinate_vector(ring, value)
        for coefficient in coordinates:
            denominator = denominator.lcm(SageQQ(coefficient).denominator())

    integral_values = tuple(
        order(denominator * value) for value in basis_values
    )
    integral_ideal = order.ideal(integral_values)
    if not bool(integral_ideal.is_principal()):
        return None
    reduced = tuple(integral_ideal.gens_reduced())
    if not reduced:
        return field.zero()
    return field(reduced[0]) / denominator


def _inverse_order_fractional_ideal(ideal):
    r"""Return ``(R:I)`` by intersecting ``g^{-1}R`` for an ``R``-generating set."""
    ring = ideal.base_ring()
    field = engine_ring(ideal.fraction_field())
    nonzero_values = tuple(
        field(value)
        for value in ideal._preamble_module_generator_values
        if field(value) != 0
    )
    if not nonzero_values:
        raise ZeroDivisionError("the zero fractional ideal is not invertible")

    inverse_integer_submodule = _integer_coordinate_submodule(
        FractionalIdeal(ring, (nonzero_values[0] ** -1,))
    )
    for value in nonzero_values[1:]:
        inverse_integer_submodule = inverse_integer_submodule.intersection(
            _integer_coordinate_submodule(FractionalIdeal(ring, (value**-1,)))
        )
    values = _order_integer_submodule_values(ring, inverse_integer_submodule)
    return _fractional_ideal_from_order_values(
        ring,
        values,
    )


def _fractional_ideal_from_backend(base_ring, backend, *, integral=False):
    ring = owned_ring_view(base_ring)
    assert engine_ring(ring) is SageZZ
    principal = SageQQ(backend)
    values = () if principal == 0 else (principal,)
    ideal = FractionalIdealModule(
        ring,
        owned_ring_view(SageQQ),
        values,
        integral=integral,
    )
    ideal._preamble_inclusion = _fractional_ideal_inclusion(ideal, integral)
    from dzack_research.preamble.categories.modules.pure.projective_modules import (
        ProjectiveModules,
    )

    refine(ideal, ProjectiveModules(ring))
    return ideal


def FractionalIdeal(base_ring, module_generating_set):
    r"""Return the fractional ideal of ``R`` spanned by the stated elements of ``Frac(R)``."""
    ring = owned_ring_view(base_ring)
    values = tuple(module_generating_set)
    engine = engine_ring(ring)
    if engine is SageZZ:
        return _fractional_ideal_from_backend(
            ring,
            _zz_fractional_generator(values),
            integral=False,
        )
    if ring not in OwnedOrders():
        raise NotImplementedError(
            "the active nonprincipal fractional-ideal engine currently requires ZZ or a number-field order"
        )
    field = engine_ring(ring.fraction_field())
    field_values = tuple(field(value) for value in values)
    return _fractional_ideal_from_order_values(
        ring,
        field_values,
        integral=False,
    )


def Ideal(base_ring, module_generating_set):
    r"""Return the integral ideal of ``R`` generated by the stated elements."""
    ring = owned_ring_view(base_ring)
    engine = engine_ring(ring)
    values = tuple(engine(value) for value in module_generating_set)
    backend = engine.ideal(values)
    if engine is SageZZ:
        ideal = FractionalIdealModule(
            ring,
            ring.fraction_field(),
            tuple(backend.gens()),
            integral=True,
        )
        ideal._preamble_inclusion = _fractional_ideal_inclusion(ideal, True)
        from dzack_research.preamble.categories.modules.pure.projective_modules import (
            ProjectiveModules,
        )

        refine(ideal, ProjectiveModules(ring))
        return ideal
    if ring not in OwnedOrders():
        raise NotImplementedError(
            "the active owned ideal-module adapter currently handles ZZ and number-field orders"
        )
    field = engine_ring(ring.fraction_field())
    field_values = tuple(field(value) for value in values)
    return _fractional_ideal_from_order_values(
        ring,
        field_values,
        integral=True,
    )


__all__ = [
    "FractionalIdeal",
    "FractionalIdeals",
    "Ideal",
    "Ideals",
]
