r"""Modules over varying commutative scalar rings and semilinear arrows.

For a commutative-ring morphism ``sigma : R -> S``, extension of scalars
``S tensor_R -`` is left adjoint to restriction of scalars.  Thus a
``sigma``-semilinear map ``M -> N`` is represented here by its actual additive
map, equivalently the ``R``-linear map ``M -> Res_sigma(N)``.  Its ``S``-linear
transpose ``S tensor_R M -> N`` is derived from the scalar-extension
adjunction owned by
:class:`~dzack_research.preamble.categories.modules.pure.modules.Modules`.

This is the Grothendieck construction of the pseudofunctor
``R |-> Modules(R)`` on commutative rings: an arrow over ``R -> S`` is a map
``M -> Res_sigma(N)``, with the equivalent scalar-extended map available by
adjunction.  See the Stacks Project,
Tag 05DQ, for the scalar-extension/restriction adjunction, and Dai Tamaki,
*The Grothendieck Construction and Gradings for Enriched Categories*,
arXiv:0907.0061, for the Grothendieck construction.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import FramedModules, Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    CommutativeRings,
)


class _DerivedRestrictedSemilinearMorphism(ModuleMorphism):
    r"""A restricted-target linear map whose linearity follows from its construction."""

    def __init__(self, parent, evaluator, decision) -> None:
        self._semilinear_linearity_decision = decision
        super().__init__(parent, evaluator, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._semilinear_linearity_decision


class SemilinearModuleMorphism(Morphism):
    r"""A module arrow over a morphism of commutative scalar rings.

    If ``sigma : R -> S``, the defining map is the equivalent ``R``-linear map
    ``M -> Res_sigma(N)``.  The ``S``-linear transpose
    ``S tensor_R M -> N`` is derived from the scalar-extension/restriction
    adjunction when that represented scalar extension is available.
    """

    def __init__(self, parent, scalar_map, restricted_morphism) -> None:
        Morphism.__init__(self, parent)
        if scalar_map.domain() is not self.domain().base_ring():
            raise ValueError("a semilinear scalar map starts at the source module base ring")
        if scalar_map.codomain() is not self.codomain().base_ring():
            raise ValueError("a semilinear scalar map ends at the target module base ring")
        restricted = parent.restricted_codomain(scalar_map)
        linear_hom = Modules(self.domain().base_ring()).Mor(self.domain(), restricted)
        restricted_morphism = linear_hom(restricted_morphism)
        self._scalar_map = scalar_map
        self._restricted_codomain = restricted
        self._restricted_morphism = restricted_morphism

    def scalar_map(self):
        return self._scalar_map

    def source(self):
        return self.domain()

    def target(self):
        return self.codomain()

    def restricted_codomain(self):
        r"""Return ``Res_sigma(N)``, the target read in the source fibre."""
        return self._restricted_codomain

    def restricted_morphism(self):
        r"""Return the defining ``R``-linear map ``M -> Res_sigma(N)``."""
        return self._restricted_morphism

    @cached_method
    def additive_map(self):
        r"""Return the underlying additive map ``M -> N`` of this semilinear arrow."""
        additive = AdditiveGroups().AdditiveCommutative().HomCategory().Of(
            self.domain(),
            self.codomain(),
        )
        return additive.elementwise(
            lambda element: self.codomain()(
                self.restricted_morphism()(element).underlying_element()
            )
        )

    @cached_method
    def linearization(self):
        r"""Return the adjoint transpose ``S tensor_R M -> N`` when represented."""
        adjunction = Modules(self.domain().base_ring()).base_change_adjunction(
            self.scalar_map()
        )
        return adjunction.hom_set_isomorphism_inverse(
            self.restricted_morphism(),
            self.codomain(),
        )

    def extended_source(self):
        return self.parent().extended_domain(self.scalar_map())

    def _call_(self, element):
        return self.additive_map()(element)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, SemilinearModuleMorphism) or other.parent() is not self.parent():
            return False
        scalar_equal = self.scalar_map() == other.scalar_map()
        if scalar_equal is False:
            return False
        if scalar_equal is not True:
            return Unknown
        source = self.domain()
        if source in FramedModules(source.base_ring()):
            return all(
                self(source.module_generator(label))
                == other(source.module_generator(label))
                for label in source.module_generating_set()
            )
        return self.additive_map() == other.additive_map()

    def __ne__(self, other):
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __mul__(self, other):
        match other:
            case SemilinearModuleMorphism() if other.codomain() is self.domain():
                pass
            case _:
                return NotImplemented
        source = other.domain()
        scalar_map = self.scalar_map() * other.scalar_map()
        hom = ModulesOverCommutativeRings().Mor(source, self.codomain())
        restricted = hom.restricted_codomain(scalar_map)
        linear_hom = Modules(source.base_ring()).Mor(source, restricted)
        decision = (
            True
            if self.restricted_morphism().linearity_decision() is True
            and other.restricted_morphism().linearity_decision() is True
            else Unknown
        )
        composite = _DerivedRestrictedSemilinearMorphism(
            linear_hom,
            lambda element: restricted.wrap(self(other(element))),
            decision,
        )
        return hom(scalar_map, composite)

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
        morphism = Modules(source.base_ring()).Mor(source, target)(morphism)
        hom = ModulesOverCommutativeRings().Mor(source, target)
        scalar_map = source.base_ring().Mor(source.base_ring()).identity()
        restricted = hom.restricted_codomain(scalar_map)
        compatible = _DerivedRestrictedSemilinearMorphism(
            Modules(source.base_ring()).Mor(source, restricted),
            lambda element: restricted.wrap(morphism(element)),
            morphism.linearity_decision(),
        )
        return hom(scalar_map, compatible)


class SemilinearModuleHomset(CategoricalHomset):
    r"""All semilinear arrows between two modules over commutative rings."""

    Element = SemilinearModuleMorphism

    def _validate_scalar_map(self, scalar_map) -> None:
        source_ring = self.domain().base_ring()
        target_ring = self.codomain().base_ring()
        if scalar_map not in CommutativeRings().Mor(source_ring, target_ring):
            raise TypeError("a semilinear module arrow lies over a morphism of commutative rings")

    @cached_method(key=lambda self, scalar_map: id(scalar_map))
    def base_change_adjunction(self, scalar_map):
        r"""Return the one scalar-extension/restriction adjunction for ``scalar_map``."""
        self._validate_scalar_map(scalar_map)
        return Modules(self.domain().base_ring()).base_change_adjunction(scalar_map)

    def extended_domain(self, scalar_map):
        return self.base_change_adjunction(scalar_map).left_adjoint()(self.domain())

    def restricted_codomain(self, scalar_map):
        r"""Return ``Res_sigma(N)`` in the source module fibre."""
        return self.base_change_adjunction(scalar_map).right_adjoint()(self.codomain())

    def compatible_hom(self, scalar_map):
        r"""Return ``Hom_R(M, Res_sigma(N))`` classifying these semilinear arrows."""
        restricted = self.restricted_codomain(scalar_map)
        return Modules(self.domain().base_ring()).Mor(self.domain(), restricted)

    def _element_constructor_(self, scalar_map, compatible_map=None):
        if compatible_map is None and isinstance(scalar_map, SemilinearModuleMorphism):
            if scalar_map.parent() is self:
                return scalar_map
            compatible_map = scalar_map.restricted_morphism()
            scalar_map = scalar_map.scalar_map()
        self._validate_scalar_map(scalar_map)
        restricted = self.restricted_codomain(scalar_map)
        compatible_hom = self.compatible_hom(scalar_map)
        match compatible_map:
            case Morphism() if (
                compatible_map.domain() is self.domain()
                and compatible_map.codomain() is self.codomain()
            ):
                additive = AdditiveGroups().AdditiveCommutative().HomCategory().Of(
                    self.domain(), self.codomain()
                )(compatible_map)
                if isinstance(compatible_map, ModuleMorphism):
                    compatible_map = _DerivedRestrictedSemilinearMorphism(
                        compatible_hom,
                        lambda element: restricted.wrap(additive(element)),
                        compatible_map.linearity_decision(),
                    )
                else:
                    compatible_map = compatible_hom.elementwise(
                        lambda element: restricted.wrap(additive(element))
                    )
            case _:
                compatible_map = compatible_hom(compatible_map)
        return self.element_class(self, scalar_map, compatible_map)

    def _from_linearization(self, scalar_map, linearization):
        r"""Construct from the equivalent target-fibre map ``S tensor_R M -> N``."""
        self._validate_scalar_map(scalar_map)
        extended = self.extended_domain(scalar_map)
        linear_hom = Modules(self.codomain().base_ring()).Mor(
            extended,
            self.codomain(),
        )
        linearization = linear_hom(linearization)
        adjunction = self.base_change_adjunction(scalar_map)
        compatible = adjunction.hom_set_isomorphism_forward(
            linearization,
            self.domain(),
        )
        return self.element_class(self, scalar_map, compatible)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism Hom")
        module = self.domain()
        ring = module.base_ring()
        scalar_map = ring.Mor(ring).identity()
        restricted = self.restricted_codomain(scalar_map)
        compatible = _DerivedRestrictedSemilinearMorphism(
            Modules(ring).Mor(module, restricted),
            lambda element: restricted.wrap(module(element)),
            True,
        )
        return self(scalar_map, compatible)


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
    ``sigma : R -> S`` and retains the compatible additive map as the
    ``R``-linear arrow ``M -> Res_sigma(N)``.  Scalar extension and restriction
    give the cocartesian/cartesian transports of the represented fibration.
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

    def fiber(self, ring):
        r"""Return the fixed-base fibre ``Modules(R)`` over a commutative ring ``R``."""
        if ring not in CommutativeRings():
            raise TypeError("the module fibration is based on commutative rings")
        return Modules(ring)

    def cocartesian_transport(self, ring_map):
        r"""Return scalar extension ``S tensor_R -`` along ``R -> S``."""
        source, target = ring_map.domain(), ring_map.codomain()
        if ring_map not in CommutativeRings().Mor(source, target):
            raise TypeError("cocartesian module transport lies over a commutative-ring morphism")
        return self.base_change_adjunction(ring_map).left_adjoint()

    def cartesian_transport(self, ring_map):
        r"""Return restriction of scalars ``Res_f : Modules(S) -> Modules(R)``."""
        source, target = ring_map.domain(), ring_map.codomain()
        if ring_map not in CommutativeRings().Mor(source, target):
            raise TypeError("cartesian module transport lies over a commutative-ring morphism")
        return self.base_change_adjunction(ring_map).right_adjoint()

    def base_change_adjunction(self, ring_map):
        r"""Return the existing ``S tensor_R - dashv Res_f`` transport adjunction."""
        source, target = ring_map.domain(), ring_map.codomain()
        if ring_map not in CommutativeRings().Mor(source, target):
            raise TypeError("module base change lies over a commutative-ring morphism")
        return self.fiber(source).base_change_adjunction(ring_map)

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
