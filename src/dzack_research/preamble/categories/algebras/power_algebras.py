r"""Exterior and divided-power algebras assembled from their graded pieces.

For a finitely presented module ``M`` the authoritative degree pieces are the
module constructions ``Lambda^n(M)`` and ``Gamma^n(M)``.  This module forms
their direct sum as an algebra; no second quotient-ring presentation is kept.
"""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring as _engine_ring

from sage.misc.cachefunc import cached_function
from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism

from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    DividedPowerAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
)
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
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
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.refine import refine


class PowerAlgebraElement(GradedDirectSumElement):
    r"""An element of a power algebra, using graded-direct-sum storage."""

    def _mul_(self, other):
        return self.parent().multiply(self, other)


class PowerAlgebra(GradedDirectSumModule):
    r"""The graded algebra ``Lambda(M)`` or ``Gamma(M)``."""

    Element = PowerAlgebraElement

    def __init__(self, module, flavor) -> None:
        if flavor not in {"alternating", "divided"}:
            raise ValueError("power algebra flavor must be alternating or divided")
        self._preamble_free_algebra_source_module = module
        self._flavor = flavor
        base = _owned_ring(module.base_ring())
        self._preamble_algebra_base_ring = base

        constructor = AlternatingPower if flavor == "alternating" else DividedPower
        degree_index_set = None
        if flavor == "alternating" and module in FinitelyGeneratedFreeModules(base):
            from dzack_research.preamble.categories.sets.set_categories import Sets

            degree_index_set = Sets.Δ[int(module.rank())]

        GradedDirectSumModule.__init__(
            self,
            base,
            lambda degree: constructor(module, int(degree)),
            name=(f"Lambda({module})" if flavor == "alternating" else f"Gamma({module})"),
            degree_index_set=degree_index_set,
        )

        flavor_category = (
            AlternatingAlgebras(base)
            if flavor == "alternating"
            else DividedPowerAlgebras(base)
        )
        categories = [flavor_category, FramedAlgebras(base)]
        if module in FinitelyGeneratedFreeModules(base):
            categories.extend([FreeAlgebras(base), GradedFreeAlgebras(base)])
        self._preamble_algebra_generating_set = module.module_generating_set()
        from dzack_research.preamble.categories.sets.indexed_families import indexed_family

        self._preamble_algebra_generator_values = indexed_family(
            self._preamble_algebra_generating_set,
            lambda label: self.from_component(1, module.module_generator(label)),
            name=f"Algebra generator values of {self}",
        )
        refine(self, categories)

    def flavor(self):
        return self._flavor

    def algebra_base_ring(self):
        return self.base_ring()

    def free_source_module(self):
        return self._preamble_free_algebra_source_module

    def _power_algebra_homset(self, codomain):
        r"""Return the concrete Hom parent for two compatible power algebras."""
        if not isinstance(codomain, PowerAlgebra) or codomain.flavor() != self.flavor():
            raise TypeError("power-algebra Hom requires two algebras of one flavor")
        return power_algebra_homset(self, codomain)

    def algebra_generating_set(self):
        return self.free_source_module().module_generating_set()

    def algebra_generator(self, label):
        return self.from_component(
            1, self.free_source_module().module_generator(label)
        )

    def number_of_algebra_generators(self):
        return self.algebra_generating_set().cardinality()

    _from_component = GradedDirectSumModule.from_component
    _from_components = GradedDirectSumModule.from_components

    def __call__(self, value):
        r"""Construct an element through the owned graded-algebra parser."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, GradedDirectSumElement):
            if value.parent() is self:
                return value
            raise TypeError("the algebra element belongs to a different power algebra")
        if value in self.free_source_module():
            return self.from_component(1, self.free_source_module()(value))
        try:
            scalar = self.base_ring()(value)
        except (TypeError, ValueError):
            if isinstance(value, dict):
                return GradedDirectSumModule._element_constructor_(self, value)
            raise TypeError(f"{value!r} does not define an element of {self}") from None
        piece = self.graded_piece(0)
        return self.from_component(
            0, piece.scalar_multiple(scalar, piece.module_generator(0))
        )

    def one(self):
        return self(self.base_ring().one())

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
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
                result += self.from_component(
                    left_degree + right_degree, component
                )
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
            return value
        if not value.is_homogeneous() or value.degree() != 1:
            raise NotImplementedError(
                "the represented canonical divided-power operation is currently evaluated on degree-one elements"
            )
        return self.from_component(
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
        return ring_morphism(
            self.base_ring(),
            self,
            lambda scalar: self(scalar),
        )

    algebra_structure_morphism = _ring_morphism_defining_algebra_structure

    def ring_center(self):
        if self.flavor() == "divided":
            return self
        raise NotImplementedError(
            "the ordinary center of an exterior algebra is not represented by a scalar-only shortcut"
        )

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


class PowerAlgebraHomset(CategoricalHomset):
    Element = PowerAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
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
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def _element_constructor_(self, degree_one_map):
        return self.element_class(self, degree_one_map)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        module = self.domain().free_source_module()
        return self(module_homset(module, module).identity())


def power_algebra_homset(domain, codomain):
    category = (
        AlternatingAlgebras(domain.base_ring())
        if domain.flavor() == "alternating"
        else DividedPowerAlgebras(domain.base_ring())
    )
    return category.Mor(domain, codomain)


@cached_function(key=lambda module, flavor: (id(module), flavor))
def _power_algebra_of(module, flavor):
    result = PowerAlgebra(module, flavor)
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
