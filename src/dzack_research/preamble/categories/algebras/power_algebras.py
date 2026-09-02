r"""Exterior and divided-power algebras assembled from their graded pieces.

For a finitely presented module ``M`` the authoritative degree pieces are the
module constructions ``Lambda^n(M)`` and ``Gamma^n(M)``.  This module forms
their direct sum as an algebra; no second quotient-ring presentation is kept.
"""

from itertools import count

from sage.categories.category import Category
from sage.categories.enumerated_sets import EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    DividedPowerAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.categories.modules.framed.framed_modules import (
    FramedModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.powers import (
    AlternatingPower,
    DividedPower,
    alternating_power_morphism,
    alternating_power_product,
    divided_power_element,
    divided_power_morphism,
    divided_power_product,
)
from dzack_research.preamble.categories.rings import owned_ring_view
from dzack_research.preamble.categories.sets import aleph0
from dzack_research.preamble.refine import refine


class _GradedPowerGeneratorSet(Parent):
    r"""The selected homogeneous module generators ``(degree, label)``."""

    def __init__(self, algebra) -> None:
        self._algebra = algebra
        if algebra.flavor() == "alternating":
            category = FiniteEnumeratedSets()
        else:
            category = EnumeratedSets()
        Parent.__init__(self, category=category)

    def algebra(self):
        return self._algebra

    def _maximum_degree(self):
        if self.algebra().flavor() == "alternating":
            return len(
                tuple(self.algebra().free_source_module().module_generating_set())
            )
        return None

    def __iter__(self):
        maximum = self._maximum_degree()
        degrees = range(maximum + 1) if maximum is not None else count()
        for degree in degrees:
            piece = self.algebra().graded_piece(degree)
            for label in piece.module_generating_set():
                yield (degree, label)

    def __contains__(self, candidate) -> bool:
        if not isinstance(candidate, tuple) or len(candidate) != 2:
            return False
        degree, label = candidate
        try:
            degree = int(degree)
        except (TypeError, ValueError):
            return False
        if degree < 0:
            return False
        maximum = self._maximum_degree()
        if maximum is not None and degree > maximum:
            return False
        return label in self.algebra().graded_piece(degree).module_generating_set()

    def _element_constructor_(self, candidate):
        degree, label = candidate
        degree = int(degree)
        normalized = (degree, label)
        if normalized not in self:
            raise ValueError(f"{candidate!r} is not a homogeneous generator index")
        return normalized

    def cardinality(self):
        rank = len(tuple(self.algebra().free_source_module().module_generating_set()))
        if self.algebra().flavor() == "alternating":
            return self.algebra().base_ring()(2) ** rank
        if rank == 0:
            return self.algebra().base_ring().one()
        return aleph0

    def __getitem__(self, position):
        if position < 0:
            raise IndexError("homogeneous generator positions are nonnegative")
        for index, label in enumerate(self):
            if index == position:
                return label
        raise IndexError(position)

    def position(self, candidate):
        if candidate not in self:
            raise ValueError(f"{candidate!r} is not a homogeneous generator index")
        for index, label in enumerate(self):
            if label == candidate:
                return index
        raise AssertionError("a represented homogeneous generator must be enumerated")

    index = position

    def _repr_(self):
        return f"Homogeneous generator indices of {self.algebra()}"


class _PowerAlgebraModuleGenerators(Parent):
    def __init__(self, algebra) -> None:
        self._algebra = algebra
        Parent.__init__(self, category=EnumeratedSets())

    def __iter__(self):
        return (
            self._algebra.module_generator(label)
            for label in self._algebra.module_generating_set()
        )

    def __contains__(self, element) -> bool:
        if (
            not isinstance(element, PowerAlgebraElement)
            or element.parent() is not self._algebra
        ):
            return False
        coefficients = element.monomial_coefficients()
        return (
            len(coefficients) == 1
            and next(iter(coefficients.values())) == self._algebra.base_ring().one()
        )

    def cardinality(self):
        return self._algebra.module_generating_set().cardinality()


class PowerAlgebraElement(ModuleElement):
    r"""A finite sum of homogeneous exterior/divided-power components."""

    def __init__(self, parent, components) -> None:
        ModuleElement.__init__(self, parent)
        normalized = {}
        for degree, component in components.items():
            degree = int(degree)
            piece = parent.graded_piece(degree)
            if component.parent() is not piece:
                component = piece(component)
            if component != piece.zero():
                normalized[degree] = component
        self._components = normalized

    def homogeneous_components(self):
        return dict(self._components)

    def homogeneous_component(self, degree):
        degree = int(degree)
        return self._components.get(degree, self.parent().graded_piece(degree).zero())

    def is_homogeneous(self) -> bool:
        return len(self._components) <= 1

    def degree(self):
        if not self._components:
            return 0
        if len(self._components) != 1:
            raise ValueError("a nonhomogeneous element has no single degree")
        return next(iter(self._components))

    def monomial_coefficients(self):
        result = {}
        for degree, component in self._components.items():
            for label, coefficient in module_coefficients(
                component, self.parent().graded_piece(degree)
            ).items():
                result[(degree, label)] = coefficient
        return result

    def _add_(self, other):
        degrees = set(self._components) | set(other._components)
        return self.parent()._from_components(
            {
                degree: self.homogeneous_component(degree)
                + other.homogeneous_component(degree)
                for degree in degrees
            }
        )

    def _neg_(self):
        return self.parent()._from_components(
            {degree: -component for degree, component in self._components.items()}
        )

    def _lmul_(self, scalar):
        return self.parent()._power_algebra_scalar_multiple(scalar, self)

    def _mul_(self, other):
        return self.parent().multiply(self, other)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if (
            not isinstance(other, PowerAlgebraElement)
            or other.parent() is not self.parent()
        ):
            equal = False
        else:
            degrees = set(self._components) | set(other._components)
            equal = all(
                self.homogeneous_component(degree)
                == other.homogeneous_component(degree)
                for degree in degrees
            )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        if not self._components:
            return "0"
        return " + ".join(
            f"[{degree}]({component})"
            for degree, component in sorted(self._components.items())
        )


class PowerAlgebra(Parent):
    r"""The graded algebra ``Lambda(M)`` or ``Gamma(M)``."""

    Element = PowerAlgebraElement

    def __init__(self, module, flavor) -> None:
        if flavor not in {"alternating", "divided"}:
            raise ValueError("power algebra flavor must be alternating or divided")
        self._preamble_free_algebra_source_module = module
        self._flavor = flavor
        self._base_ring = owned_ring_view(module.base_ring())
        self._preamble_algebra_base_ring = self._base_ring
        self._module_generating_set = None
        flavor_category = (
            AlternatingAlgebras(self._base_ring)
            if flavor == "alternating"
            else DividedPowerAlgebras(self._base_ring)
        )
        categories = [
            flavor_category,
            FramedAlgebras(self._base_ring),
            FramedModules(self._base_ring),
        ]
        if module in FinitelyGeneratedFreeModules(self._base_ring):
            categories.extend(
                [FreeAlgebras(self._base_ring), GradedFreeAlgebras(self._base_ring)]
            )
        Parent.__init__(
            self,
            base=self._base_ring,
            category=Category.join(tuple(categories)),
        )
        self._preamble_algebra_generating_set = module.module_generating_set()
        self._preamble_algebra_generator_values = {
            label: self._from_component(1, module.module_generator(label))
            for label in module.module_generating_set()
        }
        refine(self, categories)

    def flavor(self):
        return self._flavor

    def algebra_base_ring(self):
        return self._base_ring

    base_ring = algebra_base_ring

    def engine(self):
        r"""This parent is itself the authoritative arithmetic engine."""
        return self

    def free_source_module(self):
        return self._preamble_free_algebra_source_module

    def algebra_generating_set(self):
        return self.free_source_module().module_generating_set()

    def algebra_generator(self, label):
        return self._from_component(
            1, self.free_source_module().module_generator(label)
        )

    def number_of_algebra_generators(self):
        return self.algebra_generating_set().cardinality()

    def module_generating_set(self):
        if self._module_generating_set is None:
            self._module_generating_set = _GradedPowerGeneratorSet(self)
        return self._module_generating_set

    def module_generator(self, label):
        degree, piece_label = self.module_generating_set()._element_constructor_(label)
        return self._from_component(
            degree, self.graded_piece(degree).module_generator(piece_label)
        )

    def module_generators(self):
        return _PowerAlgebraModuleGenerators(self)

    def linear_combination(self, coefficients):
        by_degree = {}
        for (degree, label), coefficient in coefficients.items():
            if not coefficient:
                continue
            piece = self.graded_piece(degree)
            contribution = piece.scalar_multiple(
                coefficient, piece.module_generator(label)
            )
            by_degree[degree] = by_degree.get(degree, piece.zero()) + contribution
        return self._from_components(by_degree)

    def graded_piece(self, degree):
        degree = int(degree)
        if degree < 0:
            raise ValueError("a graded degree is nonnegative")
        constructor = (
            AlternatingPower if self.flavor() == "alternating" else DividedPower
        )
        return constructor(self.free_source_module(), degree)

    def _from_component(self, degree, component):
        return self.element_class(self, {int(degree): component})

    def _from_components(self, components):
        return self.element_class(self, components)

    def _element_constructor_(self, value):
        if isinstance(value, PowerAlgebraElement):
            if value.parent() is self:
                return value
            raise TypeError("the algebra element belongs to a different power algebra")
        if value in self.free_source_module():
            return self._from_component(1, self.free_source_module()(value))
        try:
            scalar = self.base_ring()(value)
        except (TypeError, ValueError):
            if isinstance(value, dict):
                return self.linear_combination(value)
            raise TypeError(f"{value!r} does not define an element of {self}") from None
        piece = self.graded_piece(0)
        return self._from_component(
            0, piece.scalar_multiple(scalar, piece.module_generator(0))
        )

    def zero(self):
        return self._from_components({})

    def one(self):
        return self(self.base_ring().one())

    def _power_algebra_scalar_multiple(self, scalar, element):
        if element.parent() is not self:
            element = self(element)
        scalar = self.base_ring()(scalar)
        return self._from_components(
            {
                degree: component.parent().scalar_multiple(scalar, component)
                for degree, component in element.homogeneous_components().items()
            }
        )

    def multiply(self, left, right):
        result = self.zero()
        product = (
            alternating_power_product
            if self.flavor() == "alternating"
            else divided_power_product
        )
        for left_degree, left_component in left.homogeneous_components().items():
            for right_degree, right_component in right.homogeneous_components().items():
                component = product(
                    self.free_source_module(),
                    left_degree,
                    left_component,
                    right_degree,
                    right_component,
                )
                result += self._from_component(left_degree + right_degree, component)
        return result

    def divided_power(self, value, exponent):
        if self.flavor() != "divided":
            raise TypeError("divided powers are defined on a divided-power algebra")
        exponent = int(exponent)
        if exponent < 0:
            raise ValueError("a divided-power exponent is nonnegative")
        if exponent == 0:
            return self.one()
        value = self(value)
        if value == self.zero():
            return value if exponent > 0 else self.one()
        if not value.is_homogeneous() or value.degree() != 1:
            raise NotImplementedError(
                "the represented canonical divided-power operation is currently evaluated on degree-one elements"
            )
        return self._from_component(
            exponent,
            divided_power_element(
                self.free_source_module(),
                exponent,
                value.homogeneous_component(1),
            ),
        )

    gamma = divided_power

    def augmentation(self, value):
        value = self(value)
        component = value.homogeneous_component(0)
        coefficients = module_coefficients(component, self.graded_piece(0))
        return self.base_ring()(coefficients.get(0, self.base_ring().zero()))

    def _ring_morphism_defining_algebra_structure(self):
        return SetMorphism(
            Hom(self.base_ring(), self, _OwnedRings()),
            lambda scalar: self(scalar),
        )

    def algebra_structure_morphism(self):
        return self._ring_morphism_defining_algebra_structure()

    def ring_center(self):
        if self.flavor() == "divided":
            return self
        raise NotImplementedError(
            "the ordinary center of an exterior algebra is not represented by a scalar-only shortcut"
        )

    def hom(self, images, codomain=None):
        if codomain is None:
            codomain = images.codomain() if isinstance(images, ModuleMorphism) else None
        if codomain is None:
            raise TypeError("the target power algebra is required")
        return power_algebra_homset(self, codomain)(images)

    def _repr_(self):
        symbol = "Lambda" if self.flavor() == "alternating" else "Gamma"
        return f"{symbol}({self.free_source_module()})"


class PowerAlgebraMorphism(Morphism):
    r"""A morphism induced by a linear map on the degree-one generators."""

    def __init__(self, parent, degree_one_map) -> None:
        Morphism.__init__(self, parent)
        source_module = self.domain().free_source_module()
        target_module = self.codomain().free_source_module()
        if isinstance(degree_one_map, ModuleMorphism):
            if (
                degree_one_map.domain() is not source_module
                or degree_one_map.codomain() is not target_module
            ):
                raise ValueError("the degree-one module map has the wrong endpoints")
            self._degree_one_map = degree_one_map
            return

        def target_component(label):
            image = (
                degree_one_map[label]
                if isinstance(degree_one_map, dict)
                else degree_one_map(label)
            )
            if isinstance(image, PowerAlgebraElement):
                if (
                    image.parent() is not self.codomain()
                    or not image.is_homogeneous()
                    or image.degree() != 1
                ):
                    raise ValueError(
                        "power-algebra generator images must lie in degree one"
                    )
                return image.homogeneous_component(1)
            if image not in target_module:
                raise ValueError(
                    "power-algebra generator images must lie in the target degree-one module"
                )
            return target_module(image)

        self._degree_one_map = module_homset(source_module, target_module)(
            target_component
        )

    def degree_one_map(self):
        return self._degree_one_map

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        result = self.codomain().zero()
        power_map = (
            alternating_power_morphism
            if self.domain().flavor() == "alternating"
            else divided_power_morphism
        )
        for degree, component in element.homogeneous_components().items():
            mapped = power_map(self.degree_one_map(), degree)(component)
            result += self.codomain()._from_component(degree, mapped)
        return result

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if (
            not isinstance(other, PowerAlgebraMorphism)
            or other.codomain() is not self.domain()
        ):
            return NotImplemented
        return power_algebra_homset(other.domain(), self.codomain())(
            self.degree_one_map() * other.degree_one_map()
        )


class PowerAlgebraHomset(Homset):
    Element = PowerAlgebraMorphism

    def __init__(self, domain, codomain) -> None:
        if not isinstance(domain, PowerAlgebra) or not isinstance(
            codomain, PowerAlgebra
        ):
            raise TypeError(
                "a represented power-algebra Hom requires two power algebras"
            )
        if domain.flavor() != codomain.flavor():
            raise ValueError("power-algebra morphisms preserve the construction flavor")
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("power-algebra morphisms require one common base ring")
        Homset.__init__(
            self,
            domain,
            codomain,
            category=Category.join((domain.category(), codomain.category())),
        )

    def _element_constructor_(self, degree_one_map):
        return self.element_class(self, degree_one_map)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        module = self.domain().free_source_module()
        return self(module_homset(module, module).identity())


def power_algebra_homset(domain, codomain):
    return PowerAlgebraHomset(domain, codomain)


_POWER_ALGEBRA_CACHE = {}


def _power_algebra_of(module, flavor):
    key = (id(module), flavor)
    cached = _POWER_ALGEBRA_CACHE.get(key)
    if cached is not None and cached.free_source_module() is module:
        return cached
    result = PowerAlgebra(module, flavor)
    _POWER_ALGEBRA_CACHE[key] = result
    return result


def AlternatingAlgebraOf(module):
    return _power_algebra_of(module, "alternating")


def DividedPowerAlgebraOf(module):
    return _power_algebra_of(module, "divided")


def AlternatingAlgebraOn(base_ring, algebra_generating_set):
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModuleOn,
    )

    return AlternatingAlgebraOf(FreeModuleOn(base_ring, algebra_generating_set))


def DividedPowerAlgebraOn(base_ring, algebra_generating_set):
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModuleOn,
    )

    return DividedPowerAlgebraOf(FreeModuleOn(base_ring, algebra_generating_set))


__all__ = [
    "AlternatingAlgebraOf",
    "AlternatingAlgebraOn",
    "DividedPowerAlgebraOf",
    "DividedPowerAlgebraOn",
    "PowerAlgebra",
    "PowerAlgebraElement",
    "PowerAlgebraHomset",
    "PowerAlgebraMorphism",
    "power_algebra_homset",
]
