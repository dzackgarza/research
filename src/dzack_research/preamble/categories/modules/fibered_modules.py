r"""Modules over varying commutative scalar rings and semilinear arrows.

For a commutative-ring morphism ``sigma : R -> S``, extension of scalars
``S tensor_R -`` is left adjoint to restriction of scalars.  Thus a
``sigma``-semilinear map ``M -> N`` is represented here by the equivalent
``S``-linear map ``S tensor_R M -> N``.  The scalar-extension adjunction is
the one owned by :class:`~dzack_research.preamble.categories.modules.pure.modules.Modules`.

This is the Grothendieck construction of the pseudofunctor
``R |-> Modules(R)`` on commutative rings: an arrow over ``R -> S`` is a map
from the scalar-extended source in the ``S``-fiber.  See the Stacks Project,
Tag 05DQ, for the scalar-extension/restriction adjunction, and Dai Tamaki,
*The Grothendieck Construction and Gradings for Enriched Categories*,
arXiv:0907.0061, for the Grothendieck construction.
"""

from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.base_change import _base_change_element
from dzack_research.preamble.categories.modules.pure.modules import FramedModules, Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    CommutativeRings,
)


def _scalar_extension_associator(source, direct, iterated):
    r"""Represent ``T tensor_R M ~= T tensor_S (S tensor_R M)``.

    Scalar extension is a pseudofunctor.  Its direct and iterated values are
    canonically isomorphic by associativity of tensor product.  The currently
    materialized framed scalar extensions retain the source framing, so this
    comparison and its inverse are the identity on those labels.
    """

    source_ring = source.base_ring()
    target_ring = direct.base_ring()
    assert source in FramedModules(source_ring), (
        "represented scalar-extension coherence currently requires a selected source framing"
    )
    assert direct in FramedModules(target_ring) and iterated in FramedModules(target_ring), (
        "represented scalar-extension coherence must preserve the selected framing"
    )
    modules = Modules(target_ring)
    forward = modules.Mor(direct, iterated)(
        lambda label: iterated.module_generator(label)
    )
    inverse = modules.Mor(iterated, direct)(
        lambda label: direct.module_generator(label)
    )
    return modules.Core().Mor(direct, iterated)(forward, inverse)


class SemilinearModuleMorphism(Morphism):
    r"""A module arrow over a morphism of commutative scalar rings.

    If ``sigma : R -> S``, the stored linearization is the ``S``-linear map
    ``S tensor_R M -> N`` corresponding to the semilinear arrow ``M -> N``.
    """

    def __init__(self, parent, scalar_map, linearization) -> None:
        Morphism.__init__(self, parent)
        if scalar_map.domain() is not self.domain().base_ring():
            raise ValueError("a semilinear scalar map starts at the source module base ring")
        if scalar_map.codomain() is not self.codomain().base_ring():
            raise ValueError("a semilinear scalar map ends at the target module base ring")
        extended = parent.extended_domain(scalar_map)
        if linearization.domain() is not extended:
            raise ValueError("the linearization must start at the scalar-extended source")
        if linearization.codomain() is not self.codomain():
            raise ValueError("the linearization must end at the target module")
        self._scalar_map = scalar_map
        self._linearization = linearization

    def scalar_map(self):
        return self._scalar_map

    def source(self):
        return self.domain()

    def target(self):
        return self.codomain()

    def linearization(self):
        return self._linearization

    def extended_source(self):
        return self.linearization().domain()

    def _call_(self, element):
        match self.scalar_map():
            case ring_map if ring_map.is_identity():
                return self.linearization()(self.domain()(element))
            case _:
                source = self.domain()
                assert source in FramedModules(source.base_ring()), (
                    "represented evaluation of a cross-fiber module arrow currently requires a selected framing"
                )
                return self.linearization()(
                    _base_change_element(
                        source,
                        self.extended_source(),
                        self.scalar_map(),
                        element,
                    )
                )

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, SemilinearModuleMorphism) or other.parent() is not self.parent():
            return False
        if self.scalar_map() != other.scalar_map():
            return False
        source = self.domain()
        if source in FramedModules(source.base_ring()):
            return all(
                self(source.module_generator(label))
                == other(source.module_generator(label))
                for label in source.module_generating_set()
            )
        return self.linearization() == other.linearization()

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        match other:
            case SemilinearModuleMorphism() if other.codomain() is self.domain():
                pass
            case _:
                return NotImplemented
        source = other.domain()
        match self.scalar_map(), other.scalar_map():
            case left, right if left.is_identity():
                scalar_map = right
            case left, right if right.is_identity():
                scalar_map = left
            case left, right:
                scalar_map = left * right
        hom = ModulesOverCommutativeRings().Mor(source, self.codomain())
        direct_extension = hom.extended_domain(scalar_map)

        second_extension = Modules(self.domain().base_ring()).scalar_extension(
            self.scalar_map()
        )
        extended_first_linearization = second_extension(other.linearization())
        iterated_extension = extended_first_linearization.domain()
        if extended_first_linearization.codomain() is not self.extended_source():
            raise ValueError("scalar extension selected an incompatible middle module")
        iterated_linearization = self.linearization() * extended_first_linearization
        match direct_extension is iterated_extension:
            case True:
                linearization = iterated_linearization
            case False:
                reassociation = _scalar_extension_associator(
                    source,
                    direct_extension,
                    iterated_extension,
                )
                linearization = iterated_linearization * reassociation.forward()
        return hom(scalar_map, linearization)

    @classmethod
    def identity(cls, module):
        r"""The identity of ``module`` in the varying-ring module category."""
        return ModulesOverCommutativeRings().Mor(module, module).identity()

    @classmethod
    def from_linear(cls, morphism):
        r"""Regard a fixed-fiber linear map as semilinear over the identity ring map."""
        source = morphism.domain()
        target = morphism.codomain()
        if source.base_ring() is not target.base_ring():
            raise ValueError("a linear map has one scalar ring")
        hom = ModulesOverCommutativeRings().Mor(source, target)
        scalar_map = source.base_ring().Mor(source.base_ring()).identity()
        return hom(scalar_map, morphism)


class SemilinearModuleHomset(CategoricalHomset):
    r"""All semilinear arrows between two modules over commutative rings."""

    Element = SemilinearModuleMorphism

    def _validate_scalar_map(self, scalar_map) -> None:
        source_ring = self.domain().base_ring()
        target_ring = self.codomain().base_ring()
        if scalar_map not in CommutativeRings().Mor(source_ring, target_ring):
            raise TypeError("a semilinear module arrow lies over a morphism of commutative rings")

    def extended_domain(self, scalar_map):
        self._validate_scalar_map(scalar_map)
        return Modules(self.domain().base_ring()).scalar_extension(scalar_map)(self.domain())

    def _element_constructor_(self, scalar_map, linearization=None):
        if linearization is None and isinstance(scalar_map, SemilinearModuleMorphism):
            if scalar_map.parent() is self:
                return scalar_map
            linearization = scalar_map.linearization()
            scalar_map = scalar_map.scalar_map()
        extended = self.extended_domain(scalar_map)
        if not isinstance(linearization, Morphism):
            linearization = Modules(self.codomain().base_ring()).Mor(
                extended,
                self.codomain(),
            )(linearization)
        return self.element_class(self, scalar_map, linearization)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism Hom")
        module = self.domain()
        ring = module.base_ring()
        scalar_map = ring.Mor(ring).identity()
        extended = self.extended_domain(scalar_map)
        if extended is not module:
            raise ValueError("identity scalar extension must be normalized to the original module")
        linearization = Modules(ring).Mor(module, module).identity()
        return self(scalar_map, linearization)


class SemilinearModuleHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom family of the Grothendieck category of modules over rings."""

    def fixed_category_class(self):
        return SemilinearModuleHomset


class ModuleBaseRingProjection(Functor):
    r"""The projection ``(R,M) |-> R`` from modules over varying rings."""

    def __init__(self) -> None:
        super().__init__(ModulesOverCommutativeRings(), CommutativeRings())

    def _apply_object(self, module):
        return module.base_ring()

    def _apply_morphism(self, morphism):
        return morphism.scalar_map()

    def _repr_(self):
        return "Base-ring projection from modules over commutative rings"


class ModulesOverCommutativeRings(OwnedCategory):
    r"""The Grothendieck category of ``R |-> Modules(R)`` on commutative rings.

    Objects are modules ``M`` together with their commutative scalar ring
    ``R = M.base_ring()``.  An arrow ``M/R -> N/S`` lies over a ring map
    ``sigma : R -> S`` and is an ``S``-linear map ``S tensor_R M -> N``.
    """

    _HomCategory = SemilinearModuleHomCategoryConstruction

    def an_object(self):
        return CommutativeRings().an_object().free_module(1)

    def super_categories(self):
        return [AdditiveGroups().AdditiveCommutative()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("semilinear Hom endpoints must be modules over commutative rings")
        return self.HomCategory().Of(domain, codomain)

    def projection(self):
        return ModuleBaseRingProjection()

    @classmethod
    def _repr_object_names(cls):
        return "modules over commutative rings"


__all__ = [
    "ModuleBaseRingProjection",
    "ModulesOverCommutativeRings",
    "SemilinearModuleHomset",
    "SemilinearModuleMorphism",
]
