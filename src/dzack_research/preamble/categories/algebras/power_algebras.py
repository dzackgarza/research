r"""Exterior and divided-power algebras assembled from their graded pieces.

For a finitely presented module ``M`` the authoritative degree pieces are the
module constructions ``Lambda^n(M)`` and ``Gamma^n(M)``.  This module forms
their direct sum as an algebra; no second quotient-ring presentation is kept.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebraStructureConstruction,
    FramedAlgebras,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    DividedPowerAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
)
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _owned_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring as _engine_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class _PowerAlgebraConstruction:
    r"""The selected source module and flavor defining one power algebra."""

    def __init__(self, source_module, flavor) -> None:
        self._source_module = source_module
        self._flavor = flavor

    def source_module(self):
        return self._source_module

    def flavor(self):
        return self._flavor


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
        self._power_algebra_construction = _PowerAlgebraConstruction(module, flavor)
        base = _owned_ring(module.base_ring())
        self._algebra_structure_construction = AlgebraStructureConstruction(base)

        match flavor:
            case "alternating":
                component_constructor = module.exterior_power
            case "divided":
                component_constructor = module.divided_power_module
        degree_index_set = None
        if flavor == "alternating":
            generator_count = module.module_generating_set().cardinality()
            if generator_count.is_finite():
                degree_index_set = Sets.Δ[int(generator_count.finite_value())]

        flavor_category = AlternatingAlgebras(base) if flavor == "alternating" else DividedPowerAlgebras(base)
        categories = [flavor_category, FramedAlgebras(base)]
        if module in FinitelyGeneratedFreeModules(base):
            categories.extend([FreeAlgebras(base), GradedFreeAlgebras(base)])
        self._preamble_algebra_generating_set = module.module_generating_set()

        self._preamble_algebra_generator_values = indexed_family(
            self._preamble_algebra_generating_set,
            lambda label: self.from_component(1, module.module_generator(label)),
            name="Power-algebra generator values",
        )
        GradedDirectSumModule.__init__(
            self,
            base,
            lambda degree: component_constructor(int(degree)),
            name=(f"Lambda({module})" if flavor == "alternating" else f"Gamma({module})"),
            degree_index_set=degree_index_set,
            extra_categories=tuple(categories),
        )

    def is_commutative(self) -> bool:
        r"""Divided powers commute; an alternating algebra commutes on at most one generator or in characteristic two."""
        if self.flavor() == "divided":
            return True
        generators = self._preamble_algebra_generating_set.cardinality()
        if generators.is_finite() and int(generators.finite_value()) <= 1:
            return True
        return int(self.base_ring().characteristic()) == 2

    def power_algebra_construction(self):
        return self._power_algebra_construction

    def flavor(self):
        return self.power_algebra_construction().flavor()

    def algebra_base_ring(self):
        return self.base_ring()

    def free_source_module(self):
        return self.power_algebra_construction().source_module()

    def _power_algebra_homset_class(self):
        return PowerAlgebraHomset

    def algebra_generating_set(self):
        return self.free_source_module().module_generating_set()

    def algebra_generator(self, label):
        return self.from_component(1, self.free_source_module().module_generator(label))

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
        return self.from_component(0, piece.scalar_multiple(scalar, piece.module_generator(0)))

    def one(self):
        return self(self.base_ring().one())

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        result = self.zero()
        source_module = self.free_source_module()
        match self.flavor():
            case "alternating":
                product = source_module.exterior_power_product
            case "divided":
                product = source_module.divided_power_product
        for left_degree, left_component in left.homogeneous_components().items():
            for right_degree, right_component in right.homogeneous_components().items():
                target_degree = left_degree + right_degree
                if target_degree not in self.degree_index_set():
                    continue
                component = product(
                    left_degree,
                    left_component,
                    right_degree,
                    right_component,
                )
                result += self.from_component(target_degree, component)
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

    def _ring_morphism_defining_algebra_structure(self):
        return self.base_ring().Mor(self)(
            lambda scalar: self(scalar),
        )

    algebra_structure_morphism = _ring_morphism_defining_algebra_structure

    @cached_method
    def ring_center(self):
        if self.flavor() == "divided":
            return self
        if self.is_commutative():
            return self
        return self.predicate_subring(
            self.is_central,
            "z commutes with every element",
            OwnedRings().Commutative(),
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
            if degree_one_map.domain() is not source_module or degree_one_map.codomain() is not target_module:
                raise ValueError("the degree-one module map has the wrong endpoints")
            self._degree_one_map = degree_one_map
            return

        def target_component(label):
            image = degree_one_map[label] if isinstance(degree_one_map, dict) else degree_one_map(label)
            if isinstance(image, PowerAlgebraElement):
                if image.parent() is not self.codomain() or not image.is_homogeneous() or image.degree() != 1:
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
            result += self.codomain()._from_component(degree, mapped)
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
        if not isinstance(domain, PowerAlgebra) or not isinstance(codomain, PowerAlgebra):
            raise TypeError("a represented power-algebra Hom requires two power algebras")
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



@cached_function(key=lambda module, flavor: (id(module), flavor))
def _power_algebra_of(module, flavor):
    result = PowerAlgebra(module, flavor)
    return result


def _alternating_algebra_of(module):
    return _power_algebra_of(module, "alternating")


def _divided_power_algebra_of(module):
    return _power_algebra_of(module, "divided")


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
