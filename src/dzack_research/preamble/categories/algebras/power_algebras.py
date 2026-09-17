r"""Exterior and divided-power algebras assembled from their graded pieces.

For a finitely presented module ``M`` the authoritative degree pieces are the
module constructions ``Lambda^n(M)`` and ``Gamma^n(M)``.  This module forms
their direct sum as an algebra; no second quotient-ring presentation is kept.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function
from sage.misc.unknown import Unknown
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras, FramedAlgebras, _algebra_on_module
from dzack_research.preamble.categories.algebras.graded_algebras import _graded_multiplication_from_components
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


class _PowerAlgebraConstruction:
    r"""The selected source module and flavor defining one power algebra."""

    def __init__(self, source_module, flavor) -> None:
        self._source_module = source_module
        self._flavor = flavor

    def source_module(self):
        return self._source_module

    def flavor(self):
        return self._flavor


class _PowerAlgebra:
    r"""The power construction on a graded module, without duplicate arithmetic."""

    def __init__(self, power_algebra_construction, **rest) -> None:
        self._power_algebra_construction = power_algebra_construction
        super().__init__(**rest)

    def power_algebra_construction(self):
        return self._power_algebra_construction

    def flavor(self):
        return self.power_algebra_construction().flavor()

    def free_source_module(self):
        return self.power_algebra_construction().source_module()

    def _power_algebra_homset_class(self):
        return PowerAlgebraHomset

    def algebra_generating_set(self):
        match self.flavor():
            case "alternating":
                return self.free_source_module().module_generating_set()
            case "divided":
                # Degree-one elements alone need not generate Gamma over Z.
                # A module generating family is also an algebra generating family.
                return self.module_generating_set()

    def algebra_generator(self, label):
        source = self.free_source_module()
        match label:
            case _ if label in source.module_generating_set():
                return self.from_component(1, source.module_generator(label))
            case _:
                return self.module_generator(self.algebra_generating_set()(label))

    def _element_constructor_(self, value):
        source = element_parent(value)
        match value:
            case _ if source is self:
                return value
            case _ if source is self.free_source_module():
                return self.from_component(1, value)
            case dict():
                return super()._element_constructor_(value)
            case _ if value in self.base_ring():
                return self.scalar_multiple(self.base_ring()(value), self.one())
            case _:
                return super()._element_constructor_(value)

    def is_commutative(self):
        match self.flavor():
            case "divided":
                return True
            case _:
                size = self.free_source_module().module_generating_set().cardinality()
                if (self.base_ring()(2) == self.base_ring().zero()) is True:
                    return True
                if size.is_finite() and int(size.finite_value()) <= 1:
                    return True
                return Unknown

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
        assert value.is_homogeneous() and value.degree() == 1, (
            "the represented canonical divided-power operation is evaluated on homogeneous degree-one elements"
        )
        return self.from_component(
            exponent,
            self.free_source_module().divided_power_element(
                exponent,
                value.homogeneous_component(1),
            ),
        )

    gamma = divided_power

    def augmentation(self, value):
        value = self(value)
        component = value.homogeneous_component(0)
        coefficients = self.graded_piece(0).framing_coefficients(component)
        return self.base_ring()(coefficients.get(0, self.base_ring().zero()))

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
            if degree_one_map.domain() is not source_module or degree_one_map.codomain() is not target_module:
                raise ValueError("the degree-one module map has the wrong endpoints")
            self._degree_one_map = degree_one_map
            return

        def target_component(label):
            image = degree_one_map[label] if isinstance(degree_one_map, dict) else degree_one_map(label)
            if element_parent(image) is self.codomain():
                if not image.is_homogeneous() or image.degree() != 1:
                    raise ValueError("power-algebra generator images must lie in degree one")
                return image.homogeneous_component(1)
            if image not in target_module:
                raise ValueError("power-algebra generator images must lie in the target degree-one module")
            return target_module(image)

        self._degree_one_map = source_module.module_category().Mor(source_module, target_module)(target_component)

    def degree_one_map(self):
        return self._degree_one_map

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        result = self.codomain().zero()
        degree_one_map = self.degree_one_map()
        for degree, component in element.homogeneous_components().items():
            match self.domain().flavor():
                case "alternating":
                    mapped = degree_one_map.exterior_power(degree)(component)
                case "divided":
                    mapped = degree_one_map.divided_power(degree)(component)
            result += self.codomain().from_component(degree, mapped)
        return result

    def __call__(self, element):
        return self._call_(element)

    def is_identity(self) -> bool:
        return bool(getattr(self, "_preamble_is_identity", False))

    def __mul__(self, other):
        if not isinstance(other, PowerAlgebraMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        return other.domain().Mor(self.codomain())(self.degree_one_map() * other.degree_one_map())


class PowerAlgebraHomset(CategoricalHomset):
    Element = PowerAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        category = hom_family.base_category()
        assert domain in category and codomain in category, "power-algebra arrows use the stated category"
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
        identity = self(module.module_category().Mor(module, module).identity())
        identity._preamble_is_identity = True
        return identity



def PowerAlgebraElement(parent, components):
    r"""Construct a power-algebra element from homogeneous components."""
    return parent.from_components(components)


def PowerAlgebra(module, flavor):
    r"""The named power construction, through its category entry."""
    from dzack_research.preamble.categories.algebras.free_algebras import AlternatingAlgebras, DividedPowerAlgebras

    match flavor:
        case "alternating":
            return AlternatingAlgebras(module.base_ring())(module)
        case "divided":
            return DividedPowerAlgebras(module.base_ring())(module)
        case _:
            raise ValueError("power algebra flavor must be alternating or divided")


@cached_function(key=lambda source, flavor: (id(source), flavor))
def _power_algebra_of(source, flavor):
    r"""The graded sum and product of the module's exterior or divided powers.

    The degree owners supply the wedge/divided product, including their
    relations; distributive extension is the shared graded-algebra classifier.
    See Mathlib LinearAlgebra/ExteriorAlgebra/Basic and Algebra/DirectSum/Ring;
    divided-power multiplication uses the identities in Stacks, Tag 07GL.
    """
    from dzack_research.preamble.categories.algebras.free_algebras import AlternatingAlgebras, DividedPowerAlgebras

    ring = source.base_ring()
    graded = GradedModules(ring)
    match flavor:
        case "alternating":
            category = AlternatingAlgebras(ring)
            power = source.exterior_power
            product = source.exterior_power_product
        case "divided":
            category = DividedPowerAlgebras(ring)
            power = source.divided_power_module
            product = source.divided_power_product
        case _:
            raise ValueError("power algebra flavor must be alternating or divided")

    def piece(degree):
        match degree < 0:
            case True:
                return ring.free_module(0)
            case False:
                return power(degree)

    module = graded(indexed_family(graded.grading_monoid(), piece), placements=(FramedModules(ring),))
    multiplication = _graded_multiplication_from_components(module, product)
    unit = module.from_component(0, module.graded_piece(0).module_generator(0))
    return _algebra_on_module(
        module, multiplication, placement=(category, FramedAlgebras(ring)), unit=unit,
        construction_data={"power_algebra_construction": _PowerAlgebraConstruction(source, flavor)},
    )


def _alternating_algebra_of(module):
    return PowerAlgebra(module, "alternating")


def _divided_power_algebra_of(module):
    return PowerAlgebra(module, "divided")


def _alternating_extension(module_morphism):
    r"""Extend an alternating linear map uniquely to ``Lambda(M) -> A``.

    The target is an arbitrary represented unital associative algebra over the
    same base ring.  The selected generator images must square to zero and
    anticommute, exactly the relations defining the exterior algebra.  The
    current verification is finite-framing based; no finite subset is sampled
    from an infinite framing.
    """
    from dzack_research.preamble.categories.algebras.algebras import Algebras
    from dzack_research.preamble.categories.algebras.comparison_maps import (
        _construction_algebra_homset,
    )

    if not isinstance(module_morphism, ModuleMorphism):
        raise TypeError("an alternating extension starts from a represented module morphism")
    module = module_morphism.domain()
    target = module_morphism.codomain()
    base = module.base_ring()
    if target not in Algebras(base).Associative().Unital():
        raise TypeError("an alternating extension requires a unital associative algebra target")
    labels = module.module_generating_set()
    cardinality = labels.cardinality()
    if not cardinality.is_finite():
        raise NotImplementedError(
            "verification of the exterior-algebra relations currently requires a finite selected framing"
        )
    labels = tuple(labels)
    images = {
        label: target(module_morphism(module.module_generator(label)))
        for label in labels
    }
    zero = target.zero()
    if any(image * image != zero for image in images.values()):
        raise ValueError("alternating generator images must square to zero")
    if any(
        images[left] * images[right] + images[right] * images[left] != zero
        for position, left in enumerate(labels)
        for right in labels[position + 1 :]
    ):
        raise ValueError("alternating generator images must anticommute")

    source = module.exterior_algebra()

    def evaluate(element):
        element = source(element)
        result = target.zero()
        for degree, component in element.homogeneous_components().items():
            piece = source.graded_piece(degree)
            for basis_label, coefficient in piece.framing_coefficients(component).items():
                if degree == 0:
                    value = target.one()
                elif degree == 1:
                    value = images[basis_label]
                else:
                    value = target.one()
                    for generator_label in basis_label:
                        value *= images[generator_label]
                result += coefficient * value
        return result

    return _construction_algebra_homset(source, target)(evaluate)


__all__ = [
    "PowerAlgebra",
    "PowerAlgebraElement",
    "PowerAlgebraHomset",
    "PowerAlgebraMorphism",
]
