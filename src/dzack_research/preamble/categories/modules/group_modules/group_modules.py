r"""Native-backed modules equipped with an action of a specified group."""

from sage.categories.category import Category
from sage.categories.map import Map
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.constructions import (
    CoequalizerOfFamily,
    EqualizerOfFamily,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.scalar_change import (
    ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.group.class_functions import (
    finite_group_class_function,
)
from dzack_research.preamble.categories.group.g_objects import GObjectHomset, GObjects
from dzack_research.preamble.categories.group.groups import (
    _engine_group,
    _owned_group,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.group_modules.isotypic import (
    _split_irreducible_characters,
    isotypic_component,
    isotypic_decomposition,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _initialize_module_hom_parent,
    _ModuleHomsetCommonMethods,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModules,
    LinearEndCategoryConstruction,
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    CoproductOfFamily,
    Sets,
)


class GroupModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GroupModuleHomset


class _CategoryOverRingAndActingGroup(OwnedCategory):
    r"""Shared Python parameter handling for categories indexed by ``(R,G)``."""

    @staticmethod
    def __classcall__(cls, base_ring, group):

        return Category.__classcall__(
            cls,
            _owned_ring(base_ring),
            _owned_group(group),
        )

    def __init__(self, base_ring, group) -> None:
        self._base_ring = base_ring
        self._group = group
        OwnedCategory.__init__(self)

    def base_ring(self):
        return self._base_ring

    def acting_group(self):
        return self._group


class GroupModules(CategoryPacketMethods, _CategoryOverRingAndActingGroup):
    r"""The category of ``R[G]``-modules for a specified ring and group."""

    def _repr_object_names(self):
        return f"{self.base_ring()}[{self.acting_group()}]-modules"

    def super_categories(self):
        return [
            GObjects(self.acting_group(), Modules(self.base_ring())),
            Modules(self.base_ring()),
        ]

    _HomCategory = GroupModuleHomCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    def is_semisimple(self) -> bool:
        r"""Return the conclusion of Maschke's theorem when it applies."""
        ring = self.base_ring()
        group = self.acting_group()
        if not ring.is_field():
            raise NotImplementedError(
                "this method applies Maschke's theorem over a field; it does not classify semisimplicity over a general coefficient ring"
            )
        if group.is_finite() is not True:
            raise NotImplementedError(
                "semisimplicity of the group algebra is not decided here for an infinite group"
            )
        characteristic = ring.characteristic()
        zero = characteristic.parent().zero()
        return characteristic == zero or group.order() % characteristic != zero

    class ParentMethods:
        def __init__(
            self,
            acting_group,
            unacted_module,
            source_action,
            action_is_trivial=False,
            **rest,
        ) -> None:
            self._preamble_unacted_module = unacted_module
            self._preamble_action_is_trivial = bool(action_is_trivial)

            def generator_images(group_element):
                forget_action = self.forget_action_morphism()
                equip_action = self.equip_action_morphism()
                return {
                    label: equip_action(
                        _apply_action(
                            source_action,
                            group_element,
                            forget_action(self.module_generator(label)),
                        )
                    )
                    for label in self.module_generating_set()
                }

            super().__init__(
                acting_group=acting_group,
                action=generator_images,
                underlying_category=Modules(unacted_module.base_ring()),
                **rest,
            )

        def group(self):
            return self._preamble_acting_group

        def acting_group(self):
            # ``GroupLattices`` enters through refinement and supplies
            # ``group()`` itself, so the acting group is read through it.
            return self.group()

        def is_trivial_action(self) -> bool:
            return self._preamble_action_is_trivial

        def unacted_module(self):
            r"""Return the module from which this chosen action was equipped."""
            return self._preamble_unacted_module

        @cached_method
        def forget_action_morphism(self):
            unacted = self.unacted_module()
            return module_homset(self, unacted)(
                {
                    label: unacted.module_generator(label)
                    for label in self.module_generating_set()
                }
            )

        @cached_method
        def equip_action_morphism(self):
            unacted = self.unacted_module()
            return module_homset(unacted, self)(
                {
                    label: self.module_generator(label)
                    for label in self.module_generating_set()
                }
            )

        def _Hom_(self, codomain, category=None):
            if codomain not in GroupModules(self.base_ring(), self.group()):
                raise TypeError("an R[G]-module morphism requires the same acting group")
            return group_module_homset(self, codomain)

        def module_invariants(self):
            r"""Return ``M^G`` as the equalizer subobject of the action and identity."""
            if self.is_trivial_action():
                return self.unacted_module()
            return self._represented_action_equalizer()

        def isotypic_characters(self):
            r"""Return the irreducible-character indices appropriate to the coefficient ring."""

            return _split_irreducible_characters(self)

        def isotypic_component(self, character):
            r"""Return the integral/base-ring isotypic component as a subobject."""

            return isotypic_component(self, character)

        def isotypic_decomposition(self):
            r"""Return the sum of isotypic components together with its inclusion in ``M``."""

            return isotypic_decomposition(self)

        def module_coinvariants(self):
            r"""Return ``M_G`` as the coequalizer of the action and identity."""
            if self.is_trivial_action():
                return self.unacted_module()
            return self._represented_action_coequalizer()

        def character(self):
            r"""Return the ordinary trace character in characteristic zero."""
            group = self.group()
            if group.is_finite() is not True:
                raise NotImplementedError("ordinary character tables here require a finite group")
            if self not in FinitelyGeneratedFreeGroupModules(self.base_ring(), group):
                raise NotImplementedError(
                    "the ordinary character is implemented here for a finite free group module; a finite presentation alone does not supply the finite-dimensional linear representation used by this construction"
                )
            if self.base_ring().characteristic() != 0:
                raise TypeError(
                    "ordinary characters are not obtained by treating modular traces as characteristic-zero class functions; use the native Brauer-character machinery when appropriate"
                )
            representatives = group.conjugacy_classes_representatives()
            traces = tuple(
                self.action_of(group_element).trace()
                for group_element in representatives
            )

            return finite_group_class_function(
                group,
                self.base_ring(),
                traces,
                representatives=representatives,
            )

        def brauer_character(self):
            r"""Return the Brauer character of a finite-dimensional modular representation."""
            group = self.group()
            if group.is_finite() is not True:
                raise NotImplementedError("Brauer characters here require a finite group")
            if self not in FinitelyGeneratedFreeGroupModules(self.base_ring(), group):
                raise NotImplementedError(
                    "the Brauer character is defined here for a finite free group module"
                )
            if self.base_ring().characteristic() == 0:
                raise TypeError("Brauer characters are the positive-characteristic representation invariant")
            if not self.base_ring().is_field():
                raise TypeError(
                    "Brauer characters require a finite-dimensional representation over a field of positive characteristic"
                )

            from sage.combinat.free_module import CombinatorialFreeModule

            indices = tuple(range(int(self.rank())))
            computation_module = CombinatorialFreeModule(
                _engine_ring(self.base_ring()),
                indices,
            )
            basis = computation_module.basis()

            def on_basis(group_element, index):
                action_matrix = self.action_of(group_element).matrix()
                return computation_module.sum(
                    _engine_element(
                        self.base_ring(),
                        action_matrix[image_index, index],
                    )
                    * basis[image_index]
                    for image_index in indices
                )

            # Sage maintains the Teichmuller-lift computation on a private
            # finite-basis representation.  Only the resulting exact values
            # cross back into the owned class-function object.

            engine_group = _engine_group(group)

            def engine_on_basis(engine_group_element, index):
                return on_basis(group._from_engine(engine_group_element), index)

            backend_character = engine_group.representation(
                computation_module,
                engine_on_basis,
                side="left",
            ).brauer_character()
            backend_values = tuple(backend_character)
            if not backend_values:
                raise ArithmeticError("a finite group has at least the identity p-regular class")
            value_ring = _own_ring(backend_values[0].parent())
            engine_value_ring = _engine_ring(value_ring)
            values = tuple(
                value_ring._from_engine_element(engine_value_ring(value))
                for value in backend_values
            )
            characteristic = int(self.base_ring().characteristic())
            representatives = tuple(
                representative
                for representative in group.conjugacy_classes_representatives()
                if int(representative.order()) % characteristic
            )
            if len(representatives) != len(values):
                raise ArithmeticError(
                    "the private Brauer-character engine returned the wrong number of p-regular class values"
                )
            return finite_group_class_function(
                group,
                value_ring,
                values,
                representatives=representatives,
            )

        def base_change(self, ring_map):
            r"""Transport this group module along ``R -> S`` functorially."""

            unacted = self.unacted_module()
            scalar_extension = ScalarExtensionFunctor(ring_map)
            changed_module = scalar_extension(unacted)
            if self.is_trivial_action():
                return trivial_group_action(changed_module, self.group())

            def changed_action(group_element, vector):
                underlying_action = (
                    self.forget_action_morphism()
                    * self.action_of(group_element)
                    * self.equip_action_morphism()
                )
                return scalar_extension(underlying_action)(vector)

            return GroupModule(changed_module, self.group(), changed_action)



class FinitelyGeneratedFreeGroupModules(_CategoryOverRingAndActingGroup):
    r"""Group modules whose underlying module is finite free with a chosen basis."""

    def _repr_object_names(self):
        return f"finitely generated free {self.base_ring()}[{self.acting_group()}]-modules"

    def super_categories(self):

        return [
            GroupModules(self.base_ring(), self.acting_group()),
            FinitelyPresentedGroupModules(self.base_ring(), self.acting_group()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]


class FinitelyPresentedGroupModules(_CategoryOverRingAndActingGroup):
    r"""Group modules with a chosen finite presentation of the underlying module."""

    def _repr_object_names(self):
        return f"finitely presented {self.base_ring()}[{self.acting_group()}]-modules"

    def super_categories(self):

        return [
            GroupModules(self.base_ring(), self.acting_group()),
            FinitelyPresentedModules(self.base_ring()),
        ]

    class ParentMethods:
        def _finite_action_endomorphism_family(self):
            r"""Return ``{id_M} union {rho(s) : s in S}`` for a chosen finite ``S``.

            Choosing a finite group generating set is a represented backend for
            the wide equalizer/coequalizer of the full action; callers retain
            the universal-construction spelling.
            """
            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError(
                    "the represented action equalizer/coequalizer requires a chosen finite group generating set"
                )
            generators = group.group_generators()
            indices = CoproductOfFamily(
                Sets.Δ[1],
                lambda side: Sets.Δ[0] if int(side) == 0 else generators,
            )
            identity = module_homset(self, self).identity()
            return finite_indexed_family(
                indices,
                lambda tagged: (
                    identity
                    if int(tagged.summand_index()) == 0
                    else self.action_of(tagged.summand_element())
                ),
                name=f"Identity and chosen action generators on {self}",
            )

        def _represented_action_equalizer(self):
            return EqualizerOfFamily(self._finite_action_endomorphism_family())

        def _represented_action_coequalizer(self):
            return CoequalizerOfFamily(self._finite_action_endomorphism_family())


def _apply_action(action, group_element, vector):
    if isinstance(action, Map):
        return action(group_element)(vector)
    return action(group_element, vector)


class GroupModuleMorphism(ModuleMorphism):
    r"""An ``R``-linear map commuting with the chosen ``G``-actions."""

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
        verify_equivariance=True,
    ) -> None:
        super().__init__(
            parent,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
        )
        if verify_equivariance and parent.is_equivariant(self) is not True:
            raise ValueError("the stated module map is not G-equivariant")

    def __mul__(self, other):
        if not isinstance(other, GroupModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        return group_module_homset(
            other.domain(), self.codomain()
        )._from_equivariant_images(
            lambda element: self(other(element)),
            elementwise=True,
            verify_linearity=False,
        )


class GroupModuleHomset(_ModuleHomsetCommonMethods, GObjectHomset):
    Element = GroupModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        assert domain.group() == codomain.group(), (
            "R[G]-module morphisms require the same acting group"
        )
        _initialize_module_hom_parent(self, hom_family, domain, codomain)


    def _from_equivariant_images(
        self,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
    ):
        r"""Construct a map whose equivariance follows from its construction.

        This protected path is for functorial images, identities, and
        compositions.  Arbitrary user-supplied maps still use the ordinary
        constructor and are checked on the selected group/module generators.
        """
        return self.element_class(
            self,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
            verify_equivariance=False,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        return self._from_equivariant_images(
            lambda element: element,
            elementwise=True,
            verify_linearity=False,
        )



    def _repr_(self):
        return f"Mor_{self.domain().group()}({self.domain()}, {self.codomain()})"


def group_module_homset(domain, codomain) -> GroupModuleHomset:
    ring = domain.base_ring()
    group = domain.group()
    if codomain.base_ring() is not ring or codomain.group() != group:
        raise ValueError("R[G]-module morphisms require one coefficient ring and acting group")
    return GroupModules(ring, group).Mor(domain, codomain)


def GroupModule(module, group_or_action, action=None, *, _action_is_trivial=False):
    r"""Equip a finitely presented module with a specified left group action.

    ``GroupModule(M, rho)`` accepts a morphism ``rho`` whose domain is the
    acting group and whose values act on ``M``.  ``GroupModule(M, G, action)``
    accepts the equivalent binary action ``action(g, m)``.  The resulting
    parent is a distinct structured module; the selected module labels are
    transported unchanged.
    """

    base_ring = module.base_ring()
    if module not in FinitelyPresentedModules(base_ring):
        raise NotImplementedError(
            "the active GroupModule constructor requires a represented finite presentation"
        )
    if action is None:
        action = group_or_action
        if not isinstance(action, Map):
            raise TypeError(
                "with two arguments, GroupModule expects an action morphism whose domain is the acting group"
            )
        group = _owned_group(action.domain())
    else:
        group = _owned_group(group_or_action)

    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise NotImplementedError(
            "the active native GroupModule constructor currently materializes a finite framing"
        )

    is_free = module in FinitelyGeneratedFreeModules(base_ring)
    if not is_free and module not in ModulesWithChosenFinitePresentation(base_ring):
        raise TypeError(
            "a nonfree group module requires a chosen finite presentation"
        )

    categories = [
        GroupModules(base_ring, group),
        FinitelyPresentedGroupModules(base_ring, group),
    ]
    if is_free:
        categories.append(FinitelyGeneratedFreeGroupModules(base_ring, group))
    construction_data = {
        "acting_group": group,
        "unacted_module": module,
        "source_action": action,
        "action_is_trivial": _action_is_trivial,
    }
    if is_free:
        return FreshFreeModuleOn(
            base_ring,
            labels,
            _extra_categories=tuple(categories),
            _extra_construction_data=construction_data,
        )
    return FinitelyPresentedModule(
        module.presentation(),
        _extra_categories=tuple(categories),
        _extra_construction_data=construction_data,
    )


def trivial_group_action(module, group):
    r"""Equip ``module`` with the trivial action of ``group``."""
    return GroupModule(
        module,
        group,
        lambda _group_element, vector: vector,
        _action_is_trivial=True,
    )


__all__ = [
    "FinitelyGeneratedFreeGroupModules",
    "FinitelyPresentedGroupModules",
    "GroupModule",
    "GroupModuleHomset",
    "GroupModuleMorphism",
    "GroupModules",
    "group_module_homset",
    "trivial_group_action",
]
