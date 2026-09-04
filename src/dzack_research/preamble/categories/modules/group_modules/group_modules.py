r"""Native-backed modules equipped with an action of a specified group."""

from sage.categories.category import Category
from sage.categories.map import Map
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _initialize_module_hom_parent,
    ModuleHomset,
    _ModuleHomsetCommonMethods,
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    LinearEndCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.refine import refine


class GroupModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GroupModuleHomset


class _CategoryOverRingAndActingGroup(Category):
    r"""Shared Python parameter handling for categories indexed by ``(R,G)``."""

    @staticmethod
    def __classcall__(cls, base_ring, group):
        from dzack_research.preamble.categories.group.groups import _owned_group

        return Category.__classcall__(
            cls,
            _owned_ring(base_ring),
            _owned_group(group),
        )

    def __init__(self, base_ring, group) -> None:
        self._base_ring = base_ring
        self._group = group
        Category.__init__(self)

    def base_ring(self):
        return self._base_ring

    def acting_group(self):
        return self._group


class GroupModules(CategoryPacketMethods, _CategoryOverRingAndActingGroup):
    r"""The category of ``R[G]``-modules for a specified ring and group."""

    def _repr_object_names(self):
        return f"{self.base_ring()}[{self.acting_group()}]-modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

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
        def group(self):
            return self._preamble_acting_group

        def is_trivial_action(self) -> bool:
            return bool(self.__dict__.get("_preamble_action_is_trivial", False))

        def unacted_module(self):
            r"""Return the module from which this chosen action was equipped."""
            return self._preamble_unacted_module

        def forget_action_morphism(self):
            return self._preamble_forget_action_morphism

        def equip_action_morphism(self):
            return self._preamble_equip_action_morphism

        def action(self):
            r"""Return the chosen action datum used to construct this group module."""
            return self._preamble_action

        def act(self, group_element, vector):
            r"""Return ``group_element * vector`` in this group module."""
            if group_element not in self.group():
                raise TypeError(f"{group_element} is not an element of {self.group()}")
            if vector.parent() is not self:
                raise TypeError(f"the action is on elements of {self}")
            return _apply_action(self.action(), group_element, vector)

        def _Hom_(self, codomain, category=None):
            if codomain not in GroupModules(self.base_ring(), self.group()):
                raise TypeError("an R[G]-module morphism requires the same acting group")
            return group_module_homset(self, codomain)

        def action_of(self, group_element):
            r"""Return the linear automorphism induced by ``group_element``."""
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            return module_homset(self, self)(
                {
                    label: self.act(group_element, self.module_generator(label))
                    for label in self.module_generating_set()
                }
            )

        def is_invariant(self, vector) -> bool:
            from dzack_research.preamble.categories.group.groups import _owned_group

            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError(
                    "deciding invariance here requires a chosen finite group generating set"
                )
            return all(
                self.act(group_generator, vector) == vector
                for group_generator in group.group_generators()
            )

        def module_invariants(self):
            r"""Return ``M^G`` as the equalizer subobject of the action and identity."""
            if self.is_trivial_action():
                return self.unacted_module()
            from dzack_research.preamble.categories.group.groups import _owned_group
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError(
                    "constructing invariants here requires a chosen finite group generating set"
                )
            fixed_subobjects = []
            for group_generator in group.group_generators():
                difference = module_homset(self, self)(
                    {
                        label: self.act(group_generator, self.module_generator(label))
                        - self.module_generator(label)
                        for label in self.module_generating_set()
                    }
                )
                fixed_subobjects.append(difference.kernel())
            if not fixed_subobjects:
                return self.subobject_on(self.module_generators())
            invariants = fixed_subobjects[0]
            for fixed in fixed_subobjects[1:]:
                invariants = invariants.intersection(fixed)
            return invariants

        def isotypic_characters(self):
            r"""Return the irreducible-character indices appropriate to the coefficient ring."""
            from dzack_research.preamble.categories.modules.group_modules.isotypic import (
                _split_irreducible_characters,
            )

            return _split_irreducible_characters(self)

        def isotypic_component(self, character):
            r"""Return the integral/base-ring isotypic component as a subobject."""
            from dzack_research.preamble.categories.modules.group_modules.isotypic import (
                isotypic_component,
            )

            return isotypic_component(self, character)

        def isotypic_decomposition(self):
            r"""Return the sum of isotypic components together with its inclusion in ``M``."""
            from dzack_research.preamble.categories.modules.group_modules.isotypic import (
                isotypic_decomposition,
            )

            return isotypic_decomposition(self)

        def module_coinvariants(self):
            r"""Return ``M_G = M / <g m - m>`` with the current framing retained."""
            if self.is_trivial_action():
                return self.unacted_module()
            from dzack_research.preamble.categories.group.groups import _owned_group
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                BasedFreeModule,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )
            from dzack_research.preamble.categories.sets.set_categories import Sets
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image

            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError(
                    "constructing coinvariants here requires a chosen finite group generating set"
                )
            group_generators = group.group_generators()
            module_labels = self.module_generating_set()
            group_count = int(group_generators.cardinality())
            module_count = int(module_labels.cardinality())
            positions = Sets.Δ[group_count * module_count - 1]
            relation_labels = finite_ordered_image(
                positions,
                lambda position: (
                    group_generators.unrank(int(position) // module_count),
                    module_labels.unrank(int(position) % module_count),
                ),
                name="Coinvariant relation indices",
            )
            relation_module = BasedFreeModule(self.base_ring(), relation_labels)
            images = {
                relation_label: self.act(
                    relation_label[0], self.module_generator(relation_label[1])
                )
                - self.module_generator(relation_label[1])
                for relation_label in relation_labels
            }
            return module_homset(relation_module, self)(images).cokernel()

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
            from dzack_research.preamble.categories.group.class_functions import (
                finite_group_class_function,
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
            from dzack_research.preamble.categories.group.groups import _engine_group
            from dzack_research.preamble.categories.group.class_functions import (
                finite_group_class_function,
            )
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

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
            from dzack_research.preamble.categories.functors.scalar_change import (
                ScalarExtensionFunctor,
            )

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
        from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules

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
        from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules

        return [
            GroupModules(self.base_ring(), self.acting_group()),
            FinitelyPresentedModules(self.base_ring()),
        ]


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
        if verify_equivariance:
            group = self.domain().group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError(
                    "checking equivariance requires a chosen finite group generating set"
                )
            for group_generator in group.group_generators():
                for label in self.domain().module_generating_set():
                    source = self.domain().module_generator(label)
                    if self(self.domain().act(group_generator, source)) != self.codomain().act(
                        group_generator, self(source)
                    ):
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


class GroupModuleHomset(_ModuleHomsetCommonMethods, CategoricalHomset):
    Element = GroupModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.group() != codomain.group():
            raise ValueError("R[G]-module morphisms require the same acting group")
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


def GroupModule(module, group_or_action, action=None):
    r"""Equip a finitely presented module with a specified left group action.

    ``GroupModule(M, rho)`` accepts a morphism ``rho`` whose domain is the
    acting group and whose values act on ``M``.  ``GroupModule(M, G, action)``
    accepts the equivalent binary action ``action(g, m)``.  The resulting
    parent is a distinct structured module; the selected module labels are
    transported unchanged.
    """
    from dzack_research.preamble.categories.modules.pure.modules import (
        FinitelyGeneratedFreeModules,
    )
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreshFreeModuleOn,
    )
    from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
    from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.group.groups import _owned_group

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
    from dzack_research.preamble.categories.sets.cardinals import cardinal
    if not cardinal(labels.cardinality()).is_finite():
        raise NotImplementedError(
            "the active native GroupModule constructor currently materializes a finite framing"
        )

    is_free = module in FinitelyGeneratedFreeModules(base_ring)
    if is_free:
        represented_module = FreshFreeModuleOn(base_ring, labels)
    elif module in ModulesWithChosenFinitePresentation(base_ring):
        represented_module = FinitelyPresentedModule(module.presentation())
    else:
        raise TypeError(
            "a nonfree group module requires a chosen finite presentation"
        )

    forget_action = module_homset(represented_module, module)(
        {label: module.module_generator(label) for label in labels}
    )
    equip_action = module_homset(module, represented_module)(
        {label: represented_module.module_generator(label) for label in labels}
    )

    def represented_action(group_element, vector):
        if vector.parent() is not represented_module:
            raise TypeError(f"the action must be applied to elements of {represented_module}")
        source_vector = forget_action(vector)
        source_image = _apply_action(action, group_element, source_vector)
        return equip_action(source_image)

    represented_module._preamble_acting_group = group
    represented_module._preamble_action = represented_action
    represented_module._preamble_unacted_module = module
    represented_module._preamble_forget_action_morphism = forget_action
    represented_module._preamble_equip_action_morphism = equip_action
    categories = [
        GroupModules(base_ring, group),
        FinitelyPresentedGroupModules(base_ring, group),
    ]
    if is_free:
        categories.append(FinitelyGeneratedFreeGroupModules(base_ring, group))
    return refine(represented_module, categories)


def trivial_group_action(module, group):
    r"""Equip ``module`` with the trivial action of ``group``."""
    acted = GroupModule(module, group, lambda _group_element, vector: vector)
    acted._preamble_action_is_trivial = True
    return acted


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
